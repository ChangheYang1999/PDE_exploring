# Positive Gaussian source and a conditional transport-moment diagnostic

Date: 2026-10-20. Status: the formulas and conditional identity below are proved. Whether this family supplies a positive-vorticity nonprofile satisfying the single strain identity is OPEN. No profile or nonexistence conclusion is asserted.

## Statement and exact inverse

Fix beta>2, c=1+beta/2, sigma>0 and b>0. Put a=1/(2 sigma^2), S=x^2+(y-b)^2 and

    B(S)=(1-exp(-a S))/S, B(0)=a,
    F0=c/[-2b B'(b^2)], A=F0/sigma^4,
    Omega=A x exp(-a S), Psi=F0 x B(S).

B'(S)<0 for S>=0, so A>0 and Omega>0 on x>0. The canonical full-plane stream function is Psi up to its irrelevant constant. Its centered representative is Psi_rel=Psi-u0 x, where u0=F0 B(b^2), and

    V1=-2 F0 x (y-b) B'(S),
    V2=F0 [B(S)+2x^2 B'(S)-B(b^2)],
    W=beta(x,y)+V.

The field is smooth, V(0)=0, div V=0, -curl V=Omega and Psi_xy(0)=c. The vorticity center jet is Omega_x(0)=A exp(-a b^2). Thus the necessary temperature coefficient is

    a0=(beta/4) A exp(-a b^2)>0.

These are the exact local linear and quadratic compatibility conditions only. They do not imply either complete stationary equation.

Proof. The integral representation B(S)=int_0^a exp(-qS)dq gives smoothness and strict negativity of B'. Direct differentiation gives

    2B'(S)+S B''(S)=-a^2 exp(-aS),
    -Delta[xB(S)]=4a^2 x exp(-aS).

Since 4a^2=1/sigma^4, this proves the Poisson identity. Differentiating Psi gives the displayed velocity. Psi=O(r^-1) and its velocity is O(r^-2) at infinity before centering. These decays select the whole-plane inverse of this exponentially decaying, zero-total-circulation source: a smooth harmonic difference with gradient tending to zero is constant. The centering subtracts exactly the value of this inverse at the origin. Finally Psi_xy(0)=-2F0 b B'(b^2)=c. Parity is even for V2 and odd for V1,Omega,Psi; no y-reflection has been added.

## Conditional temperature construction

Assume additionally that W has a smooth normalized eigen-coordinate xi on the full plane satisfying

    W.grad xi=lambda xi, lambda=(beta-2)/2,
    xi(-x,y)=-xi(x,y), xi_x(0)=1,
    xi=0 exactly on x=0,

and that Theta=a0 xi^2 and its gradient satisfy the far-field bounds Theta=O(r^(1-2/beta)), grad Theta=O(r^(-2/beta)). These are extra assumptions in this statement; the numerical experiment does not prove them. They hold for the usual smooth global-source construction if its required flow and extension hypotheses have been established. Then Theta solves the temperature equation exactly, is positive off the axis, and has the required center jet.

For a backward characteristic X(-t) approaching zero, with x nonzero, write Theta=x^2 F. Let

    Q(X)=beta-2-2W1(X)/x=-(beta+2)+4F0(y-b)B'(S).

Along a backward orbit, d[log F(X(-t))]/dt=-Q(X(-t)). Consequently the exact finite-time formula is

    F(X)=F(X(-T)) exp(int_0^T Q(X(-t))dt).

At the origin Q=0. If alpha_y denotes the y derivative of W1/x at zero, then

    alpha_y=-2F0[B'(b^2)+2b^2 B''(b^2)],
    F(x,y)/a0=1+f01 y+O(r^2), f01=-2alpha_y/(beta+c).

This follows by substituting the center expansion into W.grad F=QF. The experimental cutoff formula uses this finite Taylor jet and therefore has a cutoff error. It is not exact temperature transport at a finite cutoff radius.

## The scalar diagnostic and its limits

Let K=xy/r^4 and g=K_x. Define N=int Omega V.grad K, I=int g Theta. Under the preceding conditional temperature hypotheses, every integral is absolutely convergent and

    D=N-I-pi c
      =N-(1/2)int Theta V.grad g-pi c
      =-int K [W.grad Omega+Omega-Theta_x].

Proof. The Gaussian source and bounded centered V satisfy the hypotheses of packet79 for any nu=1/beta. Theta and its gradient satisfy its stated local and far-field hypotheses. Its identity (2), with zero temperature residual, gives int Theta V.grad g=2I. Its identity (3) proves the last equality. Near zero each integrand has absolute radial bound C dr; at infinity the terms involving Omega decay exponentially and g Theta has radial bound C r^(-1-2/beta)dr. No principal value or discarded boundary term is involved.

A zero D would establish only one weighted residual identity. Even a rigorous zero would not establish the vorticity PDE. Indeed an exponentially decaying nonzero source cannot be a full target profile by the already proved circulation-tail obstruction. Conversely a sign for D throughout this one-parameter Gaussian family would not establish its sign for general positive vorticity.

Dependencies: explicit Gaussian Poisson inversion, elementary differentiation and packet79. Global eigen-coordinate and tail bounds are conditional hypotheses, not conclusions from the code.

## A proved global-flow range: beta=3, sigma=1, 2<=b<=7/2

For this parameter interval, the conditional eigen-coordinate and temperature hypotheses above are in fact satisfied. This conclusion concerns prescribed kinematic fields, not a solution of the vorticity equation.

First, for all S>=0,

    C(S):=B(S)+2S B'(S) >= -1/9.                       (4)

To prove (4), set z=S/2 and f(z)=(2z+1)exp(-z)-1+(2/9)z. It suffices to show f>=0. Here f(0)=0, f tends to infinity,

    f'(z)=(1-2z)exp(-z)+2/9,
    f''(z)=(2z-3)exp(-z).

Thus f' decreases up to3/2 and increases afterwards. It has at most two zeros; any positive local minimum of f occurs at the second zero z_*>3/2. In fact f'(25/8)<0. Indeed e^3<81/4 and e^(1/8)<8/7 imply e^(25/8)<162/7<189/8, which is exactly that inequality. The bound e^3<81/4 follows, for example, from e<87/32: sum through degree3 and bound the remaining exponential series by the geometric series (1/24)sum_(j>=0)(1/5)^j=5/96. Therefore z_*>25/8. At a zero of f', substitution of exp(-z)=2/[9(2z-1)] gives

    f(z)=(4z^2-16z+11)/[9(2z-1)].

The numerator is positive for z>=25/8, since it is increasing there and equals1/16 at25/8. Hence the only possible positive local minimum is positive; this proves f>=0. The displayed formula C=(1/2)[(2z+1)exp(-z)-1]/z now gives (4), with its value at0 by continuity.

Next define q=B(b^2)-3b/F0. With c=5/2 and z=b^2/2,

    q=[-7+(12z+7)exp(-z)]/(10z),
    2<=z<=49/8.

On this interval q<-1/9. Indeed h(z)=7-(10/9)z-(12z+7)exp(-z) has h''=(17-12z)exp(-z)<0, so its minimum on the interval is at an endpoint. At z=2, h=43/9-31/e^2>0, using e>8/3. At z=49/8, h=7/36-(161/2)exp(-49/8)>0, using

    exp(49/8)=e^6 exp(1/8)>(65/24)^6(9/8)>2898/7.

The first strict bound uses the exponential series through degree4 for e and the linear lower bound for exp(1/8); the last comparison is exact rational arithmetic. Thus C(S)-q>0 uniformly in S for each b in the closed interval (indeed uniformly in both variables).

Write Y=y-b. Direct substitution gives, for x!=0,

    W2-(Y/x)W1=3b+F0[C(S)-B(b^2)]=F0[C(S)-q]>0.        (5)

It follows that W has no off-axis zero. On the axis W2=3y+F0[B((y-b)^2)-B(b^2)]. It is negative for y<0 and positive for0<y<=2b. For y>2b use q<0, hence F0 B(b^2)<3b, to obtain W2>3y-3b>0. Consequently the origin is its only zero.

The field W=3X+V has bounded V, so it is complete, backward orbits stay in a fixed compact ball, and sufficiently large circles are strictly outward crossing in forward time. The origin has derivative diag(1/2,11/2), hence is a hyperbolic source. Every nonzero backward orbit tends to it. Here is the planar limit-set argument with the possible equilibrium issue made explicit. A sufficiently small Lyapunov ball for reversed time is positively invariant and attracts every point in it. If a backward limit set contains the origin, the orbit eventually enters this ball and converges to the origin. Otherwise the nonempty compact limit set has no equilibrium; the Poincare-Bendixson theorem supplies a periodic orbit. A periodic Jordan orbit is impossible because div W=6 and the divergence theorem would give positive flux through a curve tangent to W. The same argument, together with the repelling neighborhood of the origin and the outward large circles, shows that every nonzero forward orbit escapes to infinity.

It remains to construct temperature without assuming it. The smooth even function

    q1(X)=lambda-W1(X)/x, lambda=1/2,

extends across x=0 and vanishes at0. Define

    u(X)=int_0^infinity q1(phi_(-t)(X))dt,
    xi(X)=x exp(u(X)).                                  (6)

These are smooth globally. For completeness, choose a small origin ball in which the symmetric part of DW is bounded below by a fixed positive multiple alpha I. The reversed flow and its first derivative decay at least as exp(-alpha t) in that ball. For each k>=2 its kth derivative satisfies the same contracting linear variational equation with forcing consisting of products of at least two lower derivatives and bounded derivatives of W. Induction and variation of constants give a bound C_k exp(-alpha t), uniformly for starting points in a smaller ball. Composition with q1, which vanishes at0, then bounds every derivative of the integrand in(6) by C_k exp(-alpha t). The integral converges with all derivatives locally. At any other point a finite backward time enters the smaller ball, so finite-time flow dependence extends the same conclusion to a neighborhood of that point. This also proves convergence of(6) itself everywhere.

Changing variables in the integral yields W.grad u=q1. Therefore W.grad xi=lambda xi. Reflection gives u even and xi odd in x, u(0)=0, xi_x(0)=1, and xi has exactly the sign of x. Set Theta=a0 xi^2 with the positive a0 above. This is smooth, even in x, positive off the axis, zero on the axis, solves exact global temperature transport, and has the required quadratic center jet.

Finally Theta=O(r^(1/3)) and grad Theta=O(r^(-2/3)). One may use the large outward circle as a compact transverse section. Along each outgoing orbit, V is bounded and DV=O(r^-3); radial comparison gives r(t) comparable to exp(3t), uniformly over this section. The temperature is exp(t) times its bounded section value. The variational equation has D phi_t=exp(3t)M(t), with M and its inverse uniformly bounded, because the integral of |DV(phi_t)| is uniformly finite. The transported gradient is exp(t)(D phi_t)^(-T) times its bounded section value, giving the claimed gradient bound. Compact interior bounds complete the statement. These estimates also justify all integrals in the scalar diagnostic for this parameter interval.

This establishes the global kinematic hypotheses analytically. The sign or zero of D still requires an independent argument or quantified computation; no such exact sign claim is included in this proof.
