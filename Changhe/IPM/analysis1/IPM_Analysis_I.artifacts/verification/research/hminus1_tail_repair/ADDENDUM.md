# Mandatory clarifications after the actual Opus 5.5 proof review

This accompanies the unchanged proof-first PROOF.md. The exact theorem is
qualitative and concerns explicitly constructed trials. It is not an
existence or exclusion endpoint.

## A1. Exact exponent, column and resonance obligations

The two input audits read the original binary64 archive and its exact hex
export independently. The first uses Fraction arithmetic on the hexadecimal
mantissa and exponent; the second uses the original NPZ binary64 integer
ratios. They compare all 2600 outer coefficients and all 1573 knots.
Both check all 55 pairs among the eleven distinct original density
exponents. The archive checksum and JSON checksum are pinned. Column2 has
(j,l)=(2,0), column6 has (0,1), and the eleven density exponents include
3-bo from the exact recomputed fast join, not a twelfth unknown exponent.

The normalization is exactly the modal_repair definition: only A_00 changes
by z, and the fast joined mode0 correction changes by

 -z exp(-bo tau) sum_(i=0)^6 ((k-3+bo)tau)^i/i!.

All other columns and angular modes are unchanged. The seven vanishing
join jets of the resulting scalar basis follow by the binomial identity

 (k-3)^n=sum_(j=0)^n binom(n,j)(-bo)^(n-j)(k-3+bo)^j, 0<=n<=6.

These identities are checked exactly again here. The existence, positivity
of the strain slope and exact real definition of z remain the independently
validated modal_repair dependency; no decimal value replaces z.

For every original exponent a and every 1<=n<=261, the audits check
(2n)^2-(a+1)^2 != 0, independently in expanded and factored form.
For every new tail at a1,a2,d they check all required modes through
522,783,261 respectively. All new denominators are strictly positive.
Every outer Green integral also converges, since a_i-2n<-1. Thus there is
no resonant increase of logarithmic degree, and the stated exponent12
in the residual bound is justified. The exact check k<1/4 proves a3<-2.
The bound r>=2T and its constant depend on the chosen T; no uniform bound
in T is asserted.

## A2. Sufficient counterterms, without an unproved necessity claim

The proof constructs coefficients which cancel the a1,a2,d residual rows.
This is sufficient to leave exponent at most a3. It has not independently
proved that the actual a2 and d residual rows of the topic105 trial are
nonzero. Consequently the review's assertion that both new cancellations
are necessary, or that the topic105 residual definitely fails the new
weighted L2 condition, is not adopted. If a row is already zero, its
correction may vanish. Likewise k<1/4 is sufficient for the stated
remainder estimate to imply integrability; failure of that inequality
alone would not prove nonintegrability without a nonzero leading row.

The review's phrase that every ordered pair involving d gives 2k-3 is
also too strong. The largest such exponent, from pairing d with k, is
2k-3. All others are smaller. Both exact enumeration methods check the
weaker and correct upper bound. Neither correction affects the proof.

## A3. The two-dimensional homogeneous space and the zero mean

Define the norm on distributions by

 ||f||_(dot H^-1)=sup{|<f,phi>|: phi in C_c^infty(R2),
                                    ||grad phi||_2<=1}.

Finiteness gives the continuous extension to the gradient completion.
The explicitly constructed vector J is in L2 and satisfies div J=f,
so the definition is unambiguous and the bound follows directly. No
choice of a potential or value at infinity is used. Constants are not
nonzero elements of C_c^infty and the seminorm completion may equivalently
be realized with the usual constant gauge; the direct test-functional
construction avoids relying on any pointwise realization of that space.

Here epsilon_T is also in L1: compact continuity and a3<-2 with a finite
logarithmic power give absolute integrability. Oddness in y implies
integral_(R2) epsilon_T=0 automatically. Thus the cancellation required
for such an integrable homogeneous negative-norm forcing is satisfied.
The phrase about no radial moment cancellation in PROOF means that no
additional moment assumption is imposed. It does not mean that a
nonzero total integral would be allowed. Zero angular mean on every
circle is the stronger already established condition. The exact constant1
uses only the L2 Fourier multiplier 1/nu on that mean-zero angular space;
it is unrelated to the IPM Holder-operator issue in PROMPT.

## A4. Regularity and exact scope

The added correction and its center factor are C7 at r=T and r=2T.
The full trial retains the original C6 joins; if T=R_b, those joins
coincide and only C6 is asserted for the full density there. This corrects
any reading of the original sentence as an upgrade of an existing join.
Near zero the density is exactly the old density and the center factor
is merely required to be continuous, as in the kinematic P2 conditions.
Stationarity, and hence membership in P2 itself, remain unproved.

The construction leaves the leading r^k coefficient unchanged. The new
C2 and Cd weighted-factor constants are finite expressions but have not
been enclosed numerically. No finite numerical ceiling for the full
residual norm, smallness as T grows, full inverse, source coupling bound,
nonlinear closing inequality or X3 uncertainty neighborhood follows.
The raw forcing E rho_T still has its nonzero growing leading coefficient
and is outside dot H^-1. This result only repairs the forcing-space
membership obstruction for the fixed-scalar residual.
