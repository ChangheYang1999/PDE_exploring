# Final finite decay-rate diagnostics for the canonical logarithmic runs

Status: CONFIRMED finite computations under the stated input hypotheses; initial cutoff label corrected.

## Exact statement and hypotheses

For each supplied finite sequence of interval-enclosed Fourier-log coefficients, let M_n be the sum of the absolute values of all density coefficients, including every logarithmic column. Assume the supplied coefficient enclosures contain the coefficients under discussion. This audit verifies finite norms and finite statistics under that input hypothesis. It does not rerun every nonlinear recurrence or establish an infinite asymptotic law.

The cases are delta=4/9 through300, delta=2/5 through240, delta=9/20 through240, delta=1/2 through300, and the previously admitted canonical delta=2/3 prefix through329. For each final order N use the thirty increments d_n=log10(M_n/M_(n-1)) with n=N-29,...,N. All required norm intervals must be strictly positive.

## Argument

The absolute-value map sends a real interval to an enclosure of the absolute values of every represented number. Addition of these intervals therefore encloses M_n. Monotonicity of logarithm on the positive real axis encloses log10 M_n and each difference d_n. The finite telescoping identity gives

    (1/30) sum_(n=N-29)^N d_n = (log10 M_N-log10 M_(N-30))/30.

The nth-root diagnostic is exp(log(M_N)/N). A printed decimal with rounding unit u is confirmed only if the entire computed interval is inside the open bin centered at that decimal with radius u/2. Replaying at higher precision checks numerical consistency. A finite rate or root never implies convergence of the infinite series.

The source labeled as the certified two-thirds part must end at329 to agree with the established campaign cutoff. A statistic ending at348 instead refers to a different order window and cannot be used as the claimed statistic through329. This is a data-selection error even if the scalar arithmetic on the selected records is correct.

## Dependencies and scope

Topic64 supplies the independently recomputed norm enclosures through329 at delta=2/3; topic291 supplies the half-exponent enclosures. The other three finite checkpoints are independently decoded for their norm statistics. Exact source hashes and extracted scalar enclosures are retained. These calculations neither repair nor discard input uncertainty and do not certify a global solution.

Written 2026-10-31T23:12:54+00:00.

## Completed checks, V628

2026-10-31T23:16:47+00:00. For delta=4/9,2/5,9/20,1/2,2/3, respectively, the thirty-increment means reproduce as -0.328,-0.254,-0.338,-0.419,-0.691 and the final roots as 0.4576,0.5387,0.4450,0.3716,0.1952. The final orders are300,240,240,300,329. All150 increments are negative and all10 displayed mean/root rounding bins pass. The three newly decoded checkpoints contribute385583 coefficient positions per precision replay. The initial two-thirds JSON used N348 while labeling its row certified; the corrected table explicitly uses N329 and orders300..329. All five corrected table windows and its approximate scalar entries agree with the independent calculation.

CONFIRMED as finite norm statistics under the input-enclosure hypotheses in the proof. REFUTED initial two-thirds cutoff label, now corrected. This admits no new all-order geometric law and does not rerun every nonlinear coefficient recurrence.

The complete norm-and-rate computation took 7.813494062 real seconds. Checkpoint decoding handles exact three-part dyadic balls; the reused norm receipts have four-part dyadic encodings. The two initial decoder attempts failed before producing a result and supplied no numerical evidence.
