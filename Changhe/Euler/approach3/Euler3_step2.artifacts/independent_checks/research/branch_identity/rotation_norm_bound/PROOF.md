# Rotation-independent lower bound for a shell field distance

Status: proved for the exact shell L2 norm. The numerical applications use floating-point quadrature and are empirical.

## Statement, spaces and notation

Let 0<a<b<infinity, let S={y in R3: a<|y|<b}, and let U,V be elements of L2(S;R3), with positive norms. Use the normalized norm

||U||_S = (|S|^(-1) integral_S |U(y)|^2 dy)^(1/2).

For Q in SO(3) define T_Q U(y)=Q U(Q^(-1)y). Then ||T_Q U||_S=||U||_S and

max( ||T_Q U-V||_S / ||V||_S, ||T_Q U-V||_S / ||U||_S )
  >= | ||U||_S - ||V||_S | / min(||U||_S,||V||_S).

The right side is independent of Q. If it exceeds a fixed threshold tau>=0 on even one shell, the maximum directional field distance over any family containing that shell exceeds tau for every Q. In particular the assertion holds for rotations about the z axis, the rotation symmetry relevant to the campaign.

## Proof

The map y=Qx sends S onto itself and has Jacobian determinant 1. Orthogonality gives |Q U(x)|=|U(x)|. Applying this change of variables to the squared integral proves norm invariance.

The triangle inequality applied to T_Q U=(T_Q U-V)+V gives ||U||_S-||V||_S <= ||T_Q U-V||_S. Applying it to V=(V-T_Q U)+T_Q U gives the opposite signed difference. Hence the absolute norm difference is bounded by the difference norm. Divide by each positive denominator and take the larger quotient, which uses the smaller denominator. Finally the maximum over shells is at least its value on this shell. This proves every assertion.

## Dependencies and scope

Dependencies: orthogonal invariance of Euclidean length, change of variables for Lebesgue integrals, and the L2 triangle inequality. No Euler equation or parameter-sensitivity assumption is used.

The result does not say that a small norm difference implies a small field difference. It does not distinguish solution branches of a differential equation. A finite angular quadrature need not be invariant under every rotation; numerical RMS values alone are not rigorous bounds on the exact integrals. Refinement and independent reconstruction support the campaign's numerical application, with this limitation retained.
