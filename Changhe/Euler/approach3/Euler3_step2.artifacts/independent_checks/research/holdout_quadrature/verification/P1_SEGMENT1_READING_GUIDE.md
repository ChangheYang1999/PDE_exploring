# Reading the independent P1 segment-1 comparison

Written 2026-10-29T12:07:31.815139+00:00. Numerical verdict: V281 in verification record. Read the exact finite-quadrature statement in ../PROOF.md before this evidence guide.

The three current segment endpoints have been compared on identical sampled points and weights. The result is mixed. FREE has smaller maximum rho_u on several shell families than FIXED, but it does not improve every physical residual or every denominator-normalized metric. Both optimized endpoints have larger physical residual RMS in the small registered core ball than INITIAL. The complete comparison includes every scalar from both pressure levels, so conclusions need not rely on the table excerpt.

## States and evidence

The immutable input directories and hashes, actual parameters, bound source hashes, sampled core diagnostics and real evaluation times are in ../../../artifacts/P1_segment1_comparison_v1/comparison.json. That file has SHA256 d3e98040292d0b19e1e288281e9e19a87e6e9d0054d4c51fd04fc2ad22dc5443. The comparison checks identical complete radial, angular-direction and angular-weight byte hashes. It has697 passing provenance/geometry controls,224 summary rows, and116 domain rows across two levels. Each level therefore has58 domains. All three pair differences appear in the JSON and the adjacent summary.csv and shells.csv.

The driver computes the physical field from the saved coefficients using the independent Cartesian route and evaluates pressure through the independent full-space radial Green route. The compact audit checks retained grid arrays, selected witnesses, provenance and scalar identities. Full field arrays were not saved. A full-array recomputation requires rerunning the bound driver.

## Exact domains

The common reference radius is r_ref=0.4304351316933. It selects dyadic shell coverage and small-ball radii. It is not itself the radius of registered_core_ball. Every domain below is centered at the origin; no domain is centered at a certified vorticity maximum.

| Family | Domain count at each level | First outer radius | Last outer radius |
|---|---:|---:|---:|
| physical_common | 13 | 0.037499999999999999 | 153.59999999999999 |
| dyadic | 19 | 0.0078125 | 2048 |
| half_offset | 19 | 0.011048543456039806 | 2896.3093757400989 |
| registered_core_ball | 1 | 0.013451097865415625 | 0.013451097865415625 |
| unit_ball | 1 | 1 | 1 |
| unit_ball_composite | 1 | 1 | 1 |
| origin_ball | 1 | 0.0016813872331769531 | 0.0016813872331769531 |
| far_thin | 3 | 7757.4741174293304 | 496478.34351547714 |

The small registered_core_ball has radius r_ref/32=0.013451097865415625. The still smaller origin_ball has radius r_ref/256=0.0016813872331769531. A producer diagnostic over r<=0.4304351316933 is a different integral. V269 incorrectly attached that larger radius to the small-ball number; V281 corrects the statement without altering its saved numerical evidence.

The composite unit ball divides the radius interval at r_ref/32 and successive doublings, ending at1. Its96 radial nodes give a different rule from the separate12-node single-panel unit ball. The resulting difference is visible in the full table. Neither radial rule comes with an error enclosure.

## Quantities that must remain distinct

Write R=L+DU U+gradP and use the positive normalized volume quadrature from PROOF.md. The reported rho_u is the sampled RMS of R divided by the sum of the RMS norms of the five registered momentum terms. The reported sigma_u uses only the RMS norm of (1-c_l)U in the denominator. The residual/U ratio is the sampled RMS of R divided by that of U. Even the last ratio can fall when its denominator increases. Its dimensional numerator, residual_rms, is retained for every domain.

The weighted absolute residual multiplies residual_rms by (1+r_k)^(2 alpha+1), with alpha=(1-c_l)/c_l and r_k the domain's geometric reference radius. That weight changes with c_l. It equals1 for a ball whose inner radius is0. Thus the small-ball weighted absolute residual is its physical RMS, while general shell values must be read with their recorded parameter-dependent weights.

## Pressure comparison and limits

Pressure levels are20 radial nodes per panel with48x96 angular source points, and32 radial nodes with64x128 angular points. The phase parameter is0.417. The two source quadratures are evaluated independently of the held-out field grid, which has12 radial nodes per ordinary domain and42x84 angular points. Every pairwise residual-RMS change exceeds the sum of its two measured pressure-gradient refinement changes. The largest measured-change-to-difference ratio is0.0005793107052085993 in a far-thin domain. The finite norm inequality in PROOF.md explains the comparison between two computed quadratures; it supplies no bound against exact continuum pressure.

The evaluation is a partial momentum/pressure comparison. Vorticity-centered balls, independent vorticity residuals, origin Taylor data, pressure-Poisson defects, continuous extrema, energy, helicity, tail onset and stationarity remain separate conditions. No Tier candidate or exact Euler solution follows from these results.
