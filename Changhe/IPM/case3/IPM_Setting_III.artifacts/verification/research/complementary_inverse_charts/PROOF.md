# Complementary endpoint charts for the independent angular inverse

Date: 2026-10-20. Status: derivation CONFIRMED and manufactured tests PASS21:15:58Z. The proof was written before the implementation tests. This concerns finite coefficient formulas, not exact profiles.

## Scope and common inverse

The canonical angular logarithmic Green inverse is proved in ../angular_log_inverse/PROOF.md. If rho/r=sum_j b_j(log r) sin((2j+1)theta), its n=2j+2 stream coefficients are

    P_n=psi_n/r^2=(beta_n-alpha_n)/2,
    E_n=psi_n'/r=[n(alpha_n+beta_n)-b_j-b_(j+1)]/2,
    alpha_n=int_0^infty e^(-(n+2)u)b_j(log r-u)du,
    beta_n=int_0^infty e^(-(n-2)u)b_(j+1)(log r+u)du.

At n=2 the last integral is a primitive. These formulas apply both to the complete density and to the density minus a*y, provided the corresponding center harmonic field is restored in the latter case. Using the complete density avoids subtracting an O(1) affine field at infinity. Using the defect avoids cancellation of a constant slope at the origin. They are algebraically identical. Neither procedure changes the inverse or imposes a finite boundary.

For the defect chart use h=rho-ay, v=U-(-cx,cy), delta=ell+c-1. Then

    R/r = F/r+a*delta*sin(theta),
    F=W.grad h-h+a*v_2.

For the full chart take a=c=0 in this same algebra and use the actual complete b_j and beta_2. It returns the full U/r, rho/r, gradient and R/r. Cartesian denominators divided by r can then be formed without overflow. The exact x-axis is omitted from normalized maxima when both denominators vanish; all raw values remain recorded. Floating point agreement is evidence, not an interval bound.

## Q coefficients

Write s for the compact coordinate and w=1-s, with

    r=r_c*s^(1/2)*w^(-kappa), r_c=L*2^(-kappa),
    b_0=w*(B0(2s-1)-s*B1(2s-1)/2),
    b_j=w*s^j*(Bj(2s-1)-s*B_(j+1)(2s-1))/2, j>=1.

These follow from sin(theta)cos(2j theta)=[sin((2j+1)theta)-sin((2j-1)theta)]/2. The full upper primitive is

    beta_2 = int_s^1 [(1-u)/4+kappa*u/2]*(B1(2u-1)-u*B2(2u-1))du.

It is a polynomial integral, and at infinity is evaluated on v=1-u in [0,w]. This preserves its small value. For s>=1/2, compute

    log w=(log r_c-log r+(log s)/2)/kappa.

Do not reconstruct w by subtracting a rounded s from 1. For s<1/2, direct w=1-s is stable. Derivatives use ds/dlog r=2sw/(w+2kappa s), and differentiate each finite polynomial. The defect chart and exact center primitive are already given in results65 and67.

## The verifier's separate smooth basis

For the verifier's own basis let 0<p<1, alpha=(1-p)/2, L>0,

    s=r^2/(L^2+r^2), w=(1-s)^alpha,
    t=1-2w, tau=1-w,
    rho/r=w*sin(theta)*sum_j s^j B_j(t)cos(2j theta).

The full b_j have the same algebraic expressions as above with this w and t. At the origin, write B0(t)-a=(t+1)Q0(t). Exact binary-rational polynomial division produces Q0 and a. Then

    h_0=tau*(2w Q0(t)-a)-w*s*B1(t)/2,
    h_j=b_j for j>=1.

Compute log(1+r^2/L^2) by a stable logarithmic sum and tau=-expm1(-alpha*log(1+r^2/L^2)), s=-expm1(-log(1+r^2/L^2)). These expressions preserve small quantities. Their logarithmic derivatives are

    s'=2s(1-s), w'=-2alpha*s*w, t'=4alpha*s*w.

For the n=2 primitive, substituting v=w gives

    b_1 dlog r = -[B1(1-2v)-(1-v^(1/alpha))*B2(1-2v)]dv/(4alpha).

Consequently

    beta_2(full)=int_0^w [B1(1-2v)-(1-v^(1/alpha))*B2(1-2v)]dv/(4alpha),
    beta_2(defect)=-int_w^1 [B1(1-2v)-(1-v^(1/alpha))*B2(1-2v)]dv/(4alpha),
    c=-a/4+beta_2(full at w=1).

At small radius the second integral is evaluated by v=1-tau*u on u in [0,1]. At large radius the first is evaluated by v=w*u. Hence neither endpoint primitive requires subtraction of close O(1) integrals. Polynomial factors and the positive integrable power v^(1/alpha) make both integrals convergent. These formulas follow by substitution from the full-plane inverse and are independent of the solver's velocity matrix. The full primitive at w=1 is also computed exactly from the binary polynomial coefficients: expand B_j(1-2v) in powers v^k and use int_0^1 v^(k+q)dv=1/(k+q+1), with q=0 or 1/alpha. Thus the canonical c has an exact rational value for the saved binary exponent alpha; it is not a fitted center constraint.

## Manufactured reference

For B0=a and all other Bj=0 in the smooth basis, the exact full inverse has beta_n=0, all modes n>=4 zero, and

    alpha_2=(a/4)*hypergeometric_2F1(alpha,2;3;-r^2/L^2).

This follows by integrating r^-4 int_0^r a*t^3*(1+t^2/L^2)^(-alpha)dt. The radial density and its derivative are elementary. It supplies an independent high-precision reference at both endpoints. For integer kappa and constant B0 in the Q chart, changing variable to s in the same radial integral gives

    alpha_2=a*(1-s)^(4kappa)/(2s^2)
            *int_0^s u*(1-u)^(-4kappa)*[1+(2kappa-1)u]du.

For rational s and integer kappa>1 this integral and the prefactor are rational. Expanding the degree-two numerator in 1-u evaluates it by three powers, which gives an exact reference distinct from logarithmic quadrature.

## Limitations

Finite precision, quadrature and finite sampled points still need comparison and are not certified. Center strain is independently evaluated from the coefficients, never replaced by 1-ell. Complementary charts correct evaluation cancellation; they cannot correct a candidate's nonzero PDE residual, failed refinement or center defect.

## High-precision density derivative and parameter semantics

For independent arithmetic refinement of the Q density set

    F(s,theta)=sum_j s^j B_j(2s-1)cos(2j theta),
    s_dot=2s(1-s)/(1-s+2kappa*s),  G=(1-s)F.

Direct chain differentiation gives rho/r=sin(theta)G, rho_r=sin(theta)[G+s_dot*(-F+(1-s)F_s)], and rho_theta/r=(1-s)[cos(theta)F+sin(theta)F_theta]. Rotation gives the Cartesian gradient. Both s and w=1-s must be retained as separately solved endpoint quantities. A safeguarded scalar Newton solve in s near zero and in w near infinity avoids subtracting a small endpoint from a rounded number. Polynomial coefficients and metadata are interpreted as their saved binary rational values, then evaluated with increasing precision.

The density exponent of this formula is p=1-1/kappa. Independently saved binary ell and kappa need not obey ell*p=1 exactly, even if the generating solver computed kappa=ell/(ell-1) in machine arithmetic. Consequently an extremely large absolute residual can be dominated by the small but nonzero binary leading coefficient (ell*p-1)*rho. Audit both parameter conventions explicitly: the saved binary ell, and a separately labeled parameter ell_coupled=kappa/(kappa-1) with the density and canonical inverse unchanged. The latter is a change in ell, not a reinterpretation of the saved value. It changes the center defect by exactly ell_coupled-ell. Neither convention establishes an exact solution. This distinction prevents machine rounding of an intended exponent identity from being mistaken for a macroscopic shape defect.
