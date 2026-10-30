# Independent audit of the gradient-structured commutator identity

## Statement and notation

Let R_j be the real Riesz operator with Fourier multiplier i xi_j/|xi|. Multiplication by a function is denoted by that function, and [A,B]=AB-BA. For real rho in C_c^infinity(R²), set a=rho_x, b=rho_y and

K=(1/2)[R1,[R1,b]]-(1/2)[R1,[R2,a]].

Then K is self-adjoint and Hilbert-Schmidt on real or complex L²(R²), and

||K||_HS² = (log2-1/2)/(16pi) ||D rho_x||_2²
           + (3log2-2)/(16pi) ||D rho_y||_2².                 (1)

In particular,

||K||_(L² to L²) <= ||K||_HS
 <= sqrt((log2-1/2)/(16pi)) ||D²rho||_2.                   (2)

The Hessian norm is the ordered Cartesian norm, so the mixed derivative is counted twice. The identity extends to any smooth rho admitting compact smooth approximations whose Hessians converge in L² and whose gradients converge uniformly. This includes each smooth sublinear profile with |D^j rho(X)|=O(|X|^(gamma-j)), j=0,1,2, outside a ball, where gamma<1.

Equation (1) is the N4 claim reviewed here. The proof below independently checks its constants, orientation and extension. It does not certify a background numerical norm, an inverse gap, or a nonlinear existence claim.

## 1. Exact kernel and angular dependence

Use hat f(xi)=integral exp(-iX.xi)f(X)dX and the unitary Fourier map hat f/(2pi). The multiplication kernel is hat a(xi-eta)/(2pi)². Put q=xi-eta and d=u(xi)-u(eta), u(xi)=xi/|xi|. The double commutator therefore has kernel

k(xi,eta)=[-d1² hat b(q)+d1 d2 hat a(q)]/[2(2pi)²]
         =i d1(q1 d2-q2 d1)hat rho(q)/[2(2pi)²].          (3)

This also follows directly by expanding both nested commutators, so there is no single-commutator replacement. Since each R_j is skew-adjoint and the R_j commute, both terms in K are self-adjoint.

For q=t(cos alpha,sin alpha), t>0, rotate eta and scale it by t. Write d_parallel,d_perp for d in coordinates parallel and perpendicular to q. Then d1=cos(alpha)d_parallel-sin(alpha)d_perp, while q1 d2-q2 d1=t d_perp. The Jacobian contributes another t². Reflection about the parallel axis leaves d_parallel unchanged and reverses d_perp. Consequently the cross integral vanishes and

integral d1²(q1 d2-q2 d1)² deta
=t^4 (A cos²alpha+B sin²alpha),                           (4)

where A=integral d_parallel²d_perp² and B=integral d_perp^4, both evaluated for q=(1,0). The q=(1,0) orientation thus pairs A with rho_x, as in (1).

## 2. Evaluation of A and B

For eta=((cosh(mu)cos(nu)-1)/2,sinh(mu)sin(nu)/2), mu>0 and 0<=nu<2pi, put c=cosh(mu), s=sinh(mu), C=cos(nu), S=sin(nu), D=s²+S². Away from a measure-zero focal segment this is a one-to-one coordinate system with Jacobian D/4. The two distances are (c-C)/2 and (c+C)/2. Subtracting the corresponding unit vectors gives

d_parallel=2c S²/D, d_perp=-2s SC/D.

Using four equal angular quadrants and then z=tanh(mu), direct substitution gives

A=16 integral_(0,pi/2) integral_(0,1) z² S^6 C²/(S²+C²z²)^3 dz dnu,
B=16 integral_(0,pi/2) integral_(0,1) z^4 S^4 C^4/(S²+C²z²)^3 dz dnu.

The integrands are nonnegative, so the next exchange of integrals is justified without an integrability assumption. Set v=z cot(nu). The upper angular endpoint becomes arctan(1/v), and

integral_0^arctan(1/v) sin³nu/cos(nu) dnu
=(1/2)[log(1+v^-2)-1/(1+v²)].

Therefore A and B are respectively

8 integral_0^infinity v^(2p)/(1+v²)^3
  [log(1+v^-2)-1/(1+v²)]dv,  p=1,2.                    (5)

To check the constants independently, substitute t=v². The logarithmic integral is one half of Beta(p+1/2,5/2-p) times [psi(3)-psi(p+1/2)]. This is obtained by differentiating the defining beta integral with respect to its first argument while holding its second argument fixed. Its logarithmic majorants are integrable for both p. The subtracted integral is one half of Beta(p+1/2,7/2-p).

For p=1 these three quantities are pi/16, 2log2-1/2, and pi/32. For p=2 they are 3pi/16, 2log2-7/6, and pi/32. Substitution in (5) yields

A=pi(log2-1/2), B=pi(3log2-2).                            (6)

The elementary bounds 2/3<log2<3/4 follow by applying the strict midpoint and trapezoidal bounds to the convex function 1/t on [1,2]. They imply 0<B<A.

## 3. Plancherel and extension

Integrating (3) and using (4),

||K||_HS²=1/[4(2pi)^4] integral |hat rho(q)|² |q|²
                  (A q1²+B q2²)dq.

Plancherel replaces each integral by (2pi)² times the respective squared derivative norm. The coefficient is thus 1/(16pi²), and (6) gives (1). The operator inequality and A>B give (2).

For the extension, let rho_R=chi(X/R)rho with a fixed compact smooth cutoff chi equal to one on the unit ball. The Hessian tail tends to zero in L². The cutoff derivative errors have amplitude O(R^(gamma-2)) on an annulus of area O(R²), so their L² norms are O(R^(gamma-1)). The gradient error is O(R^(gamma-1)) uniformly. Both converge to zero for gamma<1. Applying (1) to differences rho_R-rho_S makes K[rho_R] a Cauchy sequence in Hilbert-Schmidt norm. The operator norm of each nested commutator is at most four times the coefficient supremum. Uniform convergence of the gradients therefore identifies its operator limit as K[rho]. Hessian convergence passes the right side of (1) to the limit, proving the identity for rho.

The same proof works for any approximating sequence satisfying the two stated convergence conditions. Merely assuming a Hessian in L² without specifying coefficient behavior is not used here.

## Dependencies, evidence and scope

The frozen N4 source is source/N4_proof.md, SHA-256 e5f6483e981baff0ba8edc00abc4bb661dcd5edba06e68a243d699acba7c6994. This is an independent proof audit of that source. Dependencies are Fourier Plancherel, the elementary beta integral and cutoff approximation. No numerical quadrature is needed for the identity. The finite profile belongs to its domain because of the sublinear derivative bounds; its exact numerical Hessian and column norms are separate claims.
