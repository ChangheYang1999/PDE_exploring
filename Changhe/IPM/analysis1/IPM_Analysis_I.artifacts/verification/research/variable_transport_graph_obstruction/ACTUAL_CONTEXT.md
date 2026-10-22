# Executed evidence and explicit input scope

{
  "start_utc": "2026-10-22T03:48:05.140401+00:00",
  "utc": "2026-10-22T03:48:09.145460+00:00",
  "status": "PASS_SOURCE_RECTANGLE_STRICT_MISMATCH_AND_CONJUGATIONS",
  "proof_sha256": "5f6216563558ba2bbf28709c1a24bb2772b792d19f9fa75ee87eb033763202a4",
  "code_sha256": "79d478bf5791e2279b99b99a0f7c6ab3bf6f78a3fd37cafa6199812aaed80140",
  "parent_pin_count": 1811,
  "parents": {
    "moving_source": {
      "path": "research/moving_source/evidence/verdict.json",
      "sha256": "dbe8a4e8794275a1524c9879c0bbfe949eb931bb3acc1014c7f30c9e90d83e11",
      "status": "CONFIRMED_MOVING_SOURCE_THEOREM_WITH_SCALAR_CORRECTION",
      "utc": "2026-10-21T02:34:55.022641+00:00",
      "pins": 36,
      "byte_identical_rebindings": {}
    },
    "annular_degree_five_leakage_v2": {
      "path": "research/annular_degree_five_leakage_v2/evidence/verdict.json",
      "sha256": "e278d00ef75c8622235c16e9064d9cbd9be810f42e47f4eff28de8b077a88d25",
      "status": "CONFIRMED_ACTUAL_FINITE_REGULARITY_ANNULAR_DEGREE_FIVE_LEAKAGE",
      "utc": "2026-10-22T02:44:08.697628+00:00",
      "pins": 173,
      "byte_identical_rebindings": {}
    },
    "logarithmic_frozen_range_inverse": {
      "path": "research/logarithmic_frozen_range_inverse/evidence/verdict.json",
      "sha256": "a5cce5f36cf56efdd512eb8ef5274f0b8708151342f4a16ec93892006601c3d7",
      "status": "CONFIRMED_ACTUAL_LOGARITHMIC_FROZEN_CLOSED_RANGE_INVERSE",
      "utc": "2026-10-22T03:39:57.005461+00:00",
      "pins": 299,
      "byte_identical_rebindings": {}
    },
    "source_instance": {
      "path": "research/source_instance/evidence/verdict.json",
      "sha256": "be3a8ee307d1ed499af009c767be40b5e5982a1230fc51518355e77fee43516d",
      "status": "CONFIRMED_ACTUAL_LOCAL_SOURCE_INSTANCE",
      "utc": "2026-10-21T02:09:44.300415+00:00",
      "pins": 34,
      "byte_identical_rebindings": {}
    },
    "n8_velocity_hessian": {
      "path": "research/n8_velocity_hessian/evidence/verdict.json",
      "sha256": "8a35f9cb43b241bd7a880b03aa8fcfdc01806a2517f50dbea99530e03a2455d5",
      "status": "CONFIRMED_VELOCITY_HESSIAN_BOUND_WITH_ARCHIVE_DEPENDENCY",
      "utc": "2026-10-21T01:43:36.820235+00:00",
      "pins": 41,
      "byte_identical_rebindings": {}
    },
    "n8_density_hessian": {
      "path": "research/n8_density_hessian/evidence/verdict.json",
      "sha256": "c590ba0d354b26595bd1131f68ca87bbc9875c9d248b4cf5fdf71344ef6e01ca",
      "status": "CONFIRMED_DENSITY_HESSIAN_BOUND_WITH_ARCHIVE_DEPENDENCY",
      "utc": "2026-10-21T01:30:51.600029+00:00",
      "pins": 41,
      "byte_identical_rebindings": {}
    },
    "canonical_full_radial_linkage": {
      "path": "research/canonical_full_radial_linkage/evidence/verdict.json",
      "sha256": "4d91f313ec6dc475fc85a075f4154f6f302081112a0b5f7d77f7a172414eed1e",
      "status": "CONFIRMED_COMPLETE_CANONICAL_RADIAL_MODELS_ARCHIVE_PREMISE_DISCHARGED",
      "utc": "2026-10-22T00:18:37.442287+00:00",
      "pins": 1419,
      "byte_identical_rebindings": {
        "numerics/src/cert_green.py": {
          "sha256": "7f1c067b15d087b0688e3b4f1dc0b3abaf301a421b600ce96f5cedf662d6f8f0",
          "replacement": "research/derivative_intended_partition/sources/cert_green.py"
        },
        "numerics/src/cert_green_outer.py": {
          "sha256": "aed9892b6b89720374c9ff4d6cbf5f455e2ea7c39572376675ea87a387d3b60e",
          "replacement": "research/derivative_intended_partition/sources/cert_green_outer.py"
        },
        "numerics/src/cert_resid.py": {
          "sha256": "1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053",
          "replacement": "research/derivative_intended_partition/sources/cert_resid.py"
        },
        "numerics/src/cert_resid_deriv.py": {
          "sha256": "38e45bcd4400d119fb0a887794c4866bcc1d61eed1c3d69f58616eb7c95d5ac8",
          "replacement": "research/derivative_intended_partition/sources/cert_resid_deriv.py"
        },
        "numerics/src/midrad.py": {
          "sha256": "5b5feb4ad511e66d57d228a3b754e44cfa2ceb17a33f717dde991c464d5f598e",
          "replacement": "research/derivative_intended_partition/sources/midrad.py"
        },
        "numerics/src/xnorm_cert.py": {
          "sha256": "4ea4f2717ccfa8c4b6ec5ee223ee39efae22b486138bbd558418e9c4d899f882",
          "replacement": "research/weighted_derivative_scalar_norms/sources/xnorm_cert.py"
        }
      }
    }
  },
  "source_accepted_bounds": {
    "p_lower": "43/5",
    "mu_lower": "99/100",
    "A0_upper": "51/5",
    "M": "743/2500",
    "R": "99/2000"
  },
  "actual": {
    "k": "1615536043799051/9007199254740992",
    "A": "16398862465682933/1615536043799051",
    "D": "34413260975164917/1615536043799051",
    "e": "1/10000",
    "y_min": "1/2000",
    "y_max": "3/2000",
    "Taylor_remainder": "83959/250000000000",
    "b_lower": "43590141723577828524328261933/4341702632208580842156250000"
  },
  "strict_window": [
    "2509968174709/250000000000",
    "10039872698837/1000000000000"
  ],
  "arb512": {
    "lower_exact": "8413292799192201354826026742838313999724173123604498965368383943094565954501188877297390392796277924824429342313674504201320528989902708249365466042094231/837987995621412318723376562387865382967460363787024586107722590232610251879596686050117143635431464230626991136655378178359617675746660621652103062880256",
    "upper_exact": "8413292799192201354826026742838313999724173123604498965368383943094565954501188877297390392796277924824429342313674504201320528989902708249365466042094241/837987995621412318723376562387865382967460363787024586107722590232610251879596686050117143635431464230626991136655378178359617675746660621652103062880256"
  },
  "symbolic_identities": {
    "frozen_characteristic_phase": "0",
    "frozen_full_conjugation_and_phase_cancellation": "0",
    "variable_full_conjugation": "0",
    "velocity_vector_symbol_square": "0",
    "strain_kernel_sign": "0",
    "strain_F1_cancellation": "0",
    "strain_F3_factor": "0"
  },
  "scope": "Finite rational/interval and conjugation checks only. Function-space estimates and exact corrected sequence depend on the analytic proof.",
  "check_sha256": "f21271ab0959d931d045d18c9a38d65b4fab33a48d0b18846283294f72aa7046",
  "independent": {
    "start_utc": "2026-10-22T03:48:55.241880+00:00",
    "utc": "2026-10-22T03:48:58.241779+00:00",
    "status": "PASS_SEPARATE_HEX_FMPQ_IV_AND_EULER_JET_CHECKS",
    "proof_sha256": "5f6216563558ba2bbf28709c1a24bb2772b792d19f9fa75ee87eb033763202a4",
    "code_sha256": "530aa2b0bc676ac2c903140aaf6aa689675d6478bb54ec59801a61598de715d2",
    "check_sha256": "f21271ab0959d931d045d18c9a38d65b4fab33a48d0b18846283294f72aa7046",
    "parent_pin_count": 1811,
    "exact_values_compared": 8,
    "exact_algebra_checks": [
      "Euler_jet_frozen_conjugation",
      "Euler_jet_phase_cancellation",
      "Euler_jet_variable_zero_order_remainder",
      "direct_strain_kernel_rational_derivative",
      "vector_symbol_numerator_identity"
    ],
    "iv220": {
      "lower_exact": "14176370322584016619261163366094312595794268385510581219245274555435787535271409078838171604380344787085783594140978078936796502616375515540312074514806997927538994727729260088573635891426689379474749794978321224837764677/1412006979354108748474554421102313931675676955925788762341700965431346915180599249952936960497614998485448932749141998289061648432939195473813276544243473053215398045741358060286316036246351763861878679739417265182867456",
      "upper_exact": "7088185161292008309630581683047156297897134192755290609622637277717893767635704539419085802190172393542891797070489039468398251308187757770156037257403498963769497363864630044286817945713344689737374897489160612418882339/706003489677054374237277210551156965837838477962894381170850482715673457590299624976468480248807499242724466374570999144530824216469597736906638272121736526607699022870679030143158018123175881930939339869708632591433728"
    },
    "strict_window": [
      "2509968174709/250000000000",
      "10039872698837/1000000000000"
    ],
    "scope": "Independent arithmetic libraries and algebra construction; analytic Sobolev/sequence proof is not replaced by these finite checks."
  }
}

The omitted complete parent_files map remains in evidence/check.json. It has been rehashed by both checkers. The actual review examines the analytic proof and executed arithmetic; these records do not themselves certify infinite-dimensional estimates. Canonical parent foreign-source substitutions are byte identical and recorded in parents. No whole-plane image membership or full IPM noninvertibility is claimed.
