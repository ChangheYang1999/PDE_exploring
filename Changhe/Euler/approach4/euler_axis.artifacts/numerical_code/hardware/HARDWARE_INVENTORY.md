# Hardware inventory (real, recorded 2026-10-28T18:04:30Z)

## GPUs visible to the primary numerical search (CUDA_VISIBLE_DEVICES=2,3)
index, name, memory.total [MiB], driver_version
0, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08
1, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08
2, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08
3, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08
4, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08
5, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08
6, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08
7, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08

## CPU affinity of the primary numerical search shell
pid 966586's current affinity list: 41-46
nice level: 19
CPU(s):                                  96
Model name:                              Intel(R) Xeon(R) Platinum 8275CL CPU @ 3.00GHz
Thread(s) per core:                      2
Socket(s):                               2
NUMA node(s):                            2

## Memory
               total        used        free      shared  buff/cache   available
Mem:            1121          59         408          61         653         993

## Disk
/dev/nvme2n1    876G  748G  128G  86% (build volume)

## Kernel
6.12.95-124.187.amzn2023.x86_64

## Python stack
python 3.12.13
numpy 2.5.0
scipy 1.18.0
torch 2.13.0+cu130 cuda 13.0
mpmath 1.3.0
sympy 1.14.0

## fp64 GEMM benchmark one A100 (4096^3 x10)
11.4 TFLOPS measured 2026-10-28T18:01Z
## GPU update 2026-10-28T20:31:41Z: the primary numerical search keeps GPUs 0,1,2,3 (GPU 4 reassigned to the independent verifier, 5-7 to other teams).
