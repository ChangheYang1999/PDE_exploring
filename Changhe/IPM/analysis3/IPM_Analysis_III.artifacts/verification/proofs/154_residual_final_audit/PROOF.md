# A full-plane certificate for the exact modal residual

## Exact statement

Let rho_bar be the exact normalized C6-joined case1 modal trial constructed in topics4 and15 from the binary-rational entries of the original file

 source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz,

whose SHA-256 is a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874. The scalar normalization is the uniquely specified correction of proof 4, enforcing 3 ell-c[rho_bar]=1; ell=1/k and k=1615536043799051/9007199254740992. Use the canonical full-plane velocity U=(-R_1R_2,R_1^2) and define

 F=-rho_bar+ell X.grad rho_bar+U[rho_bar].grad rho_bar.

Put t=log r, p(X)=x^2y and E gamma=p(X)gamma(t). Define

 w(X)=|x|^(-17/2) max(1,|X|)^(29/4),
 g(t)=exp(-t/2) for t<0, and exp(27t/4) for t>=0,
 G=L2(R,g(t)dt), R=L2_P(R^2,w(X)dX), Y=E G direct-sum R.

P denotes even-x, odd-y parity. The norm on Y is ||E gamma+h||Y^2=||gamma||G^2+||h||R^2. The splitting is unique for the finite angular class here. Then

                   6049.11 < ||F||Y < 8601.42.          (1)

Both decimal bounds in (1) are exact rational numbers. This is a certificate for the stated normalized modal trial and norm. It does not describe the raw unnormalized X3 table, an unknown exact solution, or a high Sobolev residual norm.

## Reduction to a finite interval and two tails

Proof 98 proves the exact angular identity. On each radius write

 F/r^3=cos(theta)^2 sin(theta)[gamma(t)+cos(theta)^2 Q(t,theta)].

The angular target norm squared is

 N(F/r^3)^2=gamma(t)^2+M H(Q), M=2 Beta(1/4,3/2),

where H is the exact probability Gram form with the rational moments in proof 98. Hence ||F||Y^2=int g(t)N(F/r^3)^2 dt. All sine indices through522 are retained, including zero padding; there is no angular truncation or sampled angular quadrature in this certificate.

The finite interval [-40,20] is partitioned at every nonempty exact original spline span and at0, with the endpoint subdivisions specified in topics127 and134. There are1757 base intervals. Adaptive bisection produces1860 accepted leaves:176 on the inner analytic branch,1559 on spline spans, and125 on the outer branch. Each leaf lies in a single analytic formula and on one side of0.

For a leaf, proof 134 constructs a degree28 radial Taylor polynomial using the exact Green differential equations. The older first155 leaves retain the valid exponential-polynomial method of proof 127, with their original timestamps and complete migration hashes. Both methods enclose the identical trial. The first angular division is structural; the second is the exact axis subtraction and polynomial quotient. The triangle and reverse triangle inequalities in the angular Hilbert norm give lower and upper bounds throughout the whole leaf. Multiplication by the exact positive integral of g gives directed energy bounds. Their validity follows from the proofs in topics127 and134, whose algorithms and code were independently checked during this run.

The inner tail (-infinity,-40] uses the exact cubic residual cancellation before bounding the positive exponential powers, as proved in proof 127. The outer tail [20,infinity) is the independently checked full Y tail of proof 122, including its axis component. Every term is nonnegative, so lower and upper bounds add without conditional convergence issues.

## Independent audit and exact arithmetic

The checker code/audit.py reloads the read-only original, reconstructs the base partition independently of the integrator, and verifies its exact agreement with the production metadata. It validates the source, scalar, Green-cache, code, proof and outer-tail hashes. It checks both generations of migrated journals record for record.

For every leaf it checks the dyadic identifier, exact rational endpoints, unique index, depth, analytic branch, knot containment, the split at0, positive energy bounds, acceptance rule, and successful center and velocity-derivative comparisons. Sorting exact rational endpoints proves gap-free, overlap-free coverage from-40 to20. There are3720 independently reconstructed norm-to-energy arithmetic checks. Finally the checker independently sums the saved exact outward rational endpoints, including both tails, and checks the reported square roots.

Thirteen leaves, selected near both endpoints, interior knots, the source region, the large-residual region and the outer branch, were recomputed at640 bits with degree36. Their center norms and energy intervals agree with the production enclosures. The proof of all leaves is the checked interval algorithm; these replays are additional independent consistency tests, not a statistical substitute for full coverage.

The inner upper bound was independently recomputed at640 bits. The two directed upper estimates differ by less than10^(-140), and need not have overlapping rounding balls: each is an upper estimate, rather than an enclosure of a common exact supremum. The first replay checker incorrectly required overlap, and its successor required a monotonicity between precisions which also need not hold. Those failed checks and their logs are retained. The finalizer correctly retains the larger exact upper endpoint and increases the total upper energy by their nonnegative difference. No production record was changed.

The final certificate in evidence/final_certificate.json gives the exact rational lower and upper energies and the hashes of all three audit inputs. The pure rational finalizer verifies

 (604911/100)^2 < E_lower <= ||F||Y^2
                   <= E_upper < (860142/100)^2.

This proves (1). Its calculation uses integer arithmetic and Fraction arithmetic only. The journal hash is e55db223ddf33de34546465e17ad8a3eacfa13509916d958987d94612c6c9f4b and the production metadata hash is f151f44f1a1d82abd1aa9477f8d5c7d24ea17e20fa367c85299914998f25bfd7.

## Evidence and reproduction

The production journal and metadata are in ../134_residual_green_taylor/evidence/production_28. This topic contains:

- code/audit.py and evidence/journal_audit.json: provenance, exact partition and sum checks;
- evidence/replay.json: all thirteen successful640-bit, degree36 leaf replays;
- code/inner_replay.py and evidence/inner_replay.json: independently computed inner-tail upper bound and the retained failed monotonicity check;
- code/finalize.py and evidence/final_certificate.json: exact rational maximum of the two tail upper bounds and the final strict decimal inequalities;
- the original diagnostic logs, including the reporting conversion error corrected before the journal audit completed.

The original integrator, the Green ODE proof, exact angular norm, central normalization and analytic outer tail are dependencies, not unchecked numerical assumptions. Their exact sources and hashes are recorded in the production metadata and audit. No formal proof-assistant build was used.

## Scope

This completes a residual-norm certificate in Y. Its interval is deliberately conservative because radial coefficient norms were used to enclose each leaf. It confirms that the residual is not small in this particular low strong norm. It supplies no lower bound for a nonlinear correction, no inverse norm, no finite-section complement, no high Sobolev residual norm, and no existence or nonexistence theorem for the IPM profile.
