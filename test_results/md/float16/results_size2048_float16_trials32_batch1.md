# Test Lab: Verification Results

**Generated:** 2026-01-14 10:03:47

## Parameters

- **Matrix Size:** 2048×2048
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.2655e-02 | 1.0345e-03 | 1.6303e-03 | 6.2533e-04 | 6.9902e-03 | 9.1917e-03 | 5.3545e-03 |
| strassen | 1.2660e-02 | 4.3992e-03 | 4.5908e-03 | 4.3227e-03 | 1.1449e-02 | 1.3763e-02 | 8.5307e-03 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.8336e-05 | 3.8663e-06 | 5.3847e-06 | 1.6395e-06 | 1.1540e-04 | 1.6236e-04 | 5.1164e-05 |
| strassen | 1.8899e-05 | 1.0544e-05 | 9.6450e-06 | 6.3096e-05 | 1.6376e-04 | 1.3889e-04 | 6.7472e-05 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.27e-02 | 1.27e-02 | +0.0% | Alpha |
| relu | 1.03e-03 | 4.40e-03 | +76.5% | Alpha |
| gelu | 1.63e-03 | 4.59e-03 | +64.5% | Alpha |
| biased | 6.25e-04 | 4.32e-03 | +85.5% | Alpha |
| attention | 6.99e-03 | 1.14e-02 | +38.9% | Alpha |
| causal_transformer | 9.19e-03 | 1.38e-02 | +33.2% | Alpha |
| **Average** | | | **+49.8%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.83e-05 | 1.89e-05 | +3.0% | Alpha |
| relu | 3.87e-06 | 1.05e-05 | +63.3% | Alpha |
| gelu | 5.38e-06 | 9.65e-06 | +44.2% | Alpha |
| biased | 1.64e-06 | 6.31e-05 | +97.4% | Alpha |
| attention | 1.15e-04 | 1.64e-04 | +29.5% | Alpha |
| causal_transformer | 1.62e-04 | 1.39e-04 | -16.9% | Strassen |
| **Average** | | | **+36.8%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +49.8%)
- **StdDev:** Alpha wins 5/6 distributions (avg +36.8%)
