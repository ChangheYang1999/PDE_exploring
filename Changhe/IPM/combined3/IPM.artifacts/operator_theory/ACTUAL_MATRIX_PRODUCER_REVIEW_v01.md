# Independent review of the actual pointwise-matrix producer

Reviewed `../certify_actual_matrix.py` on 2026-11-04. Result: the mathematical
method and the enclosure arithmetic pass this independent review. This is
not an assertion that its live 898-panel computation has completed.

The matrix being certified is exactly
\[
\mathcal M_*=(c+1+a_W-qc)I-qS-K,
\quad K=\begin{pmatrix}-\rho_y&\rho_x/2\\\rho_x/2&0\end{pmatrix},
\quad S=\begin{pmatrix}u_{1x}&(u_{1y}+u_{2x})/2\\
(u_{1y}+u_{2x})/2&-u_{1x}\end{pmatrix}.
\]
The signs and coefficients in aa,dd,bb are correct after subtracting beta.
The expression for aW is
\((c r²+r[u1 cos(theta)+u2 sin(theta)])/(1/4+r²)\), exactly the specified
weight expression. Divergence freeness supplies S22=-S11. Reflection
symmetries make both diagonals even in each coordinate and the off-diagonal
odd in each; hence quarter-plane eigenvalue certification covers the plane.

Every radial field enclosure uses the actual frozen `fields013.py` Taylor
coefficients and its source Cauchy majorants. The radius of each base panel
is less than the allowed r/8. The Taylor remainder is explicitly added to
every harmonic. The adaptive degree decision only affects performance; the
reported remainder remains part of the enclosure even if its comparison
with the degree-selection threshold were indeterminate. The frozen field
routine asserts actual retained series degree, preventing silent global-cap
truncation. Angular arcs include both endpoints and cover [0,pi/2].

The Arb-to-binary64 conversion rounds both endpoints outward with nextafter.
Each addition and multiplication is then enclosed by another outward step;
negation is exact. The square upper uses the maximum of both endpoint
squares and rounds upward. Thus the lower determinant is a valid lower for
aa*dd-bb². Requiring both diagonal lowers and that determinant lower to be
nonnegative certifies a real symmetric positive semidefinite matrix.
Nonfinite endpoint checks prevent a NaN from being interpreted as a pass.

Assembly checks producer/evaluator hashes and complete configuration equality,
requires every base-panel index exactly once, and verifies that each adaptive
leaf-path set is a complete prefix-free binary partition. Failed or missing
leaves cannot produce the certified status. The exact-rational check of the
base-panel count guarantees coverage up to the final clipped outer radius.

The origin center is diagonal by actual reflection parity. Its entries are
base-q(c-1)+rho_y(0) and base+q(c-1), because the exact structural verifier
proved u1x(0)=c-1. The perturbation bound is valid: the aW error is at most
4r0²(c+sup|u|/r), the traceless strain error is bounded by the sum of the
absolute diagonal/off-diagonal entry errors, and the source K error is at
most |delta rho_y|+|rho_x|. The finite origin expansion has only nonnegative
powers in these errors. A useful replay guard would explicitly assert that
all p=0 rho_y harmonics are cos0 and that the p=0 u1x coefficient equals c-1;
both identities are already proved from the exact same input hashes in
`STRUCTURE013_PROOF.md`.

At infinity the scalar matrix part is bounded below by
\[
1+(2-q)c-c/(1+4rF²)-\sup_{r\ge rF}|u|/r.
\]
The further subtractions q*(|S11|+|S12|) and sqrt(rho_x²+rho_y²) bound the
strain and K operator norms. All required far exponents are strictly negative,
so endpoint substitution gives uniform exterior uppers. Its finite expansion
remainders use sufficiently many terms for every physical derivative order.

The review does not discharge a separate global strain-supremum assumption,
and does not turn a matrix certificate into a full generator-energy estimate.
Actual all-panel completion and the resulting origin/exterior numbers remain
obligations of the producer's final assembly.
