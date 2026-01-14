# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:34

## Parameters

- **Matrix Size:** 128×128
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 2.5355e-02 | 6.6102e-03 | 1.0862e-02 | 4.1009e-03 | 1.4798e-02 | 1.8373e-02 | 1.3350e-02 |
| strassen | 2.5307e-02 | 1.2753e-02 | 1.5751e-02 | 1.1860e-02 | 2.1381e-02 | 2.6017e-02 | 1.8845e-02 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 4.8316e-04 | 1.2196e-04 | 2.5242e-04 | 4.7593e-05 | 7.9208e-04 | 9.4411e-04 | 4.4022e-04 |
| strassen | 3.7192e-04 | 3.5878e-04 | 4.5660e-04 | 3.3705e-04 | 7.6678e-04 | 9.9821e-04 | 5.4822e-04 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 2.54e-02 | 2.53e-02 | -0.2% | Strassen |
| relu | 6.61e-03 | 1.28e-02 | +48.2% | Alpha |
| gelu | 1.09e-02 | 1.58e-02 | +31.0% | Alpha |
| biased | 4.10e-03 | 1.19e-02 | +65.4% | Alpha |
| attention | 1.48e-02 | 2.14e-02 | +30.8% | Alpha |
| causal_transformer | 1.84e-02 | 2.60e-02 | +29.4% | Alpha |
| **Average** | | | **+34.1%** | Alpha: 5/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 4.83e-04 | 3.72e-04 | -29.9% | Strassen |
| relu | 1.22e-04 | 3.59e-04 | +66.0% | Alpha |
| gelu | 2.52e-04 | 4.57e-04 | +44.7% | Alpha |
| biased | 4.76e-05 | 3.37e-04 | +85.9% | Alpha |
| attention | 7.92e-04 | 7.67e-04 | -3.3% | Strassen |
| causal_transformer | 9.44e-04 | 9.98e-04 | +5.4% | Alpha |
| **Average** | | | **+28.1%** | Alpha: 4/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 5/6 distributions (avg +34.1%)
- **StdDev:** Alpha wins 4/6 distributions (avg +28.1%)
