# Retained interval audits beyond the initial logarithmic prefix

Status: finite audits in progress. Every snapshot has its own result directory and is identified by a checkpoint hash. This topic extends the fixed earlier evidence in topic53 without overwriting it.

## Exact claim being checked

For each retained snapshot of the canonical rational logarithmic recursion with f_1=sin(theta), audit both density and stream coefficient balls. Decode their exact dyadic centers and radii independently. Report the largest radius relative to its column's largest center and relative to the column's sum of absolute centers. Count uncertain-zero columns explicitly. Compute interval enclosures for each retained column norm and for q! times that norm relative to the constant column.

A finite prefix is not a convergence theorem. These certificates are conditional on the correctness of the coefficient enclosures produced by the independently cross-checked recursion. The norm and comparison operations are independently recomputed here.

## Method and proof of the norm enclosure

A stored coefficient is a ball [m-r,m+r] with exact dyadic m and r>=0. Its absolute value lies in [max(0,|m|-r),|m|+r]. Summing these intervals gives an enclosure of the angular Wiener norm because the physical sine convention has norm equal to the sum of absolute amplitudes. Arb operations at640 bits implement this enclosure with outward rounding.

For a column, put S=sum|m|, T=sum r, M=max|m| and R=max r. If M>0, R/M is its maximum-center-scale relative radius, and T/S is its Wiener-scale relative radius. If M=0<R, neither relative precision is assigned a finite value. Such columns are reported as uncertain zero instead of being silently ignored.

For positive constant-column norm C_0 and another column norm C_q, compute log10(q! C_q/C_0) by outward-rounded logarithms. A strict interval comparison certifies its sign or a unique maximizing column. An overlap is left undecided. Individual coefficient relative radii are also inspected where the center is nonzero, but they are not substituted for the stated column-scale measures.

Only the selected coefficients needed to reproduce the most consequential comparisons are copied. All snapshot paths and source references are relative to the verification directory. The source checkpoint's hash identifies the complete prefix read during the audit.

## Completed snapshots, 2026-10-31T05:02:50Z

For delta=2/3 through N=210, the audit checks671997 density and681729 stream balls. The largest column-scale radius ratios are respectively below9.039e-60 and6.558e-58. Every individual nonzero coefficient also has relative radius below6.612e-57. There are no uncertain-zero columns or coefficients. Every existing nonconstant factorial-weighted column is smaller than the constant column in this finite prefix. At n=210, the largest logarithmic ratios log10(q! C_q/C_0) are -0.644974286992898968523145 for density and -0.378903485179940404703071 for stream, both uniquely attained at q=1. The saved interval strings specify the outward rounding of these displayed values. Actual audit time12.841854252386838 seconds.

For delta=4/9 through N=290, the audit checks571091 density and576965 stream balls. The largest column-scale radius ratios are below1.567e-29 and1.584e-26; all individual nonzero coefficient ratios are below3.267e-25. No uncertain-zero column or coefficient occurs. Every existing nonconstant factorial-weighted column is again smaller than the constant column. At n=290, the density and stream logarithmic ratios are -2.65891178416770515692095 and -2.63859947437201489272382, uniquely attained at q=1. Actual audit time11.255099205765873 seconds.

Each result directory retains the exact selected coefficient balls, the complete norm/comparison table, the input checkpoint hash, and the exact audit source used. The first snapshot's older field name `all_column_scale_radii_below_1e20` denotes a bound of10^(-20), as its retained source confirms. Later snapshots spell the exponent out unambiguously. This provenance is preserved rather than edited retrospectively.

## Update 2026-10-31T05:18:40Z: delta2/3 through240

The retained checkpoint `log_sin1_c3_p512_N240_20261031T051735Z` contains1005597 density and1018319 stream coefficient balls. Every column norm is resolved; no coefficient ball has uncertain zero center. The largest column-scale relative radius is below2.846e-44 and the largest individual relative radius below1.653e-42. Every nonconstant factorial-weighted column remains strictly below the constant column through240.

The density winner among positive log degrees first becomes interior at n235: q40, with log10 ratio in[-0.562316701502,-0.562316701501]. At n240 the density winner is q42, log10 ratio in[-0.235011466114,-0.235011466113]. These winners are unique by interval separation. The stream winner remains q1 through240; at240 its log10 ratio is in[-0.402060154264,-0.402060154263]. These finite statements do not decide the subsequent growth or convergence. Actual audit19.503650921862572 seconds.

## Positive-hump update, 2026-10-31T05:25:36Z

The245 snapshot certifies the first positive density factorial-column maximum at244,q40. Its logarithm to base10 lies in [0.0708636653818074655293940 +/- 8.81e-27]. At245,q42 the logarithm lies in [0.173493925022960554567504 +/- 3.99e-25]. All earlier density comparisons are strictly negative. The stream maximum first leaves q1 at242,q41 but remains negative through245. These are strict interval results, not rounded sign tests.

There are2153555 decoded coefficients. The largest individual relative radius is less than1.322e-40, and no zero-centered coefficient has nonzero radius. Checkpoint SHA256:a545410818481d0f614ad955e11152b2c0548c21e3f969c506bbb0f2a196bed4. The actual audit took21.725657150149345 seconds. This update changes the finite numerical picture only.

## Update 2026-10-31T05:36:24Z: order255 and interval growth diagnostics

V098 audits2429211 stored coefficient balls through255. The stream's first positive factorial-column maximum is248,q40 (.0503196074310668344323894 +/-9.86e-27 in log10); density first crossed at244. At255 the density and stream maxima are .890237408707184381408617 +/-4.85e-25 and .583958610496180036557523 +/-1.34e-25. Individual relative radii are below1.222e-36; no zero is unresolved. The checkpoint digest and exact selected balls are retained in verification/log_sin1_c3_p512_N255_20261031T053039Z/.

V099 reconstructs499 plain interval norms from their column logs and computes2745 fixed-deficit five-block increments. For L(n)=log10 of the plain norm, the same-residue increment is [L(n)-L(n-9)]/9. The three grouped one-step means average L(m)-L(m-1) for m in[n-8,n], separated by m modulo3. Their average equals the same-residue increment by telescoping, but none is individually that increment. All interval checks pass. Every result is finite-order evidence only.

## Update 2026-10-31T05:38:07Z: order260

V100 audits2575450 balls with checkpoint digest f7c91c519c8b4573aba3b9ecb9f8ba690abe5344c8713c247dfa9534c7d442a8. Both factorial-column maxima occur atq46: density1.35620895838413961947408 +/-8.56e-25 and stream1.00138076893503044656983 +/-2.26e-24. Individual relative radii are below2.063e-33, with no unresolved zeros. Actual audit24.743531393352896 seconds. Exact selected balls and interval growth diagnostics are retained in verification/log_sin1_c3_p512_N260_20261031T053559Z/.

## Update 2026-10-31T05:51:53Z: order 270 and stream-window correction

V111 checks 2,885,306 coefficient balls through 270. The checkpoint SHA256 is c6ee2c0f2995a2d007244f900b62ed5bd3dcd8dca1098f5c338ba612f9cc39da. All individual relative radii are below 3.312e-30 and no zero is unresolved. Both factorial-column winners are q=48 at 270, with logarithmic ratios 2.15495250102085277869210 +/-3.86e-24 for density and 1.70053123171108818377491 +/-4.04e-24 for stream. The selected coefficient balls and all column-norm intervals are retained in verification/log_sin1_c3_p512_N270_20261031T054922Z/.

V112 refutes two literal finite growth windows in theory version 10. For the precise statistic [L(n)-L(n-9)]/9, the first claimed interval [-.711,-.701] misses n=180,230,250; the later interval [-.689,-.667] misses n=263,264,265,268. The source excerpt, disjoint interval comparisons, and full growth diagnostics are retained with this snapshot. The qualitative late stream acceleration remains a valid finite observation.

## Update 2026-10-31T06:08:32Z: order280

V119 certifies3219104 coefficient balls with no unresolved zeros and individual relative radii below5.297e-26. Both factorial-column maxima occur atq50, with logarithmic ratios3.040434246627835 for density and2.290724037236659 for stream. All549 plain-norm reconstructions overlap. Exact intervals and the checkpoint hash are retained in verification/log_sin1_c3_p512_N280_20261031T060240Z/.
