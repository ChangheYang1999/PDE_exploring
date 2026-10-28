# Low-order Holder boundedness and higher-order loss for the frozen source

## The realization and precise claims

Let A>1 and g>0. Put

    a=g/(A-1), b=(A-1)/A, p=A/(A-1), q=(1+g)/A,
    r(sigma)=b sigma+1/A,

and assume 1<a<A+1. On L2(R^2), let

    L=A x partial_x+y partial_y-1-gM,
    Mhat(xi,eta)=xi^2/(xi^2+eta^2).

The domain is the maximal distributional domain of the dilation A x partial_x+y partial_y in L2. Let R=L^(-1) on this domain. Fix a compact input support K and a smooth inhomogeneous dyadic decomposition defining C_*^sigma=B_(infinity,infinity)^sigma. The following claims hold, with finite constants depending on the displayed parameters, K and the fixed decomposition.

1. R exists on L2, with norm at most 2/(A+3).
2. For 0<alpha<1 and f supported in K, ||Rf||_(C_*^alpha)<=C||f||_(C_*^alpha). For noninteger alpha this is a same-order estimate for the usual bounded Holder norm, up to the fixed norm-equivalence constants.
3. For 1<sigma<a, ||Rf||_(C_*^r(sigma))<=C||f||_(C_*^sigma). No larger output exponent works uniformly on smooth inputs supported in any fixed source neighborhood, even with even-x odd-y parity.
4. For 1<sigma<q, there are smooth compact parity-compatible inputs with bounded C_*^sigma norms for which the local C_*^sigma norm of the output is comparable to N^((sigma-1)/(A-1)), N tending through powers of two.
5. At sigma=1, the dyadic upper bound is C lambda^(-1)(1+log lambda). At sigma=a it is C lambda^(-q)(1+log lambda). For sigma>a, the output belongs to C_*^q with a uniform bound.
6. One fixed smooth compact parity-compatible forcing has a selected solution outside every local C_*^beta, beta>q.

This topic proves these claims. It does not claim an explicit numerical inverse constant. The sharper necessity of the logarithm at sigma=1 is discussed in the audit notes below but is not needed for claims 1-6. Necessity of the sigma=a logarithm in the odd class is not established. No variable-coefficient extension, localized boundary realization or full IPM inverse is inferred.

## Explicit semigroup and domain

Use fhat(zeta)=integral exp(-iX dot zeta)f(X)dX and inverse factor (2pi)^(-2). If B=diag(A,1), direct Fourier transport gives

    (S_t f)hat(zeta)=exp((a-A-2)t)|zeta|^(-a)
        |exp(-Bt)zeta|^a fhat(exp(-Bt)zeta).               (1)

Equivalently S_t=exp(-t)D_t Q_t, where D_t f(X)=f(exp(Bt)X) and

    Q_t(zeta)=[(xi^2+eta^2)/(exp(2(A-1)t)xi^2+eta^2)]^(a/2).

The product is defined directly by this bounded multiplier; separate homogeneous fractional operators at zero frequency are unnecessary. Since 0<=Q_t<=1,

    ||S_t||_(L2 -> L2)<=exp(-(A+3)t/2).

The multiplier cocycle proves the semigroup law. Strong continuity follows from dominated convergence and the dilation group. On smooth Fourier data compactly supported away from zero, differentiation of (1) yields L. Frequency cutoffs near zero and infinity have bounded logarithmic derivatives; their commutator errors vanish in L2 by shrinking support in the tails. Smooth approximation on the remaining annuli proves these test functions form a core for the maximal dilation domain. Alternatively the quadrant-logarithm proof in proof 08 applies with s=0 and mu=1. The bounded multiplier perturbation preserves the domain. Therefore (1) is the semigroup of this exact realization.

Consequently Rf=-integral_0^infinity S_t f dt converges in L2. Its norm bound and two-sided inverse property follow from the closed-generator argument in proof 08. Reflections and real-valuedness are preserved.

## The compact-support gain

Write Delta_N for a homogeneous annular block at dyadic frequency N. For N>=1 and f supported in K,

    ||Delta_N f||_infinity+||Delta_N f||_(L_x^1 L_y^infinity)
          <=C_K N^(-sigma)||f||_(C_*^sigma).             (2)

Inside a fixed enlargement of the x-projection of K, use the usual block bound and the finite strip width. Outside that strip, the Schwartz convolution kernel and the compact support give a bound C_M N^(-M)(1+distance(x,K))^(-M)||f||_infinity, uniformly in y. Choose M>sigma+2 and integrate in x. Applying |D|^a on an annular block costs at most C N^a in either norm, since its localized kernel has L1 norm C N^a.

The kernel of Delta_lambda |D|^(-a) has L1 norm at most C lambda^(-a) and satisfies

    integral sup_x |K_lambda(x,y)|dy <= C lambda^(1-a).

Both identities follow by scaling a fixed Schwartz kernel. The dilation D_t preserves the supremum norm and multiplies the mixed norm in (2) by exp(-At). Equation (1), now as the single well-defined composition on annular data, gives

    ||Delta_lambda S_t Delta_N f||_infinity
      <=C exp((a-1)t)(N/lambda)^a N^(-sigma)
                    min(1,lambda exp(-At))||f||_(C_*^sigma). (3)

Frequency support restricts t, up to fixed additive constants, to

    log(lambda/N)/A <= t <= log(lambda/N), t>=0.

Integrating (3) uses a-1>0 before t=log(lambda)/A and a-A-1<0 after it. The first branch alone is bounded by C N/lambda; splitting at that point gives C N^a/lambda^q. Hence

    ||Delta_lambda R Delta_N f||_infinity
      <=C N^(-sigma) min(N/lambda,N^a/lambda^q)
                                      ||f||_(C_*^sigma). (4)

Fixed annular overlap factors only change C. The two powers cross at N=lambda^b, because (a-1)b=q-1.

For homogeneous low input blocks N<=1, use |fhat|<=||f||_1. The part of the input annulus mapped into the output annulus has area at most C N lambda exp(-At). Fourier inversion in (1) yields

    ||Delta_lambda S_t Delta_N f||_infinity
       <=C||f||_1 lambda^(1-a) N^(a+1) exp((a-A-1)t).

Integrating from t>=log(lambda/N)/A, up to a fixed shift, gives

    ||Delta_lambda R Delta_N f||_infinity
       <=C||f||_1 lambda^(-q) N^(q+2).                   (5)

The sum converges because q>1. The homogeneous splitting of the low block is legitimate in L2, and (5) gives absolute convergence after projecting to high output frequency. The low output block itself is bounded by the L2 inverse and its L2 convolution kernel; compact support bounds ||f||_2 by C_K||f||_infinity.

## Upper bounds from explicit geometric sums

For lambda>=2, (4)-(5) reduce the high-output estimate to

    C||f||_(C_*^sigma) [lambda^(-q)
      +lambda^(-q) sum_(1<=N<=lambda^b) N^(a-sigma)
      +lambda^(-1) sum_(lambda^b<=N<=C lambda) N^(1-sigma)], (6)

where the sums run over powers of two. If 0<sigma<1 the last sum is O(lambda^(1-sigma)), so (6) is O(lambda^(-sigma)). If 1<sigma<a both nonconstant sums are dominated by their crossover endpoints and equal O(lambda^(-r(sigma))). If sigma=1 or sigma=a, the corresponding zero-power sum counts O(1+log lambda) terms. If sigma>a both contributions are O(lambda^(-q)). These facts prove claims 2, 3's upper bound and 5. The finite geometric-series constants, including their divergence as an exponent approaches an endpoint, are part of the unspecified C; they are not omitted numerical errors.

## Packet lower bound

Choose real even compact smooth phi,psi with psi(0)>0 and phihat(kappa_0) nonzero for some kappa_0>0. Put

    f_N(x,y)=N^(-sigma)phi(x)psi(y)sin(Ny),
    t_N=log(N)/(A-1), lambda_N=N^p,
    H_N(Z)=N^(sigma+1/(A-1))Rf_N(Z/lambda_N).

Their C_*^tau input norms are bounded by C_tau N^(tau-sigma). Substitute t=t_N+tau in (1), then v=exp(-tau)nu. On compact frequency sets where kappa and nu are positive and bounded away from zero, direct cancellation gives

    Hhat_N(kappa,nu)=(iN/2)|(kappa,nu)|^(-a)nu^(a-A-2)
      integral_0^(nu N^(1/(A-1))) v^(A+1)
        [1+kappa^2 v^(2A-2)/(N^2 nu^(2A))]^(a/2)
        phihat(kappa(v/nu)^A)
        [psihat(N(v-1))-psihat(N(v+1))]dv.                (7)

Near v=0 the factor is O(v^(A+1)); at infinity the Schwartz decay of phihat dominates every displayed polynomial. These bounds are uniform on the stated frequency compacts and for N>=1. The approximate identity N psihat(N(v-1)) has total mass tending to 2pi psi(0); the negative carrier has no positive root and vanishes. The limit is locally uniform:

    Hhat_N -> i pi psi(0)|(kappa,nu)|^(-a)nu^(a-A-2)
                          phihat(kappa/nu^A).           (8)

It is nonzero on a suitable compact set. Select a Schwartz test W with Fourier support in that set and phase giving a nonzero limiting pairing. All polynomial moments of W vanish. It follows that

    |<Rf_N,lambda_N^2 W(lambda_N .)>|
                        >=c N^(-sigma-1/(A-1)).         (9)

For a fixed ball B containing zero and any beta>0, such tests satisfy

    |<h,lambda^2 W(lambda .)>|
      <=C lambda^(-beta)||h||_(C_*^beta(B))
                               +C_M lambda^(-M)||h||_2. (10)

To prove the local version, take a bounded extension for the restriction norm, multiply by a fixed cutoff equal to one near zero, and apply the whole-space dyadic testing inequality. The difference is away from zero, where the Schwartz tail is smaller than any power in L2. The cutoff extension's extra L2 term is absorbed into the first term. Thus no global smoothness of h is assumed in (10).

Using the L2 inverse to bound the last term of (10), (9) implies

    ||Rf_N||_(C_*^beta(B)) >=c N^(p beta-sigma-1/(A-1)). (11)

The exponent is positive exactly when beta>r(sigma), proving sharpness. At beta=sigma>1 it is (sigma-1)/(A-1). For sigma<q, choose tau=(A sigma-1)/(A-1), which lies in (1,a), in the already proved upper estimate and the input bound. This gives the matching upper power and proves claim 4. All inputs have the stated parity and can be supported in arbitrarily small fixed neighborhoods.

## Fixed smooth forcing at the regularity ceiling

Take nonzero real even compact smooth u,v with nonzero integrals. Let phi=u*u and psi=v*v, so their Fourier transforms are nonnegative, and put f=-phi(x)psi'(y). Define

    G_lambda(S,Y)=lambda^q Rf(S/lambda,Y/lambda^(1/A)).

Substitute t=log(lambda)/A+tau into (1). On compact positive frequency sets away from the axes, every lambda power cancels and

    Ghat_lambda -> -|kappa|^(-a) integral_R exp((a-A-2)tau)
      |(exp(-A tau)kappa,exp(-tau)nu)|^a
      fhat(exp(-A tau)kappa,exp(-tau)nu)d tau.            (12)

At negative infinity, Schwartz decay dominates. At positive infinity, oddness gives fhat=O(exp(-tau)), and the integrand is O(exp(-(A+3)tau)). This proves locally uniform convergence by domination. The limit is nonzero: fhat=-i eta phihat psihat has constant imaginary sign on the positive quadrant, and the other factors are positive, with a strictly nonzero integrand for some finite tau.

The associated tests are lambda^(1+1/A)W(lambda x,lambda^(1/A)y). Their Fourier support lies in an isotropic annulus of radius comparable to lambda, their L1 norm is fixed, and their tails away from a fixed ball are smaller than any inverse power. The same local testing argument as (10) therefore shows that membership of Rf in C_*^beta locally would force the nonzero limiting pairing to be O(lambda^(q-beta)). This is impossible for beta>q. Claim 6 follows.

## Audit of endpoints and applicability

The supplied Analysis I frozen_holder proof also gives two separate lower arguments at input order one. A single oscillatory packet has uniformly bounded classical C1 norm but output derivative proportional to log N. This does not alone show a C_*^1 lower bound; the supplied proof correctly uses a sum of separated carriers for that different claim. Those more detailed endpoint lower statements are not prerequisites of the six theorems proved here.

The low-order result requires compact input support and the L2-selected inverse. It neither proves boundedness on every whole-plane weighted Holder class nor chooses the correct matching for the actual profile. Transfer of the packet obstruction to a variable-coefficient graph domain requires cutoff, coefficient and nonlocal-tail estimates; no such transfer is implicit. Finally, bounding h in a low-order Holder norm does not itself control the derivative in U[h] dot grad h. A nonlinear theorem needs an additional compatible strong norm or a separately proved transport iteration.
