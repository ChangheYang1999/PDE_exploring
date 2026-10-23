# An absolutely convergent strain formula and a restricted sign exclusion

Status: CONFIRMED after independent derivation/checking and completed Opus 5.5 review 10. Date: 2026-10-20. The actual returned model was claude-opus-5-5; the review is in ../../evidence/opus_review_10/answer.md. Its suggestions were independently checked.

## Statement and dependencies

Assume the exact primary class from PROMPT.md; explicitly the gradient satisfies |grad rho(X)|<=C(1+|X|)^(gamma-1), 0<gamma<1, and rho is smooth, even in x and odd in y. With c=psi_xy(0),

    c=(1/pi) integral_(R^2) x y |X|^(-4) rho_x(X) dX=1-c_l<0.       (1)

The integral is absolutely convergent. Consequently rho_x is negative somewhere in the open first quadrant. This is a restriction on possible solutions, not a nonexistence theorem for the whole class. The proof uses the canonical inverse and center relation proved in ../inverse/PROOF.md and ../origin/PROOF.md.

## Proof

Parity and smoothness give rho_x(x,y)=x y h(x,y) with h smooth locally. Thus rho_x=O(r^2) at zero, and the absolute value of the integrand before dX is O(1). At infinity it is O(r^(gamma-3)); multiplication by the polar area element leaves an integrable radial power r^(gamma-2), since gamma<1.

Write the sin(2 theta) coefficient of rho_x as f_2(r), with the convention that the subscript is the angular frequency. Polar coordinates and absolute convergence give

    (1/pi) integral x y r^(-4) rho_x dX
      =(1/(2pi)) integral_0^infinity integral_0^(2pi)
                      sin(2 theta) rho_x(r,theta) dtheta dr/r
      =(1/2) integral_0^infinity f_2(r) dr/r=c.

The final equality is the canonical regular quadratic stream-function coefficient. This agrees with differentiating the Newtonian kernel -log(r)/(2pi): its mixed derivative is xy/(pi r^4). There is no mixed-derivative contact term. The primary center relation gives the last equality in (1).

The product xy rho_x is even in x and even in y. If rho_x>=0 in the first quadrant, the integrand in (1) is nonnegative everywhere, which contradicts c<0. Smoothness then supplies an open neighborhood with rho_x<0 somewhere in that quadrant.

For each fixed positive y, the growth bound and rho(x,0)=0 also imply

    |rho(x,y)| <= integral_0^y |rho_y(x,s)| ds
               <= C_y (1+|x|)^(gamma-1) -> 0.

For positive a0 this already forces negative rho_x somewhere on every horizontal ray starting from a positive axis value. For negative a0, a profile negative on the upper half-plane and with |rho| nonincreasing in x>0 is excluded by (1). No global density sign is assumed in the theorem, and negative a0 alone is not excluded.

## Manufactured sign check

For rho=y exp(-r^2), rho_x=-2xy exp(-r^2). The integral in (1) is

    -(2/pi) [integral_0^infinity r exp(-r^2) dr]
             [integral_0^(2pi) cos^2(theta) sin^2(theta) dtheta]
      =-(2/pi)(1/2)(pi/4)=-1/4.

This agrees with the independent modal and Fourier checks. This manufactured density does not solve the transport equation.
