# Scope of leading-sector tail norm formulas

## Exact formulas for a pure exterior power

Let E(theta) be a nonzero square-integrable angular profile with full-circle norm A. For F(r,theta)=r^e E(theta) on r>R, direct polar integration gives

||F||_(L2(r>R)) = A R^(e+1)/sqrt(-2e-2), if e<-1,
||rF||_(L2(r>R)) = A R^(e+2)/sqrt(-2e-4), if e<-2.

At the endpoint exponent the corresponding integral diverges logarithmically. These formulas are equalities for the stated pure power, not lower bounds for a field whose asymptotic expansion begins with that power.

## Counterexample to an unconditional leading-sector lower bound

Fix e<-2 and R>0. Choose a smooth radial function eta supported in r>1, equal to1 for r>=2, and taking values in [0,1]. For each L>R define

F_L(r,theta)=eta(r/L) r^e E(theta).

For instance, take E(theta)=sin(theta), so each field extends smoothly through the origin and has S1 parity. Every F_L equals r^e E(theta) for r>=2L, hence has exactly the same nonzero leading asymptotic coefficient. However,

||F_L||_(L2(r>R))^2 <= A^2 L^(2e+2)/(-2e-2),
||rF_L||_(L2(r>R))^2 <= A^2 L^(2e+4)/(-2e-4),

and both right sides tend to zero as L tends to infinity. Therefore the leading asymptotic coefficient alone supplies no positive norm lower bound at the fixed radius R. The same conclusion for the unweighted L2 norm holds for every e<-1. It is not changed by knowing an asymptotic expansion with exact coefficients but no quantitative remainder bound at R.

The example disproves the general inference from asymptotics to a fixed-radius lower bound. It need not belong to a particular finite generator family or arise as an IPM residual. A theorem restricted to such a family requires additional information about that family. The finite-family result in ../l2_family_floor/PROOF.md supplies such information by an exact finite-dimensional distance, without assuming an onset radius.

## Valid ways to obtain a lower bound

If F=F0+G on r>R, the reverse triangle inequality gives

||F|| >= ||F0||-||G||,

in either weighted or unweighted L2, provided the terms are finite. Thus a pure-tail formula and a certified upper bound for the complete remainder yield a valid lower bound. Alternatively, exact full-polynomial antiderivatives or a separately proved dual test provide a direct norm bound. Dropping signed cross terms between asymptotic sectors is not valid.

## What a finite root screen proves

A finite list of formal-series coefficients cannot prove convergence, divergence, or the radius of convergence of the infinite series. Any prescribed finite prefix admits a continuation with every later coefficient zero, a continuation with geometric growth at an arbitrary rate, or one with factorial growth. A numerical root screen on the prefix is a heuristic for choosing trial radii. It does not justify a statement that the full series converges only beyond a specified radius.

## Scope of this audit

The target is section3 and related conclusions in the immutable numerical_results/numerics_v01.md, frozen in source/numerics_v01.md. Its exact leading-sector coefficients and separately validated candidate norms remain useful. This audit rejects only the unsupported lower-bound and convergence inferences, and separately checks the arithmetic of the displayed pure-power examples. It does not refute a candidate-specific bound established by complete integration or a finite-family theorem.
