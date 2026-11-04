# Literal executed weak-axis audit excerpt

{
  "start_utc": "2026-10-22T04:24:30.539694+00:00",
  "utc": "2026-10-22T04:24:34.075849+00:00",
  "status": "PASS_WEAK_AXIS_EXACT_MODAL_HYPOTHESES_AND_FACTOR_IDENTITIES",
  "proof_sha256": "0a812be3f4653b8d124d0483e616f055131296204e0acf3613d93fbbca1454dd",
  "code_sha256": "d6192a61a8d4dd87df42adb211dde48bcc4423139770d84c7e1fcc46e24ba485",
  "parent_pin_count": 1845,
  "actual": {
    "k": "1615536043799051/9007199254740992",
    "bi": "3518437208883275/70368744177664",
    "bo": "2210212141903103/17592186044416",
    "s": "153/50",
    "theta": "3/50",
    "center_rate_infimum": "11/25",
    "far_rate_minimum": "25406061720423925/9007199254740992",
    "inner_factor_gap": "3377699720527947/70368744177664",
    "outer_correction_gap": "1106222554933964811/9007199254740992"
  },
  "degree": 7,
  "modes": 260,
  "knots_checked": 1573,
  "distinct_knots": 1559,
  "outer_exponents": [
    "-25406061720423925/9007199254740992",
    "-16398862465682933/4503599627370496",
    "-40189388142307807/9007199254740992",
    "-11895262838312437/2251799813685248",
    "-54972714564191689/9007199254740992",
    "-31182188887566815/4503599627370496",
    "-43420460229905909/9007199254740992",
    "-25406061720423925/4503599627370496",
    "-58203786651789791/9007199254740992",
    "-61434858739387893/9007199254740992"
  ],
  "shapes": {
    "S": [
      260,
      1565
    ],
    "D": [
      260,
      7
    ],
    "Aout": [
      260,
      10
    ],
    "Ei": [
      260,
      7
    ],
    "Eo": [
      260,
      7
    ]
  },
  "symbolic_identities": {
    "exact_global_x2y_factor": "0",
    "weighted_Euler_factor_p0_q0": "0",
    "weighted_Euler_factor_p0_q1": "0",
    "weighted_Euler_factor_p0_q2": "0",
    "weighted_Euler_factor_p0_q3": "0",
    "weighted_Euler_factor_p0_q4": "0",
    "weighted_Euler_factor_p1_q0": "0",
    "weighted_Euler_factor_p1_q1": "0",
    "weighted_Euler_factor_p1_q2": "0",
    "weighted_Euler_factor_p1_q3": "0",
    "weighted_Euler_factor_p2_q0": "0",
    "weighted_Euler_factor_p2_q1": "0",
    "weighted_Euler_factor_p2_q2": "0",
    "weighted_Euler_factor_p3_q0": "0",
    "weighted_Euler_factor_p3_q1": "0",
    "weighted_Euler_factor_p4_q0": "0",
    "logarithmic_weight_conjugation": "0",
    "center_L2_exponent": "0",
    "far_L2_exponent": "0",
    "fractional_interpolation_exponent": "0"
  },
  "arb256": {
    "far_rate_minimum": {
      "lower_exact": "25406061720423925/9007199254740992",
      "upper_exact": "25406061720423925/9007199254740992"
    },
    "inner_factor_gap": {
      "lower_exact": "3377699720527947/70368744177664",
      "upper_exact": "3377699720527947/70368744177664"
    },
    "outer_correction_gap": {
      "lower_exact": "1106222554933964811/9007199254740992",
      "upper_exact": "1106222554933964811/9007199254740992"
    }
  },
  "strict_windows": {
    "far_rate_minimum": [
      "1410319734353/500000000000",
      "2820639468707/1000000000000"
    ],
    "inner_factor_gap": [
      "48000000000001/1000000000000",
      "24000000000001/500000000000"
    ],
    "outer_correction_gap": [
      "24563075016947/200000000000",
      "1918990235699/15625000000"
    ]
  },
  "scope": "Qualitative compact-test membership only. Finite checks verify actual exponents and algebra, not Sobolev convergence, canonical harmonic estimates or any physical norm.",
  "check_sha256": "d875bdcdc6ae69f524e4de974a40226e460622e37d17917d4c98847e5beb59be",
  "independent": {
    "start_utc": "2026-10-22T04:25:36.222468+00:00",
    "utc": "2026-10-22T04:25:39.226814+00:00",
    "status": "PASS_INDEPENDENT_HEX_FMPQ_IV_AND_NORMAL_ORDER_ALGEBRA",
    "proof_sha256": "0a812be3f4653b8d124d0483e616f055131296204e0acf3613d93fbbca1454dd",
    "code_sha256": "af2c319dc2e2b895d0b05a7d9973b30e2af64593dea0d716da4677341b51935d",
    "check_sha256": "d875bdcdc6ae69f524e4de974a40226e460622e37d17917d4c98847e5beb59be",
    "parent_pin_count": 1845,
    "exact_values_compared": 9,
    "outer_exponents_compared": 10,
    "knots_compared": 1573,
    "differential_ring_checks": 16,
    "iv100": {
      "far_rate_minimum": {
        "lower_exact": "25406061720423925/9007199254740992",
        "upper_exact": "25406061720423925/9007199254740992"
      },
      "inner_factor_gap": {
        "lower_exact": "3377699720527947/70368744177664",
        "upper_exact": "3377699720527947/70368744177664"
      },
      "outer_correction_gap": {
        "lower_exact": "1106222554933964811/9007199254740992",
        "upper_exact": "1106222554933964811/9007199254740992"
      }
    },
    "strict_windows": {
      "far_rate_minimum": [
        "1410319734353/500000000000",
        "2820639468707/1000000000000"
      ],
      "inner_factor_gap": [
        "48000000000001/1000000000000",
        "24000000000001/500000000000"
      ],
      "outer_correction_gap": [
        "24563075016947/200000000000",
        "1918990235699/15625000000"
      ]
    },
    "scope": "Separate data decoding, arithmetic engine and finite differential algebra. Harmonic convergence, shell geometry and Sobolev membership remain analytic proof obligations, not finite-test conclusions."
  },
  "independent_sha256": "26970cde00cade9f00644cd5de38ef2e0673839be0a0b3164d25418541760634"
}

All1845 inherited pins remain in check.json. The numerical intervals here happen to be exact singletons, because their dyadic expressions fit the chosen arithmetic precision. The three decimal windows are strictly outward. No physical norm is computed.
