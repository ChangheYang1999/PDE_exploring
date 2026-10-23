# Far-field residual coefficients of a stored smooth finite formula

Date: 2026-10-20. This result explains the actual residual of a finite formula with exact stored parameters. It does not repair those parameters or assert an exact nearby profile.

## Statement, notation and dependencies

Use the density, coefficients C_(k,l), length L, exponent alpha and canonical velocity of result84, ../smooth_full_inverse_primitives/PROOF.md. Put p=1-2alpha in(0,1), beta=2alpha=1-p, and ell>1. The real numbers in the stored formula are interpreted exactly. Define finite angular functions

    Theta_l(theta)=L^(2alpha(l+1)) sin(theta) sum_k C_(k,l) cos(2k theta),
    e_l=p-l beta.

A missing coefficient is zero. On the circle, as r tends to infinity,

    rho = r^p Theta_0 + r^(2p-1) Theta_1 + O(r^(3p-2)),
    grad rho = grad(r^p Theta_0) + grad(r^(2p-1) Theta_1)
               + O(r^(3p-3)).                                           (1)

The remainders and their finitely many angular derivatives are uniform. Their radial derivative has the corresponding one-power improved bound. The estimates are statements about this finite basis only. If Theta_1=0 they remain valid. Define S_(2j)^0 by

    S_(2j)^0=L^(2alpha)[j C_(j,0)
                    -eta_j(alpha+j-1) C_(j-1,0)
                    +(alpha-j-1) C_(j+1,0)/2],
    eta_1=1, eta_j=1/2 for j>=2.

Set b_j=S_(2j)^0/[(2j)^2-(p+1)^2] and define

    V_r(theta)=-sum_j 2j b_j cos(2j theta),
    V_theta(theta)=(p+1) sum_j b_j sin(2j theta).

Then U=r^p(V_r e_r+V_theta e_theta)+o(r^p), uniformly in angle. Consequently the exact transport residual satisfies

    R=(ell p-1) r^p Theta_0 + r^(2p-1) E_1 + o(r^(2p-1)),       (2)
    E_1=[ell(2p-1)-1] Theta_1
                  +p V_r Theta_0+V_theta Theta_0'.            (3)

The expansion is valid even when 2p-1 is negative. If ell p=1, its first term vanishes exactly and ell(2p-1)-1=1-ell. If ell p differs from1, the first term is retained; rounding it to zero changes the density formula being audited.

At any fixed angle where Theta_0 is nonzero, put

    G_x=p cos(theta) Theta_0-sin(theta) Theta_0',
    G_y=p sin(theta) Theta_0+cos(theta) Theta_0'.

The pointwise normalizations in the prompt have limits

    N_f/r^p -> ell(|cos(theta) G_x|+|sin(theta) G_y|)+|Theta_0|,
    N_v/r^p -> (1+p)|Theta_0|.                                  (4)

In particular |R|/N_v -> |ell p-1|/(1+p). At the vertical axis with Theta_0(pi/2) nonzero, |R|/N_f -> |ell p-1|/(1+ell p). These statements do not assign ratios at an exact symmetry zero or at an angle where the leading angular coefficient vanishes.

## Proof of the density expansion

For one term, use the Cartesian/polar formula of result84:

    y C_(k,l) z^k(1+z)^(-alpha(l+1)-k) cos(2k theta)
      =C_(k,l)L^(2alpha(l+1)) r^(1-2alpha(l+1)) sin(theta)
          cos(2k theta)(1+L^2/r^2)^(-alpha(l+1)-k).

The last factor equals1+O(r^-2) with all derivatives asserted above, by the convergent binomial series at L^2/r^2=0. The contributions l=0 and l=1 give (1). Every l>=2 has exponent at most3p-2. The largest omitted radial correction has exponent p-2, and p-2<3p-2 because p>0. There are finitely many k,l, so all sums and derivative bounds are uniform in angle. Differentiating once in Cartesian coordinates lowers the radial order by one, giving the gradient expansion.

## Proof of the velocity expansion

Result84 gives S_(2j)=r^(p-1)S_(2j)^0+O(r^(2p-2)). The coefficient is the sum A+B+E at l=0, after converting z^-alpha to L^(2alpha)r^(p-1); simplifying that sum gives the displayed S_(2j)^0.

For n=2j, write S_n(r)=s_n r^(p-1)+E_n(r), E_n(r)=o(r^(p-1)). The modal Green formula is

    psi_n=(1/(2n))[r^-n int_0^r s^(n+1)S_n(s)ds
                         +r^n int_r^infinity s^(1-n)S_n(s)ds].

Integrating the leading power gives the coefficient

    (s_n/(2n))[1/(n+p+1)+1/(n-p-1)]
      =s_n/[n^2-(p+1)^2].

Both denominators are positive since n>=2 and p<1. For the remainder choose R_e so that |E_n(s)|<=epsilon s^(p-1) for s>=R_e. The inner integral over [0,R_e] contributes O(r^-n), and the remainder of the inner integral and all the exterior integral contribute O(epsilon r^(p+1)). Differentiating the Green formula cancels its two boundary terms; the same split bounds the derivative by O(r^-n-1)+O(epsilon r^p). Angular differentiation multiplies a finite mode by n. Let r tend to infinity and then epsilon to zero. Thus psi_n=b_j r^(p+1)+o(r^(p+1)) with derivative o(r^p), and the stated U expansion follows from U_r=-r^-1 psi_theta, U_theta=psi_r. No exterior boundary or harmonic field has been added.

## Residual and denominators

The linear differential operator ell r partial_r-1 applied to the two terms in (1) gives their factors ell p-1 and ell(2p-1)-1; its remainder is O(r^(3p-2))=o(r^(2p-1)). The product of the leading U with the leading gradient is r^(2p-1)(p V_r Theta_0+V_theta Theta_0'). All other products are o(r^(2p-1)), because U-r^p V=o(r^p) and the next density derivative is O(r^(2p-2)). This proves (2)-(3), including negative exponents.

For (4), the leading Cartesian gradient is r^(p-1)(G_x,G_y), while U/r tends to zero. Hence (ell x+U1)rho_x/r^p tends to ell cos(theta)G_x and the analogous y term tends to ell sin(theta)G_y. Also X.grad rho/r^p tends to p Theta_0, and U.grad rho/r^p tends to zero because p-1<0. Take absolute values to obtain (4). Its denominators are positive when Theta_0 is nonzero, so division in (2) is legitimate. On the vertical axis parity gives Theta_0'=0, so G_y=p Theta_0 and G_x=0, establishing the final axis formula.

## Scope and verification

The results are exact asymptotic identities for finite smooth density formulas under the canonical inverse. They do not imply that the finite formula solves the PDE. A nonzero ell p-1 can generate a large absolute residual at enormous r while both normalized residuals remain very small. Whether a computed extreme-radius value is this term or numerical cancellation must be checked with adequate precision and the exact coefficient. A two-precision comparison is an empirical check, not a global or interval certificate. A separate evaluator and manufactured tests are to be recorded alongside this proof before any numerical conclusion.
