# Selected checkpoint: all four residuals

Date: 2026-10-23T08:19:19.271321+00:00. Exact checkpoint SHA256: 0b690cfd0b74062c9ebbdcb20bd8fbc6bf97346a7e2966d0d6cab690fd404284. Source evidence: `evidence/checkpoint-0b690cfd0b74062c-b401c544dd-d33806fc.json`, SHA256 d261290ce3b5da8d4af6e8417fd3c75b94c3bc59ab091cb4beedfdea0265858a.

These are the already evaluated values, transcribed without running a model again. The ten regions contain eight independent physical-volume shells, a Cartesian grid and an axis tube. The grid and tube are diagnostic measures, not additional volume-shell samples. Each relative RMS uses the denominator stored for that equation; vector residuals use Euclidean magnitude. Quantiles and maxima describe only the sampled points. No sampled maximum is an infinity-norm certificate. The complete unrounded values, denominator and measure are in SELECTED_RESIDUALS.tsv.

| Region | Equation | N | Relative RMS | Absolute RMS | Absolute q99 | Absolute q99.9 | Sampled maximum |
|---|---|---:|---:|---:|---:|---:|---:|
| shell_0_0.25 | momentum | 256 | 0.01001440962 | 0.004210379156 | 0.008123292244 | 0.00839293643 | 0.008419827312 |
| shell_0_0.25 | divergence | 256 | 1.571432682e-10 | 2.095315062e-10 | 7.947605574e-10 | 1.180057358e-09 | 1.241964309e-09 |
| shell_0_0.25 | vorticity | 256 | 0.09964184707 | 0.09602649274 | 0.1878266336 | 0.2162763201 | 0.2229440432 |
| shell_0_0.25 | pressure_poisson | 256 | 0.01622072945 | 0.05391159026 | 0.1546829065 | 0.176308392 | 0.1789154786 |
| shell_0.25_1 | momentum | 256 | 0.09896448288 | 0.02493077277 | 0.0464628953 | 0.2714187076 | 0.314812861 |
| shell_0.25_1 | divergence | 256 | 4.117520779e-11 | 3.382141765e-11 | 1.450446388e-10 | 2.279105056e-10 | 2.464177751e-10 |
| shell_0.25_1 | vorticity | 256 | 0.407857176 | 0.6711873648 | 2.107137343 | 7.356746496 | 7.967540875 |
| shell_0.25_1 | pressure_poisson | 256 | 0.3836998166 | 0.2276199617 | 0.4456861248 | 2.687426053 | 3.373390934 |
| shell_1_2 | momentum | 256 | 0.1482320076 | 0.01478206485 | 0.01994117584 | 0.1762380603 | 0.2252726331 |
| shell_1_2 | divergence | 256 | 7.308595622e-11 | 2.115270946e-11 | 1.100477588e-10 | 2.119810621e-10 | 2.407388316e-10 |
| shell_1_2 | vorticity | 256 | 0.5621740119 | 0.30771733 | 0.1911247227 | 3.80179462 | 4.834150771 |
| shell_1_2 | pressure_poisson | 256 | 0.8255789774 | 0.04819569591 | 0.06360311453 | 0.5886609082 | 0.7426605021 |
| shell_2_4 | momentum | 256 | 0.02902138479 | 0.0006590327459 | 0.001852896282 | 0.002285266998 | 0.002380245419 |
| shell_2_4 | divergence | 256 | 1.544418151e-10 | 5.598070676e-12 | 3.01798078e-11 | 5.597517474e-11 | 6.390142929e-11 |
| shell_2_4 | vorticity | 256 | 0.036485106 | 0.00260609755 | 0.00896244911 | 0.01740320431 | 0.01946088509 |
| shell_2_4 | pressure_poisson | 256 | 0.6224069043 | 0.0008915104061 | 0.003567942278 | 0.00561259686 | 0.005915304583 |
| shell_4_8 | momentum | 256 | 0.02230775908 | 0.0001859811679 | 0.0004926009728 | 0.0007247689746 | 0.0007818248343 |
| shell_4_8 | divergence | 256 | 1.080240751e-10 | 5.854869236e-13 | 2.29868328e-12 | 5.31456005e-12 | 5.344998749e-12 |
| shell_4_8 | vorticity | 256 | 0.01958298328 | 0.0002044674124 | 0.0008492616589 | 0.001177555811 | 0.001181073735 |
| shell_4_8 | pressure_poisson | 256 | 0.8370947512 | 5.011064084e-05 | 0.0002263180775 | 0.0003679040412 | 0.0003841765176 |
| shell_8_16 | momentum | 256 | 0.01194552365 | 3.983139913e-05 | 0.0001369538929 | 0.0002203198992 | 0.0002387891762 |
| shell_8_16 | divergence | 256 | 2.156108664e-10 | 2.726340151e-13 | 5.834091673e-13 | 3.1930161e-12 | 4.006727133e-12 |
| shell_8_16 | vorticity | 256 | 0.005900520349 | 1.467307054e-05 | 5.127134681e-05 | 0.0001121709781 | 0.0001279183397 |
| shell_8_16 | pressure_poisson | 256 | 0.8731159327 | 2.195363133e-06 | 9.722280479e-06 | 1.546865385e-05 | 1.71044843e-05 |
| shell_16_32 | momentum | 256 | 0.003790502421 | 5.031440124e-06 | 1.44006559e-05 | 2.004407413e-05 | 2.027890112e-05 |
| shell_16_32 | divergence | 256 | 7.662960464e-11 | 1.564909949e-14 | 7.620942045e-14 | 1.237770202e-13 | 1.335559538e-13 |
| shell_16_32 | vorticity | 256 | 0.001806076638 | 7.112800392e-07 | 2.697672192e-06 | 3.919864465e-06 | 4.083219671e-06 |
| shell_16_32 | pressure_poisson | 256 | 0.8106587583 | 5.867256938e-08 | 2.792798304e-07 | 3.190588127e-07 | 3.242592625e-07 |
| shell_32_64 | momentum | 256 | 0.001099420702 | 5.704412528e-07 | 1.737039542e-06 | 2.116548095e-06 | 2.18491666e-06 |
| shell_32_64 | divergence | 256 | 8.461813423e-11 | 4.090352718e-15 | 1.75667137e-14 | 3.512447303e-14 | 3.947503199e-14 |
| shell_32_64 | vorticity | 256 | 0.0003751745148 | 3.543832076e-08 | 1.560050624e-07 | 2.192555993e-07 | 2.347620715e-07 |
| shell_32_64 | pressure_poisson | 256 | 0.8300995318 | 2.065873257e-09 | 8.989020617e-09 | 9.108362228e-09 | 9.127376802e-09 |
| cartesian_grid_core | momentum | 1331 | 0.09095126552 | 0.01643029664 | 0.05555616044 | 0.1801804415 | 0.1859550082 |
| cartesian_grid_core | divergence | 1331 | 1.062405264e-10 | 6.158499651e-11 | 2.987360359e-10 | 8.86126077e-10 | 1.045964815e-09 |
| cartesian_grid_core | vorticity | 1331 | 0.4227802577 | 0.5168384748 | 1.798168436 | 6.591257861 | 6.631958022 |
| cartesian_grid_core | pressure_poisson | 1331 | 0.3204474829 | 0.1468761202 | 0.3006470211 | 2.485014412 | 3.041637994 |
| axis_line | momentum | 129 | 0.01628172927 | 0.001523201685 | 0.005618174468 | 0.007412573709 | 0.007603084378 |
| axis_line | divergence | 129 | 2.923013911e-10 | 1.137755933e-10 | 3.57455372e-10 | 1.106440167e-09 | 1.197956068e-09 |
| axis_line | vorticity | 129 | 0.1105235119 | 0.01888629678 | 0.08129033676 | 0.1323876512 | 0.1388986886 |
| axis_line | pressure_poisson | 129 | 0.02149277297 | 0.02199816056 | 0.09332293717 | 0.1600693451 | 0.1697532603 |

The checkpoint fails momentum and nonlinear-tail screening. Small divergence is an implementation consistency result and does not compensate for the momentum, vorticity or pressure Poisson errors. This table supplies the absolute statistics omitted from the compact lead report; it changes no frozen numerical value.
