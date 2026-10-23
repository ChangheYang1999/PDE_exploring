# Audit of draft 47 and the 24 low-slope endpoint formulas

Written 2026-10-21 before the checks below. The report is frozen in evidence/lead_merge_audit/draft47. The purpose is to audit stated finite observations and their scope, not to establish an IPM endpoint.

## Exact quotient criterion

Use the finite Q formula and radial map proved in ../low_slope_state_audit/PROOF.md. Let a=B_0(-1), d_0=B_0'(-1), b_1=B_1(-1), and ell_c=L 2^{-kappa}. Since s=r^2/ell_c^2+O(r^4), expansion of (1-s) sum_j s^j B_j(2s-1) cos(2j theta) gives

    rho=y [a + (b_core x^2 + e_core y^2)/ell_c^2 + O(r^4)],
    b_core=2d_0-a+b_1,   e_core=2d_0-a-b_1.

For binary coefficients all three core coefficients are rational. Compute a=sum_k(-1)^k B_0k, d_0=sum_k(-1)^(k+1) k^2 B_0k, and b_1=sum_k(-1)^k B_1k. If e_core/a>0, then q(0,y)>1 for all sufficiently small nonzero y. If b_core/a>0, q(x,0)>1 for all sufficiently small nonzero x; continuity of the smooth quotient then gives q>1 at some y!=0 as well. Either positive coefficient disproves q<=1 globally for that saved formula. A nonzero b_core or e_core proves rho-a y is not flat at the origin. If both are nonpositive the criterion is inconclusive, not a confirmation of a global bound. These statements follow directly by dividing the displayed expansion by a y and using the sign of its first nonzero quadratic coefficient. The separately established finite-formula smoothness uses the radial inverse function theorem and homogeneous Cartesian angular factors, without assuming an exact PDE.

## Log and table observations

An accepted producer step is identifiable by its printed norm decrease, positive step length, and the logged post-update ell and a. The producer source is inspected only to verify this logging convention; it is not imported or executed. A regime-exit statement must distinguish six initial releases from six continuations. A continuation already outside a<2(ell-1) does not newly leave that regime on its first step. A failed first line search gives no accepted step.

The 24 table rows are compared with the saved coefficient slope and ell and with their logs. Reported bin residuals remain producer evaluations unless one of the independent canonical audits is cited. Their ranges can be checked as transcription/arithmetic without converting them to independently verified residual bounds. Rounded decimal endpoints in prose denote rounded observed values.

## Point selection and report logic

Result 143 selected the six maximizers of the canonical residual from result 136 on the shared sample set. The producer interpolant was evaluated at those same physical points afterwards. The algebraic identity between residual differences and velocity differences is pointwise. It neither changes the maximizer provenance nor proves a bound at unexamined points. The radius-choice repair in A.3.67 is valid for k>=1 because R_k^(-k delta/2) tends to zero, while k=0 needs a separate unrestricted radius. Other claims depend on the completed audits 142, 143, 145 and 146, not on this finite table.

## Scope

Exact signs apply only to the saved 24 formulas, with their hashes recorded. A failed one-sided bound for those formulas is not a nonexistence theorem for any branch. Full canonical residuals of the other 22 states, global convergence and the primary YES/NO endpoint remain OPEN. Actual model collaboration and dated verification evidence are recorded separately.
