# Two lost hypotheses in the a5a3e2e8 assembly

## 1. Exact audit scope

The frozen coordinator report is this report, SHA256 a5a3e2e8b0ccc6034510e40d955561a1fc1439ca0b61fc84a37a24c7331f69ed. This result checks two new formulations in the report against their mathematical sources. It does not assert a counterexample to any Euler-profile theorem. All quantities below have their source meanings. The report is not approved as assembled at this pin.

## 2. Finite-order criterion as printed

The new Theorem 7(e) permits some c0 > 0, an integer n, and a sequence y_j tending to y0 with

    |curl U(y_j)| >= c0 |y_j-y0|^n.

It does not require y_j != y0. At any zero of curl U, choose n=1, c0=1 and y_j=y0 for every j. The inequality is 0 >= 0. Thus the printed predicate provides no finite-order or nonflatness condition at all. For an elementary local diagnostic, the smooth scalar f(y)=exp(-1/|y-y0|^2) for y!=y0, f(y0)=0 is flat at y0 and satisfies the printed sequence predicate. This scalar is not offered as a profile. It disproves the interpretation of the predicate as nonflatness; the corresponding weakened profile conclusion remains unproved.

## 3. Correct finite-order condition

The source is in the team records, Section 3. Its condition requires an integer n>=0, c0>0, and a sequence y_j!=y0 tending to y0 such that the same inequality holds. For a smooth field flat at y0, Taylor's theorem gives |curl U(y)|=o(|y-y0|^n) for every fixed nonnegative n, contradicting this condition after division by the positive |y_j-y0|^n. This condition therefore excludes flatness. The source's scattering proof, with all its profile and natural-regularity hypotheses retained, applies. Restoring these explicit quantifiers transfers the source result. No use is made of a lower bound on a neighbourhood.

## 4. General nonlinear-weight reduction as printed

The new Appendix A C65 row states that 0<c<2/3, ell>0, b>=0, b ell<2, a C1 weight g, and positivity of the four SF.8 functions for every t in (0,M^2] imply all hypotheses of SF.3. That implication omits the weight conditions of SF.8. For a direct countertest take c=1/2, ell=1, M=1, b=0 and g(t)=-1 on [0,1]. Then alpha=0 and delta=3/(2t)-1/2. Consequently the four functions are

    F_1a = (3/2)x^2 + 3/2 - t/2,
    F_1b = 6x^2 + 3/2 - t/2,
    F_1c = 2x^2 - 2x + 2 + 3/2 - t/2,
    F_3  = (3/2)y^2 + 3/2 - t/2.

For 0<t<=1, the first, second and fourth are at least 1. The third is at least 5/2, since 2x^2-2x+2=2(x-1/2)^2+3/2. These bounds hold in particular on every required interval. But g is negative, g(0)=-1, and g'(0)=0. Thus all four displayed positivity tests hold while the required weight premises fail. The statement that these tests alone imply the SF.3 hypotheses is false.

## 5. Correct nonlinear-weight reduction

The pinned source in the team records, Lemma SF.8, additionally requires M>0 and

    g in C1([0,M^2]), g>=0, g(0)=0,
    g'(0)>1/[4(1-3c/2)].

The reduction has a=1. With these hypotheses retained, the four positivity tests establish positivity of the density at every nonzero pair (S,W) in the prescribed product, as already independently proved in the team records. That proof controls t=0 separately and the four strain boundary reductions at t>0. The explicit C65 polynomial satisfies the required conditions, so the particular mixed-strain vanishing theorem and its constants are unaffected by this editorial omission.

## 6. Status and dependencies

The two printed implications above are REFUTED as sufficient finite-order and weight criteria, respectively. Their corrected formulations are CONFIRMED under their unchanged source hypotheses. The unrestricted smooth decaying rotating-profile problem remains OPEN. This review relies on direct elementary countertests, the complete original-vorticity finite-order proof and the independently checked nonlinear-weight reduction. No numerical approximation or new formal build is used. Other changes in this report pin are assessed separately; this proof does not approve the complete assembly.
