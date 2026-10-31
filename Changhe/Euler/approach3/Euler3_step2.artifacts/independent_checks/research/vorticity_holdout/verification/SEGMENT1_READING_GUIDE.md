# Segment-one independent vorticity comparisons

Reviewed 2026-10-29T13:27:06.295600+00:00.

These are finite-grid pressure-independent diagnostics at END CURRENT endpoints. The complete five-term vorticity residual, three normalization ratios, divergence, sampled maxima, axis caps, centered balls and finite-volume aggregation are specified in ../PROOF.md and SEGMENT1_COMMON_plan_v1.md. Neither quadrature level provides an enclosure.

## P1

Comparison SHA256 593a76e8cf6eb8c86194a2e9404d2d5675e088663430e41a404db8fd4763ebe1. All 492 comparison controls pass; INITIAL/FIXED/FREE audits pass 3994/4000/4000 controls.

| Family | Metric | INITIAL | FIXED | FREE | Largest level-change / FREE-FIXED difference |
|---|---|---:|---:|---:|---:|
| dyadic | rho_vorticity_max | 0.0697501279475 | 0.081211369744 | 0.0689276477003 | 0.0194922 |
| dyadic | sigma_vorticity_max | 0.565376859724 | 0.615464966831 | 0.606072456101 | 0.476435 |
| half_offset | rho_vorticity_max | 0.0686930488649 | 0.0805436364586 | 0.0655165337162 | 0.0171681 |
| half_offset | sigma_vorticity_max | 0.559466712751 | 0.6066732458 | 0.595781335827 | 0.720221 |
| physical_common | rho_vorticity_max | 0.0702122361853 | 0.0707939160372 | 0.0679128822121 | 0.17808 |
| physical_common | sigma_vorticity_max | 0.578194121412 | 0.627166120775 | 0.615922507573 | 0.42738 |
| registered_core_ball | rho_vorticity_max | 0.0599062772599 | 0.0799363387291 | 0.0591010385002 | 0.000146445 |
| registered_core_ball | sigma_vorticity_max | 0.275687864496 | 0.375415430253 | 0.272834594549 | 0.000114454 |
| origin_ball | rho_vorticity_max | 0.0625732967953 | 0.0819742607426 | 0.0609010775751 | 4.16644e-06 |
| origin_ball | sigma_vorticity_max | 0.28571326717 | 0.382342113524 | 0.279064408629 | 1.70307e-06 |
| unit_ball | rho_vorticity_max | 0.0580726268131 | 0.0614049571236 | 0.0573191222666 | 5.60828 |
| unit_ball | sigma_vorticity_max | 0.454117535692 | 0.51534484777 | 0.494648210176 | 12.5775 |
| finite_global_partition | rho_vorticity_max | 0.0697501279475 | 0.081211369744 | 0.0689276477003 | 0.0194922 |
| finite_global_partition | sigma_vorticity_max | 0.565376859724 | 0.615464966831 | 0.606072456101 | 0.476435 |
| axis_caps | rho_vorticity_max | 0.0812148994831 | 0.117938093043 | 0.109662361853 | 0.150999 |
| axis_caps | sigma_vorticity_max | 0.504737739546 | 0.505523339353 | 0.575445672036 | 0.331181 |
| centered_core_balls | rho_vorticity_max | 0.0639028324918 | 0.076942550235 | 0.0761939601982 | 0.0593522 |
| centered_core_balls | sigma_vorticity_max | 0.364363893686 | 0.411584885945 | 0.406173426757 | 0.317048 |
| finite_ball_r1024 | sigma_vorticity | 0.406301072984 | 0.458942620802 | 0.445781749565 | 0.399345 |

The final column is the sum of absolute coarse-to-fine changes of FREE and FIXED divided by their finer-level difference. Values above one leave a claimed difference unresolved by these two levels. Values below one are not an error bound. Centered core balls are state-specific; they do not define a common-domain comparison. The finite ball of radius1024 omits its exterior.

## P2

Comparison SHA256 091315c7a19557cc592b70cd9b8f8d4cf67c5ad7ff5d552c9161e4bd5fae4eef. All 498 comparison controls pass; INITIAL/FIXED/FREE audits pass 4041/4041/4041 controls.

| Family | Metric | INITIAL | FIXED | FREE | Largest level-change / FREE-FIXED difference |
|---|---|---:|---:|---:|---:|
| dyadic | rho_vorticity_max | 0.113603047604 | 0.108856213402 | 0.109234359438 | 33.2591 |
| dyadic | sigma_vorticity_max | 1.68537087205 | 1.75089229017 | 1.74633904832 | 0.635389 |
| half_offset | rho_vorticity_max | 0.100997873263 | 0.103295076119 | 0.102958515044 | 14.984 |
| half_offset | sigma_vorticity_max | 1.52300223782 | 1.58084530751 | 1.57929522261 | 1.06952 |
| physical_common | rho_vorticity_max | 0.0922646384623 | 0.0895261703887 | 0.0899086614923 | 18.9907 |
| physical_common | sigma_vorticity_max | 1.62822044876 | 1.66686174531 | 1.66299742524 | 0.171471 |
| registered_core_ball | rho_vorticity_max | 0.0165104122102 | 0.0173952216906 | 0.0179185548465 | 0.000188188 |
| registered_core_ball | sigma_vorticity_max | 0.38512298153 | 0.406636977456 | 0.418993294013 | 0.000105613 |
| origin_ball | rho_vorticity_max | 0.0165777060105 | 0.0174469800798 | 0.017991938388 | 5.46452e-06 |
| origin_ball | sigma_vorticity_max | 0.385956604562 | 0.407096073489 | 0.419934335361 | 1.55157e-06 |
| unit_ball | rho_vorticity_max | 0.125256740868 | 0.119067001362 | 0.119260859747 | 383.92 |
| unit_ball | sigma_vorticity_max | 1.06356528698 | 1.03691405627 | 1.03812823087 | 710.189 |
| finite_global_partition | rho_vorticity_max | 0.113603047604 | 0.108856213402 | 0.109234359438 | 33.2591 |
| finite_global_partition | sigma_vorticity_max | 1.68537087205 | 1.75089229017 | 1.74633904832 | 0.635389 |
| axis_caps | rho_vorticity_max | 0.10532611045 | 0.10692092802 | 0.107382756881 | 27.5666 |
| axis_caps | sigma_vorticity_max | 3.5885200794 | 3.6174240232 | 3.63242150986 | 3.11301 |
| centered_core_balls | rho_vorticity_max | 0.0437107633559 | 0.0428580291351 | 0.0427616847094 | 0.0405133 |
| centered_core_balls | sigma_vorticity_max | 0.704951707674 | 0.699489363299 | 0.702025985242 | 0.900605 |
| finite_ball_r1024 | sigma_vorticity | 1.22796490907 | 1.25503451894 | 1.25463664603 | 41.2161 |

The final column is the sum of absolute coarse-to-fine changes of FREE and FIXED divided by their finer-level difference. Values above one leave a claimed difference unresolved by these two levels. Values below one are not an error bound. Centered core balls are state-specific; they do not define a common-domain comparison. The finite ball of radius1024 omits its exterior.

P1 illustrates the distinction between ratios: FREE has lower dyadic rho_vorticity than FIXED, whereas both optimized members have higher dyadic sigma_vorticity and finite-ball sigma_vorticity than INITIAL. P2 changes are small and differ in sign across domains. No uniform improvement is established. The origin scalar consistency audits agree with the separate exact finite-field canonical intervals, but no Taylor-order or exact-Euler conclusion follows.
