# Direct Candidate013 L² certificate

This is a proof specification and reproducibility guide. The complete authoritative result is now `L2_signed_far_v05/result.json`, with status `CERTIFIED_DIRECT_L2`, every core/endpoint flag passing, verified bindings and a final finite-scalar audit. It uses the first1856 verified core panels and a complete infinite exterior proof. The original2994-panel backup `L2_cert_v04` was intentionally stopped after2208 saved panels once the sufficient whole-plane proof was complete; no final result is claimed for that redundant backup.

Write \(a=\partial_x\rho_*\), \(b=\partial_y\rho_*\), and let the real Riesz operators have multipliers \(i\xi_j/|\xi|\). The actual canonical velocity satisfies

\[
U[h]=(-R_1R_2h,R_1^2h).
\]

The symmetrization of \(Qh=U[h]\cdot\nabla\rho_*\) is

\[
\operatorname{Sym}Q=P_0+K,\qquad
P_0=R_1bR_1-\tfrac12(R_1aR_2+R_2aR_1),
\]

\[
K=\tfrac12[R_1,[R_1,b]]-\tfrac12[R_1,[R_2,a]].
\]

Integration using the skew-adjoint Riesz operators gives

\[
\langle P_0h,h\rangle
=\int[-b|R_1h|^2+a(R_1h)(R_2h)]
\le\theta_*\|h\|_2^2,
\quad \theta_*:=\sup_X\frac{\sqrt{a^2+b^2}-b}{2}.
\]

The independently audited gradient-structured Hilbert–Schmidt identity inherited from combined2 is

\[
\|K\|_{\mathrm{HS}}^2
=\frac{\log2-1/2}{16\pi}\big(\|\rho_{xx}\|_2^2+\|\rho_{xy}\|_2^2\big)
+\frac{3\log2-2}{16\pi}\big(\|\rho_{xy}\|_2^2+\|\rho_{yy}\|_2^2\big).
\]

Its inherited statement and exact provenance are recorded in `combined2/IPM.artifacts/EXISTING_PROOFS_REFERENCE.md`, R1, especially the quoted `[HS]` identity and cutoff extension. No Candidate007 numerical value is transferred. The Hessian norms and signed theta bound are computed directly for Candidate013.

The cutoff extension applies to the actual rational-potential background: \(\rho_*=O(r^{1/c})\), \(D\rho_*=O(r^{1/c-1})\), \(D^2\rho_*=O(r^{1/c-2})\), with \(c>1\). Thus the gradient decays uniformly, the Hessian is square-integrable, and smooth cutoffs approximate the gradient uniformly and the Hessian in L². The exact origin and far expansions in `asymptotics013.py` also verify these properties from the finite source.

For \(A_k=(cX+u_*+U[k])\cdot\nabla-1+U[\cdot]\cdot\nabla\rho_*\), divergence \(2c\) yields on compact smooth tests

\[
\operatorname{Re}\langle A_kh,h\rangle
\le-(c+1-\theta_*-\|K\|_{\mathrm{HS}})\|h\|_2^2.
\]

The perturbation transport contributes zero when it is divergence free and admits the usual integration by parts. Constructing the generator, identifying its domain, and extending the estimate to its realization are separate analytic tasks; the scalar cover does not claim them automatically.

## Complete scalar cover

For \(T=1/80\), the square-root-free test

\[
a^2\le4T(b+T),\qquad b+2T\ge0
\]

is equivalent to \(\theta(X)\le T\). S1 symmetry makes \(a^2,b\), and hence this test, invariant under reflections of both axes. The first quadrant therefore suffices, with its axes included by closed angular arcs.

The core annulus \(10^{-5}\le r\le10^8\) has 2994 radial panels of exact endpoint ratio 201/199, with the last endpoint shortened to \(10^8\). Each panel has 1024 containing angular arcs. The actual Cartesian derivatives are summed as radial Taylor series before interval evaluation. Every omitted radial Taylor term is charged by the complex Cauchy majorant in `fields013.py`; the outer potential disks lie in \(\Re(t+z^2)>0\). Degrees are at most 72 and their realized series precision is asserted. Arb encloses the trigonometric endpoints; each floating product and sum subsequently receives explicit outward `nextafter` rounding.

For the three Hessian norms, the squared radial Taylor polynomials are integrated exactly in \(r\,dr\). For a coefficient \(p+e\), the radial L² norm is at most \((\int|p|^2r\,dr)^{1/2}+\|e\|_\infty(\int r\,dr)^{1/2}\). Angular orthogonality gives the exact factors \(\pi\), or \(2\pi\) for the constant mode. Origin and exterior contributions use exact homogeneous expansions, with rigorous differentiated coefficient-tail estimates.

The original backup assembler requires exactly indices0 through2993. The completed v05 assembly instead requires exactly indices0 through1855 and proves the entire remaining exterior: it factors the common negative leading gradient power, covers its exact angular polynomial and all normalized remainders, and uses signed theta monotonicity. Finite far Hessian power sums are integrated with exact angular orthogonality and radial cross-power integrals, evaluated through native containing Arb polynomials; omitted analytic tails are added in L². Source/code/cache/chunk hashes, all core theta flags and both endpoint proofs are checked. Its final theta upper is1/80, kappa upper0.710328127935052 and signed rate greater than2.087491082264946. A directory of partial chunks alone is never a completed whole-plane certificate.

## Reproduction

From the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
  /tmp/ipm-combined3-venv/bin/python -B \
  Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/certify_L2_013.py \
  --out Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/L2_cert_v04 \
  --workers 8 --chunk 32
```

The script preserves and verifies complete saved chunks before continuing. The source JSON files in combined1 and combined2 are read without modification. The first two prototype configurations are explicitly invalidated after detecting the python-flint process-global series cap; no bound from those runs is adopted.
