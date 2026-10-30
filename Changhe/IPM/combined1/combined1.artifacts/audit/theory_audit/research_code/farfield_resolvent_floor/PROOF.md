# A genuine far-field lower bound for the dyadic inverse

## Exact statement

Use the space Y=Y_(a,s,Rw) of ../dyadic_weighted_closure/PROOF.md, allowing its low summand to use w_Rw=(1+r^2/Rw^2)^(-a/2) with any fixed Rw>0 and keeping all dyadic terms at scale1. Assume0<a<2,0<s<1, q=2+s. Let c>0, b=a-1, and

    beta_infinity=1+c-ca>0.

Let rho be a smooth S1 density and u=U[rho] its smooth canonical velocity. Suppose each Cartesian component of u and of D rho has a finite angular Fourier expansion. For some delta>0 assume that the coefficients of u/r and D rho, and their first three logarithmic radial derivatives, are O(r^-delta) for r>=1. Set L=(cX+u).D-1+U[.].D rho. Suppose L has the consistent injective low realization used in the dyadic theorem.

If its high inverse satisfies

    Y(L^(-1)f)<=M Y(f)                                   (1)

for every f in Y with f_y(0)=0, then necessarily

    M >= 1/beta_infinity.                                (2)

Thus the uniform hypothesis(H) of the dyadic theorem implies(2), since its ball contains k=0. This is an actual inverse bound. It does not follow from a numerical-range inequality. The finite rational campaign backgrounds satisfy the finite-angular and differentiated decay hypotheses with delta=1-1/c; that fact must be checked for any new representation.

## Weighted logarithmic mode formulas

Write t=log r. For one angular mode m odd, write a scalar input as f_m(r)=r^b g_m(t). The canonical Beurling transform B=D_-/D_+ sends it to mode m-2. Put n=m-1. After extracting the same factor r^b, its radial envelope is

    B_m g(t)=g(t)-2n integral_0^infinity exp(-(n-a)v)g(t+v)dv,  n>0,
    B_m g(t)=g(t)+2n integral_0^infinity exp(-(a-n)v)g(t-v)dv,  n<0,
    B_1 g(t)=g(t),                                           n=0.

These formulas follow from solving the first-order radial equation for D_+ with the regular-origin and canonical far-field endpoints. They are also the formulas in ../weighted_l2_commutator/PROOF.md after conjugation by r^(a-1). Every nonzero n is an even integer. Since0<a<2, all displayed kernels are in L1. Translation invariance and differentiation under these integrals therefore give, for every nonnegative integer k,

    ||B_m g||_(H^k(R)) <= C_(m,a) ||g||_(H^k(R)).         (3)

For real inputs U2+iU1=-(I+B)f/2. Thus each finite angular collection has the same bound for its velocity envelopes, with a constant depending only on a and that finite collection. These are exact canonical formulas, including any exterior tails.

## A uniform estimate for inputs supported far from the origin

Let G=r^b sum_m g_m(log r)e^(im theta) be smooth, S1, with finitely many angular modes, g_m in H3(R), and G=0 on r<e^T, T>log8. Then

    Y(G) <= C sum_m ||g_m||_H3,                          (4)

where C depends on a,s,Rw, the fixed cutoffs and angular modes, but not on T or the envelopes.

For the low term, use w_Rw<=Rw^a r^-a, so polar integration is bounded by a constant times sum ||g_m||_2^2. For the dyadic density terms, in the j-th rescaling the prefactor r^b contributes2^(bj), which cancels the external factor2^((1-a)j). On the fixed cutoff annulus all Cartesian derivatives through order3 are bounded by finitely many logarithmic radial derivatives and angular derivatives. Hq is bounded by H3. The cutoff intervals in t have uniformly bounded overlap. Summing proves the density estimate, and(3) proves the same dyadic estimate for U[G].

It remains to control the core term chi0 U[G]. For r<4 only n>0 can contribute in the mode formulas, since all source envelopes vanish for t<T. Its term is a constant times

    r^(n-1)e^(i(n-1)theta) integral_T^infinity exp(-(n-a)v)g_m(v)dv.

Here n>=2 is even, so the spatial factor is a harmonic polynomial. Its H3 norm on r<4 is finite with a mode-dependent bound. The integral is bounded by exp(-(n-a)T)||g_m||_2/sqrt(2(n-a)). This gives the remaining uniform core estimate. The density core is zero. The estimate for a real input follows by its conjugate mode decomposition. This proves(4) without assuming a general unproved Calderon-Zygmund theorem on Y.

## The normalized far-field tests

Choose a fixed nonzero smooth real chi supported in(0,1). For N>=1 set T_N=N+log8 and

    phi_N(t)=chi((t-T_N)/N),
    h_N(r,theta)=r^b phi_N(log r) sin(theta).

Every h_N is compactly supported, smooth and S1. Its only input modes are m=1 and m=-1. In the first mode B is the identity. In the second n=-2 and the convolution is backward in t. Hence U[h_N] vanishes identically on r<exp(T_N). In particular h_N and U[h_N] vanish near the origin, and the exact strain c[h_N]=0 without a corrector.

The low density norm satisfies

    Y(h_N)>=C_lower sqrt(N),                             (5)

with a positive constant independent of N. Indeed r^(2b)r dr w_Rw^2 equals a factor tending to Rw^(2a) times dt, bounded below on t>=T_N for sufficiently large N, and integral phi_N^2=N integral chi^2. Also(3),(4) give Y(h_N)<=C_upper sqrt(N), because all fixed logarithmic derivatives of phi_N have L2 norm at most a constant times sqrt(N).

Let L_infinity=c r partial_r-1. Direct differentiation gives

    (L_infinity+beta_infinity)h_N
       =c r^b phi_N'(log r)sin(theta).

The envelope phi_N' has H3 norm O(N^(-1/2)), so(4),(5) imply

    Y((L_infinity+beta_infinity)h_N)/Y(h_N)=O(1/N).       (6)

The remaining term is

    (L-L_infinity)h_N=u.D h_N+U[h_N].D rho.

It has finitely many odd angular modes and vanishes inside exp(T_N). Factoring out r^b, its envelopes are products of the coefficients u/r or D rho with phi_N, phi_N', or the velocity envelopes from(3). The ordinary product rule through three t derivatives, the assumed O(exp(-delta t)) bounds, and(3) give an H3 envelope bound

    C exp(-delta T_N)||phi_N||_H4=O(exp(-delta T_N)sqrt(N)).

Applying(4),(5) proves

    Y((L-L_infinity)h_N)/Y(h_N)=O(exp(-delta T_N)).       (7)

No tail has been omitted: the m=-1 velocity convolution and every velocity of the resulting finite angular source are included by(3),(4).

## Passage to the inverse bound

Set f_N=Lh_N. The preceding bounds show f_N in Y. It vanishes near zero, because h_N and U[h_N] do, so (f_N)_y(0)=0. The compact smooth h_N belongs to the maximal low domain, and the consistency and injectivity assumption give L^(-1)f_N=h_N. Equations(6),(7) imply

    Y(f_N)/Y(h_N) -> beta_infinity.

Applying(1) and taking the limit proves(2). This argument would also preclude a bounded inverse at beta_infinity=0, if such a low realization were otherwise posited. In the stated theorem beta_infinity>0 is the relevant dyadic closure window.

## Consequence and status

Combining(2) with M Y(F)<=R and the already audited radius ceiling gives the necessary condition

    Y(F) < sqrt(8pi) beta_infinity^2/(1+a).               (8)

This is conditional only on the actual dyadic closure hypotheses and the explicit finite-angular decay assumptions. A certified lower bound violating(8) rules out that particular sufficient scheme. It does not rule out a solution in another space or through another inverse construction.

This is original T4 work, OPEN pending independent review. The proof is analytic; no large-radius numerical wave packet is executed. Dependencies are the exact canonical angular formulas, the stated Y definition, elementary Sobolev comparison on a fixed annulus, and the consistent low inverse.
