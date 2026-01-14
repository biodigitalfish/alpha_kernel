# Test Lab: Verification Results

**Generated:** 2026-01-14 10:10:21

## Parameters

- **Matrix Size:** 4096×4096
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 6.6724e-06 | 3.6887e-07 | 6.1551e-07 | 2.0742e-07 | 4.1657e-06 | 5.6147e-06 | 2.9408e-06 |
| strassen | 6.6708e-06 | 2.7664e-06 | 2.8325e-06 | 2.4140e-06 | 6.7784e-06 | 8.5234e-06 | 4.9976e-06 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 6.2254e-09 | 1.4747e-09 | 1.8980e-09 | 4.5592e-10 | 6.8367e-08 | 9.3092e-08 | 2.8585e-08 |
| strassen | 6.0759e-09 | 6.5906e-09 | 9.7865e-09 | 4.9510e-09 | 8.8834e-08 | 7.7203e-08 | 3.2240e-08 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 6.67e-06 | 6.67e-06 | -0.0% | Strassen |
| relu | 3.69e-07 | 2.77e-06 | +86.7% | Alpha |
| gelu | 6.16e-07 | 2.83e-06 | +78.3% | Alpha |
| biased | 2.07e-07 | 2.41e-06 | +91.4% | Alpha |
| attention | 4.17e-06 | 6.78e-06 | +38.5% | Alpha |
| causal_transformer | 5.61e-06 | 8.52e-06 | +34.1% | Alpha |
| **Average** | | | **+54.8%** | Alpha: 5/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 6.23e-09 | 6.08e-09 | -2.5% | Strassen |
| relu | 1.47e-09 | 6.59e-09 | +77.6% | Alpha |
| gelu | 1.90e-09 | 9.79e-09 | +80.6% | Alpha |
| biased | 4.56e-10 | 4.95e-09 | +90.8% | Alpha |
| attention | 6.84e-08 | 8.88e-08 | +23.0% | Alpha |
| causal_transformer | 9.31e-08 | 7.72e-08 | -20.6% | Strassen |
| **Average** | | | **+41.5%** | Alpha: 4/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 5/6 distributions (avg +54.8%)
- **StdDev:** Alpha wins 4/6 distributions (avg +41.5%)
