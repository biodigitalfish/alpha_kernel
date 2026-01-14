# Test Lab: Verification Results

**Generated:** 2026-01-14 10:04:26

## Parameters

- **Matrix Size:** 2048×2048
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 4.8464e-06 | 3.6713e-07 | 6.1776e-07 | 1.7957e-07 | 3.1422e-06 | 4.0861e-06 | 2.2065e-06 |
| strassen | 4.8476e-06 | 2.0089e-06 | 2.0857e-06 | 1.7722e-06 | 5.0536e-06 | 6.2346e-06 | 3.6671e-06 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 7.3192e-09 | 2.9906e-09 | 3.6854e-09 | 8.7252e-10 | 5.9956e-08 | 8.2255e-08 | 2.6180e-08 |
| strassen | 1.0182e-08 | 9.3754e-09 | 1.3752e-08 | 7.5608e-09 | 9.5673e-08 | 7.0133e-08 | 3.4446e-08 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 4.85e-06 | 4.85e-06 | +0.0% | Alpha |
| relu | 3.67e-07 | 2.01e-06 | +81.7% | Alpha |
| gelu | 6.18e-07 | 2.09e-06 | +70.4% | Alpha |
| biased | 1.80e-07 | 1.77e-06 | +89.9% | Alpha |
| attention | 3.14e-06 | 5.05e-06 | +37.8% | Alpha |
| causal_transformer | 4.09e-06 | 6.23e-06 | +34.5% | Alpha |
| **Average** | | | **+52.4%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 7.32e-09 | 1.02e-08 | +28.1% | Alpha |
| relu | 2.99e-09 | 9.38e-09 | +68.1% | Alpha |
| gelu | 3.69e-09 | 1.38e-08 | +73.2% | Alpha |
| biased | 8.73e-10 | 7.56e-09 | +88.5% | Alpha |
| attention | 6.00e-08 | 9.57e-08 | +37.3% | Alpha |
| causal_transformer | 8.23e-08 | 7.01e-08 | -17.3% | Strassen |
| **Average** | | | **+46.3%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +52.4%)
- **StdDev:** Alpha wins 5/6 distributions (avg +46.3%)
