# Actual207 finite checks

{
  "start_utc": "2026-10-22T05:10:14.862855+00:00",
  "utc": "2026-10-22T05:10:19.139591+00:00",
  "status": "PASS_CENTER_POTENTIAL_SCALING_CONJUGATION_AND_TRACE_ALGEBRA",
  "proof_sha256": "1520a97d475afcfd62a464c32d7549d299d2d33ddf3ef24776528006ecdd3f58",
  "code_sha256": "67670fb417b00053e359e73c26a60dbcb7ca3f8397a743739f5c8ec99e3672fa",
  "parent_pin_count": 1980,
  "actual": {
    "k": "1615536043799051/9007199254740992",
    "A": "16398862465682933/1615536043799051",
    "D": "34413260975164917/1615536043799051",
    "D_minus_2A": "1",
    "example_weight": "3/2",
    "example_decay_power": "1",
    "s": "153/50"
  },
  "symbolic_identities": {
    "two_term_scaling": "0",
    "H2_expansion": "0",
    "Poisson_stream": "0",
    "velocity_divergence": "0",
    "velocity_curl": "0",
    "center_density": "0",
    "center_J": "0",
    "center_Sigma": "0",
    "frozen_conjugation": "0",
    "lower_decay_power": "0",
    "upper_decay_power": "0",
    "power_preservation_order1": "0",
    "power_preservation_order2": "0",
    "power_preservation_order3": "0",
    "power_preservation_order4": "0",
    "power_preservation_order5": "0",
    "power_preservation_order6": "0"
  },
  "center_J": "1",
  "center_Sigma": "0",
  "delta_powers": [
    "5/2-b",
    "9/2-b"
  ],
  "scope": "Finite exact identities only. General Sobolev convergence, sublinear-gauge uniqueness and nonclosability follow from the informal proof and REVIEW_RESPONSE, not these checks.",
  "check_sha256": "b6287da288cd52b22d0b00388d9b3c64a733f7f42339d5bc33c3920d540f9400",
  "independent": {
    "start_utc": "2026-10-22T05:10:27.840126+00:00",
    "utc": "2026-10-22T05:10:30.929311+00:00",
    "status": "PASS_INDEPENDENT_FMPQ_DIFFERENTIAL_RING_CENTER_TRACE",
    "proof_sha256": "1520a97d475afcfd62a464c32d7549d299d2d33ddf3ef24776528006ecdd3f58",
    "code_sha256": "4fda9483926657ea450c446f89be72ac98a957361dabfa389d9cb3641694ec13",
    "check_sha256": "b6287da288cd52b22d0b00388d9b3c64a733f7f42339d5bc33c3920d540f9400",
    "parent_pin_count": 1980,
    "exact_parameters_compared": 7,
    "ring_checks": {
      "physical_two_term_scaling": true,
      "physical_Poisson_stream": true,
      "physical_divergence": true,
      "physical_curl": true,
      "density_even_x": true,
      "density_odd_y": true,
      "center_density": true,
      "center_J": true,
      "center_strain": true,
      "frozen_weight_conjugation": true,
      "closed_Euler_order1": true,
      "closed_Euler_order2": true,
      "closed_Euler_order3": true,
      "closed_Euler_order4": true,
      "closed_Euler_order5": true,
      "closed_Euler_order6": true
    },
    "center_J": "1",
    "center_Sigma": "0",
    "source_reuse": "Independent fmpq Leibniz differential ring and Stirling normal ordering; no NPZ, Sympy or primary code import.",
    "scope": "Finite algebra and exact parameter instance only. Sobolev convergence, canonical uniqueness and nonclosability are analytic arguments."
  },
  "independent_sha256": "b30bceb6f9cae06c36c5d83d77850c642fbac70f79d4666b6589612c4b9e34f2"
}

The omitted parent hash map is present in evidence/check.json. Both implementations independently rehashed all1980pins. The finalizer will compare this exact JSON to current check records. No interval computation or background norm is involved.
