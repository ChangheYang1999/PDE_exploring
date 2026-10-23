# Hydrostatic export identity and report-source audit

Written 2026-10-21T10:03:01.394293+00:00 before the checker. This is a reproducibility and source audit, not a theorem about existence or a new residual evaluation.

## Exact claim and dependencies

The finite trial density is defined by its stored real coefficient vector u, stored radial nodes tk, basis tag and the scalar parameters N,M,L,P,c. In the local basis, mode k is the degree-N-k Chebyshev polynomial in (2t-1-tk[k])/(1-tk[k]), multiplied by sigma^k, the common radial factor and the angular cosine. Equality of u, tk and these parameters defines the same finite formula. Equality of derived beta arrays is not required, since conversion to their sampled values incurs rounding. The saved binary P is authoritative, even when printed nominally as3/2,2 or3. It is not rebuilt from a final free-c value.

Freeze the exported state files and spectral arrays. Compare the21 previously independently evaluated states with their previous frozen inputs. Read the seven new states with the verifier's own numeric-only reader, retaining both their coefficients and the information needed for later independent evaluation. For spectral exports, verify each vector u and tk against the corresponding state, and the dimensions, state hashes and scalar parameters against metadata. Check nonnegative descending finite singular values, recompute the three reported threshold counts, sum the visible per-mode dimensions, and recompute the norm and maximum of the exported residual vector. Verify the Pythagorean identity among the three exported projection fractions. These are consistency checks of numeric exports: without independently rebuilding J and its singular vectors they do not establish those fractions, spectra or the continuum residual.

Results185,187 and190 provide an independent hydrostatic inverse and finite-state evaluations; result195 proves the finite-dimensional interpretation of the SVD quantities. In particular, the square of the retained residual fraction is only the linearized full-step decrease, and neither a small singular value nor a restricted-space computation certifies exact rank or a small physical field change. The repaired report must preserve those scopes.

The producer's axis-primitive comparison is checked against exact rational center values already computed by187/190. The four rounded-reference comparisons are distinguished from full-precision comparisons. The next seven fields and all freshly rebuilt producer Jacobians remain pending for independent recomputation. A log is evidence of what a run printed, not a substitute for that recomputation. Numerical domain maxima from187 refer to its specified finite samples through radius10000; they are not infinite-domain suprema or the producer's different finite grid.

## Method and scope of the report check

Read the proposed three paragraphs and pair their headline values with the frozen logs and the verifier's existing21-state summary. Classify every claim as independently recomputed, producer-record consistent, or open. Scope the claim about line-search failures to the reported c=2,3 trials: the excluded c=1.5,N64 radius-scaled run reached its iteration budget with a large residual and is not a line-search stall. A hydrostatic conclusion alone does not establish an original SettingIII profile; no separate general nonintersection theorem is inferred from these data. No end-point follows from this static audit.

## Numerical export diagnostic detail

The projection fractions were computed in double precision using numerical singular vectors. The exact Pythagorean identity need not hold to a fixed fraction of one unit roundoff independent of matrix size. Record its actual defect and compare with the diagnostic threshold10*max(number of rows,number of columns)*machine_epsilon. This threshold is not a rigorous error bound for the producer SVD. The report rounds these fractions at far lower precision; independent matrix and singular-vector recomputation remains necessary.
