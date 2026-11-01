# Later coefficients of the thirty-term edge truncation

Status: CONFIRMED finite interval audit through order 300, V338. No infinite growth law is asserted.

## Statement and hypotheses

Set delta = 2/3, c = 3, and F_1(theta) = sin(theta). Let t = log r.
Generate the canonical polynomial-in-t density and stream coefficients,
except that at order n retain only the ordered nonlinear pairs i+j=n
with min(i,j) <= 30. Set the constant of each newly resonant stream
harmonic to zero. Denote this modified sequence by F_n and G_n, and
its sums of absolute sine coefficients over all t columns by M_n and N_n.
The full canonical sequence retains every ordered pair.

This audit compares these two sequences at a finite range of orders,
checks every Poisson coefficient at the selected last order, and checks
its nonlinear equation using all sixty retained ordered pairs. It also
compares the modified sequence with its earlier floating approximation.
The last order and every checked range are recorded in the certificate.
No conclusion at an uncomputed order is asserted.

## Interval norms and provenance

Each saved coefficient has an exact dyadic midpoint and radius. Decode
both without converting through binary64. Summing their absolute-value
intervals encloses the exact coefficient norm. Subtracting logarithms
of positive norm intervals encloses the logarithmic difference between
the modified and full sequences. The full-sequence intervals are those
already checked in topic 82.

Before using the later checkpoint, compare every coefficient-array hash
used by topic 161 with that checkpoint. Require the same exact leading
datum, precision, exponent, truncation parameter and absence of a radius
reset. This verifies the common prefix. The audited interval recurrence
construction supplies the exact-sequence provenance; interval residuals
containing zero are additional consistency checks, not a replacement for
that construction.

## Differential identities

At order n put P = 2-2n/3. For logarithmic degree q and positive even
frequency m, the Poisson equation is

    (m^2-P^2) G[q,m] - 2P(q+1) G[q+1,m]
      - (q+1)(q+2) G[q+2,m]
    = ((P-m) F[q,m-1] + (q+1) F[q+1,m-1]
       + (P+m) F[q,m+1] + (q+1) F[q+1,m+1])/2.

Unrepresented coefficients are zero. The identity follows by applying
the polar Laplacian to r^P G(t,theta) and the x derivative to
r^(P-1) F(t,theta).

For the nonlinear identity, represent sine fields by their antisymmetric
signed Laurent coefficients. The Cartesian operators on r^p A(t,z) are

    X A = sum_m [((p+m)A_m+A'_m) z^(m-1)
                 +((p-m)A_m+A'_m) z^(m+1)]/2,
    Y A = sum_m [((p+m)A_m+A'_m) z^(m-1)
                 -((p-m)A_m+A'_m) z^(m+1)]/2.

The phase convention is the one derived in topics 01 and 21. It gives
nonlinear forcing (XG_i)(YF_j)-(YG_i)(XF_j). Its sum over all admissible
pairs must equal 2(n-1)F_n-3 partial_t F_n. Full signed polynomial
multiplication checks this identity independently of the source's
angular product formulas.

The bivariate products may be encoded into one polynomial: place angular
offset u and logarithmic degree q at index u+stride*q. Choose the stride
strictly larger than the sum of the two input angular widths. Then every
output index has a unique decomposition, so ordinary polynomial
multiplication reproduces the bivariate coefficients without carry.

## Scope and retained evidence

A positive interval difference proves a finite departure of the modified
recurrence from the full recurrence. A finite fitted slope or agreement
with a floating computation proves no infinite growth law. Topic 111's
separate Gevrey estimate for edge truncations is not improved by this audit.

Freeze the selected last coefficient arrays, the source fingerprints,
all dependent array hashes and the exact norm enclosures. Other dependent
arrays may be recovered from a later source checkpoint only after their
hashes agree. The storage constraint precludes another full archive.

## Completed check at 2026-10-31T13:18:07+00:00

All142 prior array hashes agree. At order300, all30100 Poisson coefficients and119097 Cartesian coefficients from60 ordered products pass. The norm-relative radii are below8.5e-21. The edge-minus-full logarithmic norm differences are1.0784167885784676645 and2.47012930666855613decades, while the old floating results exceed the ball results by2.69671821381974648849 and2.81990003694947898555decades. The exact dyadic norm data, selected coefficient archive and complete dependency hashes are retained in verification/checks.json. Actual audit time331.0735558937304seconds.
