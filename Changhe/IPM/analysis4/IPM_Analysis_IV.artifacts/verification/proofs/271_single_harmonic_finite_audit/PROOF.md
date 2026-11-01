# Independent finite audits of the tuned single-harmonic runs

Status: the argument below is written before the new calculations. Numerical admissions will be dated separately.

## Statement, notation and scope

Let (h,Q,M) be (2,5,7), (2,7,9), (2,9,11), or (3,13,17). Set delta=2h/Q, c=1/(1-delta), p_n=1-n delta, and f_1(theta)=sin(M theta). The all-order compatibility, nonzero-response and convergence theorems for these exact profiles are in topics241,233,227 and242, with their later refinements. This topic checks finite numerical files for these branches. It makes no inference about a sharp convergence radius from finite root tests or fits.

A source checkpoint is admissible under the following hypotheses: its parameter intervals contain the stated exact rationals; its initial coefficient vector is exactly the stated unit sine; its interval operations enclose exact arithmetic; each nonresonant denominator and each tuning-response interval excludes zero; and no coefficient is replaced by a midpoint. Under these hypotheses the completed tuning blocks enclose the uniquely tuned exact coefficients. At a final resonant order whose free harmonic has not been set, the density and particular stream are admissible, but its full stream norm is excluded.

## Exact recurrence and independent arithmetic

Use signed Laurent coefficients with sin(m theta) represented by (t^m-t^(-m))/2. This omits the common factor i; the formal derivative Y is physical partial_y divided by i. For a homogeneous field r^q sum_m v_m t^m, define

X(v)_m contributions: (q+m)v_m/2 at m-1 and (q-m)v_m/2 at m+1;

Y(v)_m contributions: (q+m)v_m/2 at m-1 and -(q-m)v_m/2 at m+1.

The physical Laplacian is X X - Y Y. The real sine amplitudes of the advective term are therefore represented by X(g)Y(f)-Y(g)X(f). The density recurrence is this sum over every ordered i+j=n divided by (n-1)(c-1). The stream is the solution of -X X g+Y Y g=X f with the chosen kernel coefficient. These identities follow by differentiating r^q exp(i m theta) in Cartesian coordinates and accounting for the common sine factor. They are the same independent calculus proved in topic01.

For an independent prefix we continue twice through each Q-order block, first with its free stream coefficient H_n=0 and then with H_n=1. Write R for the next obstructed density coefficient in the first continuation and sigma for the difference between the two. The tuning is H_n=-R/sigma. This uses full nonlinear continuations rather than the producer's linear response recurrence.

## Why two continuations suffice

A free stream harmonic at n=kQ first affects density at n+1. Two affected factors in an advective product require total order at least 2n+1. Since n>=Q, n+Q<=2n. Thus all coefficients through the next resonant density order n+Q depend affinely on H_n. Taking the difference of the H_n=1 and H_n=0 continuations gives the exact response. Its nonzero value, established for these profiles in their all-order certificates, makes H_n unique. Induction over blocks proves agreement with the exact tuned branch.

The same affine identity proves enclosure for the producer's direct response recurrence. All finite sums, derivatives, products and divisions with denominators excluding zero preserve inclusion under outward rounding. Algebraic dependence between balls can enlarge intervals, but cannot invalidate inclusion. The exact first compatibility and the exact affine cancellation justify omitting the kernel forcing at resonance. A ball merely containing zero does not by itself prove compatibility. The latter comes from the exact profile theorem and induction. At an unfinished final block H_n is absent, so the stored zero kernel is provisional and must not be advertised as the tuned stream.

## Checks and interpretation

The checker retains source hashes and the producer source, verifies all parameter and initial-data hypotheses, and recomputes a prefix in Cartesian interval arithmetic. It compares every positive-frequency coefficient, every computed tuning response and harmonic, and retains small exact dyadic evidence. It independently sums norms for every checkpoint order and checks the differential Poisson identity. Reported decimal statistics are compared as finite approximations, with their discrepancies recorded. Selected full ordered nonlinear sums check the density equation beyond the prefix. The final resonant stream norm is excluded whenever its harmonic is missing.

These consistency checks do not formally verify Python or the interval library. Their scope is the written interval-algorithm theorem and the inspected, hashed finite files. The all-order convergence theorem and its conservative sufficient radius are independent of any observed finite growth fit.
