# Actual executed evidence for graph constraint limits

{
  "start_utc": "2026-10-22T05:44:38.982488+00:00",
  "utc": "2026-10-22T05:44:42.083252+00:00",
  "status": "PASS_SYMBOLIC_POLARIZATION_AND_FINITE_PROJECTION_FIXTURES",
  "proof_sha256": "5938f6fb1e1d96d44cce1e962cb24fc94fd2367d3dca5449a6646174da6de3c6",
  "code_sha256": "7f397ce03a4ad3058abaeea80a813b641dd41d77760174e8c4a85bd38f1c454a",
  "parent_pin_count": 2069,
  "symbolic_identities": {
    "polarization_unsymmetric": "0",
    "quadratic_homogeneity": "0",
    "fixed_correction_cross": "0",
    "trace_subtraction_given_unit_trace": "0",
    "scaled_difference": "0"
  },
  "projection_fixtures": [
    {
      "m": 0,
      "r": 0,
      "dim": 3,
      "matrix": [],
      "basis_columns": [],
      "plateau_null": [
        "1"
      ],
      "input": [
        "2/3",
        "-3/4",
        "4/5"
      ],
      "coefficients": [],
      "correction": [
        "0",
        "0",
        "0"
      ],
      "projected": [
        "2/3",
        "-3/4",
        "4/5"
      ]
    },
    {
      "m": 1,
      "r": 0,
      "dim": 4,
      "matrix": [
        [
          "0",
          "0",
          "0",
          "0"
        ]
      ],
      "basis_columns": [],
      "plateau_null": [
        "1",
        "0"
      ],
      "input": [
        "2/3",
        "-3/4",
        "4/5",
        "-5/6"
      ],
      "coefficients": [],
      "correction": [
        "0",
        "0",
        "0",
        "0"
      ],
      "projected": [
        "2/3",
        "-3/4",
        "4/5",
        "-5/6"
      ]
    },
    {
      "m": 1,
      "r": 1,
      "dim": 4,
      "matrix": [
        [
          "1",
          "6",
          "19/3",
          "7"
        ]
      ],
      "basis_columns": [
        0
      ],
      "plateau_null": [
        "-6",
        "1"
      ],
      "input": [
        "2/3",
        "-3/4",
        "4/5",
        "-5/6"
      ],
      "coefficients": [
        "-23/5"
      ],
      "correction": [
        "-23/5",
        "0",
        "0",
        "0"
      ],
      "projected": [
        "79/15",
        "-3/4",
        "4/5",
        "-5/6"
      ]
    },
    {
      "m": 2,
      "r": 1,
      "dim": 5,
      "matrix": [
        [
          "1",
          "6",
          "19/3",
          "7",
          "39/5"
        ],
        [
          "1",
          "6",
          "19/3",
          "7",
          "39/5"
        ]
      ],
      "basis_columns": [
        0
      ],
      "plateau_null": [
        "-6",
        "1",
        "0"
      ],
      "input": [
        "2/3",
        "-3/4",
        "4/5",
        "-5/6",
        "6/7"
      ],
      "coefficients": [
        "73/35"
      ],
      "correction": [
        "73/35",
        "0",
        "0",
        "0",
        "0"
      ],
      "projected": [
        "-149/105",
        "-3/4",
        "4/5",
        "-5/6",
        "6/7"
      ]
    },
    {
      "m": 2,
      "r": 2,
      "dim": 5,
      "matrix": [
        [
          "1",
          "1",
          "47/6",
          "37/5",
          "107/15"
        ],
        [
          "1",
          "2",
          "28/3",
          "39/5",
          "97/15"
        ]
      ],
      "basis_columns": [
        0,
        1
      ],
      "plateau_null": [
        "-19/3",
        "-3/2",
        "1"
      ],
      "input": [
        "2/3",
        "-3/4",
        "4/5",
        "-5/6",
        "6/7"
      ],
      "coefficients": [
        "461/70",
        "-191/420"
      ],
      "correction": [
        "461/70",
        "-191/420",
        "0",
        "0",
        "0"
      ],
      "projected": [
        "-1243/210",
        "-31/105",
        "4/5",
        "-5/6",
        "6/7"
      ]
    },
    {
      "m": 4,
      "r": 2,
      "dim": 7,
      "matrix": [
        [
          "1",
          "1",
          "47/6",
          "37/5",
          "107/15",
          "146/21",
          "191/28"
        ],
        [
          "1",
          "2",
          "28/3",
          "39/5",
          "97/15",
          "110/21",
          "57/14"
        ],
        [
          "1",
          "3",
          "65/6",
          "41/5",
          "29/5",
          "74/21",
          "37/28"
        ],
        [
          "1",
          "4",
          "37/3",
          "43/5",
          "77/15",
          "38/21",
          "-10/7"
        ]
      ],
      "basis_columns": [
        0,
        1
      ],
      "plateau_null": [
        "-19/3",
        "-3/2",
        "1",
        "0",
        "0"
      ],
      "input": [
        "2/3",
        "-3/4",
        "4/5",
        "-5/6",
        "6/7",
        "-7/8",
        "8/9"
      ],
      "coefficients": [
        "9463/1260",
        "-1763/1260"
      ],
      "correction": [
        "9463/1260",
        "-1763/1260",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      "projected": [
        "-8623/1260",
        "409/630",
        "4/5",
        "-5/6",
        "6/7",
        "-7/8",
        "8/9"
      ]
    },
    {
      "m": 4,
      "r": 4,
      "dim": 7,
      "matrix": [
        [
          "1",
          "1",
          "1",
          "1",
          "6701/420",
          "2003/126",
          "19991/1260"
        ],
        [
          "1",
          "2",
          "4",
          "8",
          "4909/105",
          "2696/63",
          "24349/630"
        ],
        [
          "1",
          "3",
          "9",
          "27",
          "15077/140",
          "3865/42",
          "10573/140"
        ],
        [
          "1",
          "4",
          "16",
          "64",
          "21659/105",
          "10474/63",
          "39086/315"
        ]
      ],
      "basis_columns": [
        0,
        1,
        2,
        3
      ],
      "plateau_null": [
        "-39/5",
        "2/3",
        "-53/7",
        "-5/4",
        "1"
      ],
      "input": [
        "2/3",
        "-3/4",
        "4/5",
        "-5/6",
        "6/7",
        "-7/8",
        "8/9"
      ],
      "coefficients": [
        "10429/1260",
        "-571/252",
        "2618701/317520",
        "-319/630"
      ],
      "correction": [
        "10429/1260",
        "-571/252",
        "2618701/317520",
        "-319/630",
        "0",
        "0",
        "0"
      ],
      "projected": [
        "-9589/1260",
        "191/126",
        "-472937/63504",
        "-103/315",
        "6/7",
        "-7/8",
        "8/9"
      ]
    },
    {
      "m": 6,
      "r": 3,
      "dim": 9,
      "matrix": [
        [
          "1",
          "1",
          "1",
          "211/15",
          "1544/105",
          "649/42",
          "4099/252",
          "1541/90",
          "8914/495"
        ],
        [
          "1",
          "2",
          "4",
          "517/15",
          "3859/105",
          "824/21",
          "5273/126",
          "4009/90",
          "23413/495"
        ],
        [
          "1",
          "3",
          "9",
          "341/5",
          "2588/35",
          "3361/42",
          "2417/28",
          "2783/30",
          "49162/495"
        ],
        [
          "1",
          "4",
          "16",
          "1729/15",
          "13259/105",
          "2894/21",
          "9430/63",
          "14561/90",
          "86161/495"
        ],
        [
          "1",
          "5",
          "25",
          "527/3",
          "20344/105",
          "8929/42",
          "58447/252",
          "4529/18",
          "26882/99"
        ],
        [
          "1",
          "6",
          "36",
          "1247/5",
          "9673/35",
          "6392/21",
          "4663/14",
          "10867/30",
          "193909/495"
        ]
      ],
      "basis_columns": [
        0,
        1,
        2
      ],
      "plateau_null": [
        "-7",
        "-2/5",
        "-20/3",
        "1",
        "0",
        "0",
        "0"
      ],
      "input": [
        "2/3",
        "-3/4",
        "4/5",
        "-5/6",
        "6/7",
        "-7/8",
        "8/9",
        "-9/10",
        "10/11"
      ],
      "coefficients": [
        "11773/3465",
        "-49381/13860",
        "703541849/192099600"
      ],
      "correction": [
        "11773/3465",
        "-49381/13860",
        "703541849/192099600",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      "projected": [
        "-9463/3465",
        "19493/6930",
        "-549862169/192099600",
        "-5/6",
        "6/7",
        "-7/8",
        "8/9",
        "-9/10",
        "10/11"
      ]
    }
  ],
  "scope": "General functional analysis is the informal proof. Eight exact manufactured matrices are regression checks only, including rank0 and rank deficiency. No new modal enclosure or norm ceiling is computed.",
  "check_sha256": "9f5823900f93b014ce539c9916d34835f5f4c9bf19989c55c7121c023c7fd7fd",
  "independent": {
    "start_utc": "2026-10-22T05:44:42.410705+00:00",
    "utc": "2026-10-22T05:44:45.356588+00:00",
    "status": "PASS_INDEPENDENT_FMPQ_POLYNOMIAL_AND_ROW_ELIMINATION_CHECKS",
    "proof_sha256": "5938f6fb1e1d96d44cce1e962cb24fc94fd2367d3dca5449a6646174da6de3c6",
    "code_sha256": "505e22d441746b1bf5fdc8cf3ff6565cf4a4ce7c39467069aaad56671325ec76",
    "check_sha256": "9f5823900f93b014ce539c9916d34835f5f4c9bf19989c55c7121c023c7fd7fd",
    "parent_pin_count": 2069,
    "ring_checks": {
      "polarization_unsymmetric": true,
      "quadratic_homogeneity": true,
      "fixed_correction_cross": true,
      "scaled_difference": true
    },
    "projection_fixtures_compared": 8,
    "fixture_class_counts": {
      "rank_zero": 2,
      "rank_deficient_positive": 3,
      "full_row_rank": 3
    },
    "scope": "Exact finite algebra only. Sparse polynomial expansion and separate rational row operations reproduce primary fixtures; these eight matrices do not prove the general continuous-constraint theorem. No new modal data, interval or norm ceiling."
  },
  "independent_sha256": "07346e9a0a8e35399108dfa63b00ddaaba2b674f8edbc4fc392a578d3dde20c0"
}

The omitted parent map is in evidence/check.json. Both programs freshly rehashed all2069parentfiles. No interval enclosure, numerical inverse constant or finite-dimensional verification of the full analytic theorem is claimed. Read the full informal proof and REVIEW_RESPONSE.md.
