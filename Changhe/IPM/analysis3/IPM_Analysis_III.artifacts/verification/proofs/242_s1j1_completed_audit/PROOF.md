# Completed shifted-junction section: accounting and exact input comparison

## Statement and exact objects

Use the exact38-column S1J1 section of proof 239, in its frozen metadata order and positive binary scales:

 h_i=2r^3 cos(theta)^4 sin(theta) B_i(log r)/s_i, 0<=i<38.

The input norm is the low L2 norm with weight

 w=|cos(theta)|^(-17/2) exp(mu(log r)),
 mu(t)=-17t/2 for t<0, and mu(t)=-5t/4 for t>=0.

Let G be the exact Gram of these functions. Proof 239 gives a positive definite enclosure for every entry by exact angular and radial moments, including both infinite ends, from the immutable original data. Let G_f and B_f be the exact dyadic interpretation of the binary matrices obtained below by summing only the four final part files and then taking their binary symmetric parts. The present result will establish exact cell accounting and a relative comparison of G_f with G. Its numerical bound is to be taken only from a passed evidence/check.json and RESULTS.md. Until that run passes, the comparison is a conditional computation specification.

No statement below identifies B_f with the exact output Gram. The division and total quadrature error are not certified. Every displayed eigenvalue is a floating diagnostic of a finite matrix pair, not an operator lower bound. In particular a positive finite-section eigenvalue proves neither injectivity nor a complement estimate.

## Exact accounting

The frozen producer declares the expected IDs0,...,1568 and four workers. Worker w receives precisely the ordered subsequence w,w+4,... of this set. Each final part file must have a done array equal to that subsequence and a diagnostic count equal to its length. The four subsequences are disjoint and their union is the expected set, with sizes393,392,392,392. Require all four completion records in the production log, no resumed-launch marker and no base accumulator files. Each retained checkpoint must be an initial subsequence of the corresponding final done array. It is then a duplicate and is excluded.

Sum the four final arrays entrywise with math.fsum and take the symmetric part in binary arithmetic. These operations define G_f and B_f, including their rounding. They do not repair cell production errors. Preserve and hash the metadata, frozen producers, final parts and completed log. The frozen producer hash, exact-template input setting, mode count530 and shifted join t_plus+1 must be the ones in proof 239. No unrecorded restart or changed basis is allowed by this proof.

## Input quadratic-form comparison

Let [G] be the640-bit entrywise enclosure of the exact Gram in proof 239. Choose any square matrix T whose entries are exact dyadic numbers and enclose, with directed arithmetic,

 e >= ||T^T G T-I||_2,
 d >= ||T^T(G_f-G)T||_2,
 e<1.                                                     (1)

Maximum absolute row sums of the symmetric matrices bound their spectral norms, so interval row sums suffice. The positive lower bound T^T G T >= (1-e)I proves T invertible. For every v=Tz,

 |v^T(G_f-G)v| <= d ||z||_2^2
                   <= d/(1-e) v^T G v.                    (2)

Thus the saved directed upper endpoint of d/(1-e) is a certified relative input-form error. A rounded displayed decimal is valid only if it is at least that endpoint. T may be selected by approximate Cholesky whitening of an interval midpoint: its construction is irrelevant to the proof once its exact dyadic entries and (1) are checked. The code uses a higher precision approximate whitener to avoid losing the near-dependent outer-column directions, then interprets its stored values exactly in Arb. It encloses all arithmetic in (1), including the interval radii. This is a comparison with the entire source-defined input form, not with its floating midpoint.

The exact source, coefficient, metadata, Gram and producer hashes are checked before any result is accepted. The basis and strain identities in proof 239 and high-domain classification in proof 240 are already independently confirmed. No new assumption about a floating rank is made.

## Floating restrictions and membership

The entire38-column section is in the low transport graph. Its intersections with the high correction space and full maximal high graph have exact dimensions32 and29 by proof 240. Their rational nullspace bases are in coordinates of the already scaled columns h_i. Restricting G_f and B_f with these exact rational bases therefore studies the declared subspaces. It still uses the low norms and the uncertified output matrix. Neither a high-domain restriction nor exact input integration turns it into a high-norm estimate.

For numerical stability, restrictions and whitening may be formed at fixed high floating precision before a symmetric double eigen-solve. The eigenvalues reported in RESULTS.md are explicitly numerical; the exact jump constraints remain rational. The code reports the common pure-column block separately. Any comparison with a different junction section requires that section's separate provenance. A changed outer-junction value is an observation about two finite sections, not a continuum or convergence theorem.

## Verification scope

The standalone argument is written before the completed-run calculation. The calculation is single-threaded and only uses local files. There are no formal sources or Lean builds. A failed check must be retained and cannot be called a certificate. Required successful evidence is the exact accounting, the bound(1), source hashes, and a separately labelled numerical table. No scalar normalization closure, full inverse, complement bound, high norm, quantitative smallness or profile existence is asserted.
