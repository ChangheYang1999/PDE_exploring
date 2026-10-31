
### case S01_shift_a (file gates_gpu_v1_S01_shift_a.json; precision dd_fp64jac; device NVIDIA A100-SXM4-80GB; pair [0.42, 0.3]; n_opt 1469; rows 433009; cost 182.2150936146346; wall 3252 s)
summary: {"G1_Jf": false, "G1_Jcw_production": false, "G1_Jc": false, "G1_coef_Jf": false, "G1_coef_Jcw": false, "G1_coef_Jc": false, "G2a": true, "G2c": true, "G4a": true, "G4b": true, "G3": true, "G5a": true, "G5b": true}

| test | direction / item | second-order errors per step | Richardson | verdict |
|---|---|---|---|---|
| G1 J_f parameter columns | optimizer:z_c | 1e-03:1.9e-08 1e-04:1.8e-10 1e-05:5.7e-11 1e-06:7.8e-10 1e-07:2.9e-08 | 9.0e-12 | FAIL |
| G1 J_f parameter columns | optimizer:z_w | 1e-03:6.6e-07 1e-04:6.5e-09 1e-05:1.2e-09 1e-06:1.3e-08 1e-07:1.5e-07 | 1.4e-10 | PASS |
| G1 J_f parameter columns | physical:c_l | 1e-03:2.5e-06 1e-04:2.5e-08 1e-05:2.5e-10 1e-06:2.7e-11 1e-07:1.9e-10 | 2.7e-12 | PASS |
| G1 J_f parameter columns | physical:omega | 1e-03:2.1e-08 1e-04:2.8e-10 1e-05:1.0e-09 1e-06:9.3e-09 1e-07:1.5e-07 | 1.7e-10 | PASS |
| G1 J_cw (production) parameter columns | optimizer:z_c | 1e-03:1.9e-08 1e-04:1.8e-10 1e-05:5.7e-11 1e-06:7.8e-10 1e-07:2.9e-08 | 9.1e-12 | FAIL |
| G1 J_cw (production) parameter columns | optimizer:z_w | 1e-03:6.6e-07 1e-04:6.5e-09 1e-05:1.2e-09 1e-06:1.3e-08 1e-07:1.5e-07 | 1.4e-10 | PASS |
| G1 J_cw (production) parameter columns | physical:c_l | 1e-03:2.5e-06 1e-04:2.5e-08 1e-05:2.5e-10 1e-06:2.7e-11 1e-07:1.9e-10 | 2.7e-12 | PASS |
| G1 J_cw (production) parameter columns | physical:omega | 1e-03:2.1e-08 1e-04:2.8e-10 1e-05:1.0e-09 1e-06:9.3e-09 1e-07:1.5e-07 | 1.7e-10 | PASS |
| G1 J_c parameter columns | optimizer:z_c | 1e-03:1.9e-08 1e-04:1.8e-10 1e-05:5.7e-11 1e-06:7.8e-10 1e-07:2.9e-08 | 9.1e-12 | FAIL |
| G1 J_c parameter columns | optimizer:z_w | 1e-03:6.6e-07 1e-04:6.5e-09 1e-05:1.2e-09 1e-06:1.3e-08 1e-07:1.5e-07 | 1.4e-10 | PASS |
| G1 J_c parameter columns | physical:c_l | 1e-03:2.5e-06 1e-04:2.5e-08 1e-05:2.5e-10 1e-06:2.7e-11 1e-07:1.9e-10 | 2.7e-12 | PASS |
| G1 J_c parameter columns | physical:omega | 1e-03:2.1e-08 1e-04:2.8e-10 1e-05:1.0e-09 1e-06:9.3e-09 1e-07:1.5e-07 | 1.7e-10 | PASS |
| G1 J_f coefficient columns | 20 columns | | | 19/20 PASS; all_pass False |
| G1 J_cw coefficient columns | 20 columns | | | 19/20 PASS; all_pass False |
| G1 J_c coefficient columns | 20 columns | | | 19/20 PASS; all_pass False |
| G2 | G2a_identity_c_l | {"near_origin(r<=0.1R0)": 2.1653423002306958e-17, "core_intermediate": 1.1506544405952934e-16, "far(r>256R0)": 4.0387192 | n/a | PASS |
| G2 | G2c_Up_DUp_c_l | {"1e-03": {"near_origin(r<=0.1R0)": 5.510503334929023e-06, "core_intermediate": 3.16197048653638e-06, "far(r>256R0)": 0. | n/a | PASS |
| G2 | G2a_identity_omega | {"near_origin(r<=0.1R0)": 1.4501788651642665e-17, "core_intermediate": 1.5573069463578898e-16, "far(r>256R0)": 2.3754069 | n/a | PASS |
| G2 | G2c_Up_DUp_omega | {"1e-03": {"near_origin(r<=0.1R0)": 1.1036768438323666e-10, "core_intermediate": 3.7134519899145434e-07, "far(r>256R0)": | n/a | PASS |
| G4 | G4a_gradP_c_l | {"1e-03": {"near_origin(r<=0.1R0)": 1.3224404679539101e-05, "core_intermediate": 3.0656967861600475e-05, "far(r>256R0)": | n/a | PASS |
| G4 | G4b_source_c_l | {"rel": 6.848066959940304e-17, "PASS": true} | n/a | PASS |
| G4 | G4a_gradP_omega | {"1e-03": {"near_origin(r<=0.1R0)": 4.116324205796168e-08, "core_intermediate": 1.2450676465468848e-07, "far(r>256R0)":  | n/a | PASS |
| G4 | G4b_source_omega | {"rel": 7.196042394104527e-17, "PASS": true} | n/a | PASS |
| G3 complete gradient | e_zc(optimizer) | 1e-03:1.4e-07 1e-04:1.4e-09 1e-05:6.7e-11 1e-06:7.1e-10 1e-07:3.0e-08 | 7.4e-12 | PASS |
| G3 complete gradient | e_zw(optimizer) | 1e-03:6.5e-07 1e-04:6.4e-09 1e-05:7.7e-10 1e-06:1.5e-08 1e-07:1.5e-07 | 1.1e-10 | PASS |
| G3 complete gradient | random_scaled_0 | 1e-03:5.9e-04 1e-04:5.9e-06 1e-05:5.9e-08 1e-06:5.5e-09 1e-07:9.7e-08 | 6.1e-09 | PASS |
| G3 complete gradient | random_scaled_1 | 1e-03:4.4e-04 1e-04:4.4e-06 1e-05:4.3e-08 1e-06:2.4e-08 1e-07:4.0e-07 | 2.5e-08 | PASS |
| G3 complete gradient | random_scaled_2 | 1e-03:1.8e-03 1e-04:1.8e-05 1e-05:1.8e-07 1e-06:1.2e-08 1e-07:9.9e-07 | 1.1e-08 | PASS |
| G3 complete gradient | mixed_0 | 1e-03:3.3e-04 1e-04:3.3e-06 1e-05:3.4e-08 1e-06:1.8e-08 1e-07:4.8e-08 | 1.7e-08 | PASS |
| G3 complete gradient | mixed_1 | 1e-03:2.0e-05 1e-04:2.0e-07 1e-05:2.8e-09 1e-06:2.8e-09 1e-07:2.2e-08 | 7.9e-10 | PASS |
| G3 complete gradient | e_c_l(physical) | 1e-03:4.2e-05 1e-04:4.2e-07 1e-05:4.2e-09 1e-06:5.9e-11 1e-07:2.0e-10 | 2.9e-12 | PASS |
| G3 complete gradient | e_omega(physical) | 1e-03:7.8e-09 1e-04:2.5e-10 1e-05:1.7e-09 1e-06:6.3e-09 1e-07:1.5e-07 | 1.7e-10 | PASS |
| G5a spatial FD vs DU (best relative per group) | | {"near_origin(r<=0.1R0)": 1.6863266423968264e-10, "core_intermediate": 2.97868664467777e-10, "far(r>256R0)": 2.546068040 | | PASS |
| G5b divergence | | {'U': 1.9819820888633496e-15, 'U_c': 1.6280424006698558e-15, 'U_w': 6.258749041759669e-16} | | PASS |
| G5c source consistency | | 0.0 | | see entrywise test |

wall: G1 2495 s, G2+G4 37 s, G3 447 s, G5 266 s

### case S05_shift_c (file gates_gpu_v1_S05_shift_c.json; precision dd_fp64jac; device NVIDIA A100-SXM4-80GB; pair [0.45, 1.0]; n_opt 1469; rows 433009; cost 18.43902094780627; wall 2944 s)
summary: {"G1_Jf": false, "G1_Jcw_production": false, "G1_Jc": false, "G1_coef_Jf": true, "G1_coef_Jcw": true, "G1_coef_Jc": true, "G2a": true, "G2c": true, "G4a": true, "G4b": true, "G3": true, "G5a": true, "G5b": true}

| test | direction / item | second-order errors per step | Richardson | verdict |
|---|---|---|---|---|
| G1 J_f parameter columns | optimizer:z_c | 1e-03:8.5e-08 1e-04:8.4e-10 1e-05:1.8e-11 1e-06:2.9e-10 1e-07:1.1e-08 | 5.3e-12 | FAIL |
| G1 J_f parameter columns | optimizer:z_w | 1e-03:5.5e-07 1e-04:5.5e-09 1e-05:9.1e-12 1e-06:5.2e-10 1e-07:3.4e-10 | 3.1e-12 | PASS |
| G1 J_f parameter columns | physical:c_l | 1e-03:2.1e-06 1e-04:2.1e-08 1e-05:2.0e-10 1e-06:4.9e-11 1e-07:4.3e-10 | 2.7e-12 | FAIL |
| G1 J_f parameter columns | physical:omega | 1e-03:7.4e-08 1e-04:7.5e-10 1e-05:9.0e-12 1e-06:3.4e-10 1e-07:3.4e-10 | 1.9e-12 | PASS |
| G1 J_cw (production) parameter columns | optimizer:z_c | 1e-03:8.5e-08 1e-04:8.4e-10 1e-05:1.8e-11 1e-06:3.3e-10 1e-07:1.1e-08 | 5.4e-12 | FAIL |
| G1 J_cw (production) parameter columns | optimizer:z_w | 1e-03:5.5e-07 1e-04:5.5e-09 1e-05:9.1e-12 1e-06:5.2e-10 1e-07:3.4e-10 | 3.4e-12 | PASS |
| G1 J_cw (production) parameter columns | physical:c_l | 1e-03:2.1e-06 1e-04:2.1e-08 1e-05:2.0e-10 1e-06:4.9e-11 1e-07:4.3e-10 | 2.7e-12 | FAIL |
| G1 J_cw (production) parameter columns | physical:omega | 1e-03:7.4e-08 1e-04:7.4e-10 1e-05:9.1e-12 1e-06:3.4e-10 1e-07:3.4e-10 | 2.4e-12 | PASS |
| G1 J_c parameter columns | optimizer:z_c | 1e-03:8.5e-08 1e-04:8.4e-10 1e-05:1.8e-11 1e-06:3.3e-10 1e-07:1.1e-08 | 5.4e-12 | FAIL |
| G1 J_c parameter columns | optimizer:z_w | 1e-03:5.5e-07 1e-04:5.5e-09 1e-05:9.1e-12 1e-06:5.2e-10 1e-07:3.4e-10 | 3.4e-12 | PASS |
| G1 J_c parameter columns | physical:c_l | 1e-03:2.1e-06 1e-04:2.1e-08 1e-05:2.0e-10 1e-06:4.9e-11 1e-07:4.3e-10 | 2.7e-12 | FAIL |
| G1 J_c parameter columns | physical:omega | 1e-03:7.4e-08 1e-04:7.4e-10 1e-05:9.1e-12 1e-06:3.4e-10 1e-07:3.4e-10 | 2.4e-12 | PASS |
| G1 J_f coefficient columns | 20 columns | | | 20/20 PASS; all_pass True |
| G1 J_cw coefficient columns | 20 columns | | | 20/20 PASS; all_pass True |
| G1 J_c coefficient columns | 20 columns | | | 20/20 PASS; all_pass True |
| G2 | G2a_identity_c_l | {"near_origin(r<=0.1R0)": 3.933552198650274e-17, "core_intermediate": 1.063906643454923e-16, "far(r>256R0)": 2.268509880 | n/a | PASS |
| G2 | G2c_Up_DUp_c_l | {"1e-03": {"near_origin(r<=0.1R0)": 4.809388572056496e-06, "core_intermediate": 1.9770280060559662e-05, "far(r>256R0)":  | n/a | PASS |
| G2 | G2a_identity_omega | {"near_origin(r<=0.1R0)": 4.769647178149225e-18, "core_intermediate": 1.3832468728853195e-16, "far(r>256R0)": 2.11378525 | n/a | PASS |
| G2 | G2c_Up_DUp_omega | {"1e-03": {"near_origin(r<=0.1R0)": 2.590831449636786e-10, "core_intermediate": 3.727414213291104e-06, "far(r>256R0)": 0 | n/a | PASS |
| G4 | G4a_gradP_c_l | {"1e-03": {"near_origin(r<=0.1R0)": 5.572016347883869e-05, "core_intermediate": 3.265982091010856e-05, "far(r>256R0)": 0 | n/a | PASS |
| G4 | G4b_source_c_l | {"rel": 8.555115925534645e-17, "PASS": true} | n/a | PASS |
| G4 | G4a_gradP_omega | {"1e-03": {"near_origin(r<=0.1R0)": 1.298260303202845e-06, "core_intermediate": 3.974454099918066e-06, "far(r>256R0)": 0 | n/a | PASS |
| G4 | G4b_source_omega | {"rel": 8.050066263814343e-17, "PASS": true} | n/a | PASS |
| G3 complete gradient | e_zc(optimizer) | 1e-03:9.3e-09 1e-04:8.8e-11 1e-05:5.2e-12 1e-06:2.7e-10 1e-07:1.1e-08 | 4.4e-12 | PASS |
| G3 complete gradient | e_zw(optimizer) | 1e-03:2.6e-06 1e-04:2.6e-08 1e-05:1.9e-10 1e-06:4.9e-10 1e-07:6.4e-10 | 6.3e-11 | PASS |
| G3 complete gradient | random_scaled_0 | 1e-03:1.3e-03 1e-04:1.3e-05 1e-05:1.4e-07 1e-06:8.0e-08 1e-07:1.1e-06 | 7.9e-08 | PASS |
| G3 complete gradient | random_scaled_1 | 1e-03:1.2e-03 1e-04:1.2e-05 1e-05:1.2e-07 1e-06:3.7e-09 1e-07:2.8e-07 | 5.0e-09 | PASS |
| G3 complete gradient | random_scaled_2 | 1e-03:1.3e-04 1e-04:1.3e-06 1e-05:1.7e-08 1e-06:4.0e-08 1e-07:5.3e-07 | 4.1e-08 | PASS |
| G3 complete gradient | mixed_0 | 1e-03:1.4e-04 1e-04:1.4e-06 1e-05:1.3e-08 1e-06:3.4e-08 1e-07:3.3e-07 | 3.4e-08 | PASS |
| G3 complete gradient | mixed_1 | 1e-03:5.4e-05 1e-04:5.4e-07 1e-05:1.1e-08 1e-06:4.4e-08 1e-07:2.7e-07 | 5.5e-09 | PASS |
| G3 complete gradient | e_c_l(physical) | 1e-03:1.2e-04 1e-04:1.2e-06 1e-05:1.2e-08 1e-06:7.1e-11 1e-07:4.2e-10 | 4.8e-11 | PASS |
| G3 complete gradient | e_omega(physical) | 1e-03:8.8e-07 1e-04:8.8e-09 1e-05:8.5e-11 1e-06:3.4e-10 1e-07:6.4e-10 | 2.0e-12 | PASS |
| G5a spatial FD vs DU (best relative per group) | | {"near_origin(r<=0.1R0)": 3.171525837815206e-10, "core_intermediate": 3.0509141059312945e-10, "far(r>256R0)": 5.47316412 | | PASS |
| G5b divergence | | {'U': 2.657851708472192e-15, 'U_c': 1.6917981332741038e-15, 'U_w': 1.2823634792559223e-15} | | PASS |
| G5c source consistency | | 0.0 | | see entrywise test |

wall: G1 2248 s, G2+G4 32 s, G3 387 s, G5 270 s

### case manu_small_omega (file gates_gpu_v1_manu_small_omega.json; precision dd_fp64jac; device NVIDIA A100-SXM4-80GB; pair [0.44, 0.05]; n_opt 1469; rows 433009; cost 0.23146061619311312; wall 2706 s)
summary: {"G1_Jf": true, "G1_Jcw_production": true, "G1_Jc": true, "G1_coef_Jf": false, "G1_coef_Jcw": false, "G1_coef_Jc": false, "G2a": true, "G2c": true, "G4a": true, "G4b": true, "G3": true, "G5a": true, "G5b": true}

| test | direction / item | second-order errors per step | Richardson | verdict |
|---|---|---|---|---|
| G1 J_f parameter columns | optimizer:z_c | 1e-03:6.8e-08 1e-04:6.9e-10 1e-05:4.5e-11 1e-06:1.1e-10 1e-07:1.9e-08 | 1.1e-11 | PASS |
| G1 J_f parameter columns | optimizer:z_w | 1e-03:6.7e-07 1e-04:6.3e-09 1e-05:1.3e-09 1e-06:5.8e-09 1e-07:1.0e-07 | 3.4e-10 | PASS |
| G1 J_f parameter columns | physical:c_l | 1e-03:2.3e-06 1e-04:2.3e-08 1e-05:2.3e-10 1e-06:1.3e-11 1e-07:3.4e-10 | 3.6e-14 | PASS |
| G1 J_f parameter columns | physical:omega | 1e-03:7.6e-09 1e-04:2.8e-10 1e-05:2.2e-09 1e-06:5.8e-09 1e-07:4.6e-07 | 2.8e-10 | PASS |
| G1 J_cw (production) parameter columns | optimizer:z_c | 1e-03:6.8e-08 1e-04:6.9e-10 1e-05:4.6e-11 1e-06:1.2e-10 1e-07:1.9e-08 | 1.1e-11 | PASS |
| G1 J_cw (production) parameter columns | optimizer:z_w | 1e-03:6.7e-07 1e-04:6.3e-09 1e-05:1.3e-09 1e-06:5.8e-09 1e-07:1.0e-07 | 3.4e-10 | PASS |
| G1 J_cw (production) parameter columns | physical:c_l | 1e-03:2.3e-06 1e-04:2.3e-08 1e-05:2.3e-10 1e-06:1.3e-11 1e-07:3.4e-10 | 9.2e-14 | PASS |
| G1 J_cw (production) parameter columns | physical:omega | 1e-03:7.6e-09 1e-04:2.8e-10 1e-05:2.2e-09 1e-06:5.8e-09 1e-07:4.6e-07 | 2.8e-10 | PASS |
| G1 J_c parameter columns | optimizer:z_c | 1e-03:6.8e-08 1e-04:6.9e-10 1e-05:4.6e-11 1e-06:1.2e-10 1e-07:1.9e-08 | 1.1e-11 | PASS |
| G1 J_c parameter columns | optimizer:z_w | 1e-03:6.7e-07 1e-04:6.3e-09 1e-05:1.3e-09 1e-06:5.8e-09 1e-07:1.0e-07 | 3.4e-10 | PASS |
| G1 J_c parameter columns | physical:c_l | 1e-03:2.3e-06 1e-04:2.3e-08 1e-05:2.3e-10 1e-06:1.3e-11 1e-07:3.4e-10 | 9.2e-14 | PASS |
| G1 J_c parameter columns | physical:omega | 1e-03:7.6e-09 1e-04:2.8e-10 1e-05:2.2e-09 1e-06:5.8e-09 1e-07:4.6e-07 | 2.8e-10 | PASS |
| G1 J_f coefficient columns | 20 columns | | | 8/20 PASS; all_pass False |
| G1 J_cw coefficient columns | 20 columns | | | 10/20 PASS; all_pass False |
| G1 J_c coefficient columns | 20 columns | | | 10/20 PASS; all_pass False |
| G2 | G2a_identity_c_l | {"near_origin(r<=0.1R0)": 8.925102546309476e-17, "core_intermediate": 1.1631711133661447e-16, "far(r>256R0)": 1.31503813 | n/a | PASS |
| G2 | G2c_Up_DUp_c_l | {"1e-03": {"near_origin(r<=0.1R0)": 5.0289565580669815e-06, "core_intermediate": 2.8430731660447693e-06, "far(r>256R0)": | n/a | PASS |
| G2 | G2a_identity_omega | {"near_origin(r<=0.1R0)": 1.1777190627725982e-16, "core_intermediate": 1.1927552103451742e-16, "far(r>256R0)": 1.3420747 | n/a | PASS |
| G2 | G2c_Up_DUp_omega | {"1e-03": {"near_origin(r<=0.1R0)": 1.7553392389688085e-10, "core_intermediate": 8.871091393158899e-09, "far(r>256R0)":  | n/a | PASS |
| G4 | G4a_gradP_c_l | {"1e-03": {"near_origin(r<=0.1R0)": 1.5902848855397495e-06, "core_intermediate": 3.3494317665303675e-06, "far(r>256R0)": | n/a | PASS |
| G4 | G4b_source_c_l | {"rel": 7.248301201627186e-17, "PASS": true} | n/a | PASS |
| G4 | G4a_gradP_omega | {"1e-03": {"near_origin(r<=0.1R0)": 6.47177679843101e-10, "core_intermediate": 7.256938283495305e-09, "far(r>256R0)": 4. | n/a | PASS |
| G4 | G4b_source_omega | {"rel": 8.975161296028402e-17, "PASS": true} | n/a | PASS |
| G3 complete gradient | e_zc(optimizer) | 1e-03:3.2e-06 1e-04:3.2e-08 1e-05:2.7e-10 1e-06:1.2e-10 1e-07:1.9e-08 | 5.3e-11 | PASS |
| G3 complete gradient | e_zw(optimizer) | 1e-03:4.4e-07 1e-04:4.0e-09 1e-05:1.3e-09 1e-06:5.6e-09 1e-07:1.0e-07 | 3.4e-10 | PASS |
| G3 complete gradient | random_scaled_0 | 1e-03:1.3e-02 1e-04:1.3e-04 1e-05:1.3e-06 1e-06:1.3e-08 1e-07:3.8e-07 | 3.9e-07 | PASS |
| G3 complete gradient | random_scaled_1 | 1e-03:8.3e-03 1e-04:8.3e-05 1e-05:8.0e-07 1e-06:3.7e-07 1e-07:1.1e-06 | 3.7e-07 | PASS |
| G3 complete gradient | random_scaled_2 | 1e-03:8.9e-03 1e-04:8.9e-05 1e-05:8.9e-07 1e-06:8.0e-08 1e-07:1.3e-06 | 8.9e-08 | PASS |
| G3 complete gradient | mixed_0 | 1e-03:1.8e-02 1e-04:1.8e-04 1e-05:1.8e-06 1e-06:4.5e-08 1e-07:5.9e-07 | 5.9e-07 | PASS |
| G3 complete gradient | mixed_1 | 1e-03:7.4e-03 1e-04:7.4e-05 1e-05:7.4e-07 1e-06:1.4e-08 1e-07:2.1e-07 | 6.7e-09 | PASS |
| G3 complete gradient | e_c_l(physical) | 1e-03:1.3e-03 1e-04:1.3e-05 1e-05:1.3e-07 1e-06:1.3e-09 1e-07:3.2e-10 | 1.0e-11 | PASS |
| G3 complete gradient | e_omega(physical) | 1e-03:1.2e-07 1e-04:8.8e-10 1e-05:2.2e-09 1e-06:5.7e-09 1e-07:4.6e-07 | 2.8e-10 | PASS |
| G5a spatial FD vs DU (best relative per group) | | {"near_origin(r<=0.1R0)": 1.0513046470242528e-09, "core_intermediate": 3.113000454186415e-10, "far(r>256R0)": 2.86683422 | | PASS |
| G5b divergence | | {'U': 1.870889839275817e-15, 'U_c': 4.058890670833663e-15, 'U_w': 1.010917374264423e-15} | | PASS |
| G5c source consistency | | 0.0 | | see entrywise test |

wall: G1 2033 s, G2+G4 27 s, G3 367 s, G5 268 s
