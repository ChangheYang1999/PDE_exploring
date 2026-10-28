# Sharper local deficiencies in the finite-part upper bound

## Statement

Let0<alpha<1 and0<rho<1/2. Work on the real or complex homogeneous Euclidean Holder space on R^2, modulo constants, with seminorm [f]_alpha=sup_(x!=y)|f(x)-f(y)|/|x-y|^alpha. Use the kernels K_xx=(z1^2-z2^2)/(2pi|z|^4), K_xy=z1 z2/(pi|z|^4), T_xx=p.v.K_xx, T_xy=p.v.K_xy and R_1^2=T_xx-I/2, with the increment extension proved in ../../../01_setup/PROOF.md. C_alpha and D_alpha denote the sharp scalar seminorm constants of T_xx and R_1^2. The same C_alpha applies to T_xy by rotation.

Retain the explicit quantities a2(alpha), A(alpha), E(rho), N0(rho), L(rho), T(alpha), J_C(alpha,rho), J_D(alpha,rho), B_C(rho), B_D(rho) from ../linear_remainder/PROOF.md. In particular E(rho)=-log(1-rho^2)/2. Define the Catalan constant here by its convergent integral and alternating series,

    G=integral_0^1 arctan(t)/t dt
      =sum_(n>=0) (-1)^n/(2n+1)^2,

and put

    B_C^*(rho)=rho^2/[2(1-rho)^2]
                  [-log(rho)+1/2+2G/pi],
    B_D^*(rho)=rho^2/[2(1-rho)^2]
                  [-log(rho)+1/2+log(2)].

Then the proposed sharper bounds are

    C_alpha <= J_C(alpha,rho)-alpha[B_C(rho)-B_C^*(rho)],
    D_alpha <= J_D(alpha,rho)-alpha[B_D(rho)-B_D^*(rho)].    (1)

They are explicit and hold throughout the stated exponent and radius intervals, conditional only on the already accepted finite-part transport theorem. Both improvements in square brackets are positive. They leave the sharp first and second small-alpha terms unchanged.

For the uniform elementary envelopes in ../linear_envelope/PROOF.md, replace B_C and B_D by B_C^* and B_D^*. Precisely, with0<epsilon<1 and all other quantities K_C,K_D as in that proof, every0<alpha<=epsilon satisfies

    C_alpha <= 2/(pi alpha)+C0
                    +[K_C-B_C+B_C^*]alpha,
    D_alpha <= 2/(pi alpha)+2C0
                    +[K_D-B_D+B_D^*]alpha.                (2)

The retained radial reflection saving can additionally be subtracted from the second bound in(1), after its independent acceptance, because the improved deficiency estimate does not change which flow is retained.

## A sharper estimate for a circle pair

In the circle construction of the parent proof, a pair has own densities u and -u with u>=0, actual densities A=u+e and B=-u+f, and |e|,|f|<=H, where H=1/[2pi(1-rho)^2]. Its extracted opposite-sign mass is

    m=(|A|+|B|-|A+B|)/2.

The sharper estimate is |m-u|<=H. To prove it, first m<=min(|A|,|B|)<=u+H. If u<=H, the lower bound m>=u-H follows from m>=0. If u>H, then A>0 and B<0, so m=min(A,-B)>=u-H. These cases establish the assertion even when the perturbation reverses both signs. The estimate for residual variation |A+B|<=|e|+|f| is unchanged.

The exact cost difference in the parent proof is twice the integral of (m-u)(d^alpha-1) over four pair families at one pole, plus the residual antipodal error. Since d=2r sin(t)<1 and |d^alpha-1|<=alpha[-log(d)], its first error is now at most

    8alpha H integral_0^rho r dr
                   integral_0^(pi/4) [-log(2r sin(t))]dt,  (3)

instead of16alpha H times that integral. No cancellation between distinct pairs is assumed.

The exact angular integral is

    integral_0^(pi/4) [-log(2r sin(t))]dt
         =-(pi/4)log(r)+G/2.                              (4)

For completeness, integrate the Abel-regularized Fourier expansion
-log|1-q exp(2it)|=sum_(n>=1)q^n cos(2nt)/n for0<q<1. As q increases to1, the integral converges to the integrable log-sine singularity; for q>=1/2, its absolute value is bounded by a constant plus |log(sin t)|. Integration of each series term gives sum q^n sin(n pi/2)/(2n^2), which converges absolutely and tends to G/2. This proves(4). The identity with the displayed arctangent integral follows by integrating the geometric expansion of arctan(t), or by dominated convergence from a radial parameter below1.

Radial integration in(3) gives exactly alpha B_C^*(rho). The residual still has mass at most E(rho), so its error remains alpha E(rho)L(rho). Every remaining term in the finite-part identity is unchanged. This proves the first bound in(1).

## Maximum deficiency on a projection edge

Use the parent projection transport plan and its precise retention rule: retain the fraction min(1-q_s,1-q_t) on an edge, where q_s and q_t are its source and target deficiency fractions. Thus the removed fraction is max(q_s,q_t), not their sum.

Parametrize a projection edge by a half-lobe angle0<t<pi/4 and radius0<r<rho. Put lambda=cos(2t) and c(t)=sin(2t)/(2pi)>0. Its original flow density is

    c(t) dr dt/r.

Its source own-kernel marginal has density c(t)/r^2 relative to plane area. Its target is at radius r'=lambda r on the reflected ray. The target own-kernel marginal density is c(t)/(lambda^2 r^2). For r'<lambda rho it is supplied by the projection plan; for lambda rho<r'<rho the complementary Q translation plan supplies that same negative kernel marginal. The two radial portions are disjoint apart from their common boundary. The other pole has the centrally reflected description. The pole disks are disjoint since rho<1/2, and the atoms are not perturbed.

The absolute cross-kernel perturbation is at most H. Consequently, on this edge,

    q_s <= H r^2/c(t),
    q_t <= H lambda^2 r^2/c(t).

These bounds remain true when a fraction reaches1. Since0<lambda<1,

    max(q_s,q_t) c(t) dr dt/r <= H r dr dt.                (5)

This pointwise maximum improves the parent's sum bound H(1+lambda^2)r dr dt. It uses the same retained plan, so its residual mass estimate and all length1 edge estimates remain valid without alteration.

There are four projection families at each pole. Their length is d=r sin(2t)<1. By(5), the removed-flow error is therefore at most

    8alpha H integral_0^rho r dr
                    integral_0^(pi/4)[-log(r sin(2t))]dt.

The angular integral equals (pi/4)[-log(r)+log(2)], using the log-sine integral on(0,pi/2). Radial integration gives alpha B_D^*(rho). The antipodal residual error remains3alpha E(rho)L(rho), and the normalized identity contribution remains1/2. This proves the second bound in(1).

## Positivity, convergence and the uniform envelope

For rho<1/2, -log(rho)>log(2)>0. Also0<G<1, directly from its arctangent integral. Thus

    B_C-B_C^*
      =rho^2/[2(1-rho)^2]
          [-log(rho)+5/2-log(2)-2G/pi] >0,
    B_D-B_D^*
      =rho^2/[4(1-rho)^2][-log(rho)+log(2)+1] >0.

For the first inequality, use -log(rho)>log(2), G<1 and pi>2. All changes above improve finite error estimates only. The parent proofs of principal-value normalization, integrability at the pole, finite removed and residual flow masses, and convergence at infinity remain applicable. The maximum bound(5) adds no singular factor at lambda=0, an endpoint of angular measure zero.

The derivation of the uniform envelope used B_C and B_D only as coefficients of explicitly linear terms. Substituting their replacements therefore proves(2) with no optimization or exchange of limits. Phase uniformity, coordinate rotation and scalar complex projection are inherited from the parent theorem.

## Status

Written before numerical evaluation. OPEN pending independent lead cross-read, particularly the exact target marginal and maximum-deficiency step(5). No displayed decimal changes until that review and directed numerical evaluation are complete.
