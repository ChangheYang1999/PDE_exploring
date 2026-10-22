# Preflight audit record

This note records incomplete or failed diagnostics as well as passing ones.
No full radial or canonical-flow claim is made.

The first small endpoint diagnostic omitted engine_arb.setup() before
constructing an artificial 1400-bit integer at the process's default
precision. Its test margin was then too small. The production coefficient
and remainder functions restore their fixed precision themselves. The
corrected diagnostic checks the proper outward inclusion of exact
endpoints and passes, including negative values and endpoints below eta.

Smoke v1 used cells0,4102,7808, modes1,2,3,64,261. Both coefficient
methods passed390 containments and30 remainder containments; all6264
forcing coefficients and all six same-point E checks passed. The output
auditor rejected the runtime metadata: platform.libc_ver() returned a
tuple while JSON stored a list. common.runtime() now explicitly produces
a list. This is a false-negative bookkeeping repair. Candidate arrays
and budgets are unchanged. The v1 log, output, and complete source snapshot
remain in evidence and source/smoke_v1. They are not FINAL evidence.

The manufactured diagnostic checks109620 exact recurrence/integral
weights,1680 particular-solution weights,336 positive derivative weights,
42 directed interval conversions,120 signed endpoint comparisons and six
rational-exponential/Arb overlap diagnostics. These finite checks support
implementation review only; the proof is independently written.

Smoke v2 completed at2026-10-21T04:42:48.256730+00:00 on cells0,4102,7808,
all261 modes. Each independent engine passed20358 coefficient and1566
remainder containments;6264 forcing coefficients and six same-point E
witnesses passed. The actual output auditor regenerated45 candidate arrays,
checked30 exact saved witnesses and independently recomputed572 coefficients
and44 remainders by the particular-solution method. Whole-cell replay
passed for cells0 and7808.

The real restart diagnostic kept the first completed cell, appended a
15-byte incomplete JSON tail, and ran the actual producer with --resume.
The producer preserved all20938 complete prefix bytes, removed only the
incomplete tail and completed the remaining two cells. The actual auditor
and both-engine whole-cell replay then passed for all three cells,
including the interruption neighbors0 and4102. Fourteen fault and actual
continuation checks passed at2026-10-21T04:43:36.067028+00:00. Source pins
and frozen candidates were unchanged. The runtime/pin repair from v1 was
included before the v2 snapshot. These tests do not cover the other7806
cells. Exhaustive computation and its closure remain OPEN.
