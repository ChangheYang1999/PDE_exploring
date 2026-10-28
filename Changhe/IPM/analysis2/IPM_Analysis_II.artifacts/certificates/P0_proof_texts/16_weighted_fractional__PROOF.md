# Fractional weighted norms, bounded gradients and rough products

## 1. Statement and scope

Use the weighted E2 norm from07_weighted/SHARP_WEIGHTED_H2_PROOF.md:

    E2(H)^2=||omega2 D2H||_2^2
             +2^22||omega1 DH||_2^2+2^53||(wH)||_(Hdot^-1)^2,
    omega0=<r>^-6/5, omega1=<r>^-1/5,
    omega2=(1+4r2)^2/5, w=(1+r2/2^70)^-11/10.

Derivatives are ordered Cartesian tensors. Functions have the even-x, odd-y density parity. Let J=(1-Delta)^1/2, 0<s<=1/2, and define the completion of the compact smooth parity core by

    N_s^w(g)=E2(J^s g).

All Fourier transforms below are unitary in dimension2, so inversion and the product convolution carry the factor1/(2pi). This is a different norm from the unweighted-bottom N_s of09_quasilinear. The superscript w must be retained when comparing statements.

The following estimates hold:

    (1/(2pi)) int |xi| |g_hat(xi)| dxi
        <=2^11 s^-1/2 N_s^w(g),                          (1)
    ||Dg||_infinity <=2^11 s^-1/2 N_s^w(g),
    [Dg]_(C^(s/2)) <=2^12 s^-1/2 N_s^w(g).               (2)

In(1), the weighted Fourier transform is an L1 function as a distribution; no integrable unweighted Fourier transform is claimed. The same inequalities hold for U[g], with the appropriate Euclidean derivative tensors and the SAME constants. The canonical velocity is the multiplier(-R1R2,R1^2).

Moreover P0(g)<=4N_s^w(g), P1(g)<=2N_s^w(g), P2(g)<=3N_s^w(g). In particular g is locally H2, and

    |g(X)|<=2^13 max(1,|X|)^1/5 N_s^w(g).                 (3)

Finally, for f in the ordinary unweighted H^s space, multiplication by v=Dg is bounded:

    ||v f||_(H^s) <=2^14 s^-1/2 N_s^w(g)||f||_(H^s).     (4)

This includes Euclidean tensor contractions and v=DU[g]. The estimates do not assert a nonlinear inverse. They remove the need to assume a global L2 gradient in the rough multiplication argument. A complete weighted commutator and semigroup argument remains a separate task.

## 2. A dyadic H2 localization with explicit constants

The E2 interpolation inequality of V073 gives P0(H)<=E2(H); also P1(H),P2(H)<=E2(H). Put

    P(t)=35t4-84t5+70t6-20t7, 0<=t<=1,

extended by0 and1 on the adjacent half-lines, and let chi(X)=1-P(|X|-1). Thus chi=1 on B1, vanishes outside B2, takes values in[0,1], and is C3. Its Cartesian derivative bounds are |Dchi|<=3 and |D2chi|_F<=30: on the transition annulus use |P'|<=3, |P''|<=27 and r>=1.

Define chi_0=chi and, for j>=1,

    chi_j(X)=chi(2^-j X)-chi(2^(-j+1) X), t_j=2^j.

They are nonnegative and sum to1 pointwise. For j>=1, chi_j is supported in t_j/2<=r<=2t_j. The rescaled cutoffs have absolute value at most1, first derivative at most9 and Hessian norm at most150. Those bounds also apply to chi_0.

Let F_j(Y)=chi_j(t_jY)H(t_jY). On its support, the change of variables and the three weight definitions give

    ||H(t_j .)||_2<=3t_j^1/5 P0(H),
    ||D_Y H(t_j .)||_2<=2t_j^1/5 P1(H),
    ||D_Y^2 H(t_j .)||_2<=t_j^1/5 P2(H).

For j=0 the same bounds hold on B2. Here5^(3/5)<3 and5^(1/10)<2. Since the Bessel H2 norm is the square root of ||F||2^2+2||DF||2^2+||D2F||2^2, the product rule and sqrt(2)<=2 imply

    ||F_j||_(H2)
       <=t_j^1/5[507P0(H)+40P1(H)+P2(H)]
       <=548t_j^1/5 E2(H).                               (5)

The three coefficients are3+2*27+450, 4+36 and1. No derivative of H above order2 appears.

## 3. Fourier L1 derivative bound without global L2

Write H=J^s g=sum_j f_j, where f_j(X)=F_j(X/t_j). For t>=1,

    <eta/t>^-s <=t^s<eta>^-s.

Scaling the Fourier transform and applying Cauchy-Schwarz therefore give

    (1/(2pi)) int |xi|<xi>^-s |f_j_hat(xi)| dxi
       <=t_j^(s-1) c_s ||F_j||_(H2),
    c_s=1/[2sqrt(pi s(1+s))].                            (6)

The exact integral behind(6) is

    int_R2 |eta|2<eta>^(-4-2s) deta=pi/[s(1+s)].

Because1/5+s-1<=-3/10, the sum of t_j^(1/5+s-1) is less than6. One exact check is(6/5)^10<8, which implies2^-3/10<5/6. Also c_s<1/(3sqrt(s)), since pi>9/4. Equations(5)-(6) then give a constant less than1096/sqrt(s), hence less than2^11/sqrt(s), proving(1).

The distributional equality is part of the argument. The dyadic sum H=sum f_j converges in tempered distributions because P0(H) is finite. J^-s is continuous on tempered distributions and on Schwartz tests. The derivative Fourier series just estimated converges absolutely in L1. Its distributional limit is exactly the Fourier transform of Dg, so no additional distribution supported at xi=0 may be inserted. Fourier inversion proves the bounded continuous derivative representative in(2).

For alpha=s/2, use instead

    int_R2 |eta|^(2+2alpha)<eta>^(-4-2s) deta
       =pi Beta(2+alpha,s-alpha)<=pi/(s-alpha).

The scale exponent becomes1/5+s-1-alpha and has the same summable upper bound. The elementary Fourier difference inequality |exp(iu)-1|<=2^(1-alpha)|u|^alpha proves

    [Dg]_(C^alpha)
       <=548*6*sqrt(2/pi) s^-1/2 N_s^w(g)
       <2^12 s^-1/2 N_s^w(g).

The multiplier for U has Euclidean norm |xi_1|/|xi|<=1. Thus the identical absolute Fourier estimates prove(1)-(2) for U[g] without multiplying the constants by a weighted Riesz bound.

## 4. Weighted lower derivatives and growth

The Bessel kernel b_s of J^-s is a positive probability kernel with second moment2s. This follows directly from

    b_s=int_0^infinity exp(-t)p_t t^(s/2-1)dt/Gamma(s/2),

where the planar heat kernel p_t has second moment4t. The weight ratios at separation z are bounded respectively by

    (1+|z|)^(6/5)<=2(1+|z|2),
    (1+|z|)^(1/5)<=1+|z|,
    (1+2|z|)^(4/5)<=1+2|z|.

Minkowski's inequality, the probability property and the second moment show that J^-s has weighted L2 bounds4,2,3 in the omega0,omega1,omega2 spaces, respectively, for s<=1/2. Derivatives commute with it, proving the three Pj estimates.

Applying the localization calculation(5) directly to g gives

    ||chi_j(t_j .)g(t_j .)||_(H2)
       <=2111 t_j^1/5 N_s^w(g),
    2111=507*4+40*2+3.

The planar H2 embedding has constant1/(2sqrt(pi))<1, by Fourier Cauchy-Schwarz and int <xi>^-4 dxi=pi. At any nonzero point at most three of the cutoffs are nonzero. If r>=1, each relevant t_j is at most2r; if r<1, only j=0 contributes. Since sum_j chi_j=1, evaluation and the triangle inequality give

    |g(X)|<=3*2111*2^(1/5) max(1,r)^(1/5) N_s^w(g)
          <2^13 max(1,r)^(1/5) N_s^w(g).

The last strict bound follows from2^(1/5)<5/4 and3*2111*5/4<8192. This establishes(3) with an explicit finite overlap argument, without assuming that any one partition cutoff equals one at the point.

The weighted velocity bound from V067 and the derivative bounds from V044 give E2(U[H])<=(13/2)E2(H), componentwise with the combined Euclidean norm. Thus the same argument also gives a sublinear representative for U[g], with growth bound(13/2) times(3). The multiplier-defined velocity agrees with the canonical parity-preserving singular integral: the first-order far subtraction converges for this sublinear growth, and the origin value is fixed by parity. No harmonic velocity is added.

## 5. Product with a derivative that is not globally L2

First recall the ordinary Sobolev product estimate, for0<s<=1/2,

    ||vf||_(H^s)<=s^-1/2||v||_(H^(1+s))||f||_(H^s).       (7)

Here is a direct proof of its constant. Fourier Cauchy-Schwarz reduces it to bounding

    int <xi>^(2s)/[<eta>^(2+2s)<xi-eta>^(2s)] deta
       <=2pi/s+16pi<=10pi/s.

On |xi-eta|>=|xi|/2 the first bound is2pi/s. On the complementary disk, <eta>>=<xi>/2 and its area is pi|xi|2/4, giving at most2pi, and hence the stated16pi bound. Division by(2pi)^2 and10<4pi prove(7). The same proof uses Euclidean norms for vector or tensor factors.

Let v=Dg and decompose its Fourier transform into |xi|<=1 and |xi|>1 parts. The low part has normalized Fourier L1 norm at most A=2^11s^-1/2N_s^w(g), by(1). Since<eta+zeta>^s<=2<eta>^s when |zeta|<=1, convolution proves

    ||v_low f||_(H^s)<=2A||f||_(H^s).                     (8)

For the high part,

    ||v_high||_(H^(1+s))
       =||1_(|xi|>1) |xi|<xi> H_hat||_2
       <=sqrt(2)||D2H||_2<=sqrt(2)N_s^w(g).               (9)

Apply(7) to(9), add(8), and use2*2^11+sqrt(2)<2^14. This proves(4). The decomposition is legitimate in distributions by section3; the high piece is in H^(1+s), and the low piece is the bounded continuous inverse of an L1 transform. The same argument for DU[g] uses the pointwise multiplier norm at most1, so its constant is unchanged.

## 6. Completion and limitations

All bounds first hold on the compact smooth core after applying J^s. They pass to the completion. The isometric map J^s:N_s^w -> E2 is onto: apply J^-s to an E2 compact core function; the result is Schwartz with the same parity and can be approximated by smooth compact cutoffs in Schwartz topology. Applying J^s preserves that topology, which implies convergence in E2, including the weighted negative norm by parity Hardy. This proves density of the isometric range, hence surjectivity.

The Fourier and product bounds give no estimate for the full weighted high commutator by themselves. In particular the low component of that commutator must retain the radius-dependent conversion between w and omega0, and the derivative weights must be handled by relative, rather than absolute, weight differences. These are explicit open steps. A theorem for the unweighted N_s cannot be transferred by changing its name.
