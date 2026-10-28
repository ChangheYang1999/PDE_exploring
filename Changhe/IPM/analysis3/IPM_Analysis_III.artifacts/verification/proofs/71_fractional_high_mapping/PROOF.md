# Fractional high regularity compatible with the modal knot ceiling

## Exact setting

Let r=|X|, t=log r, p=x^2 y and a=17/4. All densities have even-x,
odd-y parity. Set

 w=|x|^(-17/2) max(1,r)^(29/4), R=L2_P(w dX),
 G=L2(e^(-t/2)dt on t<0; e^(27t/4)dt on t>0), E beta=p beta(t).

The background is the normalized exact-join modal density of proof 04.
Its velocity is V=ell X+U[rho]. Assume the positive-axis condition(A)
from proof 38: d(t)=V_2(0,e^t)/e^t is bounded above and below by positive
constants, d-D and d' are O(e^(2t)) at minus infinity, and d-ell and d'
are O(e^(-(1-k)t)) at plus infinity, where D=4ell-1 and k=1/ell.
Put H(t)=exp(-int_(-infinity)^t (D-d-2d')/d ds), and

 omega(t)=e^(-t/2) for t<0, e^(2(k+3/8)t) for t>0.

The scalar domain B consists of beta=H z with locally absolutely
continuous z, z(+infinity)=0, z(-infinity)=J, and finite norm

 ||beta||_B^2=|J|^2+||z'||_L2(omega)^2
       +||z-J||_L2(omega,t<0)^2+||z||_L2(omega,t>0)^2.

Set X0=E B direct-sum R, Y=E G direct-sum R and
Z=E B direct-sum D_R, where D_R={h in R:(V.grad-1)h in R}
with its maximal graph norm. These are the fixed low spaces.
The canonical velocity U and strain c are as in topics02 and44;
W[h]=U[h]+c[h]X/3.

Choose a smooth scalar q(t) equal0 on t<=0 and1 on t>=1; put
chi=1-q and

 a_(delta,gamma)(t)=exp(delta t+(gamma-3-delta)t q(t)).

Fix 1/4<delta<2, gamma<-3/8 and sigma>6. Define

 H_base^sigma={p[j chi+a_(delta,gamma)u]:
                 j real, u in H^sigma(R times S1),
                 u even under both Cartesian reflections},
 ||h||_base^2=|j|^2+||u||_Hsigma^2.

For s>2 and epsilon>0, let b(t) be smooth and positive, equal
exp((3+delta)t) for t<=0 and exp(gamma t) for t>=1, and define

 Q={b(t)v(t,theta):v in H^s(R times S1), v has parity P,
                       supp v subset {|cos theta|>=epsilon}}.

Its norm is ||v||_Hs. The high space is the infimum Hilbert sum
H_high^sigma=H_base^sigma+Q. One can restrict Q further to t<=T
for any fixed T. The same conclusions also hold with Q replaced by
a compactly supported H^s component whose support is disjoint from x=0.

## Theorem and scope

H_high^sigma embeds continuously in Z. The cubic coefficient J is
continuous and classical. There are finite constants C_B,C_V such that

 ||W[d].grad h||_Y<=C_B||d||_X0||h||_Hhigh,
 ||DW[h]||_infinity+|c[h]|<=C_V||h||_Hhigh.

Thus the mapping theorems V060 and V065 require sigma>6, rather than
the integer order7. In particular sigma=25/4, delta=3/2, gamma=-1/2,
s=21/10 is allowed. The choice25/4 is strictly below the residual's
local spline-knot ceiling13/2 in V069. This is only local compatibility
with that obstruction. It does not prove global high-target membership,
a high inverse, propagation, or a nonlinear existence theorem.

## Sobolev estimate that replaces the integer order

On the two-dimensional cylinder, the Fourier variables are (xi,n),
xi real and n integer. For every multi-index alpha of length m<=5,
Cauchy-Schwarz gives

 ||partial^alpha u||_infinity
 <= C [sum_n int_R (1+xi^2+n^2)^(m-sigma) dxi]^(1/2)
       ||u||_Hsigma.

The bracket is finite exactly when sigma>m+1. To see sufficiency,
compare the sum and integral outside the unit ball with the radial
integral int_1^infinity R^(2(m-sigma)+1)dR; on bounded frequency sets
there is no singularity. This proves a bounded C5 representative when
sigma>6. The same argument applied to Fourier tails proves continuity
of the fifth derivatives. Smooth spectral cutoffs converge in this
C5 norm. No sixth pointwise derivative is used below.

## Low-space and normalization membership

Write the cofactor of a base element as B_h=j chi+a u, and let
A_h(t)=B_h(t,pi/2). The preceding estimate gives all scaled derivatives
through order5 with envelopes j+O(r^delta) at0 and O(r^(gamma-3)) at
infinity. Reflection evenness gives B_h-A_h and its t derivative an
extra factor cos^2(theta). Angular differentiation loses at most one
factor cos(theta).

Consequently h-E A_h has finite R norm. Its squared radial-logarithmic
integrands are bounded by constants times e^((2delta-1/2)t) near0
and e^((2gamma+3/4)t) at infinity. Both integrate. The same powers put
A_h in B because H=1+O(r^2) at0 and H is comparable to r^(k-3) at
infinity, with the derivative estimates in(A). The coefficient
V.grad theta is O(cos theta sin theta), so applying V.grad restores
the angular factor lost on differentiation. All other scaled
coefficients are bounded. This proves membership in Z and its norm
bound. It also proves J=j and h/p=j+O(r^delta) uniformly off the axes,
with the continuous extensions used in proof 63.

A Q element has the annular C1,alpha envelope b(t), for any
0<alpha<min(1,s-2). Its angular support avoids x=0. Direct integration
with the same two powers proves membership in D_R. Oddness across y=0
makes v divisible by sin(theta) with bounded continuous quotient, so
h/p=O(r^delta) at0 and J=0. The sum map from the Hilbert product to Z
is continuous. Its kernel is closed, and quotienting gives exactly
the infimum Hilbert sum with an injective continuous embedding. J is
independent of decomposition and remains classical and continuous.

## Product estimate: derivative inventory and integrable kernels

The trace estimates of proof 46 hold for every d in X0:

 |T_d(r)/r-c[d]|+|T_d'(r)-c[d]|<=C r^2||d||_X0 for r<=1,
 |T_d(r)/r|+|T_d'(r)|<=C r^(-11/8)||d||_X0 for r>=1,
 T_d(y)=U_2[d](0,y).

The exact axis row of W[d].grad h is

 Gamma=(A_h+A_h')T_d/r-2A_h T_d'+c[d](A_h+A_h'/3)
      =(A_h'-A_h)(T_d/r-c[d])-2A_h(T_d'-T_d/r)
                                      +(4/3)c[d]A_h'.

It has the G integrability powers2delta-1/2 and2gamma+3/4. Only the
first t derivative of the cofactor and its second angular derivative
are needed for this row and the extra cos^2 factor.

For the remainder, apply the local axis-subtracted strip estimate of
proof 23 and the radial-versus-vertical lift estimate of proof 48 on
annuli of comparable input and output radius R0. These estimates have
operator bound C times the scaled C5 norm of the high density; that
norm was established above. Their bounds are
C min(R0^2,R0^(gamma-1))||h||_base. Annular overlap is bounded.
For smaller separated input radii, parity subtraction and the
axis-jet subtraction give square integrals bounded by

 int_0^1 r^3 dr+int_1^infinity r^(2gamma-3)dr.

For larger input radii, the canonical velocity kernel has expansion
c_Z(-x,y)+O(r^3|Z|^-5), with |c_Z|<=C|Z|^-3. Subtraction of the axis
row cancels the constant cubic cofactor. The remaining kernel is
bounded by

 C cos^4(theta)|sin(theta)|
         [r^(3+delta)|Z|^-3+r^5|Z|^-5]||h||_base.

The input inverse-weight integral of |Z|^-10 near0 has radial
exponent2a-9=-1/2 and is finite; its far part is also finite.
The output integrals are int_0^1(r^(2delta-3/2)+r^(5/2))dr and
int_1^infinity r^(2gamma-3)dr. These converge under the stated
conditions. They are precisely the separated kernel estimates proved
in proof 57, whose high-input hypotheses are the C5 bounds, parity and
power envelopes just checked. The uncut strain at infinity has the
same2gamma+3/4 integrability and vanishes near0 after a cutoff split.
No integer Sobolev derivative enters any of these steps.

For Q the product has zero vertical-axis row. Its first derivative
is bounded on each annulus by C b(log R0)/R0. The comparable-scale
L2 velocity bound gives the desired R estimate. The two separated
kernel estimates of proof 63 have radial powers3+2delta and
2delta-3/2 at0, and2gamma-3 at infinity; they also converge. These
proofs need only the C1,alpha envelope, not base regularity sigma.
Smooth approximation in H^sigma gives C5 convergence for the base;
H^s approximation gives local C1,alpha convergence for Q. The
bounded kernel estimates and trace pairings identify the limits with
the canonical product. This proves the asserted bilinear estimate.

## Velocity derivative estimate

For a base element the annular bounds imply that grad h is bounded,
globally Lipschitz and in L2; its second derivatives are bounded at0
and infinity. For Q, grad h is globally C^alpha and in L2 for any
0<alpha<min(1,s-2). Its annular seminorm is bounded by
C b(log R0)R0^(-1-alpha), which is bounded at both ends. Separated
annuli give the global seminorm by the pointwise envelope. The L2
radial powers are5+2delta at0 and2gamma-1 at infinity.

For each canonical velocity component and g bounded, C^alpha and L2,
the kernel split at unit radius gives

 ||U_i[g]||_infinity <=(1/2)||g||_infinity
                  +[g]_Calpha/alpha+||g||_2/(2 sqrt(pi)).

The local difference integral is int_0^1 r^(alpha-1)dr, the outer
kernel is in L2, and the point-mass term is at most half the input.
Applying this to the derivatives of h, which commute with the
canonical operator by smooth approximation, bounds DU, c and DW.
Taking the infimum over the two summands proves the velocity bound.

## Dependencies

The exact low spaces and axis integrating factor are from topics38,
44 and57. The low trace, strip, jet-input and separated-kernel lemmas
are proved in topics23 and46-48. The modal coefficient hypotheses are
proved in topics50 and52; positivity(A) is still explicitly assumed.
This proof checks every place in those mapping arguments where the
high Sobolev order enters and replaces it by sigma>6.
