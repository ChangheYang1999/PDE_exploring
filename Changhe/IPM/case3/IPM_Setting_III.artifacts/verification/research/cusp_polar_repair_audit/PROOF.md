# Audit of the producer's corrected polar cusp evaluation

Result236. This proof and scope note precedes the record checker. It concerns only the three frozen c=3 hsH hydrostatic trials independently evaluated in229 and231. The producer's new polar derivative may be compared with those independently derived exact-data results. Its entire regenerated table is not thereby independently checked.

Let f be homogeneous of degree p in (0,1), q(s)=f_xx(1,s), and Q the leading coefficient of q(s) as s tends to infinity. Define C(S)=integral_0^S s[q(s)-Q s^(p-2)]ds and T(S)=integral_S^infinity s[q(s)-Q s^(p-2)]ds. These converge at the relevant endpoints for the smooth finite angular trigonometric profiles. Then the full cusp coefficient is exactly C_p=C(S)+T(S). The independently derived convergent tail series and its explicit truncation bound in229 justify evaluation of T(S). This bound concerns an exact analytic series; numerical rounding has separate empirical checks.

The fact T(S)=O(S^(p-2)) does not imply its absolute size is about1e-10 at S=1e6: the implied coefficient depends on the angular profile and may be large. Dividing by its nonzero K preserves the additive identity. Subtracting T(S)/K from the independently evaluated full coefficient yields the exact cutoff coefficient, which is the appropriate object to compare with a finite-S producer integral. Adding the same tail to a producer cutoff separately reveals its remaining quadrature/rounding error.

The corrected polar formula
q=r^(p-2){p[(p-1)cos^2(theta)+sin^2(theta)]Theta-2(p-1)sin(theta)cos(theta)Theta'+sin^2(theta)Theta''}
is the Cartesian second derivative obtained by differentiating r^p Theta(theta). Its terms need not cancel at relative order s^-2 near the axis, unlike p(p-1)F-2(p-1)sF'+s^2F''. Result229's manufactured test independently demonstrated that numerical mechanism. Agreement of the corrected producer cutoffs with the independent cutoffs supports the reported correction for these trials; it does not establish a universal error bound.

For a polynomial trial with actual stored exponent p and c=3, G(0,y)=K y^p+lower powers. The leading transport discrepancy is (cp-1)K y^p. Its normalized scaled coefficient is (cp-1)/(|cp|+1) times y when the leading transport and density have these signs. With exact cp=1, K different from1 causes no such discrepancy. Thus K-1 is neither the source of the extra linear contribution nor an independent obstruction to a constant axis limit. A nonzero r2 already gives a growing y^p term; the binary cp-1 gives an additional linear term at larger radius. The recorded exact K values may independently disprove an asserted size for K-1.

Dependencies: hydrostatic_cusp_row_audit/PROOF.md, REVIEW_ADDENDUM.md, STABILITY_PROOF.md and AXIS_TAIL_PROOF.md; hydrostatic_cusp_128_audit/AXIS_TAIL_PROOF.md. This audit changes no candidate or theorem scope. The target full-plane IPM endpoint remains UNRESOLVED.
