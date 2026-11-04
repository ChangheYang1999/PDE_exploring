# Carrier and entropy transfer in report 02ab05b9

Status: the mathematical transfers are confirmed. One source-history correction is required before cumulative approval of this exact report pin.

## 1. Exact scope and reading boundary

The report pin is 02ab05b9f08a856c0d5f9382b24260599257c1b564dd92811836ecf979d4d8da, 995876 bytes, with recorded verdict cutoff A2513. Its baseline is ec70e1c8, reviewed in A2513-A2514. The complete changed-line comparisons were read: the report 20575 characters, ASSUMPTIONS 28478, and PROOF_OBSTRUCTIONS 5558. THEOREM_ATTEMPTS is byte-identical to the baseline. The four source hashes and exact copies are in the team records. Unchanged text inherits only its previous scoped review. Historical Appendix B is not newly certified.

## 2. Mathematical transfers

Section 10 and O12 now say that no completion of the constructed pressure-free carriers to the full system (F) is provided. This repairs A2499: a construction for a subsystem and an OPEN completion question do not imply impossibility of completion. The integrability range is correctly restricted to 0<p<2.

The C70 row accurately states A2501-A2506. For smooth complex f flat at the origin, the inequality |partial_zbar f|<=(B+C0/|z|)|f| with B nonnegative in L2 and finite C0>=0 forces f=0. Splitting the measurable coefficient into an L2 part and a part bounded by C0/|z| gives a Cauchy transform with bound 20C0+4C0 log(R/|z|) for the latter part. The resulting finite power of |z| is absorbed by flatness. The carrier consequence uses the already checked local div-curl reduction and smooth coordinate changes. Every finite C0 is allowed; the constants need not be uniform in omega. The contrapositive in the full common-flat setting states that each positive part (Q-C0/|y|)_+ fails to be L2. No upper bound from (F) or arbitrary weak-L2 continuation is asserted.

The LIT304 addition accurately records A2508-A2511. For the circulating Volterra carrier, both actual vorticity quotients are bounded above and below by positive multiples of ell(r)/r, with ell=r g'/g. The specified g=exp(-t log t), t=log(1/r), gives ell=log t+1. Positivity of g off the centre is inherent in defining ell; the general statement uses smooth positive nondecreasing derivative-flat g with ell tending to infinity, as in the referenced independent proof. The lower bound gives failure of L2 and of every L2+C0/r majorant directly. It neither supplies pressure nor excludes a completion to the full system.

X5's conditioning wording now states the correct entropy loss bound H(R_m), independent of block length. Section 2C.3 correctly separates primary-source comparisons for X1-X3 from the independent proofs of the two X5 steps. The kernel-affinity application remains A2513. For exact terminology, a common increasing sequence of finite Borel partitions generating the sigma algebra is preferable to 'finite generators'; no finite dynamical generator is needed.

## 3. Source-history error

The C70 row in both the report and ASSUMPTIONS says that Pan and Zhang's Theorem 4.3 was not read. This is false as a description of the audit coverage. The actual 2023 manuscript was obtained and read in the endpoint audit; the inverse-radius independent proof, Section 4, records that Theorem 4.3 contains the scalar C/|z| result and that its one-variable proof cites Pan1992 Lemma7. That earlier lemma has not been obtained here. The direct independent proof A2501-A2506 does not use the unread earlier lemma.

Required replacement: 'The case B=0 is the scalar case of Theorem 4.3 of Pan and Zhang 2023, whose manuscript was read; the earlier Pan1992 Lemma7 cited in its proof was not obtained here. The present smooth-flat case has the independent proof cited above.' This is a documentary correction, not a discovered gap in the scalar or carrier theorem. No novelty claim follows from the comparison.

## 4. Verdict boundary

The A2499 repair, C70 transfer, LIT304 transfer and entropy wording are confirmed. The literal unread-Theorem-4.3 statement is refuted by the retained reading evidence. Cumulative front/main/Appendix A approval of 02ab05b9 is withheld pending the concrete source-history correction. This does not revoke the previous cace15a2 approval at its original cutoff or the individually confirmed later theorems. No unrestricted Euler nonexistence, complete common-flat exclusion, future report revision or blanket historical Appendix B approval follows.
