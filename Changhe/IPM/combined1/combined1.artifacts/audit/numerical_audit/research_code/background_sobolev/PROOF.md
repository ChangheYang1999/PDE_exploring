# Exact background Sobolev seminorms

## Statement and representation

For the exact finite potential family, rho=-chi_xxy-chi_yyy has the same radial representation used by the residual norm evaluator:

rho=r sum_(j,n) u^((j+1)delta/2) P[j,n](t) sin(n theta),

t=r²/(1+r²), u=1-t. Indeed a third potential derivative is R^(p_j) r^(-3) Q[j,n](t); division of Q by t² gives P and the identity R^(p_j)r^(-3)t²=r u^((j+1)delta/2). Divisibility is checked exactly. Thus the derivative recurrence and full-plane power integration in ../whole_plane_norms/PROOF.md apply verbatim to rho rather than F.

The targets are ||D²rho||_2 and ||D³rho||_2, with ordered Cartesian tensor multiplicities. Because rho has leading order r^gamma with 0<gamma<1, its second derivatives have order r^(gamma-2), and third derivatives decay one additional power. Both are square-integrable at infinity; smoothness handles the origin. The exact endpoint test in the code verifies this for every branch rather than relying only on the leading order.

## Relevance and scope

T4's double-commutator proposal asks for ||D²rho||_2. This note supplies that numerical quantity independently of the proposed operator theorem. If that theorem is confirmed, the product sqrt((4log2-1)/(8pi))||D²rho||_2 can be used as its Hilbert-Schmidt upper bound. The product is recorded conditionally and does not certify an inverse or any nonlinear result. The gradient of a sublinear profile need not be in L²; no finite value for ||grad rho||_2 is assumed in a frequency-cutoff estimate.
