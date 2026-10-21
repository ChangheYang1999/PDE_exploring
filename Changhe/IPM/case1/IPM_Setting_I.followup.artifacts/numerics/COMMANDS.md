# Command sequences of the full solves

The numerical researcher ran the full solves through shell chains. The chains themselves (job drivers with logging) are not included; this file lists, for each chain, the exact command sequence it ran, with the logging wrappers (echo of the clock, grep filters of warnings, redirections) removed. Run the commands from the top of the numerics part, after creating runs/ and copying data/ into it (the programs read states from and write outputs to runs/). Chains are listed in the order they were run; each comment line is the chain's own description.

## dense_chain

```
python3 src/jac_dense.py runs/psi5_n120m48_it2.npz n120m48 32 1e-5 0.01
python3 src/dense_newton.py runs/J_n120m48.pt dn_n120m48 14 20 480
```

## dense_chain2

```
# accurate-inverse Jacobian (Npsi 240 for the Jacobian columns; the residual in dense_newton uses Npsi 480) at the dn_n120m48 state,
# then LM-Newton + SVD + B_3, then the S4 (e) row.
python3 src/jac_dense.py runs/dn_n120m48.npz n120m48_acc 32 1e-5 0.01 240
python3 src/dense_newton.py runs/J_n120m48_acc.pt dn2_n120m48 12 20 480
python3 src/s4e_row.py runs/dn2_n120m48.npz dn2_n120m48
```

## psi_chain

```
# resolution and domain chain for the hybrid Psi-map Newton; waits for psi5 to finish, then seeds each run from the previous.
COMMON="--far_psi --n_coll 3 --coll_scale 0.02 --scl 400 --dt_jac 0.01 --gmres 60 --gtol 1e-3 --soft_cut 1e-3"
python3 src/run_psi_newton.py --N 160 --M 64 --beta 0.9 --L 8 --seed runs/psi6_n120m48.npz --tag psi6_n160m64 --maxit 8 $COMMON > runs/psi6_n160m64.out 2>&1
python3 src/b3_axis.py runs/psi6_n160m64.npz psi6_n160m64 > runs/b3_psi6_n160m64.out 2>&1
python3 src/run_psi_newton.py --N 240 --M 96 --beta 0.9 --L 8 --seed runs/psi6_n160m64.npz --tag psi6_n240m96 --maxit 8 $COMMON > runs/psi6_n240m96.out 2>&1
python3 src/b3_axis.py runs/psi6_n240m96.npz psi6_n240m96 > runs/b3_psi6_n240m96.out 2>&1
python3 src/run_psi_newton.py --N 120 --M 48 --beta 0.9 --L 4 --seed runs/psi6_n120m48.npz --tag psi6_n120m48L4 --maxit 8 $COMMON > runs/psi6_n120m48L4.out 2>&1
python3 src/b3_axis.py runs/psi6_n120m48L4.npz psi6_n120m48L4 > runs/b3_psi6_n120m48L4.out 2>&1
python3 src/run_psi_newton.py --N 120 --M 48 --beta 0.9 --L 16 --seed runs/psi6_n120m48.npz --tag psi6_n120m48L16 --maxit 8 $COMMON > runs/psi6_n120m48L16.out 2>&1
python3 src/b3_axis.py runs/psi6_n120m48L16.npz psi6_n120m48L16 > runs/b3_psi6_n120m48L16.out 2>&1
```

## s3_seeds

```
for cfg in "120 48" "160 64" "240 96"; do set -- $cfg
  python3 - <<PY
import sys; sys.path.insert(0,'src')
import ipm_newton as ipn, run_newton as rn
m=ipn.Model($1,$2,8.0,device='cuda',beta=0.9); x=rn.seed_from_x3(m); ipn.save_state('runs/seed_n$1m$2b09.npz',m,x,extra=dict(tag='seed'))
PY
  python3 src/s3_svd.py runs/seed_n$1m$2b09.npz seed_n$1m$2b09 10
done
```

## s3_domains

```
for L in 4 16; do
  python3 - <<PY
import sys; sys.path.insert(0,'src')
import ipm_newton as ipn, run_newton as rn
m=ipn.Model(120,48,float($L),device='cuda',beta=0.9); x=rn.seed_from_x3(m); ipn.save_state('runs/seed_n120m48b09L$L.npz',m,x,extra=dict(tag='seed'))
PY
  python3 src/s3_svd.py runs/seed_n120m48b09L$L.npz seed_n120m48b09L$L 10
done
```

## s3_npsi

```
for t in seed_n120m48b09 seed_n120m48b09L4 seed_n120m48b09L16 seed_n160m64b09 seed_n240m96b09; do
  python3 src/s3_svd.py runs/$t.npz ${t}_npsi360 10 360
done
```

## s3f_chain

```
python3 src/s3f_alpha.py runs/seed_n160m64b09.npz seed_n160m64b09 10 1e-6
for cfg in "120 48" "160 64"; do set -- $cfg; python3 src/s3_svd.py runs/seed_n$1m$2b09.npz seed_n$1m$2b09 10
```

## colcheck_npsi

```
for NP in 360 480; do python3 src/col_check.py runs/dn_n120m48.npz $NP 0.01 1e-5
```

## chainA_n144m56

```
# chain A: refinement (144,56) at L = 8: project the converged (120,48) state, dense Jacobian (Npsi 480, dt 0.01 = the residual's,
# eps 1e-6 one-sided, step cut tau_far 7.5), LM-Newton on the residual (Npsi 480, dt 0.01), SVD, S4 (e) row.
SEED=${1:-runs/dn2_n120m48.npz}
python3 src/project_seed.py $SEED 144 56 0.9 8 480 runs/seed_n144m56_from_dn2.npz
python3 src/jac_dense.py runs/seed_n144m56_from_dn2.npz n144m56 32 1e-6 0.01 480 7.5
python3 src/constrained_newton.py runs/J_n144m56.pt dn_n144m56 --free --scut 1e-5 --maxit 25 --Delta 0.05 --tol 1e-3
python3 src/soft_refresh.py runs/J_n144m56.pt runs/dn_n144m56.npz n144m56 12 2 1e-4 480
python3 src/s4e_row.py runs/dn_n144m56.npz dn_n144m56
python3 src/svd_report.py runs/J_n144m56_refreshed.pt n144m56_ref 8 480
python3 src/s3g_section.py runs/J_n144m56_refreshed.pt n144m56_ref 24 480
```

## chainB_rebuild_coarse_domains

```
# chain B: (1) rebuild the (120,48) Jacobian at the converged state (Npsi 480, dt 0.01, eps 1e-6, step cut 7.5; SVD at stationarity),
# SVD report, S3 (g) test, fixed-c_l continuation; (2) coarser grid (96,40) at L = 8 with SVD report and S3 (g); (3) domains L = 4, 16 at (96,40).
SEED=${1:-runs/dn2_n120m48.npz}
python3 src/jac_dense.py $SEED n120m48_conv 32 1e-6 0.01 480 7.5
python3 src/svd_report.py runs/J_n120m48_conv.pt n120m48_conv 8 480
python3 src/s3g_section.py runs/J_n120m48_conv.pt n120m48_conv 24 480
for DCL in 0.001 -0.001 0.01 -0.01; do
  CL=$(python3 -c "import numpy as np; d=np.load('$SEED'); print(float(d['c_l'])+$DCL)")
  python3 src/constrained_newton.py runs/J_n120m48_conv.pt fixcl_n120m48_d${DCL} --cl $CL --maxit 12
done
python3 src/project_seed.py $SEED 96 40 0.9 8 480 runs/seed_n96m40_from_dn2.npz
python3 src/jac_dense.py runs/seed_n96m40_from_dn2.npz n96m40 32 1e-6 0.01 480 7.5
python3 src/dense_newton.py runs/J_n96m40.pt dn_n96m40 12 20 480
python3 src/s4e_row.py runs/dn_n96m40.npz dn_n96m40
python3 src/svd_report.py runs/J_n96m40.pt n96m40 8 480
# rebuild at the converged (96,40) state (SVD at stationarity on the coarse grid; cheap) and the S3 (g) test there
python3 src/jac_dense.py runs/dn_n96m40.npz n96m40_conv 32 1e-6 0.01 480 7.5
python3 src/svd_report.py runs/J_n96m40_conv.pt n96m40_conv 8 480
python3 src/s3g_section.py runs/J_n96m40_conv.pt n96m40_conv 24 480
for L in 4 16; do
  python3 src/project_seed.py $SEED 96 40 0.9 $L 480 runs/seed_n96m40L${L}_from_dn2.npz
  python3 src/jac_dense.py runs/seed_n96m40L${L}_from_dn2.npz n96m40L${L} 32 1e-6 0.01 480 7.5
  python3 src/dense_newton.py runs/J_n96m40L${L}.pt dn_n96m40L${L} 12 20 480
  python3 src/s4e_row.py runs/dn_n96m40L${L}.npz dn_n96m40L${L}
  python3 src/svd_report.py runs/J_n96m40L${L}.pt n96m40L${L} 8 480
done
# optional (verifier q1design point 4): fresh Jacobian at a fixed-c_l end point on the coarse grid, to confirm the minimal residual
CL=$(python3 -c "import numpy as np; d=np.load('runs/dn_n96m40.npz'); print(float(d['c_l'])+0.01)")
python3 src/constrained_newton.py runs/J_n96m40_conv.pt fixcl_n96m40_d0.01 --cl $CL --maxit 12
python3 src/jac_dense.py runs/fixcl_n96m40_d0.01.npz n96m40_fixcl 32 1e-6 0.01 480 7.5
python3 src/constrained_newton.py runs/J_n96m40_fixcl.pt fixcl_n96m40_d0.01_fresh --cl $CL --maxit 8
```

## chainC_post_rebuild

```
# chain C: after the Npsi-480 Jacobian rebuild at dn2 (runs/J_n120m48_conv.pt): truncated Gauss-Newton to convergence (dn4: s_cut 1e-4,
# dn5: s_cut 1e-5 from dn4), soft-subspace refresh of J at the converged state, SVD report with response, S4 (e) row, S3 (g) test,
# dirtest, fixed-c_l continuation (+-1e-3, +-1e-2); then chain A ((144,56) from the converged state) in the background and the
# (96,40) grid with its own rebuild and the domains L = 4, 16 at (96,40).
python3 src/constrained_newton.py runs/J_n120m48_conv.pt dn4_n120m48 --free --scut 1e-4 --maxit 25 --Delta 0.05 --tol 1e-3
python3 src/constrained_newton.py runs/J_n120m48_conv.pt dn5_n120m48 --free --scut 1e-5 --maxit 25 --Delta 0.05 --tol 1e-3 --z0 runs/dn4_n120m48.npz
BEST=$(python3 -c "
import numpy as np
f4=float(np.load('runs/dn4_n120m48.npz')['F2']); f5=float(np.load('runs/dn5_n120m48.npz')['F2'])
print('runs/dn5_n120m48.npz' if f5 < f4 else 'runs/dn4_n120m48.npz')")
python3 src/soft_refresh.py runs/J_n120m48_conv.pt $BEST n120m48_conv 8 3 0.02 480
python3 src/svd_report.py runs/J_n120m48_conv_refreshed.pt n120m48_conv_ref 8 480
python3 src/s4e_row.py $BEST dn_best_n120m48
python3 src/s3g_section.py runs/J_n120m48_conv_refreshed.pt n120m48_conv_ref 24 480
# chain A (144,56) from the best state, in the background (shares the GPU from here on)
python3 src/dirtest.py runs/J_n120m48_conv_refreshed.pt n120m48_conv_ref runs/n120m48_conv_ref_softvecs_node_cl400.pt 480
for DCL in 0.001 -0.001 0.01 -0.01; do
  CL=$(python3 -c "import numpy as np; d=np.load('$BEST'); print(float(d['c_l'])+$DCL)")
  python3 src/constrained_newton.py runs/J_n120m48_conv_refreshed.pt fixcl_n120m48_d${DCL} --cl $CL --scut 1e-5 --maxit 12 --z0 $BEST
done
# coarser grid (96,40) at L = 8: project, J, Newton, rebuild at the converged state, SVD, S4 (e), S3 (g)
python3 src/project_seed.py $BEST 96 40 0.9 8 480 runs/seed_n96m40_from_best.npz
python3 src/jac_dense.py runs/seed_n96m40_from_best.npz n96m40 32 1e-6 0.01 480 7.5
python3 src/constrained_newton.py runs/J_n96m40.pt dn_n96m40 --free --scut 1e-5 --maxit 25 --Delta 0.05 --tol 1e-3
python3 src/jac_dense.py runs/dn_n96m40.npz n96m40_conv 32 1e-6 0.01 480 7.5
python3 src/soft_refresh.py runs/J_n96m40_conv.pt runs/dn_n96m40.npz n96m40_conv 8 2 0.02 480
python3 src/svd_report.py runs/J_n96m40_conv_refreshed.pt n96m40_conv_ref 8 480
python3 src/s4e_row.py runs/dn_n96m40.npz dn_n96m40
python3 src/s3g_section.py runs/J_n96m40_conv_refreshed.pt n96m40_conv_ref 24 480
for L in 4 16; do
  python3 src/project_seed.py $BEST 96 40 0.9 $L 480 runs/seed_n96m40L${L}_from_best.npz
  python3 src/jac_dense.py runs/seed_n96m40L${L}_from_best.npz n96m40L${L} 32 1e-6 0.01 480 7.5
  python3 src/constrained_newton.py runs/J_n96m40L${L}.pt dn_n96m40L${L} --free --scut 1e-5 --maxit 25 --Delta 0.05 --tol 1e-3
  python3 src/s4e_row.py runs/dn_n96m40L${L}.npz dn_n96m40L${L}
  python3 src/svd_report.py runs/J_n96m40L${L}.pt n96m40L${L} 8 480
done
```

## chainD_twostage

```
# chain D (two-stage solve at (120,48) with the Npsi-480 Jacobian): stage A converges the stiff directions (s >= 1e-3) with the
# truncated Gauss-Newton; stage B refreshes J along the softest directions with exact directional derivatives at the stage-A state
# and continues with a small trust radius and a low cutoff; stage C repeats the refresh and the solve once more; then the
# diagnostics (SVD with response, S4 (e) row, S3 (g)) and chain A ((144,56) from the final state) in the background.
python3 src/constrained_newton.py runs/J_n120m48_conv.pt dnA_n120m48 --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
python3 src/soft_refresh.py runs/J_n120m48_conv.pt runs/dnA_n120m48.npz n120m48_A 12 2 0.01 480
python3 src/constrained_newton.py runs/J_n120m48_A_refreshed.pt dnB_n120m48 --free --scut 1e-6 --maxit 40 --Delta 2e-3 --tol 3e-3
python3 src/soft_refresh.py runs/J_n120m48_A_refreshed.pt runs/dnB_n120m48.npz n120m48_B 12 2 0.005 480
python3 src/constrained_newton.py runs/J_n120m48_B_refreshed.pt dnC_n120m48 --free --scut 1e-6 --maxit 40 --Delta 2e-3 --tol 3e-3
BEST=$(python3 -c "
import numpy as np
c={t: float(np.load(f'runs/{t}_n120m48.npz')['F2']) for t in ('dnA','dnB','dnC')}; b=min(c, key=c.get); print(f'runs/{b}_n120m48.npz')")
python3 src/soft_refresh.py runs/J_n120m48_B_refreshed.pt $BEST n120m48_final 12 2 0.005 480
python3 src/svd_report.py runs/J_n120m48_final_refreshed.pt n120m48_final 10 480
python3 src/s4e_row.py $BEST dn_best_n120m48
python3 src/s3g_section.py runs/J_n120m48_final_refreshed.pt n120m48_final 24 480
python3 src/dirtest.py runs/J_n120m48_final_refreshed.pt n120m48_final runs/n120m48_final_softvecs_node_cl400.pt 480
for DCL in 0.001 -0.001 0.01 -0.01; do
  CL=$(python3 -c "import numpy as np; d=np.load('$BEST'); print(float(d['c_l'])+$DCL)")
  python3 src/constrained_newton.py runs/J_n120m48_final_refreshed.pt fixcl_n120m48_d${DCL} --cl $CL --scut 1e-6 --maxit 30 --Delta 2e-3 --tol 3e-3 --z0 $BEST
done
```

## chainE_n96m40

```
# chain E: coarse grid (96,40) at L = 8 and the domains L = 4, 16 at (96,40), from the best (120,48) state; waits for chain D's S3 (g)
# output (which precedes chain A's launch). Shares the GPU with chain A.
BEST=runs/dnC_n120m48.npz
# first: re-refresh the (120,48) Jacobian at dnC with s = 1e-4 (the earlier refresh at s = 0.005 was accurate to 5e-4 only), SVD, valley scan
python3 src/soft_refresh.py runs/J_n120m48_conv.pt runs/dnC_n120m48.npz n120m48_final2 12 3 1e-4 480
python3 src/svd_report.py runs/J_n120m48_final2_refreshed.pt n120m48_final2 10 480
python3 src/valley_scan.py runs/J_n120m48_final2_refreshed.pt n120m48_final2 4 480
python3 src/project_seed.py $BEST 96 40 0.9 8 480 runs/seed_n96m40_from_best.npz
python3 src/jac_dense.py runs/seed_n96m40_from_best.npz n96m40 32 1e-6 0.01 480 7.5
python3 src/constrained_newton.py runs/J_n96m40.pt dnA_n96m40 --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
python3 src/soft_refresh.py runs/J_n96m40.pt runs/dnA_n96m40.npz n96m40_A 12 2 1e-4 480
python3 src/constrained_newton.py runs/J_n96m40_A_refreshed.pt dnB_n96m40 --free --scut 1e-6 --maxit 20 --Delta 2e-3 --tol 3e-3
python3 src/soft_refresh.py runs/J_n96m40_A_refreshed.pt runs/dnB_n96m40.npz n96m40_final 12 2 1e-4 480
python3 src/svd_report.py runs/J_n96m40_final_refreshed.pt n96m40_final 10 480
python3 src/valley_scan.py runs/J_n96m40_final_refreshed.pt n96m40_final 4 480
python3 src/s4e_row.py runs/dnB_n96m40.npz dnB_n96m40
python3 src/s3g_section.py runs/J_n96m40_final_refreshed.pt n96m40_final 24 480
for L in 4 16; do
  python3 src/project_seed.py $BEST 96 40 0.9 $L 480 runs/seed_n96m40L${L}_from_best.npz
  python3 src/jac_dense.py runs/seed_n96m40L${L}_from_best.npz n96m40L${L} 32 1e-6 0.01 480 7.5
  python3 src/constrained_newton.py runs/J_n96m40L${L}.pt dnA_n96m40L${L} --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
  python3 src/soft_refresh.py runs/J_n96m40L${L}.pt runs/dnA_n96m40L${L}.npz n96m40L${L}_final 12 2 1e-4 480
  python3 src/svd_report.py runs/J_n96m40L${L}_final_refreshed.pt n96m40L${L}_final 10 480
  python3 src/s4e_row.py runs/dnA_n96m40L${L}.npz dnA_n96m40L${L}
done
```

## chainE2_smooth

```
# chain E2 (13:00Z): the smooth discrete system (charmap.TAU_SWITCH = 7.5: orbit step dt for tau < 7.5, dt_near after; same
# dt 0.01 / dt_near 0.04 / Npsi 480 as before). Stage 1: re-solve (120,48) from dnC (two-stage: truncated GN, soft refresh at s = 1e-4,
# LM), SVD with response, valley scan, S4 (e), S3 (g). Stage 2: dt/2 re-solve (orbit-step sensitivity of the floor and of c_l).
# Stage 3: (96,40) at L = 8 (dense Jacobian with the smooth residual, two-stage solve, refresh, SVD, valley, S4 (e), S3 (g)).
# Stage 4: L = 4 and L = 16 at (96,40).
python3 src/constrained_newton.py runs/J_n120m48_conv.pt dnSA_n120m48 --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3 --z0 runs/dnC_n120m48.npz
python3 src/soft_refresh.py runs/J_n120m48_conv.pt runs/dnSA_n120m48.npz n120m48_SA 12 3 1e-4 480
python3 src/constrained_newton.py runs/J_n120m48_SA_refreshed.pt dnSB_n120m48 --free --scut 1e-6 --maxit 40 --Delta 2e-3 --tol 3e-3
python3 src/soft_refresh.py runs/J_n120m48_SA_refreshed.pt runs/dnSB_n120m48.npz n120m48_S 12 3 1e-4 480
python3 src/svd_report.py runs/J_n120m48_S_refreshed.pt n120m48_S 10 480
python3 src/valley_scan.py runs/J_n120m48_S_refreshed.pt n120m48_S 4 480
python3 src/s4e_row.py runs/dnSB_n120m48.npz dnSB_n120m48
python3 src/s3g_section.py runs/J_n120m48_S_refreshed.pt n120m48_S 24 480
python3 src/constrained_newton.py runs/J_n120m48_S_refreshed.pt dnS_dt0005_n120m48 --free --dt 0.005 --scut 1e-3 --rebuild_cols --maxit 15 --Delta 0.05 --tol 1e-3 --z0 runs/dnSB_n120m48.npz
BEST=runs/dnSB_n120m48.npz
python3 src/project_seed.py $BEST 96 40 0.9 8 480 runs/seed_n96m40_from_S.npz
python3 src/jac_dense.py runs/seed_n96m40_from_S.npz n96m40S 32 1e-6 0.01 480 7.5
python3 src/constrained_newton.py runs/J_n96m40S.pt dnA_n96m40S --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
python3 src/soft_refresh.py runs/J_n96m40S.pt runs/dnA_n96m40S.npz n96m40S_A 12 2 1e-4 480
python3 src/constrained_newton.py runs/J_n96m40S_A_refreshed.pt dnB_n96m40S --free --scut 1e-6 --maxit 30 --Delta 2e-3 --tol 3e-3
python3 src/soft_refresh.py runs/J_n96m40S_A_refreshed.pt runs/dnB_n96m40S.npz n96m40S_final 12 2 1e-4 480
python3 src/svd_report.py runs/J_n96m40S_final_refreshed.pt n96m40S_final 10 480
python3 src/valley_scan.py runs/J_n96m40S_final_refreshed.pt n96m40S_final 4 480
python3 src/s4e_row.py runs/dnB_n96m40S.npz dnB_n96m40S
python3 src/s3g_section.py runs/J_n96m40S_final_refreshed.pt n96m40S_final 24 480
for L in 4 16; do
  python3 src/project_seed.py $BEST 96 40 0.9 $L 480 runs/seed_n96m40SL${L}.npz
  python3 src/jac_dense.py runs/seed_n96m40SL${L}.npz n96m40SL${L} 32 1e-6 0.01 480 7.5
  python3 src/constrained_newton.py runs/J_n96m40SL${L}.pt dnA_n96m40SL${L} --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
  python3 src/soft_refresh.py runs/J_n96m40SL${L}.pt runs/dnA_n96m40SL${L}.npz n96m40SL${L}_A 12 2 1e-4 480
  python3 src/constrained_newton.py runs/J_n96m40SL${L}_A_refreshed.pt dnB_n96m40SL${L} --free --scut 1e-6 --maxit 30 --Delta 2e-3 --tol 3e-3
  python3 src/soft_refresh.py runs/J_n96m40SL${L}_A_refreshed.pt runs/dnB_n96m40SL${L}.npz n96m40SL${L}_final 12 2 1e-4 480
  python3 src/svd_report.py runs/J_n96m40SL${L}_final_refreshed.pt n96m40SL${L}_final 10 480
  python3 src/s4e_row.py runs/dnB_n96m40SL${L}.npz dnB_n96m40SL${L}
done
```

## chainE2b_smooth

```
# chain E2 (13:00Z): the smooth discrete system (charmap.TAU_SWITCH = 7.5: orbit step dt for tau < 7.5, dt_near after; same
# dt 0.01 / dt_near 0.04 / Npsi 480 as before). Stage 1: re-solve (120,48) from dnC (two-stage: truncated GN, soft refresh at s = 1e-4,
# LM), SVD with response, valley scan, S4 (e), S3 (g). Stage 2: dt/2 re-solve (orbit-step sensitivity of the floor and of c_l).
# Stage 3: (96,40) at L = 8 (dense Jacobian with the smooth residual, two-stage solve, refresh, SVD, valley, S4 (e), S3 (g)).
# Stage 4: L = 4 and L = 16 at (96,40).
python3 src/soft_refresh.py runs/J_n120m48_conv.pt runs/dnSA_n120m48.npz n120m48_SA 12 3 1e-4 480
python3 src/constrained_newton.py runs/J_n120m48_SA_refreshed.pt dnSB_n120m48 --free --scut 1e-6 --maxit 40 --Delta 2e-3 --tol 3e-3
python3 src/soft_refresh.py runs/J_n120m48_SA_refreshed.pt runs/dnSB_n120m48.npz n120m48_S 12 3 1e-4 480
python3 src/svd_report.py runs/J_n120m48_S_refreshed.pt n120m48_S 10 480
python3 src/valley_scan.py runs/J_n120m48_S_refreshed.pt n120m48_S 4 480
python3 src/s4e_row.py runs/dnSB_n120m48.npz dnSB_n120m48
python3 src/s3g_section.py runs/J_n120m48_S_refreshed.pt n120m48_S 24 480
python3 src/constrained_newton.py runs/J_n120m48_S_refreshed.pt dnS_dt0005_n120m48 --free --dt 0.005 --scut 1e-3 --rebuild_cols --maxit 15 --Delta 0.05 --tol 1e-3 --z0 runs/dnSB_n120m48.npz
BEST=runs/dnSB_n120m48.npz
python3 src/project_seed.py $BEST 96 40 0.9 8 480 runs/seed_n96m40_from_S.npz
python3 src/jac_dense.py runs/seed_n96m40_from_S.npz n96m40S 32 1e-6 0.01 480 7.5
python3 src/constrained_newton.py runs/J_n96m40S.pt dnA_n96m40S --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
python3 src/soft_refresh.py runs/J_n96m40S.pt runs/dnA_n96m40S.npz n96m40S_A 12 2 1e-4 480
python3 src/constrained_newton.py runs/J_n96m40S_A_refreshed.pt dnB_n96m40S --free --scut 1e-6 --maxit 30 --Delta 2e-3 --tol 3e-3
python3 src/soft_refresh.py runs/J_n96m40S_A_refreshed.pt runs/dnB_n96m40S.npz n96m40S_final 12 2 1e-4 480
python3 src/svd_report.py runs/J_n96m40S_final_refreshed.pt n96m40S_final 10 480
python3 src/valley_scan.py runs/J_n96m40S_final_refreshed.pt n96m40S_final 4 480
python3 src/s4e_row.py runs/dnB_n96m40S.npz dnB_n96m40S
python3 src/s3g_section.py runs/J_n96m40S_final_refreshed.pt n96m40S_final 24 480
for L in 4 16; do
  python3 src/project_seed.py $BEST 96 40 0.9 $L 480 runs/seed_n96m40SL${L}.npz
  python3 src/jac_dense.py runs/seed_n96m40SL${L}.npz n96m40SL${L} 32 1e-6 0.01 480 7.5
  python3 src/constrained_newton.py runs/J_n96m40SL${L}.pt dnA_n96m40SL${L} --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
  python3 src/soft_refresh.py runs/J_n96m40SL${L}.pt runs/dnA_n96m40SL${L}.npz n96m40SL${L}_A 12 2 1e-4 480
  python3 src/constrained_newton.py runs/J_n96m40SL${L}_A_refreshed.pt dnB_n96m40SL${L} --free --scut 1e-6 --maxit 30 --Delta 2e-3 --tol 3e-3
  python3 src/soft_refresh.py runs/J_n96m40SL${L}_A_refreshed.pt runs/dnB_n96m40SL${L}.npz n96m40SL${L}_final 12 2 1e-4 480
  python3 src/svd_report.py runs/J_n96m40SL${L}_final_refreshed.pt n96m40SL${L}_final 10 480
  python3 src/s4e_row.py runs/dnB_n96m40SL${L}.npz dnB_n96m40SL${L}
done
```

## chainF_fixcl_smooth

```
# chain F (relaunched 13:21Z; order: ritz, cross-grid, fixed-c_l family): waits for the smooth-system (120,48) refreshed Jacobian and soft vectors; then
# (1) exact-action Ritz values on the candidate soft subspace at dnSB (src/ritz_subspace.py: matrix-softest 24 + stored soft vectors),
# (2) fixed-c_l family under the smooth system from dnSB, two stages per dc_l (truncated GN with Delta 0.05, then LM with Delta 2e-3),
# (3) cross-grid test (120,48) -> (144,56) with the smooth system at dnSB.
BEST=runs/dnSB_n120m48.npz
python3 src/ritz_subspace.py runs/J_n120m48_S_refreshed.pt n120m48_S 24 runs/n120m48_S_softvecs_node_cl400.pt 1e-4 480
python3 src/crossgrid_action.py $BEST runs/n120m48_S_softvecs_node_cl400.pt 144 56 0.9 8 n144m56_from_dnSB 10 1e-4 480
for DCL in 0.001 -0.001 0.01 -0.01 0.03 -0.03; do
  CL=$(python3 -c "import numpy as np; d=np.load('$BEST'); print(float(d['c_l'])+$DCL)")
  python3 src/constrained_newton.py runs/J_n120m48_S_refreshed.pt fixclSA_n120m48_d${DCL} --cl $CL --scut 1e-3 --maxit 12 --Delta 0.05 --tol 1e-3 --z0 $BEST
  python3 src/constrained_newton.py runs/J_n120m48_S_refreshed.pt fixclS_n120m48_d${DCL} --cl $CL --scut 1e-6 --maxit 25 --Delta 2e-3 --tol 1e-3 --z0 runs/fixclSA_n120m48_d${DCL}.npz
done
```

## chainF2_fixcl_smooth

```
# chain F2 (13:36Z): the fixed-c_l family of chain F (smooth system, (120,48), from dnSB, two stages per dc_l), started after the
# (144,56) two-grid solve (runs/tg2_n144m56.log says 'done') to keep at most two heavy GPU jobs. Appends to runs/chainF.out so that
# chain G's wait condition ('chain F done') is met at the end.
BEST=runs/dnSB_n120m48.npz
for DCL in 0.001 -0.001 0.01 -0.01 0.03 -0.03; do
  CL=$(python3 -c "import numpy as np; d=np.load('$BEST'); print(float(d['c_l'])+$DCL)")
  python3 src/constrained_newton.py runs/J_n120m48_S_refreshed.pt fixclSA_n120m48_d${DCL} --cl $CL --scut 1e-3 --maxit 12 --Delta 0.05 --tol 1e-3 --z0 $BEST
  python3 src/constrained_newton.py runs/J_n120m48_S_refreshed.pt fixclS_n120m48_d${DCL} --cl $CL --scut 1e-6 --maxit 25 --Delta 2e-3 --tol 1e-3 --z0 runs/fixclSA_n120m48_d${DCL}.npz
done
# the cross-grid test at the (144,56) two-grid state with the (120,48) soft vectors
python3 src/crossgrid_action.py $BEST runs/n120m48_S_softvecs_node_cl400.pt 144 56 0.9 8 n144m56_at_tg2 10 1e-4 480 --target_state runs/tg2_n144m56.npz
```

## chainG_fixcl_n96

```
# chain G (relaunched 14:52Z: the 96/120 cross-grid tests, ritz, fixed-c_l family at (96,40)): fixed-c_l family at (96,40), smooth system, from the converged (96,40) state (waits for chain E2's stage 3 and for
# chain F's fixcl part to finish, so that at most two heavy GPU jobs run). Two stages per dc_l as in chain F. Then exact-action Ritz values at (96,40).
BEST=runs/dnB_n96m40S.npz
# ((120,48) anatomy and angular-refinement tests moved to chain H, 14:52Z)
# cross-grid tests between the two full-solve grids, both at stationary-stiff states: (96,40) soft vectors on (120,48) at dnSB, and
# (120,48) soft vectors on (96,40) at dnB_n96m40S
python3 src/crossgrid_action.py $BEST runs/n96m40S_final_softvecs_node_cl400.pt 120 48 0.9 8 n120m48_from_n96S 10 1e-4 480 --target_state runs/dnSB_n120m48.npz
python3 src/crossgrid_action.py runs/dnSB_n120m48.npz runs/n120m48_S_softvecs_node_cl400.pt 96 40 0.9 8 n96m40_from_n120S 10 1e-4 480 --target_state $BEST
python3 src/ritz_subspace.py runs/J_n96m40S_final_refreshed.pt n96m40S 24 runs/n96m40S_final_softvecs_node_cl400.pt 1e-4 480
for DCL in 0.001 -0.001 0.01 -0.01 0.03 -0.03; do
  CL=$(python3 -c "import numpy as np; d=np.load('$BEST'); print(float(d['c_l'])+$DCL)")
  python3 src/constrained_newton.py runs/J_n96m40S_final_refreshed.pt fixclSA_n96m40_d${DCL} --cl $CL --scut 1e-3 --maxit 12 --Delta 0.05 --tol 1e-3 --z0 $BEST
  python3 src/constrained_newton.py runs/J_n96m40S_final_refreshed.pt fixclS_n96m40_d${DCL} --cl $CL --scut 1e-6 --maxit 25 --Delta 2e-3 --tol 1e-3 --z0 runs/fixclSA_n96m40_d${DCL}.npz
done
```

## chainH_anatomy

```
# chain H (14:52Z): (120,48) diagnostics run now as the second GPU job while chain E2 builds the (96,40) Jacobian:
# mode_anatomy (step sweep, shape/C/c_l split, r_far and Npsi sensitivity of the three softest Ritz directions at dnSB) and the
# angular-refinement cross-grid tests (120,64), (120,96) at the projected dnSB state. (Moved here from the start of chain G.)
python3 src/mode_anatomy.py runs/ritz_n120m48_S.pt runs/J_n120m48_S_refreshed.pt n120m48_S 3 480
python3 src/crossgrid_action.py runs/dnSB_n120m48.npz runs/n120m48_S_softvecs_node_cl400.pt 120 64 0.9 8 n120m64_from_dnSB 10 1e-4 480 --no-source
python3 src/crossgrid_action.py runs/dnSB_n120m48.npz runs/n120m48_S_softvecs_node_cl400.pt 120 96 0.9 8 n120m96_from_dnSB 10 1e-4 480 --no-source
```

## chainH2_rfar

```
# chain H2 (14:58Z): the r_far = 1e8 discrete system at (120,48) (the far Psi row placed at r = 1e8 instead of 1e10): stiff re-solve
# from dnSB with the stored (120,48) Jacobian, soft refresh (s 1e-4), exact-action Ritz values. Tests whether the near-kernel depends on the
# placement of the far row (mode_anatomy found the actions along the r_far = 1e10 soft directions change to 7e-4 when r_far changes,
# which conflates the state change and the operator change). Waits for chain H.
export IPM_RFAR=1e8
python3 src/constrained_newton.py runs/J_n120m48_S_refreshed.pt dnR8_n120m48 --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3 --z0 runs/dnSB_n120m48.npz
python3 src/soft_refresh.py runs/J_n120m48_S_refreshed.pt runs/dnR8_n120m48.npz n120m48_R8 12 3 1e-4 480
python3 src/ritz_subspace.py runs/J_n120m48_R8_refreshed.pt n120m48_R8 24 1e-4 480
```

## chainH3_mech

```
# chain H3 (15:36Z): two mechanism tests at (120,48) from dnSB, each = stiff re-solve with the stored Jacobian, soft refresh (s 1e-4),
# exact-action Ritz values (24 directions): (a) coll_scale 0.2 instead of 0.02 (the three innermost collocation rows weighted 10x: does the
# weak origin normalization carry the C-shape mode?); (b) Npsi 720 instead of 480 (inverse resolution: mode 2's action grew 3x at Npsi 720
# in the anatomy test at the mismatched state).
export IPM_COLLSCALE=0.2
python3 src/constrained_newton.py runs/J_n120m48_S_cs02.pt dnCS2_n120m48 --free --scut 1e-3 --rebuild_cols --maxit 8 --Delta 0.05 --tol 1e-3 --z0 runs/dnSB_n120m48.npz
python3 src/soft_refresh.py runs/J_n120m48_S_cs02.pt runs/dnCS2_n120m48.npz n120m48_CS2 12 3 1e-4 480
python3 src/ritz_subspace.py runs/J_n120m48_CS2_refreshed.pt n120m48_CS2 24 1e-4 480
unset IPM_COLLSCALE
python3 src/constrained_newton.py runs/J_n120m48_S_refreshed.pt dnP720_n120m48 --free --scut 1e-3 --rebuild_cols --maxit 8 --Delta 0.05 --tol 1e-3 --z0 runs/dnSB_n120m48.npz --Npsi 720
python3 src/soft_refresh.py runs/J_n120m48_S_refreshed.pt runs/dnP720_n120m48.npz n120m48_P720 12 3 1e-4 720
python3 src/ritz_subspace.py runs/J_n120m48_P720_refreshed.pt n120m48_P720 24 1e-4 720
```

## chainK_n72m30

```
# chain K (18:33Z): third full-solve resolution (72,30) at L = 8 under the smooth system (same dt 0.01 / dt_near 0.04 / Npsi 480,
# TAU_SWITCH 7.5), seeded from the (120,48) stagnation state dnSB (seed_n72m30S, projected |F| 0.295). Waits for chain E2 ('chain E2 done'
# in runs/chainE2.out), first runs the L = 16 exact-action Ritz test, then the (72,30) chain: dense Jacobian, two-stage solve (truncated GN,
# soft refresh at s = 1e-4, LM), final refresh, SVD with response, S4 (e), exact-action Ritz on the 24 softest matrix directions + refreshed
# soft vectors. Purpose: the third point of the S3 (e) resolution sequence (72,30) -> (96,40) -> (120,48), grid ratios 4/3 and 5/4.
if [ -f runs/J_n96m40SL16_final_refreshed.pt ]; then
  python3 src/ritz_subspace.py runs/J_n96m40SL16_final_refreshed.pt n96m40SL16 24 runs/n96m40SL16_final_softvecs_node_cl400.pt 1e-4 480
fi
python3 src/jac_dense.py runs/seed_n72m30S.npz n72m30S 32 1e-6 0.01 480 7.5
python3 src/constrained_newton.py runs/J_n72m30S.pt dnA_n72m30S --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
python3 src/soft_refresh.py runs/J_n72m30S.pt runs/dnA_n72m30S.npz n72m30S_A 12 2 1e-4 480
python3 src/constrained_newton.py runs/J_n72m30S_A_refreshed.pt dnB_n72m30S --free --scut 1e-6 --maxit 30 --Delta 2e-3 --tol 3e-3
python3 src/soft_refresh.py runs/J_n72m30S_A_refreshed.pt runs/dnB_n72m30S.npz n72m30S_final 12 2 1e-4 480
python3 src/svd_report.py runs/J_n72m30S_final_refreshed.pt n72m30S_final 10 480
python3 src/s4e_row.py runs/dnB_n72m30S.npz dnB_n72m30S
python3 src/ritz_subspace.py runs/J_n72m30S_final_refreshed.pt n72m30S 24 runs/n72m30S_final_softvecs_node_cl400.pt 1e-4 480
```

## chainK2_n72m30_refine

```
# chain K2 (20:25Z): is the (72,30) floor solver-limited? Re-refresh the (72,30) Jacobian with 24 soft vectors and 3 rounds at the stagnation state dnB_n72m30S,
# LM again, refresh, SVD, S4 (e), Ritz values. If |F| drops well below 7.58e-4 the earlier floor was solver-limited (it is recorded as an upper bound either way).
python3 src/soft_refresh.py runs/J_n72m30S_final_refreshed.pt runs/dnB_n72m30S.npz n72m30S_R2 24 3 1e-4 480
python3 src/constrained_newton.py runs/J_n72m30S_R2_refreshed.pt dnC_n72m30S --free --scut 1e-6 --maxit 40 --Delta 2e-3 --tol 1e-3
python3 src/soft_refresh.py runs/J_n72m30S_R2_refreshed.pt runs/dnC_n72m30S.npz n72m30S_final2 12 2 1e-4 480
python3 src/svd_report.py runs/J_n72m30S_final2_refreshed.pt n72m30S_final2 10 480
python3 src/s4e_row.py runs/dnC_n72m30S.npz dnC_n72m30S
python3 src/ritz_subspace.py runs/J_n72m30S_final2_refreshed.pt n72m30S_C 24 runs/n72m30S_final2_softvecs_node_cl400.pt 1e-4 480
```

## chainL_n84m35

```
# chain L (20:55Z): a fourth full-solve resolution (84,35) at L = 8 (between (72,30) and (96,40)), same smooth system, seeded from dnSB (120,48).
# Purpose: a fourth point for the resolution sequence of section 5 (consistency of the fitted exponents); not audited by the verifier (launched after its cut-off).
python3 src/project_seed.py runs/dnSB_n120m48.npz 84 35 0.9 8 480 runs/seed_n84m35S.npz
python3 src/jac_dense.py runs/seed_n84m35S.npz n84m35S 32 1e-6 0.01 480 7.5
python3 src/constrained_newton.py runs/J_n84m35S.pt dnA_n84m35S --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
python3 src/soft_refresh.py runs/J_n84m35S.pt runs/dnA_n84m35S.npz n84m35S_A 12 2 1e-4 480
python3 src/constrained_newton.py runs/J_n84m35S_A_refreshed.pt dnB_n84m35S --free --scut 1e-6 --maxit 30 --Delta 2e-3 --tol 3e-3
python3 src/soft_refresh.py runs/J_n84m35S_A_refreshed.pt runs/dnB_n84m35S.npz n84m35S_final 12 2 1e-4 480
python3 src/svd_report.py runs/J_n84m35S_final_refreshed.pt n84m35S_final 10 480
python3 src/s4e_row.py runs/dnB_n84m35S.npz dnB_n84m35S
python3 src/ritz_subspace.py runs/J_n84m35S_final_refreshed.pt n84m35S 24 runs/n84m35S_final_softvecs_node_cl400.pt 1e-4 480
```

## chainM_n108m44

```
# chain M (21:58Z): a fifth full-solve resolution (108,44) at L = 8 (between (96,40) and (120,48)), same smooth system, seeded from dnSB (120,48).
# Purpose: a fourth point for the resolution sequence of section 5 (consistency of the fitted exponents); not audited by the verifier (launched after its cut-off).
python3 src/project_seed.py runs/dnSB_n120m48.npz 108 44 0.9 8 480 runs/seed_n108m44S.npz
python3 src/jac_dense.py runs/seed_n108m44S.npz n108m44S 32 1e-6 0.01 480 7.5
python3 src/constrained_newton.py runs/J_n108m44S.pt dnA_n108m44S --free --scut 1e-3 --rebuild_cols --maxit 12 --Delta 0.05 --tol 1e-3
python3 src/soft_refresh.py runs/J_n108m44S.pt runs/dnA_n108m44S.npz n108m44S_A 12 2 1e-4 480
python3 src/constrained_newton.py runs/J_n108m44S_A_refreshed.pt dnB_n108m44S --free --scut 1e-6 --maxit 30 --Delta 2e-3 --tol 3e-3
python3 src/soft_refresh.py runs/J_n108m44S_A_refreshed.pt runs/dnB_n108m44S.npz n108m44S_final 12 2 1e-4 480
python3 src/svd_report.py runs/J_n108m44S_final_refreshed.pt n108m44S_final 10 480
python3 src/s4e_row.py runs/dnB_n108m44S.npz dnB_n108m44S
python3 src/ritz_subspace.py runs/J_n108m44S_final_refreshed.pt n108m44S 24 runs/n108m44S_final_softvecs_node_cl400.pt 1e-4 480
```

