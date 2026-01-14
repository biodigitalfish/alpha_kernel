# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:11

## Parameters

- **Matrix Size:** 32×32
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.3903e-07 | 6.7776e-08 | 9.6662e-08 | 5.6223e-08 | 9.7180e-08 | 1.1180e-07 | 9.4778e-08 |
| strassen | 1.3946e-07 | 9.4348e-08 | 1.1606e-07 | 8.7640e-08 | 1.2608e-07 | 1.3647e-07 | 1.1668e-07 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 5.0201e-09 | 3.0599e-09 | 4.6819e-09 | 1.5851e-09 | 7.1908e-09 | 7.8485e-09 | 4.8977e-09 |
| strassen | 5.6092e-09 | 5.1145e-09 | 7.8674e-09 | 2.8708e-09 | 1.0430e-08 | 9.0999e-09 | 6.8320e-09 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.39e-07 | 1.39e-07 | +0.3% | Alpha |
| relu | 6.78e-08 | 9.43e-08 | +28.2% | Alpha |
| gelu | 9.67e-08 | 1.16e-07 | +16.7% | Alpha |
| biased | 5.62e-08 | 8.76e-08 | +35.8% | Alpha |
| attention | 9.72e-08 | 1.26e-07 | +22.9% | Alpha |
| causal_transformer | 1.12e-07 | 1.36e-07 | +18.1% | Alpha |
| **Average** | | | **+20.3%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 5.02e-09 | 5.61e-09 | +10.5% | Alpha |
| relu | 3.06e-09 | 5.11e-09 | +40.2% | Alpha |
| gelu | 4.68e-09 | 7.87e-09 | +40.5% | Alpha |
| biased | 1.59e-09 | 2.87e-09 | +44.8% | Alpha |
| attention | 7.19e-09 | 1.04e-08 | +31.1% | Alpha |
| causal_transformer | 7.85e-09 | 9.10e-09 | +13.8% | Alpha |
| **Average** | | | **+30.1%** | Alpha: 6/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +20.3%)
- **StdDev:** Alpha wins 6/6 distributions (avg +30.1%)
