# The rotation generator and the explicit omega column

## Statement and notation

Let J be the matrix with J(x,y,z)=(-y,x,0), and let Q_t=exp(tJ). Let U be a C^1 vector field on a rotation-invariant open set D in R^3. Define

    (T_t U)(y) = Q_{-t} U(Q_t y),
    L U(y) = DU(y) J y - J U(y),

where DU has component rows and spatial-derivative columns. Then d(T_t U)/dt at t=0 equals L U. Further, L U vanishes identically if and only if U(Q_t y)=Q_t U(y) for every t and y in D. This is axisymmetry of a vector field about the third coordinate axis.

For constants c and omega, the momentum expression

    (1-c)U + DU(c y - omega J y + U) + omega J U + grad P

has explicit omega dependence -omega L U. Here explicit means that the represented field and its associated pressure are held fixed. If U depends differentiably on omega, the full derivative also includes

    (1-c)U_omega + DU U_omega + DU_omega(c y-omega J y+U)
      + omega J U_omega + grad P_omega.

For a finite angular expansion U=sum_{m=0}^M U_m into the real azimuthal frequency subspaces of this vector rotation action, at each radius at which the field is defined,

    ||L U||^2_{L2(S^2)} = sum_{m=1}^M m^2 ||U_m||^2_{L2(S^2)}.

Thus ||U_nonaxisymmetric|| <= ||L U|| <= M ||U_nonaxisymmetric|| on a sphere. The same inequalities hold after any fixed, nonnegative, rotation-invariant radial weighting. If only even frequencies are active, the lower constant can be replaced by 2. The inequalities also hold when all quantities vanish.

## Proof

Differentiate the matrix product and composition defining T_t U. Since dQ_t/dt=J Q_t and Q_t commutes with J, at t=0 the two terms are -J U(y) and DU(y) J y. At general t the derivative is Q_{-t} (L U)(Q_t y). If L U is identically zero, T_t U is constant in t, and T_0 U=U gives the claimed equivariance. Conversely, differentiating the equivariance identity at t=0 gives DU(y) J y=J U(y).

Distribute the advective term in the momentum expression. The two explicit omega terms are -omega DU J y and omega J U, whose sum is -omega L U. The formula for a varying U follows by the product rule; it agrees with the omega identity in the parameter-derivative result, whose decaying-pressure hypotheses justify P_omega when that pressure convention is used.

On a fixed sphere, T_t is unitary for the vector L2 inner product: Q_{-t} preserves Euclidean vector lengths and Q_t preserves spherical area. Distinct azimuthal frequency subspaces are orthogonal, as follows by integrating their Fourier factors over a full rotation. On the two-dimensional real frequency-m representation, L acts as m times a skew-symmetric ninety-degree rotation. Its squared norm is therefore m^2 times the squared norm on that subspace. Summing the orthogonal squared norms proves the identity and both inequalities. Integrating those identities against a fixed nonnegative radial measure proves their weighted versions.

The toroidal-poloidal construction used here has these same frequency labels. Multiplication by y and differentiation by curl commute with the action T_t. The radial envelopes, radial twist, and the mode-by-mode reduced tail solve do not mix azimuthal frequencies. Setting every m nonzero coefficient to zero therefore gives an axisymmetric represented field. In this subspace the twist is zero, and the reduced tail equations contain omega only multiplied by m, so the represented U_omega is also zero at fixed reduced coefficients. With the unique decaying Newton-pressure convention, the differentiated source is zero and P_omega is zero. The full physical omega column then vanishes.

## Dependencies and scope

Dependencies: the chain rule, rotations preserving spherical measure, real Fourier orthogonality, the existing mode-by-mode representation, and the decaying-pressure differentiation theorem in ../pressure_consistency/PROOF.md. No numerical output is needed for this proof.

The result does not say that a small non-axisymmetric velocity alone controls the full omega derivative in an arbitrary coefficient norm. Such a bound also needs control of radial twist factors and conditioning of the coefficient representation and tail solve. The stated two-sided bound applies directly to the explicit rotation column in the continuous rotation-invariant L2 norm. Finite quadrature reports are numerical approximations to that norm. No existence or stationarity claim follows from a small column.
