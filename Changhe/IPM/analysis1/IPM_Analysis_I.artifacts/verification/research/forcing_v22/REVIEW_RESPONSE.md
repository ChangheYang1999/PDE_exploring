# Response to the first actual Opus5.5 review

Written 2026-10-21T09:43:01.050623+00:00. The response from request
f4b7c98b-0755-4a00-b5a7-12f6f5d49848 used actual model
claude-opus-5-5 and stopped at max_tokens. Its partial response is retained
and is not counted as an acceptance. Followup is required.

F1. The geometry proof is about a fixed canonical partition. The new
certificate must explicitly use that partition. check_source_geometry.py
will hash the external Green and trial files before and after checking,
compare all7810 canonical partition points with the Green tb/tb_rad
boxes, and identify every local endpoint with the prior geometry input.
It compares all three source statements defining XSTAR_LO,XSTAR_HI,
XSTAR,XRAD by AST and their evaluated exact binary values. No missing
historical runtime is inferred. The current external data are retained
read-only at their documented numerics paths rather than duplicated here.
Application stays OPEN until these checks succeed.

F2. cart_derivative_table is absent in both compared source files.
The original check did not claim a successful body comparison for it,
but its silent skip was unhelpful. The supplement explicitly records
ABSENT_BOTH_NO_INHERITED_CLAIM and compares the actual function
faa_di_bruno_tables. The exact symbolic composition audit separately
checks that actual table and the Leibniz expressions in the new source.

F3. The Arb output key transition counts all17870 nonconstant cutoff
rows, meaning16502 transition plus1368 straddling rows. The final audit
will use the name nonconstant_cutoff_rows. The original reviewed output
is preserved; its quantity is not the H2 row count.

F4. The response truncated at the start of its inside-row discussion.
Inside rows have tau=1 and derivatives exactly zero; T0>=1 and each
other cutoff field nonnegative suffice. The replacement exact rational
checker tests finiteness and nonnegativity for all six fields before
entering this branch. It never interprets infinities as rational numbers.

The first iv batch timed out. The separate-factor rational attempt also
timed out on3000rows, and its10-row completion returned OPEN because
that overestimate exceeded several saved bounds. Neither event refutes
the saved physical cutoff fields. RANGE_REFINEMENT.md proves the revised
full-polynomial Bernstein method, independent of the Arb critical roots.
Its first1000rows passed; the complete disjoint coverage is still pending.
The new code and retained failures will be included in the followup.
