# Matlab code for "A Novel Channel Model for Reconfigurable Intelligent Surfaces with Consideration of Polarization and Switch Impairments"
(c) 2023 De-Ming Chian and Chao-Kai Wen e-mail: icefreeman123@gmail.com and chaokai.wen@mail.nsysu.edu.tw

## Introduction
This repository contains the channel model for Reconfigurable Intelligent Surfaces (RIS) described in 
De-Ming Chian, Chao-Kai Wen, Chi-Hung Wu, Fu-Kang Wang, and Kai-Kit Wong, “A novel channel model for reconfigurable intelligent surfaces with consideration of polarization and switch impairments,” arXiv preprint arXiv:2304.03713, 2023. [Online]. Available: https://arxiv.org/abs/2304.03713.

The final version is published in D.-M. Chian, C.-K. Wen, C.-H. Wu, F.-K. Wang and K.-K. Wong, "A Novel Channel Model for Reconfigurable Intelligent Surfaces With Consideration of Polarization and Switch Impairments," IEEE Transactions on Antennas and Propagation, vol. 72, no. 4, pp. 3680-3695, April 2024. Available: https://ieeexplore.ieee.org/document/10462906.

## Requirements
- Matlab (R2022b)

## Hint
- If this code is applied in different cases, the transformation of polarization for the scattered and reflected waves and their tuning coefficients must be redefined. They are described in equations [22] and [23] of our article.

## File 1: RIS element (Consideration of polarization and switch impairments)

### Step1. Download the main script, functions, and data
- Main script: Main.m
- Functions: CalculateCC.m / CalculateReflect.m / CalculateScatter.m / <br>
&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; ChangeGrid.m / LinearInterpolate.m / <br>
&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; LoadParameter.m / RotateAntenna.m <br>
- Data: Pattern file (AntH2.xlsx / AntH3.xlsx / AntH4.xlsx / <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; AntV2.xlsx / AntV3.xlsx / AntV4.xlsx) <br>

### Step2. Run the main script

### Results
The following results are reproduced from Fig. 7(c) of our paper: <br>
![Image text](https://github.com/icefreeman123/FrequencyEstimation/blob/main/results.png)
