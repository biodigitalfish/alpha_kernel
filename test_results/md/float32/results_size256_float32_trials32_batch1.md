# Test Lab: Verification Results

**Generated:** 2026-01-14 10:02:01

## Parameters

- **Matrix Size:** 256×256
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.2080e-06 | 2.3318e-07 | 3.9200e-07 | 1.0949e-07 | 8.1970e-07 | 9.9311e-07 | 6.2592e-07 |
| strassen | 1.2106e-06 | 5.4254e-07 | 6.3870e-07 | 4.9950e-07 | 1.2566e-06 | 1.4617e-06 | 9.3495e-07 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 1.2412e-08 | 3.7240e-09 | 5.8708e-09 | 1.2940e-09 | 2.8831e-08 | 4.1120e-08 | 1.5542e-08 |
| strassen | 1.2104e-08 | 1.3163e-08 | 1.2400e-08 | 1.0782e-08 | 6.0431e-08 | 4.7858e-08 | 2.6123e-08 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.21e-06 | 1.21e-06 | +0.2% | Alpha |
| relu | 2.33e-07 | 5.43e-07 | +57.0% | Alpha |
| gelu | 3.92e-07 | 6.39e-07 | +38.6% | Alpha |
| biased | 1.09e-07 | 4.99e-07 | +78.1% | Alpha |
| attention | 8.20e-07 | 1.26e-06 | +34.8% | Alpha |
| causal_transformer | 9.93e-07 | 1.46e-06 | +32.1% | Alpha |
| **Average** | | | **+40.1%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 1.24e-08 | 1.21e-08 | -2.5% | Strassen |
| relu | 3.72e-09 | 1.32e-08 | +71.7% | Alpha |
| gelu | 5.87e-09 | 1.24e-08 | +52.7% | Alpha |
| biased | 1.29e-09 | 1.08e-08 | +88.0% | Alpha |
| attention | 2.88e-08 | 6.04e-08 | +52.3% | Alpha |
| causal_transformer | 4.11e-08 | 4.79e-08 | +14.1% | Alpha |
| **Average** | | | **+46.0%** | Alpha: 5/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +40.1%)
- **StdDev:** Alpha wins 5/6 distributions (avg +46.0%)
