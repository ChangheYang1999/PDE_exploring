# Exact vertical-axis coefficient of the canonical modal residual

Date 2026-10-22T02:59:40.356713+00:00. Proof written before new scalar enclosures. Status OPEN pending two independent arithmetic paths, complete actual Claude Opus5.5 review and later own adjudication. This is a forcing-space obstruction for one exact trial, not an exclusion of an exact profile near X3.

## Definition and statement

Let rho be the exactly joined, canonically normalized modal trial of modal_repair/PROOF.md, using the endpoint knots a,b as exact log radii, the exact binary64 input k,D,S,Aout, the exact recomputed C6 join coefficients Ei,Eo, and the exact real scalar change to A00 only. Put ell=1/k, sigma=3ell-1, beta=ell+sigma=4ell-1, U=(-psi_y,psi_x), -Delta psi=partial_x rho, with the canonical sublinear inverse. The stationary residual is

 epsilon=(ell X+U).grad rho-rho.

Near the origin the density is x^2y+O(r^5) with the differentiated bounds and finite regularity established in center_obstruction and modal_graph_scaling. For y>0 set b0(y)=rho_xx(0,y)/2, u(y)=U2(0,y). Define exact constants

 B=exp(-2a) sum_(m=0)^259 (-1)^m D_(m,1),
 I=integral_(-infinity)^infinity [a1(t)+a2(t)-a3(t)-a4(t)]dt,
 H4=I/16-1/64,
 A=-1/6-4H4,
 Q=2 beta B-5A=2 beta B+25/48+5I/4.                       (1)

Here the subscripts on D use j=1,...,7; stored column0 is j=1. The symbol b0(y) is an axis trace, distinct from the exterior endpoint b. The mode functions a_m are the exact joined ones. I converges and is rational, because modes1 through4 have zero inner constant and are unaffected by the sole scalar modification of mode0. The exact formula for I is given below.

Then, as y decreases to0,

 b0(y)=y+B y^3+o(y^3), b0'(y)=1+3B y^2+o(y^2),
 u(y)=sigma y+A y^3+o(y^3), u'(y)=sigma+3A y^2+o(y^2),
 epsilon_xx(0,y)/2=Q y^3+o(y^3).                           (2)

If an outward enclosure proves Q is nonzero, epsilon restricted to x>0 is not in Y_(a_w,s) for every real a_w>=5/2 and every s>=0. Here Y is the logarithmic pullback in anisotropic_frozen_transport_inverse, with zeroth squared contribution integral x^(-2a_w)|epsilon|^2 dxdy. The divergence is local near a positive portion of the vertical axis. In particular it obstructs placing this trial residual in Y_(6,153/50). It does not exclude all possible correction domains or other residual spaces.

## Stream expansion and the origin boundary term

Let F_l(r) be the l-th density sine coefficient normalized by1/pi over the circle. Its source coefficient for even n is

 f_n=[F_(n-1)'-(n-1)F_(n-1)/r+F_(n+1)'+(n+1)F_(n+1)/r]/2.

For each r>0 the complete radial Green formula, followed by integration by parts separately over(0,r) and(r,infinity), gives

 psi_n(r)=-(1/2)r^(-n)integral_0^r t^n F_(n-1)(t)dt
                 +(1/2)r^n integral_r^infinity t^(-n)F_(n+1)(t)dt. (3)

To check signs, the lower source integral has boundary +(1/2)r^(n+1)(F_-+F_+) and interior -n integral_0^r t^n F_-; the upper has the opposite boundary -(1/2)r^(1-n)(F_-+F_+) and interior +n integral_r^infinity t^(-n)F_+. Multiplication by the two Green prefactors cancels the boundary terms and gives(3). The lower endpoint terms vanish since F_l=O(r^3); upper terms vanish by sublinear density growth. Exact joins allow integration by parts across both joins without interface terms.

At the center rho3=x^2y=r^3(sin theta+sin3theta)/4. Consequently F1=F3=r^3/4+O(r^5) and F5=O(r^5). The formula at n2 gives

 psi2=(sigma/2)r^2-r^4/12+O(r^6).

Indeed Sigma=integral r^(-2)F3, the lower part contributes -r^4/48 and the removed portion of the upper part contributes -r^4/16. At n4, formula(3) gives

 psi4=r^4[(1/2)integral_0^infinity t^(-4)F5(t)dt-1/64]+O(r^6).

The -1/64 term comes from -r^(-4)/2 times integral_0^r t^4(t^3/4)dt. It cannot be omitted. The compact-annular formula Gamma4=(1/2)integral r^-4 F5 applies when the density vanishes near0; here the cubic density changes the lower term. Equivalently the integration-by-parts boundary of r^-3 F3 at0 is1/4.

The exact angular product with cos^2(theta)sin(theta) gives

 F5=r^3(a1+a2-a3-a4)/8.

Hence the integral in the quartic coefficient is I/8 and the coefficient is H4 from(1). All stream modes n>=6 contribute only O(r^6(1+|log r|)) and differentiated versions. This follows termwise from the finite modal inner expansion: source degree2 is solely n2, higher source degrees start at4, and the first possible resonance is stream degree6. The exact finite-power/log argument in center_obstruction gives the same bounds after the needed derivatives. Thus

 psi=sigma xy-r^4 sin2theta/12+H4 r^4 sin4theta
                                     +O(r^6(1+|log r|)).

Since r^4 sin2theta=2xy(x^2+y^2) and r^4 sin4theta=4(x^3y-xy^3), restriction of psi_x to x=0 gives A=-1/6-4H4. Its derivative remainder is o(y^2). This proves the velocity lines of(2). In particular H4 is the actual harmonic quartic coefficient, not the compact-source moment without its origin correction.

## Axis coefficient of the residual

On the vertical axis rho=rho_x=rho_y=rho_xy=U1=U2,x=0. Divergence freedom gives U1,x=-u'. Twice differentiating the residual in x and dividing by2 yields exactly

 epsilon_xx(0,y)/2=(2ell-1-2u'(y))b0(y)
                                  +(ell y+u(y))b0'(y).     (4)

For the ell X.grad rho term, x rho_x contributes2b0 and y rho_y contributes y b0'; the remaining terms follow from the same product differentiation as in axis_compatibility_moment_domain. The finite inner expansion of rho=x^2y a gives b0=y+B y^3+o(y^3) and its derivative in(2); cos(2m theta)=(-1)^m at x=0,y>0. Inner corrections with exponent bi>4 and higher D powers do not affect B. Substituting the velocity and density traces into(4), the coefficient of y is3ell-1-sigma=0. The coefficient of B y^3 is5ell+sigma-1=8ell-2=2beta; the coefficient of A y^3 is-6A+A=-5A. This proves(2) and all forms of Q in(1).

The residual is C2 near any fixed nonzero axis point by the accepted finite regularity. It is even in x and vanishes at x=0, so epsilon_x=0 there. If Q!=0, (2) gives a small closed positive y interval on which epsilon_xx(0,y) has constant sign and is bounded away from0. Continuity extends this bound to a rectangle. Taylor's integral formula therefore gives |epsilon(x,y)|>=c x^2. Its zeroth weighted squared norm dominates integral_0^delta x^(4-2a_w)dx, which diverges for a_w>=5/2. Membership in H^s implies L2 for s>=0; hence failure of the weighted L2 component proves the stated Y nonmembership.

## Exact rational integral and independent algorithms

Let w=(1,1,-1,-1) on modes1,2,3,4, and define projected coefficients S_i=sum w_m S_mi, D_j=sum w_m D_mj, A_q=sum w_m A_mq, with Ei,Eo recomputed from the projected exact endpoint jets. Linearity permits projection before recomputation. With alpha_q=(k-3)-j_q(1-k)-2l_q, the three exact pieces are

 I_inner=sum_(j=1)^7 D_j/(2j)
                       +sum_(i=0)^6 Ei_i (-1)^i i!/bi^(i+1),
 I_middle=sum_(i=0)^(N-1) S_i (t_(i+8)-t_i)/8,
 I_outer=sum_q A_q/(-alpha_q)+sum_(i=0)^6 Eo_i i!/bo^(i+1).  (5)

Every denominator is nonzero and every tail integral converges by bi,bo>0 and alpha_q<0. The exact join formula is Ei_i=sum_(j=0)^i (-bi)^(i-j)(J_j-P_j)/[(i-j)!j!], with b=-bo in place of bi for Eo. It enforces derivatives0 through6 exactly. No stored approximate Ei/Eo is substituted.

The spline integral formula in(5) follows from an explicit antiderivative. Add one endpoint knot at each end, raise degree7 to8, put q0=0 and q_(i+1)-q_i=S_i(t_(i+8)-t_i)/8. The derivative coefficient formula gives exactly S_i on the original knots. The clamped degree8 spline takes endpoint values q0 and qN. The fundamental theorem of calculus, with continuity across the simple knots, gives(5). This also proves the sum over the entire interval, not a sampled quadrature identity.

One implementation reads the binary NPZ and converts exact binary64 values to Fractions. It uses the global antiderivative integral, exact local Cox polynomials for the two endpoint jets, the join equations and Arb512 for the sole exponential exp(-2a) and Q. The independent implementation decodes the hexadecimal JSON using integer arithmetic, reconstructs endpoint jets by repeated derivative-spline coefficients, and integrates the projected degree7 spline on all1558 spans using an exact eight-node rule. Its rational nodes j/7 and Lagrange-integral weights satisfy sum w_j(j/7)^d=1/(d+1) for every0<=d<=7; hence the rule integrates every span polynomial exactly. Values come from the de Boor value recurrence, independently of the Cox reconstruction. It uses mpmath.iv220 and exp(-a)^2 for B. Both paths reconstruct the angular projection and axis algebra by distinct polynomial methods, independently enclose Q in the same strictly signed rational window, and freshly check inherited evidence pins.

No quadrature approximation error or tail truncation occurs in(5). Roundoff in the scalar exponential and final arithmetic is enclosed separately in both engines. Python exact rationals, python-flint/Arb and mpmath.iv are trusted computational dependencies. Agreement checks implementation consistency; analytic validity rests on(1)-(5) and the independent arguments above.

## Dependencies and scope

Dependencies: modal_repair for exact joins and normalization, center_obstruction for the finite inner expansion and differentiated stream remainder, modal_graph_scaling for canonical finite regularity, anisotropic_frozen_transport_inverse for Y, and axis_compatibility_moment_domain for the axis-domain comparison. Their accepted sources are pinned through the latter verdict. A hash proves byte identity, not the mathematical claim. The numerical application requires a strictly nonzero enclosure for Q; until that exists no nonmembership verdict is accepted.

This conclusion concerns the exactly defined normalized modal trial. It does not use the literal unjoined stored trial, does not exclude an exact profile in P2, does not control distance to X3, and does not prove a full inverse or nonlinear closure. A small but nonzero Q would still yield the stated divergence. No decisive endpoint follows.
