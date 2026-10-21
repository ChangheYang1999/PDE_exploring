# Fifth-resolution field verification

Observed acceptance: 2026-10-21T00:16:50.584420+00:00. Verdict: CONFIRMED for the finite diagnostics and exact fixed-field exclusions below. YES_inf and NO_inf remain OPEN.

## Data and method

The published108x44 state is frozen byte-for-byte in data/dnB_n108m44S.npz, SHA2565e206e31ba980c3b43d597456b8f3e2ff77b2859c86edc8766b31d0dbbd15bc2, MD5306dbedbf3d5f31045a4de1e4c28e028. Its parameters are L=8, beta=0.9 and c_l=5.575189191804838. L is a compactification scale, not a physical box boundary. This lane used its own barycentric field reconstruction, Cartesian eighth-order differences, analytic-gradient comparison, and separately implemented angular/radial whole-plane inverse. No numerical-lane code was imported. The prepared proof/protocol is PROOF.md, SHA256431926a219392fc954c093ab8d5efd208ea0bd5c7b4ac86b2fda198be05cc252.

The pipeline completed at2026-10-21T00:12:28.280974+00:00. All20 prepared source pins match the completion record and current bytes. The later independent acceptance program reconstructed74 transport rows and4 elliptic checks using rational arithmetic on saved binary components, checked208 conditions, and obtained PASS. Its maximum scalar rounding difference is4.547473508864641e-13. This rational audit validates component arithmetic, not the exact physical inverse values. The manual program was added after completion and is pinned separately. No historical direct-import or process-environment attestation is invented.

## Recomputed results

With R=(c_l X+U) dot grad rho-rho, N_f=|rho|+sum_i |(c_l X_i+U_i) partial_i rho| and N_v=|rho|+|X dot grad rho|+|U dot grad rho|, the58point maximum |R|/N_f is0.0025261349397718218 at(2.898862035813389,7.45631268773781). The exact saved-component audit gives0.0025261349397719996, consistent with scalar rounding. The maximum |R|/N_v is0.003877478019096504 and maximum |R| is0.8327323743550608. These are finite sample maxima. The8additional points have maximum |R|/N_f0.0028250449638228137.

The root found in the prescribed bracket[8,9] is x*=8.576668173142153. It is not certified as the first or unique positive root. At(x*,0.1) and(x*,1), |R|/N_f equals2.394100516468261e-6 and5.194756404619478e-5. The respective elliptic residuals, normalized by the sum of absolute signed equation components, are6.380912462230253e-8 and2.139670805715819e-8 at Cartesian step0.0025. Step0.005 gives consistent values. The source Jacobian has w'=10.150376712170956 and h_P=1.0000016716298212, with divergence1.9110224513951835e-10.

The origin velocity is(0,0). Density reflection defects vanish at the checked points; velocity reflection defects are at most1.7763568394002505e-15. The normalization row consists exactly of ones. Nodal reconstruction error is1.9539925233402755e-13. These observations validate the represented symmetry and normalization, not a new global solution.

Changing2048angles/order24/panel0.1 to4096angles/order28/panel0.08 changes normalized R at the6fixed inverse-comparison points by at most3.934566884483509e-9. This is a combined angular/radial sensitivity. The58point maximum gradient-step and chain-rule effects are2.531292172104627e-10 and2.0441269786327445e-10. None is a certified bound on interior quadrature error. The separately proved exterior estimate gives max U-tail4.769756928e-14 beyond10^30; propagation through the computed gradients gives max normalized R-tail2.1463579813577606e-15. The exact center-strain tail bound is1863/390625000000000000000.

## Exact center exclusions and scope

Two independently implemented Arb center integrals give overlapping enclosures for 3c_l-1-psi_xy(0). Both exclude zero, with defect approximately-6.26417130098318052529726964594480178759233024e-7. The first ball has radius4.20e-57 and the second2.65e-52 in their recorded decimal displays. The canonical whole-plane law leaves no freely adjustable harmonic strain to repair this fixed-field defect.

The coefficient of r^5 sin(7theta) is[0.000193523216232982235140741280331593438884507449 +/-1.03e-50]. It excludes C^5 regularity of the fixed ideal-node binary interpolant. The induced x^5 log(x) axis coefficient is three times this value and is also nonzero. The exact transport-balance determinant is[-2.73195279526462683564672283776548005948482087e-7 +/-2.19e-52], giving the previously proved fixed-field transport obstruction. The analytic proofs and hypotheses are the center-regularity and center-moment topics referenced by PROOF.md.

No reliable B_3,B_5,B_7 measurement for a genuine coupled profile follows from these nonsmooth finite interpolants. The field fails the candidate evidentiary standard. No conclusion excluding another field, a smooth limiting profile, the full admissible class, or a nonlinear family follows. These results change neither task endpoint.

## Verification files

- verification/dnB_n108m44S_summary.json: SHA2563bc313edd64dd950ec87b6ea9285ac9f8212f33ee6bcb92a15575a58f2cadcf5.
- verification/manual_acceptance.json: SHA2561208fae7864b3fed776fb7097ede13bfd2468de4f0d9f6ac206853453b32e601.
- code/manual_acceptance.py: SHA2568d400e0aa4e6a29e6255b97aa6b7f74db3869e460219edf4d52faed24690378d.
- verification/completion.json: SHA2563fbc89ac0bbcb034fbcb7a1973afc3137908f05d7083569e84b9178c9d1bac63.
- verification/runtime_observed_0010.json records the actual live environment observation at00:09:18, scoped to that observation.

Full row data, exact JSON inputs, both center certificates, source pins and independent scalar checks are alongside these files.
