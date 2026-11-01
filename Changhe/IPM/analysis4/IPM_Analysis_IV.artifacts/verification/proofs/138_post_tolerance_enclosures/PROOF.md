# Validated coefficient norms after a stopping tolerance is exceeded

Status: the elementary interval principle below is proved. The accompanying finite checkpoint audit is CONFIRMED in V271. It concerns the canonical polynomial-log sequence at delta=2/3, c=3 and f_1=sin(theta), with all resonant stream constants zero.

## Statement and notation

Write F_n(t,theta)=sum_q t^q F_(n,q)(theta) and similarly G_n. Define M_n=sum_q ||F_(n,q)||_1 and N_n=sum_q ||G_(n,q)||_1, using the absolute sine-coefficient norm. Suppose a checkpoint stores an enclosing real ball I_(n,q,j) for each exact coefficient. Applying absolute value and summation in outward-rounded ball arithmetic gives enclosing intervals for M_n and N_n. If the lower endpoint of the M_n interval is positive, their interval quotient encloses N_n/M_n. In particular, a positive lower bound for N_n/M_n-1 certifies N_n>M_n. None of these conclusions requires relative coefficient uncertainty below a chosen numerical stopping tolerance.

## Proof

For every exact coefficient a in its stored ball I, the image interval |I| contains |a|. A finite Minkowski sum of those image intervals contains the exact sum of the absolute values. This proves the norm enclosures. Division by a strictly positive interval is inclusion preserving when evaluated with outward rounding, so the quotient interval encloses the exact positive ratio. The lower bound test is then immediate.

A stopping rule only decides when a computation ceases. In the audited implementation the flag called midpoint_only is a diagnostic comparison with 10^(-6). It does not replace coefficient balls by their centers, alter the recurrence, or alter checkpoint packing. The restart unpacks both exact dyadic centers and dyadic radii, and all coefficient operations continue to use Arb arithmetic. Therefore crossing this tolerance does not itself destroy the enclosure property. A displayed midpoint alone is not a certified decimal, but an independently recomputed interval may still decide a coarse inequality or enclose some digits.

The coefficient enclosure induction uses the source recurrence audit from topics10,19,53 and the frozen source code: exact rational input parameters, outward-rounded additions, multiplications, nonzero scalar divisions, finite polynomial operations, and exact dyadic serialization. The independent Poisson residual calculation in this folder checks every new retained coefficient against the differential identity. Residual intervals containing zero are consistency checks, not by themselves a substitute for the enclosure induction. This audit does not independently regenerate every high-order nonlinear convolution.

## Finite scope and reproducibility

The selected new coefficient orders are retained as a compressed pickle with its exact raw and compressed hashes. The original full checkpoint is identified by its hash but is not copied in full. Earlier canonical orders are already retained in topics64 and82. The script sums coefficients directly from the stored balls at640 bits, rather than using the source's floating diagnostic sums. It reports norm enclosures, relative norm radii, individual unresolved counts, regression slope intervals and direct coefficientwise Poisson identities.

Any certified violation of a proposed bound N_n<=H_0 M_n disproves that bound for this sequence and that particular H_0. It does not disprove boundedness for some larger H_0, ordinary convergence, or an eventual estimate after finitely many exceptions. A finite slope remains a finite slope, even when rigorously enclosed.

## Completed finite result

The source checkpoint at340 and the retained exact selected balls give N_332/M_332>1.49 and N_338/M_338>1.70. All375226 Poisson coefficient tests and3canonical constants at331through340 pass; all individual new balls remain resolved. The proposed global bound N_n<=0.34 M_n fails at332,335,338and340. The coefficient enclosures remain valid even though the chosen1e-6 stopping threshold has been exceeded. See the frozen input manifest and checks for exact interval outputs. Neither ratio boundedness at all future orders nor convergence of this canonical logarithmic series is decided.
