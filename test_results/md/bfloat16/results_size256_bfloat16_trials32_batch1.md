# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:51

## Parameters

- **Matrix Size:** 256×256
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 5.0492e-02 | 9.7859e-03 | 1.6428e-02 | 5.0531e-03 | 2.9608e-02 | 3.6622e-02 | 2.4665e-02 |
| strassen | 5.0567e-02 | 2.2412e-02 | 2.6295e-02 | 2.0781e-02 | 4.5555e-02 | 5.3980e-02 | 3.6598e-02 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 6.2245e-04 | 1.1440e-04 | 2.3525e-04 | 4.8540e-05 | 1.0465e-03 | 1.4333e-03 | 5.8339e-04 |
| strassen | 3.4626e-04 | 3.1460e-04 | 4.9073e-04 | 5.5503e-04 | 1.8989e-03 | 1.5919e-03 | 8.6624e-04 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 5.05e-02 | 5.06e-02 | +0.1% | Alpha |
| relu | 9.79e-03 | 2.24e-02 | +56.3% | Alpha |
| gelu | 1.64e-02 | 2.63e-02 | +37.5% | Alpha |
| biased | 5.05e-03 | 2.08e-02 | +75.7% | Alpha |
| attention | 2.96e-02 | 4.56e-02 | +35.0% | Alpha |
| causal_transformer | 3.66e-02 | 5.40e-02 | +32.2% | Alpha |
| **Average** | | | **+39.5%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 6.22e-04 | 3.46e-04 | -79.8% | Strassen |
| relu | 1.14e-04 | 3.15e-04 | +63.6% | Alpha |
| gelu | 2.35e-04 | 4.91e-04 | +52.1% | Alpha |
| biased | 4.85e-05 | 5.55e-04 | +91.3% | Alpha |
| attention | 1.05e-03 | 1.90e-03 | +44.9% | Alpha |
| causal_transformer | 1.43e-03 | 1.59e-03 | +10.0% | Alpha |
| **Average** | | | **+30.3%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +39.5%)
- **StdDev:** Alpha wins 5/6 distributions (avg +30.3%)
