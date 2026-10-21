# Independent audit of the completed L=16 trial

Date: 2026-10-20T20:00:42.928612+00:00. Input dnB_n96m40SL16.npz, MD5 bc8c82ca4baaf6c000a144284ff21bec, N=96, M=40, L=16, beta=0.9, c_l=5.583652796413529. Every density, derivative and inverse evaluation uses this lane's own code, with no numerics-lane evaluator imported. L is a radial compactification scale on the full plane.

The independent tensor reconstruction matches the supplied nodal data to 7.55e-15. The first radial node row is exactly one. Cubic normalization and density parity hold. At (1,0.5), the paired inverse velocity parity defects vanish to stored floating precision. The canonical velocity has U(0)=0; no harmonic strain is added.

On the same 58 physical points as L=4 and L=8, the 4096-angle inverse with radial Gauss order 28, log-panel width at most 0.08 and outer radius 1e30 gives max |R|/N_f=0.00892470774710 at (3.623577544766736,9.320390859672262). Here R=(c_l X+U).grad rho-rho and N_f=|rho|+sum_i |(c_l X_i+U_i) partial_i rho|. The corresponding L=4 and L=8 snapshots give 0.00382566619497 and 0.00548170121946. These are maxima on one fixed sample, not uniform estimates. Using N_v=|rho|+|X.grad rho|+|U.grad rho| gives a different sampled maximum, 0.00924335413671.

The independent axis zero is x*=8.589582468340156. Its change under inverse refinement is -2.68e-11. At the source, g=29.543881672226455 and h(P)-1=9.10852727e-7. At (x*,0.1) and (x*,1), |R|/N_f is respectively 8.39395295e-7 and 3.00627693e-4. The corresponding |E|/|rho_x| values are 6.93782888e-8 and 2.14565739e-7, using the smaller velocity differentiation step. Here E=-partial_x U_2+partial_y U_1-partial_x rho. The coarser step gives 6.95523955e-8 and 2.14535557e-7. Passing these two elliptic checks does not remove the transport defects elsewhere.

The maximum signed normalized transport effect from changing the density differentiation step is 1.697e-10. An independently implemented polynomial chain rule differs by at most 9.851e-11 in the same fixed-denominator test. At six fixed main-audit points, changing the inverse from 2048 to 4096 angles and refining its radial rule changes signed R/N_f by at most 3.919e-9. These are observed differences, not certified quadrature-error bounds over the 58-point sample.

The exact exterior bound |rho|<=2031616 r^(1/5), r>=1, gives an omitted velocity norm at most 5.079547904e-14 at every sample point. Propagation through the numerical gradient gives at most 2.286e-15 in R/N_f. This certifies only the infinite exterior contribution; the interior quadrature remains unvalidated.

Separately, the exact full-plane Bessel/Chebyshev moment formula in ../center-moment gives c=15.75095920992015115384516384566, with interval radius below 1.5e-39. The exact saved-parameter defect 3c_l-1-c is -8.20679564932298272380111436e-7 and excludes zero. The direct numerical angular moment gives the same displayed value. The certificate is for the ideal-node interpolant with exact binary input values, and its program remains subject to the requested independent code review.

Exact interval center tests exclude zero from the forbidden degree-five sine-7 coefficient, -9.9884980913702799784e-5, and from the transport balance determinant, 5.2840720559152377327e-9. Thus this fixed interpolant has no smooth center factor and cannot satisfy exact transport with the assumed C3 center velocity. These are necessary-condition exclusions for this represented field, not for a nearby or limiting profile.

Verdict: CONFIRMED for the finite numerical diagnostics, parity, normalization and canonical-gauge choice; REFUTED for a smooth center and exact transport of this fixed interpolant; OPEN for a smooth limit or another coupled branch. The three scales do not give residual convergence toward the endpoint tolerance. No endpoint is reached.

Evidence: dnB_n96m40SL16_summary.json records hashes of the five underlying completed JSON files. The exact center moment is in ../center-moment/verification/dnB_n96m40SL16_certificate.json. Code and proof are in this topic's code/ and PROOF.md.
