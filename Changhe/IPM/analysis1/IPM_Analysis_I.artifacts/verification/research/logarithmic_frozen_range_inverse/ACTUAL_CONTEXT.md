# Exact literal audit excerpt

{
  "start_utc": "2026-10-22T03:31:37.564387+00:00",
  "utc": "2026-10-22T03:31:38.135809+00:00",
  "status": "PASS_GENERAL_COERCIVE_IDENTITY_MELLIN_CONSTRAINT_AND_EXACT_MINIMA",
  "proof_sha256": "e4ac31efdbd4e846c5d4765033cb6b5a7b71e209458b4dcc9153742d6abf753d",
  "code_sha256": "79bc07116f1175e466bc3bb42418c51cfc0268eb3d0d80e3b553463795cb4732",
  "parent_pin_count": 275,
  "parent_path": "research/logarithmic_frozen_spectrum/evidence/verdict.json",
  "parent_sha256": "eda22fba890eeb985df010d272895e436f06460972cfec584ac576f85d7e664f",
  "symbolic_identities": {
    "coercive_quadratic": "0",
    "endpoint_left": "0",
    "endpoint_right": "0",
    "vertex_stationarity": "0",
    "vertex_value": "0",
    "completed_square": "0",
    "vertex_right_margin": "0",
    "potential_derivative": "0",
    "adjoint_integrating_factor": "0",
    "original_adjoint_scalar_and_exponents": "0",
    "weighted_pairing_cancels_sobolev_exponent": "0",
    "pairing_conjugates_phase": "0"
  },
  "actual": {
    "k": "1615536043799051/9007199254740992",
    "A": "16398862465682933/1615536043799051",
    "D": "34413260975164917/1615536043799051",
    "s": "153/50",
    "u": "10622735298540043/1615536043799051",
    "v": "4734092164273230151/80776802189952550",
    "inverse_norm": "1615536043799051/10622735298540043"
  },
  "inverse_strict_window": [
    "38020716849/250000000000",
    "152082867397/1000000000000"
  ],
  "cases": [
    {
      "name": "actual_a0",
      "u": "10622735298540043/1615536043799051",
      "v": "4734092164273230151/80776802189952550",
      "D": "34413260975164917/1615536043799051",
      "m": "112842505222848616481367274441849/2609956708813889231028868500601",
      "vertex_value": null,
      "sharp_inverse_norm": "1615536043799051/10622735298540043"
    },
    {
      "name": "concave",
      "u": "2",
      "v": "3",
      "D": "4",
      "m": "4",
      "vertex_value": null,
      "sharp_inverse_norm": "1/2"
    },
    {
      "name": "linear",
      "u": "3",
      "v": "5",
      "D": "4",
      "m": "9",
      "vertex_value": null,
      "sharp_inverse_norm": "1/3"
    },
    {
      "name": "convex_left_endpoint",
      "u": "1",
      "v": "10",
      "D": "4",
      "m": "1",
      "vertex_value": null,
      "sharp_inverse_norm": "1"
    },
    {
      "name": "vertex_boundary",
      "u": "4",
      "v": "7",
      "D": "4",
      "m": "16",
      "vertex_value": null,
      "sharp_inverse_norm": "1/4"
    },
    {
      "name": "interior_asymmetric",
      "u": "5",
      "v": "7",
      "D": "4",
      "m": "22",
      "vertex_value": "22",
      "sharp_inverse_norm": null
    },
    {
      "name": "interior_symmetric",
      "u": "8",
      "v": "8",
      "D": "4",
      "m": "32",
      "vertex_value": "32",
      "sharp_inverse_norm": null
    }
  ],
  "scope": "Exact finite identities and parameters; infinite-dimensional closed range and compatibility rely on standalone proof.",
  "check_sha256": "8e91d5f3d5aed3f523f54126bbdea2edabb738d7f4e0d3b3bf2debd3dfd66488",
  "independent": {
    "start_utc": "2026-10-22T03:32:13.311696+00:00",
    "utc": "2026-10-22T03:32:13.451169+00:00",
    "status": "PASS_INDEPENDENT_POLYNOMIALS_ORIGINAL_FOURIER_PAIRING_AND_MINIMA",
    "code_sha256": "444afd9e8e68b09b5e06a30b8992f76079555720ef9ac1750cd3e4cda3098a34",
    "check_sha256": "8e91d5f3d5aed3f523f54126bbdea2edabb738d7f4e0d3b3bf2debd3dfd66488",
    "parent_pin_count": 275,
    "universal_polynomial_identities": {
      "coercive_quadratic_from_square_plus_derivative": "ZERO_POLYNOMIAL",
      "completed_square_numerator": "ZERO_POLYNOMIAL",
      "vertex_complement_numerator": "ZERO_POLYNOMIAL",
      "original_eta_power_margin": "ZERO_POLYNOMIAL",
      "adjoint_zero_integrability_margin": "ZERO_POLYNOMIAL",
      "adjoint_infinity_integrability_margin": "ZERO_POLYNOMIAL",
      "full_original_adjoint_log_eta_coefficient": "ZERO_POLYNOMIAL",
      "full_original_adjoint_log_B_coefficient": "ZERO_POLYNOMIAL",
      "full_original_adjoint_log_weight_coefficient": "ZERO_POLYNOMIAL"
    },
    "separate_integer_pairing_coefficients_checked": true,
    "exact_values_compared": 7,
    "inverse_strict_window": [
      "38020716849/250000000000",
      "152082867397/1000000000000"
    ],
    "independent_minimum_cases": [
      "actual_a0",
      "concave",
      "linear",
      "convex_left_endpoint",
      "vertex_boundary",
      "interior_asymmetric",
      "interior_symmetric"
    ],
    "scope": "Different polynomial implementation and direct weighted-adjoint method; analytic domain/range/projection still requires proof and review."
  }
}

The full275 inherited parent hash entries are omitted from this excerpt only. Both checkers freshly rehash them. The finalizer must authenticate the excerpt against the complete JSON. Hashes establish byte identity, not analytic truth.
