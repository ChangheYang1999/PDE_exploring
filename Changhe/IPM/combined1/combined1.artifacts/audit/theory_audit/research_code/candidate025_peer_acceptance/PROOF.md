# Acceptance of the independent candidate025 shape comparison

The exact statement is T4-436: the 2918 pre-constraint potentials and
 their density images are independent, with 81 objective probes and 46
specified probes outside that analytic span. The complete proof, copied
as source/436_PROOF.md, uses distinct noninteger branches, highest poles
at the three auxiliary radial singularities, and the harmonic polynomial
argument for density injectivity. Its regularity, canonical density map,
exact c, growth and full-circle hypotheses remain unchanged.

This result accepts the independent N4-365 comparison. It binds that
comparison's complete result, proof and code, its N4-361 input result and
code, and the original T4-436 proof and result. The peer sources are read
but not executed. The checker independently recalculates the closed
formula for all 348 highest Laurent coefficients,

 R^8*v_R^4*binom(2*N,N)*(1-v_R)^(m+N)/(R^2-1)^(4+N),
 v_R=-1/(R^2-1),

and compares it with both independent expanded records and the peer
comparison. Six cross-pole values are also compared. The proof of the
formula and its sufficiency is in the copied T4-436 proof: a highest
nonzero pole in a finite relation cannot cancel, so descending induction
removes each generator after fractional branches are separated. The
same argument applies to each of the 36 noninteger branch conditions.

All 81 ordered rows, split exact weights, 46 outside probes, and all
60 reported iteration records are compared. Recomputing a displayed
sum of mesh step norms gives a FLOAT diagnostic, not a certified
full-plane norm. In particular, the original result JSON's phrase
'projection ... excluded' needs correction: only the initial Taylor
projection is excluded. The copied launch source projects the initial
vector before calling optimize2. Within optimize2, each trial is Taylor
projected before its difference from the current vector is measured.
Thus the logged per-step norms include that trial's Taylor projection.
The final exact conversion and quadrature error are not bounded by those
numbers. No assertion about a certified total correction follows.

The checker validates the peer's 161 own-input hashes and 41 retained
source hashes once, recording that read-only attestation. It does not
copy those entire transitive graphs into this topic. The attestation
is provenance evidence rather than a substitute for the independent
348-coefficient comparison or T4-436's existing local source graph.
No optimizer, foreign code, server, JavaScript, cluster or Lean build
is executed. Current source bytes do not certify earlier save times.
The result is structural and does not claim residual smallness, an
inverse or an existence theorem.
