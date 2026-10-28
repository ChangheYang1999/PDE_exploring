# Compact coupling from outside a separated vertical strip

## Statement and hypotheses

Fix R>0, Y>0, 0<a<9/2 and eta<2. On the full plane let

 w_a(X)=|x|^(-2a) for r<1,
 w_a(X)=|cos(theta)|^(-2a) r^(-eta) for r>=1.

Let H_out be the closed subspace of L2(w_a dX) consisting of functions even in x and supported in |x|>2R. Oddness in y may also be imposed. Let Omega={|x|<R, |y|<Y}. Suppose the prescribed background derivatives on Omega have expansions

 rho_x=2x rho_2(y)+x^3 r1(x,y),
 rho_y=x^2 rho_2'(y)+x^4 r2(x,y),

where rho_2, rho_2', r1 and r2 are bounded. Define the canonical velocity on Omega by its ordinary, nonsingular kernel integral against h. Define T h=U2[h](0,y) and T1 h=partial_x U1[h](0,y). Then

 E_out h=U[h].grad rho-x^2(2rho_2 T1 h+rho_2' T h)

is Hilbert-Schmidt, hence compact, from H_out into L2(Omega,w_a dX).

For every finite nonnegative integer j the maps h -> partial_y^j T h and h -> partial_y^j T1 h are bounded from H_out into L2((-Y,Y),dy). In particular multiplication by bounded C1 coefficients with compact support in (-Y,Y) makes the trace coupling compact into ordinary local L2, by its local H1 bound. No pointwise trace of an arbitrary weighted L2 input is presumed; these traces are defined by the separated kernel.

The actual candidate a=17/4, eta=5/4 satisfies the hypotheses. This theorem fills the separated outside-to-inside contribution on a fixed bounded strip. It does not give a uniform estimate as R tends to0 or Y tends to infinity, does not handle the adjacent input zone R<|x|<2R, and does not prove the full global edge Garding inequality.

## Kernels and Taylor cancellation

Away from its contact point the canonical velocity has kernels

 K1(z)=-z_x z_y/(pi |z|^4)=Im[(z_x+i z_y)^(-2)]/(2pi),
 K2(z)=(z_x^2-z_y^2)/(2pi |z|^4)=Re[(z_x+i z_y)^(-2)]/(2pi).

The contact term -h/2 in U2 vanishes on Omega because the input is supported outside |x|>2R. For s>2R, evenness in x gives

 B_i(x,y;s,v)=K_i(x-s,y-v)+K_i(x+s,y-v),
 U_i[h](x,y)=integral_(s>2R) B_i(x,y;s,v)h(s,v)dsdv.

B1 is odd in x and B2 is even. Put

 delta(s,v)=sqrt((s-R)^2+((|v|-Y)_+)^2).

For all |x|<=R, |y|<=Y and all intermediate points in the x Taylor expansion, both kernel distances are at least delta. It is at least R. Complex differentiation gives

 |partial_x^j B_i| <= (j+1)!/(pi delta^(j+2)).

The same estimate holds for any derivative of total order j in x and y, since differentiation in y introduces only powers of i. Taylor's theorem, with the vanished parity coefficients retained exactly, gives the pointwise kernel bounds

 |B1-x partial_x B1(0,y;s,v)| <=(4/pi)|x|^3 delta^(-5),
 |B2-B2(0,y;s,v)| <=(3/pi)x^2 delta^(-4),
 |B1| <=(2/pi)|x| delta^(-3),
 |B2| <=(1/pi)delta^(-2).

For example the first bound is x^3/3! times the order3 derivative bound 4!/pi. The second is x^2/2! times the order2 bound3!/pi. No formal weighted Riesz theorem is used.

Consequently E_out has an ordinary integral kernel K_E with

 |K_E(x,y;s,v)| <= |x|^4 A(s,v),

 A=(8||rho_2||_infinity/pi)delta^(-5)
   +(3||rho_2'||_infinity/pi)delta^(-4)
   +(2||r1||_infinity/pi)delta^(-3)
   +( ||r2||_infinity/pi)delta^(-2).                         (1)

All suprema here are on the indicated bounded output region.

## Weighted Hilbert-Schmidt bound

On Omega the multiplier w_a(X)|x|^(2a) equals1 for r<1 and r^(2a-eta) for r>=1. It therefore has a finite upper bound C_Omega. Hence

 integral_Omega |x|^8 w_a(X)dX
 <=4Y C_Omega R^(9-2a)/(9-2a)<infinity.                    (2)

For the input region s>2R, delta>=R and delta is comparable, with positive constants depending on R,Y, to1+sqrt(s^2+v^2). Outside the unit disk,

 w_a(s,v)^(-1)=|cos(theta)|^(2a) r^eta <=r^eta.

The bounded input region is separated from0. Thus

 I_beta=integral_(s>2R) delta^(-2beta)w_a(s,v)^(-1)dsdv

is finite whenever eta<2beta-2. Each beta in {2,3,4,5} satisfies this since eta<2. The coefficients in (1), the triangle inequality in weighted L2, and (2) give the explicit finite bound

 ||E_out||_HS
 <=[4Y C_Omega R^(9-2a)/(9-2a)]^(1/2)
   *[8||rho_2|| sqrt(I5)+3||rho_2'|| sqrt(I4)
       +2||r1|| sqrt(I3)+||r2|| sqrt(I2)]/pi.              (3)

Here the input is measured on s>2R. Its half-plane norm is1/sqrt(2) times the full-plane norm for even inputs; using (3) unchanged is a valid, slightly larger full-plane operator bound. The formula refers to the Hilbert-Schmidt kernel on the half-plane weighted input. Restricting it to the even full-plane subspace preserves compactness.

For completeness, a kernel square integrable against w_a(X)dX times w_a(S)^(-1)dS defines a Hilbert-Schmidt operator: conjugate the input and output by their square-root weights and apply Cauchy-Schwarz. Approximate the resulting L2 kernel by finite sums of products of simple functions in X and S. Each approximant has finite rank and the operator norm error is bounded by its L2 kernel error. This proves compactness directly.

## Trace estimates and completion

At x=0 the kernel for partial_y^j T is bounded by (j+1)!/(pi delta^(j+2)), while that for partial_y^j T1 is bounded by (j+2)!/(pi delta^(j+3)). Each has a finite squared dual integral uniformly for |y|<Y, by the same I_beta argument. Cauchy-Schwarz gives the claimed L2_y bounds and justifies differentiation under the integral by dominated convergence, initially on compactly supported smooth inputs.

A trace coupling with compactly supported C1 coefficients is bounded into H1 on a bounded interval when the coefficients multiplying T1 and T are C1. Approximation by averages on intervals of length epsilon gives an L2 error bounded by epsilon times the derivative norm, so its image is relatively compact in local L2.

Truncated smooth functions supported in |x|>2R are dense in H_out. The kernel bounds give unique continuous extensions to all of H_out and ensure that they agree with the canonical velocity wherever both are originally defined. This completes the proof.

## Dependencies and limitations

Only the canonical kernels from V002, parity, Taylor's theorem, elementary weighted integrability and finite-rank approximation are used. The coefficient expansions are hypotheses, exactly as in the local strip theorem V026. No claim is made about arbitrary jet input, the origin-normalized scalar trace, the adjacent strip, a global weighted trace target, the complement inverse, or any numerical constant for the actual profile.
