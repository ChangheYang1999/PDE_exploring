# Cartesian field formula used by the extended-precision reference

Status: exact algebraic identity for a finite smooth toroidal-poloidal expansion. This result makes no Euler existence claim.

## Statement and notation

Let H be a real homogeneous harmonic polynomial of integer degree ell >= 1 on R^3. Let f,g be smooth real functions on an open interval containing [0,infinity). For y in R^3 put q=|y|^2, h=grad H(y), K=D^2 H(y), and

V(y)=curl(f(q) H(y) y)+curl curl(g(q) H(y) y).

Use the Jacobian convention (DV)_{ij}=partial_j V_i. Define

A=(ell+1)g+2qg', B=-2ell g',
A'=(ell+3)g'+2qg'', B'=-2ell g''.

Then, including at y=0,

V=f(h cross y)+A h+B yH,

partial_j V_i = 2f' y_j(h cross y)_i
 +f[(K e_j cross y)_i+(h cross e_j)_i]
 +A K_{ij}+2A' y_j h_i
 +B[delta_{ij}H+y_i h_j]+2B' y_j y_i H.

If f,g depend smoothly on a parameter p, the same formulas with f,g replaced by partial_p f,partial_p g give partial_p V and its Jacobian. Finite sums over modes obey these identities term by term and are divergence free.

## Proof

For the toroidal term, curl(a y)=grad a cross y. With a=f(q)H, the radial part 2f'H y of grad a has zero cross product with y, leaving f(h cross y).

For the poloidal term use curl curl(a y)=grad div(a y)-Delta(a y). Euler's identity gives y dot h=ell H, so div(gH y)=[(ell+3)g+2qg']H. Since Delta H=0 and Delta(gH)=[4qg''+(4ell+6)g']H,

Delta(gH y)=[4qg''+(4ell+10)g']yH+2g h.

Differentiating the divergence and subtracting the displayed Laplacian leaves [(ell+1)g+2qg']h-2ell g' yH. This proves the formula for V. The stated Jacobian is its Cartesian product rule; q_j=2y_j. Smoothness makes the identity valid at the origin without a limiting convention.

Parameter differentiation commutes with the finite spatial derivatives. The divergence of either curl term vanishes by commutation of Cartesian mixed partials, and finite sums preserve this property.

## Basis convention and verification scope

The reference constructs each real H from the explicit Legendre polynomial formula, with the same normalization as the saved coefficient format: no Condon-Shortley sign, unit L2 norm on S^2, and a factor sqrt(2) for positive azimuthal order. Rational polynomial coefficients are formed exactly; pi, square roots, radial Chebyshev polynomials, logarithms and trigonometric functions are evaluated in at least 70 decimal digits. Saved float64 coefficients and parameters are interpreted as their exact binary values. The reduced tail constraints are solved in the same extended precision, from their two defining equations.

The formulas are mathematical identities. Numerical agreement in this reference is evidence about an implementation at sampled points, not a formal or interval proof.

## Dependencies

The Cartesian curl-curl identity, Euler's identity for a homogeneous polynomial, the harmonic equation for H, ordinary product rules, and the neighboring proof of the reduced tail solve.
