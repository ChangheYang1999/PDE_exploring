# Critical angular Hardy control of four sector dilation derivatives

## Statement and spaces

Let R be the parity space L2_P(|x|^(-17/2) max(1,r)^(29/4) dX), where P means even in x and odd in y. Set t=log r, p(X)=x^2 y and g(t)=exp(-t/2) for t<0, exp(27t/4) for t>=0. Fix a smooth function chi(t) equal1 at negative infinity and0 at positive infinity. Let a(t)>0 be smooth, equal exp(delta t) for t<=0 and exp((gamma-3)t) for t>=1, with delta>1/4 and gamma<-3/8. All its derivatives used below have bounded ratio to a on the fixed transition interval.

For u in H^(25/4)(R times S1), even under both Cartesian reflections, and j real, define

 h(X)=p(X)[j chi(t)+a(t)u(t,theta)],
 beta_h(t)=j chi(t)+a(t)u(t,pi/2),
 h_R=h-E beta_h=p a(t)[u(t,theta)-u(t,pi/2)].                (1)

The axis trace in (1) exists in the Sobolev sense and agrees with the continuous representative. Let E=X.grad. Then

 sum_(m=0)^4 ||E^m h_R||_R <= C ||u||_(H^(25/4)),           (2)

where C is finite and depends only on a and the fixed angular charts. Thus h_R belongs to the sector graph space R_(4,s) of proof 109 for every fixed degree-zero smooth sector cutoff chi_s.

For the cone-bulk sum space of proof 71, assume the additional bulk summand is supported in {|cos theta|>=epsilon}, and choose chi_s supported in {|cos theta|<epsilon}. Its axis trace is zero and chi_s annihilates that summand. Consequently (2), with the R norm of the bulk summand added, proves a continuous map from the full high sum space into R_(4,s) after subtraction of its axis jet. This only verifies the remainder-domain embedding needed in topics109-110. It does not identify a compatible high scalar target or prove the full high inverse.

## An exact one-dimensional Hardy estimate

Use the unitary Fourier transform on R. For every even Schwartz function f,

 integral_R |x|^(-9/2)|f(x)-f(0)|^2 dx
 <= C_H^2 integral_R |xi|^(9/2)|fhat(xi)|^2 dxi,            (3)

where

 C_H^2=(256/441)(c_s J_s)^2, s=1/4,
 c_s=Gamma((1-s)/2)/(2^s sqrt(pi) Gamma(s/2)),
 J_s=Beta(1/2,s)+Beta(1/2-s,s)+Beta(1/2,1/2-s).             (4)

No optimality of this constant is needed or asserted.

Here is a proof including the fractional step. The inverse Fourier multiplier |D|^(-s), for0<s<1/2, has convolution kernel c_s |x|^(s-1). For instance, insert

 |xi|^(-s)=Gamma(s/2)^(-1) integral_0^infinity tau^(s/2-1) exp(-tau xi^2) d tau

and the inverse Gaussian transform, then substitute tau=x^2/(4v). This gives exactly c_s in the convolution normalization. For the weighted integral operator with kernel

 K(x,y)=c_s |x|^(-s)|x-y|^(s-1)

use the positive Schur weight w(x)=|x|^(-1/2). Scaling x or y to1 gives

 integral K(x,y)w(y)dy = c_s J_s w(x),
 integral K(x,y)w(x)dx = c_s J_s w(y).                    (5)

To check (5), split the scaled variable into (-infinity,0), (0,1), (1,infinity). The first row has beta integrals Beta(1/2,1/2-s), Beta(1/2,s), Beta(1/2-s,s). The column has the same three beta integrals in another order. Every endpoint is integrable precisely because0<s<1/2. Schur's inequality follows directly by Cauchy-Schwarz with weight w(y)/w(x), followed by Tonelli. It yields

 || |x|^(-s)g ||_2 <= c_s J_s || |D|^s g ||_2.             (6)

One may first take Fourier data supported in a compact set away from zero. General g in the displayed homogeneous Sobolev class follows by spectral approximation, the L2 bound (5), and distributional identification of the limit. In particular (6) applies to g=f''.

For even f, f'(0)=0 and f(x)-f(0)=O(x^2). On each half-line integration by parts and Cauchy-Schwarz give

 integral x^(-9/2)|f-f(0)|^2 <= (16/49) integral x^(-5/2)|f'|^2,
 integral x^(-5/2)|f'|^2 <= (16/9) integral x^(-1/2)|f''|^2. (7)

The boundary terms vanish at0 by the stated Taylor orders; they vanish at infinity since f decays and f-f(0) stays bounded. Multiplying (7), using (6) with s=1/4, and applying Plancherel proves (3).

## Periodic angular form

There is a finite constant C_ang such that every reflection-even F in H^(9/4)(S1) satisfies

 integral_0^(2pi) |cos theta|^(-9/2) sin(theta)^2
                   |F(theta)-F(pi/2)|^2 dtheta
 <= C_ang ||F||_(H^(9/4)(S1))^2.                          (8)

To prove this, choose two smooth even cutoff charts about pi/2 and3pi/2, equal1 on smaller neighborhoods. In each chart the local coordinate z has |cos theta| comparable to |z|. Apply (3) to the compactly supported even extension f(z)=eta(z)F(theta_axis+z). On the smaller neighborhood f(z)-f(0)=F(theta)-F(theta_axis). The two axis values agree by reflection symmetry. On the complement of the smaller neighborhoods the weight is bounded, and the difference is bounded in L2 by the H^(9/4) norm and the bounded point-evaluation functional.

For completeness, multiplication by a fixed smooth compact cutoff and passage from a periodic function to a chart extension is bounded in H^(9/4). Integer derivatives through order2 obey Leibniz estimates. For the remaining quarter derivative use the equivalent difference norm of the second derivative:

 integral integral |v(x)-v(y)|^2/|x-y|^(3/2) dx dy.

The term where the cutoff is differenced is bounded by its Lipschitz constant for |x-y|<=1 and by its supremum for |x-y|>1; both resulting one-dimensional integrals converge. The term where v is differenced is the local periodic difference norm. This also proves the required bound for the chart extension. The difference-norm identity follows by Plancherel and the substitution z=xi(x-y): its Fourier weight is a finite positive constant times |xi|^(1/2). Approximation by reflection-preserving trigonometric polynomials extends (8) from smooth functions to the stated Sobolev space.

## Radial derivatives and the critical total order

The exact polar norm of the remainder in (1) is

 ||h_R||_R^2=integral_R g(t)a(t)^2 integral_0^(2pi)
       |cos theta|^(-9/2)sin(theta)^2|u(t,theta)-u(t,pi/2)|^2 dtheta dt. (9)

Moreover

 E^m h_R=r^3 cos(theta)^2 sin(theta)
          (partial_t+3)^m[a(t)(u-u_axis)].                (10)

Expand (10). For m<=4 each term is a fixed multiple of a^(b)(t) times a t derivative of u-u_axis of order l<=4. The factors g(t)^(1/2)a^(b)(t) are bounded: their endpoint exponents are delta-1/4>0 on the left and gamma+3/8<0 on the right. Hence (8) reduces the required squared norms to

 sum_(l=0)^4 integral_R ||partial_t^l u(t,.)||_(H^(9/4)(S1))^2 dt.

The cylinder Fourier variables are (xi,n). For every l<=4,

 |xi|^(2l)(1+n^2)^(9/4) <= (1+xi^2+n^2)^(25/4).          (11)

Plancherel proves (2). Smooth approximation also proves that the derivatives are the maximal distributional E derivatives and that axis subtraction commutes with the t derivatives in the relevant trace space. Since E commutes with every degree-zero cutoff, (2) gives the sector graph assertion.

For the bulk term the R bound was proved in proof 63 directly from delta>1/4, gamma<-3/8 and the angular support. Its zero trace and its annihilation by chi_s are distributional as well as pointwise. Taking the infimum over all high-space decompositions proves the claimed sum-space bound.

## Status and remaining scalar compatibility

The exponent25/4 is sufficient for four sector dilation derivatives without an epsilon loss:4+9/4=25/4. This is a statement about the remainder after exact axis subtraction. A general H^(25/4) cylinder function has only H^(23/4) axis trace; it does not automatically put A beta_h in H_g^6. Thus topics109-110 cannot be combined with (2) to assert J2 on the whole original high space unless the scalar-domain condition is checked separately. Nor does this embedding settle J1, which includes a differentiated jet lift. These are separate regularity requirements.
