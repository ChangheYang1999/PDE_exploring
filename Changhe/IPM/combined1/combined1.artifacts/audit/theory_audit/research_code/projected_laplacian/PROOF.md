# Selected-mode weighted Laplacian obstruction

## Statement

Let Y be the exact dyadic norm of T4-058, with the fixed unit and annular plateaux, 0<a<2 and 0<s<1. Let Pi_S denote the orthogonal angular projection onto a finite set S of positive sine frequencies. For any S1 residual F in Y,

    Y(F)>=5^((a-2)/2)||<r>^(2-a) Delta Pi_S F||2.       (1)

If the finite-generator background meets the hypotheses of the audited inverse floor T4-097, the closure scheme needs

    5^((a-2)/2)||<r>^(2-a) Delta Pi_S F||2
       <B(a)=sqrt(8pi)(1+c-ca)^2/(1+a), 0<a<1+1/c.     (2)

Each violating point is a necessary-test failure at its a. Excluding the full parameter range requires an explicit cell cover. No such conclusion follows from a finite grid alone.

## Proof

Angular projection commutes with the polar Laplacian. Its L2 operator norm is1 on each circle. The weight depends only on radius, so integration gives ||<r>^(2-a) Delta Pi_S F||2 <= ||<r>^(2-a) Delta F||2. The audited continuous plateau estimate T4-107 gives(1). Combine it with the audited necessary ceiling from T4-097 and T4-096 to get(2).

For a finite canonical mode, write

    Pi_S F = r sum_(ell,n in S) z^(ell delta/2) P_(ell,n)(t) sin(n theta),
    t=r²/(1+r²), z=1-t, delta=1-1/c.

Apply T_(d,1) twice and subtract n², where T_(d,k)P=(k-2dt)P+2t(1-t)P'. The exact divisibility test K=tL and the finite moment formula are those of T4-107. All cross terms between branches of the same angular frequency are retained; different angular frequencies are orthogonal. The resulting squared norm is a finite sum of rational coefficients divided by affine functions of a, times pi/2. All individual diagonal integrability conditions are checked before summation.

## Candidate007 input and scope

The first run uses S={1} and the exact candidate C1-N1-007-d2w-j7-e2bal. The stored first-mode polynomial was already independently reconstructed from the exact canonical potential in T4-108. Its frozen comparison record and input hashes accompany this computation. This is a lower bound from one angular mode, not the full weighted Laplacian norm. Adding disjoint modes may only increase the squared lower bound.

The computation records pointwise bounds and cell comparisons. A failed comparison is inconclusive. This elementary consequence of audited theorems and its new numerical application remain open pending independent reproduction of the new moment values.
