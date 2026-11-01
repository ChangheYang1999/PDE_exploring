# Density and stream precision monitoring

Status: CONFIRMED source behavior and finite stored-ball audit. The claim about a monitor is separate from the accuracy of an actual checkpoint.

## Statement and notation

Write a logarithmic coefficient as F_n(t,theta)=sum_q t^q f_(n,q)(theta), and similarly G_n. A stored scalar ball is m+[-r,r], where m and r are exact dyadic numbers and r>=0. For one angular column define M=max_k |m_k|, R=max_k r_k, S=sum_k |m_k| and T=sum_k r_k. If M>0 and S>0, R/M and T/S respectively bound the relative coefficient error on the column's maximum scale and the relative error of its midpoint Wiener norm. The triangle inequality gives

    max(0,S-T) <= ||column||_1 <= S+T.

If M=0<R, a relative error normalized by M is undefined, not zero. If M=R=0, the column is exactly zero.

The current numerical logarithmic monitor computes its stopping statistic from the density columns only. It records stream midpoint norms but no stream-radius statistic. Therefore an accurate density column and an inaccurate stream column can pass its precision test. Also, its zero-midpoint branch skips a column even when that column has positive radius. These statements concern the executed source snapshot, not every earlier or future version of the implementation.

## Proof of the monitor defect

Take F_2 to have the single exact coefficient1 and G_2 to have a single uncertain coefficient1+[-1/10,1/10] at its first allowed frequency. The density normalized radius is zero. The source computes its radius list inside the density loop and never adds stream radii. Its reported stopping statistic is therefore zero, although the stream relative radius is at least1/10. Replacing a density column by0+[-epsilon,epsilon] invokes the zero-midpoint skip, so that uncertainty also fails to enter the radius list.

These synthetic states are not asserted to arise from the IPM recurrence. They disprove the general monitor guarantee. A real checkpoint must be examined separately.

## Independent checkpoint method

Read one atomically saved checkpoint as bytes, retain its SHA256 and metadata, and decode its plain packed dyadic tuples. Reconstruct midpoints and radii exactly at640-bit precision; the checkpoint uses512-bit midpoints. Compute the error ratios above directly, without importing the numerical checkpoint loader or statistics routine. Compute each norm and its base10 logarithm by outward interval arithmetic. Retain selected complete coefficient orders and all audited per-column statistics as JSON. The source routine is imported only for the distinct synthetic tests, with bytecode writes disabled.

The resulting enclosures certify the precision of the stored balls and the reported finite norms conditional on those balls enclosing the intended coefficients. They do not independently rederive every high-order coefficient. The independent exact Cartesian prefix and product audits provide separate evidence for the recurrence implementation.

## Scope

A density-only stopping statistic does not justify a joint density-and-stream precision claim. Conversely, its defect does not establish that a particular saved stream coefficient is inaccurate. Neither a small interval radius nor a long finite prefix proves convergence of the infinite logarithmic series.

## Finite result

The retained checkpoint has maximum order180, delta2/3, leading input sin(theta), canonical resonant stream constants zero, and512-bit Arb arithmetic. Its SHA256 and the executed source hashes are in verification/checks.json. Independent640-bit decoding checks421797 density and428939 stream coefficients. Every column has both relative-radius measures below10^(-70), and no column has all midpoints zero with a positive radius. The largest maximum-scale ratio is below2.107*10^(-73) for density and4.683*10^(-72) for stream. These are upper bounds rounded outward from the retained intervals.

At n180, the largest nonconstant factorial-weighted column ratio has base10 logarithm in -0.68811740952741468979+[-10^(-20),10^(-20)] for density and -0.30200318659330409756+[-10^(-20),10^(-20)] for stream. Both maximizers are q1, certified by strict comparison of the intervals for every other q. This is a finite checkpoint result; it does not decide the later interior maximum or the infinite growth rate.

The final audit computation took7.109384603798389 actual seconds. An earlier7.095700226724148-second run checked the same checkpoint before adding the explicit strict-maximizer and uniform10^(-70) assertions.

## Resetting radii changes the certified input

Suppose an exact coefficient x is enclosed by [m-r,m+r] with r>0. Replacing that interval by [m,m] is an enclosure of a new input, not necessarily of x. For example x=1/3 lies in [0.33,0.34], whereas its midpoint0.335 differs from x. Exact propagation of the reset point through the identity map does not repair that difference. Applying outward-rounded subsequent arithmetic only encloses the continuation from reset midpoints. It cannot restore an error term already discarded.

The canonical log-series continuation resumed from order345 with every saved radius replaced by zero. Its narrow new radii therefore do not certify the original exact recurrence. The source save method does not retain the reset marker in its pickle, while the launch header records radii_reset_at=345. The per-order midpoint_only flag depends on the new radius alone, so that flag can become false again without restoring certification. Future audits must use the launch provenance or an independently retained exact-input checkpoint. The numerics11:44Z note already calls this a midpoint-only continuation. This observation does not contradict that note.
