# UNRESOLVED: independent verification completed under the 48-hour wall-clock cap

Final file fixed at the actual report cutoff T_end = 2026-10-22T12:43:58.033893+00:00. T0 = 2026-10-20T12:44:15+00:00. Elapsed wall time = 172783.033893 seconds (47 h 59 min 43 s). The file-write bracket and hashes are in FINALIZATION_RECORD.json. No accepted YES or NO endpoint has been established. The controlling limit was 48 wall hours; this is not a claim of 48 active research hours. The final session may close after this report cutoff; its end event is written by the outer shift loop.

The target is a smooth nontrivial profile on all of R2 with x-reflection symmetry only, Theta(0,y)=0, Theta=a0 x2+terms of degree at least3, a0 nonzero, beta>0, a sublinear canonical velocity and polynomially controlled tails. Neither y=0 nor a numerical box is a physical boundary. The broad target is not replaced by positivity, analyticity, bounded temperature or finite energy.

The chronological item-by-item verdicts are in the chronological verification report (not published; its verdicts are summarized in the main report). The mathematical and computational reading-order index is [proofs/INDEX.md](proofs/INDEX.md); the [complete catalog](proofs/CATALOG.md) supplies chronological navigation. Each result's PROOF.md states its hypotheses, argument, dependencies and scope. This summary does not enlarge any packet's verdict.

## Equations, inverse and center

The audited equations are

    W.grad Omega + Omega = Theta_x,
    W.grad Theta = (beta-2) Theta,
    W = beta X + U(X)-U(0),
    -Delta Psi = Omega, U=(-Psi_y,Psi_x).

Thus curl U=-Omega. The relative whole-plane velocity is

    V(X) = integral [K(X-Y)-K(-Y)] Omega(Y) dY,
    K(Z)=(Z2,-Z1)/(2 pi |Z|2).

[The inverse proof](proofs/03_inverse/PROOF.md) establishes absolute convergence for power-decaying smooth vorticity and uniqueness among sublinear div-curl velocities up to a vertical constant. [Backward transport](proofs/01_transport/PROOF.md) first excludes beta<2. For beta>=2, [the polynomial-tail reduction](proofs/40_polynomial_tail_reduction/PROOF.md) proves that possible profiles in the prompt's broad polynomial-tail class have the decay needed by the inverse. This is an equivalence of solution classes, not of arbitrary fields.

The lead selects U=V and v0=0, the observer in which the marked material center is stationary. This is a declared regularized inverse, as the prompt permits. It does not impose a B1 integral-moment condition. Any other vertical observer drift requires the exact translation of all physical fields given below; it is not a fitted transport parameter. For every nontrivial profile in the target class, the sector circulation theorem proves absolute divergence of the ordinary center-component integral. This absolute-divergence argument does not decide convergence of a signed circular truncation. The uniform angular tail separately gives v0(R)=B R^(1-1/beta)+o(R^(1-1/beta)); B is the first cosine moment divided by 2 pi (1-1/beta). If B=0, that leading theorem leaves convergence undecided. [P351](proofs/351_spec_absolute_and_signed_drift/PROOF.md) derives the coefficient and its positivity under the nonnegative right-half-plane hypothesis. When an ordinary inverse converges and is the selected convention, its center value must be reproduced.

Independent Taylor expansion gives c=Psi_xy(0)=1+beta/2 and Omega_x(0)=4a0/beta. The exact divided center defects are (beta+2-2c)a0 and (beta-c+1)b0-2a0. The [reconstruction proof](proofs/07_reconstruction_scaling/PROOF.md) derives zc=zstar-v0 tau^beta/beta and the required subtraction of that representative's v0. For an added vertical drift d, the physical translation is a(t)=-d tau^beta/beta: translate both scalars, translate velocity and add a'(t), and translate the material center. It also checks signed spatial scaling by any nonzero real factor, which changes a0 and v0 but leaves beta unchanged. These identities do not make an approximate field exact or turn unbounded initial data into bounded data.

## Independent numerical evidence

My evaluator reads the stored coefficient format independently with SciPy splines and angular recurrences. It differentiates scalar fields with seven-point Cartesian differences at two step sizes. The broad residual grids use separately implemented adaptive full-plane modal Green integrals. A second inverse integrates physical-space Duffy triangles and the complete compactified exterior for selected cross-checks and manufactured tests. The stored whole-plane continuation uses z=(1+(r/L)^2)^(-1/(2 beta_basis)) and t=1-z. Its radial spline factors are z^(beta_basis+2) for F and z^(beta_basis+1) for G; odd angular indices carry an additional r/sqrt(r^2+L^2). A forced source retains its own recorded basis parameters. The modal inverse integrates these represented fields to infinity and uses a once-subtracted first angular mode. This specifies the numerical tail closure, not an exact PDE tail. I did not import or execute the fitting lane's code. This is source and computational independence, not a claim that every broad-grid point received both inverse calculations.

[P313](proofs/313_consolidated_123_state_audit/SUMMARY.md) traces 123 keyed entries in 62 audit folders to the saved evaluator arrays: 121 forced-problem entries and two manufactured controls. They comprise 5904 regional measurement rows and 119 distinct source-archive hashes; four pairs deliberately reuse an archive. Actual radii counts are 145, 161, 166, 177 or 189, with 13630 to 18144 field-dependent points. The finite grid reaches radius 1e8. Cartesian axis ratios are omitted where parity makes them vacuous; divided axis equations and separate origin checks are retained.

The pointwise normalizer is the sum of absolute terms in each equation, with grouping documented in the evaluator. The forced transport variant changes the velocity in those same residual and normalizer terms. Computed N=R=0 gives ratio 0; N=0 with R nonzero gives infinity. There is no positive denominator floor. With N positive, the exact ratio lies between 0 and 1 by the triangle inequality; a value near 1 means poor equation balance. Underflow and roundoff remain floating-point limitations.

[P350](proofs/350_final_reading_order_audit/SUMMARY.md) checks the counter scopes directly. Across the 121 forced entries and both velocities, the regional masks retain no zero normalizers or infinite ratios. The original full grids contain 76012 zero thermal-normalizer sample instances, all on the axis, with exactly two per radius per entry and velocity. These are repeated sample instances, not distinct spatial points. A separate exact polynomial control gives 25 field/step/point instances with ratio 1 from tiny roundoff terms where the true normalizer vanishes. That polynomial has a nonsublinear velocity and is a control only. Absolute residuals and divided equations must also be inspected.

Across all 121 forced entries, the sampled unforced B2 divided maxima range from 0.693002738 to 1 for F and 0.412113426 to 0.993766813 for G. Those measurements provide no numerical YES. They are not continuum exclusion bounds. [P348](proofs/348_final_verifier_synthesis/PROOF.md) independently re-reduces the frozen table and records the limits of this synthesis.

The following comparison uses the same 20 Anderson map calls, physical seed, beta=3.0113961, Nt=56 and forcing parameter lambda=0.95. This is equal call count, not equal wall time. Every number is a maximum over the stored regional evaluation points. The first two columns are divided normalized residuals; the last two are original Cartesian absolute residuals. The forced velocity belongs to a modified problem and does not supply a B2 YES; even its sampled absolute thermal residual remains above 2.

| Angular K | Velocity | F ratio | G ratio | absolute thermal | absolute vorticity |
|---:|---|---:|---:|---:|---:|
| 24 | B2 self | 0.742534 | 0.458304 | 163.873 | 11.6518 |
| 24 | forced | 0.00147267 | 0.00431471 | 2.66952 | 0.00569731 |
| 32 | B2 self | 0.742534 | 0.458317 | 167.495 | 11.6533 |
| 32 | forced | 0.00024977 | 0.000855856 | 2.22293 | 0.00156911 |
| 40 | B2 self | 0.742534 | 0.458316 | 166.789 | 11.6534 |
| 40 | forced | 0.000244816 | 0.00031882 | 2.16591 | 0.000390965 |

The complete tables preserve both absolute and normalized residuals in six radial bands. [P316](proofs/316_portable_residual_package/SUMMARY.md) independently reconstructs the CSV from packaged regional JSON and matching coefficients. The coefficient inputs require both numerics/artifacts/verifier and numerics/runs: 61 hashes are packaged and 58 further hashes are in runs only. This verifies table-data sufficiency, not execution of the numerics resolver or complete solver reproducibility. [P333](proofs/333_actual_numerics_wording/PROOF.md) confirms adoption of the grid, scope and input-root corrections.

On six manufactured points, the physical-space inverse used square radii 8, 16, 32 and orders 12, 20, 32. The largest order 32 error is 2.22e-16 for the Gaussian and 7.11e-15 for the slow-stream field. Omitting the exterior for the slow field instead leaves errors 1.812, 1.403 and 1.101 at those radii. These are floating-point controls, not rigorous candidate-specific inverse bounds. Individual candidate packets separately inspect elliptic errors, center jets, stagnation points and exact far-field coefficients. The consolidated table does not claim universal exact-certificate coverage.

## Mathematical conclusions and open scope

The following are independently checked results under the precise hypotheses in their proofs.

- [Backward transport](proofs/01_transport/PROOF.md) excludes beta<2 using local Lipschitz velocity, sublinearity and C1 temperature, without parity or tail hypotheses. For beta>2, completeness of every forward orbit and Theta(phi_t Y)=exp((beta-2)t)Theta(Y) exclude bounded nonzero temperature, whether the orbit escapes or not. Bounded nonzero temperature is therefore compatible only with beta=2; unbounded temperature is allowed by the target.
- [Circulation and integrability](proofs/17_circulation_mass/PROOF.md), [sector circulation](proofs/18_sector_circulation/PROOF.md), and subsequent tail proofs impose substantial necessary conditions. In particular, the circulation argument excludes vorticity in any Lp with 1<=p<=2 beta under sublinear velocity alone. These restrictions do not exclude the nonintegrable slow-tail class.
- [The beta=2 analytic obstruction](proofs/08_analytic_beta2/PROOF.md) excludes its stated analytic subclasses; flat smooth behavior remains a different case. The report's later local restrictions on flat endpoints also have explicit hypotheses.
- [Formal all-order compatibility](proofs/321_all_order_formal_resonance/PROOF.md), finite exact nonlinear recurrence checks, and [formal temperature factorization](proofs/331_formal_temperature_factorization/PROOF.md) establish local formal consistency. A common interval of analyticity for each coefficient does not provide convergence in the transverse variable.
- [P357](proofs/357_lower_width_formal_extension/SUMMARY.md) completes a finite exact order12 calculation. Its368 internal controls and816 additional consistency controls do not prove convergence. Comparison with width300 reaches finalized order11 only:6610 nonpolynomial-range powers (6523nonzero,87zero), plus the10000-power exactly polynomial v0 range (3nonzero,9997zero). Both runs share recurrence and Fraction arithmetic. [P355](proofs/355_euler_resonance_operator_bounds/PROOF.md) conjugates the coefficient equations to scalar Euler operators; [P361](proofs/361_euler_one_radius_loss/PROOF.md) proves a sharp-order single radius-loss bound for their two-derivative composition. Bounds in the transverse index and on the resonant constants remain missing.
- [Actual smooth simple-end temperature factorization](proofs/337_general_smooth_endpoint/PROOF.md) and [vorticity factorization](proofs/339_smooth_vorticity_factorization/PROOF.md) are conditional theorems for an existing profile at a finite simple axis endpoint. They do not construct such a profile. The [formal vorticity factorization](proofs/344_formal_vorticity_factorization/PROOF.md) is a separate statement about formal series.

No exact full-plane nontrivial profile has been constructed. Sign-changing branches were allowed but have not been exhaustively searched; exhaustiveness is not a prompt requirement for a YES. The three map-scale comparisons do not amount to three independent full inverse-domain representations. Finite samples and solver residual floors do not decide nearby exact solutions. No interval certificate is supplied; the prompt requests it if attainable. No a posteriori existence certificate or finite-energy bounded-data blow-up theorem is supplied. The physical reconstruction is verified as an identity conditional on exact profile equations.

## Review record and time

The lead's actual mathematical report fd3b9935 and SPEC v93 b7e96108 were checked in [P346](proofs/346_actual_summary_endpoint_entry/PROOF.md) against the approved complete preview. The subsequent A5 clarification in SPEC v94 f6be1c04 is confirmed by [P353](proofs/353_actual_spec_drift_clarification/SUMMARY.md); the report hash remains fd3b9935. These check entry of the already audited mathematics, not future finalization. The final successful write, current report hash and archive coverage require their own readback.

The requested Claude Opus 5.5 collaboration used the permitted Python Bedrock client. Public response metadata records actual claude-opus-5-5; no silent model substitution was made. Reviews were challenged and followed up where needed. Empty or unavailable reviews are preserved and are not endorsements. Their advice and the lead's summaries were not treated as proof.

[P347](proofs/347_final_evidence_and_time/SUMMARY.md) separates wall time, shift-session occupancy and active work. At T_end, the recorded intervals for shifts 2-10 total 171206.033893 seconds (47 h 33 min 26 s), comprising 168922 seconds from completed shifts 2-9 and 2284.033893 seconds of shift 10. Eight explicit restart gaps total 240 seconds. The initial 22 minutes 17 seconds (1337 seconds) before the model switch has no recorded shift1 end and remains unclassified. These three quantities sum to the reported wall time. Active research time was not separately measured; background work could also continue during a gap. The session log is in the working archives, which are not published.

The readbacks of the earlier packaging of the working archives and of the report files as they stood at their cutoffs (P358 to P360) concern working files that are not published; they are omitted here. The verdict on the broad B2 problem is unchanged: no accepted endpoint.
