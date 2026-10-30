# Scope audit of numerics_v05

This audit concerns the immutable batch N publication numerics_v05, SHA256 9e569e6419671b1e9665e7aad3f4f40526db18372f4af4863dee766d9bb9bf2d. It changes no candidate and no closure-matrix row.

## 1. Scalar distance and graded point tests are different arguments

For the exact candidate007 at the fixed reference c, the already independently confirmed k=128 weak test gives a necessary L2 correction norm greater than 0.000043987003470047303. The largest scalar-family L2 budget is less than 0.0000037930. Therefore this necessary condition excludes every registered scalar family to which that budget applies: if such a correction existed, its norm would have to be both larger than the first number and smaller than the second.

The original graded-family budget is less than 0.00045717, as stated in theory_v02 section5. The displayed weak lower bound is smaller than this upper budget. These two inequalities are compatible. Hence the displayed weak lower bound does not by itself exclude every graded box. Numerics_v05 section8 incorrectly attributes the exclusion of every registered ball, including the graded budget in its own parentheses, to this weak bound. Section7's similar attribution to the fixed-c distance is also too broad.

The graded exclusion remains true by the separate point argument N4-102, independently confirmed by T4-122. For every original graded or gradedL2 box with positive top margin

    1/2 - 4708s - (217/50 + (1049/5)s) nu > 0,
    nu = sqrt(r2^2+2r1^2+r0^2)/sqrt(s),

the necessary point inequality at (1/10,73/100) has a positive gap greater than 0.07073905. Thus no fixed-c exact correction in those boxes exists. The hypothesis on the original top margin is essential. This is not a claim about every possible graded norm or box.

The correct publication statement is: candidate007 fails the registered scalar balls by the weak distance and the original graded boxes by the uniform point test.

## 2. The small-a dyadic interval is already excluded

Numerics_v05 R2-3 and section5b retain an open status for 0<a<4/5 in FW-T-DYADIC-Y-v1. Section8 of the same publication instead records exclusion for every 0<a<2. The latter reflects N4-132 and the independent origin-floor reviews, under the explicitly registered inverse, domain and nonlinear-closure hypotheses. The former two passages are stale. The full Laplacian norm is useful as calibration but is no longer required to exclude this registered scheme.

The inference is an application of the already reviewed result in ../origin_dyadic_ceiling/PROOF.md and its frozen peer reviews. No claim is made about other realizations, parameter-changing equations, nonlinear estimates or weighted spaces.

## 3. Compare the same probe before diagnosing quadrature

Numerics_v05 section5b compares the FLOAT maximum over k=0,...,8 with N4-091's larger maximum over k in {0,128,512,1024}, attained at128. The difference between these maxima is not a measurement of quadrature error because their index sets differ. A matched-k comparison of I,A,B,C,H and m is being recorded in ../weak_mesh_comparison/. The numerical value 3.7931e-5 remains FLOAT until that calculation and any needed independent review are complete.

Even when a point estimate and a rigorous enclosure nearly agree, this is a check of that input and those probes. It supplies no universal error bound for the numerical algorithm.

## Dependencies and status

The frozen theory_v02 records the exact scalar/graded distinction at lines74-79 and in NC-T-DIST, and states the point-margin hypotheses. N4-091 and N4-102 have independent T4 confirmations. N4-132 records the Opus origin review. This audit independently checks the logical comparison and publication consistency; it performs no new PDE existence argument. Results in sections1 and2 are CONFIRMED scope corrections. Numerical attribution in section3 is OPEN until the matched computation finishes.
