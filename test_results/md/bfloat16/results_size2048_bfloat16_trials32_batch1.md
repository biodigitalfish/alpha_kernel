# Test Lab: Verification Results

**Generated:** 2026-01-14 10:03:19

## Parameters

- **Matrix Size:** 2048×2048
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.0125e-01 | 8.2752e-03 | 1.3043e-02 | 5.0053e-03 | 5.4849e-02 | 7.2714e-02 | 4.2522e-02 |
| strassen | 1.0125e-01 | 3.5220e-02 | 3.6719e-02 | 3.4531e-02 | 8.8402e-02 | 1.0876e-01 | 6.7481e-02 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.6138e-04 | 3.3070e-05 | 4.1657e-05 | 1.4302e-05 | 8.9643e-04 | 1.2761e-03 | 4.0383e-04 |
| strassen | 1.5567e-04 | 7.8231e-05 | 8.8210e-05 | 4.8852e-04 | 1.2454e-03 | 1.1510e-03 | 5.3450e-04 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.01e-01 | 1.01e-01 | +0.0% | Alpha |
| relu | 8.28e-03 | 3.52e-02 | +76.5% | Alpha |
| gelu | 1.30e-02 | 3.67e-02 | +64.5% | Alpha |
| biased | 5.01e-03 | 3.45e-02 | +85.5% | Alpha |
| attention | 5.48e-02 | 8.84e-02 | +38.0% | Alpha |
| causal_transformer | 7.27e-02 | 1.09e-01 | +33.1% | Alpha |
| **Average** | | | **+49.6%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.61e-04 | 1.56e-04 | -3.7% | Strassen |
| relu | 3.31e-05 | 7.82e-05 | +57.7% | Alpha |
| gelu | 4.17e-05 | 8.82e-05 | +52.8% | Alpha |
| biased | 1.43e-05 | 4.89e-04 | +97.1% | Alpha |
| attention | 8.96e-04 | 1.25e-03 | +28.0% | Alpha |
| causal_transformer | 1.28e-03 | 1.15e-03 | -10.9% | Strassen |
| **Average** | | | **+36.8%** | Alpha: 4/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +49.6%)
- **StdDev:** Alpha wins 4/6 distributions (avg +36.8%)
