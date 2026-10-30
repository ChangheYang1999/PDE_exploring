# Far-field spectral obstruction for the dyadic space

## Exact statement and scope

Fix c>0, 0<a<2, 0<s<1, Rw>0 and beta=1+c-ca>0. Put q=2+s, b=a-1 and w(X)=(1+|X|²/Rw²)^(-a/2). S1 means even in x and odd in y. Let U[h]=(-R1R2h,R1²h) be the canonical weighted extension on S1 functions. Choose fixed smooth radial cutoffs chi0, chi in[0,1], with chi0=1 on r<=2 and zero on r>=4, and chi=1 on1<=r<=2 and zero outside1/2<r<4. The real Hilbert space Y has norm

    ||h||Y²=||w h||2²+||chi0 h||Hq²+||chi0 U[h]||Hq²
      +sum_(j>=1)2^(2(1-a)j)(||chi(.)h(2^j .)||Hq²
                            +||chi(.)U[h](2^j .)||Hq²).

Vector norms sum the component squares; Hq uses the unitary Fourier transform and multiplier(1+|xi|²)^(q/2). The space in the statement below is the complexification of Y, with this same norm.

Let rho be a smooth S1 background, u=U[rho], and

    Lh=(cX+u).Dh-h+U[h].D rho.

Suppose u/r and D rho have finitely many angular Fourier modes whose coefficients and first three log-radial derivatives are O(r^-delta) for some delta>0 on r>=1. Let L denote any closed densely defined realization on Y which contains the compact smooth test functions constructed below and acts on them by this displayed expression.

For every real xi, lambda_xi=-beta+i c xi lies in the approximate point spectrum of L: there are domain elements e_N with

    ||e_N||Y=1, e_N weakly converges to0 in Y,
    ||(L-lambda_xi)e_N||Y ->0.                         (1)

Consequently the following claims hold.

1. If L generates a strongly continuous semigroup T(t) on Y, then ||T(t)||>=exp(-beta t) for every t>=0. In particular no finite C and beta'>beta can satisfy ||T(t)||<=C exp(-beta' t) for all t>=0.
2. For every compact bounded K:Y->Y the same sequence proves(1) with L+K. Thus a compact or finite-rank bounded perturbation cannot remove this spectral line or the associated long-time decay limitation.
3. If z is in the resolvent set of L+K, then

       ||(z-L-K)^(-1)|| >= 1/|Re z+beta|,              (2)

   where the assertion with zero denominator means no such resolvent point exists. In particular, a bounded inverse at zero has norm at least1/beta.

The semigroup assertion reviews T1's R1-013 remark3. The weakly null and compact-perturbation extensions are separate T4 statements. These are obstructions for this Y and these operator realizations. They do not exclude a profile, a different correction space or a preconditioned residual theorem with different constants. We do not assert that the hyperplane c[h]=0 is invariant under the semigroup. The normalized tests have c[e_N]=0 and (Le_N)_y(0)=0, which is precisely the domain-to-range normalization used by the earlier inverse-floor theorem.

## Logarithmic envelope estimates used in the proof

Write t=log r. For a finite angular sum G=r^b sum_m g_m(t)e^(im theta), supported outside r=exp(T)>8, the independently audited T4-097 estimates give

    ||G||Y <= C sum_m ||g_m||H3(R),                    (3)

with C independent of T and the envelopes, for a fixed set of odd m. The estimate includes the canonical velocity of G. For completeness, the radial Beurling block with n=m-1 is

    B_m g=g-2n int_0^infinity exp(-(n-a)v)g(t+v)dv, n>0,
    B_m g=g+2n int_0^infinity exp(-(a-n)v)g(t-v)dv, n<0,
    B_1 g=g.

The nonzero n are even and a<2, so all kernels are integrable. These formulas bound all Hk envelope norms for each fixed k. On dyadic annuli the factors r^b and2^((1-a)j) cancel; Cartesian derivatives through order3 become bounded combinations of log-radial and angular derivatives on a fixed annulus. Bounded overlap then proves the annular terms in(3). The low term follows from w<=Rw^a r^-a. For the velocity core, only forward blocks n>0 contribute; their inner tails are harmonic polynomials times int_T^infinity exp(-(n-a)v)g(v)dv, bounded by C exp(-(n-a)T)||g||2. These observations prove(3), including the core and nonlocal tails.

## Construction of the singular sequence

Choose a nonzero real smooth eta compactly supported in(0,1), set T_N=N+log8, and define

    p_N(t)=eta((t-T_N)/N) exp(i xi t),
    h_N(r,theta)=r^b p_N(log r) sin(theta).

For fixed xi, ||p_N||Hk=O(sqrt(N)) for every fixed k. Also

    ||p_N'-i xi p_N||H3=O(N^(-1/2)).                   (4)

Each h_N is compactly supported and smooth on the plane. Its input modes are m=1,-1. The first Beurling block is the identity and the second is a backward convolution with n=-2. Hence h_N and both components of U[h_N] vanish on r<exp(T_N), including all origin jets and the exact strain. Complexification causes no change: apply the real formulas to the real and imaginary parts separately.

The low norm has exact angular factor pi and radial density

    r^(2b) r² w(r)²=(Rw²/(1+Rw² exp(-2t)))^a.

This is bounded above and below by positive constants on t>=T_N. Thus(3) and the low term give constants d,D>0, independent of N, such that

    d sqrt(N)<=||h_N||Y<=D sqrt(N).                   (5)

Let L_infinity=c r partial_r-1. Since c b-1=-beta,

    (L_infinity-lambda_xi)h_N
       =c r^b exp(i xi log r) N^-1 eta'((log r-T_N)/N) sin(theta).

Equations(3)-(5) make the ratio of its Y norm to ||h_N||Y be O(N^-1). The difference

    (L-L_infinity)h_N=u.Dh_N+U[h_N].D rho

vanishes below exp(T_N). After r^b is extracted, it has a fixed finite angular support. Product differentiation through order3, the stated background decay and the envelope bounds through order4 show that its H3 envelope norm is O(exp(-delta T_N)sqrt(N)). This also includes the noncompact outer tail of U[h_N]. Applying(3) gives

    ||(L-lambda_xi)h_N||Y/||h_N||Y
         =O(N^-1)+O(exp(-delta T_N)) ->0.             (6)

The same support calculation gives(Le_N)_y(0)=0. Define e_N=h_N/||h_N||Y.

## Weak escape and compact perturbations

The definition of Y is an isometric embedding into the Hilbert direct sum of the weighted low component and all localized density and velocity Hq components. For every fixed dyadic index, both localized components of e_N vanish once N is large enough. The two core components do as well. The weighted low component is bounded and supported on r>=exp(T_N), so its pairing with any fixed weighted L2 test tends to zero by the Cauchy-Schwarz inequality and the vanishing L2 tail of that test.

Thus every fixed component converges weakly to zero. Uniform boundedness in the direct sum lets one first truncate an arbitrary direct-sum test to finitely many components and then bound its remaining tail. This proves e_N weakly converges to zero in Y. Every compact bounded K therefore satisfies ||K e_N||Y->0: otherwise a subsequence of the compact image would converge in norm to a nonzero vector, contradicting its weak limit zero. Together with(6), this proves(1) for L+K.

## Resolvent and semigroup consequences

Let A=L+K, including K=0. If z-A has a bounded inverse, apply it to

    (z-A)e_N=(z-lambda_xi)e_N-(A-lambda_xi)e_N.

Taking norms and the limit gives1<=||(z-A)^(-1)|| |z-lambda_xi|. Choose xi=Im(z)/c to obtain(2). If z=lambda_xi, the right side tends to zero, contradicting bounded invertibility.

If A generates T(t), the domain property permits differentiation of T(t-s)exp(lambda_xi s)e_N. Integration yields

    T(t)e_N-exp(lambda_xi t)e_N
      =int_0^t T(t-s)exp(lambda_xi s)(A-lambda_xi)e_N ds.

For fixed t the semigroup norm is bounded on[0,t], so the right side tends to zero. It follows that ||T(t)||>=|exp(lambda_xi t)|=exp(-beta t). If ||T(t)||<=C exp(-beta't) with beta'>beta, then exp((beta'-beta)t)<=C for all t, a contradiction. On a real Hilbert space the operator norm equals the norm of its complexification, so the conclusion also applies to real semigroup bounds.

## Dependencies and verification status

The exact mode and Y estimates are T4-097, independently accepted in T1 R1-013 and T4-114. No numerical wave packets, finite sections, spectrum plots or distant-domain computations enter this proof. The proof uses only the displayed envelope formulas, Hilbert direct-sum arguments and the differentiated semigroup identity. The source review is frozen in source/T1_REVIEWS_v09.md. The T1 spectral and semigroup remark is independently CONFIRMED by this argument. The additional compact-perturbation statement is OPEN pending independent review.
