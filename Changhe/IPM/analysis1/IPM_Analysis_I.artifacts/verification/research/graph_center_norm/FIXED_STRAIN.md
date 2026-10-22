# The same graph density at fixed canonical strain

2026-10-21. This is an additional consequence of PROOF.md with the same background and domain hypotheses. It needs no extra annular function and no extra regularity estimate. Assume the canonical strain is linear on the perturbation domain D_L, as it is for the fixed canonical inverse. Let 0<delta<=min(1,L)/2 and define

    b_delta=(4h_delta-h_(2delta))/3.

Both terms belong to D_L. The exact identities J(h_delta)=J(h_(2delta))=1 and Sigma(h_delta)=delta^2/56 give

    J(b_delta)=1,  Sigma(b_delta)=0.

Moreover b_delta tends to0 in the graph norm, since

    ||b_delta||_X+||Lb_delta||_X
       <= (4/3)(||h_delta||_X+||Lh_delta||_X)
          +(1/3)(||h_(2delta)||_X+||Lh_(2delta)||_X).

The right side tends to0 by(1). In the expression for Lb_delta the rank-one term cancels exactly by linearity, not by an error estimate. The function is C5, compactly supported and has a continuous even-even center factor. It need not have a positive factor away from the center; no such positivity is a hypothesis of this perturbation theorem.

For any h in D_L and any j, the functions h+(j-J(h))b_delta lie in the same affine strain level as h, have central coefficient j, and converge to h in the graph norm. Therefore every central coefficient level is dense relative to every nonempty strain level in D_L. In particular, for a fixed C an estimate ||h||_X<=C||Lh||_X on {J=0,Sigma=0} holds if and only if it holds on {Sigma=0}. The proof is to approximate any member of ker Sigma by h-J(h)b_delta and pass to the limit, as in ADDENDUM.md. This is a statement about those specified algebraic subspaces; it does not assert that Sigma is graph-continuous or that D_L is complete or closed.

If a nonzero K in D_L satisfies Sigma(K)=0 and LK=0, both exact constraints J=0 and Sigma=0 fail to restore the displayed estimate: K-J(K)b_delta is an explicit counterexample sequence. At a trial with nonzero LK, the same construction gives only the necessary limiting quotient already described. No actual K membership, kernel or numerical spectrum is supplied here.
