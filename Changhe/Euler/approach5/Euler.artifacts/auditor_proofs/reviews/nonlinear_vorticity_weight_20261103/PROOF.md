# Nonlinear vorticity weights and their endpoint

## 1. Exact hypotheses and statement

Let 0<c<2/3, omega be any finite real number, Jx=e3 cross x, and let U in C2(R3;R3), P in C1(R3) satisfy

    (1-c)U+[(cI-omega J)y+U].grad U+omega JU+grad P=0,
    div U=0.

Assume Hb: U is bounded and U(R.) tends to zero in distributions as R tends to infinity. Write B=(cI-omega J)y+U, W=curl U, S=(DU+DU^T)/2, t=|W|² and s=|S|, with the Frobenius matrix norm.

Suppose a,M>0 and g in C1([0,M²]) satisfy g(0)=0, g'>=0 and

    H(t)=2g'(t)t-3c g(t)-at/2-(2/(3a))g'(t)²t²>0
                                            for 0<t<=M².       (1)

If sup|W|<=M, then U=0 and P is constant. In particular, for every 0<c<=1/2 and every omega,

    sup |curl U|² <= tstar := (15sqrt(7)-20)/42                 (2)

implies the same conclusion. Thus every nonzero profile in this class has supremum strictly greater than sqrt(tstar). The submitted strict inequality is a consequence; its endpoint is added here. No pointwise decay rate, helicity condition, angular truncation, global bound on DU or global integrability of W is assumed.

## 2. The two compactly supported identities

The distributional curl of the profile equation is classical after cancellation because U is C2. Taking its scalar product with W gives

    B.grad t=2(W.SW-t), div B=3c.                            (3)

The skew rotation contributes zero to this scalar equation. Let phi_R=chi(|y|/R), where chi is smooth, nonnegative, nonincreasing, one on [0,1] and zero on [2,infinity). If R>2||U||infinity/c, then

    B.grad phi_R=(chi'(|y|/R)/R)(c|y|+U.y/|y|)<=0.           (4)

The rotation is tangent to each sphere. The composition g(t) is C1; a C1 extension of g off its closed defining interval justifies the chain rule at an attained endpoint. Integrating (3) gives

    integral phi_R T=F_R:=-integral g(t) B.grad phi_R>=0,
    T=2g'(t)W.SW-2g'(t)t+3c g(t).                          (5)

All these integrals have compact support. Separately, divergence freedom and two integrations by parts give

    integral phi_R (s²-t/2)=E_R,
    E_R=integral U_i U_j partial_i partial_j phi_R.          (6)

Indeed s²-t/2=tr((DU)²), and the terms containing a divergence derivative vanish. The energy theorem A040/A052 under Hb, with its composition A1530, gives U=0 for c<2/5, finite L2 energy for c=2/5 and integral_(B_R)|U|²=O(R^(5-2/c)) for c>2/5. Consequently

    |E_R|<=C R^(-2)integral_(R<|y|<2R)|U|² ->0              (7)

for every 0<c<2/3. This is the sole nonlocal analytic input. Its hypotheses are exactly Hb and the displayed profile regularity; no pressure normalization is added. The full independent proof of this energy composition is in the team records, Sections1-2.

## 3. A nonnegative density proves the general lemma

For trace-free symmetric S,

    W.SW<=sqrt(2/3)s t.

To verify the constant, if lambda is the largest eigenvalue, the other two sum to -lambda, so s²>=lambda²+lambda²/2. Set

    D=a(s²-t/2)-T.

Since g'>=0, completing the square gives

    D>=a(s-sqrt(2/3)g'(t)t/a)²+H(t)>=0.                    (8)

Also (5)-(7) give integral phi_R D=a E_R-F_R<=a|E_R|->0. The cutoffs increase pointwise to one; monotone convergence therefore implies integral D=0, without presupposing the integrability of any separate term of D. Since D is continuous, it vanishes everywhere. Condition (1) then gives t=0. Formula (8) gives s=0 as well. Thus DU=0; Hb removes the constant velocity, and the equation makes P constant. This proves the stated lemma without an integration at infinity of unsigned stretching terms.

## 4. The explicit polynomial and its exact root

Take a=1 and g(t)=t+(21/20)t². Direct expansion yields

    H_c(t)=(3/2-3c)t+[(21/20)(4-3c)-2/3]t²
                         -(14/5)t³-(147/50)t⁴,
    H_(1/2)(t)=t²[47/24-(14/5)t-(147/50)t²],
    H_c(t)=H_(1/2)(t)+(3/2-3c)g(t).                       (9)

The bracket in the second line is strictly decreasing for t>=0, positive at zero, and has the single positive root tstar in (2). Multiplying its equation by600 gives 1764t²+1680t-1175=0. Its discriminant is 11113200=(1260sqrt(7))², yielding exactly (15sqrt(7)-20)/42. In particular 0<tstar<1. No numerical grid or floating computation is needed for these statements.

For c<=1/2, (9) is strictly positive on 0<t<tstar. Applying Section3 with any M² between sup|W|² and tstar proves the submitted theorem with strict supremum. The displayed decimals in the source merely approximate this exact algebraic constant. Its uniform nature does not mean it improves the earlier c-dependent constant sqrt(3)(1-3c/2) at every c.

## 5. Equality is also impossible

Assume the weak inequality (2). For c<1/2, the final term in (9) is positive at t=tstar, so the general lemma applies directly. At c=1/2, H is nonnegative on [0,tstar] and has exactly two zeros there, 0 and tstar. The argument through (8) still gives D=0 everywhere. Therefore continuous t takes values only in this two-point set. Connectedness of R3 makes t constant.

If t=0 the conclusion is already proved. Otherwise t=tstar>0. Equation (3) then gives W.SW=t at every point. The definition of D and its vanishing imply

    s²-t/2=3c g(t)>0                                    (10)

pointwise, with a positive constant right side. But (6) says its integral against phi_R equals E_R->0, whereas the integral of that positive constant is 3c g(t) R³ integral phi_1 and diverges. This contradiction excludes equality. This proof needs neither an attained maximum of W nor a separate bounded-gradient theorem.

## 6. Scope, numerical material and review

The entire submitted mathematical source and its check script were read. The completed square, coefficients, root and endpoint above are direct mathematical derivations. The expensive random check script was not run or relied upon. The proposed optimal-weight ODE and its numerical thresholds are outside this confirmation; an optimality/existence proof and rigorous numerical bounds were not supplied. The cutoff sign in (5) uses a global supremum restriction through (8), so this proof supplies no criterion involving only a far-field limsup. None of these additional smallness conditions is known here to follow from bare decay for a general profile.

The existing Theory Agent A source is a configured model collaboration input; runtime model attestation is unavailable. The endpoint argument is sent back through working files for comparison. No new model client or agent is used. No formal source or Lean build is produced. The main nonexistence conjecture under bare decay and arbitrary helicity remains open.
