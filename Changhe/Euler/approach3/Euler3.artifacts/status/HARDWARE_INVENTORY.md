# Hardware and software inventory (captured 2026-10-24T17:21:56Z)

## GPUs visible to this lane (CUDA_VISIBLE_DEVICES=0,1,4,5)
index, name, memory.total [MiB], driver_version, uuid
0, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08, GPU-be5b4b96-0f5d-350b-93a4-ffc95b88d0af
1, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08, GPU-3fdf3f09-36af-6c79-d6df-85c02d06dc87
2, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08, GPU-bc19b8cd-df71-f325-123b-f3e2db381af7
3, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08, GPU-adc24e3c-3d4b-4dad-aebb-355cbb974602
4, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08, GPU-17842559-568c-feb6-de09-c62a8ca2ac5f
5, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08, GPU-b21218d8-cb89-c501-98a7-9f4d91477290
6, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08, GPU-eada0581-e39e-ce69-1bf8-8caa3e270128
7, NVIDIA A100-SXM4-80GB, 81920 MiB, 580.167.08, GPU-0d9e1063-68d4-3595-4da4-807ff85e7da2

## CPU affinity
pid 1408958's current affinity list: 0,2-4,10,14,16,18,22,23,49,53
CPU(s):                                  96
Model name:                              Intel(R) Xeon(R) Platinum 8275CL CPU @ 3.00GHz
Thread(s) per core:                      2
NUMA node(s):                            2
NUMA node0 CPU(s):                       0-23,48-71
NUMA node1 CPU(s):                       24-47,72-95

## Memory
               total        used        free      shared  buff/cache   available
Mem:            1121         126         150          76         845         912
Swap:              0           0           0

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme2n1    876G  736G  140G  85% <shared volume>

## Software
Python 3.9.25
torch 2.8.0+cu128 cuda 12.8 cudnn 91002
numpy 2.0.2 scipy 1.13.1 sympy 1.14.0 mpmath 1.3.0 numba 0.60.0
| NVIDIA-SMI 580.167.08             Driver Version: 580.167.08     CUDA Version: 13.0     |

## Other jobs on the box at start
pid, used_gpu_memory [MiB], gpu_uuid
1400241, 658 MiB, GPU-eada0581-e39e-ce69-1bf8-8caa3e270128
1400242, 658 MiB, GPU-0d9e1063-68d4-3595-4da4-807ff85e7da2
 17:22:01 up 22 days, 23:55,  0 users,  load average: 47.72, 43.71, 41.39
