# Candidate016: a complete Hardy upper from the checked mode1,3,5,7 prefix

Written UTC 2026-10-29T16:09:54.740158+00:00 before this lane's finite checker. This independently audits N4-403's prefix7 certificate. Its full-field inputs and individual moment certificates are retained explicitly; no omitted moment is treated as zero.

## Exact statement, domain and dependencies

Fix the real S1 candidate C1-N1-016-legqs25-quot013, raw SHA256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42 and c=4076476460239181/2251799813685248. Set delta=1824676646553933/4076476460239181. Use its canonical velocity, including the local contact term, and its complete residual F=(cX+U[rho]).grad rho-rho. All norms use Lebesgue measure on R2. The accepted T4-467 component certificate gives rF in L2. The exact source representation binds1360 branches and every positive odd sine frequency1 through319. F is smooth and locally integrable. Define H(F) as the dual norm against compact smooth tests with gradient norm at most1.

Write F=sum f_n(r)sin(n theta), q_n=pi int_0^infty r^3 f_n(r)^2 dr and S=||rF||2^2=sum q_n. For the complete included prefix n=1,3,5,7, set m=9. Then

 H(F)^2<=M2=sum q_n/n^2<=S/81+sum_(n=1,3,5,7)(1/n^2-1/81)q_n.   (1)

This is the finite candidate specialization of T4-474 and also N4's independent angular-tail proof. The infinite-series extension of474 is not needed here. If each complete included q_n is contained in[L_n,U_n] and S<=U, every coefficient in(1) is positive, so its right side is bounded above by

 U_M=U/81+sum_(n=1,3,5,7)(1/n^2-1/81)U_n.                     (2)

The sum of the included lower endpoints divided by n^2 is a lower bound for M2, not for H(F)^2. The separate dual lower comes from T4-470/472. The complete finite-mode divergence-free theorem469 is AUDITED through Opus T2, accepted by T4-475. For its exact n1 and n3 tests, T4-472 gives the strict improvement J>59664789113139289718803/250000000000000000000000. Therefore

 H(F)^2<U_M-59664789113139289718803/250000000000000000000000.    (3)

The source moment and exact representation premises named below remain explicit. Passing this finite audit will give the whole-field bounds H(F)<1.063013 from(2), and H(F)<0.944107 from(3). The established independent dual bound H(F)>0.529469576110512066428681 remains valid. These are bounds for this one exact residual, not its exact negative norm and not correction-distance bounds. The narrower later low-mode prefix is a separate input, not presumed here.

## Complete informal argument

Set A_F=-e_theta r sum f_n cos(n theta)/n. Angular orthogonality gives ||A_F||2^2=M2<=S. For a compact smooth phi, integration by parts on the angular circle gives -int A_F.grad phi=int Fphi. Since A_F is tangential, radial cutoffs produce no derivative term. Local integrability of the smooth F and L2 of A_F justify the origin limit. Thus div A_F=F on the whole plane and Cauchy-Schwarz proves H(F)^2<=M2. This checks the sign, ordinary pi angular factor and absence of a contact distribution in this auxiliary angular divergence identity. It does not remove the contact term already present in the IPM velocity.

Every omitted mode is at least9, so sum_(n>=9)q_n/n^2<=sum_(n>=9)q_n/81. Substituting sum_n q_n=S proves(1). Positivity proves(2). An equivalent safe split formula is sum U_n/n^2+(U-sum L_n)/81. Its difference from(2) is sum(U_n-L_n)/81>=0; this independently checks the direction of the numerical cancellation. Require the omitted-energy upper U-sum L_n to be nonnegative. No numerical lower tail energy is required for the upper.

For the two separately accepted admissible tests psi_n, set Z_n=A_(Delta psi_n)-grad psi_n, a_n=||Z_n||2^2>0 and b_n=<A_F,Z_n>. The reviewed theorem gives div Z_n=0 and orthogonality of the distinct-mode Z_n. Expanding ||A_F+t_1 Z_1+t_3 Z_3||2^2 and selecting t_n=-b_n/a_n yields H(F)^2<=M2-b_1^2/a_1-b_3^2/a_3. Insert the complete(2) and the independently replayed strict T4-472 correction floor to obtain(3). The finite trial space need not be complete. A same-frequency test would require a Gram matrix or selection, not addition.

For the fixed registered energy define

 E2(F)^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H(F)^2,
 G0=||F||2, G1=||grad F||2, P2=||(1+4r^2)^(2/5)D2F||2.

All terms are positive. Directed insertion of the accepted T4-467 component endpoints and the independent dual or complete upper square gives E2(016)>608.392385921614 and E2(016)<722.969. This retains E2(007)<606.820219<E2(016) from470/472. It is a comparison of identical definitions and weights, not of arbitrary candidates, inverses or existence thresholds.

## Exact mode groups and what this finite replay proves

The source independently reconstructed F from the exact raw potential, including all ordered products, and bound its complete representation to its already Cartesian-checked full production. The complete branch record lists the key(ell,s,n), denominator powers and numerator hashes. The present audit rechecks the1360 ordered records, all160 positive odd frequencies, their canonical representation hash, identical raw field and complete weighted-norm input. It does not regenerate those full numerators. Equality of hashes binds the accepted construction; hashing alone is not a new proof of the construction.

The exact radial convention is f_n=r sum_ell v^(ell delta/2) A_(ell,n)(t), t=r^2/(1+r^2),v=1-t. For each mode expand all ordered branch pairs. Grouping by E=ell+ell' gives the square integral

 q_n=(pi/2)sum_E int_0^1 v^(E delta/2-4)(1-v)^2 G_E(1-v)dv.

The factors arise from rF_n=r^2 sum v^(ell delta/2)A, r dr=-dv/(2v^2), and the angular sine square integral pi. After extracting the exact numerator factor v^k, require the endpoint exponent E delta/2-4+k>-1. The actual denominator factor1+624v is positive. Every nonzero group must be included. The source's exact partial-fraction reconstruction, positive-pole moment and directed remainder algorithm establish each saved integral enclosure. Those source-specific soundness and execution premises are retained, with the complete program graph rehashed read-only. No copied peer code, FLOAT quadrature, candidate optimizer or new field integration runs here.

The independent replay parses every650-digit source group ball and extracts its exact dyadic lower and upper endpoints. It adds those endpoints as exact rationals, then multiplies the resulting positive total interval by a containing pi/2 at8192bits. This avoids dependence on the source's sequential ball-summation order. The exact sums and the original separately rounded mode balls need not have identical radii. The source group sum is the enclosure premise; overlap of independently rounded outputs is only a consistency check. Recheck the literal lower and upper endpoints used in N4's formula as containing the independently composed group enclosures, or use the new rigorous endpoints and verify the coarser directed published bounds separately.

Every source group is checked against its complete mode branch sums, exact exponent, denominator powers, numerator hash and decomposition record. Recheck all angular, ordered-pair and group counts, complete omitted support, integral accuracy and serialization radii. The interval algebra uses no sample-based or small-loss premise. The candidate field, component bounds, selected dual/cross tests and prefix group certificates must all bind the same exact raw candidate. T4-475 accepts the Opus review of469; T1's scheduled reciprocal R1-049 is not attributed to that earlier review. Any remaining source-premise limitation is reported expressly in the result. No stationary inverse, normalization map, contraction or existence theorem is produced.

Exact inputs, including asserted display endpoints, are in JSON and registered in the manifest. The proof precedes the checker. All original verification outputs remain immutable. Existing Opus5.5 lanes supply collaboration; configured identity us.anthropic.claude-opus-5-5, actual provider unobservable. No new model call, JavaScript/TypeScript, server, cluster or additional numerical worker is used.
