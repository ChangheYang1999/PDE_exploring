# Audit of the report's proof appendices and numerical thresholds

Status: the mathematical bounds in Appendices A and B are confirmed with the proof clarifications below. One rounded threshold in the opening summary does not support its stated certificate.

## Claims and dependencies

Appendix A restates the Diophantine convergence theorem proved in topic 07. Appendix B restates the rational logarithmic degree and factorial-norm Gevrey bounds proved in topic 17. The complete independent proofs, including their hypotheses and inverse estimates, are those two topics. This audit checks that the report uses the same constants and arguments.

Appendix A's scalar recursion, tree packing, layer-cake integral and explicit single-sine and Candidate-profile constants agree with topic 07. In particular the candidate norm multiplier is `T`, while its convergence-base multiplier is `7T`, because the bandwidth constant changes from `B+1=3` to `21`. The reported radii `2^36` and `2^54` and their density tail constants are valid.

In A.6 the undifferentiated stream bound is valid, but does not follow merely from the displayed differentiated estimate A.2. It follows directly from the undifferentiated two-channel inverse:

\[
 \|g_n\|_\sigma\le \frac{e^\sigma}{2}
    \left(d_n^{-1}+(n\delta)^{-1}\right)F_n
 \le e^\sigma(2+\delta^{-1})\kappa^{-1}n^\tau F_n.
\]

Here `d_n<=1`, `n>=1`, and `d_n>=kappa n^(-tau)` were used. This supplies the stated bound without an extra power of `n`. The potential estimate and polynomial derivative losses then give the claimed convergent differentiated sums. In A.7, the displayed divisor proof treats `|m-n/sqrt(5)|<1/2`; in the complementary case the same lower bound is immediate because `kappa/n<1/2`.

Appendix B correctly uses the total resonant normalization `B_(n,j)(0)=0`. With the factorial weight `s=4b`, each nonzero first-order inverse costs at most `4b/3`, integration costs `4b`, and the extra constant subtraction has the stated cost. The column bound is at most `2b+4b/3<4b`. The four differentiated factors cost at most `4i`, `Bj`, `Bi`, and `3j`, so the scalar constant is precisely `C=56bB/(c-1)`. Normalizing by the sharp allowed degree factorials removes the product binomial, and the Catalan estimate gives the stated `kappa_n! F (8CF)^(n-1)/n` bound. This is a Gevrey estimate, not convergence. The analytic-data extension uses the stated `C_an`; its stream estimate also has the frequency-shift factor `exp(sigma_0)`, as detailed in topic 17.

## Rounded radius in the opening summary

For a single sine at the exact stored Candidate parameter, topic 22 proves the stated tiny residual when

\[
 r\ge (2A)^{1/\delta},\qquad
 \log_{10}((2A)^{1/\delta})
   =11.7101980148021746094\ldots.
\]

The report instead attaches the same residual exponent to `r>=10^11.7`. That radius is smaller, and does not satisfy the condition `A r^(-delta)<=1/2` used to prove the binary residual exponent. Thus the quoted theorem does not certify the stated residual at that threshold. This does not assert that the actual residual violates the bound there; that separate stronger statement has not been proved. Keeping the exact expression above or using the outward threshold `10^11.711` resolves the issue.

## Other wording that changes meaning

The compact-interior multipoles `r^(-2j) sin(2j theta)` describe the stream. Their velocity fields have radial degree `-2j-1`. Describing those same expressions as velocity multipoles is inaccurate. The first-resonance coefficient is a nonzero homogeneous polynomial in the finite-dimensional input, so its zero set is a proper real algebraic set. Calling it a hypersurface requires an additional argument about its real zero set. Finally, the finite scan's phrase “no compatible rational” is restricted to the stated input `sin(theta)`; topic 25 exhibits a different input with a compatible first resonance.

## Scope

The appendices are mathematical restatements, not additional computational evidence. The source snapshot is retained with a hash in `verification`. The threshold defect is a defect in the claim of certification, and does not refute Theorem E or the independently certified exact-radius bound.
