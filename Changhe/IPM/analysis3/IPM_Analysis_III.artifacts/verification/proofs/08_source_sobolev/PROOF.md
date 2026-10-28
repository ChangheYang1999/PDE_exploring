# The full nonlocal frozen source has a bounded Sobolev inverse

## Statement, definition, and scope

This is a theorem about a full-plane constant-coefficient dilation model. It is not an inverse theorem for the variable-coefficient profile equation. Let A >= mu > 0, g >= 0, s >= 0, b = 1 + (A+mu)/2, and

    delta_s = min(b-s mu, b+g-s A).

Assume delta_s > 0. Use the unitary Fourier transform in R^2 with prefactor (2 pi)^(-1), and the norm

    ||h||_Hs^2 = integral (1+xi^2+eta^2)^s |hhat(xi,eta)|^2 dxi deta.

Let M have symbol m = xi^2/(xi^2+eta^2), with its value at zero irrelevant. Define

    L h = A x h_x + mu y h_y - h - g M h,
    D(L) = {h in Hs : A x h_x + mu y h_y is in Hs as a distribution}.

Then L is a closed bijection from D(L) onto Hs and

    ||L^(-1) f||_Hs <= delta_s^(-1) ||f||_Hs.                  (1)

The same domain can equivalently require Lh in Hs, because the other terms are bounded on Hs. The result holds on real functions even in x and odd in y. If s>2, then

    |partial_y L^(-1)f(0)| <=
    [delta_s sqrt(8 pi (s-1)(s-2))]^(-1) ||f||_Hs.            (2)

For the explicit rational box

    10 <= A <= 51/5,
    99/100 <= mu <= 101/100,
    29 <= g <= 30,
    s = 31/10,

one may use delta_s = 1687/500 and hence inverse norm 500/1687. Every parameter in this box also has a positive uniform energy margin at every fixed order

    0 <= s < 2373/680.

The strict upper endpoint is the minimum of (b+g)/A over the box. This observation supplies a local Sobolev regularity window, not a global error bound.

No claim here identifies a particular candidate's source coefficients with this box. That requires a separate source-location and derivative certificate. The model omits the spatially varying coefficients and the global normalization rank-one term.

## Independent derivation of the operator and energy

For -Delta psi = partial_x h and U=(-psi_y,psi_x), the velocity has Fourier symbol

    Uhat = (xi eta/(xi^2+eta^2), -xi^2/(xi^2+eta^2)) hhat.

At a source point with density gradient (0,g), the full frozen velocity coupling is therefore -g M h. This already includes the local -h/2 contribution of the second velocity component. There is no additional half factor.

Put w=(1+xi^2+eta^2)^(s/2), F=w hhat, and B=diag(A,mu). Fourier transformation and one product differentiation give

    w (Lh)hat = (D0+C)F,
    D0 = -A xi partial_xi - mu eta partial_eta - (A+mu)/2,
    C = s(A xi^2+mu eta^2)/(1+xi^2+eta^2) - b - g m.

D0 generates the unitary group

    G_t F(zeta) = exp(-(A+mu)t/2) F(exp(-Bt)zeta).

Since s>=0 and A>=mu>0,

    C <= s[A m+mu(1-m)]-b-g m
      = -(b-s mu)(1-m) -(b+g-s A)m
      <= -delta_s.                                          (3)

Both frequency endpoints matter. Dropping the nonlocal term would replace the second margin by b-sA and would destroy the relevant high-order estimate.

## Maximal domain, without boundary conditions at frequency axes

On each open Fourier quadrant write xi=epsilon_1 exp(q_1), eta=epsilon_2 exp(q_2). The isometry

    F -> exp((q_1+q_2)/2) F(epsilon_1 exp(q_1),epsilon_2 exp(q_2))

takes D0 to -A partial_(q_1)-mu partial_(q_2) on L2(R^2_q). Its maximal distributional domain is closed: a further Fourier transform in q makes it multiplication by -i(A omega_1+mu omega_2). Smooth compactly supported q functions form a core. Indeed expanding cutoffs have directional derivatives O(1/R), and convolution by an approximate identity then converges in the function and directional-derivative norms.

This quadrant description also gives the full-plane distributional domain. To check it, use logarithmic cutoffs chi_R(q) equal to one on [-R,R]^2, zero outside [-2R,2R]^2, with first derivatives bounded by C/R. Extend each cutoff by zero outside its quadrant. Each extension is a smooth frequency cutoff avoiding both axes. Its derivative under A xi partial_xi+mu eta partial_eta is O((A+mu)/R). Test the quadrant identities against chi_R times an arbitrary compact smooth global test function and let R grow. The error tends to zero by Cauchy-Schwarz; all other terms converge by dominated convergence. The axes have measure zero. Thus no extra axis-supported distribution is present or permitted by the maximal domain. Conversely, a global identity restricts to each quadrant immediately.

C is a bounded real multiplier. Adding it preserves this closed domain and core. Conjugation by w and the unitary Fourier transform identifies that domain exactly with D(L) above.

## Semigroup and two-sided inverse

The formula

    S_t F(zeta) = exp(-(A+mu)t/2)
      exp(integral_0^t C(exp(-Bu)zeta) du) F(exp(-Bt)zeta)

defines a strongly continuous semigroup. The cocycle identity proves multiplication in time. Strong continuity follows first on a dense core by dominated convergence, then on all L2 by the uniform norm bound. Differentiation on the core gives D0+C, so the closed generator is the domain just established. Equation (3) and change of variables give

    ||S_t||_(L2 -> L2) <= exp(-delta_s t).

For F in L2 set H=-integral_0^infinity S_t F dt as a Bochner integral. Then ||H||<=||F||/delta_s and

    S_a H-H = integral_0^a S_t F dt.

Dividing by a and using strong continuity shows H belongs to the generator domain and (D0+C)H=F. If (D0+C)H=0, semigroup differentiation gives S_tH=H, whereas decay forces H=0. This proves both existence and uniqueness on the stated maximal domain, not merely an energy estimate on test functions. All constructions preserve the two parity projections and real physical functions.

## Exact rational margins and source derivative

At s=31/10, minimizing the two affine expressions over the box gives

    b-s mu = 1+A/2-(13/5)mu >= 1687/500,
    b+g-s A = 1+g+mu/2-(13/5)A >= 159/40.

The second lower bound is larger than the first. More generally the positive-order threshold b/mu is at least 1301/202, and the other threshold (b+g)/A is at least 2373/680. The latter is the smaller one. Both minima follow by monotonicity of their displayed quotients; they are also checked at every corner by exact rational arithmetic.

For s>2, Fourier inversion and Cauchy-Schwarz give

    |h_y(0)|^2 <= (2 pi)^(-2) integral eta^2 (1+r^2)^(-s) dxi deta
                 times ||h||_Hs^2
               = [8 pi(s-1)(s-2)]^(-1) ||h||_Hs^2.

The radial integral is integral_0^infinity r^3(1+r^2)^(-s)dr = 1/[2(s-1)(s-2)], and the angular integral is pi. This proves (2).

For s=31/10, h and Mh have two continuous derivatives, with second derivative Holder order every alpha<1/10. This follows directly from Fourier Cauchy-Schwarz applied to increments: the relevant integral with |zeta|^(4+2alpha)(1+|zeta|^2)^(-s) is finite exactly when s>3+alpha. Consequently differentiating the model equation at zero is legitimate. For f=y exp(-x^2-y^2), f_y(0)=1 and the equation gives

    1=(mu-1)h_y(0)-g(Mh)_y(0).

At mu=1 the second term equals one. Thus division by mu-1 in the isolated transport jet is not a lower bound on the coupled inverse norm. The bounded full-plane inverse above remains uniform through mu=1.

## Dependencies and verification scope

This proof uses Fourier inversion, elementary integration, the explicitly proved maximal-domain and semigroup arguments, and boundedness of the displayed multipliers. It independently audits the supplied Analysis I source_pole proof. The neighboring code checks the rational margins, the Fourier conjugation algebra, and the numerical enclosures with Arb. Such arithmetic checks supplement, and do not replace, the domain proof. No source location, global profile inverse, nonlinear estimate, or residual number is certified by this topic.
