# Closure of independently reviewed proofs

Status: CONFIRMED, subject to the exact hypotheses in the referenced standalone proofs.

## Statements and dependencies

The prime-denominator theorem in topic31 is confirmed for every finite rational odd-sine leading profile with nonzero first harmonic, outside the finitely many excluded input primes. Its consequence is density of incompatible rational parameters, hence the residual zero-radius set of irrational parameters proved in topic15. The result is unconditional for the single-sine input and the exact Candidate007 profile. Topic42's stronger arbitrary-real-coefficient extension is also confirmed by V051 after its separate independent review.

Topic32's deterministic nested-interval construction now gives a computable divergent Liouville parameter in every rational interval inside (0,1), for each such rational profile. The intervals use a coefficient with nonzero pole residue. For a general finite profile with highest frequency L and coefficient alpha_L, this can be the sin((L+2j_0)theta) coefficient, with residue

\[
 -\frac{\kappa j_0(L+\gamma_*)\alpha_L}{2p^2(c_*-1)}.
\]

For the single-sine input only, L=1 and alpha_L=1 give the shorter formula in topic32. This distinction is needed when transcribing the proof for Candidate007.

Topic37's two Baire results for analytic input data are confirmed. The first concerns generic data with dense incompatible rational centers. The second says that, at a fixed irrational parameter admitting one zero-radius datum, such data form a dense G_delta in the stated analytic Wiener space. Neither assertion assigns a measure to that infinite-dimensional space.

Topics26 and34's finite nontermination results are confirmed under their analytic angular symmetry assumptions and the condition that the least density exponent is below one. They allow arbitrary finite real exponent sets; topic34 also allows polynomial logarithms.

Topic38's top-frequency scalar recurrence, positive normalized coefficients, inverse incomplete-beta formula, and exact radius are confirmed. The conclusion bounds the full angular-series radius from above and is valid for the specified lattice logarithmic extension. It does not identify the full series radius, singularity type, or singularity location.

## Verification and transcription audit

The theory part's dated review individually checks the algebraic and analytic steps of all these proofs. Its independent exact direct Fourier recurrence tests all37 pairs with prime5<=p<=23 and even4<=a<p. Its complete f_p reductions match the predicted pattern. I inspected the independent code and checked all37 recorded pass flags; earlier verifier Cartesian tests supply a separate implementation. Review, code, log and report snapshots are retained in verification/ with hashes.

An independent512-bit Arb evaluation confirms the two new printed top-growth values: 0.1778863332588136175741083... at delta=2/3 and 0.3243651603366984655498784... at delta=1/2. Gamma-function and incomplete-beta evaluations overlap. Existing topic38 certificates cover the other printed constants.

The theory part's Section10.3 currently uses the single-sine coefficient and residue when it also states the Candidate007 construction. The theorem is valid, but this sentence must use the highest-frequency coefficient above for Candidate007. Section9(iii) still labels dense obstruction conditional although topic31 now proves it for the stated rational-profile class. Section8.2's comparison of the exact top-mode radius with an observed finite growth rate does not rigorously establish which full-series singularity dominates. Replace that conclusion with a finite-order comparison. These are transcription and scope corrections; they do not refute the supporting theorems.

## Model collaboration

This record concerns the existing theory part's written adversarial review and independent code. No additional external review was launched.

## Subsequent closure and repairs

The theory part's03:56Z review independently confirms every step of topic41, including the432/X^2 potential estimate and all weighted derivatives under the joint geometric density/stream hypothesis. The current Section14.5 faithfully transcribes that conditional theorem. V053 closes its all-order statement. The review and repaired theory snapshot are retained in verification/.

The same snapshot repairs the V050 deductions: Section10.3 now selects the highest-frequency residue for a general finite profile, Section8.2 labels the full-series comparison finite-order and singularity dominance OPEN, and Section9 cites the proved prime obstruction. These repairs are confirmed.
