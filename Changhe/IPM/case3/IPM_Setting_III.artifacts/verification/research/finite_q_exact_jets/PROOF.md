# Exact canonical center jets and axis-gradient witnesses for finite Q data

Status: CONFIRMED. Informal proof preceded the independent checker. Manufactured arithmetic checks passed at 21:00:59Z; actual Claude Opus 5.5 lead hand review and a separate 30-digit integral check confirmed formulas (1)-(6) at 21:03Z. Date: 2026-10-20.

## Statement, hypotheses and notation

Let L>0, kappa>1 and let B_j be real polynomials, zero for j>=M. Define

    r = r_c sigma^(1/2) (1-sigma)^(-kappa), r_c=L 2^(-kappa),
    rho = r (1-sigma) sin(theta) sum_j sigma^j B_j(2sigma-1) cos(2j theta).

The map defines a smooth density at the origin with even-x/odd-y parity and sublinear growth exponent 1-1/kappa. Let psi be its canonical full-plane inverse, with no harmonic strain. Write

    rho = a y + b x^2 y + e y^3 + O(r^5),
    psi = c xy + q1 x^3 y + q2 xy^3 + O(r^6).

The coefficients a,c and the scaled coefficients b_c=r_c^2 b, e_c=r_c^2 e, H_c=r_c^2(q1-q2), q1_c=r_c^2 q1, q2_c=r_c^2 q2 have the exact formulas

    a = B0(-1),
    b_c = 2 B0'(-1)-a+B1(-1),
    e_c = 2 B0'(-1)-a-B1(-1),                                  (1)
    c = -a/4 + int_0^1 [(1-s)/4+kappa s/2]
                              [B1(2s-1)-s B2(2s-1)] ds,        (2)
    H_c = -B1(-1)/4 + int_0^1 (1-s)^(2kappa)
                   [1+(2kappa-1)s][B2(2s-1)-s B3(2s-1)] ds,    (3)
    q1_c = (H_c-b_c/3)/2, q2_c = -(H_c+b_c/3)/2.                 (4)

If the stored polynomial coefficients and kappa are rational, every quantity in (1)-(4) is rational and can be computed exactly, including for noninteger kappa. In particular IEEE binary coefficient files have an exact rational interpretation; no coefficient conversion or collocation reconstruction is necessary for the Q files whose u entries are the Chebyshev coefficients.

For rational 0<s<1 put

    f_-(s)=(1-s) sum_j (-s)^j B_j(2s-1),
    f_+(s)=(1-s) sum_j s^j B_j(2s-1),
    d(s)=2s(1-s)/(1-s+2kappa s).

At the corresponding positive radius r(s),

    rho_y(0,r(s)) = f_-(s)+d(s)f_-'(s),
    rho_y(r(s),0) = f_+(s),                                    (5)

while the other density-gradient component is zero on either axis. Thus (5) gives exact rational witnesses for a strict global gradient excess over |a|. Any reported physical radius may be approximate; the defining compact coordinate s and the inequality are exact.

For any real ell, the scaled cubic residual coefficients are

    [x^2 y]R r_c^2 = (3ell-c-1)b_c + 3a q1_c,
    [y^3]R r_c^2   = (3ell+3c-1)e_c + a q2_c.                  (6)

When delta=ell+c-1=0 these reduce to 2(2ell-1)b_c+3a q1_c and 2e_c+a q2_c. Both versions must be distinguished for an approximate state.

If c<0 and q2_c<0, the continuous strain norm strictly exceeds its origin value |c| at sufficiently small positive points on x=0. This last implication concerns the canonical field of the finite interpolant; it neither asserts the profile PDE nor gives a numerical global maximum.

## Proof of the local density and axis formulas

The map satisfies r^2/r_c^2=sigma+O(sigma^2), with a smooth locally invertible relation between sigma and r^2. Expanding B0(2sigma-1)=a+2B0'(-1)sigma+O(sigma^2) and retaining the j=1 term proves (1). Every factor sigma^j cos(2j theta) is a homogeneous even polynomial divided by a smooth radial factor, so the apparent polar formula is smooth at zero. At infinity 1-sigma=O(r^(-1/kappa)); bounded finite polynomials give the stated density and first-derivative growth. The canonical inverse exists by the separately proved cancellation formula.

On x=0, cos(2j theta)=(-1)^j and rho=y f_-(sigma). Logarithmic differentiation of the map gives d sigma/d log r=d(sigma). Differentiating y f_- proves the first formula (5). On y=0 the density has an explicit factor y, and differentiating that factor gives the second formula; parity sets rho_x to zero on both axes. All expressions in (5) use only rational operations at rational inputs.

## Canonical center and quartic harmonic coefficient

Use the angular logarithmic Green formula proved in ../angular_log_inverse/PROOF.md. Write rho/r=sum b_(2j+1)(log r) sin((2j+1)theta). In particular

    b3=(1-sigma)sigma(B1-sigma B2)/2,
    b5=(1-sigma)sigma^2(B2-sigma B3)/2.

The center identity c=-a/4+int b3 d log r and the expression for d log r/dsigma immediately give (2). The integral is convergent at both endpoints, with no unregularized absolute two-dimensional strain integral being used.

For the n=4 stream mode,

    psi4/r^2=(beta4-alpha4)/2,
    alpha4=int_0^infty exp(-6u)b3(log r-u)du,
    beta4=int_0^infty exp(-2u)b5(log r+u)du.

Since b3=B1(-1)r^2/(2r_c^2)+O(r^4),

    lim_(r->0) alpha4/r^2=B1(-1)/(16r_c^2).

Changing variables in beta4 gives beta4/r^2=int_r^infty b5(log t)t^(-3)dt. The limit is finite: b5=O(t^4) at zero and is bounded at infinity. Its value, after multiplication by r_c^2, is

    int_0^1 (1-s)^(2kappa)[(1-s)/4+kappa s/2]
                                      [B2(2s-1)-s B3(2s-1)]ds.

The sin(4theta) coefficient of q1 x^3y+q2 xy^3 is (q1-q2)r^4/8. In detail, (q1-q2)/8 = lim (beta4-alpha4)/(2r^2), so H_c = 4 r_c^2 lim (beta4-alpha4)/r^2. This factor 4 changes the beta-integrand factor [(1-s)/4+kappa s/2] into [1+(2kappa-1)s], and changes the alpha term into -B1(-1)/4. This proves (3). The cubic Poisson equation gives q1+q2=-b/3, proving (4). This derivation fixes the harmonic coefficient by its full-plane integral, not by a profile compatibility constraint.

To compute (3) exactly, convert each finite Chebyshev polynomial to powers of s by the recurrence for T_k(2s-1). For p>-1 and integer k>=0, elementary integration by parts gives

    int_0^1 s^k(1-s)^p ds = k! / product_(j=1)^(k+1)(p+j).

The k=0 case is 1/(p+1); the recurrence follows by one integration by parts, whose endpoint terms vanish. Setting p=2kappa proves the rationality assertion. Large alternating coefficients can cause floating-point cancellation, which exact arithmetic avoids.

## Residual and strain consequences

Insert the displayed Taylor expansions into W.grad rho-rho. The linear velocity is (-cx,cy), the cubic velocity is (-q1 x^3-3q2 xy^2,3q1 x^2y+q2 y^3). Collecting cubic monomials proves (6), and delta=0 gives the special form.

The symmetric velocity gradient has diagonal entry S11=-psi_xy. On x=0, oddness of psi in x forces S12=(psi_xx-psi_yy)/2=0. Thus

    S11(0,y)=-c-3q2 y^2+O(y^4).

When c<0 and q2<0, this is strictly larger than -c=|c| for sufficiently small nonzero y, proving the strain assertion. Likewise a e>0 forces |rho_y(0,y)|>|a| near zero; (5) can replace this qualitative statement by an exact witness. These facts refute a claimed continuous equality with the origin norm when their signs hold. They do not refute a carefully labelled finite sampled maximum, and they do not establish that an exact profile is close to the interpolant.

## Dependencies and scope

Only the finite density formula, the canonical inverse, parity, smooth Taylor expansion and elementary beta integration are used. No exact transport equation, global strain cap, analyticity of an unknown profile or numerical existence conclusion is assumed. Exact computation for a frozen finite coefficient file is a statement about that file, not a rigorous enclosure of any unknown solution.
