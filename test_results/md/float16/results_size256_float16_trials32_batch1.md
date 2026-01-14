# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:56

## Parameters

- **Matrix Size:** 256×256
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 6.3198e-03 | 1.2267e-03 | 2.0487e-03 | 6.3239e-04 | 3.8232e-03 | 4.6712e-03 | 3.1203e-03 |
| strassen | 6.3076e-03 | 2.8026e-03 | 3.2791e-03 | 2.5963e-03 | 5.9343e-03 | 6.9020e-03 | 4.6370e-03 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 6.0215e-05 | 1.7023e-05 | 2.6796e-05 | 5.3090e-06 | 1.2915e-04 | 1.7645e-04 | 6.9157e-05 |
| strassen | 5.5311e-05 | 5.9363e-05 | 5.9547e-05 | 7.5707e-05 | 2.4644e-04 | 2.1693e-04 | 1.1888e-04 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 6.32e-03 | 6.31e-03 | -0.2% | Strassen |
| relu | 1.23e-03 | 2.80e-03 | +56.2% | Alpha |
| gelu | 2.05e-03 | 3.28e-03 | +37.5% | Alpha |
| biased | 6.32e-04 | 2.60e-03 | +75.6% | Alpha |
| attention | 3.82e-03 | 5.93e-03 | +35.6% | Alpha |
| causal_transformer | 4.67e-03 | 6.90e-03 | +32.3% | Alpha |
| **Average** | | | **+39.5%** | Alpha: 5/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 6.02e-05 | 5.53e-05 | -8.9% | Strassen |
| relu | 1.70e-05 | 5.94e-05 | +71.3% | Alpha |
| gelu | 2.68e-05 | 5.95e-05 | +55.0% | Alpha |
| biased | 5.31e-06 | 7.57e-05 | +93.0% | Alpha |
| attention | 1.29e-04 | 2.46e-04 | +47.6% | Alpha |
| causal_transformer | 1.76e-04 | 2.17e-04 | +18.7% | Alpha |
| **Average** | | | **+46.1%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 5/6 distributions (avg +39.5%)
- **StdDev:** Alpha wins 5/6 distributions (avg +46.1%)
