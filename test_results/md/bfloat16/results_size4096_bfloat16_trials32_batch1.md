# Test Lab: Verification Results

**Generated:** 2026-01-14 10:06:10

## Parameters

- **Matrix Size:** 4096×4096
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.0131e-01 | 6.6158e-03 | 9.7458e-03 | 4.6961e-03 | 5.2967e-02 | 7.2536e-02 | 4.1312e-02 |
| strassen | 1.0129e-01 | 3.4520e-02 | 3.5365e-02 | 3.4241e-02 | 8.5406e-02 | 1.0811e-01 | 6.6488e-02 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 6.3825e-05 | 1.0110e-05 | 1.2358e-05 | 1.2389e-05 | 5.9047e-04 | 8.9733e-04 | 2.6441e-04 |
| strassen | 7.5986e-05 | 3.3997e-05 | 4.1454e-05 | 3.1667e-04 | 1.0424e-03 | 8.1134e-04 | 3.8697e-04 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.01e-01 | 1.01e-01 | -0.0% | Strassen |
| relu | 6.62e-03 | 3.45e-02 | +80.8% | Alpha |
| gelu | 9.75e-03 | 3.54e-02 | +72.4% | Alpha |
| biased | 4.70e-03 | 3.42e-02 | +86.3% | Alpha |
| attention | 5.30e-02 | 8.54e-02 | +38.0% | Alpha |
| causal_transformer | 7.25e-02 | 1.08e-01 | +32.9% | Alpha |
| **Average** | | | **+51.7%** | Alpha: 5/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 6.38e-05 | 7.60e-05 | +16.0% | Alpha |
| relu | 1.01e-05 | 3.40e-05 | +70.3% | Alpha |
| gelu | 1.24e-05 | 4.15e-05 | +70.2% | Alpha |
| biased | 1.24e-05 | 3.17e-04 | +96.1% | Alpha |
| attention | 5.90e-04 | 1.04e-03 | +43.4% | Alpha |
| causal_transformer | 8.97e-04 | 8.11e-04 | -10.6% | Strassen |
| **Average** | | | **+47.6%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 5/6 distributions (avg +51.7%)
- **StdDev:** Alpha wins 5/6 distributions (avg +47.6%)
