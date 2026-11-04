# Repaired report: precise statements and transferred proofs

## 1. Statement and frozen sources

The claim checked here is that the mathematical changes in the coordinator's Note 110 preserve the independently confirmed results, with the three specified corrections. The frozen report is this report, captured at 2026-11-03T19:55:38.221642+00:00, SHA256 d0d9f21ab2cecfe7c833a00234906e4823789070683be98ea42f105d7873f4f2. The preceding c8963e47 report and its complete delta are retained. The source manifest also pins the companion files. in the team records and THEOREM_ATTEMPTS.md have not changed since that preceding pin. A pin alone does not establish that every companion file was freshly read.

The exact fresh assembly scope is the front matter, Sections 0-10 and Appendix A. Appendix B remains a historical record whose individual entries retain only the scopes of their cited verdicts. Appendix C is revision history. Appendix D's file map was read. The separate complete-coverage proof records how every line in the fresh scope was covered. This is an audit of the stated results, including conditional results and open steps; it is not a proof of the campaign's unrestricted conjecture.

## 2. Formal Lyapunov normalization

Theorem 3(g) now quantifies over C1 functions of (y,U,DU,P) whose derivative along B is nonpositive at every admissible formal second jet. At omega=0 it uses

    H_0 = H - c(1-2c)|y|^2/2,

not the unshifted rotating Bernoulli quantity H. This is exactly the classification proved in A2178: a nondecreasing function of H_0 in the nonrotating case, and a constant function when omega is nonzero. The proof first uses the surjective free second-jet map to eliminate dependence on DU; free first derivatives then give the gradient constraint, and the nonzero-omega bracket eliminates the remaining dependence. All hypotheses are formal-jet hypotheses; the statement does not infer the same classification merely by restricting to the jets realized by unknown global profiles.

The corrected table also uses H_0 in the first-, second- and higher-order classification rows. The higher-order entries retain their earlier source and verdict scopes; this repair does not freshly prove a stronger higher-order theorem. The selected historical Appendix B occurrences are repaired in the same way. The underscore distinguishes this scalar from the report's regularity tag H0. The A2177 countertest to unshifted H therefore no longer applies to the repaired statement.

## 3. Decay in rotation-rate uniqueness and the linear kernel

The corrected Appendix A row explicitly assumes H0,H1 and speaks of a nonzero decaying profile and the decaying linear kernel. This matches A2202. For a common decaying full profile at two different rates, subtraction yields L U = grad q, with L U = (Jy).grad U - JU. This vector is both curl-free and divergence-free. Its harmonic mean value formula, with the angular derivative integrated by parts, forces L U=0 from decay. The profile is then axisymmetric and the verified ordinary Liouville result applies. The linear assertion follows by transporting curl V backward along the spiral carrier and then using harmonicity and decay of V.

Decay is essential in both arguments. The countertest U=e3, P=-(1-c)x3 from A2201 is excluded by H1. The table's range 0<c<1/2 is within the verified linear range c>0. No uniqueness claim for arbitrary nondecaying profiles is inserted.

## 4. Finite-jet pressure means and the normalized ratio

The repaired LIT261 row distinguishes two statements. Here m>=1, v is C^m near zero, P is continuous, div v=0 and div div(v tensor v+P I)=0 distributionally. The first nonzero homogeneous Taylor term V_m has degree m. Brackets denote normalized averages on the unit sphere; K=<|V_m(theta)|^2> is positive and N=<(V_m(theta).theta)^2>. The ratio of spherical means of P(0)-P and |v|^2 has the exact finite-jet limit

    ((2m+3)N-K)/(2mK) <= 1/2.

This statement is invariant under constant pressure changes. The consequence for R=|v|^2/H explicitly requires P(0)=0, H=|v|^2/2-P>=0 and v=0 on {H=0}. The limsup is taken on {H>0}. Under those hypotheses, a bound R<=r<1 near a nontrivial finite-order zero would imply -P>=(1/r-1/2)|v|^2 throughout a small ball. The coefficient exceeds 1/2, contradicting the exact ratio of means. This is the complete normalization argument of A2204; the local stationary countertest with P(0)=-1 is excluded.

The Section 10 tail version is equivalent. There P2(0)=0 and S<=0, with S=P2-|V|^2/2 and V=0 on {S=0}. Hence H=-S=|V|^2/2-P2 and R=|V|^2/|S|. The finite-jet, divergence and pressure-stress hypotheses are inherited from the stated tail setting. No pressure normalization is inferred solely from its Poisson equation.

## 5. General axial finite-order obstruction

The new Section 10 paragraph and Appendix A row combine LIT290 and LIT291, already confirmed in A2180-A2186 and A2194-A2199. For 2/5<c<1/2 and omega!=0, consider a smooth exact finite-order velocity zero of order N>=2 at a nonzero point on the rotation axis. Require positive pressure scalar, all the leading equations and the full C1 next-pressure scalar. LIT291 forces zero transverse pressure gradient; LIT290 excludes that remaining case. Thus all pressure data at such an axial zero are excluded. This is stronger than the earlier exclusion of one specified Cauchy-data family, and the text keeps the two results distinct.

The actual-profile application retains global zero helicity, both natural bounds, a supported zero in a smooth open k=0,S>0 region, and the nonresonant or averaged next-scalar construction. In particular c=3/7 is covered by the already verified averaged construction. Supportedness and the actual pointwise law supply finite order at least two. The paragraph explicitly leaves off-axis zeros, S=0 and boundary points unresolved. The later LIT292 carrier-critical off-axis result is not part of this frozen report and is not silently included in its approval.

The companion obstruction-ledger delta describes the same actual-tail setting. Its short phrase "every finite-order axial zero" is read in that preceding supported smooth-tail context, where N>=2 is forced. For standalone quotation the coordinator should repeat N>=2 and the full next-scalar premise. This compression does not supply an additional theorem or remove the contextual hypotheses.

## 6. Exact foundation transfer and verdict boundary

The independently read Sections 2A, 2B, 2C and 2D are byte-identical to the corresponding c8963e47 blocks. Their 483, 679, 1069 and 1005 split lines, respectively, have the hashes recorded in the complete-coverage certificate. Thus the energy audit A2148-A2152, dynamical audit A2142-A2146, smooth basin audit A2040-A2043 with A2062, and helicity-sign audit A2072-A2076 transfer without a mathematical delta. The current comparison took 0.19841334968805313 actual seconds. It is file-comparison evidence, not numerical evidence for any theorem.

All six sections of this independent proof and the entire mathematical report delta were read. The three precision repairs, combined axial insertion and foundation transfer are CONFIRMED at the exact scopes above. Fresh approval of the historical appendices as a whole, a new blanket approval of every companion file, and unrestricted rotating nonexistence do not follow.
