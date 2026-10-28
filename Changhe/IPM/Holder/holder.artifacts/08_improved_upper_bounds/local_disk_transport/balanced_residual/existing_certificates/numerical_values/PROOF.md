# Numerical upper bounds from balanced local residuals

## Statement

For real functions on R^2 let [f]_a be the Euclidean homogeneous Holder
seminorm, 0<a<1. Define T_xx and T_xy by circular principal-value kernels
cos(2theta)/(2 pi r^2) and sin(2theta)/(2 pi r^2). On the homogeneous
space modulo constants they are defined by convergent kernel increments.
Their common operator seminorm C_a satisfies the following bounds when
../verification/accepted.json has verdict CONFIRMED:

| a | upper bound for C_a |
|---|---:|
| 1/1000 | 637.0404731132 |
| 1/100 | 64.0882487113 |
| 1/20 | 13.1842542383 |
| 1/10 | 6.8518151599 |
| 1/5 | 3.7439481769 |
| 3/10 | 2.7740919924 |
| 1/2 | 2.1956582224 |
| 3/4 | 2.6421673707 |
| 9/10 | 5.0112078400 |
| 99/100 | 42.2225505534 |

These bounds also hold on smooth compactly supported functions. The
first row is weaker than another accepted bound and is not used in the
best-bound table. No finite-exponent equality is asserted.

## Proof

Apply the residual-replacement theorem in ../PROOF.md with delta=1/64,
256 equally spaced radial bins between delta and 1/2, 512 angular cells
per pole circle, and phases j pi/32 for j=0,...,16. The exact signed
integer masses use unit 2^44. These masses are independent of a.

For every radial row k and phase j, replay the deterministic angular
extraction at 160 bits from the identical source used by the accepted
certificates. Preserve all 512 signed integers for the right pole;
the left integers are their negative central reflection. Verify their
sum, absolute sum, exact radial endpoints and all source hashes. Let
Vhat and Qhat be outward bounds for the residual variation and the
absolute value of its exact signed mass, as defined in ../PROOF.md.
For the right endpoint r of the radial bin, the paired residual cost is
bounded by

    Vhat (2r)^a + min(Vhat,Qhat) [(1+2r)^a-(2r)^a].

This follows by matching the balanced part within each disk and sending
only the unmatched signed mass across the two disks. Its proof uses the
Jordan decomposition and the respective distance bounds 2r and 1+2r.

All extracted transport plans and the middle and exterior costs remain
those of the accepted certificates. Subtract the lower endpoint of the
old residual enclosure from the old phase upper bound and add the upper
endpoints of the new residual costs. This bounds the unchanged transport
cost plus the new residual cost. Independent reconstruction of every old
residual enclosure must overlap the stored outward enclosure, and every
radial row and phase must occur exactly once.

Add the previously proved small-disk bound

    S_a = 2^(2+a/2) delta^a/[pi a(a+2)]
          +(1+2delta)^a delta^2/[2(1-delta)^2]

to sec(pi/64) times the largest of the 17 revised phase bounds. This
phase interpolation is valid for each output increment because it is
the scalar product of a fixed real two-vector with the phase direction.
The principal values and the exterior convergence are already covered
by the accepted completion theorem; no new limiting operation is used.

The certificate combiner uses exact rational serialized endpoints and
320-bit outward evaluation of sec(pi/64). Rounding its resulting upper
endpoint upward to ten decimal places gives the displayed table. The
acceptance manifest binds the complete mass replay, the original
certificates, the combiner and this proof. Thus every operation in the
numerical conclusion is an application of an explicit proved bound.

## Dependencies and scope

The parent residual-replacement theorem and its balanced-measure lemma
were independently cross-read by the lead in Note31 and accepted in
V150. The original local, middle and exterior certificates were accepted
in V131 or in the earlier paired-circle composite audits. Evidence is
preserved in ../verification/independent_audit.json, the 256 mass replay
files and ../verification/accepted.json. The new audit does not rerun
transport optimization; it preserves the previously certified plans.
