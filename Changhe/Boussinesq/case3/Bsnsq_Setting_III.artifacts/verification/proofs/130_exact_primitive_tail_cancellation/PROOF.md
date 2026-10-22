# Exact two-moment cancellation for polynomial angular source tails

Status: independent informal proof, written before implementation. Exact polynomial, independent Cartesian and nonlinear chart controls passed. Written review182 by the actual claude-opus-5-5 model CONFIRMED the algebra and chart after independently rederiving the signs. Earlier requests175,176,177 and180 did not supply a written audit, as recorded in their status files. This is a necessary tail compatibility and a trial-space construction, not a B2 existence or exclusion theorem.

## Statement and notation

The convention is exactly that of PROMPT.md: grad_perp Psi=(-Psi_y,Psi_x), Omega=-DeltaPsi and curl V=-Omega. The canonical relative kernel is K(z)=(z2,-z1)/(2pi|z|²), used as K(X-Y)-K(-Y). No sign change of temperature or a0 is made. Independent Cartesian and inverse controls use this same convention.

Let beta>2, s=1/beta, m=1-2s in(0,1). Write r=sqrt(x^2+y^2), z=y/r, and let p(z),p1(z) be real polynomials. Consider a smooth odd stream with the differentiated asymptotic expansion

    Psi=r^(2-s) cos(theta) p(z)+r^(2-2s) cos(theta) p1(z)
                                +o_symbol(r^(2-2s)).          (1)

Here x=r cos(theta), y=r sin(theta); the little-o and its spatial derivatives through order3 are uniform in angle, with the corresponding power lowered by the derivative order. Linear stream gauges are allowed and are removed by V=grad_perp Psi-grad_perp Psi(0). Define Omega=-Delta Psi and F=(beta X+V).grad Omega+Omega. Assume the remainder is sufficiently differentiated to make these operations have the displayed uniform asymptotics. Then

    F=r^(-2s) cos(theta) h(z)+o(r^(-2s)),                     (2)
    Dp=(1-z^2)p'-z p,
    L_k p=(k^2-1)p-3z p'+(1-z^2)p'',
    q=-L_(2-s)p,
    h=L_(2-2s)p1+s(Dp)q+(2-s)p(Dq).                         (3)

If h(z)=sum h_j z^j, define the two exact linear moments

    C_sigma(h)=sum_j h_j sigma^j/(j-m), sigma=+1,-1.          (4)

The homogeneous horizontal primitive of the leading source in (2), normalized to vanish on x=0, is smooth on the punctured plane if and only if C_+(h)=C_-(h)=0. In that case it has the polynomial angular form

    T_infinity=r^m cos(theta)^2 Q(z),                        (5)

where Q is the finite polynomial determined by

    Q_j=Q_(j-2)+h_j/(m-j), Q_-2=Q_-1=0.                     (6)

Only coefficients through deg(h)-2 can be nonzero. For h=0 take Q=0. This statement concerns the primitive of the leading homogeneous source. Applying it to the leading tail of the actual primitive int_0^x F requires the limit and integral interchange conditions stated below.

There are explicit smooth stream correction directions which preserve p, the center strain and center vorticity coefficient while changing p1 by arbitrary a+bz. Put R=sqrt(1+x^2+y^2), t=R^(-s), and

    H0=x R^(1-2s)(1-t)^2,
    H1=xy R^(-2s)(1-t).                                    (7)

Adding a H0+b H1 changes the constants in (4) by

    delta C_+=-(m+2)a-(m+3)b,
    delta C_-=-(m+2)a+(m+3)b.                              (8)

Consequently the unique correction

    a=(C_++C_-)/(2(m+2)), b=(C_+-C_-)/(2(m+3))              (9)

annuls both constants. This repairs this leading angular compatibility only.

## Derivation of the source tail

For an angular stream cos(theta)p(sin(theta)), its first angular derivative is Dp and its second is cos(theta)[-p-3zp'+(1-z^2)p'']. The polar Laplacian of r^k A(theta) is r^(k-2)(k^2 A+A''). This proves the expression for q and the next vorticity coefficient q1=-L_(2-2s)p1.

The leading polar velocity is r^(1-s)(-Dp,(2-s)cos(theta)p). The leading vorticity is r^(-s)cos(theta)q. Their transport interaction is r^(-2s)cos(theta)[s(Dp)q+(2-s)p(Dq)]. The Euler operator beta r partial_r+1 kills the leading vorticity and multiplies its r^(-2s) term by-1, giving -q1=L_(2-2s)p1. Terms involving the next velocity or vorticity have strictly smaller degree, as does a constant relative velocity: its contribution has degree-1-s<-2s because s<1. This proves (2)-(3). No exterior harmonic field is added.

## Proof of the moment formula

For the monomial h(z)=z^j the leading source is f_j=x y^j r^(m-2-j). On y=sigma it equals sigma^j u(1+u^2)^((m-2-j)/2). For j>=1 its integral from0 to infinity is sigma^j/(j-m), by the substitution v=1+u^2. Its value f_j(1,0) is0. For j=0 the finite part after subtracting R^m/m is-1/m, obtained from the exact primitive ((1+R^2)^(m/2)-1)/m. Thus all j>=0 give precisely (4). Linearity and the homogeneous primitive criterion in packet129 prove the smoothness equivalence. The hypotheses and proof of that criterion are restated here: a smooth odd homogeneous degree m-1 source integrates to H(x,y)+C_sign(y)|y|^m near each positive horizontal half-axis point, with H smooth; the two constants are its finite-part integrals. A nonzero constant prevents differentiability, while zero constants give smoothness. Reflection treats x<0.

To obtain (5)-(6), directly differentiate x^2 r^(m-2)Q(y/r): its x derivative is

    r^(m-1)cos(theta)[(m+(2-m)z^2)Q-z(1-z^2)Q'].

The coefficient of z^j in the brackets is (m-j)(Q_j-Q_(j-2)). Since 0<m<1, none of these denominators vanishes. This proves (6). The even and odd sums in (6) terminate if and only if their final sums are0, which is equivalent to the sum and difference of C_+ and C_- being0. Once they terminate Q has degree at most deg(h)-2. The differentiated expression has the same source and vanishes on x=0; uniqueness of the horizontal primitive gives (5). This also proves the sufficiency without a regularity bootstrap.

## Center preservation and repair rank

At0, 1-t=(s/2)(x^2+y^2)+O(r^4). Therefore H0=O(r^5) and H1=O(r^4), with smooth Taylor expansions. They do not alter grad Psi(0), Psi_xy(0) or Omega_x(0). At infinity their leading terms are respectively r^(2-2s)cos(theta) and r^(2-2s)cos(theta)z, with smaller terms separated by another r^(-s). Thus p is unchanged and p1 changes to p1+a+bz.

Because 2-2s=m+1, L_(m+1)1=m(m+2) and L_(m+1)z=(m-1)(m+3)z. Applying (4) gives (8). The even and odd directions have nonzero factors m+2 and m+3, proving (9) and uniqueness. No nonlinear term in (3) changes because p is fixed.

Both directions are combinations of the same smooth basis x R^(1-s) T_i(2t-1) T_j(y/R). Their radial polynomials are t(1-t)^2 and t(1-t), respectively. Explicitly, with u=2t-1,

    t(1-t)^2=T0(u)/16-T1(u)/32-T2(u)/16+T3(u)/32,
    t(1-t)=(T0(u)-T2(u))/8.                              (10)

Thus the correction lies in a trial space with at least four radial and two angular basis functions. All coefficients in (3)-(10) are rational when beta and input coefficients are rational. Exact serialized checks need no approximate quadrature.

The directions have velocity growth O(r^(1-2s)) and vorticity decay O(r^(-2s)), with the analogous derivative bounds. Their once-subtracted whole-plane inverse converges absolutely and equals their differentiated relative velocity: the difference is an entire sublinear harmonic vector field vanishing at0, hence0 by growing-ball gradient estimates. Therefore the correction introduces neither an artificial boundary nor an independent velocity gauge.

## Finite coefficient chart and its derivative

Within a center-constrained finite basis with at least four radial and two angular functions, H0 and H1 lie in the kernel of the two center constraints. Their coefficient positions (i,j,shift)=(3,0,0) and (2,1,0) have respective values1/32 and-1/8, with no cross entry. Fix these two free coordinates to0 to choose an affine complement, then apply (9). Every compatible coefficient field in the original affine space is reached uniquely: subtract the unique combination of H0,H1 that puts it in the complement, and (8) shows that repair adds that combination back. Thus the two-coordinate elimination does not discard a compatible field within this finite trial space.

At fixed beta, p and p1 are linear in coefficients and h is linear in p1 and quadratic in p. Therefore C_plus and C_minus, a and b, and the repaired coefficient map are polynomials of degree at most2 in the complement coordinates. Its differential is the exact polynomial differential. For a primitive residual evaluated at the repaired coefficients, apply the ordinary chain rule. Finite quadrature still needs its own accuracy tests. A free-beta derivative must also differentiate every basis exponent, center constraint, tail moment and repair direction; finite differences of the complete residual supply a numerical beta column in the planned implementation.

## Scope, temperature limits and numerical use

This construction preserves the specified center data and leading stream tail, but it can change every off-center residual and sign. It does not enforce the thermal equation, subsequent radial compatibility conditions, nontrivial uniform amplitudes or a nearby solution. It is not a nonexistence result, and a polynomial tail does not limit the broad prompt to finitely many angular modes.

For actual Theta=int_0^x F, the conclusion T_infinity=lim_(lambda->infinity) lambda^(-m)Theta(lambda X) requires a proved interchange. A sufficient condition at fixed x,y is almost-everywhere source convergence and an integrable majorant C u^(m-1) on the horizontal segment in the rescaled variable. The source bound |F(X)|<=C<X>^(m-1) is sufficient: for lambda>=1, lambda^(1-m)|F(lambda u,lambda y)|<=C u^(m-1), since m-1<0. The differentiated expansion (1) plus smoothness on a compact core implies this source bound. Under these assumptions dominated convergence identifies the pointwise homogeneous temperature limit with the primitive. This does not establish uniform convergence of angular derivatives of the actual temperature; that stronger statement needs estimates on remainders and boundary layers near the horizontal direction.

Dependencies are elementary polar differentiation, explicit one-dimensional integrals, the primitive criterion, and the canonical subtracted-inverse uniqueness argument. Complete proof precedes the code. Exact polynomial and Cartesian manufactured controls, tamper checks, nonlinear derivative controls and a written second-model audit have now passed. The fitting search may use this construction; its output still requires independent residual verification.

Written UTC: 2026-10-21T05:40:37.487685+00:00
