# Test Lab: Verification Results

**Generated:** 2026-01-14 10:02:50

## Parameters

- **Matrix Size:** 1024×1024
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 4.8590e-06 | 5.3104e-07 | 8.8354e-07 | 2.0509e-07 | 3.1686e-06 | 4.0062e-06 | 2.2756e-06 |
| strassen | 4.8543e-06 | 1.6291e-06 | 1.8011e-06 | 1.5017e-06 | 5.4824e-06 | 6.2866e-06 | 3.5925e-06 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.8972e-08 | 4.1793e-09 | 6.1129e-09 | 1.5905e-09 | 1.1660e-07 | 1.2027e-07 | 4.4621e-08 |
| strassen | 1.8439e-08 | 1.5761e-08 | 1.7755e-08 | 3.4539e-08 | 1.6319e-07 | 1.5769e-07 | 6.7895e-08 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 4.86e-06 | 4.85e-06 | -0.1% | Strassen |
| relu | 5.31e-07 | 1.63e-06 | +67.4% | Alpha |
| gelu | 8.84e-07 | 1.80e-06 | +50.9% | Alpha |
| biased | 2.05e-07 | 1.50e-06 | +86.3% | Alpha |
| attention | 3.17e-06 | 5.48e-06 | +42.2% | Alpha |
| causal_transformer | 4.01e-06 | 6.29e-06 | +36.3% | Alpha |
| **Average** | | | **+47.2%** | Alpha: 5/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.90e-08 | 1.84e-08 | -2.9% | Strassen |
| relu | 4.18e-09 | 1.58e-08 | +73.5% | Alpha |
| gelu | 6.11e-09 | 1.78e-08 | +65.6% | Alpha |
| biased | 1.59e-09 | 3.45e-08 | +95.4% | Alpha |
| attention | 1.17e-07 | 1.63e-07 | +28.5% | Alpha |
| causal_transformer | 1.20e-07 | 1.58e-07 | +23.7% | Alpha |
| **Average** | | | **+47.3%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 5/6 distributions (avg +47.2%)
- **StdDev:** Alpha wins 5/6 distributions (avg +47.3%)
