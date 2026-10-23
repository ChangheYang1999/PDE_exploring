# SPECv55 consistency and residue-coordinate repairs

Result274, written 2026-10-21T18:38:30.682625+00:00 before its checker. Freeze v55=2bdd93d3cb10f3235a80d1068dd32013941fb16f44f59c1018988051862f09ef and v53=5ee35cfee83304b85279c5198971102c0a29d50db064da2aa2db48a48029fb7c. Audit every diff block. Only the version, G45 residues/status/scope and changelog may change; all other mathematics including G43/G44 must be byte-identical.

For phi(u)=A0/u+sum Aj/(u-uj), with v=1/(1+u) and vj=1/(1+uj), direct substitution gives phi(v)=A0 v/(1-v)+sum Aj v vj/(vj-v). The residue at v=vj is therefore -Aj vj^2. Positive even Aj are u-residues and weights in the moment equations, not positive residues in v. The odd A0 resides at u=0, which maps to v=1. Independently verify this algebra as a rational identity. The necessary noninteger configuration at d107 says only that integrality matters to that residue argument; it produces no polynomial H or profile.

The v54 status update cites267, whose204-check arithmetic gate and16-check review gate verify all four degree15 cases, so the finite auxiliary necessary degree bound is17 and P>=19/2. The nine degree17 cases are explicitly PROVED-lead awaiting verification and must remain OPEN in this audit. Likewise the status of running degree19/21 work is an attributed source statement, not verified mathematics. v55 still marks e2 arithmetic n<=1000 OPEN;271 later resolves that finite arithmetic claim, with n>1000 OPEN. This chronological lag must be described, not silently used to claim all-n exclusion.

The whole-plane PDE, admissible class, canonical gauge, center and normalization are unchanged. Full-plane existence/nonexistence remains UNRESOLVED; no early finish is allowed.
