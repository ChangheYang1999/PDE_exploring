# Exact Hilbert-Schmidt norm for the gradient-structured remainder

## Statement

Use the Fourier transform rhohat(xi)=integral rho(X) exp(-i X.xi) dX, with unitary form rhohat/(2pi). Let R_j have symbol i xi_j/|xi|. For a real smooth density rho, set a=rho_x, b=rho_y and

K = (1/2)[R1,[R1,b]] - (1/2)[R1,[R2,a]].

First assume rho is smooth and compactly supported. Then K is Hilbert-Schmidt and its exact squared norm is

||K||_HS² = [(log2-1/2)/(16pi)] ||D rho_x||_2²
           +[(3log2-2)/(16pi)] ||D rho_y||_2².                 (1)

Both coefficients are positive, and the first is larger. Consequently

||K||_HS <= sqrt((log2-1/2)/(16pi)) ||D²rho||_2.              (2)

Here D rho_x=(rho_xx,rho_xy), D rho_y=(rho_xy,rho_yy), and the ordered Hessian norm has rho_xy counted twice. The same statement holds for the finite exact IPM profiles in this campaign: they are smooth, with |D^j rho(X)|=O(|X|^(gamma-j)) for j=0,1,2 outside a fixed ball and 0<gamma<1. More generally it holds whenever compact smooth density approximations converge in homogeneous H² and their gradients converge uniformly.

This is a norm identity for the compact symmetric remainder. It is not a positive inverse gap or an existence theorem. It sharpens the bound for two unrelated coefficients by using their common scalar potential.

## Fourier kernel and rotation

The double-commutator kernel in the unitary Fourier representation is

k(xi,eta) = [-(du_1)² bhat(q) + du_1 du_2 ahat(q)]/[2(2pi)²],
q=xi-eta, du=u(xi)-u(eta), u(z)=z/|z|.

Because ahat=iq_1 rhohat and bhat=iq_2 rhohat, the numerator becomes

i du_1 (q_1 du_2-q_2 du_1) rhohat(q).

Fix nonzero q=|q|(cos alpha,sin alpha). Rotate and scale eta so that q becomes e1. Write d_parallel and d_perp for the components of the corresponding unit-vector difference. The original first component is cos(alpha)d_parallel-sin(alpha)d_perp, and the determinant factor is |q|d_perp. Reflection of the integration variable across the q axis changes d_perp to its negative and leaves d_parallel unchanged. The cross term therefore integrates to zero. It follows that

integral_eta du_1² (q_1du_2-q_2du_1)² deta
= |q|^4 [A cos²(alpha)+B sin²(alpha)],

A=integral_R² d_parallel² d_perp² deta,
B=integral_R² d_perp^4 deta.                               (3)

All integrals are nonnegative and finite, as computed next.

## Exact constants

For q=e1 use elliptic coordinates

eta=((cosh(mu) cos(nu)-1)/2, sinh(mu) sin(nu)/2),
mu>=0, 0<=nu<2pi.

Put c=cosh(mu), s=sinh(mu), C=cos(nu), S=sin(nu), D=s²+S². The distances to the two foci are (c-C)/2 and (c+C)/2. Direct subtraction gives

d_parallel=2c S²/D, d_perp=-2s S C/D,
deta=(D/4) dmu dnu.

All four angular quadrants contribute equally. With z=tanh(mu),

A=16 integral_0^(pi/2) integral_0^1 z² S^6 C²/(S²+C²z²)^3 dz dnu,
B=16 integral_0^(pi/2) integral_0^1 z^4 S^4 C^4/(S²+C²z²)^3 dz dnu.

In each integral put v=z cot(nu), then exchange the nonnegative integrals. The remaining angular integral is

integral_0^atan(1/v) sin³(nu)/cos(nu) dnu
= (1/2)[log(1+v^(-2))-1/(1+v²)].

Consequently

A=8 integral_0^infinity v²/(1+v²)^3 [log(1+v^(-2))-1/(1+v²)] dv,
B=8 integral_0^infinity v^4/(1+v²)^3 [log(1+v^(-2))-1/(1+v²)] dv.

For p=1 or 2, putting t=v² and differentiating the beta integral gives

integral_0^infinity v^(2p)/(1+v²)^3 log(1+v^(-2)) dv
= (1/2) Beta(p+1/2,5/2-p) [psi(3)-psi(p+1/2)].

The corresponding integral without the logarithm and with denominator (1+v²)^4 is (1/2)Beta(p+1/2,7/2-p). Using the gamma recurrence and psi(1/2)=-EulerConstant-2log2,

A=pi(log2-1/2), B=pi(3log2-2).                            (4)

The same values can be obtained by elementary integration of the half-integer beta functions. The beta derivative is justified by integrable logarithmic majorants at zero and infinity for both p values. The positivity of B follows from log2>2/3, and A-B=pi(3/2-2log2)>0 because log2<3/4.

## Plancherel and the exact identity

The Hilbert-Schmidt norm is the integral of |k(xi,eta)|². Substituting (3), changing variables to (q,eta), and applying Plancherel gives

||K||_HS²
= 1/[4(2pi)^4] integral |rhohat(q)|² |q|² [A q_1²+B q_2²] dq
= 1/(16pi²) [A||D rho_x||_2²+B||D rho_y||_2²].

Equation (4) now proves (1), and A>=B proves (2).

## Extension to the exact sublinear profiles

Let chi be a fixed smooth radial cutoff, equal to one on B1 and zero outside B2, and let rho_R(X)=chi(X/R)rho(X). Each rho_R is smooth and compactly supported. The hypotheses on rho give

||D²(rho-rho_R)||_2 -> 0,
||D(rho-rho_R)||_infinity -> 0.

For the first statement, the Hessian tail tends to zero by square integrability. Terms involving Dchi_R Drho or D²chi_R rho have L² norms O(R^(gamma-1)), since their amplitudes are O(R^(gamma-2)) on an annulus of area O(R²). The uniform gradient error is O(R^(gamma-1)), including the cutoff derivative term. Both vanish for gamma<1.

Apply (1) to differences rho_R-rho_S. It makes K[rho_R] Cauchy in Hilbert-Schmidt norm. Uniform convergence of the gradient coefficients makes the corresponding bounded operators converge to K[rho], because each double commutator has operator norm at most four times its coefficient supremum. Thus the Hilbert-Schmidt limit is K[rho]. The Hessian components converge in L², so equality (1) passes to the limit.

## Dependencies and verification status

The argument uses the double-commutator kernel identity, Fourier Plancherel, a direct elliptic-coordinate integral, beta integrals, and cutoff approximation. The kernel normalization is the same as T4's audit record double_commutator, proof. Independent review by T4 and the Opus theory lanes is requested before this is used as a team theorem. Numerical integration of A and B is a separate check, not the proof. No profile value or inverse claim is implicit in (1).
