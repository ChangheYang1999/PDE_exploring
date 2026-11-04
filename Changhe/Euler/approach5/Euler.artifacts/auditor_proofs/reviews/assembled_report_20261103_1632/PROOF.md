# Assembled-report changes at the 16:32 snapshot

## 1. Exact object and reading coverage

The object is in the team records, captured at 2026-11-03T16:32:18.318929+00:00, 6148 lines, SHA256 8b3ae744354b37d5ff99b3223e3b819b23eca44d77a7120d72bf4b435ba3f39a. Every change in the team records was read, including the seven changes to proof sections 2A and 2D. The entire new Theorem 8 statement and proof outline were read. The comparison baseline is the 16:18 snapshot reviewed in A1642-A1647; its complete reading history, including all appendices and the earlier fresh complete-proof checks A1217-A1220, is a dependency. This is a cumulative complete-report audit, not a claim of freshly reading unchanged passages.

The equations, regularity and hypothesis tags are unchanged. The unrestricted decaying-profile question for 2/5<c<1/2 and arbitrary omega remains OPEN. Existing conditional and local conclusions retain their labels. CO64 is newly listed as SUBMITTED, not PROVED, and remains under a separate substantive audit.

## 2. Four requested repairs

All four repairs A1643-A1646 are correct. The stress is now T=-(V tensor V+P I)=(H-|V|²/2)I-V tensor V, H=|V|²/2-P. Its eigenvalues are H-3|V|²/2 and twice H-|V|²/2. The exact crossover is cstar=(2/3)(1-sqrt(tstar/3)), tstar=(15sqrt(7)-20)/42. The regular-node order is measured in H-Pinf. Theorem 3(f)'s smoothness or nonvanishing-vorticity alternative is present in the scope table. The proofs and algebra justifying these replacements are in the preceding review.

## 3. Nine-row threshold and combined criterion

The hypotheses of Theorem 8 are U in C2, P in C1, divergence-free rotating profile, any real omega, bounded U with U(R.) tending to zero in distributions. Part (a) assumes bounded W=curl U. Each exact row (c_k,T_k) is copied correctly:

    (0.41,0.894), (0.42,0.870), (0.43,0.847),
    (0.44,0.825), (0.45,0.803), (0.46,0.779),
    (0.47,0.756), (0.48,0.731), (0.49,0.707).

Every decimal in this table is rational and exact. The independent proof and exact positive endpoint certificates are in the team records, A1633-A1635. For g=bt+qt² the density h/t is a strictly concave cubic on the positive interval, with positive endpoint values; hence it has no root there and is positive. The proof needs no new Sturm computation. Since partial_c h=-3g<=0, positivity at c_k implies positivity at every 0<c<=c_k. The cutoff square-completion proof includes sup|W|=T_k. No far-field-only hypothesis is substituted.

The stated step function T(c), taking T_k on c_(k-1)<c<=c_k and sqrt(tstar) on 0.49<c<=1/2, is therefore a valid weak threshold. It exceeds the old strict linear threshold everywhere on 2/5<c<=1/2: on c<=0.49, T(c)>=0.707 and 0.707²>0.48=3(1-3(2/5)/2)². On c>0.49, the linear threshold squared is below 3(0.265)²<0.4, whereas tstar>0.4 follows from sqrt(7)>5/2. These are exact inequalities. The endpoint and optimality qualifications are correct. No optimality or unrestricted nonexistence follows.

## 4. Four energy-section clarifications

The final energy constants and the intermediate constants are now distinguished correctly. The pressure Poisson calculation uses cancellation of the two rotational divergence terms; the bounded-background argument also uses orthogonality of exp(t omega J). The three displayed energy cancellations alone were not an exhaustive account of rotation throughout section 2A.

Let pstar=3c/(1-c), k=3/pstar and alpha=3-2k, with 2/5<c<1. If |U(x)|=o(|x|^-k), then on A_R={R<|x|<2R},

    ||U 1_A_R||_(pstar,infinity)
        <= |A_R|^(1/pstar) sup_A_R |U| = o(1),
    R^-alpha integral_A_R |U|² = o(1).

Thus little-o decay implies both shell criteria. The old blanket incomparability sentence was false and was missed in the earlier complete-proof reads; it is corrected in this snapshot. The remaining incomparability with the global finite-secondary-index Lorentz condition is valid as a function-space statement. A smooth radial field with size r^-k/log log r at large r satisfies little-o but no L^(pstar,q), q finite, since its rearrangement yields a divergent integral of (log log t)^-q dt/t. Conversely disjoint smooth unit-radius bumps centered at exp(n)e1 with heights exp(-kn) have finite L^pstar mass but their peak values do not satisfy little-o. These are function-space tests, not Euler profiles.

For an exact homogeneous tail pasted to a bounded interior, E(R)=L R^alpha+C0. The refined error O(R^(5-3/c)) forces C0=0 exactly in the stated range 2/5<c<3/5. The new explicit range avoids extending this inference to a nondecaying error. These clarifications change no argument used in the target interval.

## 5. Three coverage-section clarifications

The A399 quotation now specifies full-flow-ergodic invariant probabilities not concentrated on the closed invariant set Z={B=0} union {Omega=0}. Ergodicity makes their mass on Z zero. On the compact core, recurrence to {|B|,|Omega|>=1/j}, together with D Psi_t B=B composed Psi_t and D Psi_t Omega=exp(-(1+c)t)Omega composed Psi_t, gives directional exponents 0 and -(1+c). The determinant exp(-3ct) supplies the remaining exponent 1-2c. This is exactly the source class; no time-one ergodicity or logarithmic integrability is assumed.

The cutoff in A312 is now specified exactly as in `auditor_proofs/proofs/finite_regularity_vortical_coverage/PROOF.md`: smooth radial, one near the trapping ball, positive before the outer radius, zero beyond, and with the outward radial inequality outside the trapping radius. Consequently omega Jy-rho(cy+U) agrees with -B on all trapped orbits, and its derivative growth uses only sym D[-rho(cy+U)]. The restored conditions are necessary to the quoted construction.

Remark 36 now distinguishes what Lemma 12 uses from the stronger almost-everywhere consequence of Lemma 11(c). Positivity of |(B cross Omega).e^u| on the relevant unstable arc implies Omega is nonzero there. Lemma 12 needs only the earlier conditional-density statement. No zero-set or support exclusion is added to the theorem.

## 6. Remaining exactness typo and report-level verdict

Appendix A still writes `sqrt(t*) = 0.68463` in the C57 row. This literal equality is false; use `sqrt(t*) is about 0.684632, so 0.68463 suffices`, as in the corrected front statement. It does not invalidate the theorem, whose exact algebraic constant and weak endpoint are correct. It is the one remaining concrete correction before unconditional approval of the exact pinned report as a whole.

A1666-A1669 confirm the four repairs, the threshold addition and all seven proof clarifications. A1670 refutes only the retained literal decimal equality. A1671 leaves whole-version approval OPEN pending that one-word approximation repair. All already confirmed theorems retain their exact hypotheses and verdicts. The older blanket little-o incomparability is expressly withdrawn in Section 4, so the audit history must not be read as continuing to endorse it.

No mathematical computation was run in this review. The recorded exact table computation remains the one from 16:14. The configured model coordinator's checked notes were read and independently verified; configuration is not runtime model attestation. No new model client, agent, external write or prohibited execution was used.
