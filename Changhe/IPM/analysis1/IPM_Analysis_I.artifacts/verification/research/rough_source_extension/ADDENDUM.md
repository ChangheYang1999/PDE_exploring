# Review clarifications and the full order-family dependency

The actual Opus5.5 review completed2026-10-21T04:06:35.496042+00:00,
request391bdd6f-7594-47c7-9f47-2ecf7e3d4258. It accepted the reconstructed
proof, rejected the specified lead r3 continuity assertions, and requested
these qualifications. They are part of the result.

In PROOF section3, the auxiliary theorem permits every P in R2, including
P=0. Only the local sections require P=(p,0), p>0 and separation from the
origin. Every step of the auxiliary proof uses D(X-P) through its constant
divergence, linear growth, or the earlier translation-invariant Fourier
energy. The additive constant -DP has purely imaginary Fourier symbol and
commutes with J^s. Thus all constants and the proof hold for arbitrary P.
The conjugated auxiliary operator in section7 legitimately uses P=0.

When applying the auxiliary theorem to the local coefficients, their common
regularity can be taken as sigma_* = min(sigma,4). A compact C4 function is
in H4; multiplying W by fixed smooth cutoffs preserves Hsigma. Therefore
both w=theta(V-Dz) and q=theta(grad rho-(0,g)) are compact H^(sigma_*), with
sigma_*>=s and sigma_*>3. No Hsigma assertion for the C4 background is
needed when sigma>4. The local approximation itself only uses the indicated
norms of the differences and fixed compact C4 background terms.

The request bundle supplied the complete source_order_family/PROOF.md and
ADDENDUM.md, not excerpts. Nevertheless the review reported that it had
only checked excerpted text. The verifier reread the entire order-family
proof. Its frozen margin is the minimum of two affine expressions on the
parameter box; the fast-minus-slow minimum is601/1000. Its commutators
need s>=3 and t=s-1>2, its remote H4 bounds need s<4, and its off-diagonal
heat representation needs2<s<4. All hold throughout[61/20,31/10]. Its
section Local estimate and normalization explicitly checks every part of
topic77 sections5-7 at variable s. Constant divergence occurs only in the
separate displayed bound on E_s, not in the local identities with the actual
E_s or in the auxiliary inverse. The leading commutator has norm Hs->L2,
as its mandatory ADDENDUM states. The new follow-up review is given the
complete order-family proof, both addenda and the canonical sign proof80.
The corresponding finalized verdict manifests are checked as dependencies.

For the K1 consequence at3.06, all source-location, diagonal source-jet,
parameter-box, constant-divergence and Hessian-budget hypotheses remain.
Equation(18) bounds the whole Hessian only for a correction in global Hs.
Weighted far-field spaces have no new completion theorem here. In the
operator L u+W[h].grad u, h determines the velocity and u is the function
being estimated; rho is the fixed smooth background. Section6 concerns
u with zero origin jets and local Hs forcing for this fixed velocity.
No uniform bounds for K2,K3,K4 over h, no rough-coefficient semigroup and
no physical inverse are asserted.

The counterexample refutes the stated intermediate claims N(h_eps)<infinity
and N(g)->0 in lead r3. The finally jet-corrected test function there can
have finite N. The repaired theorem is valid because N is applied to the
zero-jet difference only, with its second term included.
