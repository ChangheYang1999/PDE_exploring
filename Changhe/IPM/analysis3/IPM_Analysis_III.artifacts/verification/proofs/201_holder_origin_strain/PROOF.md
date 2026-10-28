# The central velocity derivative for Holder inputs

## Statement

Let 0<alpha<1 and beta>1. Suppose h is bounded on R^2, belongs to C^alpha on B2, is even in x and odd in y, and satisfies |h(X)|<=L|X|^beta on B1. Let U=(-R1 R2 h,R1^2 h) be the canonical velocity, with the far kernel subtracted at the origin. Then U is Frechet differentiable at the origin and

 U(0)=0, DU(0)=diag(-c[h],c[h]),
 c[h]=(1/pi) integral sin(3theta) r^(-3)h(X)dX.        (1)

The integral is absolute. Put gamma=min(beta,2) and M=||h||_infinity+||h||_(C^alpha(B2))+L. There is a finite constant C_(alpha,beta), independent of h, such that, for 0<r=|X|<=1/8,

 |U(X)-c[h](-x,y)|<=C_(alpha,beta) M r^gamma(1+|log r|). (2)

In particular every input h in E_p of proof 199, with 1<=p<=2, meets these hypotheses with beta=p+alpha and M bounded by a constant times ||h||_(E_p). No derivative of h on a neighborhood is required. The derivative asserted in(1) is at the origin only.

For a C4 background rho with the parities of proof 199 and rho=x^2y+O(r^4), the normalized coupling therefore has zero cubic leading coefficient:

 (U[h]+c[h]X/3).grad rho
       =O_(alpha,p,rho)(||h||_(E_p) r^(gamma+2)(1+|log r|)). (3)

Here gamma=min(p+alpha,2)>1. Multiplication by a cutoff equal1 near0 does not alter(3). Neither this origin cancellation nor the frozen inverse of proof 200 makes the cubic coefficient a closed functional on E_p.

## Canonical integral and derivative candidate

Proof 01 derives the velocity kernels and contact terms. In the present convention they are

 K1(X)=-xy/(pi r^4),
 K2(X)=(x^2-y^2)/(2pi r^4),
 U1=PV K1*h, U2=PV K2*h-h/2,

with canonical subtraction for the far part. Each kernel has zero mean on circles, and |D^j K(X)|<=C_j r^(-2-j). Local Holder regularity makes its principal value well defined on B1. The subtracted far integral converges absolutely and is smooth there. Reflections give U1 odd in x and even in y, and U2 even in x and odd in y; hence U(0)=0.

The vector matrix integral

 D=integral DK(-Y)h(Y)dY                              (4)

is absolutely convergent. Near0 its absolute radial bound is C L integral_0^1 t^(beta-2)dt; at infinity it is C||h||_infinity integral_1^infinity t^(-2)dt. This candidate is not obtained by assuming that differentiation under the principal value is valid. We prove differentiability next. The contact term has derivative0 at the origin because |h(X)|/|X| tends to0.

## Remainder at the singular point

Fix |X|=r<=1/8 and split the kernel difference at |Y|=3r. In the outer part, Taylor's formula gives

 |K(X-Y)-K(-Y)-DK(-Y)X|<=C r^2 |Y|^(-4).

Its integral against h is at most

 C L r^2 integral_(3r)^1 t^(beta-3)dt+C||h||_infinity r^2.

For beta<2 this is O(M r^beta); for beta=2 it is O(M r^2(1+|log r|)); for beta>2 it is O_(beta)(M r^2). Each is bounded by the right side of(2).

The inner subtraction terms are directly bounded by

 integral_(|Y|<3r)|K(-Y)h(Y)|dY
   +r integral_(|Y|<3r)|DK(-Y)h(Y)|dY
 <=C_beta L r^beta.                                  (5)

It remains to control PV integral_(|Y|<3r)K(X-Y)h(Y)dY. Set epsilon=r^(beta/alpha). Since beta>alpha and r<1, epsilon<=r and the disk |Y-X|<epsilon lies inside |Y|<3r. Circular cancellation on that disk permits replacing h(Y) by h(Y)-h(X). Its integral is bounded by

 C [h]_(C^alpha(B2)) integral_0^epsilon t^(alpha-1)dt
 <=C_alpha M r^beta.

On the rest of |Y|<3r, the displacement satisfies epsilon<=|Y-X|<=4r, while |h(Y)|<=3^beta L r^beta. Absolute integration of the kernel gives the upper bound

 C_beta L r^beta log(4r/epsilon)
 <=C_(alpha,beta) M r^beta(1+|log r|).                 (6)

The contact term is O(L r^beta). Combining(5)-(6) and the outer estimate proves U(X)-U(0)-DX has the bound in(2). Since gamma>1, this is o(r). Thus D is indeed the Frechet derivative.

## Evaluation and the weighted Holder inputs

Direct differentiation yields

 partial_y K2(-Y)=y(3x^2-y^2)/(pi r^6),
 partial_x K1(-Y)=-y(3x^2-y^2)/(pi r^6).

The two off-diagonal entries of(4) vanish by the stated parity. These identities give exactly(1), with the sign fixed independently of any differentiation under a singular integral.

For h in E_p, oddness and the weighted y seminorm imply

 |h(x,y)|<=[h]_(y,p)|x|^p |y|^alpha
             <=||h||_(E_p) r^(p+alpha).

On B2 the x and y difference estimates in that norm give an ordinary C^alpha bound, with a finite factor depending only on alpha,p. Thus beta=p+alpha>1 and all hypotheses apply. Proof 200's explicit functional norm bound uses the same integral(1). The possible distributional contact correction for a nonzero linear y coefficient is absent here because h is Frechet differentiable at0 with derivative0.

Finally write P=x^2y and U=c(-x,y)+E, with E bounded by(2). The background assumptions and C4 Taylor's theorem give grad(rho-P)=O(r^3) and grad rho=O(r^2). The exact polynomial identity

 (c(-x,y)+cX/3).grad P=0

then gives the remainder O(|c|r^4+M r^(gamma+2)(1+|log r|)). Absolute convergence in(1) bounds |c| by C_beta M. Since gamma<=2, this proves(3).

## Dependencies and scope

Only proof 01's explicit distributional velocity kernels and proof 199's definition of E_p enter the proof. The singular-point differentiability argument is supplied above and does not reuse proof 01's stronger C^(2,alpha) input hypothesis. This closes the regularity step in proof 200's use of the word strain and its leading-cancellation statement. No global derivative estimate, actual-transport inverse, closed cubic normalization or nonlinear closure follows.
