# A fixed source tail survives in the full-plane velocity

Date:2026-10-20. Status: complete elementary proof. No profile or continuation theorem is asserted.

## Statement and hypotheses

Use Omega=-Delta Psi, V=(-Psi_y,Psi_x), the centered full-plane inverse

    B[f](X)=integral [K_v(X-Y)+K_v(Y)] f(Y)dY,
    K_v(z)=(z_2,-z_1)/(2pi|z|^2).

The fields below are smooth, odd in x, and have finitely many angular modes with polynomial bounds. Finitely differentiable spline fields obey the same argument whenever they have the stated bounds and local regularity. Write X=(r sin phi,-r cos phi). Suppose

    f_S(r,phi)=sum_(n=1)^J H_n(r) sin(n phi),
    H_n(r)=a_n r^-nu_S+o(r^-nu_S), 0<nu_S<1,

and at least one a_n is nonzero. Let p=2-nu_S. Then

    r^(-(1-nu_S)) B[f_S](r,phi) -> v_a(phi)

uniformly in angle, where in the oriented polar frame e_r=(sin phi,-cos phi), e_phi=(cos phi,sin phi),

    v_a . e_r = -sum n a_n cos(n phi)/(n^2-p^2),
    v_a . e_phi = sum p a_n sin(n phi)/(n^2-p^2).

The vector function v_a is not identically zero. If f_N is any finite angular representation with f_N=O(r^-nu), nu_S<nu<1, then

    r^(-(1-nu_S)) [B[f_N]-B[f_S]] -> -v_a,
    sup_(r>=1,phi) r^(-(1-nu)) |B[f_N]-B[f_S]| = infinity.

Multiplication by a fixed nonzero lambda does not change the infinite-norm conclusion. Appending a constant velocity changes neither limit, although it is not allowed as an independently fitted B2 parameter.

This global weighted-norm obstruction coexists with local inverse convergence. Specifically, cut off f_S outside radius R with a fixed smooth radial cutoff. The resulting compact sources have any decay exponent, while their centered velocities converge on every fixed compact set in C1 at rate O(R^-nu_S). A compact correction can preserve the exact center strain while maintaining that local convergence. This is a scope limitation, not a contradiction.

## 1. Convergent canonical inverse and modal formulas

For fixed X the far-field difference K_v(X-Y)+K_v(Y) is O(|X|/|Y|^2); with f_S=O(|Y|^-nu_S), its integral converges absolutely at infinity. The local 1/|X-Y| singularity is integrable. Oddness and smoothness give f_S=O(r) at0, and the remaining K_v(Y) term is locally integrable. The centered gauge gives B[f_S](0)=0.

Separation of -Delta Psi=f_S gives Psi=sum P_n(r)sin(n phi). For n>=2 the full-plane regular subquadratic inverse is

    P_n=(1/(2n))[r^-n integral_0^r s^(n+1)H_n(s)ds
                    +r^n integral_r^infinity s^(1-n)H_n(s)ds].

For n1 the center subtraction gives

    P_1=(1/2)[r^-1 integral_0^r s^2 H_1(s)ds
                  -r integral_0^r H_1(s)ds].

These formulas follow either from variation of parameters in the radial Poisson equation or by differentiating them directly. The integrals converge; local regularity discards the r^-n solution. For n>=2 the r^n growing exterior homogeneous solution is absent, since it would give non-sublinear velocity. For n1 the displayed subtraction fixes the linear stream term by zero velocity at0. Thus no affine strain or independent harmonic field has been introduced. These formulas agree with the absolutely convergent centered vector kernel, by uniqueness: their difference has harmonic sublinear velocity and is zero at0.

Set A_n(r)=integral_0^r s^(n+1)H_n(s)ds and B_n(r)=integral_r^infinity s^(1-n)H_n(s)ds. For n>=2, the elementary asymptotic integration estimates give

    A_n=[a_n/(n+2-nu_S)]r^(n+2-nu_S)+o(r^(n+2-nu_S)),
    B_n=[a_n/(n+nu_S-2)]r^(2-n-nu_S)+o(r^(2-n-nu_S)).

The denominators are positive. Splitting an integral at a fixed large radius and bounding the o(1) remainder proves these estimates; no differentiated remainder is required. Consequently

    P_n=[a_n/(n^2-p^2)]r^p+o(r^p).

The terms containing H_n cancel on differentiation of the exact formula, so

    P_n'=p[a_n/(n^2-p^2)]r^(p-1)+o(r^(p-1)).

For n1, integral_0^r H_1=[a_1/(1-nu_S)]r^(1-nu_S)+o(r^(1-nu_S)). Combining it with A_1 gives the same P_1 asymptotic, since

    (1/2)[1/(3-nu_S)-1/(1-nu_S)] = 1/[1-(2-nu_S)^2].

Differentiating the exact P_1 formula gives the same derivative asymptotic. The finite angular sum makes both limits uniform. Velocity in this frame is V_r=-(partial_phi Psi)/r and V_phi=partial_r Psi, proving the displayed v_a formula. Since p is strictly between1 and2, no denominator vanishes. Orthogonality of sine modes in v_a.e_phi shows that v_a=0 would force every a_n=0. This proves nontriviality.

## 2. The stronger-weight velocity error

The same modal integrals with H_n=O(r^-nu) imply B[f_N]=O(r^(1-nu)); no nonzero leading coefficient is needed. Thus r^(-(1-nu_S))B[f_N] tends uniformly to0. Subtract the first result. At a direction with |v_a|>0 the error is bounded below by a positive multiple of r^(1-nu_S). Dividing by r^(1-nu) gives growth r^(nu-nu_S), proving the infinite supremum.

A constant vector is o(r^(1-nu_S)), because nu_S<1, and a fixed nonzero lambda simply rescales the nonzero coefficient. This establishes the gauge and amplitude statements.

## 3. Local convergence despite the weighted obstruction

Choose chi smooth radial, chi=1 on r<=1, chi=0 on r>=2, and define f_R(X)=chi(|X|/R)f_S(X). Fix a compact ball of radius A and take R>2A. The source difference vanishes inside R, so for |X|<=A,

    |B[f_R-f_S](X)| <= C A integral_R^infinity r^(-1-nu_S)dr
                     <= C_A R^-nu_S.

This uses the subtracted kernel estimate already proved. Differentiating in X introduces DK_v(X-Y)=O(r^-2) and gives the same O(R^-nu_S) bound for the first derivative on that compact set. There is no singularity because the source difference is supported outside R.

The center strain c[f]=partial_x partial_y Psi(0) is a first derivative of V, so |c[f_R]-c[f_S]|=O(R^-nu_S). Choose one fixed smooth compact odd-in-x source b with c[b]=1. Such a b is obtained by normalizing b(x,y)=xy rho(|X|), with nonnegative nonzero smooth radial rho supported in an annulus: the strain integral is a positive multiple of integral rho(r)r dr. Set

    f_R^*=f_R+[c[f_S]-c[f_R]]b.

It has exactly c[f_R^*]=c[f_S], remains compactly supported, and its centered velocity still differs by O(R^-nu_S) in C1 on each fixed compact set. Its global stronger-weight error remains infinite by section2. Exact center-strain matching therefore cannot certify the missing far field.

One can also keep the source unchanged on the test compact set and improve the local rate. For fixed A choose Psi_b=xy times a smooth radial cutoff equal to1 on r<=2A and0 on r>=4A. Then b=-Delta Psi_b vanishes on the ball2A, has c[b]=1, and B[b]=(-x,y) on that ball. Let E_R=B[f_R-f_S]. Reflection and divergence give DE_R(0)=diag(-c[E_R],c[E_R]). The same correction exactly cancels this linear field. Taylor expansion of the subtracted kernel gives

    |E_R(X)-DE_R(0)X| <= C |X|^2 R^(-1-nu_S),
    |DE_R(X)-DE_R(0)| <= C |X| R^(-1-nu_S), |X|<=A.

Indeed the second derivative of K_v is O(r^-3), and its product with the tail has radial integral O(R^-1-nu_S). For R>8A the corrected source equals f_S on the ball A and its velocity converges there in C1 at the improved rate O(R^-1-nu_S), with exact center strain. Its global stronger-weight error is still infinite.


## 4. Application and limits

Packet76 verifies an actual seed source E-Omega_S with beta_S=3 and a nonzero r^-1/3 coefficient, using exact rational arithmetic on the saved binary coefficients. Every finite retied beta in(2,3) has nu=1/beta>1/3. Both the source weighted error and the velocity weighted error above are therefore infinite if the intended source remains that fixed E-Omega_S.

This conclusion does not show that a finite-grid continuation is unusable, that all weaker norms fail, or that the lambda0 endpoint cannot be validated. It means that the displayed approximation cannot be certified in the new exponent's global weighted norm. A continuation in a fixed weaker space that permits the seed tail is a different formulation. The compact-cutoff construction explicitly demonstrates why local velocity fits can remain accurate while the global stronger norm fails.

Dependencies: elementary radial Poisson inversion and estimates, finite Fourier orthogonality, and the exact seed coefficient certificate of packet76. The complete proof precedes the additional numerical tail check. No numerical computation is needed for the theorem.
