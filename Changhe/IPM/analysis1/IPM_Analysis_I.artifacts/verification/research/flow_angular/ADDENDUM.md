# Clarifications after the first Opus review

The velocity convention in PROOF equation(2) is V=c_l X+U, with U=(-psi_y,psi_x). This convention is required for the formula and is now explicit.

The pinned python-flint0.9.0 source has `lower` at lines327-338 and `upper` at340-351. Their documented outputs are exact floating-point numbers rounded outward to the current precision; the implementations call arb_get_lbound_arf and arb_get_ubound_arf. The source `__float__` at497-498 converts the midpoint with ARF_RND_NEAR. These are reference-source facts, not a proof of installed-binary provenance.

The checker explicitly assigns ctx.prec=128 immediately before every actual source factors call, without another intervening operation that changes precision. The geometry construction also resets128 before each node's arithmetic. The fresh auditor checks finiteness of every stored cache-key value, and the primary checker checks every exported coefficient midpoint/radius for finiteness. All half-widths and remainder floats are converted to exact Fraction values, which rejects NaN and infinity. This covers the exported values in the stated finite audit. Other source outputs, including those only used by box_class, are outside this result.

All4176 source remainder outputs are compared to exact rational bounds in the same primary Python process that computes them. No claim is made that a different runtime reproduces those outputs. A separate small runtime probe records the actual platform, binary hashes and rounding state and repeats the8 times2 times261 calculations in-process, comparing the saved floats bitwise. It is additional provenance for these finite values, not validation of historical numerics-lane runs.

The total coefficient-box count is221*3*3*261=519129. Both independent intervals are contained in each of these boxes, so the primary checker makes1038258 coefficient containment checks. The fresh1536-bit auditor must check all519129 again.

The first fresh-audit attempt was stopped because repeatedly loading arrays from an NPZ archive inside each coefficient comparison caused unnecessary decompression. Its source, log, exit status and diagnostic are preserved. Loading those same immutable arrays once before the loop fixes only performance. The primary computation was already complete; it is retained, and only the fresh auditor is rerun.

The second audit attempt failed at the remainder loop because the cache-repair edit had accidentally changed the initialization of remainder_checks. The failed source and logs are retained. After restoring that counter, the third attempt passed all519129 coefficient boxes,51000 nodes and4176 remainder checks at1536bits in2.5332seconds (2026-10-20T23:44:41.446648Z). The separate runtime probe then reproduced all4176 remainder floats bitwise and verified exact rational inequalities, with rounding mode0 before and after.
