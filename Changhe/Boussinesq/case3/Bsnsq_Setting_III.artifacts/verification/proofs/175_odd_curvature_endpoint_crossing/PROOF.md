# The first odd curvature jet determines endpoint crossing

Status: conditional local theorem, derived independently before exact controls. It strengthens packet174, item3. No existence, global exclusion, or crossing decision for a flat strong unstable graph follows.

## Statement and hypotheses

Assume the local hypotheses of research/174_endpoint_unstable_curve_and_index/PROOF.md: a smooth physical field W with div W=4, with curl W flat at an endpoint p of a smooth zero half-arc gamma, and DW(p)=4n tensor n. Use oriented orthonormal coordinates (s,z) centered at p, with s tangent toward p and away from the arc, and n the positive z direction. Write the arc as z=g(s), s<=0, g(0)=g'(0)=0, and the smooth strong unstable curve as s=sigma(z). Let kappa be signed curvature with respect to the continuous graph normal (-g',1)/sqrt(1+g'^2), equal to n at p, and with arclength increasing toward p. All derivatives at p below are one-sided arc derivatives, which exist smoothly. Flat means every Taylor coefficient vanishes.

Write

    g(s)=sum_(i>=0) k_i s^(i+2)/(i+2)!,
    sigma(z)=sum_(m>=2) sigma_m z^m.

Each sigma_m is a polynomial with rational coefficients in finitely many k_i. It is weighted homogeneous of degree m-1 when k_i has weight i+1, and it changes sign under k_i -> (-1)^i k_i.

If ell=2j+1 is the least odd order for which kappa^(ell)(0)!=0, where j>=0, then

    sigma_m=0 for m<2j+3,
    sigma_(2j+3)=(-1)^j kappa^(2j+1)(0)/[(2j+3)(2j+3)!].     (1)

Consequently the curve enters s>0 in every neighborhood of p. If all odd derivatives of kappa vanish at p, then sigma is flat. Conversely a nonzero odd curvature derivative makes sigma nonflat by(1). Flatness of sigma is only a statement about its jet, not its sign or actual zero set.

If the full coupled equations and analytic transverse-data assumptions in packet174 item2 also hold, the nonflat case is impossible. This is a restricted analytic-data obstruction. In the case where all odd curvature derivatives vanish, those assumptions alone have not supplied the geometric crossing premise.

## Formal determination and polynomial dependence

Packet174 constructs the smooth strong unstable curve by a weighted contraction and proves that its formal jet is uniquely determined by the arc jet. For completeness, flat curl makes the formal jet of W the gradient of a formal potential H. Normalize H(p)=0. Then Lap H=4 and H=grad H=0 on the formal arc. With d=z-g(s), set P(s,d)=H(s,d+g(s)). It satisfies

    (1+g'^2)P_dd-2g'P_sd+P_ss-g''P_d=4,
    P(s,0)=P_d(s,0)=0.                                (2)

Comparing powers of d determines all coefficients. The inverse of 1+g'^2 has constant term1; at every fixed total degree only finitely many of its terms occur and are polynomials in the k_i. Division by positive integers in integrating d does not introduce denominators depending on k_i. Thus each finite jet of H is a rational polynomial in finitely many arc coefficients. The invariant-curve equation

    H_s(sigma(z),z)=sigma'(z)H_z(sigma(z),z)             (3)

determines sigma_m at order m by division by4m: H_z=4z+O(|(s,z)|^2), whereas H_s has no linear term. Every remaining term at that order involves previously determined sigma coefficients. This proves polynomial dependence. Neither series is asserted convergent.

An independent formal construction used for the controls is as follows. Put w=s+iz, and write H=2z^2+Re A(w) with A a formal complex series. Then H_s-iH_z=A'(w)-4iz. The two zero-gradient conditions on the graph are exactly

    A'(s+i g(s))=4i g(s).                              (4)

The series s+i g(s) has derivative1 at0 and hence a unique formal inverse u(w). Therefore A'(w)=4i g(u(w)). This is a separate one-variable construction of the same unique jet, not a claim of a holomorphic extension of the actual smooth field.

## Dilation and reflection

For a positive real a put g_a(s)=a^(-1)g(as). Its coefficients are a^(i+1)k_i. The rescaled formal potential H_a(s,z)=a^(-2)H(as,az) still has Laplacian4 and zero gradient on g_a. Formal uniqueness makes it the potential constructed from g_a. Its strong unstable graph is a^(-1)sigma(az), again by(3) and uniqueness. Consequently

    sigma_m((a^(i+1)k_i)_i)=a^(m-1)sigma_m((k_i)_i).

Since sigma_m is a polynomial, comparison as a polynomial in a proves weighted homogeneity.

Now formally reflect the arc in s: g_*(s)=g(-s), so k_i maps to (-1)^i k_i. The reflected potential H_*(s,z)=H(-s,z) has the same equations, and its unstable graph is -sigma(z). This proves the asserted odd parity of the polynomial sigma_m. The reflection here acts on formal data. It need not be a global symmetry of a B2 endpoint or of its forcing direction.

## From graph jets to arclength curvature jets

For the graph, curvature and the arclength derivative are

    kappa=g''/(1+g'^2)^(3/2),
    D_l=(1+g'^2)^(-1/2)D_s.

At s=0, repeated differentiation gives

    c_i:=D_l^i kappa(0)=k_i+P_i(k_0,...,k_(i-1)).       (5)

To see the leading coefficient, the only highest derivative of g comes from differentiating g'' i times and all factors of (1+g'^2) equal1 at0. Every other term uses lower derivatives. Binomial expansions show that P_i is a rational polynomial. Scaling and reflection of these explicit formulas show that c_i has weight i+1 and parity (-1)^i under the same transformation of k. In particular every monomial in P_i for odd i contains at least one lower odd-index k.

Inducting over the odd indices in(5), vanishing of all odd c_i below ell implies vanishing of all odd k_i below ell, and c_ell=k_ell when ell is the first nonzero odd index. The same induction works to all orders if every odd c_i is zero.

Every monomial of sigma_m contains an odd number, in total multiplicity, of odd-index k_i, since sigma_m has odd reflection parity. If ell is the first available nonzero odd index, any surviving monomial has weight at least ell+1. Therefore sigma_m=0 for m<ell+2. At m=ell+2 the only possible monomial is a constant times k_ell: every additional factor has strictly positive weight. It remains to compute that constant.

## Universal coefficient

Take the formal first variation g(s)=epsilon k s^d/d!, with d=ell+2=2j+3. Write H=2z^2+epsilon H_1+O(epsilon^2). Linearizing the zero-gradient conditions gives H_1(s,0)=0 and H_1z(s,0)=-4k s^d/d!. Its harmonic extension is the finite polynomial

    H_1(s,z)=-4 sum_(l>=0) (-1)^l [d^(2l)/ds^(2l)(k s^d/d!)]
                                      z^(2l+1)/(2l+1)!.

The sum terminates when 2l>d. Only l=j+1 contributes to H_1s(0,z), yielding

    H_1s(0,z)=4(-1)^j k z^d/d!.

The first variation of(3) is 4z sigma'(z)=epsilon H_1s(0,z). Thus the coefficient of epsilon z^d is (-1)^j k/(d d!), proving(1) because k_ell=c_ell in the first-odd case. The actual smooth curve has this formal Taylor jet by the invariance equation and coefficient uniqueness in packet174; only jets, not an off-curve potential identity, are transferred. Its degree d is odd and its coefficient is nonzero. Taylor's theorem therefore gives opposite signs of sigma(z) on the two sides of0, and one side has s>0 arbitrarily near p.

If all odd curvature derivatives vanish, all odd k_i vanish by(5). The odd polynomial sigma_m then vanishes for every m. This proves precisely flatness, with no conclusion about the sign of the smooth remainder.

## Dependencies, scope, and verification

The smooth existence of the strong unstable curve and ambient-flatness propagation are proved in packet174. The present polynomial argument uses only its local derivative, flat curl, and zero-arc hypotheses. The use of(1) to exclude an endpoint additionally requires the actual coupled transport equations and the common connected interval of transverse analyticity in174. No analyticity of the arc or convergence of formal series is assumed. Exact finite algebra controls will be stored in verification/ with their input manifest. No Lean or Lake build is used.
