# Test Lab: Verification Results

**Generated:** 2026-01-14 10:07:51

## Parameters

- **Matrix Size:** 4096×4096
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.2666e-02 | 8.2687e-04 | 1.2180e-03 | 5.8674e-04 | 6.7071e-03 | 9.1384e-03 | 5.1906e-03 |
| strassen | 1.2662e-02 | 4.3176e-03 | 4.4227e-03 | 4.2863e-03 | 1.0941e-02 | 1.3632e-02 | 8.3770e-03 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 9.1129e-06 | 1.2296e-06 | 1.8804e-06 | 1.5714e-06 | 7.4156e-05 | 1.0884e-04 | 3.2799e-05 |
| strassen | 8.9454e-06 | 5.1962e-06 | 6.1627e-06 | 3.6657e-05 | 1.3273e-04 | 9.9775e-05 | 4.8245e-05 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.27e-02 | 1.27e-02 | -0.0% | Strassen |
| relu | 8.27e-04 | 4.32e-03 | +80.8% | Alpha |
| gelu | 1.22e-03 | 4.42e-03 | +72.5% | Alpha |
| biased | 5.87e-04 | 4.29e-03 | +86.3% | Alpha |
| attention | 6.71e-03 | 1.09e-02 | +38.7% | Alpha |
| causal_transformer | 9.14e-03 | 1.36e-02 | +33.0% | Alpha |
| **Average** | | | **+51.9%** | Alpha: 5/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 9.11e-06 | 8.95e-06 | -1.9% | Strassen |
| relu | 1.23e-06 | 5.20e-06 | +76.3% | Alpha |
| gelu | 1.88e-06 | 6.16e-06 | +69.5% | Alpha |
| biased | 1.57e-06 | 3.67e-05 | +95.7% | Alpha |
| attention | 7.42e-05 | 1.33e-04 | +44.1% | Alpha |
| causal_transformer | 1.09e-04 | 9.98e-05 | -9.1% | Strassen |
| **Average** | | | **+45.8%** | Alpha: 4/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 5/6 distributions (avg +51.9%)
- **StdDev:** Alpha wins 4/6 distributions (avg +45.8%)
