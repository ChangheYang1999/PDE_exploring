# Scope and review resolutions

The first actual Claude Opus5.5 response ended at max_tokens and is not
acceptance. Its visible calculations agree with both independent methods.
The following points are explicit parts of the final statement.

The canonical identification has its own regularity and decay hypotheses.
To apply the X bound to a canonically identified density, also require
h in X. Growth O(r^gamma), gamma<1 alone does not imply X membership.
The review's stronger phrase "membership needs roughly gamma < k" is
incorrect for this X. A sufficient power bound for h and r grad h is
actually gamma<k+1/2: the squared radial majorant is
r^(2gamma-2k-2)dr. Topic128 proves that calculation. It is a sufficient
majorant condition, not a necessary condition on every function.

The factor3 for speed is a stated convention in PROMPT.md, equations(norm)
and(rank-one), lines89 and96. It also follows independently from the
lowest homogeneous density p=x^2y: with canonical strain Sigma,
U=(-Sigma x,Sigma y)+o(r), so

    [(c_l-Sigma)x partial_x+(c_l+Sigma)y partial_y]p
       =[2(c_l-Sigma)+(c_l+Sigma)]p=(3c_l-Sigma)p.

For a sufficiently regular stationary density with leading term p,
the coefficient equation is 3c_l-Sigma=1. Equivalently define the affine
normalization map N(rho)=(1+Sigma(rho))/3. Its exact increment, whenever
both canonical expressions are defined, is N(rho+h)-N(rho)=Sigma(h)/3.
A background violating this normalization carries its own defect; this
argument does not discard that defect. The bound on the speed functional
is therefore Cang/3 on X, while the lead's raw-strain convention has Cang.

The additional numerical scalar 3/Cang in compute.json is only the
reciprocal bound: ||h||_X >= (3/Cang)|Sigma(h)/3|. It is not an inverse
norm for the PDE and supplies no existence or uniqueness conclusion.

All weak angular integration by parts, canonical identification, endpoint
limits and density arguments are analytic proofs in PROOF.md. The exact
codes verify their displayed algebra and constants; they do not mechanize
the functional analysis. The second calculation uses its own Fourier,
beta, Machin and integer-root formulas before inspecting the first output.
Interval overlap is a consistency check only. Each method independently
implies the same strict public decimals.

Cang is only an upper bound; this work proves no optimality or strict
non-optimality statement. The fixed-strain construction establishes density
only in D intersect {Sigma=s}, without enforcing the PDE, full admissible
class, fixed tail, or other domain conditions. D need not be closed or
dense in X for this result. Actual section spectra, global velocity mapping
on X, the nonlinear estimates and every decisive endpoint remain OPEN.
