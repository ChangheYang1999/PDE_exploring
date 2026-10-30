# Optimal negative-norm extension of prescribed exterior modes

## 1. Statement

Let H be the real S1 homogeneous negative Sobolev space Hdot^(-1)(R2), with norm ||F||H=||(-Delta)^(-1/2)F||2. S1 means even in x and odd in y. Let T>0, sigma>0, I a finite nonempty set of positive odd integers, and a_n real coefficients not all zero. Prescribe the exterior distribution

    f_ext(r,theta)=r^(-2-sigma) sum_(n in I) a_n sin(n theta), r>T.

Among all F in H whose restriction to the open exterior r>T equals f_ext, the squared norm has the exact minimum

    K=pi T^(-2sigma) sum_(n in I) a_n^2/[2sigma(n+sigma)^2].   (1)

There is a unique minimizer F*. It is the exterior density, zero on the open interior, together with a boundary layer

    F*=1_(r>T) f_ext+mu(theta) delta(r-T),
    mu(theta)=-T^(-1-sigma) sum_(n in I) a_n/(n+sigma) sin(n theta).  (2)

The convention for delta(r-T) is integration against polar measure r dr dtheta, so its action is T integral mu(theta) phi(T,theta)dtheta. The same value K is the infimum if F is additionally required to be an L2 function. That infimum is not attained in L2 when the coefficients are not all zero.

The minimum assertion and the boundary-layer description independently verify T2's new Remark R1 in its review of T4-014. The explicit L2 approximation below makes rigorous the non-improvement that the T2 review illustrated numerically. No numerical parameter is needed for this result.

## 2. Exterior Dirichlet potential

For n not equal to sigma put

    v_n(r)=a_n [r^(-sigma)-T^(n-sigma)r^(-n)]/(n^2-sigma^2), r>=T.

For n=sigma put

    v_n(r)=a_n r^(-n) log(r/T)/(2n).

Let phi=sum v_n(r)sin(n theta) on r>T and phi=0 on r<=T. Each v_n(T)=0, and direct differentiation gives

    -v_n''-r^-1 v_n'+n^2r^-2 v_n=a_n r^(-2-sigma).

The gradient of phi is square integrable because n,sigma>0; the resonant logarithm does not change integrability. The zero trace makes its extension by zero an element of the global homogeneous energy space Hdot^1. It is a limit in gradient norm of smooth S1 tests compactly supported in the open exterior: first cut off near T using its zero trace, then cut off at infinity, then mollify. Thus no boundary trace is silently discarded.

Integration by parts mode by mode gives

    ||grad phi||2^2
      =pi sum a_n integral_T^infinity r^(-1-sigma)v_n(r)dr=K.

The inner boundary term vanishes because v_n(T)=0, and the term at infinity vanishes by the displayed powers. The elementary radial integral is a_n T^(-2sigma)/[2sigma(n+sigma)^2], including n=sigma by its logarithmic formula or a continuous limit.

Let F*=-Delta phi. By the isometry from Hdot^1 modulo constants to Hdot^(-1), F* belongs to H and ||F*||H^2=K. Across r=T, the outward radial derivative jumps from zero to

    v_n'(T)=a_n T^(-1-sigma)/(n+sigma).

The distributional negative Laplacian therefore has layer coefficient -v_n'(T), yielding (2), with the stated polar-measure normalization.

## 3. Minimality and uniqueness

Let F be any admissible H distribution and G=F-F*. Then G annihilates every compact smooth test in the open exterior. Approximation of phi by the tests from Section2 and continuity in the homogeneous energy norm imply

    <G,phi>=0.

The negative-norm inner product satisfies (G,F*)H=<G,phi>. Hence

    ||F||H^2=||F*||H^2+||G||H^2=K+||F-F*||H^2.              (3)

This proves the minimum and uniqueness. It also rules out a better lower bound obtained only from the same exact exterior data, without information on the extension.

## 4. Approximation by L2 extensions

The truncated exterior density 1_(r>T)f_ext belongs to L2 because sigma>0. Let eta be a smooth nonnegative function supported in(0,1), with integral eta=1. For 0<epsilon<T/2, define the interior shell function

    g_epsilon(r,theta)= T mu(theta)/(r epsilon)
                       eta((T-r)/epsilon), T-epsilon<r<T,

and zero elsewhere. It belongs to L2, is S1, and has exactly the total angular mass of the layer in(2). Put F_epsilon=1_(r>T)f_ext+g_epsilon. Its exterior restriction is exactly the prescribed f_ext.

For a compact smooth S1 test psi, the difference of the shell and layer pairings is

    T integral mu(theta) integral_0^1 eta(s)
       [psi(T-epsilon s,theta)-psi(T,theta)]ds dtheta.

The fundamental theorem of calculus in r and Cauchy-Schwarz give

    ||psi(T-epsilon s,.)-psi(T,.)||L2(theta)
       <=sqrt(epsilon/(T-epsilon)) ||grad psi||L2(shell).

After integration against eta and mu, this bounds the difference by

    sqrt(2T epsilon)||mu||L2(theta) ||grad psi||2.

Taking the energy-space dual norm proves

    ||F_epsilon-F*||H <=sqrt(2T epsilon)||mu||L2(theta) ->0.   (4)

Thus the same infimum K holds among L2 extensions. Every such F_epsilon also belongs to H by(4). Since mu is nonzero, F* has a nonzero boundary measure and is not an L2 function. Uniqueness in(3) therefore proves non-attainment in L2. A bound on the size of the L2 or higher norm could change the constrained infimum; mere membership does not.

## 5. Independent check of per-mode remainder weights

A second statement from T2 Remark R4 is also valid. Suppose an H function has exterior coefficients

    F_n(r)=a_n r^(-2-sigma)+R_n(r),
    |R_n(r)|<=epsilon_n |a_n| r^(-2-sigma), 0<=epsilon_n<1,

for n in some subset I'. Let K_n denote the nth summand of(1), including pi. Each v_n has the sign of a_n on r>T. Use the exterior test

    phi_weighted=sum_(n in I') (1-epsilon_n)v_n sin(n theta).

Angular orthogonality and the sign give <F,phi_weighted>>=sum(1-epsilon_n)^2 K_n, while the squared gradient norm is exactly that same sum. Duality therefore gives

    ||F||H^2>=sum_(n in I')(1-epsilon_n)^2 K_n.               (5)

Modes without a verified bound can be omitted. Cutoff convergence follows from the displayed per-mode bounds and the energy approximation in Section2.

## 6. Scope and dependencies

These are forcing-space statements. They do not assert that the optimal extension is the residual of an IPM profile, and they do not identify a valid onset radius T or a remainder bound for any numerical candidate. To apply(1) or(5), those hypotheses must be certified separately. They do not alter the finite-degree family obstructions proved elsewhere.

Dependencies are homogeneous Sobolev duality, elementary polar differentiation, trace-zero approximation on an exterior disk, and Cauchy-Schwarz. The original exterior lower bound was T4-014; its independent Opus review and the new minimum/per-mode remarks are frozen in source/T2_REVIEW_T4_014.md. Arithmetic tables in that review are not certified by the present analytic proof.
