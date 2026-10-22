# Literal finite outputs for the forward-weight threshold

{
  "start_utc": "2026-10-22T03:16:00.350551+00:00",
  "utc": "2026-10-22T03:16:00.414764+00:00",
  "status": "PASS_EXACT_RATIONAL_AND_GENERAL_POLYNOMIAL_THRESHOLDS_REQUIRES_INDEPENDENT_REVIEW",
  "proof_sha256": "c96953a0c0d7580b0178cf593e77d08b92ef9eed52bbf322569ddb557df362d4",
  "code_sha256": "85ab7df9279f205e77038260399870bbda2bb329b1095d8139004a49db4f040c",
  "parents": {
    "residual": {
      "path": "research/canonical_axis_residual/evidence/verdict.json",
      "sha256": "1cefbee28c5de00af4580231c5c7ca2fbc970e773bfa14faedff8227222fd001",
      "status": "CONFIRMED_ACTUAL_CANONICAL_AXIS_RESIDUAL"
    },
    "quadrant": {
      "path": "research/quadrant_euler_axis_obstruction/evidence/verdict.json",
      "sha256": "f39dd67370e62ed494d7a8bf711d574b9dbc55c30595ad0646bc9fa3b0d4678f",
      "status": "CONFIRMED_ACTUAL_QUADRANT_EULER_AXIS_OBSTRUCTION"
    }
  },
  "parent_pin_count": 234,
  "exact": {
    "k": "1615536043799051/9007199254740992",
    "A": "16398862465682933/1615536043799051",
    "D": "34413260975164917/1615536043799051",
    "b0": "10622735298540043/1615536043799051",
    "theta_153_over_50": "4734092164273230151/819943123284146650",
    "phi_307_over_100": "9502597589521625219/1639886246568293300",
    "quadrant_counterexample_delta": "81994312328414665/3231072087598102",
    "quadrant_counterexample_inverse_norm": "3231072087598102/81994312328414665",
    "Y_counterexample_delta_minus": "5776127167142890/1615536043799051"
  },
  "theta_strict_window": [
    "577368360053/100000000000",
    "5773683600531/1000000000000"
  ],
  "general_polynomial_identities": 4,
  "check_sha256": "2903452285ebe9b63268d66fa6e66b49cc6eec571d356e597142c22dd60c9759",
  "independent": {
    "start_utc": "2026-10-22T03:16:12.717136+00:00",
    "utc": "2026-10-22T03:16:13.233009+00:00",
    "status": "PASS_INDEPENDENT_INTEGER_HEX_FMPQ_AND_SYMBOLIC_GENERAL_THRESHOLDS",
    "code_sha256": "23443fcb8466455f30a5d34d7d509d3c5192375027e8a5e9d9f736697e396c98",
    "check_sha256": "2903452285ebe9b63268d66fa6e66b49cc6eec571d356e597142c22dd60c9759",
    "parent_pin_count": 234,
    "exact_values_compared": 9,
    "general_symbolic_identities": 4,
    "strict_midpoint_quantifier_identities": 2,
    "group_conjugation_power_identity": true,
    "theta_strict_window": [
      "577368360053/100000000000",
      "5773683600531/1000000000000"
    ],
    "PDE_endpoint": "UNRESOLVED"
  }
}

The full check.json also contains234 inherited file hashes. Each was freshly rehashed by both paths; this excerpt avoids repeating their long list in the review input. Parent hashes establish byte identity, not mathematical claims. The earlier review2bf9f303-cd42-4dec-8ce1-8cb2a90d2aa4 stopped at max_tokens and is incomplete, not accepted. The proof and codes are unchanged. The first independent symbolic assertion compared different equivalent expression trees; source and failure are retained under evidence/independent_first_attempt*, and the successful rerun normalized their difference.
