# Exact executed evidence for the full graph nonlinearity argument

{
  "start_utc": "2026-10-22T05:31:41.420606+00:00",
  "utc": "2026-10-22T05:31:49.025759+00:00",
  "status": "PASS_COMPACT_POTENTIAL_WAVE_AND_POLARIZATION_IDENTITIES",
  "proof_sha256": "3ecda23dfa05f97bb7aedb762506b6d21e5a40e6918d6c9fc69d3b893cce4f32",
  "code_sha256": "a8b55e82a42e01db258578649fb6ebd0f056233abdb648187bf4a8b46d17640f",
  "parent_pin_count": 2041,
  "actual": {
    "k": "1615536043799051/9007199254740992",
    "A": "16398862465682933/1615536043799051",
    "D": "34413260975164917/1615536043799051",
    "bi": "3518437208883275/70368744177664",
    "L": "8614738245908811/1125899906842624",
    "inner_tau": "-685794559684773/140737488355328",
    "spline_degree": "7",
    "modes": "260",
    "s_example": "153/50",
    "center_Vx_coefficient": "-16398862465682933/1615536043799051"
  },
  "symbolic_identities": {
    "canonical_Poisson": "0",
    "divergence_free": "0",
    "curl_sign": "0",
    "plateau_density": "0",
    "plateau_velocity1": "0",
    "plateau_velocity2": "0",
    "plateau_gradient_x": "0",
    "plateau_gradient_y": "0",
    "density_wave_expansion": "0",
    "velocity1_wave_expansion": "0",
    "velocity2_wave_expansion": "0",
    "transport_phase_factorization": "0",
    "transverse_leading_remainder": "0",
    "plateau_cross_exact": "0",
    "reflection_U_-1_-1_0": "0",
    "reflection_U_-1_-1_1": "0",
    "reflection_density_-1_-1": "0",
    "reflection_first_integral_-1_-1": "0",
    "reflection_U_-1_1_0": "0",
    "reflection_U_-1_1_1": "0",
    "reflection_density_-1_1": "0",
    "reflection_first_integral_-1_1": "0",
    "reflection_U_1_-1_0": "0",
    "reflection_U_1_-1_1": "0",
    "reflection_density_1_-1": "0",
    "reflection_first_integral_1_-1": "0",
    "reflection_U_1_1_0": "0",
    "reflection_U_1_1_1": "0",
    "reflection_density_1_1": "0",
    "reflection_first_integral_1_1": "0",
    "full_rank_one_polarization": "0",
    "zero_strain_polarization": "0",
    "modulation_power_0": "0",
    "modulation_power_1": "0",
    "modulation_power_2": "0",
    "scaled_cross_power": "0",
    "origin_saddle_relation": "0"
  },
  "reflections": [
    {
      "sx": -1,
      "sy": -1,
      "potential_sign": -1,
      "velocity_signs": [
        -1,
        -1
      ]
    },
    {
      "sx": -1,
      "sy": 1,
      "potential_sign": 1,
      "velocity_signs": [
        -1,
        1
      ]
    },
    {
      "sx": 1,
      "sy": -1,
      "potential_sign": -1,
      "velocity_signs": [
        1,
        -1
      ]
    },
    {
      "sx": 1,
      "sy": 1,
      "potential_sign": 1,
      "velocity_signs": [
        1,
        1
      ]
    }
  ],
  "scope": "Exact finite algebra and data only. First-integral existence, compact support, all-order Sobolev modulation, full graph bounds and nonlinear discontinuity are analytic claims, not inferred from these finite checks.",
  "check_sha256": "b572e32da4cd4a995d60a103d3ec70c172bd3026835297efd143322da61f2781",
  "independent": {
    "start_utc": "2026-10-22T05:32:59.363540+00:00",
    "utc": "2026-10-22T05:33:02.423249+00:00",
    "status": "PASS_INDEPENDENT_FMPQ_WAVE_JET_AND_POLARIZATION_ALGEBRA",
    "proof_sha256": "3ecda23dfa05f97bb7aedb762506b6d21e5a40e6918d6c9fc69d3b893cce4f32",
    "code_sha256": "8f2ff51a5c0a532d3161269e74dca4ba40f68965bda59b23aa8838e0696c1941",
    "check_sha256": "b572e32da4cd4a995d60a103d3ec70c172bd3026835297efd143322da61f2781",
    "parent_pin_count": 2041,
    "exact_parameters_compared": 10,
    "ring_checks": {
      "canonical_Poisson": true,
      "divergence_free": true,
      "curl_sign": true,
      "plateau_density": true,
      "plateau_velocity1": true,
      "plateau_velocity2": true,
      "plateau_gradient_x": true,
      "plateau_gradient_y": true,
      "density_wave_expansion": true,
      "velocity1_wave_expansion": true,
      "velocity2_wave_expansion": true,
      "transport_phase_factorization": true,
      "transverse_leading_remainder": true,
      "plateau_cross_exact": true,
      "reflection_density_-1_-1": true,
      "reflection_velocity_-1_-1_0": true,
      "reflection_velocity_-1_-1_1": true,
      "reflection_density_-1_1": true,
      "reflection_velocity_-1_1_0": true,
      "reflection_velocity_-1_1_1": true,
      "reflection_density_1_-1": true,
      "reflection_velocity_1_-1_0": true,
      "reflection_velocity_1_-1_1": true,
      "reflection_density_1_1": true,
      "reflection_velocity_1_1_0": true,
      "reflection_velocity_1_1_1": true,
      "flow_phase_first_integral_at_P": true,
      "vertical_phase_derivative": true,
      "full_rank_one_polarization": true,
      "zero_strain_polarization": true,
      "quadratic_homogeneity": true
    },
    "modulation_adjusted_affine_powers": [
      [
        "0",
        "0"
      ],
      [
        "-1",
        "0"
      ],
      [
        "-2",
        "0"
      ]
    ],
    "scaled_cross_power": "0",
    "reflections_compared": 4,
    "source_reuse": "Leibniz rational ring structure adapted from prior independent checkers; new phase Sin/Cos chain rule and polarization. No NumPy, Sympy or primary evaluator imported. Common n^(-s) is factored out as a spatial constant.",
    "scope": "Exact finite algebra only. The vertical phase derivative is an initial-coordinate convention, not computational evidence for existence of the flow chart. Sobolev estimates, support and discontinuity remain analytic."
  },
  "independent_sha256": "3d087d63ff2535a04b6f8126a65536d4c352c3d98fcef6dadd9028ba496c8991"
}

The omitted parent_files dictionary contains 2041 dependencies, freshly rehashed by both checks. The parent chain supplies the exact joined-normalized background. New checks establish only finite algebra and exact data decoding, not analytic Sobolev estimates, flow existence or any numerical norm constant. ADDENDUM.md is mandatory and corrects the two impossible ball-containment phrases in the original proof.
