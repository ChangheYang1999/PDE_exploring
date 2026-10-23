# Historical numerical-source audit

Written 2026-10-21 before the checker. This audit concerns fixed-c_l forced refinements, two-width least-squares releases, lineage of checkpoint 709d48d4, and early pseudo-time secant rates. Its arguments distinguish arithmetic reproducibility from independent validation of the PDE.

## Residual definition

Let R=(c_l X+U).grad rho-rho and R_forced=R-mu y phi. The static source of refine_fixed.py defines its diagnostic as abs(ev['R']-mu*ev['y']*phi)/ev['Nf']; the final rows call it 'forced-eq'. Therefore those logged values are R_forced/Nf, regardless of the abbreviated |R| in that label. They are not unforced residuals. The eight fixed-c_l entries at c_l=2.8 and 3.3 retain nonzero mu, so the distinction is consequential. For a differentiable symmetry-preserving density with slope a and actual strain c, R(0,y)=a(c_l+c-1)y+o(y), and Nf(0,y)=|a|(|c_l+c|+1)|y|+o(|y|). The unforced normalized limit is |c_l+c-1|/(|c_l+c|+1). Values inferred from the rounded logged strain describe that logged interpolant; a canonical independent strain is a separate check. This argument does not promote the logs to independent full-plane residual estimates.

The first N48 solve in each forced chain has node error below 1e-12, whereas the N64,N96,N128 solves end at 120 iterations with node errors about 1e-4. The stated between-node maxima, parameter fluctuation, and end conditions can be checked directly from frozen primary logs. The numerical source only updates the continuation seed if the node norm is less than 1e-8, so capped later levels are not a chain of accepted converged solutions.

## Release comparison and lineage

The twelve primary release logs identify the forced source and width. Compare each final c_l and a0 at widths 1/4 and 1/8, and compare each printed report entry to the width-1/4 log rather than to the average of the two starts. Independent checkpoint reading reconstructs a0=sum_j(-1)^j u_{0,j}, the constant angular mode at the origin; all higher modes carry sigma^k and vanish there. The exact finite sum is evaluated as a rational sum of stored binary coefficients. This requires no producer module, derivative, or inverse. Checkpoint cl,N,M,Lf are direct metadata. The stored fixed-map p may differ from the released c_l/(c_l-1); that difference is why these early releases are not the later rebuilt-map runs.

Checkpoint 709d48d4 is specifically the q_free release with the map rebuilt as c_l changes, initialized from qls_cl1.5_N128_Lf0.25.pt. It is not the earlier q_ls release from that same forced checkpoint. Its bytes must match the complete SHA256 already independently evaluated in result46. This audit checks provenance and stored parameters, not the residual computation again.

## Pseudo-time secants

For positive sampled core derivatives z_i at logged times t_i, define i_1 and i_2 as the indices nearest 0.1 and 0.5, and

s=(log z_{i_2}-log z_{i_1})/(t_{i_2}-t_{i_1}).

These are secants, not least-squares slopes. Irregular logging can place the selected points outside [0.1,0.5]. Using a nominal denominator 0.4 changes the result. Synthetic exponential data z=exp(lambda t) reproduce lambda with the actual denominator; a curved logarithm gives a different least-squares regression and thus tests the distinction. All logged rate claims are checked against this independent parser, including cutoff, time-step and frozen-flow variants. The source's norm uses the projected derivative info['Fp'], so the observable is the node-sampled fitted density derivative, not the exact unprojected PDE derivative.

Printed values have rounding uncertainty. A decimal with last unit u represents [v-u/2,v+u/2]. Since log is increasing, positive endpoint intervals give a secant numerator interval [log(z2lo/z1hi),log(z2hi/z1lo)]. Positive time-gap intervals give the corresponding quotient enclosure; its extrema occur at the four interval corners. This is an enclosure of possible unprinted decimal values, not a rigorous PDE or trajectory enclosure. Compare the reported two-decimal rate with its half-unit rounding interval. Also record direct arithmetic on printed rows and the least-squares slope so the exact meaning remains reviewable.

The first nonpositive-c_w step is a separate explicit stop log, which need not be one of the periodically printed numerical rows. Noncrossing statements are confined to the actual last recorded time. The large N128 frozen run at step .0115 is marked RK4-unstable by the producer and excluded from mechanism comparisons; its smaller-step successor is a distinct run. None of these finite experiments certifies a continuum eigenvalue, instability, or exact solution.

## Dependencies and scope

Dependencies: the representation and Q reader from independent_code/q_checkpoint_reader.py; source files and checkpoint hashes frozen alongside; result46 for earlier independent residuals of 709d48d4. No producer code is imported or executed. No statement about untested parameter values, continuum convergence, or existence follows. The endpoint remains UNRESOLVED and the deadline has not been reached.

## Source-discrepancy addendum before the second checker run

The first run passed387 of389 tests. Its two failed tests exposed a distinction between the last periodic diagnostic row and the actual final-state record, not a rate discrepancy. C=3,N128 logs a last periodic row at1.3501 and a restored final state at1.3848; N160 logs1.4000 and1.4215. Both stop after repeated numerical blow-up detection and time-step halving, with final c_w positive. The summary's1.35 and1.40 refer to periodic rows, not actual final times. The corrected checker records both, checks the summary against the periodic rows, and separately verifies the final-state times and stop reasons. This preserves the original failure as evidence rather than silently relaxing its tolerance. The final report should identify this distinction and avoid describing all listed runs as lasting through1.35..1.5: the three step-refinement runs end at1.0. The secant rates use the sampled times nearest0.1 and0.5; several lie outside that closed window.
