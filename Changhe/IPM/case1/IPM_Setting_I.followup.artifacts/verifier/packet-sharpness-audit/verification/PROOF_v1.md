# Sharp ordinary regularity of a nonzero frozen packet

Date: 2026-10-20. This verifies the non-C^4 claim for the specified frozen packet class. It does not use or prove the full homogeneous expansion.

## Statement, notation and dependencies

Let A>1, g>0, q=2(A-1), b=g/q, h=1+g, and Q=A+1. Let Phi be a nonzero smooth complex function with compact support in R minus{0}, integral Phi=0 and Phi(-t)=-conjugate(Phi(t)). Use the Fourier convention and the exact low-frequency extension in ../packet-dyadic-audit/PROOF.md. That proof defines the real continuous packet v with Fourier density away from eta=0

    Vhat(xi,eta)=sgn(eta)|eta|^(-A-2)
       (1+xi^2/eta^2)^(-b) Phi(xi/|eta|^A).

It proves v is smooth off the origin, |v(X)|<=C(1+|X|)^(1/A), and v is C^(m,alpha)_loc if (m+alpha)A<=h, where m is a nonnegative integer and 0<alpha<1. These are the only properties from that proof used below, besides the displayed Fourier formula.

We prove the following additional assertions.

1. If k is a nonnegative integer and kA>=h, v does not belong to C^k on any neighborhood of the origin. The equality case is included.
2. If m is a nonnegative integer, 0<alpha<1 and (m+alpha)A>h, v does not belong to C^(m,alpha) on any neighborhood of the origin.
3. Thus if 3<h/A<4, v belongs to C^(3,h/A-3)_loc and is not C^4 near the origin. This exact parameter condition is not certified here for any coupled numerical profile.

C^k means continuous ordinary partial derivatives through order k on an open neighborhood, not merely existence of a k-th Peano polynomial at one point. Holder spaces use the usual isotropic Euclidean distance. The first assertion at equality is stronger than required for the lead's strict inequality claim. No new global profile, nonlinear family, or task endpoint follows.

## A fixed compact Fourier projection

Choose a smooth multiplier theta(xi,eta), compactly supported where eta>0, xi!=0 and Phi(xi/eta^A) is not identically zero on the support. Such a multiplier exists because Phi is nonzero away from zero. Both eta and |xi| have positive lower bounds on its support. For integers n>=0 define

    theta_n(xi,eta)=theta(2^(-An)xi,2^(-n)eta),
    T_n v=FourierInverse(theta_n Vhat).

All products here are supported away from the singular origin, so there is no extension ambiguity. After changing variables xi=2^(An)zeta, eta=2^n nu, the scaled symbol is

    a_n(zeta,nu)=nu^(-A-2)
      (2^(-qn)+zeta^2/nu^2)^(-b) Phi(zeta/nu^A).

Indeed the density contributes 2^(-(A+2)n), the amplitude contributes 2^(-gn), and the measure contributes 2^(Qn). Consequently, exactly,

    (T_n v)(2^(-An)s,2^(-n)y)=2^(-hn) H_n(s,y),       (1)

where H_n=FourierInverse(theta a_n). On the fixed compact support of theta, all derivatives of a_n converge uniformly to those of

    a_infinity(zeta,nu)=nu^(-A-2)
                  (zeta^2/nu^2)^(-b) Phi(zeta/nu^A).

The lower bounds for nu and |zeta| justify differentiation of every order. Convergence is in every C^j norm on this support and is O(2^(-qn)) for each fixed j by the mean-value theorem applied to the positive first argument. Integration by parts shows H_n tends to H_infinity in Schwartz space. The function theta a_infinity is not identically zero, so its inverse transform H_infinity is not identically zero. Choose a fixed point Z=(s_0,y_0) with H_infinity(Z)!=0. For

    X_n=(2^(-An)s_0,2^(-n)y_0),

we obtain

    2^(hn) (T_n v)(X_n) -> H_infinity(Z)!=0.          (2)

The multiplier and kernels may be complex; the following absolute-value estimates apply without a reality restriction on theta.

## Localization and the contribution from outside the neighborhood

Suppose a claimed regularity holds for v near zero. Choose a smooth compactly supported real cutoff chi equal to1 on a ball about zero, with its support contained in that neighborhood. Then f=chi v has that regularity globally and is compactly supported. The remainder w=(1-chi)v vanishes on a fixed ball and satisfies |w(Y)|<=C(1+|Y|)^(1/A).

Let K be the Schwartz inverse transform of theta. The kernel of T_n is

    K_n(s,y)=2^(Qn) K(2^(An)s,2^n y).

For X sufficiently close to zero and Y in the support of w, |X-Y| is bounded below by a fixed positive constant. Since A>1,

    |(2^(An)(X_1-Y_1),2^n(X_2-Y_2))|
                          >=2^n |X-Y|.

Given any L>0, choose a Schwartz decay exponent N greater than Q+L and greater than 2+1/A. The absolute convolution integral is bounded by

    C_N 2^(Qn) integral (1+2^n|X-Y|)^(-N)
                                    (1+|Y|)^(1/A) dY
       <= C'_N 2^((Q-N)n) <= C''_L 2^(-Ln).          (3)

The integral after extracting the power of 2 is finite uniformly in these X because |X-Y| is bounded below and N>2+1/A controls infinity. In particular (3) holds at X_n for all sufficiently large n. Thus the exterior contribution is smaller than any prescribed exponential power. It uses growth of the density, not decay of its derivatives.

## Integer regularity obstruction, including the critical integer

For an integer k>=0 put

    b_k(zeta,nu)=(i zeta)^(-k) theta(zeta,nu),
    B_k=FourierInverse(b_k).

It is a smooth compactly supported symbol, because the support is separated from zeta=0. In particular B_k is Schwartz and its integral is b_k(0,0)=0. If f is C^k and compactly supported, the Fourier derivative identity and convolution give

    T_n f=2^(-kAn) B_(k,n) * d_s^k f,
    B_(k,n)(s,y)=2^(Qn) B_k(2^(An)s,2^n y).        (4)

The kernels have uniformly bounded L^1 norm. Equation(4) first gives |T_n f|<=C2^(-kAn). Since d_s^k f is continuous with compact support, it is uniformly continuous. The zero integral of B_k gives the stronger bound

    sup_X |(B_(k,n)*d_s^k f)(X)| ->0.               (5)

To prove(5), change variables to the unscaled kernel and subtract d_s^k f(X). For any fixed kernel argument, the displacement(2^(-An)s,2^(-n)y) tends to zero; uniform continuity makes the difference uniformly small in X on a bounded kernel set. The complement has arbitrarily small L^1 tail, and the difference there is bounded by2||d_s^k f||_infinity. This proves(5), without an unproved approximate-identity assertion.

Combining(3)-(5), if kA>=h then

    2^(hn) |T_n v(X_n)|
        <= 2^((h-kA)n) o(1)+O(2^((h-L)n)) ->0

after taking L>h. This contradicts(2). Hence the asserted local C^k regularity is impossible, including kA=h. Since h>1, k=0 never meets the hypothesis.

## Holder regularity obstruction

Suppose f=chi v belongs to C^(m,alpha) for0<alpha<1 and let F=d_s^m f. Formula(4) holds with m in place of k. In addition to its total zero integral, B_m satisfies

    integral_R B_m(s,y) ds=0 for every y.             (6)

This follows by taking the one-dimensional Fourier transform in y: the resulting function is b_m(0,nu), which vanishes identically because the symbol is supported away from zeta=0. Schwartz decay justifies the integrations.

In the convolution in(4), after changing variables to the unscaled kernel, subtract F(X_1,X_2-2^(-n)y) using(6). The Holder estimate then bounds the difference by

    [F]_alpha 2^(-alpha An)|s|^alpha.

Integrating against |B_m(s,y)| gives

    ||T_n f||_infinity<=C 2^(-(m+alpha)An),           (7)

since B_m is Schwartz. Equations(3) and(7), with L>h, contradict(2) whenever(m+alpha)A>h. This proves assertion2. The strict inequality is essential here: the independently proved positive Holder result includes equality when0<alpha<1.

## Exact scope and verification

Together with the direct dyadic upper estimate, this proves the sharp noninteger Holder threshold h/A and the non-C^4 claim in3<h/A<4. At an integer threshold k=h/A, it also excludes C^k; no preceding Lipschitz or Zygmund classification is asserted. No resonance expansion, genericity assumption, stationary-phase calculation or numerical parameter fit enters the proof. The compact multiplier can be chosen for each nonzero Phi.

The proof depends on the byte-pinned preceding packet proof, Fourier inversion of compactly supported smooth functions, elementary integration by parts, convolution, dominated convergence and the usual derivative identity. There are no formal Lean sources or numerical experiments for this analytic audit. A completed independent second-model review and the resolution of any objection will be stored in verification/ before this result is marked confirmed.
