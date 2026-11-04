# A local check of Pan-Zhang 2024v1, Example 4

The displayed coefficient in Example 4 does not satisfy the advertised equation with the displayed solution. This audit proves the mismatch for one explicit sequence permitted by the example. It concerns the actual arXiv v1 display, not the paper's continuation theorems, later versions, or the original Gong-Rosay construction. Existing configured model comparison is pending at initial writing.

## 1. Primary source and reading coverage

The source is Yifei Pan and Yuan Zhang, *Unique continuation of Schrodinger-type equations for partial_bar*, arXiv2404.01947v1, printed page 11. Its retained PDF has SHA256

    0b0954e59be965e9a3456fb7c3ba019fe45c2116ecc36ffe5bd6dd08b5741249.

The PDF and a rendering of printed page 11 are retained in `verification`. That page was visually inspected, including the denominator of the initial coefficient term, the product and exponent in each summand, the solution formula, and the claimed equation. The complete four-section submitted audit and all nine manual checks were read.

Independent reading coverage for the broader source is the title page, printed page 11 and printed pages 12-16. This is not a complete audit of that paper. For the original Gong-Rosay paper, printed pages 293-298 were read, including its example on pages 295-296. The other agent's longer reading record is retained as a source record, not adopted as this auditor's own coverage.

## 2. An allowed one-dimensional test

Use one complex variable, with dbar=(partial_x+i partial_y)/2. Take

    a_j=2^(-j-2),  j=1,2,...,  a_1=1/8,
    L_0(z)=log|z|^2,  L_j(z)=-log|z-a_j|^2.

The a_j are distinct, lie in the disc of radius 1/2 and converge to zero. This is an allowed sequence. On the disc of radius 1/2 all distances |z-a_j| are less than one, so L_j>0 away from a_j. Also L_0<0 away from zero.

For the allowed holomorphic factor h=1, the printed solution is

    u(z)=1/(L_0(z) product_(j>=1) L_j(z)^(1/j^2)).

We only need this function in a punctured neighborhood of a_1, where it is nonzero and smooth. Failure there already refutes the asserted equation even before any question of removability at the zeros.

## 3. Smoothness of the other factors

Put w=z-a_1 and work on |w|<1/64. Then |z|>7/64. For j>=2,

    |z-a_j| > 3/64,

since a_1-a_2=1/16 and all later points are farther from a_1. All these distances also have a common upper bound strictly below one. Consequently L_0 is bounded away from zero, and every L_j for j>=2 has a common positive lower bound and finite upper bound.

Define

    H(z)=1/(L_0(z) product_(j>=2) L_j(z)^(1/j^2)).

For each fixed derivative order, all derivatives of log L_j, j>=2, are uniformly bounded on this neighborhood. The series sum_(j>=2) j^(-2) log L_j and each of its differentiated series therefore converge uniformly on compact subsets, by the summability of j^(-2). Its exponential is smooth and positive. Multiplication by 1/L_0 proves that H is smooth, real and nowhere zero. In particular H and (dbar H)/H are bounded on a smaller closed disc, and H tends to the nonzero value H(a_1).

## 4. The actual logarithmic derivative

Because the exponent of L_1 is exactly one,

    u=H/L_1,  dbar L_1=-1/conjugate(w).

Ordinary differentiation on the punctured disc gives

    q := (dbar u)/u
       = (dbar H)/H + 1/(conjugate(w) L_1).

As w tends to zero, |w| L_1 tends to zero. The second term therefore dominates the bounded first term, and q is nonzero for sufficiently small nonzero w. More precisely,

    q = [1/(conjugate(w) L_1)] [1+O(|w|L_1)].

For comparison, differentiating the whole product away from its singular points yields

    q = -z/(|z|^2 L_0)
        + sum_(j>=1) (z-a_j)/(j^2 |z-a_j|^2 L_j).

No solution-product factor belongs in this logarithmic derivative.

## 5. The printed coefficient has a different leading term

In one dimension, suppressing the common differential dbar z, the coefficient actually printed on page 11 is

    V_pr =
      z/(|z|^2 |L_0|^2 product_(j>=1) L_j^(1/j^2))
      + sum_(k>=1)
        (z-a_k)/(k^2 |z-a_k|^2 L_0 L_k^(1+1/k^2)
                  product_(j!=k) L_j^(1/j^2)).

The k=1 summand is exactly

    H/(conjugate(w) L_1^2).

The initial term is O(1/L_1). For k>=2, factor H/L_1 out of the summand. The remaining factor is

    1/(k^2 conjugate(z-a_k) L_k).

Its modulus is bounded by a constant times k^(-2), uniformly in the neighborhood. Summing proves

    V_pr = H/(conjugate(w) L_1^2) + O(1/L_1).

Dividing by the expression for q in Section 4, and using boundedness of H, gives

    V_pr/q = H/L_1 + O(|w|) -> 0.

The advertised equation dbar u=V_pr u would imply q=V_pr, hence V_pr/q=1, on the same punctured disc. This contradicts the limit. The failure occurs on an open punctured neighborhood where all quantities are classical; no distributional convention or value assigned at a zero can repair it.

## 6. The original example and the regularity issue

The original Gong-Rosay example, *Differential inequalities of continuous functions and removing singularities of Rado type for J-holomorphic maps*, Math. Scand. 101 (2007), printed pages 295-296, uses log|z| and log|z-a_j| rather than the logarithms of squared moduli. Its displayed coefficient has the structure

    -z/(2|z|^2 log|z|)
    -sum_(j>=1) (z-a_j)/(2j^2 |z-a_j|^2 log|z-a_j|).

This equals the logarithmic coefficient in Section 4 after the elementary factor-of-two conversion. Its product-free structure is the relevant comparison. This audit does not reconstruct all its global integrability and removability assertions in several complex variables.

The local solution used above has continuous extension u(a_1)=0. It is not locally Lipschitz there, because

    |u(a_1+w)|/|w| = |H(a_1+w)|/(|w| L_1) -> infinity.

In particular it is not C1. It cannot be used as a counterexample to the C1 or C2 hypotheses of A2900 or LIT346. Multiplication by the alternative holomorphic factors is immaterial to the one allowed factor h=1 that refutes the printed universal assertion.

## 7. Scope and verification

The local coefficient mismatch is proved without numerical approximation, optimization or formalization. The primary page rendering is essential evidence that the extra product and logarithmic factors are actually present in the v1 display; they are not an extraction artifact.

Pan-Zhang Theorem 5.6 states scalar H1_loc continuation for the special majorant C/|z|, every finite C, with infinite L2 integral order at the origin. Its stated proof is separate from Example 4. This local mismatch does not refute that theorem, does not assert anything about a later corrected version, and supplies no Euler profile.

The submitted source proof and checks are retained with hashes. The existing configured model comparison is requested through working files, with actual provider execution independently unattested. No new model client is used. The designated verdict is recorded separately in `the auditor's ledger (AUDIT_LEDGER.md)` when comparison and final reading are complete.

## 8. Existing model comparison and finite diagnostic

The complete Theory Agent C comparison dated2026-11-04T04:43:19Z was read and checked. Its items8-10 independently derive the same leading logarithmic derivative and the same erroneous extra factor in the printed potential, using the actual v1 page11. The other factors are uniformly smooth near a1 by the separation bounds, so the infinite series cannot alter the leading mismatch. The comparison did not check the Gong-Rosay page citation; this agent's own stated original-source reading remains the evidence for that limited comparison. No uninspected source theorem is inferred.

The entire pz_ex4_check script and seven-PASS log were read, not rerun. They truncate at30 factors. Five SAMPLE conditions are finite differences or finite-radius evaluations, and the two EX conditions are finite floating examples. One EX shows a sign-flipped coefficient fails numerically. The final EX evaluates the k=1 term times L1 at one radius1e-48 and obtains a value greater than1e40. Its label says unbounded, which that one test alone does not prove; unboundedness follows analytically from nonzero H(a1) and |w|L1 tending to0. The script exits nonzero on a failed predicate. No infinite-product limit or source assertion is certified from these numerical samples.

The mathematical refutation rests on Sections2-5 and the visual inspection of the exact primary page. Existing configured model collaboration is recorded with actual provider execution independently unattested. No new model client or mathematical computation was used.


## 9. Confirmed-source status revision

The exact current source has SHA256 d1c300d825d4293ff1921f3572115e15bd24c3f645ce27218e89e1eeda8c17bc. The full difference from the retained submission has been read: one opening status line changes, and one final comparison section is added. The opening now says that the literal source equation is refuted by A2932. The new final section distinguishes the analytic unboundedness argument from one large finite sample and retains the exact-version and main-theorem limits. No displayed equation, mathematical hypothesis or proof argument changes. The old pending sentences belong to the dated original submission and are superseded by the new status section. The capture and complete difference are retained in verification.
