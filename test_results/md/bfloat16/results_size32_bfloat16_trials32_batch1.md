# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:03

## Parameters

- **Matrix Size:** 32×32
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 6.1700e-03 | 3.1360e-03 | 4.3916e-03 | 2.6535e-03 | 4.0840e-03 | 4.7882e-03 | 4.2039e-03 |
| strassen | 6.2184e-03 | 4.0554e-03 | 5.0540e-03 | 3.7683e-03 | 4.9806e-03 | 5.8514e-03 | 4.9880e-03 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 2.5354e-04 | 1.3423e-04 | 1.9949e-04 | 7.0359e-05 | 2.9476e-04 | 2.6634e-04 | 2.0312e-04 |
| strassen | 2.7588e-04 | 1.9731e-04 | 3.2810e-04 | 1.7212e-04 | 2.8646e-04 | 3.5776e-04 | 2.6960e-04 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 6.17e-03 | 6.22e-03 | +0.8% | Alpha |
| relu | 3.14e-03 | 4.06e-03 | +22.7% | Alpha |
| gelu | 4.39e-03 | 5.05e-03 | +13.1% | Alpha |
| biased | 2.65e-03 | 3.77e-03 | +29.6% | Alpha |
| attention | 4.08e-03 | 4.98e-03 | +18.0% | Alpha |
| causal_transformer | 4.79e-03 | 5.85e-03 | +18.2% | Alpha |
| **Average** | | | **+17.1%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 2.54e-04 | 2.76e-04 | +8.1% | Alpha |
| relu | 1.34e-04 | 1.97e-04 | +32.0% | Alpha |
| gelu | 1.99e-04 | 3.28e-04 | +39.2% | Alpha |
| biased | 7.04e-05 | 1.72e-04 | +59.1% | Alpha |
| attention | 2.95e-04 | 2.86e-04 | -2.9% | Strassen |
| causal_transformer | 2.66e-04 | 3.58e-04 | +25.6% | Alpha |
| **Average** | | | **+26.8%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +17.1%)
- **StdDev:** Alpha wins 5/6 distributions (avg +26.8%)
