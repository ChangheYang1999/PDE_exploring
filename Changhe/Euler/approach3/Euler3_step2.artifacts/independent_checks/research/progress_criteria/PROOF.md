# Finite accepted-step stopping predicate

Status: elementary proved finite-data statement. Its use on a stored trajectory assumes that the entries are correctly labelled accepted and contain objective values at the corresponding iterates.

## Statement and notation

Let L_0,...,L_n be positive real numbers representing one objective on a sequence of accepted iterates. Let 1 <= k <= n and let epsilon > 0. Define d_k=(L_(n-k)-L_n)/L_(n-k). Then d_k < epsilon holds if and only if L_n > (1-epsilon)L_(n-k). If d_k >= epsilon, any stopping rule requiring d_k < epsilon as one of its simultaneous requirements fails. This does not depend on the value of a second, wall-time progress condition. If the alternative early-termination route requires another predicate B and B fails, that alternative also fails.

## Proof

The denominator L_(n-k) is positive. Multiplying the strict inequality by it and moving terms proves the equivalence. A conjunction cannot hold when one of its required predicates is false. The same logical fact applies to the early-termination route. No property of a differential equation enters this argument.

For binary64 numbers imported as their exact dyadic rational values, the comparisons above can be performed by integer arithmetic without rounding. This proves the stopping decision for the stored numbers only. It gives no enclosure for the objective of the exact represented field, and does not prove that a producer accepted a step under its stated rule.

## Window and scope

Fifty accepted transitions use 51 endpoint objective values. A convention using the last 50 stored accepted endpoints spans 49 transitions. The audit reports both to expose this boundary convention. A reused local iteration counter is not a global index; an explicit cumulative index, or the verified sequence order, must be used across restarts.

Decreasing weighted objective values at changing parameters need not imply decreasing physical Euler residuals. A failed progress predicate establishes incompleteness under that specific registered rule, not nonexistence, a representation floor, or an impossibility of eventual convergence. No rate per hour is inferred from accepted-step counts. Wall-time assertions require separately bound time records.

## Dependencies and verification

Only ordered-field arithmetic and propositional logic are used. Numerical evidence is in the adjacent verification folder and its referenced immutable captures. No formal prover was run; the formal folder is reserved and empty.

## Parameter ranges and an exact logarithmic threshold

Let c_i be real and w_i>0 for a finite nonempty accepted-iterate window. Its c range is max(c_i)-min(c_i). Since the real logarithm is strictly increasing, the log w range is log(max(w_i)/min(w_i)). A sequence is nondecreasing exactly when every adjacent difference is nonnegative, and nonincreasing exactly when every adjacent difference is nonpositive. Testing every adjacent difference is necessary; an endpoint change alone does not establish monotonicity.

For an exact comparison with t=1/1000, define L=sum_{k=0}^8 t^k/k! and U=L+(t^9/9!)/(1-t/10). Every term after the ninth is at most t/10 times its predecessor. The positive exponential series therefore gives L<exp(t)<=U. If the rational ratio q=max(w_i)/min(w_i) exceeds U, its log range exceeds t. If q<=L, its log range is below t. The narrow interval between L and U is left undecided by this test. Binary64 inputs interpreted as exact rationals permit all these comparisons without rounded logarithms. Decimal logarithms may separately supply displayed values.

These finite-data statements do not bound unrecorded iterates. If the accepted-step window already violates a required range threshold, a conjunction also requiring a wall-time window fails without measuring that other window. A monotone drift is an observed property of this window, not evidence that the sequence must continue in that direction.
