# Exact nonlinear vorticity table and matrix endpoint

## 1. Statement and hypotheses

Let Jx=e3 cross x, let omega be any real constant and let 0<c<2/3. Let U in C2(R3;R3), P in C1(R3) solve

    (1-c)U+[(cI-omega J)y+U].grad U+omega JU+grad P=0,
    div U=0.

Assume Hb: U is bounded and U(R.) tends to zero in distributions as R tends to infinity. Write W=curl U, S=(DU+DU^T)/2, t=|W|² and B=(cI-omega J)y+U. All matrix norms below are Frobenius norms. Under these hypotheses each row of this table is an independent implication:

| c_k | b | q | T_k |
| --- | --- | --- | --- |
| 0.41 | 0.65 | 0.41 | 0.894 |
| 0.42 | 0.68 | 0.45 | 0.870 |
| 0.43 | 0.71 | 0.49 | 0.847 |
| 0.44 | 0.74 | 0.54 | 0.825 |
| 0.45 | 0.77 | 0.60 | 0.803 |
| 0.46 | 0.81 | 0.66 | 0.779 |
| 0.47 | 0.85 | 0.74 | 0.756 |
| 0.48 | 0.90 | 0.84 | 0.731 |
| 0.49 | 0.95 | 0.94 | 0.707 |

Every displayed terminating decimal is exact. If 0<c<=c_k and sup_R3 |W|<=T_k, then U=0 and P is constant. The bound is global and includes equality. No statement that these extra hypotheses follow from bare decay is made. Separately, for 0<c<=1/2, the same conclusion holds when

    sup |W|² <= tstar=(15sqrt(7)-20)/42.

Section 4 verifies the source's alternative endpoint proof. This is the same endpoint already established independently in A1586, not a new threshold.

## 2. The integral criterion and exact matrix completion

The energy theorem A040/A052, with the composition checked in A1530, gives

    R^(-2) integral_(R<|y|<2R) |U|² ->0.                    (1)

For clarity, its relevant bounds are U=0 for c<2/5, finite L2 energy at c=2/5 and integral_(B_R)|U|²=O(R^(5-2/c)) for 2/5<c<2/3. This is the sole previously proved global analytic input. Its proof and pressure hypotheses are in the team records. Hb is exactly the hypothesis used here.

Let phi_R=chi(|y|/R) with chi smooth, nonnegative, nonincreasing, one on [0,1] and zero on [2,infinity). If R>2||U||infinity/c then B.grad phi_R<=0, because the rotation is tangent to spheres. The vorticity identity and div-curl identity are

    B.grad t=2(W.SW-t), div B=3c,
    integral phi_R (|S|²-t/2)=E_R,
    E_R=integral U_i U_j partial_i partial_j phi_R ->0.    (2)

Both integrations have compact support; the last limit follows from (1). If a>0, g is C1 on [0,M²], g(0)=0, g'>=0 and sup |W|<=M, integration of the first identity gives

    integral phi_R [2g'(t)W.SW-2g'(t)t+3c g(t)]
        =-integral g(t) B.grad phi_R=:F_R>=0.             (3)

A C1 extension of g from its closed interval justifies the chain rule at endpoints. Define

    H(t)=2g'(t)t-3c g(t)-at/2-2g'(t)²t²/(3a),
    D=a(|S|²-t/2)-[2g'(t)W.SW-2g'(t)t+3c g(t)].          (4)

Set Q=W tensor W-(t/3)I. Since tr S=0, S:Q=W.SW and |Q|²=2t²/3. Expanding a square therefore gives the exact identity

    D=a|S-(g'(t)/a)Q|²+H(t).                             (5)

This proves that, for fixed W, the minimum of D over all trace-free symmetric S is exactly H(t). It does not assert that every minimizing matrix field is compatible with one Euler velocity field.

If H>0 on (0,M²], then D>=0 and (2)-(3) yield integral phi_R D=aE_R-F_R<=a|E_R|->0. Monotone convergence, applied to the nonnegative density D rather than its separate unsigned terms, gives D=0 everywhere by continuity. Thus t=0, then S=0 by (5), so DU=0. Hb removes the constant U; the equation makes P constant. This proves the criterion used in Section 3 with no boundary term omitted and for every omega.

## 3. Exact certification of all nine rows

For a=1 and g(t)=bt+qt², expand (4):

    H(t)/t=f(t)=A+Bt-Ct²-D0t³,
    A=b(2-3c)-1/2,
    B=q(4-3c)-2b²/3,
    C=8bq/3, D0=8q²/3.                                  (6)

All rows have b,q>0, so f''(t)=-2C-6D0t<0 on [0,T_k²]. A concave function on this interval lies above the line joining its endpoint values. Hence f(0)>0 and f(T_k²)>0 imply f(t)>=min(f(0),f(T_k²))>0 throughout. A Sturm root count is unnecessary.

The exact rational inputs are in the team records. The independent script in the team records expands (4) by polynomial operations, compares the result with (6), and evaluates both endpoints with Python Fraction. The retained in the team records contains every coefficient, every exact rational endpoint, the positive lower bound and the five pass/fail tests for each row. All nine rows pass. In particular, the left endpoints in table order are

    1/2000, 2/625, 41/10000, 2/625, 1/2000,
    11/5000, 3/2000, 1/250, 7/2000.

Every right endpoint is also an explicitly retained positive rational. These are exact arithmetic comparisons, with no rounding interval, sampled approximation or optimization claim. The computation question and pass criterion were recorded before execution. The single-core calculation ran from 2026-11-03T16:14:20.977250+00:00 to 2026-11-03T16:14:20.978474+00:00, with monotonic elapsed time 0.0012182272039353848 seconds.

At c=c_k this proves H>0 on (0,T_k²]. If 0<c<=c_k, then

    H_c(t)=H_(c_k)(t)+3(c_k-c)g(t)>=H_(c_k)(t).

The criterion in Section 2 applies with M=T_k, proving every row including its weak endpoint. A nonzero profile in Hb must consequently have sup |W|>T_k for each applicable row. The exact input and script hashes are recorded in the result and manifest; importing a table by itself would not prove this conclusion.

## 4. Rechecking the source's alternative algebraic endpoint

For g=t+(21/20)t², a=1, expansion yields

    H_(1/2)(t)=t²[47/24-(14/5)t-(147/50)t²].              (7)

The bracket decreases strictly on [0,infinity) and its only positive root is tstar. For c<1/2, H_c=H_(1/2)+3(1/2-c)g is positive on (0,tstar]; Section 2 applies. At c=1/2, H is nonnegative on [0,tstar], so the same integral argument yields D=0. Equation (5) forces continuous t to take only the values 0,tstar. Connectedness of R3 makes t constant.

If t=tstar>0, the transport identity in (2) gives W.SW=tstar. On the other hand, equality in (5) gives S=g'(tstar)Q, hence W.SW=(2/3)g'(tstar)tstar². The two equations would require (2/3)g'(tstar)tstar=1. But

    g'(tstar)=3sqrt(7)/4,
    (2/3)g'(tstar)tstar=5/4-5sqrt(7)/21<1,

where the final strict inequality follows already from sqrt(7)>21/20. This is a contradiction. Therefore t=0 and U=0. The alternative proof agrees with A1586's independent compact div-curl contradiction.

## 5. Precise limits and combination of thresholds

The exact matrix minimum in (5) is confirmed. It alone does not establish existence, uniqueness, endpoint behavior, admissible rescalings or optimality for the singular ODE proposed in the source. Those assertions and the numerical ODE threshold values remain OPEN in this audit. The source's phrase that this density family cannot do better than the ODE supremum needs that missing ODE argument before it can be treated as a theorem.

The earlier linear criterion is strict: sup |W|<sqrt(3)(1-3c/2). The uniform polynomial and table criteria above include equality. Thus a combined statement may give the union of these conditions, or the strict inequality below their maximum. It cannot automatically give a weak inequality at the maximum when the strict linear criterion is the largest one. Rounded decimal approximations must not be written as exact equalities to sqrt(tstar).

This proof uses a global supremum. It does not prove a criterion with only a small far-field limsup, nor remove the smallness condition from the target conjecture. The full source and check script were read; the source's random sampling and search script were not executed. Existing configured model working files are the collaboration input, with runtime model attestation unavailable. No new client or agent, formal build or external write was used.
