# Test Lab: Verification Results

**Generated:** 2026-01-14 10:02:17

## Parameters

- **Matrix Size:** 1024×1024
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 2.0291e-01 | 2.2005e-02 | 3.6664e-02 | 8.9770e-03 | 1.1473e-01 | 1.4651e-01 | 8.8632e-02 |
| strassen | 2.0272e-01 | 6.6143e-02 | 7.3781e-02 | 6.2803e-02 | 2.0413e-01 | 2.2819e-01 | 1.3963e-01 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 8.0289e-04 | 1.3207e-04 | 2.0591e-04 | 6.1832e-05 | 3.7952e-03 | 3.8225e-03 | 1.4701e-03 |
| strassen | 6.3586e-04 | 5.4004e-04 | 5.8607e-04 | 1.6368e-03 | 5.6331e-03 | 5.4868e-03 | 2.4198e-03 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 2.03e-01 | 2.03e-01 | -0.1% | Strassen |
| relu | 2.20e-02 | 6.61e-02 | +66.7% | Alpha |
| gelu | 3.67e-02 | 7.38e-02 | +50.3% | Alpha |
| biased | 8.98e-03 | 6.28e-02 | +85.7% | Alpha |
| attention | 1.15e-01 | 2.04e-01 | +43.8% | Alpha |
| causal_transformer | 1.47e-01 | 2.28e-01 | +35.8% | Alpha |
| **Average** | | | **+47.0%** | Alpha: 5/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 8.03e-04 | 6.36e-04 | -26.3% | Strassen |
| relu | 1.32e-04 | 5.40e-04 | +75.5% | Alpha |
| gelu | 2.06e-04 | 5.86e-04 | +64.9% | Alpha |
| biased | 6.18e-05 | 1.64e-03 | +96.2% | Alpha |
| attention | 3.80e-03 | 5.63e-03 | +32.6% | Alpha |
| causal_transformer | 3.82e-03 | 5.49e-03 | +30.3% | Alpha |
| **Average** | | | **+45.6%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 5/6 distributions (avg +47.0%)
- **StdDev:** Alpha wins 5/6 distributions (avg +45.6%)
