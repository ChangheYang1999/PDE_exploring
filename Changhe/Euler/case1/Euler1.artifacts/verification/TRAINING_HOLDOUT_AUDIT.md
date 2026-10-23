# Last-batch training/holdout audit

Date: 2026-10-23T07:39:54.658616+00:00. Verdict: CONFIRMED for this finite comparison; campaign-wide generalization remains OPEN.

Checkpoint SHA256: `2ed27e207ff9c68ecca7a1b60c7b7d52fc30b0aebb400fb3b45c50eec663eb3d`. This is v2 M1, c_l = 0.45, saved step 4476. The final stage-zero training batch was reconstructed by replaying the documented sampler from seed 2. All four holdout strata first reproduced bitwise, including their weights. The replayed training generator then matched the checkpoint generator state byte for byte after 4476 batches. Model, batch, sampler source and holdout hashes are recorded in `evidence/training-replay-2ed27e207ff9c68e.json`. No trainer module was imported.

Both sets were evaluated at the same saved model parameters with independent potential tangents and sixth-order physical finite differences at relative steps 0.002 and 0.001. The maximum relative change of all 24 regional ratios between step sizes is 3.95941269623e-08. Only disjoint core and shell importance weights enter physical-volume regional ratios. The separately oversampled axis and origin strata are diagnostic distributions.

| Region | Training points | Saved holdout points | Last-batch eps_m | Holdout eps_m | Holdout / batch |
|---|---|---|---|---|---|
| D1_R<1 | 100 | 61 | 0.1033323508 | 0.2160253524 | 2.0905878 |
| D2_1-3 | 2549 | 1658 | 0.07253264509 | 0.1153139745 | 1.5898217 |
| D3_3-10 | 4362 | 2970 | 0.01860996967 | 0.01940627393 | 1.0427891 |
| D4_10-100 | 2073 | 1445 | 0.002648269443 | 0.002569017495 | 0.97007406 |
| D5_100-1e3 | 2175 | 1407 | 4.236043894e-05 | 4.294788953e-05 | 1.0138679 |
| D6_1e3-1e5 | 1029 | 651 | 9.49636808e-07 | 8.972970916e-07 | 0.94488449 |

The R<1 comparison uses only 100 training and 61 holdout points and is sensitive to localized large errors. The unweighted core absolute residual RMS is 0.00597211 on the last batch and 0.01214858 on the saved holdout, a ratio of 2.03422; their sampled maxima are 0.31449 and 0.65619. The high quantiles and each stratum are retained in the full evidence JSON. This is an observed discrepancy at one checkpoint, not a population generalization bound or a statistic over every training batch. It does not identify overfitting as the unique cause. The saved holdout is reused by the trainer for checkpoint selection; it is not the independent final-audit set.

The fields were evaluated after the saved optimizer step, on both sets. These numbers are not compared to a logged pre-update loss or its amplitude penalty. Both sets fail the 1e-3 momentum screen in the inner regions, so the gap does not change the numerical rejection. At the nonlinear tail scale the D6 values are 14.019884 on the training batch and 14.107446 on the holdout.

Evidence: `evidence/training-holdout-gap-2ed27e207ff9c68e.json`, `evidence/training_holdout_gap_audit.json`. Reproduce with `python3 -B validation/replay_training_batch.py --help` and `python3 -B validation/training_holdout_gap.py evidence/training-replay-2ed27e207ff9c68e.json`, using one CPU thread.
