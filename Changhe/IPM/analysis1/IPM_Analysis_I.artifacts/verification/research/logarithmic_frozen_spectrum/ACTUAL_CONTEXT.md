# Exact literal audit excerpt

{
  "start_utc": "2026-10-22T03:21:58.941967+00:00",
  "utc": "2026-10-22T03:21:59.881118+00:00",
  "status": "PASS_GENERAL_SYMBOLIC_REDUCTION_AND_EXACT_PARAMETER_CASES_REQUIRES_INDEPENDENT_REVIEW",
  "proof_sha256": "14827c0b6cf6ca602e73a8ac5ed29cea56040a10d02fac37787c44e41d7c9ada",
  "code_sha256": "17fad05fadcf1e0889c31f1bf0d63dd3b8c507b7e5a3c3c300d5e56f12d23bf8",
  "parent_pin_count": 255,
  "parent_path": "research/forward_axis_weight_threshold/evidence/verdict.json",
  "parent_sha256": "6525af41c5435d37868b79a8a0dd1532129685225c7d1b2b17a82838c9a547b2",
  "symbolic_identities": {
    "full_fourier_chain": "0",
    "group_amplitude_derivative": "0",
    "group_amplitude_at_zero": "0",
    "kernel_ODE": "0",
    "adjoint_ODE": "0",
    "log_jacobian": "0",
    "potential_derivative": "0",
    "right_tail": "0",
    "left_tail": "0",
    "right_exponential_bound": "0",
    "left_exponential_bound": "0",
    "spectral_imaginary_gauge": "0",
    "actual_minus": "0",
    "actual_plus": "0"
  },
  "exact": {
    "k": "1615536043799051/9007199254740992",
    "A": "16398862465682933/1615536043799051",
    "D": "34413260975164917/1615536043799051",
    "b0": "10622735298540043/1615536043799051"
  },
  "cases": [
    {
      "a": "6",
      "s": "153/50",
      "d_minus": "-109015910092637641/1615536043799051",
      "d_plus": "-9766661864823671/4251410641576450",
      "classification": "forward",
      "inverse_norm": "4251410641576450/9766661864823671"
    },
    {
      "a": "-1",
      "s": "153/50",
      "d_minus": "5776127167142890/1615536043799051",
      "d_plus": "5554035287557376801/80776802189952550",
      "classification": "backward",
      "inverse_norm": "1615536043799051/5776127167142890"
    },
    {
      "a": "0",
      "s": "153/50",
      "d_minus": "-10622735298540043/1615536043799051",
      "d_plus": "4734092164273230151/80776802189952550",
      "classification": "interior_infinite_cokernel",
      "inverse_norm": null
    },
    {
      "a": "5/2",
      "s": "3/2",
      "d_minus": "-103239782925494751/3231072087598102",
      "d_plus": "0",
      "classification": "right_endpoint",
      "inverse_norm": null
    },
    {
      "a": "-10622735298540043/16398862465682933",
      "s": "0",
      "d_minus": "0",
      "d_plus": "0",
      "classification": "collapsed_endpoint",
      "inverse_norm": null
    }
  ],
  "scope": "Symbolic and exact scalar application; infinite-dimensional classification rests on standalone proof, not cases.",
  "check_sha256": "729c5e9912b35b6c8a5a8609c63eae07a4b172478f1a0f9eb1ab64d1c65300fd",
  "independent": {
    "start_utc": "2026-10-22T03:22:52.718658+00:00",
    "utc": "2026-10-22T03:22:52.858580+00:00",
    "status": "PASS_INDEPENDENT_GENERAL_POLYNOMIALS_DIRECT_FOURIER_ADJOINT_AND_EXACT_PARAMETERS",
    "code_sha256": "70fba0b4ada1546cf8edb07668aca9d9e8485cbdae3b17487294cc9192739bbd",
    "check_sha256": "729c5e9912b35b6c8a5a8609c63eae07a4b172478f1a0f9eb1ab64d1c65300fd",
    "parent_pin_count": 255,
    "universal_polynomial_identities": {
      "full_conjugation_numerator": "ZERO_POLYNOMIAL",
      "direct_weighted_adjoint_ODE": "ZERO_POLYNOMIAL",
      "kernel_zero_margin": "ZERO_POLYNOMIAL",
      "kernel_infinity_margin": "ZERO_POLYNOMIAL",
      "adjoint_zero_margin": "ZERO_POLYNOMIAL",
      "adjoint_infinity_margin": "ZERO_POLYNOMIAL",
      "potential_derivative_numerator": "ZERO_POLYNOMIAL",
      "right_tail_numerator": "ZERO_POLYNOMIAL",
      "left_tail_numerator": "ZERO_POLYNOMIAL",
      "right_tail_inequality_positive_remainder": "ZERO_POLYNOMIAL",
      "left_tail_inequality_positive_remainder": "ZERO_POLYNOMIAL",
      "spectral_phase_cancellation": "ZERO_POLYNOMIAL"
    },
    "independent_adjoint_method": "Original Fourier weighted adjoint and both endpoint power-integrability margins, separately from the unitary reduction. Infinite-dimensional realization remains analytic proof.",
    "exact_scalar_values_compared": 4,
    "exact_parameter_cases_checked": [
      "forward",
      "backward",
      "interior_infinite_cokernel",
      "right_endpoint",
      "collapsed_endpoint"
    ],
    "scope": "Exact identities and scalar examples do not by themselves prove any spectrum or PDE claim."
  }
}

The full check.json parent_files map is omitted solely to avoid repeating255 accepted source hashes. Both checkers freshly rehashed it. This excerpt is authenticated against the full JSON before finalization. Hash identity is not an independent proof.
