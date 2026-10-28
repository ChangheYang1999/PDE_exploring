# Accompanying artifacts

These files support the report "Hölder-seminorm constants of the planar second-order Riesz transforms".
Each theorem of the report has a complete written proof here. Each certified number has an interval
certificate here. All paths are relative to this folder, and all commands below are run from this folder.

## Before use: restore the packed certificate files

To keep the folder small, the JSON files of five folders (`05_team_audit/`, `08_improved_upper_bounds/`,
`09_uniform_comparison/`, `lead_closed_form37/`, `numerics_data/`) are packed, with their relative paths, in
`bundles/<folder>.json.tar.xz`. The proofs (`PROOF.md` and other Markdown files) and programs stay unpacked. Restore the
JSON files in place with

```sh
for a in bundles/*.json.tar.xz; do tar -xJf "$a"; done
```

Two folders of intermediate per-row replay records are not included (768 files, about 150 MB). They are inputs of the
residual-cost combinations behind the Theorem 3.6 and Theorem 3.7 values of Table 1, and are regenerated deterministically
(single-threaded, interval arithmetic) by

```sh
python3 code/replay_middle_balanced_residuals.py      # writes 08_improved_upper_bounds/middle_circle_transport/balanced_residual/verification/mass_replay/
python3 code/replay_balanced_circle_residuals.py      # writes 08_improved_upper_bounds/local_disk_transport/balanced_residual/existing_certificates/verification/mass_replay/
```

after which the combination programs `code/combine_middle_balanced_residuals.py`, `code/combine_balanced_circle_residuals.py`,
`code/extend_middle_residual_table37.py` and `code/refine_balanced_circle_radial.py` can be rerun. Their combined outputs
(the `accepted.json` and `numerical_values/` records used by Table 1) are included. Run logs, caches, copies of papers and records of web access attempts are not included.
Small exploratory outputs are retained where they document the numerical experiments.

Requirements: Python 3 with `python-flint` (Arb ball arithmetic), `mpmath` and `numpy`; the numerical experiments in
`numerics_code/` also use `scipy` (HiGHS linear programming). Numerical programs may use multiple worker processes; the command lines and certificates record worker counts.
The two replay commands above run sequentially.

## Proofs, by theorem of the report

| Report | Folder |
|---|---|
| Section 1 (definitions, identities, extension modulo constants, compact approximation) | `01_setup/` |
| Section 2 (literature, exact statements) | `04_literature/README.md`, `04_literature/hilbert_exact/`, `04_literature/hilbert_periodic_direct/` (direct proof of the periodic constants) |
| Theorem 3.1 (closed-form bound $F$) | `02_upper_bounds/`, `02_upper_bounds/shell_counterexample/` |
| Theorem 3.2 (projection bound $G$ for $R_1^2$) | `08_improved_upper_bounds/local_projection/` |
| Theorem 3.3 (midpoint split) | `08_improved_upper_bounds/midpoint_split/` |
| Theorem 3.4 (reflection orbits) | `08_improved_upper_bounds/reflection_orbits/` |
| Theorem 3.5 (exterior circles) | `08_improved_upper_bounds/far_circle_transport/` |
| Theorem 3.6 (middle circles) | `08_improved_upper_bounds/middle_circle_transport/` (with the middle-arc residual cost in `balanced_residual/`), `lead_d36/` and `05_team_audit/d36_recombination/` (the recombination on the direct certificates at $\alpha=\frac15,\frac{99}{100}$ and its independent check); the finer cross-disk enclosure on $2048^2$ rectangles: `05_team_audit/cross2048/` (program and certificate in `source/`, diagnostics in `verification/`, recombination with the phase interpolation in `recombination/`); the same on $4096^2$ rectangles: `05_team_audit/cross4096/` (same layout) |
| Theorem 3.7 (paired local circles) | `08_improved_upper_bounds/paired_local_circles/` (method), `08_improved_upper_bounds/paired_local_circles/certified_half/` (the value at $\alpha=\frac12$), `08_improved_upper_bounds/paired_local_circles/certified_more/` (the values at $\alpha=0.3,0.75,0.9$), `lead_table37/` (the values at $\alpha=0.001,0.01,0.05,0.1,0.2,0.99$ with plans chosen at each exponent) and `05_team_audit/table37_lead/` (its independent audit) |
| Theorem 3.8 (exact phase interpolation) | `08_improved_upper_bounds/phase_interpolation/` (proof `PROOF.md`, the evaluation rules in `numerical_values/`, and the evaluation and accepted values in `verification/`) |
| Theorem 3.9 (strict saving in the identity term) | `08_improved_upper_bounds/local_projection/strict_increment/` (the reflection coupling on two disks), `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/` (containment of the disks), `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/` (the density bound and $J$), `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/cutoff_plan/` (part (c)), `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/symmetric_concavity/` (the symmetric cost $A(\xi)$), `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/symmetric_concavity/fourth_moment/` ($K$) and its subfolder `numerical_values/` (earlier values and their independent evaluation), `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/` (the exact radial density on the disks, the closed forms of $J$ and $K$; the values after the saving of Theorem 3.9 in `numerical_values/` and, on the $4096^2$ cross-disk enclosure, in `cross4096_values/`) |
| Theorem 3.10 (larger disks and all even moments) | `08_improved_upper_bounds/local_projection/strict_increment/all_even_moments/` (the full even-moment saving and its cutoff version), `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/optimal_axis_disks/` (the optimal centre $c_*$ and the containment of the larger disks; the values without part (c) in `numerical_values/`), `08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/` (part (c), the phase-uniform reflection density, with its values without part (d) in `numerical_values/`), `08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/supplemental_disks/` (part (d), the four further disjoint disk pairs: `PROOF.md`, the exact geometry certificate `geometry.json`, and the values of Table 1 and of Theorem 5.7 in `numerical_values/`) |
| Corollary in Section 8, item 4 ($C_\alpha<D_\alpha$ for all sufficiently small $\alpha$) | `08_improved_upper_bounds/strict_separation_near_zero/` |
| Lemma 4.0, Theorem 4.1 (signed-distance witnesses, two-cusp bound) | `03_lower_bounds/` |
| Theorem 4.2 (refined two-cusp bound) | `03_lower_bounds/two_cusp_refinement/` |
| Theorem 4.3 (gated witness) | `03_lower_bounds/gated_witness/` |
| Theorem 4.4 (degree-three homogeneous witness) | `03_lower_bounds/homogeneous_degree_three/` |
| Theorem 4.5 (polygonal witness) | `05_team_audit/structured_layercake/`, `05_team_audit/structured_endpoints/`, `05_team_audit/structured_witness/` |
| Theorem 4.6 (projection witness for $D_\alpha$, strict separation at $\alpha=\frac1{1000},\frac1{100},\frac1{20},\frac1{10},\frac15,\frac3{10}$) | `07_diagonal_identity_term/finite_projection_witness/` (range (i)), `07_diagonal_identity_term/finite_projection_extended/` (range (ii)), `07_diagonal_identity_term/refined_profile_constant/`, `07_diagonal_identity_term/positive_profile_bound/`, `07_diagonal_identity_term/finite_certified_values/`, `07_diagonal_identity_term/finite_small_values/`, `07_diagonal_identity_term/finite_a30_value/`; the sharper profile factor: `07_diagonal_identity_term/geometric_profile_constant/`; the separation at $\alpha=\frac3{10}$: `07_diagonal_identity_term/finite_geometric_value/` |
| Theorem 5.2 (finite part in the diagonal direction) | `06_small_alpha_second_term/diagonal/` |
| Theorem 5.3 (variational form of the second term) | `06_small_alpha_second_term/general_direction/` |
| Theorem 5.4 (direction maximum, second term of $C_\alpha$) | `06_small_alpha_second_term/direction_maximum/`, `05_team_audit/lead_maximality/`, `06_small_alpha_second_term/axis/` |
| Theorem 5.5 (bracket for the second term of $D_\alpha$) | `07_diagonal_identity_term/asymmetric_cusps/`, `08_improved_upper_bounds/local_projection/` |
| Theorem 5.6 (second term of $D_\alpha$) | `07_diagonal_identity_term/local_projection_profile/` (Step 1), `07_diagonal_identity_term/projection_assembly/` (Step 3), `07_diagonal_identity_term/exact_second_term/` (complete argument) |
| Theorem 5.7 (explicit bounds with the second term) | `08_improved_upper_bounds/explicit_second_term/` (`PROOF.md`; the remainder bounds $J_C$, $J_D$ in `linear_remainder/`, the uniform envelope in `linear_envelope/`, the rational cutoffs in `verification/rational_cutoffs.json`), `08_improved_upper_bounds/explicit_second_term/sharp_deficiency/` (the sharper local deficiencies, the rational enclosure of Catalan's constant in `catalan_evaluation/`, the values of Table 1 and the envelope coefficients in `numerical_values/`), `08_improved_upper_bounds/explicit_second_term/tail_series/` (the exact exterior series $S$ and its bound $S^+_N$; the values of Theorem 5.7 in `numerical_values/`) |
| Theorem 6.1 ($\alpha\to1$) | `02_upper_bounds/`, `03_lower_bounds/homogeneous_degree_three/` |
| Theorem 4.7 (half-plane lattice lemma; axis lattice witnesses, $D_{1/2}$, $D_{3/4}$, $D_{9/10}$, $D_{99/100}$; parts (i) to (iv)) | `11_lattice_pole_constraints/half_plane/`, `11_lattice_pole_constraints/axis_clamped_layercake/`, `11_lattice_pole_constraints/axis_sector_cusp/`, `11_lattice_pole_constraints/monotone_axis/`, `11_lattice_pole_constraints/axis_projection_stieltjes/` (proofs, certificates), `07_diagonal_identity_term/full_range_profile/` (seminorm of the projection profile at $\alpha=\frac34,\frac9{10}$), `code/certify_axis_clamp_layercake.py`, `code/combine_axis_clamp_layercake.py`, `code/certify_axis_projection_stieltjes_v2.py`, `code/combine_projection_lower.py`; the two-dimensional cell enclosure of part (iv) ($D_{1/2}\ge2.4378062352$): `05_team_audit/note14_certificate/` (method proof, interval repairs, source snapshot, and the complete replay `replay_a50/` with its audit `independent_audit.json`), `code/replay_note14_sequential.py`, `code/audit_note14_replay.py` |
| Theorem 4.7(vi), (vii) ($D_{3/4}$ by cell enclosure; homogeneous tail and $D_{1/2}$, $D_{3/4}$, $D_{9/10}$) | `05_team_audit/note14_certificate/replay_a75/`, `05_team_audit/note14_certificate/replay_fine_a50/full_quadratic/` and `05_team_audit/note14_certificate/replay_fine_a75/full_quadratic/` (complete fine replays), `05_team_audit/note14_certificate/producer_fine_a50/` and `05_team_audit/note14_certificate/producer_fine_a75/` (the still finer computations at $\alpha=\frac12$ and $\alpha=\frac34$ that give the stated $D_{1/2}$ and $D_{3/4}$, with the audit of all their task records and the independent replay of $52$, respectively $70$, selected complete tasks in `quadratic_recombination/`), `05_team_audit/note14_certificate/replay_a90_refined/`, `05_team_audit/note14_certificate/refined_cells/` (the two cell refinements used at $\alpha=\frac9{10}$), `05_team_audit/note14_certificate/homogeneous_tail/` (the tail theorem `PROOF.md`, the numerical proof `numerical_values/PROOF.md`, and the audited prefix sums in `verification/`), `code/audit_note14_prefix_tail.py` |
| Theorem 4.7(v) ($D_{3/10}$ from the projection cusp) | `lead_projection/` (certifier, runner, combination, the eight chunk certificates and the combined certificate), `05_team_audit/projection_lead_a30/` (independent audit) |
| Theorem 4.7(viii) ($D_{1/10}$, $D_{1/5}$, $D_{3/10}$ from sharper Stieltjes sums) | `lead_projection/` (`V7_PROOF.md`, `cert_v7.py`, `run_queue7.py`, `combine_v7.py`, the plans in `plans/`, the chunk certificates and `a10v7_combined.json`, `a20v7_combined.json`, `a30v7_combined.json`), `05_team_audit/stieltjes_v7/a10/`, `a20/`, `a30/` (independent checks with selected replays) |
| Theorem 9.1 | `09_uniform_comparison/endpoints/`, `09_uniform_comparison/PROOF.md` |
| Theorem 9.2 (uniform comparison on $(0,1)$) | `09_uniform_comparison/lead_certificate/` (statement and proof, node lists, nodal certificates, combination, independent replay); the Theorem 3.7 family and the per-segment minimum: `09_uniform_comparison/pass3/` |
| Theorem 9.3 (closed forms $F^*$, $G^*$ for every exponent) | `lead_closed_form/` (`PROOF.md`, node remainders, the computation at $\alpha=0$, chord and endpoint checks; reproduction commands in its `README.md`), `05_team_audit/closed_form_lead/` (independent check) |
| Interval-certification conventions | `05_team_audit/numerical_certification/` |
| Theorem 1.1 (coordinate parity classes) | `14_reflection_symmetry/` |
| Theorem 1.2 (the full Hölder norm) | `15_full_norm_scope/` |
| Theorem 1.3 (finite transport approximation) | `13_transport_duality/` |
| Theorem 1.4 (complex inputs; the Beurling transform) | `16_beurling_complex_norm/` (real-kernel projection, approximation), `exact_angular_modes/` (i), `compact_flower/` and `glued_witness/` (lower bound of (ii)), `large_alpha/` and `exact_angular_modes/` (cubic witness), `optimized_upper/` (upper bound of (ii)), `strict_separation/` (iii), all inside `16_beurling_complex_norm/`; `lead_complex_upper/` (upper values at the table exponents) |
| Theorem 1.5 (continuity in the exponent) | `13_transport_duality/exponent_continuity/` |
| Theorem 1.6 (extremal functions) | `13_transport_duality/extremizer_existence/` |

Theorem 5.1 combines the upper bound of Theorem 3.1 with the lower bound of Theorem 4.1. Each `verification/`
subfolder records the independent check of that proof.

## Certified data and Table 1

`data/` holds the interval certificates. The files used by Table 1 are:
- upper bounds: `explicit_bounds_intervals.json`, `local_projection_intervals.json`,
  `midpoint_split_certificate_{coarse,fine}.json`, `reflection_orbit_certificate_v2_{coarse,fine}.json`,
  `circle_composite_upper_fine.json`, `circle_composite_upper_n768.json`, `middle_composite_upper_n512.json` (built from
  `middle_circle_certificate_n512.json`, `cross_disk_certificate.json` and `far_circle_certificate_fine.json`; independent
  check `middle_composite_independent_check.json`), `local_circle_composite_a30.json`, `local_circle_composite_a50.json`, `local_circle_composite_a75.json`,
  `local_circle_composite_a90.json` (Theorem 3.7, built from
  `local_circle_chunks/`, `middle_circle_certificate_n512.json` and `far_circle_certificate_fine.json`; independent check
  `local_circle_composite_independent.json` and `local_circle_independent_checks.json`);
  the finer cross-disk certificates `05_team_audit/cross2048/source/cross_disk_certificate_2048.json` and
  `05_team_audit/cross4096/source/cross_disk_certificate_4096.json` with the recombined values in
  `05_team_audit/cross2048/recombination/verification/accepted.json` and `05_team_audit/cross4096/recombination/verification/accepted.json`, and the values of $D_\alpha$ after the saving of
  Theorem 3.9 in `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/symmetric_concavity/fourth_moment/numerical_values/accepted.json`,
  with the exact radial density in `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/numerical_values/accepted.json`
  and `.../exact_radial_density/cross4096_values/accepted.json` (the latter on the $4096^2$ cross-disk enclosure `05_team_audit/cross4096/`);
  the values of Theorem 5.7 with the sharper deficiencies in `08_improved_upper_bounds/explicit_second_term/sharp_deficiency/numerical_values/accepted.json`,
  with the exact exterior series in `08_improved_upper_bounds/explicit_second_term/tail_series/numerical_values/accepted.json`;
  the values of $D_\alpha$ after the saving of Theorem 3.10(a), (b) in
  `08_improved_upper_bounds/local_projection/strict_increment/larger_disks/optimal_axis_disks/numerical_values/accepted.json`,
  after the saving of Theorem 3.10(c) in
  `08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/numerical_values/accepted.json`,
  and after the saving of Theorem 3.10(d) (Table 1 and Theorem 5.7) in
  `08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/supplemental_disks/numerical_values/accepted.json`;
- lower bounds: `gated_lower_intervals.json`, `cusp_refinement_intervals.json`, `homogeneous_lower_intervals.json`,
  `structured_full_a_half.json`, `structured_layercake_certificate_fine.json`, `structured_shape_certificates/`;
- lower bounds for $D_\alpha$ only (Theorem 4.6): `finite_D_lower_a001.json`, `finite_D_lower_a01.json`,
  `finite_D_lower_a05.json`, `finite_D_lower_a10.json`, `finite_D_lower_a20.json`, `finite_D_lower_a30.json`, built from the
  corresponding `finite_projection_fine_*.json` files, `profile_constant_certificate.json` and
  `profile_constant_positive_certificate.json` (independent checks `finite_D_independent_checks.json`,
  `finite_small_D_independent_checks.json`, `finite_D_a30_independent_checks.json`). `geometric_profile_certificate.json` holds the
  sharper profile factors; `finite_D_lower_a30_geometric_fine.json` combines the factor $1.007$ with the finer $\alpha=0.3$
  integral (chunks in `finite_geometric_chunks/`, independent check `finite_D_geometric_independent.json`) and gives the
  Table 1 entry at $\alpha=0.3$; the coarser `finite_D_lower_a30_geometric.json` is superseded and not used;
- Theorem 9.1: `endpoint_ratio_certificates.json`.

Files in `data/retracted/` come from a version of the reflection-orbit program with a variable-shadowing error. They
are kept for the audit trail only and are not used anywhere.

To regenerate Table 1 from the certificates:

```sh
python3 scripts/make_table1.py data --report     # the table as printed in the report
python3 scripts/make_table1.py data              # the same, with the source family of each entry
```

The certificates record the SHA-256 hashes of their source files. When the artifacts were assembled, absolute folder names inside the copied
text files were rewritten as folder names relative to this directory; the recorded hashes refer to the files as they were
certified, so a hash check of a rewritten file reports a mismatch even though the computation is unchanged. A few lines
describing the local computing environment were also removed from one proof file. The files here are therefore reading copies:
a recorded hash identifies the unmodified original that was audited, not the copy in this folder, and it was not replaced by a
hash of the rewritten copy. Reproduction commands are given in the
`verification` records of the corresponding proof folders. The programs in `code/` need Python 3 with `python-flint`
(Arb ball arithmetic), `mpmath` and `numpy`. Worker counts are recorded in the command lines or certificates. Where recorded,
the `elapsed_seconds` field gives the run time; the fine certificates took between about 3 and 6 minutes each.

## Other folders

- `scripts/`: one-dimensional reductions and high-precision checks used in Section 5 (closed forms of the finite
  parts, the moment series $R_n$, the constant $C_0$), and `make_table1.py`.
- `10_finite_envelope_witness/`, `12_balanced_projection_witness/`: two further witness constructions for $D_\alpha$ whose
  admissibility proofs were checked but which gave no improved certified number (Section 10, item 2).
  `11_lattice_pole_constraints/` also contains such exploratory constructions besides the certified ones of Theorem 4.7.
- `05_team_audit/numerical_certificate_v2/` and `data/num_v2_polygon_comparison.json`: the independent second
  certification of the polygonal witness (Section 7, item 5).
- `numerics_code/`: the linear-programming and transport experiments of Section 7, and the numerical team's certifiers
  of the polygonal and lattice witnesses (`certify_lb.py`, `certify_lattice.py`, `certify_note14.py`, with the geometry module
  `zcurve.py`). The linear-programming and transport programs are numerical experiments, not proofs. Run them from
  `numerics_code/`, for example `python3 otlp.py --alpha 0.5 --beta 0.785398 --out ../numerics_data/example.json`.
- `numerics_data/`: inputs and outputs of those programs (JSON, parameter lists and the shell scripts with the exact command
  lines, written to be run from `numerics_code/`). The certified enclosures of the polygonal witness are in `numerics_data/cert2/`,
  those of the lattice witnesses in `numerics_data/n14/`; `python3 cert_table.py` in `numerics_code/` tabulates the former.
- `table1.md`: Table 1 with the source family of every entry.

## Scope of reproduction

The table commands above reconstruct the published table from the retained interval certificates. This recombination is
not a fresh replay of every interval computation. In particular, the finest lower certificates at exponents one half
and three quarters have complete structural audits and selected independent replays, as stated in the report.

Source snapshots and historical audit scripts retain references to original working records, report revisions and
run logs that are not included. They document the original audit; they are not standalone reproduction entry points.
Recorded historical hashes are preserved, including for scripts whose paths were corrected for this reading copy.

The packed files larger than 1 MB contain task manifests, cell data or detailed independent comparisons needed by
the documented certificate audits. An unused dense-envelope proposal larger than 1 MB has been omitted; the smaller
envelope inputs and diagnostic results supporting the report remain included.
