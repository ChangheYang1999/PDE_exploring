
### case S20_own (file gates_gpu_v1_S20_own.json; precision dd_fp64jac; device NVIDIA A100-SXM4-80GB; pair [0.45, 1.0]; n_opt 2921; rows 433009; cost 2.45525786477736e-07; wall 3264 s)
summary: {"G1_Jf": true, "G1_Jcw_production": true, "G1_Jc": true, "G1_coef_Jf": true, "G1_coef_Jcw": true, "G1_coef_Jc": true, "G2a": true, "G2c": true, "G4a": true, "G4b": true, "G3": false, "G5a": true, "G5b": true}

| test | direction / item | second-order errors per step | Richardson | verdict |
|---|---|---|---|---|
| G1 J_f parameter columns | optimizer:z_c | 1e-03:8.5e-08 1e-04:8.4e-10 1e-05:2.2e-11 1e-06:3.0e-10 1e-07:2.1e-09 | 5.5e-12 | PASS |
| G1 J_f parameter columns | optimizer:z_w | 1e-03:6.6e-07 1e-04:6.6e-09 1e-05:5.2e-10 1e-06:3.7e-09 1e-07:2.5e-08 | 5.0e-12 | PASS |
| G1 J_f parameter columns | physical:c_l | 1e-03:2.2e-06 1e-04:2.2e-08 1e-05:2.2e-10 1e-06:4.9e-11 1e-07:2.2e-10 | 2.0e-12 | PASS |
| G1 J_f parameter columns | physical:omega | 1e-03:9.2e-08 1e-04:9.2e-10 1e-05:1.9e-10 1e-06:3.7e-09 1e-07:6.0e-08 | 2.2e-12 | PASS |
| G1 J_cw (production) parameter columns | optimizer:z_c | 1e-03:8.5e-08 1e-04:8.4e-10 1e-05:2.2e-11 1e-06:3.0e-10 1e-07:2.1e-09 | 5.5e-12 | PASS |
| G1 J_cw (production) parameter columns | optimizer:z_w | 1e-03:6.6e-07 1e-04:6.6e-09 1e-05:5.2e-10 1e-06:3.7e-09 1e-07:2.5e-08 | 5.0e-12 | PASS |
| G1 J_cw (production) parameter columns | physical:c_l | 1e-03:2.2e-06 1e-04:2.2e-08 1e-05:2.2e-10 1e-06:4.9e-11 1e-07:2.2e-10 | 2.0e-12 | PASS |
| G1 J_cw (production) parameter columns | physical:omega | 1e-03:9.3e-08 1e-04:9.3e-10 1e-05:1.9e-10 1e-06:3.7e-09 1e-07:6.0e-08 | 2.2e-12 | PASS |
| G1 J_c parameter columns | optimizer:z_c | 1e-03:8.5e-08 1e-04:8.4e-10 1e-05:2.2e-11 1e-06:3.0e-10 1e-07:2.1e-09 | 5.5e-12 | PASS |
| G1 J_c parameter columns | optimizer:z_w | 1e-03:6.6e-07 1e-04:6.6e-09 1e-05:5.2e-10 1e-06:3.7e-09 1e-07:2.5e-08 | 5.0e-12 | PASS |
| G1 J_c parameter columns | physical:c_l | 1e-03:2.2e-06 1e-04:2.2e-08 1e-05:2.2e-10 1e-06:4.9e-11 1e-07:2.2e-10 | 2.0e-12 | PASS |
| G1 J_c parameter columns | physical:omega | 1e-03:9.3e-08 1e-04:9.3e-10 1e-05:1.9e-10 1e-06:3.7e-09 1e-07:6.0e-08 | 2.2e-12 | PASS |
| G1 J_f coefficient columns | 20 columns | | | 20/20 PASS; all_pass True |
| G1 J_cw coefficient columns | 20 columns | | | 20/20 PASS; all_pass True |
| G1 J_c coefficient columns | 20 columns | | | 20/20 PASS; all_pass True |
| G2 | G2a_identity_c_l | {"near_origin(r<=0.1R0)": 5.67818402522847e-17, "core_intermediate": 1.0597096362672309e-16, "far(r>256R0)": 4.601891722 | n/a | PASS |
| G2 | G2c_Up_DUp_c_l | {"1e-03": {"near_origin(r<=0.1R0)": 4.808907365566759e-06, "core_intermediate": 9.30839546176734e-06, "far(r>256R0)": 0. | n/a | PASS |
| G2 | G2a_identity_omega | {"near_origin(r<=0.1R0)": 5.5177735525439534e-17, "core_intermediate": 1.4877542626346907e-16, "far(r>256R0)": 3.2785935 | n/a | PASS |
| G2 | G2c_Up_DUp_omega | {"1e-03": {"near_origin(r<=0.1R0)": 1.0295455807768463e-10, "core_intermediate": 4.377415578676286e-06, "far(r>256R0)":  | n/a | PASS |
| G4 | G4a_gradP_c_l | {"1e-03": {"near_origin(r<=0.1R0)": 2.8827980872287588e-05, "core_intermediate": 2.9784136431360497e-05, "far(r>256R0)": | n/a | PASS |
| G4 | G4b_source_c_l | {"rel": 8.548857846221014e-17, "PASS": true} | n/a | PASS |
| G4 | G4a_gradP_omega | {"1e-03": {"near_origin(r<=0.1R0)": 3.6394019114172573e-07, "core_intermediate": 2.2768990291433476e-06, "far(r>256R0)": | n/a | PASS |
| G4 | G4b_source_omega | {"rel": 8.131727978514096e-17, "PASS": true} | n/a | PASS |
| G3 complete gradient | e_zc(optimizer) | 1e-03:6.6e-01 1e-04:6.6e-03 1e-05:6.6e-05 1e-06:7.0e-07 1e-07:2.6e-08 | 2.0e-08 | PASS (absolute_only) |
| G3 complete gradient | e_zw(optimizer) | 1e-03:1.0e+00 1e-04:2.2e-02 1e-05:2.2e-04 1e-06:2.2e-06 1e-07:1.8e-08 | n/a | FAIL |
| G3 complete gradient | random_scaled_0 | 1e-03:1.0e+00 1e-04:1.6e+00 1e-05:1.6e-02 1e-06:1.6e-04 1e-07:1.6e-06 | n/a | FAIL |
| G3 complete gradient | random_scaled_1 | 1e-03:9.9e-01 1e-04:6.3e-01 1e-05:1.7e-02 1e-06:1.7e-04 1e-07:1.7e-06 | n/a | FAIL |
| G3 complete gradient | random_scaled_2 | 1e-03:9.9e-01 1e-04:6.1e-01 1e-05:1.5e-02 1e-06:1.5e-04 1e-07:1.5e-06 | n/a | FAIL |
| G3 complete gradient | mixed_0 | 1e-03:1.0e+00 1e-04:1.1e+00 1e-05:1.6e-01 1e-06:1.6e-03 1e-07:1.6e-05 | n/a | FAIL |
| G3 complete gradient | mixed_1 | 1e-03:1.0e+00 1e-04:8.6e-01 1e-05:5.6e-02 1e-06:5.9e-04 1e-07:5.9e-06 | n/a | FAIL |
| G3 complete gradient | e_c_l(physical) | 1e-03:1.0e+00 1e-04:1.0e+00 1e-05:1.1e-01 1e-06:1.1e-03 1e-07:1.1e-05 | n/a | FAIL |
| G3 complete gradient | e_omega(physical) | 1e-03:1.1e+00 1e-04:1.1e-02 1e-05:1.1e-04 1e-06:1.1e-06 1e-07:7.6e-09 | n/a | FAIL |
| G5a spatial FD vs DU (best relative per group) | | {"near_origin(r<=0.1R0)": 1.7067035606252468e-10, "core_intermediate": 3.634012366704619e-10, "far(r>256R0)": 4.22985692 | | PASS |
| G5b divergence | | {'U': 8.997284162624386e-16, 'U_c': 1.6988928847484896e-15, 'U_w': 1.4173895204585276e-15} | | PASS |
| G5c source consistency | | 0.0 | | see entrywise test |

wall: G1 2268 s, G2+G4 42 s, G3 518 s, G5 425 s
