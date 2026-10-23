# SPEC v50 scope and provenance audit

Written 2026-10-21 before the checker. This is an audit of the recorded propositions, not a new existence theorem.

## Statement and dependencies

The valid finite-polynomial axis theorem is result 245: C>0, 0<t<1, w=1-t^2, y=Ct w^{-P}, 1<P<=2, G(y)=yH(w), and V_y=k(w), with real polynomials H,k, H(0)=0 and H'(0) nonzero. No real c and differentiable V can satisfy (cy+V)G_y=G on a nonempty open interval of positive y. No bound on the degrees is fixed. Its proof and its nine exact state applications are in research/hydrostatic_finite_axis_obstruction/PROOF.md and verification/CHECKS.json. Result 249 separately checked the full corrected report text and the continuum inverse application. This audit tests whether SPEC v50 states the same proposition.

## Scope defects

The restriction C>0 makes t to y a bijection from (0,1) to (0,infinity), since y_t=C[1+(2P-1)t^2]w^{-P-1}>0 and the endpoint limits are zero and infinity. C=0 destroys this parametrization. It is not an admissible positive-axis coordinate, so the theorem must explicitly exclude it; calling it a counterexample with a valid positive-axis inverse would be imprecise.

A singleton interval is not excluded by the theorem. In fact take C=1, P=2, H(w)=w, k(w)=0, V=0 and c=7/5. Then y=t/(1-t^2)^2, G=t/(1-t^2), and at t=1/2 one has y=8/9, G=2/3, G_y=15/28. Thus (cy+V)G_y=G at that point. The conclusion must retain 'nonempty open interval of y>0'. This example does not satisfy the equation on any open interval and is not a PDE profile.

The class is infinite: H_a(w)=a w for every a nonzero already gives infinitely many members. 'Class of polynomial axis data' avoids conflating finite polynomial degree of each member with a finite class.

## Numerical and historical scope

The maxima in G44 are the stationary-point searches of result 241 over 100<=y<=10^12, not certified suprema. The cap128 and continued128 values have ratio 0.00343793061799162/0.0032578547902581733, greater than one. A decrease holds between the three resolutions 96,128,160, and not between every successive saved state. The reported 43 and 21 percent sensitivities compare the expanded search to the prior fixed 774-point grid; they do not prove a global maximum.

The v50 changelog predates the independent 247 reconstruction. Its 64-state, 3e-6 and exact-amplitude claims were then awaiting verification. Preserve that history but append the corrections: 63 saved states; both primary rounded log columns agree within 5e-6; the table agrees to displayed precision; the physical amplitude is 3.99998200914248, which rounds to 4.0000. It is not exactly four. The 247 archive retains the failed initial comparisons and corrected tolerances.

## Verdict and scope

G43 requires the three local scope repairs above. G44's numerical values are confirmed only in the previously stated finite-search scope; describe decrease by resolution. No new claim of full-plane existence or nonexistence follows. T_end is not reached and the team endpoint is UNRESOLVED.
