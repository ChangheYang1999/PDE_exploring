# the team notes (from the lead work). Newest on top.

## Note 42 (2026-10-28T11:46Z): a10v7 done, D_1/10 >= 7.0445434786 (lead computation, please audit)

To the verification work. The alpha=1/10 run of the same certifier cert_v7.py finished 11:44:50Z with EXIT 0 (log
scratch/projcert/run_a10v7.log, 20 chunks). Post-run sha256 of cert_v7.py (69fdc727...), run_queue7.py (3db66f0a...),
plans/a10v7.json (7adee1d0...), run_a10v7.sh (c64dfaa4...) and combine_v7b.py (d3259d04...) equal the pre-launch record
scratch/projcert/verification/a10v7_prelaunch_hashes.txt (11:06:33Z); no source was edited during the run.
combine_v7b.py gives scratch/projcert/verification/a10v7_combined.json (sha256 7fbc7336...; the artifacts copy
lead_projection/verification/a10v7_combined.json differs only by the path sanitization):

    alpha 1/10, b 3/8, shift -1/40, K 1003/1000,
    pieces: both signs log d in [-150,-18] 4096x512; s=+1 [-18,12] and s=-1 [-18,log 1/2] 16384x512; log v in [-6,3],
    D_1/10 >= 7.0445434786 (enclosure [7.04454347867277... +/- 2.6e-54]); rules v2 13, v4 16841879, mv2 2478992, ref 27843.

Differences from a30v7 that need your check:
1. combine_v7b.py = combine_v7.py (b676f2bf..., audited for a20/a30) plus one change: the registry branch for the profile
   constant certificate data/profile_constant_certificate.json now accepts alpha in {1/20, 1/10, 1/5} instead of {1/5}
   (diff: one line, `elif alpha in [F(1,20),F(1,10),F(1,5)]:`). For 1/10 it asserts K >= safe_upper of the 1/10 row and
   epsilon > 0, with that certificate's own source hashes. The row is the K_1/10 <= 1.002471319750 of the proof of
   Theorem 4.6, and 1003/1000 > 1.002471319750.
2. The pieces near the pole start at log d = -150 instead of -60 (the near-pole strips matter more at small alpha) and use
   4096x512 instead of 2048x256 there. Omitting strips only removes nonnegative contributions, as before.
3. b 3/8 as for a20/a30; shift -1/40 instead of -1/20.

Against the current Table 1 (D upper 7.285961 at 0.1): D ratio at 0.1 would drop from 1.0371 to 1.0343, and with
C_1/10 <= 6.8514311158 the separation would be D-C >= 0.1931 (Theorem 4.6 gives 0.1745). A selected-chunk replay as for
a20 and a30 would be enough for me. On CONFIRMED I will add (1/10, 1000/1003) to Theorem 4.7(viii); make_table1 already
lists stieltjes_v7/a10/accepted.json.

## Note 41 (2026-10-28T11:44Z): cross-read of phase_interpolation/PROOF.md: correct, no gap found

To the verification work. I read 08_improved_upper_bounds/phase_interpolation/PROOF.md (sha256 08042d70...8778) in full, together with
05_team_audit/phase_identity_reread/PROOF.md. I find no error. Points checked:

1. Interpolation identity. sin(delta-t)e^{ij delta} + sin(t)e^{i(j+1)delta} = sin(delta) e^{i(j delta+t)}, so
   M_{j delta+t} = [sin(delta-t) M_{j delta} + sin(t) M_{(j+1)delta}]/sin(delta) for any family cos(phi)M_0 + sin(phi)M_{pi/2}.
   Both coefficients are nonnegative on [0,delta], so the triangle inequality gives ||M_phi|| <= g(t) for any upper bounds
   u >= ||M_{j delta}||, v >= ||M_{(j+1)delta}||. This only needs u_j to bound the dual norm at the node; it does not need
   u_j to be a seminorm of the phase itself. That covers Theorem 3.7, where u_j is the cost of a plan chosen at the node.
2. Formula. g(t) = u cos t + ((v - u cos delta)/sin delta) sin t; amplitude^2 = (u^2 + v^2 - 2uv cos delta)/sin^2 delta. g >= 0 and
   g'' = -g give concavity; g'(0) = (v - u cos delta)/sin delta and g'(delta) = (v cos delta - u)/sin delta. The three cases
   are right, including the degenerate u = v = 0. Comparison: g(t) <= max(u,v) cos(t - delta/2)/cos(delta/2). Monotone in u
   and v because g is. A float brute-force check (20000 random pairs, 4001 nodes) matches H_delta to 7e-11. That is a
   sanity check only, not part of the proof.
3. Scope. In every place where the report now uses sec(pi/(4m)) max_j (...) (Theorems 3.3 to 3.7, including the D versions
   with the phase-uniform 2^{1-alpha}A_alpha/alpha + 1/2 and S_alpha(delta) terms outside the maximum), the bracketed
   quantity bounds the norm of the regular functional at the node, and the removed part is bounded uniformly in phase
   before the grid. So max_{0<=j<m} H_delta(u_j, u_{j+1}) may replace sec(pi/(4m)) max_j u_j there, with the same [0,pi/2]
   reduction by conjugation and pi-periodicity. I agree it does not apply to a density that keeps the identity atoms inside
   the phase-dependent problem.
4. Certification rule. This is fine: choose the endpoint formula only on a certified derivative sign; otherwise take the
   smaller of the amplitude and sec(delta/2)max(u,v), both of which are valid. Use the upper interval endpoints for u_j.

I will integrate the values after your numerical acceptance, as a one-line change of each phase display ("sec(pi/(4m))
max_j" replaced by "max_{0<=j<m} H_delta") plus the new Table 1 values. Expected size: up to about 0.12 percent of the
bracketed term when the worst node's neighbours are below u cos(pi/32).

a10v7 is in its last chunks (p3 r12288_14336 started 11:41:37Z); its result will be Note 42.


Verifier capture metadata: the full proof SHA256 is08042d70d89233410fb06a46c800deba6b3c266c0052bf0b0886378f31438778. It matches the abbreviated08042d70...8778 in the lead's note. The full digest is supplied by the verifier, not quoted from the lead.
