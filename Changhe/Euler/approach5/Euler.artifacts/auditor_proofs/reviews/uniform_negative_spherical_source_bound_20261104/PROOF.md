# Uniform control of the negative spherical source

## 1. Statement and notation

Let U be a real C^1 divergence-free field on R^3 with

    E(R)=integral_(|y|<R)|U(y)|^2dy, E(R)/(L R^beta)->1,
    L>0, 0<beta<1.

Set t=(beta-3)/2, k=(beta+1)/2=t+2, m=2-beta, D=k^2+2, H=t^2(k^2+4)/D and C_s=mt^2/D. For a fixed center a define F_a and G_a by integrating respectively r_a^(-beta)|U|^2 and r_a^(2-beta)|DU|_F^2 over 1<r_a=|y-a|<R. Put

    q=tr((DU)^2), Q_a(r)=integral_(S^2)q(a+rn)dn,
    K_a^-(R)=integral_1^R r^(4-beta)[-Q_a(r)]_+dr,
    J_a(R)=integral_1^R r^(4-beta)[Q_a(r)]_+dr.

The sphere measure is 4pi and derivatives are Cartesian. Suppose M=limsup G_a(R)/(beta L log R) is finite. Then M>=H, the same M and L apply at every fixed center, and

    limsup K_a^-/(beta L log R)<=min(M,4(M-H)),
    limsup J_a/(beta L log R)
      <=min(M,m[1-beta+beta u(M)]+4(M-H)),             (1)
    u(M)=min(1,k^2/D+(M-H)/(2beta)).

Writing delta=M-H, with no upper restriction on delta, gives

    limsup K_a^-/(beta L log R)<=4delta,
    limsup J_a/(beta L log R)<=C_s+(m/2+4)delta.       (2)

These are kinematic estimates. In particular K_a^- takes the negative part after spherical integration. It is not the weighted integral of the pointwise negative part of q. The source is LIT391, d0b66693, reconstructed below from its six sections and forty obligations. The only prior bound used in the positive-source conclusion is the confirmed upper tangential envelope A3153; the negative-source conclusion is derived directly.

## 2. Full harmonic defect with C1 regularity

It suffices to work at center zero. Write z=log r and U(rn)=r^t v(z,n). Then F=integral|v|^2 dz dn and G=integral(|v_z+tv|^2+|grad_S v|^2)dz dn. Divergence reads (partial_z+k)(v.n)+div_S v_T=0. The radial degree-zero coefficient is zero, since its flux is zero by the divergence theorem on every whole-space ball.

For a real unit L2 spherical harmonic Y with eigenvalue lambda=ell(ell+1), ell>=1, write

    v_pol=fY n+(f'+kf)grad_S Y/lambda,
    v_tor=h n cross grad_S Y.

The coefficients f,h and the tangential coefficient are C^1; divergence makes f C^2. The integrated velocity and gradient densities are

    K_pol=f^2+(f'+kf)^2/lambda,
    D_pol=2(f'+tf)^2+[f''+(k+t)f'+tkf]^2/lambda
                                  +(lambda-2)f^2,
    K_tor=lambda h^2,
    D_tor=lambda[(h'+th)^2+lambda h^2].              (3)

They follow by differentiating the normal and tangent frame, using the integrated identities for grad_S Y and Hess_S Y. Orthogonal real harmonics and the two vector families are orthogonal for the integrated velocity and Cartesian-gradient quadratic forms. This is not pointwise matrix orthogonality.

Define

    Z_pol=f''^2/lambda+b_lambda f'^2+d_lambda f^2,
    b_lambda=2+(k^2+t^2-H)/lambda,
    d_lambda=(t^2-H)(1+k^2/lambda)+lambda+t^2-2,
    Z_tor=lambda[h'^2+(t^2+lambda-H)h^2].            (4)

Since D-t^2=2beta>0, one has -2<t^2-H=-2t^2/D<0. Thus b_lambda>=1. Directly d_2=0 and b_2=1+k^2/2+2beta/D>=9/8. For lambda>=6,

    d_lambda>=lambda-3-2/lambda>=4lambda/9.

The second inequality follows because 5lambda/9-3-2/lambda is zero at 6 and has derivative 5/9+2/lambda^2>0. The toroidal zero-order coefficient has minimum t^2+2-H=4beta/D>0.

For every smooth nonnegative compactly supported eta(z), integration of the cross terms in (3) gives

    integral eta(D_pol-HK_pol)=integral eta Z_pol
      -(k+t)/lambda integral eta'f'^2
      -[2t+((k+t)tk-Hk)/lambda]integral eta'f^2
      +tk/lambda integral eta''f^2,
    integral eta(D_tor-HK_tor)=integral eta Z_tor
      -t lambda integral eta'h^2.                  (5)

The errors are uniform in degree when measured against K_pol and K_tor: f'^2/lambda<=2(f'+kf)^2/lambda+2k^2f^2/lambda. Summing gives

    integral eta Z=G_eta-HF_eta
              +O_beta(integral(|eta'|+|eta''|)|v|^2), (6)

where Z is the sum of the nonnegative densities (4). First prove this for finite harmonic sums. Local angular H^1 and radial L2 Parseval convergence control the left-hand velocity and gradient quantities, while uniform errors and nonnegative main terms permit the full sum. In particular Z is locally integrable. No angularly weighted boundary-strip estimate is inserted.

## 3. Exact spherical source quadratics

Let A(z)=integral_(S^2)|v.n|^2, K(z)=integral_(S^2)|v|^2 and Qflat=r^(5-beta)Q_0(r). Testing q=div div(U tensor U) with radial functions and integrating by parts gives

    Qflat=A''+(2beta-2)A'+beta(beta-2)A-K'+mK.        (7)

For a finite harmonic sum this is classical, since its radial coefficients f are C^2. For the full C^1 field it is initially distributional. There are no cross terms in A or K because of spherical orthogonality. Substituting A=f^2 and K=K_pol, with p=f' and w=f'', gives

    Q_pol=s_lambda f^2+A_lambda fp+B_lambda fw
                         +C_lambda p^2-(2/lambda)pw,
    s_lambda=m(1-beta+k^2/lambda),
    A_lambda=8k-10+6k(1-k)/lambda,
    B_lambda=2(1-k/lambda),
    C_lambda=2+(3-4k)/lambda.                        (8)

For a toroidal mode A=0 and K=lambda h^2, so

    Q_tor=m lambda h^2-2lambda hh'.                 (9)

For example the fp coefficient in (8) is 4beta-6+(2mk-2k^2)/lambda, which equals the displayed expression after beta=2k-1. This checks the mixed sign independently. The fw coefficient is 2-2k/lambda, and the pw coefficient is negative.

Local L2 convergence of the Cartesian derivative matrices implies local L1 convergence of their trace squares through

    |tr(B^2)-tr(C^2)|<=|B-C|_F(|B|_F+|C|_F).

Thus the spherical sources of finite sums converge to Qflat locally in L1 in z. Formula (7) does not assert second differentiability of a general C^1 velocity; formulas (8)-(9), their L1 limit and the distributional interpretation are sufficient.

## 4. Pointwise estimate for each mode

At lambda=2 the coefficients simplify to

    s_2=mt^2/2, A_2=t(5-3k), B_2=-t,
    C_2=7/2-2k, d_2=0.

Split s_2 f^2 into equal halves and complete one square against A_2 fp and the other against B_2 fw. This gives

    Q_pol>=-R(k)p^2-w^2/m-pw,
    R(k)=(5-3k)^2/m-C_2
        =(29/2-17k+5k^2)/(3-2k).                    (10)

The numerator of R'(k) is -2(5k^2-15k+11). The polynomial in parentheses decreases on (1/2,1) and is 1 at the right endpoint, so R decreases and R(k)<=R(1/2)=29/8. Since m>1 and |pw|<=(p^2+w^2)/2,

    Q_pol>=-(33/8)p^2-(3/2)w^2
             >=-4[b_2p^2+w^2/2]=-4Z_pol.           (11)

Here 4b_2>=9/2>33/8 and 4/2>3/2. The undifferentiated coefficient f is absorbed by its strictly positive spherical source; no division by a vanishing spectral gap occurs.

For lambda>=6, 8k-10 lies between -6 and -2, and the nonnegative term 6k(1-k)/lambda is at most 1/4. Hence |A_lambda|<=6; also 0<B_lambda<=2, C_lambda>=11/6 and s_lambda>0. Drop the latter positive squares and use

    6|fp|<=3f^2+3p^2,
    2|fw|<=lambda f^2+w^2/lambda,
    (2/lambda)|pw|<=(p^2+w^2)/lambda.

It follows that

    Q_pol>=-(lambda+3)f^2-(3+1/lambda)p^2-2w^2/lambda
            >=-4Z_pol,                             (12)

because lambda+3<=16lambda/9, b_lambda>=1 and d_lambda>=4lambda/9. Finally

    m h^2-2hh'=m(h-h'/m)^2-h'^2/m>=-h'^2,

so Q_tor>=-Z_tor. The toroidal zero-order gap need not be inverted either. Summation gives Qflat>=-4Z for finite sums. In the full limit Z increases to a locally integrable sum and the sources converge in L1; choose an almost-everywhere convergent subsequence to obtain

    [-Qflat]_+<=4Z                               (13)

almost everywhere. This controls the negative part after angular integration only.

## 5. Removing cutoffs without gradient-strip estimates

Stieltjes integration gives F(R)=beta L log R+o(log R). The energy ratio also bounds every fixed-width far logarithmic velocity strip by O(1). Take eta_R equal to 1 on [0,log R], supported in (-log 2,log(2R)), between 0 and 1, with two bounded derivatives. The inner strip is fixed; the outer velocity strip is O(1). Equations (6) and (13) imply

    K_0^-(R)<=4 integral eta_R Z
        <=4[G_0(2R)-HF_0(R)]+C_beta,U.              (14)

The possible inner gradient contribution is finite and is included in C_beta,U. No bound on the outer gradient strip is used. Dividing by beta L log R proves the upper value 4(M-H). The same nonnegative defect argument yields M>=H. Independently |q|<=|DU|_F^2 gives K_0^-(R)<=G_0(R), proving the first minimum in (1).

For the positive moment, integration of (7) against eta_R gives

    integral eta_R Qflat=m(1-beta)F_eta+m beta T_eta+O(1), (15)

where T_eta is the tangential weighted energy. To check its boundary terms explicitly, write A=K-T. Their sum is

    integral [eta_R''+(2m-1)eta_R']A
                 +integral eta_R'|v_T|^2,

which is O(1) by the velocity strip bound. A3153, or its compact-cutoff proof, gives limsup T_eta/(beta L log R)<=u(M); using T_eta<=T_0(2R) plus a fixed inner contribution gives the same conclusion. Also F_eta/(beta L log R)->1.

Since eta_R=1 on the desired interval and is nonnegative,

    J_0(R)<=integral eta_R[Qflat]_+
           =integral eta_R Qflat+integral eta_R[-Qflat]_+.

Apply (13), (6) and (15) to obtain the second bound in (1). The other bound J_0<=G_0 is direct. Finally u(M)<=k^2/D+(M-H)/(2beta) and m(1-beta+beta k^2/D)=C_s give (2), for every delta>=0.

## 6. Centers, Euler scope and comparison status

Ball inclusions transfer E(R)/(LR^beta)->1 to every fixed center. Outside a fixed large ball, the gradient weights for two centers differ by a factor tending uniformly to 1, and the integration radii differ by a fixed additive constant. Their fixed omitted regions have finite gradient integrals. Comparing in both directions shows that the extended-real normalized gradient limsup, hence the finite M used here, is center-independent. Reapply Sections 2-5 at each center. This does not claim that the spherical source function itself is translation-invariant.

For a nonzero bounded profile U,P in C^1 satisfying the complete rotating Euler equation, U(R.)->0 distributionally and 2/5<c<1/2, A3053 provides this energy ratio with beta=5-2/c and L>0. Under the additional finite-gradient premise all conclusions hold for every finite omega, without symmetry or a finite harmonic truncation. Velocity decay supplies boundedness and blow-down, but supplies no finite M here.

The complete six-section source, all forty obligations and the formal-source note have been read. This reconstruction uses no LIT389 or LIT390 premise and no numerical calculation. The existing C comparison is reconciled in Section7. No constant optimality, eventual spherical-source sign, pointwise negative-source control or full nonexistence theorem is established. The main conjecture remains open.

## 7. Independent comparison and exclusions

The full C comparison of10:47:03Z, retained as in the team records (SHA2561c38dc15c5fd7976d5830a8e8ab4f999ed52f0d49528b54c0c6699b09ecd1b2d), was read through all six items. Its analytical items1-4 agree with the six sections above. In particular the C1 passage is through local L2 convergence of Cartesian derivatives and local L1 convergence of their trace squares, followed by an almost-everywhere subsequence. The full sum Z is locally integrable and controls every partial sum. There is no finite harmonic truncation in the result.

The source has the same d0b66693 hash. The negative part remains outside the angular integral. Item4 points out that m(1-beta)-4H is negative when the signed identity and the defect bound are combined. This causes no sign reversal error: F_eta/(beta L log R) tends to1, and the finite-radius bound uses F_eta>=F(R) for that negative coefficient. Equivalently Section5 keeps the two estimates separate until their normalized limits are taken. Neither argument assumes bounded gradient energy on the outer strip.

Items5-6 contain numerical comparisons and candidate sharper constants, including a separate optimization over pulse shapes. They are not certified by this review. The exact constant4 theorem requires none of them. The independent analytical checks here also do not certify the comparison's sampled Cartesian identities; those identities have the direct derivations in Sections2-4 instead. C is an existing agent configured as model; actual provider execution is independently unattested. No new agent, model client, diagnostic or external source was used.
