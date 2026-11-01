# Independent verification of the completed tuned first-root prefix

Status: CONFIRMED finite audit through order401; V292. This is not a new infinite convergence theorem.

## Exact objects and scope

Set c=3, delta=2/3 and p_n=1-2n/3. Let b be the smaller real root of

    176703765525000 b^6 -222533688701250 b^5 +96180432855375 b^4
    -20675598499400 b^3 +2783057141280 b^2 -243275209320 b +10532171936.

Let f_1=sin(theta)+b sin(3theta), and use the unique compatible pure density and stream series of119. At each n=3k>=6 the free coefficient of sin((2k-2)theta) in g_n is determined by compatibility at n+3. The source1024-bit run ends at a resonance whose last free stream coefficient is still provisional. The completed prefix ends one order earlier. Its lower resonance constants have been fixed by the affine lookahead. The source harmonic table is retained and this condition is checked explicitly.

The earlier audit128 established enclosure validity and independently checked every Cartesian coefficient equation through150. This audit requires byte-identical packed density and stream coefficients through150, retains the new exact dyadic coefficients above150, and checks every new Cartesian equation. A reconstruction recipe joins that base prefix and the extension and records a hash of the resulting selected state. The original complete checkpoint is identified by hash. All norm and root data in this audit concern this particular finite prefix and unit amplitude.

## Complete argument for the finite certificates

Represent an angular sine polynomial by the real signed Laurent polynomial sum_m a_m(z^m-z^(-m))/2. Its physical value on the unit circle is minus i times this polynomial. On a radial monomial r^q z^m define

    X = ((q+m) z^(m-1)+(q-m) z^(m+1))/2,
    Y = ((q+m) z^(m-1)-(q-m) z^(m+1))/2.

Physical x and y differentiation correspond to X and iY respectively. Direct Cartesian differentiation gives the two coefficient equations

    -XX g_n+YY g_n=X f_n,
    2(n-1) f_n=sum_(i+j=n)(Xg_i Yf_j-Yg_i Xf_j).

These are evaluated using dense interval Laurent products, independently of the source sine-product code. Every coefficient residual must contain zero. At n=3k>=6 the density coefficient at frequency2k-3 must contain zero, as required by the exact compatibility theorem. Every other nonzero interval is tested for separation from zero; an unresolved coefficient is recorded rather than silently dropped.

The source enclosure induction is the one proved in128: an independently isolated exact root belongs to the starting b interval; the interval recurrence and ordinary inverse enclose their exact values; the exact affine block theorem gives H=-R/sigma, with the denominator interval separated from zero; interval affine corrections enclose the tuned coefficients. The new source code must agree with the audited version. The Cartesian residual checks provide independent consistency evidence. Containment of zero alone would not validate an arbitrary source algorithm.

For each order the sum of coefficient absolute-value intervals encloses the angular coefficient l1 norm. Positive interval logarithms and exponentials therefore enclose its nth root. Norm-relative radii and individual coefficient-relative radii are separately recorded. A floating least-squares fit to the norm midpoints is only an empirical description of these finite data. No fitted growth constant, sign pattern or finite root test is asserted at uncomputed orders, and no smaller infinite convergence radius follows.

## Dependencies and evidence

Dependencies are119 for exact tuning and compatibility,128 for the independent lower prefix and source induction, and elementary interval arithmetic. The verification directory retains the exact extension archive, reconstruction recipe, source code and source harmonic table, interval outputs, progress records and actual elapsed time. The run uses no formal proof assistant.

## Completed audit

The run finished at2026-10-31T11:27:30Z after2067.444131284021 actual seconds. All555463 new Poisson and554961 new nonlinear coefficient residuals contain zero, covering69025 ordered products and83 new compatibility projections. The45450 lower coefficients are byte-identical to the independently checked order150 prefix. All322805 individual source intervals through401 were inspected;533 are structural zeros and every other interval excludes zero. The largest individual relative radius is below3.449e-78, and the normalized nonlinear residual bound is2.60e-78.

At401 the density and stream norm roots are respectively0.25392162878449157513 and0.25228808059966923154. The final fixed harmonic is H399>0. Order402 is excluded because its free harmonic was not fixed in the source checkpoint. The selected-state reconstruction hash and source hash are retained in verification/reconstruction.json. These finite bounds do not improve the proved infinite convergence radius.
