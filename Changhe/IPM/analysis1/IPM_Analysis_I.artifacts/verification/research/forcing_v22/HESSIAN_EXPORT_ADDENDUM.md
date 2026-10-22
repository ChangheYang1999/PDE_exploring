# Auxiliary Hessian export on constant rows

Written 2026-10-21T09:53:28.570921+00:00 before the repair program.
The finite auditor rejected an auxiliary output, cutoff_hessian_bounds.json:
all26079 constant cutoff rows exported nextafter(0,+infinity)=2^(-1074),
which exceeds the producer's exact zero. Its comment claiming these
exported endpoints were also below the producer endpoint was false on
these rows. The original output and failed-audit fingerprint are retained.

This does not affect cutoff_extrema.json: that program compared the exact
Arb upper bound0, before the separate float export. No aggregate uses
this auxiliary array. Each affected row has dmax<=r_in, so tau is the
constant1 there and its Hessian is exactly zero. Set precisely those
auxiliary entries to0 in a new output, and check all other entries without
change against their saved nonnegative finite endpoints. This is an exact
constant-function argument, not a rounding tolerance or a modification of
any forcing input. Preserve the original reviewed program and output.
