# Audit of theory v05 and correction of the T4 working summary

## Scope and dependencies

The immutable target is source/theory_v05.md, SHA256 b003dd48930032569529ad4962bcb64cb531bb8dab3b616d82f2e56aa47a6cc5. All changes from the previously audited v04 were read, with the unchanged statements checked against ../theory_v04_audit/PROOF.md and its earlier dependencies. This is an audit of deductions and publication accuracy, not a new inverse theorem. The candidate certificates retain their original spaces, fixed-c chart, canonical velocity, complete weak equation and strict inequalities.

The earlier directed-rounding, dilation-covariance, weighted-endpoint and chart-status repairs are correctly incorporated at their main locations. The v05 distance table adds candidate015 to the eleven prior rows. Every one of its36 ratios is checked against the two rounded-up scalar budgets and the larger exact graded bound25/54684. The table uses the weaker n19,K600 certificate available at publication; the later n23 certificate does not make the historical row false.

## 1. Probe reductions do not establish reduced actual distance

A bounded linear functional phi supplies a necessary bound for the norm of a solution to a linear equation Lh=-F; the analogous quadratic weak bound in this campaign has the same one-sided role. Nothing in that role depends on whether an optimizer used phi. Neither a design probe nor a held-out probe, alone or as a finite collection without a proved upper comparison, determines the true distance.

For a complete counterexample take the real Hilbert space R2 with Euclidean norm and L the identity. The equation h=-F has the unique correction -F, so its distance is exactly ||F||. Use e1 as the design functional and e2 as the held-out functional. Let F_before=(0,1) and F_after=(3,1/2). The held-out lower bound falls from1 to1/2, whereas the actual distance increases from1 to sqrt(37)/2. Thus even a strict improvement of a genuinely independent held-out row does not establish an improvement of actual distance.

Conversely, a design probe alone can prove a distance change in a restricted problem. If F is known a priori to belong to span(e1), its e1 pairing equals its norm. Hence the claim that only held-out rows can test whether the distance moved is also false as a universal restriction. For any finite collection of probes in an infinite-dimensional Hilbert space, adding an arbitrarily large vector in their common kernel leaves every measured value unchanged. These exact examples explain the missing ingredient: a quantitatively exhaustive family or a separate upper bound.

Replace v05 summary item5's final clause by: “Held-out probes test necessary conditions that were not explicitly included in the analytic pairing objective. Reductions in either family of lower bounds do not establish a reduction of the actual distance.” This is consistent with the already audited weak-distance theorem and T4-219. It changes no certified exclusion.

## 2. Optimization records do not prove a span floor

Section6 item3 correctly says that the recorded optimization does not establish zero leverage, but then calls the benefit of new R25 functions consistent with a span limit of the earlier basis. The latter may be a conjectural interpretation, but the only supported conclusion is that the tested expanded basis and optimization produced better values for some probes. Even exact arithmetic for those finite trials would not certify a lower bound for the earlier span minimum.

Indeed, minimize |-1+h| over h in R. The exact infimum is zero. A damped Gauss-Newton step with damping lambda>0 is h=1/(1+lambda), whose residual magnitude lambda/(1+lambda) can be arbitrarily close to1. A stalled damped residual is therefore compatible with complete representational ability. A positive span floor requires a lower certificate for the stated optimization problem, as in ../damped_diagnostic_scope/PROOF.md. Replace “span limit” here by “a benefit from the tested expanded basis”; retain the FLOAT label.

## 3. Finite exact Beta formulas versus truncated asymptotic models

For an integer L>=0, real b>-1 and a finite polynomial P(v)=sum p_j v^j, linearity of an absolutely convergent finite integral gives

    integral_0^1 v^b (1-v)^L P(v) dv
      =sum_j p_j B(b+j+1,L+1).

This is exact, in any angular mode after exact orthogonality. For example b=1/2,L=2,P=1+v gives64/315 by direct polynomial integration. Outward evaluation of these Beta terms is a certificate when the polynomial is the complete integrand. Higher angular frequency does not turn it into an uncertified approximation.

An infinite asymptotic expansion truncated to finitely many sectors is different: the omitted integral remains and needs a bound. Therefore section6 item8 must say “finite asymptotic-sector models in the other modes still require a certified remainder or a complete residual calculation.” Its unqualified “finite Beta-sum pairings remain FLOAT” would incorrectly include the complete higher-mode certificates already used elsewhere in the same report. The first-mode uniform ceiling is a bound on a test value, not an upper bound on actual correction distance.

## 4. Framework status is not a nonexistence theorem

SectionR2(e) still says “no such framework exists”. No proof ruling out every framework with decaying weights is supplied. The supported statement is “none has been constructed or verified in this program.” Earlier sections of v05 already use this qualification. This is a report-status correction, not a proof that any such framework can be built.

## 5. An own-summary rounding error

The frozen source/AUDIT_SUMMARY_before_310.md contains the false inequality

    25/54684 < 0.00045717.

Cross multiplication gives54684*45717=2499988428<2500000000, so the displayed decimal is instead strictly smaller than25/54684. A safe upper decimal is0.000457173, since54684*457173=25000048332>25000000000. The corrected working summary uses the exact rational and this upward bound.

The v05 paper separately has a sharper graded expression50/(651 sqrt28248), which is below0.00045717. That finer inequality does not justify replacing the larger25/54684 by the same decimal. The present table checks deliberately use25/54684; no exclusion or table ratio relies on the own-summary typo.

## Verdict boundaries

The four unsupported wordings above are refuted as deductions; the replacement scope is confirmed by the explicit arguments. The own-summary displayed inequality is refuted and corrected. The numerical table and new status transitions receive an arithmetic verdict only after the adjacent checker completes. None of these checks constructs a stationary solution or promotes a pending candidate calculation.
