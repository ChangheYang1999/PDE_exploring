# A maximal-domain auxiliary inverse near the source

## Statement

Use the unitary Fourier transform fhat(xi)=(2pi)^(-1) integral exp(-iX.xi)f(X)dX on R2 and the inhomogeneous norm ||f||_Hr=||<xi>^r fhat||_2. Let J^r=(1-Delta)^(r/2), s=31/10, t=s-1. Let

    D=diag(A,mu), 10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30,
    b(X)=D(X-P)+w(X), w,q in C_c^4(R2;R2),
    Mhat(xi)=xi_1^2/|xi|^2,
    Uhat(xi)=(xi_1 xi_2,-xi_1^2)/|xi|^2,
    Au=b.grad u-u-gMu+q.Uu.

The multipliers' values at the single frequency zero are immaterial. All suprema of vector or derivative tensors use Euclidean or Frobenius norms. For compact scalar f put

    W_r(f)=(2pi)^(-1) integral <xi>^r |fhat(xi)| dxi,
    alpha_r=[2 sqrt(pi(r-1))]^(-1), r>1,
    beta_r=[2 sqrt(pi(r-1)(r-2))]^(-1), r>2,
    P_s(f)=s 2^(s-2)[W_1(f)+alpha_t ||f||_Hs],
    T_s(w)=s(s-1)2^(s-4) sum_i [W_2(w_i)+beta_t ||w_i||_Hs].

These constants are finite for the stated compact C4 coefficients. Define

    kappa=1687/500,
    E=||div w||_infinity/2+s||Dw||_(infinity,F)+||q||_infinity,
    R=T_s(w)+sum_i P_s(q_i), a_s=kappa-E,
    a_0=1+(A+mu)/2-||div w||_infinity/2-||q||_infinity,
    d=a_0-a_s=1+(A+mu)/2-kappa+s||Dw||_(infinity,F).

If E<kappa, then A on the maximal domain

    D(A)={u in Hs: b.grad u belongs to Hs in distributions}

is closed, densely defined and bijective onto Hs. Its inverse satisfies

    ||A^(-1)||_(Hs->Hs) <= (1+R/d)^s/a_s,   d>=3121/1000.       (1)

No boundary data are imposed. This is an auxiliary operator with compact coefficient deviations from a whole-plane linear source, not the full IPM linearization.

For an additional ell_delta in Hs and the raw canonical strain sigma[u]=psi[u]_xy(0), -Delta psi=partial_x u, define

    C_sigma(s)=1/[8 sqrt(pi(s-1)(s-2))].

The functional extends continuously to Hs, with its exact operator norm C_sigma(s). The operator A+ell_delta sigma on D(A) is invertible if and only if

    Delta_sigma=1+sigma[A^(-1)ell_delta] != 0.                   (2)

When K denotes the right side of (1), its inverse norm is at most

    K+K^2 ||ell_delta||_Hs C_sigma(s)/|Delta_sigma|.             (3)

## Fourier estimates and the source margin

Polar integration gives

    integral <xi>^(-2r) dxi=pi/(r-1),
    integral |xi|^2 <xi>^(-2r) dxi=pi/[(r-1)(r-2)].

Consequently (2pi)^(-1)||vhat||_1<=alpha_r||v||_Hr and (2pi)^(-1)|| |xi|vhat||_1<=beta_r||v||_Hr. For j_s(eta)=<eta>^s, the mean-value theorem and (a+b)^(s-1)<=2^(s-2)(a^(s-1)+b^(s-1)) imply

    |j_s(eta+k)-j_s(eta)|
      <=s 2^(s-2)(|k|<eta>^(s-1)+|k|^s).

The two convolution estimates L1*L2->L2 and L2*L1->L2, including the factor (2pi)^(-1), now prove

    ||[J^s,f]v||_2 <= P_s(f)||v||_Ht,
    ||fv||_Hs <= ||f||_infinity||v||_Hs+P_s(f)||v||_Ht.        (4)

The Hessian of j_s is s<eta>^(s-2)I+s(s-2)<eta>^(s-4)eta eta^T. Its norm is at most s(s-1)<eta>^(s-2). Integral Taylor remainder, the same convex estimate at exponent s-2, and integral_0^1(1-v)dv=1/2 give

    |j_s(eta+k)-j_s(eta)-Dj_s(eta).k|
      <=s(s-1)2^(s-4)|k|^2(<eta>^(s-2)+|k|^(s-2)).

Multiplying by |eta_i| and applying the two convolution bounds proves the identity and remainder bound

    [J^s,w.grad]u=-s sum_ij (partial_j w_i)partial_ij J^(s-2)u+R_wu,
    ||R_wu||_2<=T_s(w)||u||_Ht.                             (5)

The sign follows from the Fourier factors ik_j and -eta_i eta_j. Moreover sum_ij||partial_ij J^(s-2)u||_2^2<=||u||_Hs^2, so the leading term has norm at most s||Dw||_(infinity,F)||u||_Hs. Finiteness of the coefficient quantities follows from W_r(f)<=alpha_(n-r)||f||_Hn for n-r>1: take n=4,r=2 for w and n=3,r=1 for q, and use compact C4 for H4 membership. No unspecified singular-integral constants enter (4) or (5).

For the frozen operator D(X-P).grad-1-gM, Fourier integration by parts gives the real Hs quadratic form with coefficient

    -1-(A+mu)/2+s(A xi_1^2+mu xi_2^2)/(1+|xi|^2)
                         -g xi_1^2/|xi|^2.

The positive fraction is bounded by its homogeneous counterpart. The resulting coefficient is affine in xi_1^2/|xi|^2 and its endpoint negative margins are

    1+A/2+(1/2-s)mu,    1+(1/2-s)A+mu/2+g.

Their box minima are respectively 1687/500 and 159/40. For w.grad integrate the principal term by parts and use (5); for q.U use (4) and ||Uu||_(L2 vector)<=||u||_2. Thus on Schwartz u,

    Re<Au,u>_Hs <= -a_s||u||_Hs^2+R||u||_Ht||u||_Hs.        (6)

The ordinary L2 identity, positivity of M, and the same vector bound give

    Re<Au,u>_2 <= -a_0||u||_2^2.                           (7)

## Maximal transport domain and the semigroup

The field b is globally Lipschitz and grows at most linearly. Picard iteration gives its local flow Phi_tau, and the bound |Phi_tau(X)|+1<=(|X|+1)exp(C|tau|) extends it to every positive and negative time. Differentiating in X gives a C1 diffeomorphism, inverse Phi_-tau, and determinant exp(integral_0^tau div b(Phi_v(X))dv). Therefore T(tau)f=f composed with Phi_tau is a group on L2 with norm at most exp(||div b||_infinity |tau|/2). It is strongly continuous first on compact smooth functions by uniform convergence and then on L2 by density.

Its generator has the exact distributional domain D0={f in L2:b.grad f in L2}. Here are the domain details. For f in D0, smooth cutoffs chi(X/R) converge in graph norm: the extra term (b.grad chi(X/R))f is uniformly bounded by C|f| and supported outside a growing ball. For the resulting compactly supported functions, mollification is a graph approximation because

    b.grad(eta_epsilon*f)-eta_epsilon*(b.grad f)
      = integral grad eta_epsilon(X-Y).(b(X)-b(Y))f(Y)dY
        +integral eta_epsilon(X-Y)div b(Y)f(Y)dY.

Its L2 operator norm is uniformly bounded by ||Db||_infinity integral |Z||grad eta(Z)|dZ+||div b||_infinity. It converges to zero on compact smooth f by direct differentiation, hence on every L2 function by density. Thus C_c^infinity is a graph core for D0. The generator contains this entire graph closure, since it is closed. Conversely, pairing a generator difference quotient with a compact test and changing variables identifies its limit with b.grad f in distributions. This proves the claimed domain and the extension of integration by parts to it.

Conjugate now by J^s. Direct Fourier differentiation gives

    [J^s,D(X-P).grad]J^(-s)
       = multiplier s(A xi_1^2+mu xi_2^2)/(1+|xi|^2).

Equation (5), with u=J^(-s)f, shows that C_s=[J^s,b.grad]J^(-s) is bounded on L2. Equation (4) shows that B_s=J^s(-1-gM+q.U)J^(-s) is bounded there as well. The identities extend to Hs in distributions by Schwartz approximation; the compact C4 multiplications involved act on the displayed Sobolev spaces. Hence

    J^s b.grad u=b.grad J^s u+C_s J^s u,

and b.grad u belongs to Hs if and only if J^s u belongs to D0.

For completeness the bounded perturbation can be constructed directly. Put C=C_s+B_s and define on L2

    S_0(t)=T(t),
    S_(n+1)(t)=integral_0^t T(t-v) C S_n(v)dv,
    S(t)=sum_(n>=0)S_n(t).

Its nth norm is bounded by exp(omega t)||C||^n t^n/n!, omega=||div b||_infinity/2, so the sum converges uniformly on compact time intervals after its first term. The Volterra equation has a unique strongly continuous solution by the iterated integral estimate. Splitting this equation proves the semigroup law. For lambda>omega+||C||, its Laplace transform is

    R_0(lambda)[I-C R_0(lambda)]^(-1),
    R_0(lambda)=integral_0^infinity exp(-lambda t)T(t)dt.

Difference quotients of finite semigroup integrals, followed by a graph limit, show R_0=(lambda-b.grad)^(-1) on D0. Direct multiplication shows the displayed perturbed transform is the inverse of lambda-b.grad-C on D0. Applying the same finite-integral argument to S identifies its generator with b.grad+C on precisely D0. Conjugation gives the Hs semigroup S_A(t)=J^(-s)S(t)J^s with generator A on the asserted maximal domain. Closedness and density follow. Bounded perturbation preserves graph cores, so J^(-s)C_c^infinity is a core; it is contained in the Schwartz class because the multiplier <xi>^(-s) preserves that class. This justifies extending (6) to every u in D(A). Since D(A) is also contained in D0 as an L2 domain, (7) extends as well.

## Decay and inversion

A semigroup trajectory from domain initial data remains in the domain, and A S_A(t)u=S_A(t)Au by difference quotients. Let x(t)=||S_A(t)u||_Hs and y(t)=||S_A(t)u||_2. Equation (7) gives y(t)<=exp(-a_0t)y(0). Fourier Holder interpolation gives ||v||_Ht<=||v||_Hs^(1-1/s)||v||_2^(1/s). From (6), while x>0,

    x'<=-a_s x+R x^(1-1/s)y^(1/s).

Apply this to x^(1/s), multiply by exp(a_s t/s), and integrate. If x reaches zero the semigroup remains zero, so no division at zero is needed. The result is

    x(t)^(1/s)<=exp(-a_s t/s)
       [x(0)^(1/s)+(R/d)y(0)^(1/s)(1-exp(-dt/s))].

The box implies d>=1+(10+99/100)/2-1687/500=3121/1000. Since y(0)<=x(0), this gives ||S_A(t)||<= (1+R/d)^s exp(-a_s t), first on the dense domain and then on Hs. Define A^(-1)f=-integral_0^infinity S_A(t)f dt. The finite integral lies in D(A) and its A image is S_A(T)f-f. The infinite graph limit proves surjectivity and (1). If Au=0, then S_A(t)u=u; decay forces u=0. This also proves uniqueness and both inverse identities.

## Exact strain norm and rank-one reduction

The raw strain symbol evaluated at zero is -i xi_1^2 xi_2/|xi|^2. Its dual Hs norm squared is

    (2pi)^(-2) integral xi_1^4 xi_2^2 |xi|^(-4)<xi>^(-2s) dxi
      = (2pi)^(-2) [integral_0^(2pi) cos^4 theta sin^2 theta dtheta]
                      [integral_0^infinity r^3(1+r^2)^(-s)dr]
      = 1/[64pi(s-1)(s-2)].

The angular integral is pi/8 and the radial one is 1/[2(s-1)(s-2)]. Cauchy-Schwarz gives the stated constant. Equality is attained by the Riesz representer in Hs; its Fourier transform is proportional to i xi_1^2 xi_2 |xi|^(-2)<xi>^(-2s). This is the transform of a real even-in-x, odd-in-y function, so the same sharp constant holds on that real parity subspace. No vanishing jet is imposed in this assertion.

To solve (A+ell_delta sigma)u=f, apply A^(-1), then sigma. If (2) holds, solve the resulting scalar equation to obtain

    u=A^(-1)f-A^(-1)ell_delta sigma[A^(-1)f]/Delta_sigma.

This proves (3) and preserves the domain. If Delta_sigma=0, then v=A^(-1)ell_delta satisfies sigma[v]=-1 and is a nonzero null vector. This proves necessity too. There is no certified value of Delta_sigma for the actual IPM trial in this topic.

## Relation to localization and the actual trial

At an exact modal source P from proof 15, the box for A,mu,g is verified. A C4 cutoff theta, equal to one in B_(2delta)(P) and supported in B_(3delta)(P), gives w=theta(V-D(X-P)), q=theta(grad rho-(0,g)). If C_theta=delta||grad theta||_infinity and M_V,M_rho bound the Frobenius Hessians on that ball, Taylor's formula and div(V-D(X-P))=0 give

    E <= delta { [3s+(9/2)(s+1/2)C_theta] M_V+3M_rho }.      (8)

Indeed ||Dw||<= [3+(9/2)C_theta]M_V delta, ||div w||<= (9/2)C_theta M_V delta, and ||q||<=3M_rho delta. The background regularity ensures finite Hessian bounds on some ball. Thus sufficiently small delta produces an auxiliary inverse, but a numerical norm requires explicit bounds for E and R. Proof 15 alone supplies neither Hessian bounds nor R.

For localization, the identity

    A(chi h)=chi Lh+(V.grad chi)h
                +((0,g)+q).[U,chi]h-chi(X.grad rho/3)c[h]

retains an annular transport term, a nonlocal commutator and the raw strain. None is removed by the auxiliary inverse. In particular an inherited remote norm containing integral |h(X)|/|X-P|^2 dX diverges for any nonzero r^k or r^k log r tail with k>0. Such a local estimate applies directly to a decaying remainder, or after the explicit tail directions and their contributions have been separated. It cannot be used with a finite constant on the entire tail-augmented correction merely by citing (1).

This proof independently audits the earlier source_semigroup theorem and supplies a sharper strain norm. It does not establish a local boundary-value inverse, control gluing errors, certify a global rank-one denominator, or prove nonlinear closure.
