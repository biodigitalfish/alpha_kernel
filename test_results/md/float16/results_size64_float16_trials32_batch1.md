# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:23

## Parameters

- **Matrix Size:** 64×64
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.5825e-03 | 5.7728e-04 | 8.8197e-04 | 4.2164e-04 | 9.6048e-04 | 1.1671e-03 | 9.3182e-04 |
| strassen | 1.5787e-03 | 9.2963e-04 | 1.1502e-03 | 8.6438e-04 | 1.3205e-03 | 1.5719e-03 | 1.2359e-03 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 4.6117e-05 | 1.5051e-05 | 2.6048e-05 | 7.8233e-06 | 5.5727e-05 | 5.3551e-05 | 3.4053e-05 |
| strassen | 3.7751e-05 | 3.4162e-05 | 4.7973e-05 | 2.7233e-05 | 9.2383e-05 | 6.8890e-05 | 5.1399e-05 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.58e-03 | 1.58e-03 | -0.2% | Strassen |
| relu | 5.77e-04 | 9.30e-04 | +37.9% | Alpha |
| gelu | 8.82e-04 | 1.15e-03 | +23.3% | Alpha |
| biased | 4.22e-04 | 8.64e-04 | +51.2% | Alpha |
| attention | 9.60e-04 | 1.32e-03 | +27.3% | Alpha |
| causal_transformer | 1.17e-03 | 1.57e-03 | +25.8% | Alpha |
| **Average** | | | **+27.5%** | Alpha: 5/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 4.61e-05 | 3.78e-05 | -22.2% | Strassen |
| relu | 1.51e-05 | 3.42e-05 | +55.9% | Alpha |
| gelu | 2.60e-05 | 4.80e-05 | +45.7% | Alpha |
| biased | 7.82e-06 | 2.72e-05 | +71.3% | Alpha |
| attention | 5.57e-05 | 9.24e-05 | +39.7% | Alpha |
| causal_transformer | 5.36e-05 | 6.89e-05 | +22.3% | Alpha |
| **Average** | | | **+35.4%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 5/6 distributions (avg +27.5%)
- **StdDev:** Alpha wins 5/6 distributions (avg +35.4%)
