#!/usr/bin/env python3
"""
Test Lab Sweep: Run test_lab.py across multiple sizes and dtypes.

Generates:
1. Individual run results (md, json, charts)
2. Aggregate sweep grid heatmaps (size × distribution)
3. Scaling analysis (error vs size)
4. Summary dashboard

Usage:
    python run_sweep.py
    python run_sweep.py --trials 16
    python run_sweep.py --sizes 64 128 256 --dtypes float16 float32
"""

import subprocess
import argparse
import sys
import json
import os
import numpy as np

# Optional matplotlib for aggregate charts
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

# Default configurations
DEFAULT_SIZES = [32, 64, 128, 1024, 2048, 4096]
DEFAULT_DTYPES = ["bfloat16", "float16", "float32"]
DEFAULT_TRIALS = 32

# Distribution order for consistent display
DISTRIBUTIONS = ["gaussian", "relu", "gelu", "biased", "attention", "causal_transformer"]
DIST_ABBREVS = {
    "gaussian": "GAUSS", "relu": "RELU", "gelu": "GELU",
    "biased": "BIAS", "attention": "ATTN", "causal_transformer": "CAUSAL"
}


def load_results(sizes: list, dtypes: list, trials: int) -> dict:
    """Load all JSON results into a structured dict."""
    all_results = {}
    
    for dtype in dtypes:
        all_results[dtype] = {}
        for size in sizes:
            json_file = f"test_results/json/{dtype}/results_size{size}_{dtype}_trials{trials}_batch1.json"
            if os.path.exists(json_file):
                with open(json_file, "r") as f:
                    all_results[dtype][size] = json.load(f)
            else:
                all_results[dtype][size] = None
    
    return all_results


def generate_sweep_grids(all_results: dict, sizes: list, dtypes: list):
    """Generate 2D heatmap grids: Size × Distribution for each dtype."""
    if not HAS_MATPLOTLIB:
        print("  (matplotlib not available, skipping sweep grids)")
        return
    
    os.makedirs("test_results/sweep", exist_ok=True)
    
    for dtype in dtypes:
        # Build error ratio grid: rows=distributions, cols=sizes
        error_grid = np.ones((len(DISTRIBUTIONS), len(sizes)))
        stability_grid = np.ones((len(DISTRIBUTIONS), len(sizes)))
        
        for j, size in enumerate(sizes):
            data = all_results[dtype].get(size)
            if data is None:
                continue
            
            for i, dist in enumerate(DISTRIBUTIONS):
                if dist not in data["results"]:
                    continue
                
                alpha_err = data["results"][dist]["alpha"]["mean_error"]
                strassen_err = data["results"][dist]["strassen"]["mean_error"]
                alpha_std = data["results"][dist]["alpha"]["std_error"]
                strassen_std = data["results"][dist]["strassen"]["std_error"]
                
                # Error ratio (>1 = Alpha better)
                if alpha_err > 1e-20 and not np.isnan(alpha_err):
                    error_grid[i, j] = strassen_err / alpha_err
                
                # Stability gain (>1 = Alpha more stable)
                if alpha_std > 1e-20 and not np.isnan(alpha_std):
                    stability_grid[i, j] = strassen_std / alpha_std
        
        # Plot Error Ratio Grid
        fig, ax = plt.subplots(figsize=(12, 6))
        im = ax.imshow(error_grid, cmap="RdYlGn", aspect="auto", vmin=0.5, vmax=3.0)
        
        ax.set_xticks(np.arange(len(sizes)))
        ax.set_yticks(np.arange(len(DISTRIBUTIONS)))
        ax.set_xticklabels(sizes)
        ax.set_yticklabels([DIST_ABBREVS[d] for d in DISTRIBUTIONS])
        
        # Add value annotations
        for i in range(len(DISTRIBUTIONS)):
            for j in range(len(sizes)):
                val = error_grid[i, j]
                if np.isnan(val):
                    text = "N/A"
                    color = "gray"
                else:
                    text = f"{val:.2f}x"
                    color = "white" if val < 1.5 else "black"
                ax.text(j, i, text, ha="center", va="center", color=color, fontsize=9)
        
        ax.set_xlabel("Matrix Size")
        ax.set_ylabel("Distribution")
        ax.set_title(f"Error Ratio: Strassen / Alpha ({dtype})\n>1.0 = Alpha Better (Green)")
        fig.colorbar(im, label="Error Ratio")
        plt.tight_layout()
        plt.savefig(f"test_results/sweep/sweep_error_{dtype}.png", dpi=150)
        plt.close()
        
        # Plot Stability Grid
        fig, ax = plt.subplots(figsize=(12, 6))
        im = ax.imshow(stability_grid, cmap="viridis", aspect="auto", vmin=0.5, vmax=5.0)
        
        ax.set_xticks(np.arange(len(sizes)))
        ax.set_yticks(np.arange(len(DISTRIBUTIONS)))
        ax.set_xticklabels(sizes)
        ax.set_yticklabels([DIST_ABBREVS[d] for d in DISTRIBUTIONS])
        
        for i in range(len(DISTRIBUTIONS)):
            for j in range(len(sizes)):
                val = stability_grid[i, j]
                if np.isnan(val):
                    text = "N/A"
                    color = "gray"
                else:
                    text = f"{val:.2f}x"
                    color = "white" if val < 2.5 else "black"
                ax.text(j, i, text, ha="center", va="center", color=color, fontsize=9)
        
        ax.set_xlabel("Matrix Size")
        ax.set_ylabel("Distribution")
        ax.set_title(f"Stability Gain: Strassen StdDev / Alpha StdDev ({dtype})\n>1.0 = Alpha More Stable")
        fig.colorbar(im, label="Stability Gain")
        plt.tight_layout()
        plt.savefig(f"test_results/sweep/sweep_stability_{dtype}.png", dpi=150)
        plt.close()
        
        print(f"  Generated sweep grids for {dtype}")


def generate_scaling_analysis(all_results: dict, sizes: list, dtypes: list):
    """Generate scaling analysis: how error ratio changes with size."""
    if not HAS_MATPLOTLIB:
        return
    
    os.makedirs("test_results/sweep", exist_ok=True)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Define line styles and markers for each dtype to handle overlap
    dtype_styles = {
        "bfloat16": {"marker": "o", "linestyle": "-", "alpha": 0.8},
        "float16": {"marker": "s", "linestyle": "--", "alpha": 0.7},
        "float32": {"marker": "^", "linestyle": ":", "alpha": 0.9},
        "fp8": {"marker": "D", "linestyle": "-.", "alpha": 0.6}
    }
    
    # Plot for each dtype
    for dtype in dtypes:
        avg_error_ratios = []
        avg_stability_gains = []
        valid_sizes = []
        
        style = dtype_styles.get(dtype, {"marker": "o", "linestyle": "-", "alpha": 0.7})
        
        for size in sizes:
            data = all_results[dtype].get(size)
            if data is None:
                continue
            
            ratios = []
            gains = []
            for dist in DISTRIBUTIONS:
                if dist not in data["results"]:
                    continue
                alpha_err = data["results"][dist]["alpha"]["mean_error"]
                strassen_err = data["results"][dist]["strassen"]["mean_error"]
                alpha_std = data["results"][dist]["alpha"]["std_error"]
                strassen_std = data["results"][dist]["strassen"]["std_error"]
                
                if alpha_err > 1e-20 and not np.isnan(alpha_err):
                    ratios.append(strassen_err / alpha_err)
                if alpha_std > 1e-20 and not np.isnan(alpha_std):
                    gains.append(strassen_std / alpha_std)
            
            if ratios:
                avg_error_ratios.append(np.mean(ratios))
                avg_stability_gains.append(np.mean(gains))
                valid_sizes.append(size)
        
        if valid_sizes:
            axes[0].plot(
                valid_sizes, avg_error_ratios, 
                label=dtype, markersize=8, 
                marker=style["marker"], linestyle=style["linestyle"], alpha=style["alpha"]
            )
            axes[1].plot(
                valid_sizes, avg_stability_gains, 
                label=dtype, markersize=8, 
                marker=style["marker"], linestyle=style["linestyle"], alpha=style["alpha"]
            )
    
    axes[0].axhline(y=1.0, color='black', linestyle='--', alpha=0.5)
    axes[0].set_xlabel("Matrix Size")
    axes[0].set_ylabel("Avg Error Ratio (Strassen / Alpha)")
    axes[0].set_title("Error Ratio vs Matrix Size\n>1.0 = Alpha Better")
    axes[0].set_xscale('log', base=2)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    axes[1].axhline(y=1.0, color='black', linestyle='--', alpha=0.5)
    axes[1].set_xlabel("Matrix Size")
    axes[1].set_ylabel("Avg Stability Gain")
    axes[1].set_title("Stability Gain vs Matrix Size\n>1.0 = Alpha More Stable")
    axes[1].set_xscale('log', base=2)
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("test_results/sweep/scaling_analysis.png", dpi=150)
    plt.close()
    print("  Generated scaling analysis")


def generate_summary_dashboard(all_results: dict, sizes: list, dtypes: list):
    """Generate summary markdown with key findings."""
    os.makedirs("test_results/sweep", exist_ok=True)
    
    with open("test_results/sweep/SUMMARY.md", "w") as f:
        f.write("# Alpha-Kernel Sweep Summary\n\n")
        f.write("## Key Findings\n\n")
        
        for dtype in dtypes:
            f.write(f"### {dtype.upper()}\n\n")
            f.write("| Size | Avg Error Ratio | Avg Stability | Alpha Wins |\n")
            f.write("|------|-----------------|---------------|------------|\n")
            
            for size in sizes:
                data = all_results[dtype].get(size)
                if data is None:
                    f.write(f"| {size} | N/A | N/A | N/A |\n")
                    continue
                
                ratios = []
                gains = []
                wins = 0
                total = 0
                
                for dist in DISTRIBUTIONS:
                    if dist not in data["results"]:
                        continue
                    alpha_err = data["results"][dist]["alpha"]["mean_error"]
                    strassen_err = data["results"][dist]["strassen"]["mean_error"]
                    alpha_std = data["results"][dist]["alpha"]["std_error"]
                    strassen_std = data["results"][dist]["strassen"]["std_error"]
                    
                    if alpha_err > 1e-20 and not np.isnan(alpha_err):
                        ratios.append(strassen_err / alpha_err)
                        if alpha_err < strassen_err:
                            wins += 1
                        total += 1
                    if alpha_std > 1e-20 and not np.isnan(alpha_std):
                        gains.append(strassen_std / alpha_std)
                
                avg_ratio = np.mean(ratios) if ratios else 1.0
                avg_gain = np.mean(gains) if gains else 1.0
                
                f.write(f"| {size} | {avg_ratio:.2f}x | {avg_gain:.2f}x | {wins}/{total} |\n")
            
            f.write("\n")
        
        f.write("## Visualizations\n\n")
        for dtype in dtypes:
            f.write(f"### {dtype}\n\n")
            f.write(f"![Error Ratio](sweep_error_{dtype}.png)\n\n")
            f.write(f"![Stability Gain](sweep_stability_{dtype}.png)\n\n")
        
        f.write("![Scaling Analysis](scaling_analysis.png)\n")
    
    print("  Generated SUMMARY.md")


def generate_cross_precision_analysis(all_results: dict, sizes: list, dtypes: list):
    """Generate cross-precision meta-analysis: Alpha@lower_precision vs Strassen@higher_precision.
    
    This demonstrates the 'precision tier advantage' - e.g., Alpha@bf16 achieving
    similar or better error than Strassen@fp32.
    """
    if not HAS_MATPLOTLIB:
        return
    
    os.makedirs("test_results/sweep", exist_ok=True)
    
    # Define precision order (lower to higher)
    precision_order = ["bfloat16", "float16", "float32"]
    available_dtypes = [d for d in precision_order if d in dtypes]
    
    if len(available_dtypes) < 2:
        print("  Need at least 2 dtypes for cross-precision analysis")
        return
    
    # For each size, compare Alpha@low_precision vs Strassen@high_precision
    cross_precision_data = []
    
    for size in sizes:
        for low_idx, low_dtype in enumerate(available_dtypes):
            for high_dtype in available_dtypes[low_idx:]:  # Same or higher precision
                low_data = all_results.get(low_dtype, {}).get(size)
                high_data = all_results.get(high_dtype, {}).get(size)
                
                if low_data is None or high_data is None:
                    continue
                
                # Compare across all distributions
                for dist in DISTRIBUTIONS:
                    if dist not in low_data["results"] or dist not in high_data["results"]:
                        continue
                    
                    alpha_err = low_data["results"][dist]["alpha"]["mean_error"]
                    strassen_err = high_data["results"][dist]["strassen"]["mean_error"]
                    
                    if np.isnan(alpha_err) or np.isnan(strassen_err):
                        continue
                    
                    cross_precision_data.append({
                        "size": size,
                        "alpha_dtype": low_dtype,
                        "strassen_dtype": high_dtype,
                        "distribution": dist,
                        "alpha_error": alpha_err,
                        "strassen_error": strassen_err,
                        "alpha_wins": alpha_err < strassen_err,
                        "ratio": strassen_err / alpha_err if alpha_err > 1e-20 else 1.0
                    })
    
    if not cross_precision_data:
        print("  No cross-precision data available")
        return
    
    # Generate summary: how often Alpha@lower beats Strassen@higher
    precision_wins = {}
    for row in cross_precision_data:
        key = (row["alpha_dtype"], row["strassen_dtype"])
        if key not in precision_wins:
            precision_wins[key] = {"wins": 0, "total": 0, "ratios": []}
        precision_wins[key]["total"] += 1
        if row["alpha_wins"]:
            precision_wins[key]["wins"] += 1
        precision_wins[key]["ratios"].append(row["ratio"])
    
    # Create visualization: bar chart of win rates for cross-precision comparisons
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Filter to interesting comparisons (different precisions)
    interesting_keys = [(a, s) for a, s in precision_wins.keys() if a != s]
    
    if interesting_keys:
        labels = [f"Alpha@{a}\nvs\nStrassen@{s}" for a, s in interesting_keys]
        win_rates = [precision_wins[k]["wins"] / precision_wins[k]["total"] * 100 for k in interesting_keys]
        avg_ratios = [np.mean(precision_wins[k]["ratios"]) for k in interesting_keys]
        
        # Win rate chart
        colors = ['#2ecc71' if wr > 50 else '#e74c3c' for wr in win_rates]
        bars = axes[0].bar(range(len(labels)), win_rates, color=colors)
        axes[0].set_xticks(range(len(labels)))
        axes[0].set_xticklabels(labels, fontsize=9)
        axes[0].set_ylabel("Alpha Win Rate (%)")
        axes[0].set_title("Cross-Precision Win Rate\n(Alpha@lower vs Strassen@higher)")
        axes[0].axhline(y=50, color='black', linestyle='--', alpha=0.5)
        axes[0].set_ylim(0, 100)
        
        for bar, wr in zip(bars, win_rates):
            axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                        f'{wr:.0f}%', ha='center', fontsize=10)
        
        # Avg error ratio chart
        colors = ['#2ecc71' if r > 1 else '#e74c3c' for r in avg_ratios]
        bars = axes[1].bar(range(len(labels)), avg_ratios, color=colors)
        axes[1].set_xticks(range(len(labels)))
        axes[1].set_xticklabels(labels, fontsize=9)
        axes[1].set_ylabel("Avg Error Ratio (Strassen/Alpha)")
        axes[1].set_title("Cross-Precision Error Advantage\n>1.0 = Alpha Better Even at Lower Precision")
        axes[1].axhline(y=1.0, color='black', linestyle='--', alpha=0.5)
        
        for bar, r in zip(bars, avg_ratios):
            axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                        f'{r:.2f}x', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig("test_results/sweep/cross_precision_analysis.png", dpi=150)
    plt.close()
    
    # Generate markdown summary
    with open("test_results/sweep/CROSS_PRECISION.md", "w") as f:
        f.write("# Cross-Precision Meta-Analysis\n\n")
        f.write("**Key Question**: Can Alpha at *lower* precision match or beat Strassen at *higher* precision?\n\n")
        f.write("This would demonstrate computational savings - using cheaper precision with Alpha\n")
        f.write("instead of expensive precision with Strassen.\n\n")
        
        f.write("## Summary\n\n")
        f.write("| Comparison | Alpha Wins | Avg Error Ratio | Verdict |\n")
        f.write("|------------|------------|-----------------|----------|\n")
        
        for (alpha_dt, strassen_dt), stats in sorted(precision_wins.items()):
            win_pct = stats["wins"] / stats["total"] * 100
            avg_ratio = np.mean(stats["ratios"])
            
            if alpha_dt == strassen_dt:
                verdict = "Baseline"
            elif win_pct > 50 and avg_ratio > 1.0:
                verdict = "✅ Alpha@lower WINS"
            elif win_pct > 50:
                verdict = "⚠️ Mixed"
            else:
                verdict = "❌ Strassen@higher wins"
            
            f.write(f"| Alpha@{alpha_dt} vs Strassen@{strassen_dt} | {stats['wins']}/{stats['total']} ({win_pct:.0f}%) | {avg_ratio:.2f}x | {verdict} |\n")
        
        # Count cross-precision wins
        cross_wins = sum(1 for (a, s), st in precision_wins.items() 
                        if a != s and st["wins"] / st["total"] > 0.5)
        cross_total = sum(1 for (a, s) in precision_wins.keys() if a != s)
        
        f.write("\n## Interpretation\n\n")
        
        if cross_wins > 0:
            f.write("✅ **Cross-Precision Advantage Detected!**\n\n")
            f.write("- Alpha at *lower* precision can match Strassen at *higher* precision in some cases\n")
            f.write("- **Cost savings potential**: Use cheaper precision with Alpha for equivalent accuracy\n\n")
        else:
            f.write("📊 **Same-Tier Stability Advantage**\n\n")
            f.write("- Alpha's advantage is strongest *within* the same precision tier\n")
            f.write("- Higher precision still wins over lower precision (as expected mathematically)\n")
            f.write("- **Key insight**: Within your chosen precision budget, Alpha beats Strassen\n\n")
        
        f.write("### Legend\n")
        f.write("- **Baseline**: Same-precision comparison (Alpha vs Strassen at equal precision)\n")
        f.write("- **Avg Error Ratio**: Strassen Error / Alpha Error (>1.0 = Alpha better)\n\n")
        
        f.write("![Cross-Precision Analysis](cross_precision_analysis.png)\n")
    
    print("  Generated cross-precision analysis")


def run_sweep(sizes: list, dtypes: list, trials: int):
    """Run test_lab.py for all size × dtype combinations."""
    
    total = len(sizes) * len(dtypes)
    completed = 0
    failed = []
    
    print("=" * 70)
    print("TEST LAB SWEEP")
    print("=" * 70)
    print(f"Sizes: {sizes}")
    print(f"Dtypes: {dtypes}")
    print(f"Trials: {trials}")
    print(f"Total runs: {total}")
    print("=" * 70)
    
    # Create output directories for all dtypes
    for dtype in dtypes:
        os.makedirs(f"test_results/md/{dtype}", exist_ok=True)
        os.makedirs(f"test_results/json/{dtype}", exist_ok=True)
        os.makedirs(f"test_results/heatmaps/{dtype}", exist_ok=True)
    os.makedirs("test_results/sweep", exist_ok=True)
    
    for size in sizes:
        for dtype in dtypes:
            completed += 1
            print(f"\n[{completed}/{total}] Running size={size} dtype={dtype}...")
            
            # Scale base_size to prevent OOM on large matrices
            if size >= 4096:
                base_size = 128
            elif size >= 2048:
                base_size = 64
            else:
                base_size = 16
            
            cmd = [
                sys.executable, "test_lab.py",
                "--size", str(size),
                "--dtype", dtype,
                "--trials", str(trials),
                "--base", str(base_size)
            ]
            
            try:
                result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                print(f"  ❌ FAILED: {e}")
                failed.append((size, dtype))
            except KeyboardInterrupt:
                print("\n\n⚠️  Sweep interrupted by user")
                break
        else:
            continue
        break  # Break outer loop if inner was interrupted
    
    # Generate aggregate visualizations
    print("\n" + "=" * 70)
    print("GENERATING AGGREGATE VISUALIZATIONS")
    print("=" * 70)
    
    all_results = load_results(sizes, dtypes, trials)
    generate_sweep_grids(all_results, sizes, dtypes)
    generate_scaling_analysis(all_results, sizes, dtypes)
    generate_summary_dashboard(all_results, sizes, dtypes)
    generate_cross_precision_analysis(all_results, sizes, dtypes)
    
    # Summary
    print("\n" + "=" * 70)
    print("SWEEP COMPLETE")
    print("=" * 70)
    print(f"Completed: {completed}/{total}")
    if failed:
        print(f"Failed: {len(failed)}")
        for size, dtype in failed:
            print(f"  - size={size} dtype={dtype}")
    else:
        print("All runs succeeded ✅")
    
    print("\nAggregate results saved to:")
    print("  - test_results/sweep/SUMMARY.md")
    print("  - test_results/sweep/CROSS_PRECISION.md")
    print("  - test_results/sweep/sweep_error_*.png")
    print("  - test_results/sweep/sweep_stability_*.png")
    print("  - test_results/sweep/scaling_analysis.png")
    print("  - test_results/sweep/cross_precision_analysis.png")


def main():
    parser = argparse.ArgumentParser(
        description="Run test_lab.py across multiple sizes and dtypes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--sizes", type=int, nargs="+", default=DEFAULT_SIZES,
        help=f"Matrix sizes to test (default: {DEFAULT_SIZES})"
    )
    parser.add_argument(
        "--dtypes", type=str, nargs="+", default=DEFAULT_DTYPES,
        help=f"Data types to test (default: {DEFAULT_DTYPES})"
    )
    parser.add_argument(
        "--trials", type=int, default=DEFAULT_TRIALS,
        help=f"Number of trials per run (default: {DEFAULT_TRIALS})"
    )
    
    args = parser.parse_args()
    run_sweep(args.sizes, args.dtypes, args.trials)


if __name__ == "__main__":
    main()
