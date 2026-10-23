# Checkpoint and model format (numerics lane), for independent validation

All tensors are FP64. A checkpoint `runs/<exp_id>/ckpt_last.pt` (and `ckpt_best.pt`, `archive/ckpt_step*.pt`) is a
`torch.save` dict with keys: `model` (state_dict), `opt` (optimizer state, ckpt_last only), `state` (stage, step,
global_step, active_seconds, best_val, nan_count, interruptions), `sampler` (generator state), `rng` (torch/cuda/numpy/python
RNG states), `cfg` (the experiment config), `exp_id`, `saved`, `cfg_hash`. Load with `torch.load(path, weights_only=False)`.
`python3 export_npz.py <ckpt> <prefix>` writes `<prefix>.npz` (all state_dict arrays) and `<prefix>.json` (manifest with
every formula below and the config).

## Scalars
- `cl_fixed` (buffer) if `cfg.cl_trainable` is false; else `cl_theta` (parameter) with
  c_l = lo + (hi - lo) sigmoid(cl_theta), [lo, hi] = cfg.cl_bounds (default [0.4, 0.5]).
- C = cfg.C (constant, 0 in all current experiments).
- `seed_abc` = (a, b, c_M) of the seed matrix (parameter if cfg.seed.trainable, else buffer).

## Representation (euler_ss/model.py, ProfileModel)
Inputs: y in R^3 (physical similarity coordinates). Features x(y):
- `dir_tau` (v2, default): xi = y / sqrt(l_in^2 + |y|^2), x = [xi_1, xi_2, xi_3, |xi|^2]  (4 inputs, bounded, analytic).
- `dir_log` (v1 baseline): x = [y / sqrt(l_in^2+|y|^2), log(1+|y|^2/l_in^2)/xi_scale].
- `asinh`: x = [asinh(y_i/l_in)/xi_scale (i=1..3), log(1+|y|^2/l_in^2)/xi_scale]; `both`: the 7 of dir_log and asinh.
MLPs netA, netP: h_0 = x, h_{i+1} = tanh(W_i h_i + b_i) for i = 0..depth-1 (width hidden units), out = W_depth h_depth + b_depth.
State-dict keys `netA.lins.<i>.weight`, `netA.lins.<i>.bias` (i = 0..depth), same for netP.
netA has 3*n_tail outputs, reshaped to (n_tail, 3); netP has n_tail outputs. n_tail = cfg.model.n_tail (2 for dir_tau, 1 otherwise).
Both multiplied by out_scale (1.0).
Hard symmetry projection with Q = diag(-1,-1,1): SA_k(y) = [NA_k(y) + Q NA_k(Qy)]/2, SP_k(y) = [NP_k(y) + NP_k(Qy)]/2.
Envelopes with d = 1 - 1/c_l and base(y) = 1 + |y|^2/l_env^2:
    envA_k(y) = base^((d + 1 + k (d-1) + a_env_shift)/2),   envP_k(y) = base^(d + k (d-1)/2 + p_env_shift/2),  k = 0..n_tail-1.
Seed (PROMPT.md section 9): M = [[a,b,0],[c_M,-1-a,0],[0,0,1]], chi = (1+|y|^2)^(-1/(2 c_l)),
    A_seed = -(chi/3) y x (M y),   P_seed = -(chi^2/2) y . (M + M^2) y.
Fields:
    A(y) = A_seed(y) + sum_k envA_k(y) SA_k(y),    P(y) = P_seed(y) + sum_k envP_k(y) SP_k(y),    U = curl A.
Pressure gauge: P -> 0 at infinity (no additive constant anywhere). No other hard constraint.
Derivatives in the trainer: nested forward-mode AD (torch.func.jacfwd) in physical coordinates y.

## Training objective (euler_ss/losses.py), logged component by component in runs/<id>/metrics.jsonl
loss = sum over regions {core, shell, axis, origin} of mean_i |R_m(y_i)|^2 / T(y_i)^2
       + lambda_amp (N_8[U] - 1)^2  [+ optional lambda_nonaxi relu(floor - nonaxi_ratio)^2, off by default],
T(y) = base^(q/2), q = d + T_lambda (d - 1) (T_lambda 0: linear-term scale R^d; 1: nonlinear scale R^(2d-1)),
N_8[U] = (sum_i |U(g_i)|^16)^(1/16) over 2048 fixed gauge points g_i uniform in |y| < R_core (smooth max surrogate; the
realized sampled max |U| is logged as amp_max). Regions per step: core ball |y| < R_core uniform; shell log-uniform radius in
[R_core, R_max] with uniform directions; axis tube r < r_tube with log-uniform |z| in [z_min, R_max]; origin ball |y| < R_origin.
Divergence is exactly zero by construction (U = curl A); its sampled value is logged in validation (val_div_*_max).

## Holdout and validation (train.py validate(); runs/<id>/val.jsonl)
`runs/<id>/holdout.pt` is the fixed untouched holdout set (dict region -> (y, w), generator seed rng_seed + 7919; never used
in the loss). Importance weights w make sum_i w_i f(y_i) the physical integral over the region. Validation reports per region:
RMS and max of |R_m|/T at both scales, eps_m(D) and eps_nl(D) = ||R_m|| / (||U.grad U|| + ||grad P||) on radial shells
D1..D6, sampled max |U|, |Omega| and its location, core radius (50% vorticity energy), stretching ratio at the sampled
vorticity maximum, group-average non-axisymmetry ratio (8 rotations), vorticity fraction, affine fit remainder, U(0), grad U(0),
P(0), tail slope, 3D dependence ||d_3 U||/||grad U||, inversion and z-reflection parity defects, hard Q-symmetry defect,
ring Fourier energy fractions (n = 0, 2, 4, >= 6, odd), and the stagnation set of V (Newton from 192+48 fixed starts:
position, |Omega|, eig(grad V), eig(S), isolation distance).
Training batches are drawn from the sampler generator (seed rng_seed + 1), whose state is checkpointed; the exact batch
sequence is reproducible by replaying the generator from the checkpointed state.

## Ledger records (CAMPAIGN_LEDGER.jsonl)
Since 2026-10-23 07:12Z each record has "chunks": [[epoch_start, epoch_end], ...], the credited elapsed pieces between accepted
optimizer steps (a chunk is closed when a gap > 30 s occurs or at the checkpoint). Chunks include checkpoint I/O and pauses
shorter than 30 s, omit the first step after a (re)start, and have endpoints rounded to 1 ms; active_seconds is their total.
ledger.py: active_hours_union = |union of all chunks and legacy wall intervals| - sum over legacy records of their inactive
measure (lower bound of the credited elapsed time), active_hours_upper = |union|. These bound the CREDITED elapsed time; the
eligible numerical compute time is not recoverable exactly from the ledger.
Legacy records (before 07:12Z) have only interval_start/interval_end/active_seconds.

## Migration notes
- Checkpoints written before 2026-10-23 06:45Z contain a buffer `seed_scale` (always 1.0, unused); the current model has no
  such buffer and loads them with strict=False (the key is ignored; the field is identical since scale = 1).
- `batch` (optional, only when the current stage uses resample_every > 1): the current collocation batch and the step at
  which it was drawn, so that a resume inside a block is exact.

## Accounting version 3 (worker code after 2026-10-23 07:58Z; no campaign record uses it)
Records carry "accounting_version": 3 and chunks that are instrumented work intervals: [begin of the batch draw, end of the
optimizer step after torch.cuda.synchronize()] for every step, plus [begin, end] of each validation pass; intervals are never
merged, so the gaps between steps (logging, status writes, checkpoint I/O, pauses) are not credited. Endpoints are rounded to 1 ms.
Test-only options: --no-ledger, --ledger-path <file>, --ignore-global-stop. The saved batch (if any) carries
stage, counts and sampler configuration and is restored only inside a block of the same stage.
