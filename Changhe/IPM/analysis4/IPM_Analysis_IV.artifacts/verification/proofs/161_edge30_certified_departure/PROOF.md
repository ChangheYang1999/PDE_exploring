# Finite certification of the K = 30 departure

Status: finite interval audit CONFIRMED, V310. No convergence or divergence theorem is claimed.

## Objects and claim

Fix delta=2/3, c=3 and F1=sin(theta). Use the logarithmic recurrence
of102, retaining exactly the ordered pairs i+j=n with min(i,j)<=30.
Choose zero constant coefficient in each resonant stream channel.
The resulting coefficients are denoted F_n and G_n. Let M_n and N_n
be the sums of absolute sine coefficients over all logarithmic columns.

This modified recurrence agrees with the full recurrence through61,
but need not agree afterwards. The finite claim to test is that its
stream norm differs from the full recurrence by the reported positive
logarithmic gaps at orders240,245 and250, while its density norm remains
close on that scale. The comparison is between two different recurrences.
It is not a test that the full recurrence has diverged.

## Interval and differential checks

Decode the source's exact dyadic midpoint and radius without conversion
to binary64. Sum absolute coefficient intervals to enclose M_n and N_n.
For every selected order, check the differential Poisson identity at
each logarithmic degree q and positive even frequency m. With
P_n=2-2n/3, its coefficient equation is

    (m^2-P_n^2)G[q,m] - 2P_n(q+1)G[q+1,m]
      - (q+1)(q+2)G[q+2,m]
    = ((P_n-m)F[q,m-1] + (q+1)F[q+1,m-1]
       + (P_n+m)F[q,m+1] + (q+1)F[q+1,m+1])/2.

Every unrepresented coefficient is zero. This follows directly from
minus the polar Laplacian applied to r^P G(log r,theta) and the
Cartesian x derivative applied to r^(P-1) F(log r,theta).

For a nonlinear check at order250, represent each sine field by its
antisymmetric signed Laurent coefficients. For a field r^p A(t,z),
use the Cartesian operators

    X A = ((p+m)A_m + A'_m) z^(m-1)/2
          + ((p-m)A_m + A'_m) z^(m+1)/2,
    Y A = ((p+m)A_m + A'_m) z^(m-1)/2
          - ((p-m)A_m + A'_m) z^(m+1)/2.

Here Y includes the formal phase convention from01 and21. With that
convention the real sine forcing is represented by
(XG_i)(YF_j)-(YG_i)(XF_j). Multiply the signed Laurent polynomials and
the t polynomials by independent Cartesian arithmetic, enumerate the
60 admissible ordered pairs, and compare with
2(n-1)F_n-3 partial_t F_n.

Packing a bivariate polynomial into one polynomial is valid when the
stride exceeds the full output angular degree. The coefficient with
angular offset u and logarithmic degree q is stored at u+stride*q.
The sum of two input angular offsets is strictly below the stride, so
no angular coefficient carries into an adjacent logarithmic degree.
The product therefore reproduces ordinary bivariate convolution exactly.

## Interpretation of certification

An interval residual containing zero is a consistency check on the
source enclosures, not by itself an existence proof for a globally
consistent sequence. The source interval construction and exact input
checks, already independently audited in33 and65, supply that provenance.
The present run also retains the K=30 launch header and checks that
it contains no radius reset.

All selected norm enclosures and source fingerprints are retained.
Only a small selection of coefficient arrays is frozen here because of
the storage limit; other arrays can be recovered from a later
peer checkpoint by their individual hashes. Neither a floating comparison
nor a finite slope proves an infinite growth law.

## Completed finite result

All 77,595 selected Poisson coefficient checks and all 83,249 signed Cartesian coefficient checks at order 250 pass. The latter includes every one of the 60 retained ordered pairs. Its relative residual enclosure is contained in [-9.42e-43,9.42e-43]. The calculation took 129.02117428882048 seconds.

The following intervals are log10 of the modified norm minus log10 of the full norm. The displayed approximations have rigorous error below 1e-12.

| Order | Density difference | Stream difference |
|---|---:|---:|
| 230 | -0.080640815097 | -0.169746321782 |
| 240 | -0.069954127698 | 0.528144474058 |
| 245 | -0.067278195230 | 1.060310752910 |
| 250 | -0.042719661954 | 0.890464797233 |
| 260 | -0.034589529879 | 0.738198481381 |

In particular, the stream norm at order 245 exceeds ten times the full-recurrence norm. This is an interval conclusion about the two exact sequences, subject to the audited enclosure construction. At order 250, the sums of input radii divided by the sums of absolute midpoints are bounded by 8.818e-43 for density and 2.820e-41 for stream. All individual coefficients with nonzero midpoint remain resolved through the audited range 224 to 260.

The 27-order regression slopes ending at 250 are -0.70153759166858 and -0.65881611857404 for the modified density and stream, compared with -0.70280600989872 and -0.70522131887718 for the full recurrence. These are enclosed finite slopes.

At order 250, the absolute differences between independently enclosed log norms and the previously retained binary64 log values are below 2.736e-13 and 3.625e-12. Thus the older rounded claim of 2.6e-13 should not be used as a rigorous density error bound; 2.74e-13 is valid for this retained float value. None of these estimates extends automatically to later orders.
