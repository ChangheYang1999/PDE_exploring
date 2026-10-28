## Note 51 (2026-10-28T13:18Z): cross-reads V202, V200, V201: all CONFIRMED; v30 audit fixes accepted for v31

To the verification work.

1. V202 (explicit_second_term/sharp_deficiency/PROOF.md, sha 6a5469ec...): CONFIRMED on my cross-read. Checked:
   - C, extracted pair mass: m <= min(|A|, |B|) <= u + H always, and if u > H the two perturbed marginals keep opposite
     signs so m >= u - H; hence |m - u| <= H and the deficiency term is 8aH, not 16aH.
   - The log-sine integral: int_0^{pi/4} -log(2 r sin t) dt = -(pi/4) log r + G/2 (G = Catalan), giving
     B_C^* = rho^2/(2(1-rho)^2) [-log rho + 1/2 + 2G/pi].
   - D, target marginal and max step: the removed fraction of a projection edge is max(q_s, q_t), not q_s + q_t; with
     q_s <= H r^2/c and q_t <= H lambda^2 r^2/c on the edge c dr dt / r the removed density is at most H r dr dt, the
     angular integral is (pi/4)(-log r + log 2), and B_D^* = rho^2/(2(1-rho)^2) [-log rho + 1/2 + log 2]. The residual masses,
     the retained plan and the identity term are as in the accepted linear-remainder proof, so nothing is counted twice.
   - B_C - B_C^* = rho^2/(2(1-rho)^2) [-log rho + 5/2 - log 2 - 2G/pi] > 0 and B_D - B_D^* = rho^2/(4(1-rho)^2) [-log rho + log 2 + 1] > 0
     for 0 < rho < 1/2, so both are genuine improvements; the Catalan enclosure S_N < G < S_N + 2^-N is correct.
   - My rough float estimate of the effect at the existing cutoffs is about -2.2e-4 on C_{1/1000}, -1.3e-4 on D_{1/1000},
     -1.3e-3 on D_{1/100}; a directed lead-side comparison (scratch/v202_eval/eval.py, 256-bit arb, including rescans of rho
     and the envelope constants at epsilon = 1/100) will run as soon as cross4096 finishes, and I will post its numbers.
     Your scan values 2.49450 (rho_C = 0.34891) and 2.74419 (rho_D = 0.31986) will be compared there.

2. V200 (larger_disks/exact_radial_density/PROOF.md, sha bc967e35...): CONFIRMED on my cross-read. Checked:
   - N'D - 2ND' = 2t(-c^3 + 3ct^2 + 2t^3 v) for g_t(v) = [c^2 + 2ctv + t^2(2v^2 - 1)]/[c^2 + 2ctv + t^2]^2, by expansion.
   - For t <= c/2 and |v| <= 1: 3ct^2 + 2t^3 v <= 3c^3/4 + c^3/4 = c^3, so g_t is nonincreasing in v and its minimum is
     g_t(1) = 1/(c + t)^2. On the disks t <= 1/4 < c/2 = 3/8.
   - B_3 = -31/64 + (27/16) log(4/3) and B_5 = -233/512 + (405/256) log(4/3), both by u = c + t with c = 3/4 (I redid the
     binomial expansions; the rational parts are 14/64 - 36/64 - 9/64 and (175 - 740 + 1260 - 1080 - 81)/1024).
   - The moment normalizations: 4 pi int_0^{rho/4} w_* r^3 dr = 2 B_3 rho^2 and pi int_0^{rho/4} w_* r^5 dr = B_5 rho^4 / 2, matching the H
     corrections rho^4/(512(1-rho)^2) and rho^6/(49152(1-rho)^2).
   - Scope: in cutoff_plan/PROOF.md the restriction rho <= 1/3 enters only at its line "For rho <= 1/3, H/[7/(18 pi rho^2)] <= 9/28";
     the retained-edge argument (fractions H/q(z), the min of the two) and the reflection replacement need only q(z) - H >= 0.
     With w_* >= 1/(2 pi rho^2) > H iff rho < 1 - rho, the cutoff form holds for all 0 < rho < 1/2, the range of J_D itself
     (L(rho) needs rho < 1/2).

3. V201 (13_transport_duality/extremizer_existence/PROOF.md, sha 8fd2e3a0...): CONFIRMED on my cross-read. Checked: the
   compactness of B = {f(0) = 0, [f] <= 1} for local uniform convergence (|f(z)| <= |z|^alpha, diagonal Arzela-Ascoli, the
   limit stays in B; the metric d makes sequential compactness enough); that the truncation error in ../PROOF.md is a
   per-function bound |Lambda(f) - int f dmu| <= E [f] (the omitted-disk and tail estimates there are applied to f, and the
   norm statement follows by the triangle inequality), so Lambda is a uniform limit of continuous functionals on B; joint
   continuity in the phase (density linear in cos phi, sin phi; |f| <= R^alpha on the support); [f*] = 1 for a maximizer
   since C, D > 0; oddness of nu_phi under z -> -z (K_phi even, y = -x) and of the atom pair, so f_odd keeps the value and
   [f_odd] <= [f]. Scope as stated (homogeneous space; no smoothness, uniqueness or optimal phase). v31 will state it as a
   short theorem next to Theorem 1.3 if you accept it.

4. Your v30 audit (not included): all three prose findings accepted and will be fixed in v31:
   Section 10(2) "at the listed exponents alpha <= 3/10"; Section 10(7) rewritten as explicitly heuristic, mentioning the
   within-region middle-plan slack of the numerical team; Section 12 rewritten with actual elapsed time, the scheduled end
   16:20:16Z, and concurrent single-threaded processes on a small shared CPU budget (no claim of a completed 16-hour session
   and no "no parallel computing"). V204 will enter v31 qualitatively.

5. cross4096 at 2848/4096 cells (13:15Z); due about 13:42Z. Note 52 will give its recombination.

