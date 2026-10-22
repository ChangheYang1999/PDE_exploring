# Executed compact-potential checks

{
  "compact_proof_first.json": {
    "utc": "2026-10-22T03:51:19.636523+00:00",
    "status": "COMPACT_VELOCITY_PROOF_BEFORE_NEW_CHECKER",
    "proof_sha256": "1079a79a6995ed608fc21d60e221c90a3e9d253ca3fc6574456d0b3752d63342"
  },
  "compact_check.json": {
    "start_utc": "2026-10-22T03:51:54.129786+00:00",
    "utc": "2026-10-22T03:51:55.279838+00:00",
    "status": "PASS_DIRECT_CARTESIAN_COMPACT_POTENTIAL_IDENTITIES",
    "proof_sha256": "1079a79a6995ed608fc21d60e221c90a3e9d253ca3fc6574456d0b3752d63342",
    "code_sha256": "edfc8687204b4b2288424a3fd09abe6646ebc5bd3dab835f438ef2c27539c33b",
    "symbolic_identities": {
      "complete_cartesian_laplacian": "0",
      "unoscillated_log_laplacian": "0",
      "leading_velocity_1": "0",
      "leading_velocity_2": "0",
      "canonical_curl_identity": "0",
      "canonical_divergence_identity": "0"
    },
    "scope": "Analytic canonical uniqueness and norm/domain statements require the full proof; no such claim follows from symbolic zero checks."
  },
  "compact_independent.json": {
    "start_utc": "2026-10-22T03:52:31.329784+00:00",
    "utc": "2026-10-22T03:52:31.333958+00:00",
    "status": "PASS_INDEPENDENT_LAURENT_DIFFERENTIAL_POLYNOMIAL_COMPACT_CHECKS",
    "proof_sha256": "1079a79a6995ed608fc21d60e221c90a3e9d253ca3fc6574456d0b3752d63342",
    "code_sha256": "a1f377de46afed4acd68668437fea05175500c761aec6904eeba2cb243dee4b9",
    "primary_sha256": "80354635f69ca2cd7e2f3870a47b23f42cf3326fb5eb9813f090024651b636a2",
    "exact_checks": [
      "complete_Laurent_Laplacian",
      "positive_density_phase_square",
      "velocity1_leading_coefficient",
      "velocity2_leading_coefficient",
      "full_divergence_identity",
      "full_curl_identity",
      "mixed_derivative_commutation",
      "frozen_differentiation_does_not_raise_phase_degree"
    ],
    "polynomial_term_counts": {
      "Laplacian": 13,
      "velocity1": 6,
      "velocity2": 9,
      "density": 13,
      "frozen_image": 54
    },
    "scope": "No Sympy, no input formulas from primary. The primitive product/chain rules generate the full Cartesian jets. Analytic function-space conclusions remain proof claims."
  }
}

These are exact finite identities. The analytic norm estimates and closed-graph consequence are stated and proved in COMPACT_VELOCITY_PROOF.md and require an actual mathematical review. The primary checker differentiates Cartesian functions in Sympy. The independent checker implements product and chain rules with rational Laurent differential polynomials and no Sympy.
