# Normalization and the scope of response-growth arguments

Status: logical audit. The two implications below are checked against previously admitted results. No new asymptotic claim about the IPM recursion is made.

## Pure powers depend on the resonant normalization

Fix delta=4/9, c=9/5 and f_1=sin(11 theta). A statement that its pure density and stream expansion is obstructed at order18, without specifying the free harmonic at order9, is false. Topic227, admitted inV484, constructs a unique choice of resonant harmonics giving a pure density and stream series at every order, with all weighted derivatives converging on every closed exterior r>=R>2^(213/4). This is a direct counterexample to the unqualified statement.

There is no contradiction with failure at order18 when the order9 free harmonic is fixed to zero. The obstruction at order18 is affine in that free harmonic, with nonzero response. Its zero at the tuned harmonic differs from its nonzero value at the canonical choice. The canonical obstruction and the tuned construction concern different series. The common potential still requires the order9 logarithm established in228; pure density and stream series need not have a pure potential.

The same normalization qualifier is needed when quoting the earlier order18 experiment for sin(13 theta). Its later obstruction at order36 after tuning is a separate admitted result and is not removed by this observation.

## Decreasing response moduli do not alone imply increasing growth

At successive nonzero tuning steps write H_k=-R_k/sigma_k, where R_k is the obstruction before adding the current harmonic and sigma_k is its response. Whenever both numerator terms and both responses are nonzero,

    |H_(k+1)|/|H_k|
       = (|R_(k+1)|/|R_k|)(|sigma_k|/|sigma_(k+1)|).

This is an exact algebraic identity. A decreasing response modulus enlarges its second factor. It says nothing about the first factor. For an elementary counterexample to the algebraic implication, set sigma_k=1/k and R_k=1/k^2 for every positive integer k. Then H_k=-1/k, so its magnitude decreases although the response modulus decreases. Taking instead R_k=sigma_k A^k gives H_k=-A^k with a constant per-step growth factor A for any fixed A>0.

These examples are not asserted to be IPM sequences. They prove only that the displayed tuning identity, without information on the obstruction numerators, does not imply a growth or divergence law. Any assertion about the actual IPM sequences needs additional bounds or measured numerator data. The observed finite growth transitions may be reported as occurring in the same computed range as small responses. Eventual acceleration, an asymptotic growth constant, and a causal explanation based on the denominator alone remain open.

## Dependencies and scope

Dependencies are the affine tuning identity in131/144, the all-integer sin11 convergence certificate227 and its potential reconstruction228. Frozen excerpts in sources identify the statements under audit. This is an audit of normalization and logical scope, not a rerun of those certificates.
