# 165. Dynamic rescaling implementation and snapshot audit

Written 2026-10-21, before the independent audit code. This is an algebraic and numerical implementation audit, not an existence or instability theorem. The saved finite fields are defined by their coefficients; their time histories are numerical data.

## Statement and notation

Let the canonical linear inverse of a smooth density be U. Write
G[rho] = c_w rho - (c_x X + U[rho]) dot grad rho.
For fixed C > 1, a slope-preserving gauge is c_w = -c/(C-1), c_x = C c_w, where c = psi_xy(0). For c_w > 0 define rho_star = rho/c_w and U_star = U/c_w. Then
R_star = (C X + U_star) dot grad rho_star - rho_star = -G[rho]/c_w^2.
This is an instantaneous identity, not an assertion that the time derivative of rho_star is -R_star. If c_w depends on time, differentiating rho_star gives another term. A numerical snapshot using an approximate c may also have a nonzero independently computed center defect.

The Q representation is rho = y w b, b = sum_{k=0}^{M-1} sigma^k B_k(t) cos(2k theta), sigma=(1+t)/2, w=(1-t)/2, r^2=L^2 sigma (1-t)^(-2P). Here P>1 and the actual density exponent is p=1-1/P. Coefficients and the stored P are interpreted literally. Exact p=1/C is tested, not assumed from a rounded metadata field.

## Proof of the gauge and scaling identities

The first derivative at the origin satisfies a_tau = (c_w-c_x-c)a, by U_2=c y+O(r^3) and rho=a y+O(r^3). Thus c_w=c_x+c preserves any a, not only a=1. Solving this with c_x=C c_w gives the stated rates. Linearity of the canonical inverse gives U[rho/c_w]=U/c_w. Expanding R_star and multiplying by c_w^2 proves the residual identity. The right-hand side G is quadratic in rho in this gauge. Consequently rho_A(tau)=A rho(A tau) is also a trajectory when A>0. This relates a constant-shape family of initial seeds; it does not make a=1 a stationary-profile gauge.

For rho=a y+b x^2 y+e y^3+O(r^5) and psi=c xy+d x^3 y+f xy^3+O(r^6), the coefficient of y^3 in U dot grad rho is 3c e+a f. Therefore e_tau=(c_w-3c_x-3c)e-a f. On the slope gauge this is -2c_w e-a f. Holding e fixed requires c_w=-a f/(2e), when e is nonzero. Omitting a is legitimate only if a=1 is actually preserved in that run.

## Canonical center and exterior moments

Let f_3(r) be the sin(3theta) density coefficient. The canonical identity is
c = -a/4 + I(0), I(R)= integral_R^infinity f_3(r)/r^2 dr.
For the finite Q field, f_3 = r w (sigma B_1-sigma^2 B_2)/2. Differentiating the map gives dr/r = Q(t)dt/(1-t^2), Q(t)=(1-t)/2+P(1+t). Thus
I(R)= integral_{t(R)}^1 Q(t)[B_1(t)-sigma B_2(t)]/8 dt.
This is a polynomial integral. Its value at R=0 can be computed with exact rational arithmetic from the literal binary coefficients and P. This avoids the conditionally convergent unrenormalized origin strain integral. The canonical modal inverse includes both the regular inner Green integral and the decaying outer Green integral. Independently, the Cartesian cancellation-kernel inverse includes the contact term (0,-rho/2) and the complete exterior integral. It contains no harmonic xy term.

The center jets are a=B_0(-1), b=(2B_0'(-1)-a+B_1(-1))/ell_c^2, e=(2B_0'(-1)-a-B_1(-1))/ell_c^2, ell_c^2=L^2 2^(-2P). The trace amplitudes are A_1=D(B_0(1)-B_1(1)/2), A_3=D(B_1(1)-B_2(1))/2, K=D sum_k (-1)^k B_k(1), D=L^(1-p)/2. These follow by sin(theta)cos(2k theta) product identities and the radial map endpoints. They are valid for any finite Q field.

## Projection and diagnostic scope

Let S map coefficient vectors to b on the collocation grid, let P_num project grid values to coefficient vectors, and suppose the integrated equation is u_tau=P_num F(Su). The derivative of the represented density is y w S P_num F, not y w F. Equality needs the separate condition S P_num F=F. Angular truncation alone prevents that equality for general data: on a grid with 3M distinct midpoint angles, F=cos(2M theta) has zero projection onto the retained cos(2k theta), 0<=k<M, although F is not zero. Radial projection can introduce additional discrepancy. A test of a specially representable manufactured F cannot establish equality for evolved states. Both derivatives and their difference should be logged.

For fixed positive rates the exact physical-time increment is dt/dtau=exp(-int_0^tau(c_x-c_w)). Integrating this with values at the right endpoint is a rectangle rule even if the inner rate integral uses a trapezoid rule. A resume must retain the accumulated rate integral. A rollback must restore that integral, physical time and any integrated asymptotic diagnostics together with u and tau. Otherwise the fields and diagnostics refer to different histories. Finite observed physical time is not evidence that the integral converges at infinite rescaled time.

For pure leading trace A sin(theta), the previously proved law is b3_tau=(C-1)c_w b3+A^2(1-p)/(4(p+3)). Its initial value must be the actual b3. A chain seed generally has a nonzero b3 and a non-pure angular trace. The pure-trace law is not a diagnostic for that general seed without replacing the forcing by the full angular expression. Truncation-induced trace drift also needs to be measured.

## Counterexample to an eigenvector inference

Every unstable eigenvector can be concentrated outside a core and still have an exponentially growing core component. In R^2 let v=(epsilon,1), normalized in Euclidean norm, let w=(1,-epsilon), and let A be the symmetric operator with Av=v and Aw=-w. For epsilon=1/100 the unstable eigenvector has more than 99.99 percent of squared norm in the second coordinate. But the solution exp(tA)v=exp(t)v has exponentially growing first coordinate epsilon exp(t). A is symmetric and hence normal. Thus exterior localization of all unstable eigenvectors does not imply that observed core growth is nonnormal or transient. Finite projection spectra also do not establish continuum stability or instability.

## Verification protocol and dependencies

Use the verifier's pre-existing scalar Q reader, Cartesian eighth-order differences, cancellation-kernel whole-plane inverse, complementary angular Green charts and multiprecision finite primitives. No producer numerical routines may be imported or executed. Freeze source fields, source hashes, actual times and rate metadata. Recompute canonical c, center jets, trace, exterior moments, both normalizations, and selected residuals. Compare independent inverse orders and selected multiprecision points. A density fit at one instant is not a trajectory validation; matched time-step and spatial refinement remain separate requirements.

Dependencies: results 149 and 151 (DR algebra and manufactured field), 154 (pure-trace far law), 160 (remote-tail influence), the independently tested Q inverse and reader proofs. No formal source or Lean build is used. Numerical accuracy is empirical, not an interval certificate. General-profile existence, time convergence and physical blowup remain OPEN.
