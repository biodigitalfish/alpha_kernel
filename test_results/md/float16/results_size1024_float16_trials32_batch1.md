# Test Lab: Verification Results

**Generated:** 2026-01-14 10:02:30

## Parameters

- **Matrix Size:** 1024×1024
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 2.5363e-02 | 2.7521e-03 | 4.5881e-03 | 1.1223e-03 | 1.4895e-02 | 1.8763e-02 | 1.1247e-02 |
| strassen | 2.5328e-02 | 8.2756e-03 | 9.2423e-03 | 7.8685e-03 | 2.6776e-02 | 2.9204e-02 | 1.7783e-02 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.0303e-04 | 1.6135e-05 | 2.8988e-05 | 6.6750e-06 | 5.0189e-04 | 4.9593e-04 | 1.9211e-04 |
| strassen | 1.0052e-04 | 6.4424e-05 | 8.3548e-05 | 2.1693e-04 | 6.8063e-04 | 6.8094e-04 | 3.0450e-04 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 2.54e-02 | 2.53e-02 | -0.1% | Strassen |
| relu | 2.75e-03 | 8.28e-03 | +66.7% | Alpha |
| gelu | 4.59e-03 | 9.24e-03 | +50.4% | Alpha |
| biased | 1.12e-03 | 7.87e-03 | +85.7% | Alpha |
| attention | 1.49e-02 | 2.68e-02 | +44.4% | Alpha |
| causal_transformer | 1.88e-02 | 2.92e-02 | +35.8% | Alpha |
| **Average** | | | **+47.1%** | Alpha: 5/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.03e-04 | 1.01e-04 | -2.5% | Strassen |
| relu | 1.61e-05 | 6.44e-05 | +75.0% | Alpha |
| gelu | 2.90e-05 | 8.35e-05 | +65.3% | Alpha |
| biased | 6.67e-06 | 2.17e-04 | +96.9% | Alpha |
| attention | 5.02e-04 | 6.81e-04 | +26.3% | Alpha |
| causal_transformer | 4.96e-04 | 6.81e-04 | +27.2% | Alpha |
| **Average** | | | **+48.0%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 5/6 distributions (avg +47.1%)
- **StdDev:** Alpha wins 5/6 distributions (avg +48.0%)
