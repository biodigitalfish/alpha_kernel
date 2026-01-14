# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:27

## Parameters

- **Matrix Size:** 64×64
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 2.9037e-07 | 1.0403e-07 | 1.6031e-07 | 7.0388e-08 | 1.9646e-07 | 2.3316e-07 | 1.7579e-07 |
| strassen | 2.9070e-07 | 1.7681e-07 | 2.1551e-07 | 1.6023e-07 | 2.7083e-07 | 3.0845e-07 | 2.3709e-07 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 6.7368e-09 | 3.2413e-09 | 5.4735e-09 | 1.5450e-09 | 1.1938e-08 | 1.2033e-08 | 6.8281e-09 |
| strassen | 8.8628e-09 | 7.2093e-09 | 1.0563e-08 | 6.0651e-09 | 2.2860e-08 | 1.5663e-08 | 1.1870e-08 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 2.90e-07 | 2.91e-07 | +0.1% | Alpha |
| relu | 1.04e-07 | 1.77e-07 | +41.2% | Alpha |
| gelu | 1.60e-07 | 2.16e-07 | +25.6% | Alpha |
| biased | 7.04e-08 | 1.60e-07 | +56.1% | Alpha |
| attention | 1.96e-07 | 2.71e-07 | +27.5% | Alpha |
| causal_transformer | 2.33e-07 | 3.08e-07 | +24.4% | Alpha |
| **Average** | | | **+29.1%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 6.74e-09 | 8.86e-09 | +24.0% | Alpha |
| relu | 3.24e-09 | 7.21e-09 | +55.0% | Alpha |
| gelu | 5.47e-09 | 1.06e-08 | +48.2% | Alpha |
| biased | 1.55e-09 | 6.07e-09 | +74.5% | Alpha |
| attention | 1.19e-08 | 2.29e-08 | +47.8% | Alpha |
| causal_transformer | 1.20e-08 | 1.57e-08 | +23.2% | Alpha |
| **Average** | | | **+45.4%** | Alpha: 6/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +29.1%)
- **StdDev:** Alpha wins 6/6 distributions (avg +45.4%)
