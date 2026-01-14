# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:43

## Parameters

- **Matrix Size:** 128×128
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 5.8388e-07 | 1.5287e-07 | 2.4931e-07 | 8.5465e-08 | 3.9605e-07 | 4.7265e-07 | 3.2337e-07 |
| strassen | 5.8626e-07 | 3.0387e-07 | 3.6564e-07 | 2.7591e-07 | 5.7049e-07 | 6.6955e-07 | 4.6195e-07 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.0116e-08 | 3.1317e-09 | 6.3936e-09 | 1.5790e-09 | 2.2589e-08 | 2.3288e-08 | 1.1183e-08 |
| strassen | 1.1012e-08 | 1.0050e-08 | 1.2988e-08 | 8.5373e-09 | 2.4529e-08 | 2.9451e-08 | 1.6095e-08 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 5.84e-07 | 5.86e-07 | +0.4% | Alpha |
| relu | 1.53e-07 | 3.04e-07 | +49.7% | Alpha |
| gelu | 2.49e-07 | 3.66e-07 | +31.8% | Alpha |
| biased | 8.55e-08 | 2.76e-07 | +69.0% | Alpha |
| attention | 3.96e-07 | 5.70e-07 | +30.6% | Alpha |
| causal_transformer | 4.73e-07 | 6.70e-07 | +29.4% | Alpha |
| **Average** | | | **+35.2%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.01e-08 | 1.10e-08 | +8.1% | Alpha |
| relu | 3.13e-09 | 1.01e-08 | +68.8% | Alpha |
| gelu | 6.39e-09 | 1.30e-08 | +50.8% | Alpha |
| biased | 1.58e-09 | 8.54e-09 | +81.5% | Alpha |
| attention | 2.26e-08 | 2.45e-08 | +7.9% | Alpha |
| causal_transformer | 2.33e-08 | 2.95e-08 | +20.9% | Alpha |
| **Average** | | | **+39.7%** | Alpha: 6/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +35.2%)
- **StdDev:** Alpha wins 6/6 distributions (avg +39.7%)
