# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:39

## Parameters

- **Matrix Size:** 128×128
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 3.1659e-03 | 8.2901e-04 | 1.3558e-03 | 5.1297e-04 | 1.9127e-03 | 2.3222e-03 | 1.6831e-03 |
| strassen | 3.1785e-03 | 1.5955e-03 | 1.9550e-03 | 1.4955e-03 | 2.7627e-03 | 3.3117e-03 | 2.3832e-03 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 4.8589e-05 | 1.7489e-05 | 3.0792e-05 | 7.8738e-06 | 1.0216e-04 | 1.1312e-04 | 5.3337e-05 |
| strassen | 4.7722e-05 | 3.9937e-05 | 6.0654e-05 | 5.0496e-05 | 9.2498e-05 | 1.2586e-04 | 6.9528e-05 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 3.17e-03 | 3.18e-03 | +0.4% | Alpha |
| relu | 8.29e-04 | 1.60e-03 | +48.0% | Alpha |
| gelu | 1.36e-03 | 1.95e-03 | +30.7% | Alpha |
| biased | 5.13e-04 | 1.50e-03 | +65.7% | Alpha |
| attention | 1.91e-03 | 2.76e-03 | +30.8% | Alpha |
| causal_transformer | 2.32e-03 | 3.31e-03 | +29.9% | Alpha |
| **Average** | | | **+34.2%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 4.86e-05 | 4.77e-05 | -1.8% | Strassen |
| relu | 1.75e-05 | 3.99e-05 | +56.2% | Alpha |
| gelu | 3.08e-05 | 6.07e-05 | +49.2% | Alpha |
| biased | 7.87e-06 | 5.05e-05 | +84.4% | Alpha |
| attention | 1.02e-04 | 9.25e-05 | -10.4% | Strassen |
| causal_transformer | 1.13e-04 | 1.26e-04 | +10.1% | Alpha |
| **Average** | | | **+31.3%** | Alpha: 4/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +34.2%)
- **StdDev:** Alpha wins 4/6 distributions (avg +31.3%)
