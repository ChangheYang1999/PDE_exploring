# Exact accepted row and review resolutions

This addendum is mandatory with PROOF.md. The first actual Opus5.5 review
accepts the algebra, signs, rational exponential tail and radial coverage.
Its questions concern inherited-row certification and scope wording.

The T=1 row is an actual accepted output. Topic53 verdict.json has SHA
2a8ae9e75b9cc64a69f950254d01af346eb12aa600ce797680953abc391551dd
and directly pins checks.json with SHA
3742c1d9f5d7fc76f058fa2f4f8bff340acc253e0d6bc3e2e86f7a3855683a83.
The pinned output_audit.py explicitly requires the exact six values
0,1/16,1/8,1/4,1,9. For every row it checks the Arb and iv endpoints,
takes their larger upper endpoints, verifies P<=Q and both drift values,
and checks both radius intervals. The accepted actual core computation
constructs both velocity bounds for every one of these rows. The new
producer rechecks every verdict input, copies the entire T=1 row and
checks its two maxima exactly. The separate new auditor repeats those
checks against the accepted data. Thus this is not a hypothetical T=1
bound inferred from the statement for arbitrary T.

The underlying topic53 theorem supplies continuous axis extensions via
finite trigonometric polynomial identities. Its bounds on the open
quadrant therefore extend to both closed axes. This is the precise
premise used for v1,v2 and T; there is no division by a zero coordinate.

The remaining finite exterior interval means exp(t_b)<=r<=exp(t_b+5).
All radii20<=r<=exp(t_b) still require the middle certificate. The present
result proves no part of that middle interval and no part of the remaining
finite exterior interval. Exact joining at tau=5 avoids any rounded
endpoint comparison. The earlier choice9 is shortened, not a completed
finite-flow cover.

Both new scalar methods pass on the actual T=1 row. Informational values
are R approximately506529.193332153, B5 approximately-0.226329833538,
c_l-P5 approximately5.573491090564 and c_l-Q5 approximately5.571292813927.
Only exact rational endpoint comparisons are used for the strict public
claims R<510000,T<-.22,s>5.57 and vi>5.57. The saved-number audit reconstructs
the exact exponential sums by a different finite summation and checks all
18 strict comparisons. It does not claim to recompute the inherited modal
Green bounds. Both original and new proofs retain their full dependencies.
