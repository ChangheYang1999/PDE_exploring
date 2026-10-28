# A weaker low matrix hypothesis for the same weighted existence theorem

Status: independently proved below. This changes a sufficient hypothesis, not the theorem's norm or constants. It does not certify a new reference.

## Statement

Use the exact spaces, canonical velocity, maximal distributional domains, reference conditions, and parameters of topics18 and20. In particular

    9/5<c<37/20, sigma=11/5, d=4/9, R=2^31,
    w_R=(1+r^2/R^2)^(-sigma/2),
    (C_rho,C_U,C_DU,C_D2U)<=(186,22,22,56).

Keep conditions W0,Wn,W2,W3,Wm and, for the leading-profile conclusion, Wt. Replace the low matrix part of W1 by

    M=(2c+1)I+sym Du+[[rho_y,-rho_x/2],[-rho_x/2,0]]
                           >=(5/2)I on r<=R.             (1)

Then every weighted inverse, nonlinear closure, normalization, and fixed-tail conclusion of topic18 remains valid in the R=2^31 norm, with exactly the same constants. In particular, the low reference semigroup decays at rate at least1/5; the rough high rate is

    1/20-2^23 s-400 N_(s,R)(k)/sqrt(s),

and at s=3*2^-31, r0=5*2^-32, eta=2^-35 the inverse bounds are40 and6, with low contraction factor less than2/5. Existence still requires the actual residual bound N_(s,R)(F)<=eta.

One may impose(1) globally for convenience. No matrix certificate is needed outside R in addition to the stated decay coefficients. This does not claim that5/2 is optimal or necessary.

## 1. The only use of the old floor

Let g=w_Rh, phi=(-Delta)^-1g and q=Dphi. The exact weighted low energy identity is

    -<w_R L_fix h,phi>
       =int q^T(M+bI)q -(1/2)int Delta b phi^2
                                  -<D_Rg,phi>,
    b=V.D log w_R=b0+b1,
    b0=-sigma c t, t=r^2/(R^2+r^2),
    b1=-sigma u.X/(R^2+r^2).

The derivation includes every weight term and is unchanged by a different bound on M. On r<=R, t<=1/2 and Delta b0<=0. Consequently the contribution of M+b0I and Delta b0 on this region is bounded below by

    (5/2-sigma c/2) int_(r<=R)|q|^2
       >(5/2-407/200) int_(r<=R)|q|^2
       =(93/200) int_(r<=R)|q|^2
       >(2/5) int_(r<=R)|q|^2.                          (2)

Thus the old floor19/5 was stronger than required for the baseline2/5. Neither a change of weight nor an altered matrix energy is involved.

## 2. Exterior and commutator terms

For r>=R the coefficient bounds already imply

    M >= [2c+1-(C_DU+C_rho)R^-d] I.

The radial circle Poincare inequality

    int a(r) phi^2 <= int r^2 a(r)|Dphi|^2, a>=0,

applies to the positive part of Delta b0 on this region. The same exact cubic maximum as in LOW_INVERSE_PROOF gives

    t+2t(1-t)(2t-1)<=21/20, 1/2<=t<=1.

The exterior baseline is therefore

    2c+1-(21/20)sigma c
       =1-31c/100 >853/2000>2/5.                        (3)

The loss from C_DU+C_rho is included in the global error below. The velocity-weight terms and the real radial coupling commutator are independent of the floor in(1). Topics07 and20 bound their total, together with that exterior coefficient loss, by

    R^-d [C_DU+(1+21/2)C_rho
                   +sigma(9C_U+2C_DU+C_D2U/sqrt(2))].    (4)

At the stated tuple and radius, the already certified rational estimate is

    2/5-(4) >14093/70000>1/5.

Combining(2)-(4) proves the identical low coercivity. The weak-circle treatment of the radial term and ordinary parity Hardy bound for b1 are precisely the previous ones; there are no omitted interface fluxes, because the proof restricts the original integrals and applies a circle inequality rather than integrating by parts across r=R.

## 3. Generator, high inverse, and nonlinear closure

The low generator construction uses the smooth complete transport flow and the bounded canonical weighted coupling. Its domain construction needs the structure and coefficient regularity, not a particular numerical matrix floor. The positive energy margin supplies both the semigroup decay and the convergent inverse integral. Thus injectivity and surjectivity persist.

The weighted first and second derivative estimates of SHARP_WEIGHTED_H2_PROOF use the low margin1/5, W2, W3 and universal Riesz bounds. Their displayed energy identities have no further use of the number19/5. They still yield the E_R semigroup rate1/20. The fractional commutator, rough-velocity estimates and common-domain proof of topics16 and18 use this rate, the same low margin, W3 and the reference-independent multipliers. Their constants are unchanged.

The trace identity, complete high ball in the low metric, bilinear difference estimate and fixed leading profile likewise use only the already retained hypotheses. Thus the entire conditional theorem transfers, without treating a mere energy inequality as a proof of surjectivity.

## 4. Interpretation and limits

The axial shape restrictions in topic22 were proved for a specified floor kappa. They remain correct at kappa=19/5, including the certified A2/A3 distances to that stronger matrix class. They do not say that this stronger class is necessary for a weighted existence theorem. At kappa=5/2 the parameter kappa-c-1 is negative, so the positive-power concavity conclusion from that topic cannot be invoked.

In particular, failure of M>=19I/5 alone no longer disproves applicability of the conditional theorem with this weaker hypothesis. One must check(1), both W2 matrices, every W3 derivative bound, decay coefficients, normalization, membership and actual smallness for the particular reference. No A2,A3 or later candidate is declared admissible for the full theorem by this result.

## Dependencies

07_weighted/LOW_INVERSE_PROOF.md and LOW_INVERSE_FAMILY_PROOF.md: exact energy, radial cubic bound, flow and inverse.
07_weighted/SHARP_WEIGHTED_H2_PROOF.md: high derivative hierarchy from the low rate.
16_weighted_fractional/REFERENCE_AUDIT.md and the three fractional/rough proofs: retained reference contract and common realization.
18_fractional_constants/PROOF.md: final nonlinear constants.
20_real_velocity/PROOF.md: real commutator bound, radius and exact rational margin.
22_axis_constraints/PROOF.md: scope of the earlier stronger-floor obstruction.

## 5. Stronger position-dependent version, independently checking lead proposal L1

The lead's proposal L1 replaces (1) by the weaker sufficient condition

    M(X) >= [2/5 + sigma c r^2/(R^2+r^2)] I, r<=R.       (8)

This has the same conclusions and constants. Indeed, on the interior, subtracting sigma c t from (8) gives the baseline2/5 pointwise, while the term involving Delta b0 is nonnegative. Sections2 and3 then apply without any change. Thus (8) is sufficient; the constant hypothesis(1) is a convenient corollary. A sharper constant sufficient condition is M>=[2/5+(11/10)c]I on the interior.

There is a useful finite verification radius. On r>=T, the retained decay bounds imply

    M >= [2c+1-208r^(-4/9)]I.

Consequently (8) follows there if

    208 T^(-4/9) <= 3/5 + (9/10)c.                     (9)

For the original exact c, T=27057 satisfies (9); this number must not be stated uniformly for every c in(9/5,37/20). The exact arithmetic check records the smallest integer satisfying (9) for that c and also a uniform integer for the full permitted c interval. Since R=2^31 is larger than either integer, it suffices to verify (8) on the corresponding finite ball and retain the globally certified decay tuple. Condition(9) can be checked without transcendental arithmetic by raising both positive sides to the ninth power:

    208^9 <= [3/5+(9/10)c]^9 T^4.

At a fixed point in the core the correction to2/5 is of order r^2/R^2. This explains why failure of the old19/5 floor at(0,1) is not a failure of(8). It does not certify(8), W2 or W3 globally for A2,A3 or any other new reference. In particular the exact-profile concavity statement in topic22 can only be applied with its own positive-exponent hypotheses; substituting the present core floor does not meet them.
