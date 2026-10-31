# Rejected finite trials do not certify a non-descent direction

## Statement and notation

Let m be a positive integer and let lambda_1,...,lambda_m be any finite collection of nonnegative real damping parameters. Set L = max_j lambda_j. There is a smooth scalar residual r: R -> R with least-squares objective F(x) = r(x)^2/2 such that, at x = 0, every exact damped Gauss-Newton direction

    d_j = -r'(0) r(0) / (r'(0)^2 + lambda_j)

is a strict descent direction for F, but every full trial x = d_j increases F. Here strict descent means F'(0) d_j < 0. The statement concerns an exact, unconstrained one-dimensional least-squares problem with identity damping. It imposes no claim about the actual Euler trials.

## Proof

Choose any K > 1 + L and set r(x) = 1 - x + K x^2. This polynomial is smooth. At zero, r(0) = 1 and r'(0) = -1, so F'(0) = -1 and d_j = 1/(1 + lambda_j) > 0. Hence F'(0) d_j = -d_j < 0 for every j.

On the other hand, K d_j > 1 because K > 1 + lambda_j. It follows that

    r(d_j) = 1 + d_j (K d_j - 1) > 1 = r(0).

Both sides are positive. Squaring and dividing by two gives F(d_j) > F(0). Thus all m finite trials can be rejected for objective increase even though every direction is a strict descent direction. This proves the statement.

## Why this does not conflict with local descent

For each fixed j, F'(0)d_j < 0 implies F(t d_j) < F(0) for all sufficiently small positive t. In this example, one may take

    0 < t < min(1/d_j, 1/(K d_j)).

Then 0 < t d_j < 1, K t d_j < 1, and 0 < r(t d_j) < 1. The failed finite trial uses t = 1, which need not lie in this interval. Increasing a finite damping list does not remove the distinction: the construction chooses K after that finite list is specified. A fixed example need not reject every possible arbitrarily large damping value.

## Dependencies and scope

The proof uses polynomial differentiation and the scalar damped Gauss-Newton formula only. No external theorem or numerical experiment is needed. It is an exact counterexample, not a model fitted to the Euler problem. It does not prove that the campaign's frozen-weight directions were descent directions. Their signs remain a separate numerical claim, requiring the self-consistent objective gradient contracted with each actual direction, with numerical accuracy established, or equivalent local evidence. The observed rejection count can be stated without that additional claim.

## Verification evidence

verification/SOURCE_REVIEW.md identifies the draft passages and development records inspected. No Lean or other formal build was run; formal_sources/README.md records this limitation.
