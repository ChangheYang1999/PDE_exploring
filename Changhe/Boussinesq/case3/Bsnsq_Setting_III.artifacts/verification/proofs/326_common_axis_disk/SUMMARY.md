# P326: a common axis disk for every formal coefficient

Checked 2026-10-22T09:02:50.011456+00:00. Full standalone proof in PROOF.md SHA256b5fcfa12c928e89b97618897c09826a16aeed784b182bc91601395aab0908637. This is a strengthening of P321's domain statement, conditional on its exact residue identities and baseP303/P306.

For real Ck nonzero, B=s+ks^2-(Ck/260)s^13 and H=-k^7/231, all coefficients of the unique compatible formal x series extend holomorphically to the same disk

    |s| < min(1,1/(4|k|),(65/|Ck|)^(1/12)).

On that disk B/s is within1/2of1, the homogeneous cofactors have no zeros, and every zero-residue scalar primitive extends on the entire disk. Derivatives, finite products and Poisson updates preserve this open domain at every finite stage. No estimate uniform in the coefficient index is supplied.

| Item | Method and result | Verdict |
|---|---|---|
| Common disk | Explicit nonvanishing bound and scalar meromorphic continuation lemma, followed by exact hierarchy induction. | CONFIRMED |
| Uniqueness | Nonsingular compatibility matrix fixes each pair; changing initial particular solutions only translates affine coordinates. | CONFIRMED |
| Supplementary controls | 88/88: exact regular-factor identities,18manufactured scalar equations with reconstruction and nonzero-residue negative cases, exactradiusbounds. | CONFIRMED |
| Growth with index, convergence in x, actual local PDE solution | No bound or convergence theorem. | OPEN |
| Global inverse, moving-center attachment, full-plane B2 endpoint | Not constructed. | OPEN |

Controls ran 2026-10-22T09:01:26.316740+00:00 to2026-10-22T09:01:30.524721+00:00, 4.207977914s, codeSHA256503693332c21493aed4b9b23bbb73e4734802844eb86a183318e469bb7507295. Opus560 gave no audit text; actualOpus561/562 completed a full proof and normalization exchange. See verification/model_adjudication.md for limitations and corrections. A common analytic domain for coefficients alone does not imply a convergent x series, as the constant coefficients n! illustrate. General B2 remains OPEN and T_end is unset.
