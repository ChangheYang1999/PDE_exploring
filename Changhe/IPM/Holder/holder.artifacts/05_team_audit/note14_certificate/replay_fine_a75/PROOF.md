# Independent fine annular certification at exponent 3/4

## Statement and exact witness

For the real homogeneous Holder seminorm [f]_(3/4)=sup_{z!=w}|f(z)-f(w)|/|z-w|^(3/4), let D_(3/4) be the norm of R_1^2=T_xx-I/2. The operator has the circular principal-value kernel cos(2theta)/(2 pi r^2) and is extended modulo constants by convergent increments. We independently enclose the increment of the Note14 lattice witness from ../PROOF.md with

    a=3/4, b=3/4, c=-3/10, lambda=50/53.

The result is a method for proving a lower bound, not a numerical claim in advance of computation. The accepted profile certificate gives [P]_(3/4)<=53/50, so lambda[P]<=1. The lattice lemma gives [f]_(3/4)<=1 and f(e1)=-1/2, f(0)=1/2. With I0=p.v. integral [K(z-e1)-K(z)]f(z) dz, the two signs of the identity term have equal norms by rotation, and hence D_(3/4)>=|I0|+1/2. The setup's compact approximation theorem makes this a bound also for the original supremum over compact smooth real functions.

## Domain partition and analytic replacements

Use exact rational mesh endpoints selected by the independent driver, with a near-pole starting radius 1/100, near-pole endpoint 1/2, midpoint starting radius 1/100, and midpoint endpoint 10^16. This is an independent mesh; it is not asserted to reproduce the producer's mesh. The right near-pole annuli are recomputed by the accepted interval cell rules in ../PROOF.md, ../repairs/PROOF.md and ../refined_cells/PROOF.md. Reflection doubles their contribution. The midpoint cells use the same accepted geometry. Their saved exact endpoint intervals must cover each included radial interval exactly once.

The missing pole disks are covered by the analytic estimate in ../pole_profile/quadratic_lower/PROOF.md, with the optional upper refinement in ../pole_profile/quadratic_clamp/PROOF.md. Their conditions are checked outward at the actual disk radius. The disk radius can be increased to any saved near-pole task endpoint that satisfies those conditions; the discarded numerical annuli are then wholly replaced by this disk integral, never omitted or counted twice.

The midpoint sliver has the explicit symmetric error from ../PROOF.md. The exterior has the explicit main integral and error in ../homogeneous_tail/PROOF.md, optionally sharpened by ../homogeneous_tail/angular_error/PROOF.md. The relevant hypotheses lambda(1+2^(-a))>=1 and lambda[P]<=1 are checked. All endpoints and analytic terms are recombined by code/audit_note14_annular_profile.py using exact rational sums and outward arithmetic at 320 bits.

## Acceptance conditions

The driver and all three frozen cell-rule dependencies are hashed before computation and those hashes accompany every task. Complete coverage, cell counts, source identity, profile inputs, analytic hypotheses and outward rounding are independently checked by the auditor. A finite maximum over admissible disk radii is legitimate because every candidate is separately proved. A numerical endpoint is accepted only after these checks and a separate numerical statement recording the actual result. This proof precedes the computation.
