# Verification scope

The proof is analytic and precedes numerical screening. No formal proof assistant was run. The principal screen reconstructs the exact rational polar coefficients, evaluates radial coefficients with Arb384, and then uses floating trigonometric samples. Its output is FLOAT only. Positive sample margins are not continuum bounds; negative sample margins motivate exact point tests but are not yet interval certificates. The kernel, finite-rank error and high-space closure were not evaluated.

The sample grid contains321 radii and257 angles. At a=1.2,R=1 the sampled margin is0.14924; at a=1.4,R=4 it is negative. These observations guide a subsequent choice of weight but do not establish an inverse. Actual numerical runtime3.156791909 seconds, as recorded in principal_screen.json.
