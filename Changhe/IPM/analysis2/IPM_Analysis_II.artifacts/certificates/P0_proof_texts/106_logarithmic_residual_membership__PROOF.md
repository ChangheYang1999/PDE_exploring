# The actual residuals belong to the logarithmic forcing spaces

## 1. Statement

All functions and distributions are on R^2. Let f be smooth, even in x and odd in y. Suppose that for some q<1/5 and finite constants C_m,

    |D^m f(X)| <= C_m <X>^(q-m), 0<=m<=4,                 (1)

where <X>=(1+|X|^2)^(1/2) and every derivative norm is the full ordered Euclidean tensor norm. Fix any finite R>=1, A>0, tau>0 and 0<=beta<=1. Set

    omega1=<X>^(-1/5), omega2=(1+4|X|^2)^(2/5),
    w=(1+|X|^2/R^2)^(-11/10), K=log(1-Delta),
    Q=(1+tau K)^beta,
    L(f)=||wf||_(Hdot^-1),
    M_A(f)^2=||omega2 D^2Qf||_2^2
                +A^2||omega1 DQf||_2^2+A^2 2^31 L(f)^2.    (2)

The homogeneous negative norm is the canonical Fourier norm on centrally odd distributions, equivalently the dual norm against centrally odd homogeneous H1 functions. The space in (2) is the completion of the compact smooth S1 core in this norm, realized as distributions.

**Theorem.** Under (1), f belongs to this completed space, with finite M_A norm. No numerical upper bound on that norm is asserted.

Consequently the exact residuals of state131, nb_Mpen2_exact and nb_d2_exact all belong to every forcing space (2), including the native logarithmic spaces used in85 and89. Their large certified lower bounds are finite-norm obstructions, not merely extended-norm alternatives.

## 2. Weighted heat and Bessel bounds

For either omega=omega1 or omega2 there is a finite constant C such that

    omega(X)/omega(Y) <= C(1+|X-Y|)^p,                       (3)

with p=1/5 or p=4/5 respectively. For example, the elementary inequality <X><=sqrt(2)<Y><X-Y> and its scaled version prove (3); for a negative exponent interchange X and Y. In particular 0<p<1.

Let H_t=exp(t Delta). Its positive Gaussian kernel has mass1 and radial moment

    integral |Z|^p (4pi t)^(-1) exp(-|Z|^2/(4t)) dZ
       =(4t)^(p/2) Gamma(1+p/2).

Multiplying a convolution by omega, using (3), and applying the ordinary L2 convolution inequality gives

    ||omega H_t g||_2 <= C'(1+t^(p/2))||omega g||_2.          (4)

Thus H_t acts boundedly on this weighted L2 space. It is strongly continuous at0, first on compact smooth functions by the Gaussian approximate identity and then by density and the uniform bound for0<t<=1.

For a>0 the Bessel multiplier J^(-2a)=(1-Delta)^(-a) has the positive kernel representation

    J^(-2a) = Gamma(a)^(-1) integral_0^infinity
                         s^(a-1)e^(-s) H_s ds.

Using (4) and concavity of s^(p/2), its weighted L2 norm is at most

    C'[1+Gamma(a+p/2)/Gamma(a)] <= C'(1+a^(p/2)).             (5)

The second inequality is Jensen's inequality for a gamma random variable of mean a. At a=0 use the identity operator. All integrals are Bochner integrals in the stated weighted L2 space; the displayed integrable majorants justify them.

## 3. One logarithmic derivative costs two ordinary derivatives

For compact smooth g, the scalar identity log(1+lambda)=integral_0^infinity e^(-t)(1-e^(-t lambda))dt/t gives

    Kg=integral_0^infinity e^(-t)(g-H_tg) dt/t.               (6)

For0<t<=1, g-H_tg=-integral_0^t H_s Delta g ds, so (4) bounds its weighted L2 norm by2C't||omega Delta g||_2. For t>=1, (4) bounds it by [1+C'(1+t^(p/2))]||omega g||_2. Both resulting integrals in (6) converge. Hence

    ||omega Kg||_2 <= C_omega (||omega g||_2
                                  +||omega Delta g||_2),   (7)

with a finite constant independent of g. The identity and bound extend by completion whenever both terms on the right are finite and are approximated by compact smooth functions. The extension agrees with the Fourier multiplier as a tempered distribution, because the heat representation agrees there on the dense core and the same bounds give local distributional convergence.

For0<b<=1, the positive inverse B_b=(1+tau K)^(-b) has the representation

    B_b=Gamma(b)^(-1) integral_0^infinity
                         t^(b-1)e^(-t) J^(-2tau t) dt.

Equation (5) gives the finite weighted L2 bound

    ||B_b|| <= C'[1+tau^(p/2) Gamma(b+p/2)/Gamma(b)].          (8)

At b=0 again use the identity. For0<beta<=1 the exact Fourier identity

    Q=B_(1-beta)(I+tau K)

therefore proves

    ||omega Qg||_2 <= C_(omega,tau,beta)
                        (||omega g||_2+||omega Delta g||_2).
                                                                    (9)

For beta=0 this conclusion is immediate. Derivatives commute with every multiplier here. Apply (9) with omega1 and g=Df, and with omega2 and g=D^2f. The required right sides involve only Df,D^3f,D^2f,D^4f.

## 4. Integrability and membership in the actual completion

At infinity, each principal weighted derivative in (9) is O(r^(q-6/5)); the two extra derivatives decay two powers faster. The radial L2 integral is dominated by a constant times

    integral_1^infinity r^(2q-7/5) dr,

which is finite exactly when q<1/5. Smoothness handles the origin. Thus the high components in (2) are finite.

For the low component, a centrally odd smooth test phi has zero circular mean and satisfies the angular Hardy inequality

    ||phi/r||_2 <= ||Dphi||_2.

Indeed its angular Fourier series contains no zero mode, so the circular Poincare inequality has constant1; integrate it with measure dr/r. Consequently

    |integral wf phi| <= ||r wf||_2 ||phi/r||_2,
    L(f)<=||r wf||_2.                                      (10)

Since R is finite, r wf=O(r^(q-6/5)) at infinity and is O(r) near0. The same q<1/5 condition makes (10) finite.

It remains to show membership in the core completion, rather than only finiteness of formal components. Choose a smooth radial cutoff chi_T, equal to1 on r<=T and zero on r>=2T, with |D^j chi_T|<=C_j T^(-j). Set f_T=chi_T f. These are compact smooth S1 functions. By Leibniz's rule and (1),

    ||omega_j D^j(f-f_T)||_2 ->0,
    ||omega_j Delta D^j(f-f_T)||_2 ->0, j=1,2.

For terms where a derivative hits the cutoff, its factor T^(-l) on the annulus T<=r<=2T combines with D^(m-l)f to give the same bound O(r^(q-m)); the preceding integrable tail dominates each term. Equation (9) then proves convergence of both high components of f_T to those of f. Equation (10), applied to f-f_T, proves convergence of the low component. Thus f_T is Cauchy in M_A and its distributional limit is f. This proves the theorem for the actual compact-core completion.

## 5. Application to the exact case4 residuals

For the exact original state131, let gamma=1/c and delta=1-gamma with

    c=4076476460239181/2251799813685248.

The exact asymptotic algebra05 and the differentiated remainder proof20/RESIDUAL_PROOF.md give (1), in fact at every finite derivative order, for its actual residual with

    q_original=2gamma-1=427123167131315/4076476460239181 <1/5.

The leading linear density term cancels because c gamma=1. The remaining first residual power is q_original. The convergent binomial expansion of every finite regularized-power generator, with its differentiated remainder, gives a uniform symbol bound for r>=2; smoothness supplies the bounded interior constants.

For the exact refits nb_Mpen2_exact and nb_d2_exact, the source audits19,42 and52 certify cancellation of every residual sector above

    q_refit=gamma-6delta=-8696260065638350/4076476460239181 < -2.

The same differentiated finite-generator expansion gives (1) with this smaller q. The additional d2 descendant cancellation does not weaken the conclusion. Hence the theorem applies to all three actual residuals.

This result supplies finiteness and compact-core membership, but no favorable size estimate. In the parameterized d2 space A=2^189,tau=2^-210, the prior lower bound remains M_A(F)>2^178*1936535207, and the ratio to the sufficient threshold remains greater than2^243. The original and other refit exclusions remain unchanged.

## Dependencies and scope

Sections1 to4 are self-contained apart from the elementary Fourier/heat definition of the displayed multipliers. The exact source and differentiated asymptotic facts for the three applications were independently audited in05,20,19,42 and52. Verification checks the rational exponents, these source bindings, the displayed radial powers, and the Gamma/Jensen parameter ranges. No quadrature, spatial mesh, remote computation or formal build is needed. The result does not permit varying the leading profile or exponent in the correction space.
