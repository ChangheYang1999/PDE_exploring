# LIT301 transfer into the assembled report

Status: mathematical transfer CONFIRMED A2433 under the exact definitions recorded in A2434. The current row should make integer M, admissible circles and decreasing radius explicit. The full-system and global questions remain open.

## 1. Exact object and hypothesis inheritance

The report pin is 8a6af31697a9d78a63a49e8c942a7cefda89dd722d384c8908ce7013bc4af902, assembled 2026-11-03T22:02Z. Its five file differences from pin271b51f7 were read in full: this report 13935 characters, in the team records 24093, THEOREM_ATTEMPTS.md 8983, PROOF_OBSTRUCTIONS.md 4027 and in the team records zero. All four foundational blocks are unchanged. The previous cumulative mathematical approval is A2424, with the metadata-only change A2432.

The new LIT301 row explicitly inherits the complete setting of the C60 row. In standalone terms, fix 0<c<1/2 and any real omega, Jx=e3 cross x, X=(cI-omega J)x, L=(1-c)I+omega J, a=1-2c and b=2(1-c). A smooth X-flowbox G has distinguished orbit Gamma. Smooth V,S satisfy div V=0, X.V=0, DV X=-LV, XS=-bS, X cross W=aV and W.grad S=0, where W=curl V. Also P=S+|V|^2/2 and -Delta P=tr((DV)^2). S=0 on Gamma, S<0 off Gamma, and V,S are flat at a point x0 on Gamma. No realization of these local hypotheses is asserted.

Let Pi denote the flowbox projection to its transverse disc. The actual degree is the degree of the two-dimensional quotient vector field dPi V on an oriented transverse section, on a circle where that field is nonzero. Its radius is measured from the distinguished central orbit in those quotient coordinates. These are the conventions under which the cited A2426-A2427 hold.

## 2. Exact meaning of the mathematical transfer

On connected G minus Gamma, LIT288 applies because S is nonzero. V cannot be identically zero there, since that would make S harmonic and nonpositive with an interior zero in G. Thus its exact-order branch applies: every off-orbit zero has common integer order N>=1 for V and W, two-sided transverse bounds and index -N. Transport with A+L=I preserves quotient index. These are A2426, and the report's failure to assert a uniform exponent is correct.

For admissible 0<r<R, compactness and local isolation give finitely many annular zeros. The oriented degree identity gives d(r)-d(R)=sum N. Consequently the degree grows as the radius decreases across zeros, not as it increases. It tends to positive infinity if off-orbit zeros accumulate at the central orbit. An upper bound along any cofinal sequence of admissible radii prevents that accumulation. None of this excludes the central orbit when it is the only zero orbit nearby. The report and obstruction tracker explicitly retain this limitation.

For each integer M>=1, the field exp(-1/|z|^2) conjugate(sin(1/z)^M), extended by zero at z=0, is smooth and flat at zero. Its off-center zeros have order M and index -M, with first derivatives zero when M>=2. The exact degree on nonzero circles is M(1+2 floor(1/(pi r))). This is A2428. At positive radii with sin(1/r)=1 its divergence-to-norm ratio is 2/r^3, so it is neither divergence-free nor subject to a bounded |div f|<=C|f| near zero. Thus A2429 refutes only the inference from flatness and negative indices, while A2430 identifies the missing differential constraint. No false carrier or Euler example has been inserted.

## 3. Definitions that should be stated in the row

The report and ASSUMPTIONS row abbreviate the example parameter as "M >= 1". Here M must be an integer, as in the source and A2428. A noninteger power of the complex sine is not the globally single-valued smooth family asserted there: a loop about a simple sine zero changes a branch by exp(2 pi i M). This is a scope clarification of the citation, not a new counterexample to the integer theorem.

Likewise "degree on circles" necessarily requires a nonzero boundary field. The source defines admissibility explicitly; the summary should do so once and use admissible radii in its limiting statement. The words "grows by the orders" should specify shrinking radii to preserve the sign of the exact annular identity. The formulas and cited result determine all three intended conventions, but an exact theorem statement should not leave them implicit.

Under those precise conventions, the transfer is mathematically faithful. An interpretation allowing arbitrary real M, zero-bearing boundary circles, or growth when radius increases is not approved. A correction to those definitions can be checked as a small textual difference without repeating the analytic proof.

## 4. Evidence and limits

All five complete differences and all four audit sections were read. The complete six-section LIT301 audit, auditor_proofs/reviews/common_flat_annular_index_20261103/PROOF.md, supplies the exact source reconstruction A2426-A2431. Its proof and manifest are retained as dependencies. No numerical computation or formal build was needed.

The unchanged report continues to leave the full common-flat setting, its positive-trace endpoint, additional degree bounds using its differential equations, and the unrestricted smooth decaying rotating-profile conjecture open. No original helicity assumption, natural derivative bound, complete characteristic flow or pressure normalization has been silently removed from a previous global theorem. The quotient-divergence proposal is not yet part of the report and has no verdict here.
