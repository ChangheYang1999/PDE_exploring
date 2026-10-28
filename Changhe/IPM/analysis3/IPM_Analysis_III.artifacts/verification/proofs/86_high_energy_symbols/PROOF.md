# High energy symbols and the two frozen endpoint margins

## Statement and scope

Let V and rho be real smooth functions on a regular Cartesian coordinate patch, with V a vector field and w a strictly positive smooth density. Use the Euclidean Fourier multiplier Lambda^s=(1-Delta)^(s/2). The IPM velocity convention is -Delta psi=partial_x h and U[h]=(-partial_y psi,partial_x psi). Put

 Lh=V.grad h-h+U[h].grad rho,
 p(X,nu)=rho_x nu_1 nu_2-rho_y nu_1^2,
 kappa_w=1+(div V)/2+(V.grad log w)/2.

For unit Euclidean covectors nu, the principal negative-energy coefficient of the conjugated order-s equation is

 kappa_w-p(X,nu)-s nu^T DV(X) nu.                    (1)

This is a local principal-symbol identity. It neither bounds the lower-order terms nor proves a coercive estimate. The formula with Cartesian DV cannot be inserted unchanged into a cylinder norm. For a variable smooth order s(X), its additional leading logarithmic negative-energy term is +(V.grad s) log|xi|. Multiplication of the energy norm by exp(T Lambda_0(X)) adds T V.grad Lambda_0. A scalar cutoff psi adds the quadratic energy term psi(V.grad psi)|Lambda^s h|^2 w. These are identities for the indicated local calculus; uniform control of a variable-order norm, cutoffs and remainders is a separate assertion.

For the exact frozen origin rates A=2 ell-1, D=4 ell-1, Sigma=A+D=3A+1, use t=log r and q=-A cos^2 theta+D sin^2 theta, v=Sigma sin theta cos theta. At the vertical-axis endpoint theta=pi/2, the factored unknown h/(x^2 y r^delta) has angular order-sigma negative-energy coefficient

 m_y=Sigma(sigma-1/2)-delta D.                        (2)

For the pure far-field dilation ell X.grad-1 and the cylinder unknown r^(-gamma)h, the coefficient is

 m_infinity=1-ell gamma.                             (3)

For delta=9/5, sigma=25/4, gamma=-1/2 and the exact k of the original data, (2) is greater than142.5 and (3) is greater than3.7876. The number approximately1.7191 is the lower threshold for sigma in (2), not the energy margin. The x-endpoint threshold from proof 77 is approximately2.080923418258482; at s=41/20 its positive margin is greater than0.9726.

## Proof of the local symbol identity

Fourier transformation gives U_1 the multiplier xi_1 xi_2/|xi|^2 and U_2 the multiplier -xi_1^2/|xi|^2. Multiplication by grad rho therefore gives the real principal symbol p. Integration by parts for a compactly supported test function g gives

 -Re integral (V.grad g-g) conjugate(g) w
 =integral kappa_w |g|^2 w.

Conjugating V.grad by Lambda^s adds the degree-zero symbol
s xi^T DV xi/|xi|^2. To see the sign directly, the principal commutator of a(x,xi) and i V(x).xi is

 partial_xi a . partial_x(V.xi)-partial_x a . V.

For a=|xi|^s the first term divided by a is s nu^T DV nu, and the second is zero. For a=|xi|^(s(X)), the second divided by a is -(V.grad s)log|xi|. Taking negative real energy proves (1) and the asserted logarithmic sign. An additional positive multiplication a_0 has [a_0,V.grad]/a_0=-V.grad log a_0, which proves the exponential-weight formula. The cutoff formula also follows directly by integrating against psi^2 w. All terms in these calculations are local principal terms; they do not assert global pseudodifferential estimates on singular weights or across the spline knots.

## Proof of the endpoint formulas

The exact cubic identity L00(x^2 y u)=x^2 y(-A x partial_x+D y partial_y)u gives, after multiplication by r^delta, the cylinder operator

 q partial_t+v partial_theta+delta q.

With measure dt dtheta its negative zeroth-order energy is v'/2-delta q. At theta=pi/2 one has q=D and v'=-Sigma. Angular derivatives of order sigma add sigma v' to the operator, so they add +sigma Sigma to negative energy. This gives (2). At the x endpoint the unfactored bulk calculation of proof 77 gives m_x=Sigma(3/2-s)+delta A. For the far-field conjugation the operator is ell partial_t+ell gamma-1; its transport is skew on dt, proving (3).

The exact rational calculations in code/check.py verify every stated numerical comparison. They use ell=9007199254740992/1615536043799051, without substituting rounded rates. These are frozen model numbers, not a certificate of the actual variable-coefficient high inverse.

## Dependencies

The velocity convention is independently derived above. Proof 77 supplies the already proved bulk threshold and its counterexample. The only data input is the exact exponent k already checked against the original NPZ. No unproved compactness, inverse, or regularity propagation is used.
