# Actual completed premise and algebra checks

{
  "start_utc": "2026-10-22T04:52:17.637866+00:00",
  "utc": "2026-10-22T04:52:22.314963+00:00",
  "status": "PASS_HIGHER_ORDER_MODAL_PREMISES_AND_SYMBOLIC_FACTOR_IDENTITIES",
  "proof_sha256": "0dcddf0f8356c434242ffc63986a74079e578d70acb7c32acc76975018730f4f",
  "code_sha256": "18b2454c4ebf51d6472cd2f7ea6d37b58acdfd14f294ec33674eed0b68c6d4b0",
  "parent_pin_count": 1922,
  "actual": {
    "k": "1615536043799051/9007199254740992",
    "bi": "3518437208883275/70368744177664",
    "bo": "2210212141903103/17592186044416",
    "spline_degree": "7",
    "matched_derivative_order": "6",
    "weak_a_order": "7",
    "weak_g_order": "6",
    "max_uniform_s": "7/2",
    "axis_limit": "5/2",
    "center_base": "6",
    "far_margin_at_b0": "25406061720423925/9007199254740992",
    "inner_gap": "3377699720527947/70368744177664",
    "outer_log_gap": "1106222554933964811/9007199254740992"
  },
  "knots_checked": 1573,
  "distinct_knots": 1559,
  "modes": 260,
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
  "symbolic_identities": {
    "x2y_factor": "0",
    "factor_p0_q0": "0",
    "factor_p0_q1": "0",
    "factor_p0_q2": "0",
    "factor_p0_q3": "0",
    "factor_p0_q4": "0",
    "factor_p0_q5": "0",
    "factor_p0_q6": "0",
    "factor_p1_q0": "0",
    "factor_p1_q1": "0",
    "factor_p1_q2": "0",
    "factor_p1_q3": "0",
    "factor_p1_q4": "0",
    "factor_p1_q5": "0",
    "factor_p2_q0": "0",
    "factor_p2_q1": "0",
    "factor_p2_q2": "0",
    "factor_p2_q3": "0",
    "factor_p2_q4": "0",
    "factor_p3_q0": "0",
    "factor_p3_q1": "0",
    "factor_p3_q2": "0",
    "factor_p3_q3": "0",
    "factor_p4_q0": "0",
    "factor_p4_q1": "0",
    "factor_p4_q2": "0",
    "factor_p5_q0": "0",
    "factor_p5_q1": "0",
    "factor_p6_q0": "0",
    "center_L2_exponent": "0",
    "far_L2_exponent": "0",
    "interpolation": "0",
    "uniform_s_threshold": "0"
  },
  "scope": "Exact scalar/knot premises and finite derivative algebra only. Exact canonical joins are inherited; no fresh join recomputation, interval enclosure, physical norm or analytical Sobolev conclusion from finite checks.",
  "check_sha256": "274bb06737d3409b0bed32e1863b299a43964030ae32532670016c4e28c8aaba",
  "independent": {
    "start_utc": "2026-10-22T04:52:22.708150+00:00",
    "utc": "2026-10-22T04:52:25.785956+00:00",
    "status": "PASS_INDEPENDENT_HEX_FMPQ_NORMAL_ORDER_HIGHER_DERIVATIVES",
    "proof_sha256": "0dcddf0f8356c434242ffc63986a74079e578d70acb7c32acc76975018730f4f",
    "code_sha256": "eec1fbef27e7a791dca5b2994d97c26922af740dc814b927b84c02b46f86c455",
    "check_sha256": "274bb06737d3409b0bed32e1863b299a43964030ae32532670016c4e28c8aaba",
    "parent_pin_count": 1922,
    "exact_parameters_compared": 13,
    "knots_compared": 1573,
    "outer_exponents_compared": 10,
    "differential_ring_checks": 29,
    "maximum_total_derivative": 6,
    "source_reuse": "Formal differential ring adapted from independently checked result202, now extended through6. No primary evaluator or Sympy import.",
    "scope": "Exact data and finite algebra checks only. The explicit equal coefficient arrays for interpolation are tautological diagnostics, not independent analytical evidence. The annular weak derivative and Sobolev proof remain analytic; no new interval enclosure or physical norm."
  },
  "independent_sha256": "5205d1462a9814fd9195d96b9c9a924e4a679831d4296fb3043a40340b398932"
}

The omitted parent map is freshly rehashed by both programs. No new interval enclosure, matching-coefficient certificate or physical norm has been computed. Read REVIEW_RESPONSE for the exact scope of inherited inputs and tautological diagnostics.
