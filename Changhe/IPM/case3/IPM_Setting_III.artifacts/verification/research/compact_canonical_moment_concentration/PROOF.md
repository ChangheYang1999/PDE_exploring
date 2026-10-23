# Compact canonical perturbations with concentrated higher moments

Result99. Written2026-10-21 before its supporting algebra checker. This extends the value-versus-jet counterexample of result95 to the higher canonical source moments of result98. The fields below are non-profile test pairs. The conclusion concerns residual differences from a fixed non-profile background, not a sequence with full residual tending to zero.

## 1. Statement

Fix ell>1, D=ell-1, a=4D, an integer n>=2, and a real exponent1<p<2n-1. There are smooth canonical pairs (rho_eps,psi_eps), 0<eps<=eps0, with all the primary symmetries and a common sublinear density and gradient bound, such that

    (rho_eps)_y(0)=a, (psi_eps)_xy(0)=-D,
    rho_eps -> rho0=a y exp(-r^2) in C^1(R2),
    U_eps -> U0 in C^1(R2),
    sup_(y!=0) |R_eps-R0|/|rho0|
                    <=C(eps^(p-1)+eps^(2p-2)) ->0.             (1)

The residual is always R=(ell X+U).grad rho-rho. The quotient in(1) extends continuously across y=0. For small eps, rho_eps has the same strict sign as a y off that axis, and the same estimate up to a factor2 holds with either prompt denominator Nf[rho_eps] or Nv[rho_eps] in place of |rho0|, wherever those denominators are positive.

Let

    I_(2k)[rho]=int_0^infinity r^(1-2k) f_(2k)(r)dr,
    f_(2k)(r)=pi^(-1)int_0^(2pi) rho_x(r,theta)sin(2k theta)dtheta.

These moments converge absolutely for every fixed eps and every k>=1. The perturbation changes exactly one of them:

    I_(2n)[rho_eps]-I_(2n)[rho0]
                       =n^2 2^(4-2n) eps^(p+1-2n),
    I_(2k)[rho_eps]-I_(2k)[rho0]=0 for k!=n.                (2)

The source of the nonzero moment in(2) is supported in the shrinking annulus eps/2<=r<=eps. In particular, every fixed shell with positive inner radius eventually sees zero perturbation, although the total positive change in(2) diverges. This is signed moment concentration, not a statement that the source integrand has one sign.

For n=2, one may take1<p<3. The center coefficient changes are

    delta b=-12 eps^(p-3), delta e=0,
    delta q1=4 eps^(p-3), delta q2=0,
    delta r21=-24 eps^(p-3), delta r03=0,                    (3)

where rho=a y+b x^2y+e y^3+..., psi=-Dxy+q1 x^3y+q2 xy^3+..., and R=r21 x^2y+r03 y^3+... because the center normalization is exact. Thus I4 and a cubic residual coefficient diverge despite(1). For n=3 and3<p<5, both density and velocity converge in C^3 while the frequency6 moment diverges; the cubic density and quartic stream coefficients stay exactly fixed.

## 2. A compact potential gives an exactly canonical pair

Choose chi in C^infinity([0,infinity)), equal to1 for s<=1/4 and zero for s>=1. Set

    Phi_n(x,y)=x^(2n)y chi(x^2+y^2),
    sigma_n=-Delta Phi_n, phi_n=partial_x Phi_n,
    V_n=(-partial_y phi_n,partial_x phi_n).                (4)

All fields are smooth and compactly supported in the unit disc. Sigma_n is even in x and odd in y; phi_n is odd in both coordinates. Commutation of derivatives gives -Delta phi_n=partial_x sigma_n exactly, while V_n is divergence free with curl -partial_x sigma_n. Its compact support makes V_n=o(r). Entire harmonic uniqueness with the specified parities therefore identifies V_n with the canonical velocity. There is no remote harmonic strain or boundary condition.

For r<1/2, the cutoff is constant, so

    sigma_n=-2n(2n-1)x^(2n-2)y,
    phi_n=2n x^(2n-1)y.                                  (5)

Because n>=2, (sigma_n)_y(0)=(phi_n)_xy(0)=0. Define

    h_eps(X)=eps^p sigma_n(X/eps),
    varphi_eps(X)=eps^(p+1) phi_n(X/eps),
    v_eps(X)=eps^p V_n(X/eps).                            (6)

Direct differentiation verifies -Delta varphi_eps=partial_x h_eps and v_eps=(-varphi_eps,y,varphi_eps,x). These fields remain compactly supported in r<=eps, so this is again the canonical inverse. Their local derivatives of order j scale as eps^(p-j) for h_eps and v_eps. They tend to zero in C^j whenever p>j. In particular they tend to zero in C^1. No new scaling symmetry of the normalized transport equation is asserted: (6) only uses the linear inverse law.

## 3. Background, normalization and residual estimate

For rho0=a y exp(-r^2), the canonical stream is

    psi0=-xy J(r), J(r)=r^(-4)int_0^r t^3 a exp(-t^2)dt.

Differentiation proves -Delta psi0=(rho0)_x. The integral gives J(0)=a/4, and J=O(r^-4) at infinity, so U0=O(r^-3) there. These facts and the parities establish the canonical gauge and c0=-a/4=-D. Define rho_eps=rho0+h_eps and psi_eps=psi0+varphi_eps. Equations(5)-(6) fix both a and c exactly. The densities are Schwartz and the perturbation tends to zero in C^1, with support in the unit disc. Hence the primary density and gradient bound holds with a common constant for any fixed0<gamma<1.

Let W0=ell X+U0. Smoothness and parity give |W0,1|<=C|x| and |W0,2|<=C|y| on the unit disc. Smooth parity and compact support of(4) give, on r<=eps,

    |h_eps|<=C eps^(p-1)|y|,
    |partial_x h_eps|<=C eps^(p-2)|y|,
    |partial_y h_eps|<=C eps^(p-1),
    |v_eps,1|<=C eps^p,
    |v_eps,2|<=C eps^(p-1)|y|.                            (7)

Using |x|<=eps in the first transport term yields

    |W0.grad h_eps-h_eps|<=C eps^(p-1)|y|,
    |v_eps.grad h_eps|<=C eps^(2p-2)|y|.

The explicit background derivative is grad rho0=a exp(-r^2)(-2xy,1-2y^2). Equation(7) therefore gives |v_eps.grad rho0|<=C eps^(p-1)|y|. Every perturbation term is zero outside r<=eps, including its velocity. Since |rho0|>=a exp(-1)|y| on that disc and

    R_eps-R0=W0.grad h_eps-h_eps+v_eps.grad rho0+v_eps.grad h_eps,

these estimates prove(1). Also |h_eps|/|rho0|<=C eps^(p-1), so after reducing eps0 one has |rho_eps|>=|rho0|/2 with the same sign. Both Nf and Nv are at least |rho_eps| by their definitions. This proves the normalized residual-difference assertion. It does not make the full residual small; R0 is fixed and nonzero. In fact the background has b0=e0=-a and q1_0=q2_0=a/6, so its x^2y residual coefficient is -2a ell!=0.

## 4. Exact moment concentration

For any smooth canonical pair, the modal Green formula gives

    I_(2k)=4k times the coefficient of r^(2k)sin(2k theta)
                        in the stream Taylor expansion.      (8)

To check the endpoints directly, f_(2k)=O(r^(2k)) at0 by smooth parity, while compactly supported sources vanish at infinity. The Green formula is

    P_(2k)(r)=[r^(-2k)int_0^r u^(2k+1)f_(2k)(u)du
                    +r^(2k)int_r^infinity u^(1-2k)f_(2k)(u)du]/(4k).

Its first term is O(r^(2k+2)) at0, proving(8). Its uniqueness follows from regularity at0 and the sublinear velocity condition at infinity. These are the same endpoint facts used in result98, repeated here for the compact case.

The polynomial phi_n in(5) is homogeneous of degree2n, with highest sine frequency2n. Its highest-frequency coefficient follows from

    cos(theta)^(2n-1)sin(theta)
             =2^(1-2n)sin(2n theta)+lower even sine frequencies.

For example, this identity follows by expanding ((e^(i theta)+e^(-i theta))/2)^(2n-1)(e^(i theta)-e^(-i theta))/(2i) and retaining the highest exponents. Thus the coefficient of r^(2n)sin(2n theta) in phi_n is n 2^(2-2n). Multiplication by4n in(8) gives n^2 2^(4-2n). No other harmonic Taylor term r^(2k)sin(2k theta) occurs: for k<n the degree is wrong, and for k>n the stream polynomial has no such degree. This proves the unscaled form of(2).

Substituting r=eps s in the defining source integral and using partial_x h_eps=eps^(p-1)(partial_x sigma_n)(X/eps) gives the factor eps^(p+1-2k). It proves(2) with exactly the displayed scaling. For r<eps/2, the source in(5) has degree2n-2 and therefore no angular frequency2n. For r>eps it vanishes. The nonzero moment is consequently carried by the stated shrinking annulus.

When n=2, (5)-(6) give delta b=-12t, delta e=0, delta q1=4t, delta q2=0 with t=eps^(p-3). The exact normalized cubic residual identities, also obtained by directly multiplying the Taylor polynomials, are r21=2(2ell-1)b+3a q1 and r03=2e+a q2. Since a=4(ell-1), their changes are -24t and0. This proves(3). The n=3 assertion follows from degree5 density and degree6 stream in(5), and the derivative scaling in(6).

## 5. Scope and dependencies

The construction changes higher canonical moments while preserving the two exact primary center data and strict density sign. It need not preserve a strain cap or the condition rho/(a y)<=1. It is not a family of exact or asymptotically exact transport profiles. It demonstrates that C^1 field convergence, matching center normalization and uniformly small residual differences do not control higher canonical moments, even with an unchanged exterior field. Observing such a moment grow in numerical data therefore does not by itself identify a finite-regularity limit.

Dependencies are elementary smooth cutoff construction, derivative commutation, parity, the explicitly verified radial background inverse and the displayed modal Green formula. Supporting exact polynomial and Fourier checks are recorded separately. Actual Opus5.5 review is pending at creation; no formal verification is claimed or permitted in this run.
