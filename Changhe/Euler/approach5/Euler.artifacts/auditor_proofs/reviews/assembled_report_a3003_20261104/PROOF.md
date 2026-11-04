# Transfer of the ambient vector counterexample at cutoff A3003

## 1. Exact scope

This audit concerns only the pinned report with SHA256 4738c2d9f841dc3ac01f10a69883cfb1789a41479374d3e1109b5c77da21d6e9. Its predecessor is the report 7cbff5a2 approved in A3003 at cutoff A2998. The new cutoff is A3003. The live reports had already advanced to cbcc4cbe when this audit captured them; this approval does not automatically cover that newer text.

The submitted normal difference and the independently recomputed difference have the same four changes: status line, summary approval history, the LIT338 row in Appendix A, and two added historical records in Appendix C. The changed mathematical passages were read individually, with semicolon-level comparison of the long row. All four complete main proof sections 2A through 2D are byte-identical to the predecessor.

## 2. Mathematical transfer

The new paragraph states the counterexample of A2999 with every required quantifier. For each integer k >= 1 and real C > 1/4 it constructs a map on a ball about the origin in C^k with values in C^(2M), where finite M may depend on k and C. The map is smooth, nonzero away from the origin, and flat there. The bound concerns the Euclidean norm of the entire array of derivatives with respect to the conjugate variables. It is not a bound on just one derivative. These are exactly the hypotheses and conclusion checked in the independent proof at in the team records.

A2977 gives vanishing for the endpoint coefficient 1/(4|z|), for each finite target dimension, under distributional local integrability and infinite integral order. The smooth examples meet all those regularity and flatness conditions. Since examples exist for every larger constant when target dimension is free, the threshold 1/4 is sharp in that class. This does not require that M be independent of C.

For a ball of radius R in real dimension d = 2k, the coefficient b(z) = C/|z| has distribution function

    measure{b > t} = v_d min(R^d, (C/t)^d).

Hence sup over t > 0 of t measure{b > t}^(1/d) equals C v_d^(1/d). Each example therefore has a coefficient of finite weak-L^d norm. The existence of even one such nonzero flat example refutes continuation for every coefficient of finite weak-L^d norm in the vector class. It does not refute a small-norm theorem, the scalar theorem, or a statement restricted to a smaller target.

The phrase "LIT354 alone" correctly qualifies the earlier absence of a higher-dimensional sharpness conclusion. The final limitations in this paragraph concern LIT356, exactly as A3002 did at this cutoff. The subsequently confirmed fixed-target construction A3005 strengthens that separate issue, but is not contained in this pin. No logarithmic sharpness in several variables or Euler-profile conclusion is imported.

## 3. Evidence and report labels

The row names the independent proof and the existing C and coordinator comparisons. A3001 already checked the C comparison with its finite-sample qualifications. A3004, recorded after the report cutoff, additionally checked the coordinator comparison: its six diagnostics are numerical and furnish no proof premise. The transfer here follows the analytic construction, not the diagnostics. The configured collaborator models are recorded in the team records; actual provider execution remains independently unattested.

The new summary correctly attributes approval of the preceding assembly to A3003 at cutoff A2998. The two changed historical records accurately describe A2999-A3003 and do not claim self-approval. The static label check at 2026-11-04T06:09:07Z found 2511 distinct positive references and 222 explicit confirmed lists, with no missing verdict or nonconfirmed verdict in those lists. The document check found nine tables with 582 data rows, no malformed row, no absolute local path and no em dash. These checks establish syntax and reference consistency only.

## 4. Verdict and limitations

The transfer is confirmed. Cumulative approval extends to the front matter, main Sections 0-10 and Appendix A at cutoff A3003, with all existing conditional hypotheses and external-source exclusions. Historical Appendices B and C are not collectively certified; only the changed historical passages are checked here. This is an approval of an assembly of proved, conditional and open results, not a proof of the unrestricted Euler conjecture. That conjecture remains OPEN.

## 5. Additional C comparison

The C note of 2026-11-04T06:10:14Z was read in full. Its four items agree with Sections 1-4: the qualification of LIT354, the exact finite-target quantifiers of LIT356, the weak-norm scope, and the absence of higher-dimensional logarithmic sharpness. Its prospective fixed-target wording is exactly the refinement confirmed separately in A3005. The note does not establish any new Euler hypothesis. Its mention of the earlier diagnostic is not treated as mathematical evidence. The note is retained in the team records.

## 6. Fixed-target transfer in pin cbcc4cbe

The next pin has SHA256 cbcc4cbe6f504be3de8949211373dfc50b2c72143641c2c15c0388dbe7d8f947 and cutoff A3007. The independently computed difference from 4738c2d9 has three changes: the status, the same Appendix A row, and one new historical entry. A word-level comparison of the entire changed row was read, including the proof-path and comparison additions. The earlier semicolon-level display omitted some header changes; the full word comparison supplied them. Main Sections 0-10 are unchanged.

The new target statement is precisely A3005: for every k>=1 and C>1/4, the target is the fixed space C^(2k), independent of C. The construction uses coordinate powers and a half-integer envelope, not simply the old angular envelope with a different finite cover; the report identifies the new construction by its source and does not claim the proof is obtained by a literal substitution. Appending zero coordinates preserves the function norm, full derivative-array norm, smoothness, flatness and nonvanishing away from zero. Thus the positive endpoint A2977 and this construction give sharp threshold 1/4 for every prescribed finite N>=2k.

The new limitation N<2k is correctly scoped to the construction at this cutoff, A3007. The separate target k+1 proposal has no verdict in this pin. A3002 remains a historically accurate limitation of LIT356 and is supplemented by A3007. The report does not claim failure at smaller targets or any Euler conclusion. The new positive verdict in the confirmed list is A3005, actually confirmed; A3007 is placed in the open list. No table delimiter or other row content changes.

The new history correctly records A3004-A3007, including the numerical nature of the coordinator's six diagnostics. Its sentence "the same maps" is read with the immediately stated new coordinate-power construction as maps having the same asserted properties; it is not an identity between the two constructions. The summary continues to attribute the previous assembly approval to A3003 and does not claim approval of itself. Both live report files matched cbcc4cbe at capture time.

Cumulative approval therefore extends to this exact pin at cutoff A3007 with the scope of Section 4: front matter, main Sections 0-10 and Appendix A, retaining all conditional hypotheses and external-source exclusions. Historical Appendices B/C are not collectively certified. The main conjecture remains OPEN.


## 7. Approval-history revision 3fec00b9

The pin 3fec00b93d0dba2e1300c88be88c7c9c20f29594e9bd20ac8f153f34d5b2d51a differs from cbcc4cbe only in the status line, summary attribution of the preceding approvals and a new Appendix C history entry. The complete independently recomputed difference was read. No mathematical claim, table or verdict list changes, so the successful unchanged checks were not rerun.

The summary now names the 06:08Z assembly at cutoff A3007, correctly approved by A3009, and adds the intermediate A3008 to its history. The new historical entry correctly distinguishes the 06:05Z assembly approved at cutoff A3003 from the 06:08Z assembly approved at cutoff A3007, and retains the exclusion of collective historical Appendix B/C certification. The complete C comparison of 06:19:37Z was also read and agrees on these details and the preceding fixed-target transfer.

Cumulative approval covers this exact pin at cutoff A3009, with the same front-matter, main Sections 0-10 and Appendix A scope and every prior conditional and external-source qualification. The later LIT358 construction is not part of this pin and is separately covered by A3011-A3013. This history update adds no Euler theorem.


## 8. One-spare-coordinate transfer in pin 3bcba1b9

The exact pin is 3bcba1b9dc1071a8868a4537effafd6af5b34deafb16b138d5977cbf01ca5607, at cutoff A3014. The independently recomputed difference from approved 3fec00b9 has four hunks: status, preceding-approval history, the LIT338 row and new Appendix C entries. Every changed short passage, every changed word span of the long row and the entire current long row were read. The initial row-name matcher found no row; the exact title-prefix matcher then uniquely located it and the full text is retained.

The mathematical addition is exactly A3011: for every k>=1 and C>1/4 the fixed target can be C^(k+1), with coordinate powers moved sequentially through a vacant coordinate. Zero padding preserves the full-array norm, flatness and nonvanishing, so the positive endpoint A2977 gives sharpness for each fixed N>=k+1. The older A3005 citation remains valid for its weaker N>=2k result; A3011 supplies the enlarged range. No assertion for N<=k is derived. The scalar, higher-dimensional logarithmic and Euler exclusions remain explicit and are correctly tied to A3013.

The new positive verdict is A3011, actually CONFIRMED; the added scope verdict A3013 is OPEN. The new proof path and C/coordinator comparison references match the retained sources, whose diagnostic limitations were checked in A3012. The report's history accurately describes A3010-A3014. The complete C comparison of 06:27:08Z was read; all three items agree, including the target range and diagnostic limitations. Main Sections 0-10 are byte-identical to the preceding approved pin. The changed row has the same delimiter count; there are no absolute local paths or em/en dashes. Successful unchanged full-reference and table checks were not repeated.

Cumulative approval covers this exact pin at cutoff A3014, for the front matter, main Sections 0-10 and Appendix A with every prior conditional hypothesis and external-source exclusion. Historical Appendices B/C are not collectively certified. This is a delta review, not a fresh reading of the entire million-byte report, and supplies no new unrestricted Euler conclusion.

## 9. Analytic-interface transfer in pin b948ca7d

The exact pin is b948ca7d8e65a57f6c8f042857fe1ecb05e968f834218553fbf55c6f6ff7f6ad, with cutoff A3022. The independently recomputed six-hunk difference from 3bcba1b9 was read in full. The mathematical changes are one clause in the Theorem 5 heading, a remark after Proposition L0, and a new Appendix A row. The other changes update status and approval history.

The new conditional statement matches A3015. Its bounded C^2 velocity and C^1 pressure, 0<c<1/2, every finite omega, E(R)=o(R), continuous-time basins, essential domains, simple exponents and entropy agree with the independent proof. The report's (CI-4) is redundant: its Lemma 11(b), with the exact external input A2948-A2949, derives the required positive unstable densities from (CI-1)-(CI-3). Adding that listed condition therefore does not weaken or misstate the proof. All uses of basin coverage and one helicity sign remain explicit.

The coordinator's separate deduction from the energy law is correct. Decay implies Hb, and for 2/5<=c<1/2 the energy law gives E(R)=o(R), including the finite-energy endpoint. Hence the new conditional statement includes Proposition L0. The stronger observation of Theory Agent A A109, that Hb and E(R)=o(R) are equivalent for bounded profile solutions throughout 0<c<1/2, is proved separately in Section 12 of the analytic-interface review. It is not needed to approve this pin.

The phrase "o(R^3) square mean" is read as the unnormalized square integral in that review's Section 4; the volume-normalized square mean tends to zero. The report should use the explicit integral wording in its next revision. This qualification changes no estimate, theorem or hypothesis. The diagnostic description agrees with A3016 and does not turn its finite sample into a proof.

The entire A109 note and its addendum were read. A109 examined an intermediate pin ca8c6189, which was not available at the stated path during this audit. Its mathematical comments were checked directly against b948ca7d; no comparison with the missing intermediate file is certified. The preceding approved pin and b948ca7d were available and compared directly.

The new history accurately records A3015-A3022. The three unavailable 2023 manuscript DOIs are absent; the title and author-context search found no use of their unseen main theorems. The report's separate Chae-Wolf local BKM references concern the older sources, not an unseen 2023 proof. This check does not certify the missing papers or a new source inventory. The new table row has six delimiters. No absolute local paths or em/en dashes occur in this pin. Successful unchanged reference checks were not rerun.

Cumulative approval covers this exact pin at cutoff A3022, for front matter, main Sections 0-10 and Appendix A, retaining all prior conditional and external-source qualifications and the explicit square-integral reading above. Historical Appendices B/C are not collectively certified. The unrestricted rotating conjecture remains OPEN.


## 10. Energy-premise precision and angular recheck in pin 2870a413

The exact pin is 2870a413b58c059f7bfbb89352e9ae02e14d6e84a20c7e6e5ca71376d2fa42da at cutoff A3027. The full independently recomputed difference from b948ca7d has 123 lines and eight hunks. Every changed passage was read, including all three changed Appendix A rows and the complete new wording in the analytic remark. The relevant preceding kernel statement (4b), support statements (5a)-(5b), and torque statement (5c) were read in context. In the assembled report these numbered working-ledger statements are in historical Appendix B, not in the main Section 5. The changed paragraph there is checked individually, without certifying the entire historical appendix.

The analytic remark now correctly states that the Bernoulli function minus the pressure constant has square integral o(R^3) over B_R. It states Hb equivalence only for bounded solutions of the full profile equation in 0<c<1/2, and retains the measure and helicity-sign assumptions of the conditional theorem. Its direct estimate R^-3 E(LR)=o(R^-2), the separate energy-law converse, and the already-zero range below c=2/5 agree with A3026 and A109. The unchanged Theorem 5 statement remains the smooth decaying helicity-sign result; its revised heading does not replace the explicitly bounded hypothesis of the additional remark.

The angular additions accurately cite A3023-A3025. The new attribution to A073-A074 concerns the support and odd-symmetry results, and the addition beside A046 concerns only the linear kernel. Neither attribution claims a fresh proof of every other result sharing its row. The mode equations and torque formula behind (5a)-(5c) and the linear kernel in (4b) were indeed reconstructed. Their distinct decay and parameter hypotheses are preserved. The no-nonexistence conclusion in the new paragraph is read as the unrestricted conclusion under discussion; the immediately following odd-symmetry exclusions remain valid conditional exclusions.

Status and summary correctly attribute the predecessor approval to A3027 at cutoff A3022. The new Appendix C entry also discusses an unavailable intermediate ca8c6189 build. This audit does not confirm the claimed exact difference of that missing build; it confirms the mathematical comments that A109 made and the direct b948ca7d-to-2870a413 difference. This limitation has no effect on the front matter, main proof sections or Appendix A.

All three changed rows retain six delimiters; the pin has no absolute local path and no em or en dash. Unchanged full-reference checks were not repeated. Cumulative approval covers this exact pin at cutoff A3027 for front matter, main Sections 0-10 and Appendix A, with every prior conditional and external-source qualification. Historical Appendices B/C are not collectively certified. No new unrestricted Euler conclusion follows.


## 11. Pressure-symmetry transfer in pin 37391724

The exact pin is 373917244ebdfb6698e63b7b9648b4528df16192d47a9d45fb46146da69946b3 at cutoff A3032, with 7196 lines and 1116729 bytes. The independently recomputed difference from approved 2870a413 has 182 lines and twelve hunks and agrees exactly with the coordinator's supplied difference. Every changed passage was read, including the complete new Theorem AP, its proof sketch, the surrounding hypotheses of Theorem 3(b), the Section 8 table header, and all changed Appendix A and B passages.

Theorem AP has exactly the scope confirmed in A3029: a C^2 velocity and C^1 pressure solving the full profile equation on R^3, uniform sublinearity, 0<c<1/2 and every finite omega, with actual pressure axisymmetric about the rotation axis, equivalently Gamma=(Jy).U identically zero. Its conclusion is U=b e_z and P=-(1-c)b z+p_0; decay gives b=0. The four-sentence proof sketch agrees with the full independent proof. It does not replace the detailed axis regularity and exceptional-root argument. The summary row inherits 0<c<1/2 from its immediately preceding sentence, and explicitly adds the regularity and sublinearity assumptions. The Section 8 row is under the header specifying extra assumptions beyond the classical baseline and decay.

Theorem 3(b) and the Section 5 bullet say that a nonzero decaying profile has nonaxisymmetric pressure. Under their C^2 classical baseline and decay, this is the contrapositive of Theorem AP and needs no extra pressure premise. It is therefore a proved necessary condition on a hypothetical nonzero profile. Without decay the axial constants would invalidate this phrasing; the revised report includes decay, as required by A3030. The separate question whether decay forces pressure symmetry remains explicitly unresolved. No Reynolds stress or angular averaging argument is asserted to answer it.

The new Appendix A row cites the correct A3029-A3032 scope and retains A3031 as OPEN. The individually changed B.5 and B.8 passages preserve their conditions. The complete coordinator comparison in the team records was read: its main ten analytical steps agree. Its suggested range extension, diagnostic computations and source-version chronology are not newly certified here. It was not an input to A3029, which was already recorded before this reading.

The status, preceding-approval sentence and history correctly identify the predecessor approval A3028 at cutoff A3027. The pin contains no absolute local path or em/en dash; the new Appendix A row has six delimiters. Successful unchanged reference checks were not repeated. Cumulative approval covers this exact pin at cutoff A3032, for the front matter, main Sections 0-10 and Appendix A with every prior conditional hypothesis and external-source qualification. Historical Appendices B/C are not collectively certified. The unrestricted rotating conjecture remains OPEN.
