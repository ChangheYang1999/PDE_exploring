# Exact returned reference polynomials for the captured M24 endpoints

The ideal normalized-coordinate cutoff is C4. For the frozen source
SHA256d02f1ee1daaf63c846a1642c9e0a0d0e8b2bec75097c83c955d16fa41dc3d5c0,
the locally reproduced finite coefficient lists give a different result:

- ref_J and ref_Jin have exactly unit width. All ten endpoint residuals
  through order4 vanish exactly for each. They define C4 references in X.
- ref_wide has a strictly positive upper radial value trace between
  1.2121e-13 and1.2122e-13. All lower endpoint residuals vanish, but the
  upper value does not. The resulting encoded function is outside X.

These are exact rational results, not floating evaluation cancellation.
Primary rational Horner differentiation and independent hexadecimal/IEEE
binary decoding plus direct differentiated monomial sums agree on all30
endpoint derivative values. The latter separately parses both captured
NPY scalar headers and payloads. The exact ideal cutoff has also passed
all ten endpoint conditions, so its mathematical formula remains valid.

The primary check executes only the isolated, AST-checked step_pieces
function, not the numerics application or a matrix computation. It checks
the complete REFS expression and uses captured M24 tmin,t0 with their
prior hashes. No claim is made about future or historical numerics outputs.
The first AST comparison failed before arithmetic because a manually
constructed FunctionDef lacked optional parser fields. The saved failed
attempt is retained; comparing the parsed argument and complete body nodes
corrected the test without weakening the source-expression match.

Thus the current source's assertion that all three returned references
are exactly C4 cannot be used as a rigorous fact for these inputs. An
exact normalized-coordinate polynomial supplies the intended C4 function,
or one can apply an exact continuity repair. Those are newly specified
functions. Their numerical Gram or angle transfer requires its own bounds.
The two unit-width references already pass this narrow exact test, but a
continuous reference does not make an encoded singular vector continuous.
No actual singular vector, spectrum, global inverse or PDE claim is tested.
