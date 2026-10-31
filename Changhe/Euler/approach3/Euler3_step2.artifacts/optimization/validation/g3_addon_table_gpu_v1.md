### G3 at S01_own (record g3_addon_gpu_v1_S01_own.json; cost 2.7248e-07; nine directions, seven valid steps each)

| direction | registered five-step O1 (specification 3.5) | seven-step O1 (post-result step rule, 3.0 (b') (2)) | seven-step gauge-subtracted estimator (3.0 (b') (3)) | five-step gauge-subtracted | release label |
|---|---|---|---|---|---|
| e_zc(optimizer) | PASS(abs_only) (R 4.3e-08) | PASS(abs_only) (R 1.5e-08) | PASS (R 1.0e-11) | PASS (R 1.0e-11) | registered PASS (absolute-only) |
| e_zw(optimizer) | FAIL | PASS(abs_only) (R 1.0e-09) | PASS (R 2.9e-12) | PASS (R 2.9e-12) | pass under the post-result step rule (absolute-only) |
| random_scaled_0 | FAIL | FAIL | PASS (R 2.4e-07) | FAIL | pass under the post-result gauge-subtracted estimator |
| random_scaled_1 | FAIL | PASS (R 1.0e-07) | PASS (R 1.2e-08) | PASS (R 1.2e-08) | pass under the post-result step rule |
| random_scaled_2 | FAIL | PASS (R 6.5e-08) | PASS (R 6.5e-08) | FAIL | pass under the post-result step rule |
| mixed_0 | FAIL | PASS (R 1.2e-08) | PASS(abs_only) (R 2.9e-08) | FAIL | pass under the post-result step rule |
| mixed_1 | FAIL | PASS (R 1.2e-08) | PASS (R 7.4e-09) | PASS (R 7.4e-09) | pass under the post-result step rule |
| e_c_l(physical) | FAIL | PASS(abs_only) (R 5.6e-08) | PASS (R 4.8e-11) | PASS (R 4.8e-11) | pass under the post-result step rule (absolute-only) |
| e_omega(physical) | FAIL | PASS(abs_only) (R 1.3e-09) | PASS (R 3.8e-13) | PASS (R 3.8e-13) | pass under the post-result step rule (absolute-only) |

Counts: registered five-step O1 1 of 9; seven-step O1 8 of 9; seven-step gauge-subtracted 9 of 9; five-step gauge-subtracted 6 of 9. PASS = relative rule with two consecutive passing steps and Richardson; PASS(abs_only) = passes only against the absolute floor; FAIL = no two consecutive passing steps.

### G3 at S09_own (record g3_addon_gpu_v1_S09_own.json; cost 3.5632e-07; nine directions, seven valid steps each)

| direction | registered five-step O1 (specification 3.5) | seven-step O1 (post-result step rule, 3.0 (b') (2)) | seven-step gauge-subtracted estimator (3.0 (b') (3)) | five-step gauge-subtracted | release label |
|---|---|---|---|---|---|
| e_zc(optimizer) | PASS(abs_only) (R 3.5e-08) | PASS(abs_only) (R 2.3e-08) | PASS (R 5.9e-11) | PASS (R 5.9e-11) | registered PASS (absolute-only) |
| e_zw(optimizer) | PASS(abs_only) (R 1.3e-08) | PASS (R 1.3e-08) | PASS (R 1.1e-13) | PASS (R 1.1e-13) | registered PASS (absolute-only) |
| random_scaled_0 | FAIL | PASS (R 2.7e-09) | PASS (R 1.8e-10) | PASS (R 1.8e-10) | pass under the post-result step rule |
| random_scaled_1 | FAIL | PASS (R 6.3e-08) | PASS (R 1.1e-09) | PASS (R 4.7e-09) | pass under the post-result step rule |
| random_scaled_2 | FAIL | PASS (R 1.5e-07) | PASS (R 2.0e-07) | FAIL | pass under the post-result step rule |
| mixed_0 | FAIL | PASS (R 1.8e-09) | PASS (R 5.2e-10) | PASS (R 5.2e-10) | pass under the post-result step rule |
| mixed_1 | FAIL | PASS (R 7.5e-09) | PASS (R 1.7e-09) | PASS (R 1.7e-09) | pass under the post-result step rule |
| e_c_l(physical) | FAIL | PASS(abs_only) (R 7.1e-08) | PASS (R 7.2e-11) | PASS (R 7.2e-11) | pass under the post-result step rule (absolute-only) |
| e_omega(physical) | PASS(abs_only) (R 2.1e-09) | PASS(abs_only) (R 2.1e-09) | PASS (R 2.4e-13) | PASS (R 2.4e-13) | registered PASS (absolute-only) |

Counts: registered five-step O1 3 of 9; seven-step O1 9 of 9; seven-step gauge-subtracted 9 of 9; five-step gauge-subtracted 8 of 9. PASS = relative rule with two consecutive passing steps and Richardson; PASS(abs_only) = passes only against the absolute floor; FAIL = no two consecutive passing steps.

### G3 at S05_own (record g3_addon_gpu_v1_S05_own.json; cost 3.0962e-07; nine directions, seven valid steps each)

| direction | registered five-step O1 (specification 3.5) | seven-step O1 (post-result step rule, 3.0 (b') (2)) | seven-step gauge-subtracted estimator (3.0 (b') (3)) | five-step gauge-subtracted | release label |
|---|---|---|---|---|---|
| e_zc(optimizer) | PASS(abs_only) (R 3.9e-09) | PASS(abs_only) (R 3.9e-09) | PASS (R 2.2e-11) | PASS (R 2.2e-11) | registered PASS (absolute-only) |
| e_zw(optimizer) | FAIL | PASS(abs_only) (R 5.2e-08) | PASS(abs_only) (R 2.5e-10) | PASS(abs_only) (R 2.5e-10) | pass under the post-result step rule (absolute-only) |
| random_scaled_0 | FAIL | FAIL | PASS(abs_only) (R 4.2e-08) | PASS(abs_only) (R 2.4e-07) | pass under the post-result gauge-subtracted estimator (absolute-only) |
| random_scaled_1 | FAIL | PASS(abs_only) (R 2.2e-07) | PASS (R 3.9e-08) | PASS (R 3.9e-08) | pass under the post-result step rule (absolute-only) |
| random_scaled_2 | FAIL | PASS (R 2.4e-07) | PASS (R 2.4e-07) | FAIL | pass under the post-result step rule |
| mixed_0 | FAIL | FAIL | PASS (R 2.5e-07) | FAIL | pass under the post-result gauge-subtracted estimator |
| mixed_1 | FAIL | PASS (R 5.5e-07) | PASS (R 4.6e-08) | PASS (R 4.6e-08) | pass under the post-result step rule |
| e_c_l(physical) | FAIL | PASS(abs_only) (R 7.9e-09) | PASS (R 6.5e-11) | PASS (R 6.5e-11) | pass under the post-result step rule (absolute-only) |
| e_omega(physical) | PASS(abs_only) (R 2.9e-09) | PASS(abs_only) (R 2.9e-09) | PASS (R 6.4e-12) | PASS (R 6.4e-12) | registered PASS (absolute-only) |

Counts: registered five-step O1 2 of 9; seven-step O1 7 of 9; seven-step gauge-subtracted 9 of 9; five-step gauge-subtracted 7 of 9. PASS = relative rule with two consecutive passing steps and Richardson; PASS(abs_only) = passes only against the absolute floor; FAIL = no two consecutive passing steps.

### G3 at manu_large_omega (record g3_addon_gpu_v1_manu_large_omega.json; cost 1.7762e-02; nine directions, seven valid steps each)

| direction | registered five-step O1 (specification 3.5) | seven-step O1 (post-result step rule, 3.0 (b') (2)) | seven-step gauge-subtracted estimator (3.0 (b') (3)) | five-step gauge-subtracted | release label |
|---|---|---|---|---|---|
| e_zc(optimizer) | PASS (R 2.9e-10) | PASS (R 2.9e-10) | PASS (R 7.7e-12) | PASS (R 7.7e-12) | registered PASS |
| e_zw(optimizer) | PASS (R 1.4e-11) | PASS (R 1.4e-11) | PASS (R 3.7e-13) | PASS (R 3.7e-13) | registered PASS |
| random_scaled_0 | FAIL | FAIL | PASS (R 2.4e-07) | PASS (R 2.4e-07) | pass under the post-result gauge-subtracted estimator |
| random_scaled_1 | PASS (R 2.0e-08) | PASS (R 2.0e-08) | PASS (R 8.0e-10) | PASS (R 8.0e-10) | registered PASS |
| random_scaled_2 | PASS (R 9.5e-07) | PASS (R 9.5e-07) | PASS (R 2.6e-08) | PASS (R 2.6e-08) | registered PASS |
| mixed_0 | FAIL | FAIL | PASS (R 2.4e-07) | PASS (R 2.4e-07) | pass under the post-result gauge-subtracted estimator |
| mixed_1 | PASS (R 2.5e-07) | PASS (R 2.5e-07) | PASS (R 7.1e-08) | PASS (R 7.1e-08) | registered PASS |
| e_c_l(physical) | PASS (R 7.9e-11) | PASS (R 7.9e-11) | PASS (R 2.8e-13) | PASS (R 2.8e-13) | registered PASS |
| e_omega(physical) | PASS (R 3.6e-12) | PASS (R 3.6e-12) | PASS (R 3.7e-12) | PASS (R 3.7e-12) | registered PASS |

Counts: registered five-step O1 7 of 9; seven-step O1 7 of 9; seven-step gauge-subtracted 9 of 9; five-step gauge-subtracted 9 of 9. PASS = relative rule with two consecutive passing steps and Richardson; PASS(abs_only) = passes only against the absolute floor; FAIL = no two consecutive passing steps.

