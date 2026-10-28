# S2 independent verification handoff

Updated at 2026-10-28T18:14:16.287302+00:00. Current through V312. Final receipt snapshot PASS at 18:13:40 UTC.

The publication snapshot was checked from 18:11:12 to 18:11:15 UTC on 2026-10-28. Its receipt-copy refresh was checked from 18:13:37 to 18:13:40 UTC. Exact times and scopes are recorded below. The scheduled deadline is 18:20:16 UTC; that deadline is not an observed process end time.

No unconditional existence theorem for the requested full-plane profile has been established. No actual global continuum inverse or quantitative complement inverse has been certified. The exact moving-tail conditional existence theorem is confirmed, with base low injectivity and quantitative high-norm smallness still open. None of the counterexamples proves nonexistence of a profile.

The main analytical progress is actual low and variable-order high Fredholm theory, uniform inverse theory conditional on base injectivity, exact local origin and source results, and explicit global range obstructions for several Hölder targets. The main numerical progress independently confirmed here is original-data strain and coefficient bounds, residual enclosures, exact input Grams, and finite-section input comparisons. Output singular values from the large sections remain floating observations.

## How to read the files

Read [THEOREM_MAP.md](THEOREM_MAP.md) first. It groups the results by mathematical question and directs the reader to complete informal proofs. [VERIFICATION_RECORD.md](VERIFICATION_RECORD.md) is the chronological claim-by-claim ledger, with methods, verdicts, dates and evidence. [proofs/INDEX.md](proofs/INDEX.md) lists every topic. Binding audit clarifications are kept beside the original proofs so that audited source hashes are preserved.

A `CONFIRMED` verdict is limited to its exact claim. Some entries confirm a conditional theorem, a floating-data accounting check, or an input form only. They do not silently certify every conclusion mentioned in the same topic. Old `OPEN` and `DERIVED` statements are historical when a later ledger entry resolves them. The original conditional-existence proof predates the later residual norm enclosure.

## Background and provenance

The accepted raw X3 density and the exactly joined, scalar-normalized modal trial are distinct. The new global theorems use the latter. The exact exponent is

`k = 1615536043799051 / 9007199254740992`, with `ell0 = 1/k`.

The supplied source is at commit `78d87a0`. V001 copied the full case1 and analysis1 trees into this team. V285 rechecked every one of the 4,530 initial manifest paths against both the read-only source and the research copy: all hashes and byte sizes match, 113,548,373 bytes per tree. This checks listed-file identity, not mathematical validity or absence of unlisted files. The final check is certificates/source_integrity_final.json (machine-specific, not included; SHA-256 in NOT_INCLUDED.txt at the top of this folder), SHA256 `f5d31d987688b1d5dd1bd5863cea41745dde7072f6625524c37b5bd871ba6b56`.

Actual model records identify this team as `second-model referee`, the theory author as a separate model instance, and numerics as a separate model instance. Collaboration with independent occurred throughout by exchanging proof findings and counterarguments through the shared team files. Its complete audits were read and checked before adoption, and binding qualifications were retained. This team made no remote model calls. A second precision using the same source or cache is described as a consistency replay, not a second independent data source.

## Results that can be used

1. **The conventions and normalized equation are fixed.** The canonical velocity has no added harmonic strain. The physical central strain is `c=psi_xy(0)=-partial_x U1(0)=partial_y U2(0)`. Unit cubic normalization gives `3 ell-c=1`; the scalar variation is `c[h]/3`. The full leading cubic coupling cancels only after including that variation. The source-point nonlocal term and the spatially varying rank-one term are retained. Moving the far exponent introduces a logarithmic direction, handled by the exact moving-tail chart.

2. **Earlier obstructions have been audited against their actual hypotheses.** The raw X3 strain certificate verifies the saddle and origin-energy hypotheses. The stated weighted center quasimodes and nonclosed normalization results apply to their specified realizations. The negative potential-energy direction refutes that coercive pairing, not every inverse estimate. A frozen singularity is not transferred to the actual coupled inverse merely by saying the coefficient error is small.

3. **The Sobolev route has qualitative Fredholm theory.** The actual low realizations and the specified variable-order high scalar/remainder realizations are Fredholm of index zero. Small perturbations in the exact moving-tail family have uniform inverse bounds if the base low operator is injective. No numerical constants needed to establish that injectivity or the nonlinear contraction have been supplied. The archived residual's knot regularity is compatible with order `25/4`, not arbitrary high order.

4. **The Hölder route has both local theorems and global obstructions.** Local origin/source extension inverses and cutoff maps are confirmed. On `E2` and every residual-compatible `Y_gamma`, `gamma>4k`, the three maximal operators `T`, `Lren`, `A0` have infinite algebraic cokernel. The first scaled target also fails globally. The scaled quadratic-axis target has a full-operator non-surjectivity result for `alpha>1/2`. The joint-cofactor target avoids those particular packets and has a confirmed auxiliary exterior inverse, while a global inverse remains open. Transport alone has an independent source obstruction for `alpha>1/A_s` on both latter targets. No assertion that the actual residual is outside any range follows.

5. **The semilinear graph contraction fails in the stated weak topologies.** The constructed packets satisfy the required memberships and constraints. This does not refute the separate quasilinear high/low iteration. Completing a Hölder graph with an additional jet norm creates an invisible scalar unless the physical identification is proved.

6. **Avenue IV remains an input and finite-matrix result.** Exact input norms and high-conforming subspaces have been established. The large sections use projected `S1` core images after the exact jet split and low norms. Their output division and quadrature are not certified. Positive finite matrix values, poorly conditioned coordinates, a numerical near-null vector or removal of columns do not settle the continuum inverse.

## Independently confirmed numbers and their limits

The linked proofs define the norms and backgrounds exactly. Decimal endpoints in rigorous inequalities are exact rationals rounded in the stated direction.

| Quantity | Confirmed value and scope |
|---|---|
| Raw X3 strain | `15.726087821623500282 < c[X3] < 15.726087821623500289`, V018. The raw normalization defect is nonzero and about `1.0301e-8`. This is distinct from the repaired modal trial. |
| Actual modal axis rate | `d >= 5.5752` globally, V077. |
| Original anisotropic coefficient margin | `m_a >= 3` on the whole plane, with both traces at the weight join, V259. This is a coefficient inequality, not an inverse bound. |
| Radial coefficient margin | `m_R >= 5/2`, V086. |
| Decoupled family at angular parameter 4 | `margin >= 1.2501`, V191. The numerics team's sharper `1.250190` remains a one-team result; V259 does not verify those digits. |
| Low strong-target residual | `6049.11 < norm(F0)_Y < 8601.42`, V164, in its specified scalar/remainder norm. |
| Fixed high residual norm | `38666592266 < eta_* < 6.321e129`, V192 and V182. The upper bound is deliberately loose. Norm conventions, cutoff and dyadic normalization are fixed in proof 177. |
| Pure 78-column input section | All exact input Gram entries and positive definiteness, V202. High input and graph intersections have 66 and 60 columns, V220. |
| Shifted 38-column input section | All 1,444 Gram entries and 38 strain coefficients, V267. High input and graph intersection dimensions are 32 and 29, V275. |
| Floating versus exact input form, pure section | Relative form error `< 2.688e-6`, V252. Input side only. |
| Floating versus exact input form, shifted section | Relative form error `< 0.000431058`, V277. Input side only. |
| Exact strain hyperplanes inside the shifted section | Exact kernel dimensions 37, 31 and 28; projection distance `< 6.244e-16` in each inherited low input metric, V282 and V291. Exact binary-row kernels are compared; a computed floating nullspace basis has its own additional error. |

The completed three-mode pure section has floating smallest value about `2.76555`; the shifted 38-column section has floating smallest value about `4.74813`. These are not certified singular values. The shifted section's printed range `[3.74,5.59]` comes from an accumulation-only model, not a rigorous output enclosure. Its binary strain-nullspace is not exactly the source-defined strain-nullspace. High-conforming restrictions still use low input and output norms. The smaller values' concentration in outer coordinates does not prove they are artifacts, as the exact counterexample V279 shows.

## Closure remains conditional

The exact theorem V178 assumes:

- `(I)`: injectivity of the stated base low operator;
- `(S)`: some `0<r<=r_*` with `K_H eta_H<=r` and `K_L C K_H eta_H<1`;
- for final unit cubic normalization by dilation, `abs(J(h))<1`, with its stated sufficient bound.

All quantities refer to the theorem's fixed chart and compatible norms. Actual `(I)` and `(S)` are open. A large certified residual alone cannot decide `(S)` because the inverse and nonlinear constants also enter it.

Necessary scalar tests are confirmed for actual high-domain directions d with c[d]!=0. With the exact residual-subtracted image `R_d`, `(I)` and `(S)` together require `norm(R_d)_YH > 1956082280 abs(c[d])` and the relative lower bound `>0.0507 eta_* abs(c[d])`. A certified violation would refute the conjunction and hence `(S)` under `(I)`. It would not prove nonexistence of a profile. The scaling tangent is not an admissible high-domain test.

There is now an exact admissible test: proof 241's Gaussian density `d=-Delta v` has `c[d]=1`, `J[d]=0`, zero scalar input and membership in the actual high graph domain, V283. Its canonical velocity is explicitly `(-v_xy,v_xx)`. Every summand of `A0 d=Lren d+m0` and `R_d=Lren d+m0-F0/(ell0 n'_0)` belongs to the high target. Neither high norm has a certified upper bound. That is a concrete remaining calculation, not a completed rejection of `(I)` or `(S)`.

The corrected local axis identity in [proof 247](proofs/247_axis_test_identity/PROOF.md) is CONFIRMED after the complete independent follow-up, V296. Its original Gaussian specialization remains REFUTED: the canonical trace is `-g''`, not `2g-g''`. Read all binding sidecars, especially the [correction](proofs/247_axis_test_identity/AUDIT_CORRECTION.md) and [adoption](proofs/247_axis_test_identity/AUDIT_ADOPTION.md). A global extension retaining all cutoff terms is derived in [proof 248](proofs/248_global_axis_test_identity/PROOF.md), V298/V301, and is CONFIRMED after independent audit with its binding adoption. Neither identity supplies a high norm.

The exact knot-jump identity in [proof 249](proofs/249_exact_knot_jump_test/PROOF.md), V302/V307, is CONFIRMED after independent audit. Read its binding [adoption](proofs/249_exact_knot_jump_test/AUDIT_ADOPTION.md). It computes a derivative-jump ratio at a certified nonzero knot, with no high-norm ratio or bound. All late theorem audits have been resolved.

## Late audits and publication check

The sharp coupling tails are now CONFIRMED after actual independent audit, V286 and V287. For `0<alpha<1`, the full `C0` tail has norm comparable to `R^(2k-1) log R` on `E2` and `R^max(2k-1,2k-gamma/2) log R` on `Y_gamma`, `gamma>4k`. The renormalized `Cren` has sharp rate `R^(k-1) log R` on every one of these spaces, even on exact `ker c`. The restriction of `C0` to `ker c` has the same faster rate. All constants are qualitative. Proof 244's binding sign clarification and adoption are part of the theorem.

The exact strain-hyperplane theorem of proof 246 is CONFIRMED after actual independent audit, V291. The original 640-bit certificate, independent 768-bit direct solve and fractions-only audit agree. Its binding clarification separates exact kernels of the binary row from floating nullspace bases, and records the complete input provenance. No output singular value is transferred.

The eight theory author publication documents were fully reviewed through the 18:11:09 UTC snapshot, V311. All mathematical repairs are applied, including the exact axis and cubic-cofactor definitions, signed cutoff derivative and nonzero-strain conditions. All theorem audits are resolved. The final time update matches the three shift logs and leaves the final shifts ongoing at the stated observation time. FINAL_REPORT matched the main report, SHA256 `f6ea65d62ce02196a761f8387f426ab08faafa9117b0e99b6ce8f3f2a8e634a2`.

V310 checked the complete primary ledger sequence through V309 and every one of the 249 standalone proofs. All 252 reading-index links exist; the existing proof 234 entry now links directly to its proof. This is a file-inventory check, with no new mathematical assertion.

V311's publication certificate (machine-specific, not included; SHA-256 in NOT_INCLUDED.txt at the top of this folder), SHA256 `5220e1fc9b91584b06fe3b165ab52720f581ebc5edf70e056b680f66ca4594b4`, records a PASS from `2026-10-28T18:11:12.998863+00:00` to `2026-10-28T18:11:15.430970+00:00`. All 1,603 manifest entries, 1,500 source-copy comparisons, 1,278 small proof files, 24 large-file omission records, 301 explicit hash relations in 28 typed audit records and 335 handoff links passed, with no errors. The manifest stayed unchanged during the check, SHA256 `683b701f8f6181a38396571957a79d67988154a8978436a58666e5cadd2061ae`. All 249 proof topics were present. The checker ran locally in 2.432 seconds and executed no proof or numerical code.

V312 then checked the receipt-copy refresh from `2026-10-28T18:13:37.764074+00:00` to `2026-10-28T18:13:40.197063+00:00`. The receipt certificate (machine-specific, not included; SHA-256 in NOT_INCLUDED.txt at the top of this folder), SHA256 `c986f2c5e0afa09e93a3280365d80e8d11828112333032348f891ffcc8899945`, records zero errors across 1,604 manifest entries, 1,501 source-copy comparisons, the same 24 omissions and 301 registered hash relations, and 336 links. The V311 certificate and updated handoffs were present and identical; all eight report hashes were unchanged. Its stable manifest hash is `e8fb3a3831856e8111fa1c11cbbb5af3a17076456d3eeed798ed6f26d63f8219`. This confirms the previous receipt's archival copy. The new V312 receipt was written afterward and is not claimed to have checked itself.

The earlier preflight certificate (machine-specific, not included; SHA-256 in NOT_INCLUDED.txt at the top of this folder), V295, retains its failed current-copy verdict because eight source files had changed after that earlier package was assembled. The final refresh resolved those differences. Both records remain available.

The PASS concerns the observed payload and listed checks. It does not assert future file identity, certify every historic untyped hash, or include the check's own subsequently written certificate and ledger receipt as inputs. Those receipts can be archived afterward. File identity does not replace mathematical review. Omitted caches and original sources remain external replay inputs.

No JavaScript or TypeScript, server, cluster, GPU or proof-assistant build was used in this team. Computation was local; after the CPU restriction it was one single-threaded calculation at a time. No source or sibling-team file was modified. The final chat is not part of this handoff.

