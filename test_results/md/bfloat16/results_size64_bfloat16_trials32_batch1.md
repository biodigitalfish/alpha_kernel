# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:18

## Parameters

- **Matrix Size:** 64×64
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.2631e-02 | 4.5977e-03 | 7.1067e-03 | 3.3567e-03 | 7.4601e-03 | 9.1355e-03 | 7.3814e-03 |
| strassen | 1.2712e-02 | 7.4206e-03 | 9.2422e-03 | 6.8992e-03 | 1.0242e-02 | 1.2223e-02 | 9.7898e-03 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 3.2651e-04 | 1.1459e-04 | 1.9424e-04 | 5.5777e-05 | 3.6322e-04 | 4.9653e-04 | 2.5848e-04 |
| strassen | 3.4927e-04 | 2.9741e-04 | 3.6416e-04 | 2.5895e-04 | 6.9600e-04 | 4.6643e-04 | 4.0537e-04 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.26e-02 | 1.27e-02 | +0.6% | Alpha |
| relu | 4.60e-03 | 7.42e-03 | +38.0% | Alpha |
| gelu | 7.11e-03 | 9.24e-03 | +23.1% | Alpha |
| biased | 3.36e-03 | 6.90e-03 | +51.3% | Alpha |
| attention | 7.46e-03 | 1.02e-02 | +27.2% | Alpha |
| causal_transformer | 9.14e-03 | 1.22e-02 | +25.3% | Alpha |
| **Average** | | | **+27.6%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 3.27e-04 | 3.49e-04 | +6.5% | Alpha |
| relu | 1.15e-04 | 2.97e-04 | +61.5% | Alpha |
| gelu | 1.94e-04 | 3.64e-04 | +46.7% | Alpha |
| biased | 5.58e-05 | 2.59e-04 | +78.5% | Alpha |
| attention | 3.63e-04 | 6.96e-04 | +47.8% | Alpha |
| causal_transformer | 4.97e-04 | 4.66e-04 | -6.5% | Strassen |
| **Average** | | | **+39.1%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +27.6%)
- **StdDev:** Alpha wins 5/6 distributions (avg +39.1%)
