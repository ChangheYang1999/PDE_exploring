# Scope and exact-root clarification after the first review

The point P is (x*,0), where x* is the unique exact root of the canonical
trial drift V0_1(x,0) in the initial rational bracket stored in
`../modal_source/evidence/source_result.json`. The certified strict endpoint
signs and positive derivative on that whole bracket prove existence and
uniqueness by continuity and the mean value theorem. The 28 bisections retain
that root. The final values mu, g and gp were evaluated on the union of the
final rational endpoints, not at a sample point: see lines 103-114 of the
pinned `../modal_source/code/certify_source.py`. Thus they enclose the jets
at the exact P and V0(P)=0 is exact, including V0_2(P)=0 by parity.

The first actual Opus 5.5 review correctly requests this explicit binding.
Its item G2 is a scope limitation, not a gap in the local continuity proof.
Its statement that varying source location is not covered needs precision:
the computation is at the fixed trial P, and a perturbed exact solution may
have its source elsewhere. This does not affect equation (1). No certified
X3 placement or variable unnormalized exponent is asserted.

PROMPT.md states U=(-psi_y,psi_x), so partial_y U2=psi_xy=sigma, without
a minus sign or factor three. Its K2 is (x^2-y^2)/(2 pi r^4), with local
term -rho e2/2. The local term and its derivatives vanish near zero for
our remote bump. These facts justify exactly the convention used in (7).

Section 2 proves unboundedness of the normalized coupling as a map into
a fixed interior-patch norm. For large R, F_R and all its derivatives
vanish on that patch; hence the local transport and multiplication terms
applied to F_R also vanish there. This observation does not assert that
the full global linearized operator is bounded or invertible on H_b.
The patch proof and its b>2 hypothesis remain unchanged.

Section 3 is purely local, on |y|<exp(-1), and has no nonlocal IPM term.
The Dini conclusion is analytic for all sufficiently small radii. No
finite numerical test is used to prove it.
