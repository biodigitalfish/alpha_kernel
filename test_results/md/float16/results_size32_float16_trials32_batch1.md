# Test Lab: Verification Results

**Generated:** 2026-01-14 10:01:07

## Parameters

- **Matrix Size:** 32×32
- **Batch Size:** 1
- **Trials:** 32
- **Total matrices per algorithm per distribution:** 32
## Mean Error by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 7.7630e-04 | 3.9275e-04 | 5.4679e-04 | 3.3182e-04 | 5.1151e-04 | 5.9350e-04 | 5.2545e-04 |
| strassen | 7.8006e-04 | 5.0903e-04 | 6.3705e-04 | 4.6785e-04 | 6.3508e-04 | 7.3625e-04 | 6.2755e-04 |

## StdDev by Algorithm × Distribution

| Algorithm | GAUSS | RELU | GELU | BIAS | ATTN | CAUSAL | AVG |
|---|---|---|---|---|---|---|---|
| alpha | 3.3140e-05 | 1.6430e-05 | 2.2567e-05 | 1.0126e-05 | 3.5299e-05 | 3.4044e-05 | 2.5268e-05 |
| strassen | 3.4416e-05 | 2.9243e-05 | 4.1081e-05 | 1.7172e-05 | 4.1062e-05 | 4.3119e-05 | 3.4349e-05 |

## Mean Error: Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 7.76e-04 | 7.80e-04 | +0.5% | Alpha |
| relu | 3.93e-04 | 5.09e-04 | +22.8% | Alpha |
| gelu | 5.47e-04 | 6.37e-04 | +14.2% | Alpha |
| biased | 3.32e-04 | 4.68e-04 | +29.1% | Alpha |
| attention | 5.12e-04 | 6.35e-04 | +19.5% | Alpha |
| causal_transformer | 5.94e-04 | 7.36e-04 | +19.4% | Alpha |
| **Average** | | | **+17.6%** | Alpha: 6/6 |

## StdDev (Stability): Alpha vs Strassen

| Distribution | Alpha | Strassen | Improvement | Winner |
|---|---|---|---|---|
| gaussian | 3.31e-05 | 3.44e-05 | +3.7% | Alpha |
| relu | 1.64e-05 | 2.92e-05 | +43.8% | Alpha |
| gelu | 2.26e-05 | 4.11e-05 | +45.1% | Alpha |
| biased | 1.01e-05 | 1.72e-05 | +41.0% | Alpha |
| attention | 3.53e-05 | 4.11e-05 | +14.0% | Alpha |
| causal_transformer | 3.40e-05 | 4.31e-05 | +21.0% | Alpha |
| **Average** | | | **+28.1%** | Alpha: 6/6 |

## Test Configuration

- **Algorithms tested:** Alpha vs Strassen
- **Distributions tested:** 6
- **Mean Error:** Alpha wins 6/6 distributions (avg +17.6%)
- **StdDev:** Alpha wins 6/6 distributions (avg +28.1%)
