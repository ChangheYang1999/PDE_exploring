# Reading the independent P2 segment-1 comparison

Written 2026-10-29T13:13:07.602574+00:00. Numerical verdict V304 in verification record. Read ../PROOF.md for the exact finite-quadrature statement.

The comparison gives no broad FREE advantage at these segment-one end-current states. FREE has slightly larger rho_u maxima than FIXED on all eight reported domain families. Both optimized states improve some quantities against INITIAL and worsen others. For example, the small-ball momentum RMS decreases, while the dyadic weighted absolute maximum increases. These are observations of the actual endpoints, whose optimization durations and accepted-iteration counts differ. They are not a matched-wall or matched-iteration test.

The immutable coefficients, actual parameters and source hashes are in ../../../artifacts/P2_segment1_comparison_v1/comparison.json, SHA256 665e5a0f865ccfa47704ae666c59d24de3603f5acb0aad7313319ac199fc8600. All 699 comparison controls pass, including identical full radial and angular grid hashes. There are 224 summary rows and 116 domain rows over two pressure levels. All three pair differences and all scalar metrics are retained in the JSON and adjacent CSV files. Each state's compact audit has 3100 checks.

The independent Cartesian field and full-space radial Green pressure calculation uses seed 2026102902, a common reference R0=0.3 and reference core radius 0.14364049210478602. The field grid has 12 radial nodes per ordinary domain and 42 by 84 angular nodes. Pressure uses 20 and 32 radial nodes per source panel with 48 by 96 and 64 by 128 angular nodes; phase=0.593. The leading main angular degree is six throughout.

| Finest-level metric | INITIAL | FIXED | FREE |
|---|---:|---:|---:|
| dyadic rho_u max | 0.0522678986361 | 0.052336953883 | 0.0523874363095 |
| dyadic weighted absolute max | 1.92101371034 | 1.92321831442 | 1.92536136341 |
| half_offset rho_u max | 0.0717226561181 | 0.0692907098963 | 0.0694129318172 |
| half_offset weighted absolute max | 1.82629000674 | 1.89774072195 | 1.89893291383 |
| physical_common rho_u max | 0.0649478099003 | 0.0642718365393 | 0.0643200318936 |
| physical_common weighted absolute max | 1.71400122088 | 1.79343942536 | 1.79192578452 |
| registered_core_ball rho_u max | 0.00165175754937 | 0.00149722486857 | 0.00151170759655 |
| registered_core_ball weighted absolute max | 0.103607113798 | 0.0941605380618 | 0.0951464030034 |
| unit_ball rho_u max | 0.0631321085592 | 0.0603630047259 | 0.0605436878776 |
| unit_ball weighted absolute max | 0.178308929398 | 0.175411076267 | 0.175610068401 |
| unit_ball_composite rho_u max | 0.0384207328768 | 0.0382577543344 | 0.0382924723909 |
| unit_ball_composite weighted absolute max | 0.159764348885 | 0.161382069768 | 0.16138299476 |
| origin_ball rho_u max | 0.00156933057787 | 0.00136195794836 | 0.00137646900507 |
| origin_ball weighted absolute max | 0.098328170263 | 0.0855598692479 | 0.0865399888368 |
| far_thin rho_u max | 2.85331993303e-08 | 7.36171296086e-09 | 7.68556073405e-09 |
| far_thin weighted absolute max | 0.368464078049 | 0.0956379696273 | 0.097465775238 |

The origin-centered registered core ball has radius reference_core/32=0.004488765378274563. The origin ball has radius reference_core/256=0.0005610956722843204. These are not balls centered at a certified vorticity maximum. For both balls the geometric reference radius is zero, so the weighted absolute residual equals the physical residual RMS. The unit-ball composite uses 108 radial nodes across nine panels; the separately reported single-panel unit ball has only 12 radial nodes. Their different readings show that radial sampling matters.

The weighted absolute shell residual uses (1+r_k)^(2 alpha+1), alpha=(1-c_l)/c_l. This weight changes in FREE, whose parameters are c_l=0.4504018709805433 and omega=0.2992409300010186; INITIAL and FIXED use c_l=0.45, omega=0.3. The JSON also retains unweighted residual RMS, velocity RMS and their ratio on the common domains. A smaller normalized ratio alone does not establish a smaller physical residual.

All pairwise residual-RMS differences exceed the sum of their measured pressure-gradient refinement changes; the largest change-to-difference ratio is 0.0001826017332810561 on far_thin index 2 for FREE versus FIXED. For the retained family summary metrics the largest corresponding ratio is 4.421299619678618e-5. These two computed quadrature levels give no enclosure of exact continuum pressure or of continuous extrema.

The finite states have sampled dyadic rho_u maxima about 0.0523 and half-offset maxima about 0.069 to 0.072, above the necessary 0.01 shell threshold. No Tier candidate, stationarity, basis-resolution floor or exact Euler solution follows. Vorticity, origin Taylor data, pressure-Poisson defects, energy, helicity, tail onset and core-centered diagnostics remain separate checks. The independent origin calculation V286 already excludes zero for the canonical origin vorticity residual of both P2 endpoints, within that calculation's exact finite-field scope.
