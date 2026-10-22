# Actual vorticity factorization at a simple endpoint

Prepared 2026-10-22T10:16:19.467974+00:00, before computation. This is a conditional local theorem for actual smooth solutions; the dated verification verdict is in SUMMARY.md. General B2 remains OPEN.

## Exact statement and dependencies
Coordinates are x and u=y_*-y. Let V=xa(x,u) partial_x+P(x,u) partial_u be a real smooth field near(0,0), with a,P even in x, a(0,0)=A>0, P(0,0)=0 and P_u(0,0)=-kappa<0. Suppose a real smooth even temperature has the actual factorization

Theta=(C_u/2)x^2Z^n,  Z=(u-H(x))L,  L>0,  L(0,0)=1,

where C_u is nonzero, n is a positive integer, H is smooth and even with H(0)=H'(0)=0, L is smooth and even, the graph is V-invariant, and VZ=(lambda-2a)Z/n. The endpoint identity2A-lambda=n kappa is assumed. These are provided by P337, or its explicit-axis extension P338, for an actual smooth thermal solution. They are not inferred from formal Taylor series.

Let Omega be real smooth and odd in x and satisfy the actual vorticity equation

VOmega+Omega=partial_x Theta,

where the partial derivative fixes u, equivalently fixes the physical y. Set m=(A+1)/kappa. Assume m is a positive integer, n>=m+1, and the actual axis coefficient eta(u)=Omega_x(0,u) has eta(u)=D_u u^m+O(|u|^(m+1)), with D_u nonzero, as u tends to0. A one-sided version of this asymptotic together with smoothness suffices to fix the same Taylor coefficient at0. There is a smaller connected reflection-symmetric neighbourhood on which

Omega=D_u x Z^m M,

where M is smooth, even in x, strictly positive and M(0,0)=1. It is uniquely determined there by Omega and the normalized Z. Its transport identity is

VM+[1+a+m(lambda-2a)/n]M
=(C_u/D_u)[Z^(n-m)+(n/2)x Z^(n-m-1) partial_x Z].

On this smaller neighbourhood, the actual zero set of Omega is exactly the union of x=0 and u=H(x). At a graph point with x nonzero the transverse order in u is exactly m. Off these curves,

sign Omega=sign(D_u) sign(x) sign(u-H(x))^m.

When n>=m+2 the right side of the M equation vanishes on the graph. The coefficient multiplying M on its left vanishes at the endpoint. No statement of global existence, inverse compatibility, or convergence of formal jets follows.

## Complete argument
Odd smooth division gives Omega=xG with G smooth and even, G(x,u)=integral_0^1 Omega_x(tx,u)dt. Substitute in the equation, divide by x off the axis and extend by continuity. Differentiating the given temperature factorization at fixed u gives

xaG_x+PG_u+(a+1)G=S,
S=Theta_x/x=C_u Z^n+(C_u n/2)x Z^(n-1)Z_x.

The displayed S is smooth, including x=0. Put q=u-H(x). Graph invariance and smooth division yield V=x alpha partial_x+q delta partial_q, where alpha(0,0)=A and delta(0,0)=-kappa. Write g(x,q)=G(x,q+H(x)). Because Z=q ell with ell smooth, the transformed S is divisible by q^(n-1); it is not necessary to assume that Z_x is divisible by q. In fact Z_x on the graph is generally -H'(x)L and is not identically zero. This distinction accounts for the loss of one power in the source.

Let g_j(x)=partial_q^j g(x,0)/j!. Suppose g_0,...,g_(j-1) vanish as functions on an x interval. For j<m, the right side has zero j-th transverse derivative because n-1>=m. Differentiating the left side gives

x alpha(x,0)g_j'+[alpha(x,0)+1+j delta(x,0)]g_j=0.

All other product terms contain a preceding jet or its x derivative. Its coefficient divided by alpha has value (A+1-j kappa)/A=kappa(m-j)/A>0 at0. Choose one smaller interval on which every such coefficient, for the finite collection0<=j<m, is bounded below by a positive constant. Integrating the scalar equation on either punctured half-interval shows every nonzero solution grows at least as a negative power of |x| toward0. Boundedness rules this out, including solutions flat at0. Continuity supplies the value at0. Induction proves g_0 through g_(m-1) vanish identically.

Taylor's integral remainder in q gives g=q^m K with K smooth and even. At x=0, H(0)=0 and G(0,u)=eta(u), so smoothness and the assumed leading coefficient give K(0,0)=D_u. Shrink one connected rectangle in(x,q) until K/D_u>0 and the already positive ell remains positive. Returning to(x,u), define M=K(x,u-H(x))/(D_u L(x,u)^m). Then M is smooth, positive, even and normalized to1. The required factorization follows. Its uniqueness follows first off xq=0 by division and then everywhere by continuity. This uses an actual smooth factor K, not division in a formal-series ring and not a nonvanishing assumption away from the origin imposed by hand.

On the dense set where xZ is nonzero, applying V to D_u xZ^mM, adding Omega and dividing by D_u xZ^m gives the asserted unit equation. All terms extend smoothly because n-m>=1, so continuity proves it everywhere. Since (lambda-2A)/n=-kappa and m kappa=A+1, the left coefficient has value0 at the endpoint. If n-m>=2, both source powers on the right are positive and that side vanishes on Z=0.

Positivity of M and L proves the exact zero set and sign. At a point on q=0 with x nonzero, the m-th transverse derivative is m!D_u x L^m M, nonzero, and all lower derivatives vanish. This proves the transverse order. The axis intersection is explicitly excluded from this order claim.

## Transfer to central simple endpoints of B2
For actual smooth full-plane B2 profiles satisfying the prompt parity, canonical inverse, U=o(|X|), beta>=2 and a_0 nonzero, take the central nonzero temperature-axis component containing the material center. Its endpoint y_* is a finite nearest zero of the relative axis field b(y)=W_2(0,y), assumed simple. Here W=beta X+U(X)-U(0) is the moving-center relative field throughout. In the signed coordinate u=y_*-y, V is precisely W expressed as xa partial_x+P partial_u, with P=-W_2 and a=W_1/x extended smoothly and evenly by odd smooth division. Report4.13(ii) supplies the incoming leading coefficients and orders at this endpoint. In this coordinate,

A=2beta+kappa, lambda=beta-2,
n=2+(3beta+2)/kappa, m=1+(2beta+1)/kappa,
C_u=epsilon^n C, D_u=epsilon^m D, epsilon=sign(y_*).

C and D in this paragraph are the incoming coefficients of T=Theta_xx and eta=Omega_x respectively, measured against s=|y-y_*|. They are not coefficients of Theta or Omega themselves. Both are nonzero. The gap n-m=1+(beta+1)/kappa>1 is an integer, hence at least2. Thus the local theorem applies. With beta = 2 and kappa = 1 it gives n = 10 and m = 6 and the same actual graph as the temperature theorem.

For clarity, the extra vorticity-axis input is substantive. On the central component, multiply the two axis functions a=Theta_xx/2 and q=Omega_x by sign(a_0) for this linear ODE argument, keeping b fixed, to work with a>0 and q>0. This is an auxiliary axis calculation, not a sign change of a full nonlinear profile. The axis equations are b a'=(2b'-(3beta+2))a and b q'+(2beta+1-b')q=2a. A positive homogeneous integrating factor H0 for q along the forward axis flow solves dH0/dt=-(2beta+1-b')H0. Then d(q/H0)/dt=2a/H0>0. Near the simple end H0 has incoming order m; a has order n. Since n-m>0, the integral of a/H0 along the axis flow converges near the endpoint: its distance integrand is O(s^(n-m-1)). At any fixed incoming point q/H0>0, so its finite endpoint limit is strictly positive. Hence the homogeneous coefficient D is nonzero; it is not discarded in favor of the higher-order particular solution. Smoothness forces m integral, and fixes the same leading signed Taylor coefficient from both sides. This is the independently checked part of the endpoint dependency needed above, not a derivation from temperature alone. Positivity of q on the central component is the inherited result of report 4.13(i). Its center inputs also follow directly from the prompt: c=1+beta/2 gives b'(0)=beta+c=(3beta+2)/2, and the vorticity coefficient equation gives q(0)=4a_0/beta. After the auxiliary sign multiplication, q is positive at every sufficiently small nonzero axis point by continuity. Starting the integrating-factor formula at such a point, the source 2a is positive and q stays positive along the outward axis flow, whose orbits cover the relevant half of the central component. This avoids treating the fixed center b(0)=0 as a finite-time starting point for a nonconstant orbit. No positivity away from the central component is presumed.

The global parity restriction r+d odd of4.13(ii) is not needed for the local factorization. If that additional global result is invoked, n and m have the same parity. We do not derive a new NO endpoint from it. In particular, the canonical inverse and all far-field requirements remain separate obligations.

## Independent manufactured controls
For constants A=2beta+kappa, lambda=beta-2 and k, put h=k/(2A+kappa), q=u-hx^2 and V=Ax partial_x+(-kappa u+kx^2)partial_u. Then Vq=-kappa q and Theta=(C_u/2)x^2q^n has VTheta=lambda Theta. Define

Omega=D_u xq^m+E1 xq^n+E3 x^3q^(n-1),
E1=C_u/[kappa(m-n)],
E3=-C_u n h/[3A+1-kappa(n-1)].

The denominators are nonzero in the B2 parameter range considered here; the second equals A+lambda+kappa+1>0. Acting on the three monomials directly gives(V+1)Omega=Theta_x. The first coefficient is resonant and homogeneous, the second reproduces C_u xq^n, and the third reproduces -C_u n h x^3q^(n-1). The unit is1+(E1/D_u)q^(n-m)+(E3/D_u)x^2q^(n-m-1), positive near0. The evaluator differentiates these constructed expressions, checks their source sign, orders and normalization, then perturbs a lower transverse term to force failure. These identities and coefficient checks are manufactured consistency checks. They are not independent confirmations of existence or of the proof. Additional singular homogeneous controls use g_j(x)=x^(-c), c=kappa(m-j)/A>0 on x>0: A x g_j' + kappa(m-j)g_j=0, but g_j diverges at0. Thus the boundedness hypothesis removes real homogeneous modes. The variable-coefficient control x^(-c)exp(-x^2/2) likewise solves xg'+(c+x^2)g=0 and diverges. These are tests of the necessity of boundedness, not smooth counterexamples to the theorem. Each singular negative control is a pair: an exact homogeneous residual identity and a separate divergence-to-infinity check; the residual identity itself is not a failed PDE check.

These examples satisfy two transport equations and constant divergence only. In the sign convention of PROMPT.md, U=(-Psi_y,Psi_x), -Delta Psi=Omega, so the local kinematic relation in signed coordinates is Omega=P_x-x a_u. For this simple field it is2kx and generally disagrees with the manufactured Omega. This curl/Poisson failure MUST be checked and displayed, so that a pair of perfect transport residuals is never presented as a local Boussinesq solution. No inverse, gauge, center or tail is assigned to these manufactures.

The proof and all hypotheses precede tests. No Lean/Lake formalization is claimed. No JavaScript/TypeScript, servers/listeners/tunnels, RLScience cluster or human contact is used. All writes stay in this verifier lane.
