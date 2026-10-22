# Exact external source constraints of saved floating vectors

## Statement, inputs and scope

Fix the frozen column families and exact logarithmic joins t_-<t_+ of external_constraint_rank/PROOF.md, with its mandatory source and post-review qualifications. A saved coefficient array is interpreted as exact dyadic numbers, one per binary64 entry. This mathematical interpretation is distinct from the unknown exact singular vectors approximated by that array. For each mode m and each join j define C_{m,j,0}(h) and C_{m,j,1}(h) to be the sum over function columns in mode m of h_i times their left-minus-right radial value and first t-derivative traces at j. The source-assigned KP, TAU and extra coordinates have zero columns in this particular matrix. This definition does not establish their physical traces.

For each specified saved vector and each of the4M functionals, the proposed finite audit will reconstruct the coefficient exactly, form its exact trace sum and determine whether it vanishes. A nonzero exact sum refutes membership of that saved dyadic vector in the kernel of this exact source-defined matrix. A zero sum confirms only that one functional. Neither outcome certifies the numerical SVD, the unknown ideal singular vectors, a physical full field containing additional components, internal matching, Sobolev membership or an IPM endpoint.

## One-sided trace reconstruction

A stored piece on a finite interval [a,b] is exp(alpha(t-a)) P(t-a); an inner half-line piece with right endpoint b is exp(alpha(t-b)) P(t-b); an outer half-line piece with left endpoint a uses t-a. At an external join, pieces ending there contribute their left trace and pieces starting there contribute their right trace. A piece extending across a join contributes equal left and right limits and hence zero jump. The stored pieces must have disjoint interval interiors for each column, and there must be at most one piece arriving and one leaving at either join; the audit must check these facts or reject its input.

For x equal to the appropriate shifted endpoint coordinate, the value and first derivative are

    exp(alpha x) P(x), exp(alpha x)(alpha P(x)+P'(x)).

The intended exact audit is limited to cases alpha x=0 for every nonzero endpoint contribution. This is checked, not assumed from a label. All endpoints, alpha and polynomial coefficients are exact dyadics read from the saved columns. Consequently these two traces are exact rationals. The first implementation will use rational Horner evaluation and the product rule. A separate implementation will directly sum monomials and their derivative terms using the same exact inputs. Both independently reread the stored vector entries; their import route and shared data dependence must be disclosed.

## Matrix functional proof

One-sided limits and derivatives of a finite linear combination are the same finite linear combinations of the individual traces. The difference of the two sides is therefore exactly sum_i h_i j_i. Grouping by the saved angular modes gives the functionals just defined. The angular factors cos(theta)^2 sin(theta) cos(2m theta) are linearly independent, as proved in topic147, so for the function-column part all external radial value traces agree exactly if and only if every value functional vanishes; first derivative matching additionally requires the derivative functionals. This equivalence concerns the function-column part. No cancellation with the omitted physical KP/TAU/tail fields is presumed.

For each binary64 vector entry, decoding the integer sign, significand and power-of-two exponent gives its exact rational value. Exact multiplication and addition with the trace rationals gives an exact rational functional. A nonzero numerator is decisive for this finite source-matrix test even if the absolute value is extremely small. It gives no positive distance bound in any PDE norm, and it is not evidence that the floating computation is inaccurate to its intended tolerance.

## Verification obligations

Capture immutable saved-vector files and the exact frozen column files, bind their scalar Mh,nF, joins and mode arrays, and compare their claimed source hash with the captured source where available. A recorded source hash is a metadata claim, not external execution attestation. Cover all5 supplied Fminus vectors in each of the M16 and M24 H1q/NJ1 files, all modes and both external joins and orders. Keep exact sums and outward decimal magnitude intervals in JSON, with independent reconstruction, explicit counts, actual model review and final adjudication. Do not adapt the choice of vectors after seeing their constraints.
