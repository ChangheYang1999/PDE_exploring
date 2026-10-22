# Independent audit of the separable-temperature report entry

## Exact subject and verdict criteria

The subject is the lead's proposed 4.7(xxiii), candidate v1 with SHA256 28f329b9915ca8c0ec36b3de3e361c3ff620986d44da91a5fead841b8c8ec4e2. K1 is its global nonexistence theorem for a restricted temperature representation; K2 comprises its examples and limits of scope; K3 comprises the Q1 summary, evidence row and timeline. This audit checks each from the defining equations and archived evidence. It does not adopt A143's conclusions without checking them. A later revised candidate or actual insertion requires a separate comparison.

## K1: full argument and hypotheses

Let rho be positive and C2 on R, H be C1, and k_j tend to positive infinity with H'(k_j) nonzero. Let Theta(x,y)=H(x/rho(y)). Assume a C1 vector field W has W.grad Theta=0, div W=4, and W1(x,y)/x tending to2 as x tends to positive infinity at each fixed y. Discard a finite prefix to make all k_j positive.

The map (k,y) to (k rho(y),y) and its inverse are C2 with Jacobian rho>0. Set V=W2(k rho,y), Q=W1(k rho,y)-k rho'V. At fixed k,

    Q_k = rho W1_x-rho'V-k rho' rho W2_x,
    (rho V)_y = rho'V+rho(k rho'W2_x+W2_y).

Their sum is rho div W=4rho. Temperature transport is H'(k)Q/rho=0. Continuity of H' gives a neighborhood of each k_j on which Q=Q_k=0 for every y. Thus (rho V)_y=4rho on that strip. Set R(y)=integral_0^y rho(t)dt and C_j=rho(0)V(k_j,0). Integration between finite heights gives rho(y)V(k_j,y)=4R(y)+C_j. No improper integral, uniform lower bound on rho, common regular interval or uniform asymptotic limit is used.

On the same curve, Q=0 implies W1(k_j rho(y),y)/(k_j rho(y))=rho'(y)(4R(y)+C_j)/rho(y)^2. If rho' vanishes anywhere this ratio is0 there for every j, contradicting its limit2. Hence rho' is nowhere zero. Fixing one reference height gives convergence of the numerical sequence C_j. Its unique limit C must satisfy 4R+C=2rho^2/rho' at every height. Differentiating this exact C1 identity gives 4rho=4rho-2rho^2 rho''/(rho')^2, so rho''=0. Positivity of an affine function on the whole line forces its slope0, contradicting rho' nonzero. This proves K1.

For the B2 beta2 field W=2X+U(X)-U(0), sublinear U gives the horizontal limit, since |X|/x tends to1 for fixed y. Divergence4 follows from div U=0, and the temperature equation has zero right side. Neither U(0)=0, y parity, a wall, vorticity sign, the vorticity equation nor the inverse is needed in this restricted obstruction. It is not a full B2 exclusion.

## K2: scalar examples, plates and strip domain

For H(k)=k^2/(1+k^2), H'=2k/(1+k^2)^2>0 for k>0. For any smooth positive rho, Theta=x^2/(x^2+rho(y)^2) is smooth, bounded, even in x, zero on x=0 and has expansion x^2/rho(0)^2+O(x^2|y|+x^4). This is the nonzero required temperature jet. These are scalar conditions on Theta. The transport equation couples it to W and is excluded by K1; the example does not satisfy all coupled opening-paragraph assumptions.

If H is constant, W=2X gives exact transport, divergence4 and the horizontal limit for every positive rho. Its zero temperature jet prevents it from being a profile. Eventual constancy of H on a positive half-line removes the sequence used in the proof; no exclusion follows from this particular fixed-height limit argument. Other hypotheses can yield other obstructions. P220 gives a smooth eventual-plateau diagnostic retaining the nonzero jet, canonical inverse and leading center identities, while failing the full vorticity equation. The word plateau denotes exact constancy here, not a small measured derivative.

For a variant on R times a connected open interval J, retain the same equations, regularity, derivative sequence and horizontal limits only for y in J. Choose y_* in J and R_J(y)=integral_(y_*)^y rho(t)dt. The previous proof forces rho(y)=c y+d with c nonzero on J. Conversely every such positive affine rho satisfies

    4R_J(y)+2rho(y_*)^2/c = 2rho(y)^2/c.

Indeed both sides have derivative4rho and agree at y_*. The field W=(2x,2rho/c) also has divergence4, W1/x=2 and Q=0, so transports every H(x/rho). This verifies compatibility on the strip, not a global profile. If rho is defined only on J and0 is outside J, the candidate's original R=int_0^y rho is undefined; a primitive R_J is required. If rho remains globally defined and only the representation is restricted, the original R is available. The revised wording should remove this ambiguity explicitly.

For beta other than2, temperature transport becomes H'Q/rho=(beta-2)H, so Q need not vanish. Divergence and horizontal slope become2beta and beta. No extension of this theorem to those exponents is claimed.

## K3: report wording and verification history

The Q1 sentence belongs to the beta2 bullet. The ambient smoothness gives H smooth by restriction to any horizontal line, so omission of H C1 there loses no assumption. Arbitrarily large arguments means unbounded positive arguments, as in Z1. The evidence row must retain P218's independently checked restricted theorem and mark any revised entry audit separately. No placeholder is a real completion time.

P218's proof-before-code record is dated22:30:54, its symbolic checker22:36:43, and publication22:39:55 on2026-10-21. The original records, complete proof, eleven controls and actual Opus428 metadata/visible review exist and are registered. A143 was not supplied those records; its refusal to certify unseen history is appropriate, but does not refute the history. This independent checker will compare them directly. The table need not erase verified P218 evidence. Candidate entry outcomes and times become actual only after verification and insertion.

## Separate review claims and limitations

A143's C1 scale extension is correct: the divergence computation uses only Q_k, not Q_y. After the common-limit identity S=4R+C=2rho^2/rho', the quotient rho^2/S is C1, has derivative0, and gives rho'=constant nonzero, contradicting global positivity. A143's bounded-scale end exclusion is also correct: for nonconstant H choose one k_* with H'(k_*) nonzero; on a positive end with rho<=M, V=2y+o(y). Then S=rho V>0, S'=4rho, S<=3My and S'/S=4/V>=4/(3y), forcing S>=constant*y^(4/3), a contradiction. Reflection treats the negative end. These are separate strengthenings, not necessary to approve K1-K3, and not full B2 exclusions.

One display in A143 paragraph2 omits the plus sign between W1/rho and W2(-k rho'/rho); the next equality and all surrounding derivations use the correct sum. This is a transcription error requiring repair if that proof is republished. A143 reports no Opus consultation because its credentials failed. Our own collaboration is separately recorded with actual model metadata and independently checked advice.

## Evidence plan

This complete informal argument is written before the packet checker. The checker will independently verify the coordinate cancellation, limit-identity derivative, scalar example jet, affine strip construction, weaker regularity quotient identity, bounded-end comparison and original P218 chronology, then compare any revised candidate and preview exactly. No numerical sample proves nonexistence. No formalization is claimed; formal_sources records the sources, and verification records all finite checks and revisions. The smooth beta2 and beta>2 slow-tail B2 problem remains OPEN.


## Revised candidate v2: bounded ends and the plateau example

Candidate v2 has SHA256 2f58caf265d5c64c2239d7454bbd2d417c803881597e4ff63ba778096c5e9ec9. It adds the bounded-end theorem as (b); the complete independent proof is in the preceding section, including the reflection at a negative end. K1 now means (a), K2 means (b), K3 the scope, and K4 the summary, table and history. The original K1-K3 labels above refer only to v1. The revised candidate is checked in this separate record and is not yet an actual report entry.

Here is a full independent verification of its new plateau example. Put rho(y)=sqrt(1+y^2), k=x/rho(y), B(y)=2 asinh(y), F(k)=k chi(k), where chi is smooth and even, equals1 on [-1,1] and vanishes outside [-2,2]. Let H be smooth and even, equal k^2 near0 and have H'=0 for |k|>=1. Such an H exists by integrating 2k times a smooth even cutoff equal1 near0 and zero for |k|>=1. Define Psi=B F, U=(-Psi_y,Psi_x), W=2X+U, Theta=H(k). The physical derivatives give

    U1=-B'F+(k rho'/rho)B F',  U2=B F'/rho.

All fields are smooth. F and kF' are bounded. B'=2/rho, B/rho and rho'B/rho are bounded, so U is bounded. U(0)=0 because B(0)=F(0)=0. Divergence U is0 by equality of the smooth mixed partial derivatives. Since F is odd, Psi and U1 are odd in x, U2 even in x, and Theta even. Theta is zero on x=0 and equals x^2+O(|X|^4). Near0, Psi=2xy+O(|X|^4), so DU(0)=diag(-2,2) and DW(0)=diag(0,4). Thus the complete opening paragraph of4.7, which does not impose the vorticity equation, is satisfied once transport is checked.

For any k with H'(k) nonzero, |k|<1, hence F=k and F'=1. Directly

    Q=W1-k rho'W2
     =k(2rho-2y rho'-B')+B rho'/rho (kF'-kF')
     =0,

because rho-y rho'=1/rho and B'=2/rho. Where H'=0, transport H'Q/rho=0 holds without requiring Q=0. This proves transport on the whole plane, including the cutoff transition and the boundaries |k|=1. It is not merely a local calculation.

For small x at y=0, B=0, B'=2 and F(x)=x, so U=(-2x,0) and W(x,0)=0. The function Psi is odd in y because rho is even and B is odd; its Laplacian is also odd in y, so Omega=-Delta Psi=0 on y=0. But Theta_x(x,0)=2x for small nonzero x. Therefore W.grad Omega+Omega-Theta_x=-2x there, proving failure of (V). This example has b0=0 and is not the different P220 example with b0=2; they should not be conflated. It is a counterexample to removing the large-k condition from the transport-only theorem, even with the opening paragraph's jet. No canonical-inverse claim is needed for this particular report scope example, although P220 separately proves an inverse-compatible diagnostic.

The affine interval construction in v2 is valid for a positive affine rho=c y+d on a connected open interval J and c nonzero. W=(2x,2y+2d/c) gives Q=2x-k c(2y+2d/c)=0, divergence4 and W1/x=2. A proof on J uses R_J=integral_(y_*)^y rho, y_* in J; it cannot use an integral through heights at which rho is not defined. The representation curves are pieces of rays through (0,-d/c), which lies outside J. The wording that the argument of (a) gives no exclusion for eventual constancy refers to this fixed-height large-k limit, not to every consequence of transport or other hypotheses. These two clarifications can be checked in v3 without changing either theorem.

This complete addition precedes the v2 checker and the new model review. P218 history is still verified by its original records; A143's derivation of (b) and this different plateau example is independently checked above. Placeholder review times and verdicts must remain prospective until the corresponding records exist. The full smooth B2 problem remains OPEN.


## Candidate v3 and complete-preview comparison

The v3 candidate2f096e21 adopts the based primitive, fixed-height qualifier, portions-of-rays correction and existential plateau wording. It also deletes the premature expression4S/V before positivity of V has been established; S'=4rho holds at every height, while the quotient is valid only on the eventual positive end. This is a real domain correction to the displayed intermediate expression, not a change of theorem. The dummy height y_1 avoids reusing the half-line base y_0. These changes agree with the complete arguments above. A144 was read independently, including its bounded unbounded-scale example rho=(1+y^2)^(1/4): along a regular curve x=O(y^(1/2)), V~2y, so S<=C*y^(3/2) but S>=c*y^(8/5), a valid contradiction supporting existential scope. It is not needed by the entered theorem.

For the preview, reconstruct the normalized complete text outside section7 by inserting exactly Z1-Z3 before4.8, replacing exactly the quoted G1 sentence, and adding exactly the filled G2 table row. Compare the timeline entry multiset separately with the existing section7 plus G3. The first v3 preview2788e959 omits G3 from section7, though it is present in the separate entries_preview.txt. Thus K1-K3 are mathematically valid and the proposed G3 itself is checkable, but the full preview is not yet a faithful representation of the intended insertion. This defect was reported at23:17:28 before approval. The actual insertion needs an exact re-read regardless of a repaired preview.

## Complete-entry assembly audit
The lead preview omits the G3 timeline entry even though its separate entries file contains the correct text. To inspect a concrete complete proposal without modifying the lead directory, preserve its verified changes outside section7 and the existing timeline introduction, then replace only the timeline bullets with the separately verified entries list. Compare the resulting entry multiset with the old report and require exactly the G3 addition, zero deletions and zero duplicate additions. This local assembly is an entry proposal, not evidence that the actual report has changed. The omission in the source preview remains recorded.
