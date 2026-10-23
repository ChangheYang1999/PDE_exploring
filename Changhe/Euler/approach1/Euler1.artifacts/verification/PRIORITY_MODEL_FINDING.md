# Priority representation finding

2026-10-23T06:22:24.263966+00:00. Inspected numerics model.py SHA256 f7d0c7c748fed6a94651a6b4f304849d102b6be1c8c858e1264091a5caa66c76 for forward reconstruction only. The independent residual implementation was written and unit-tested before this inspection; no trainer residual has been imported.

The default radial feature currently computes R=sqrt(sum(y*y)+1e-300), then asinh(R/l_in). At the origin its Hessian has entries 1e150 before the asinh/scale factors. For resolved nonzero radii it behaves like |y|, with a cusp at the effective numerical origin. Generic potential and pressure network dependence on this feature therefore lacks resolved Cartesian smoothness, and higher autodifferentiation can overflow. Zero initialization of the final layer only hides the issue until those weights change.

Please replace this radial input before training. A smooth radial input with comparable logarithmic far-field growth is 0.5*log1p(sum(y*y)/l_in**2)/xi_scale. It is quadratic near zero, smooth in Cartesian coordinates, and behaves like log(R/l_in)/xi_scale at large R. Alternatively disable the radial feature for the pilot. No arbitrary epsilon radius is needed. I will validate the actual saved representation after the correction is published.

Secondary documentation issue: seed_fields says scaling M scales pressure quadratically, but its code uses scale*M + scale**2*M**2 in P. Moreover, scaled M+scaled M**2 need not be symmetric for scale other than 0 or 1 and b different from c. This is allowed for an approximate initializer, but the scaled field is not the exact affine residual calibration family. Scaling M is not the true spatial gauge and changes vorticity amplitude.

Tail coverage issue to retain for later checks: coordinatewise asinh followed by tanh can saturate differently along different rays, and coordinate-plane transition layers can be missed by random angular samples. I will include axis and coordinate-plane strips at large radii in addition to generic directional tail tests. A correct nominal envelope exponent does not establish uniform angular tail regularity.

Reproducer executed independently with torch 2.13.0+cu130 on CPU/FP64: the current feature returns the finite but unresolved Hessian diag(3.333333333333333e149) at y=0; the smooth log1p feature returns diag(1/3). Exact results: evidence/radial_feature_regularization.json. No trainer module was imported.

The independent third-derivative follow-up is also retained in the same JSON. Its finiteness is False for the current feature and True for log1p. The Hessian itself is huge but finite in this installed PyTorch version; do not describe it as non-finite.


Repair confirmed at 2026-10-23T06:42:08.371108+00:00: the saved dir_log pilot and current published source use log1p(R²/l_in²)/xi_scale and bounded smooth directional inputs. Five independent synthetic decoder configurations, including this branch, pass. The origin issue above is historical for this repaired checkpoint. A different conditional far-field restriction is documented in research/radial-feature-tails/PROOF.md; smoothness at the origin does not settle tail flexibility.
