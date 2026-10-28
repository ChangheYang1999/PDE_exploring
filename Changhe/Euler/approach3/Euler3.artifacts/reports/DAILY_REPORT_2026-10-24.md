# Daily report, numerics lane, 2026-10-24 23:39Z

Campaign elapsed: 6.50 h of 96 (T0 = 2026-10-24T17:09:12Z). Stage I.
Starts completed: 544; jobs completed: 103; GPU-slot minutes consumed by completed jobs: 1430 (two slots per GPU on four GPUs; wall-clock GPU share about 0.92 of the 4-GPU allocation).
Start types (formulation, nl_weighting, optimizer): {('vort', False, 'lm'): 218, ('mom', True, 'lm'): 219, ('vort', True, 'lm'): 107}

## Best states by rho_u_max (SPEC 7.3 key; none is a candidate unless tier_S is True)

- rho_u_max 4.730e-02, rho_nl_max 3.00e+00, d6t_L8_cl0.45_om+0.3_fixed start 0 (init_from), c_l=0.45, omega=0.3, mom nlw, e_F=0.04, N_core=9.28e-01, r_core=0.157, r_tail=1.972468151735338, tier S=False
- rho_u_max 5.232e-02, rho_nl_max 3.85e+00, d6u_L8_cl0.45_om+0.3_fixed start 0 (init_from), c_l=0.45, omega=0.3, mom nlw, e_F=0.04, N_core=9.06e-01, r_core=0.139, r_tail=1.972468151735338, tier S=False
- rho_u_max 5.872e-02, rho_nl_max 8.15e-01, d6v_L6_cl0.45_om+0.3_fixed start 0 (init_from), c_l=0.45, omega=0.3, mom nlw, e_F=0.05, N_core=7.76e-01, r_core=0.155, r_tail=1.9471584905095762, tier S=False
- rho_u_max 5.953e-02, rho_nl_max 3.03e+00, d6t_L6_cl0.45_om+0.3_fixed start 0 (init_from), c_l=0.45, omega=0.3, mom nlw, e_F=0.05, N_core=8.13e-01, r_core=0.155, r_tail=1.9471584905095762, tier S=False
- rho_u_max 6.354e-02, rho_nl_max 8.58e-01, d6u_L6_cl0.45_om+0.3_free start 0 (init_from), c_l=0.499, omega=0.2701693002362974, mom nlw, e_F=0.02, N_core=5.26e-01, r_core=0.133, r_tail=1.7172657131881202, tier S=False
- rho_u_max 1.037e-01, rho_nl_max 4.16e-01, s1b_momnlw_L6_cl0.49_om+1.0 start 2 (nonaxi), c_l=0.49, omega=1.0, mom nlw, e_F=0.00, N_core=6.92e-04, r_core=0.634, r_tail=1.212151600280866, tier S=False
- rho_u_max 1.066e-01, rho_nl_max 4.59e+00, d6tZ_L6_cl0.45_om+0.3_fixed start 0 (init_from), c_l=0.45, omega=0.3, mom nlw, e_F=0.01, N_core=1.23e+00, r_core=0.283, r_tail=2.222583079787227, tier S=False
- rho_u_max 1.619e-01, rho_nl_max 2.17e-01, s1b_momnlw_L6_cl0.49_om+1.0 start 1 (tail), c_l=0.49, omega=1.0, mom nlw, e_F=0.00, N_core=9.60e-04, r_core=0.634, r_tail=1.699073515847131, tier S=False

## Best rho_u_max per (c_l, omega)

- c_l=0.41, omega=0.1: rho_u_max 6.435e-01 (vort nlw, e_F=0.83)
- c_l=0.41, omega=0.3: rho_u_max 6.495e-01 (mom nlw, e_F=0.30)
- c_l=0.41, omega=1.0: rho_u_max 5.213e-01 (mom nlw, e_F=0.20)
- c_l=0.41, omega=3.0: rho_u_max 5.616e-01 (vort nlw, e_F=0.44)
- c_l=0.41, omega=10.0: rho_u_max 6.229e-01 (mom nlw, e_F=0.36)
- c_l=0.43, omega=0.1: rho_u_max 6.050e-01 (vort nlw, e_F=0.32)
- c_l=0.43, omega=0.3: rho_u_max 5.199e-01 (mom nlw, e_F=0.54)
- c_l=0.43, omega=1.0: rho_u_max 3.519e-01 (mom nlw, e_F=0.52)
- c_l=0.43, omega=3.0: rho_u_max 5.670e-01 (mom nlw, e_F=0.95)
- c_l=0.43, omega=10.0: rho_u_max 6.542e-01 (vort nlw, e_F=0.88)
- c_l=0.45, omega=0.1: rho_u_max 5.456e-01 (mom nlw, e_F=0.38)
- c_l=0.45, omega=0.3: rho_u_max 4.730e-02 (mom nlw, e_F=0.04)
- c_l=0.45, omega=1.0: rho_u_max 3.568e-01 (mom nlw, e_F=0.68)
- c_l=0.45, omega=3.0: rho_u_max 5.022e-01 (mom nlw, e_F=0.95)
- c_l=0.45, omega=10.0: rho_u_max 7.308e-01 (mom nlw, e_F=1.00)
- c_l=0.45092494315000553, omega=1.0000965966098674: rho_u_max 5.053e-01 (mom nlw, e_F=0.62)
- c_l=0.47, omega=-3.0: rho_u_max 9.835e-01 (vort, e_F=0.00)
- c_l=0.47, omega=-0.3: rho_u_max 9.835e-01 (vort, e_F=0.00)
- c_l=0.47, omega=0.1: rho_u_max 7.101e-01 (mom nlw, e_F=0.86)
- c_l=0.47, omega=0.3: rho_u_max 3.522e-01 (mom nlw, e_F=0.56)
- c_l=0.47, omega=1.0: rho_u_max 1.641e-01 (mom nlw, e_F=0.00)
- c_l=0.47, omega=3.0: rho_u_max 4.092e-01 (mom nlw, e_F=0.95)
- c_l=0.47, omega=10.0: rho_u_max 6.545e-01 (vort nlw, e_F=0.88)
- c_l=0.49, omega=-3.0: rho_u_max 9.797e-01 (vort, e_F=0.00)
- c_l=0.49, omega=-0.3: rho_u_max 9.796e-01 (vort, e_F=0.00)
- c_l=0.49, omega=0.1: rho_u_max 5.686e-01 (vort nlw, e_F=0.69)
- c_l=0.49, omega=0.3: rho_u_max 5.363e-01 (mom nlw, e_F=0.73)
- c_l=0.49, omega=1.0: rho_u_max 1.037e-01 (mom nlw, e_F=0.00)
- c_l=0.49, omega=3.0: rho_u_max 5.512e-01 (vort nlw, e_F=0.85)
- c_l=0.49, omega=10.0: rho_u_max 1.643e-01 (mom nlw, e_F=0.00)
- c_l=0.499, omega=0.2701693002362974: rho_u_max 6.354e-02 (mom nlw, e_F=0.02)

## Plain least-squares vorticity sweep s1a (138 starts without SPEC fields in the ledger)

- all converged to the omega-independent axisymmetric weak state (weighted vorticity RMS 2.366e-02 to 2.898e-02); rotation content ~1e-15; not a candidate.

## Optimizer exit statuses

- {'max_iter': 196, 'ftol': 301, 'stalled': 47}

## Job errors, retries and failures

- 39 records: job_error queue/running/c2x2_L6_cl0.47_om+1.0_free.json RuntimeError('size mismatch, got input (674), mat (674x116282), vec (116283)'); job_retry c2x2_L6_cl0.47_om+1.0_free exit 1; job_error queue/running/c2x2_L6_cl0.45_om+1.0_free.json RuntimeError('size mismatch, got input (674), mat (674x116282), vec (116283)'); job_failed c2x2_L6_cl0.45_om+1.0_free exit 1; job_error queue/running/c2x2_L6_cl0.47_om+1.0_free.json RuntimeError('size mismatch, got input (674), mat (674x116282), vec (116283)'); job_failed c2x2_L6_cl0.47_om+1.0_free exit 1; job_retry c2x2_L6_cl0.47_om+1.0_free exit 3; job_retry c2x2_L6_cl0.45_om+1.0_free exit 3; job_retry c2x2_L10_cl0.47_om+1.0_free exit 3; job_retry d6u_L6_cl0.45_om+0.3_free exit 3

## Supervisor status

- 2026-10-24T23:38:26Z: running 6, pending 92, done 103, failed 28, disk free 169.3 GB, lane usage 0.29 GB, GPUs {'0': {'mem_MiB': 67087, 'util': 100}, '1': {'mem_MiB': 28433, 'util': 0}, '4': {'mem_MiB': 19725, 'util': 8}, '5': {'mem_MiB': 55073, 'util': 86}}
