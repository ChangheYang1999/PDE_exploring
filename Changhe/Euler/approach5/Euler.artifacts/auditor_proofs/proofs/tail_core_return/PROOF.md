# Tail vortex arcs return to the compact core

## Statement, hypotheses, and dependencies

This is the independent audit of Theory Agent A C31, in the team records, Theorem TB. Let U be a C2 vector field on R3, let P be C1, and assume

    div U=0,
    (1-c)U + omega JU + ((Ay+U).grad)U + grad P=0,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0),
    2/5<c<1/2, omega in R,
    U(y)->0 as |y|->infinity,
    integral_1^infinity sup_{|y|>=r}|DU(y)| dr/r < infinity.

Decay can be replaced by boundedness and the vanishing-dilate condition of the already audited tail theorem. No pressure normalization is needed here. Put k=(1-c)/c, delta=1-2c, B=Ay+U, Omega=curl U. Thus 1<k<3/2. Let Phi and Gamma be the complete flows of B and Omega. Completeness of Phi follows from bounded U; the Dini condition and local continuity bound DU globally, hence bound Omega and give completeness of Gamma. Both fields are C1. Gamma preserves volume.

The scattering and tail results A209-A210 supply S, its compact null zero set K, and a continuous tail V with continuous curl Omega_tilde on the punctured space. The map S is a C1 volume-preserving diffeomorphism off K, |S-id| is bounded, and

    S Phi_t=exp(tA)S, DS B=AS, DS Omega=Omega_tilde composed with S.

For z=exp((rho/c)A)w, w in S2, the volume element is exp(3rho)d rho dA(w). Set G=Omega_tilde restricted to S2, G_r=w.G and

    Y=G-(G_r/c)Aw.

A274 supplies a complete continuous flow Y_t, the additive cocycle

    h_t(w)=integral_0^t G_r(Y_s w)ds,

and the complete flow (rho,w)->(rho+h_t(w),Y_t w) of X=|z|^(k+2)Omega_tilde. In particular

    area(Y_t E)=integral_E exp((k-1)h_t(w))dA(w).

The sets where h_t tends to positive infinity in either time direction have area zero. A014 excludes nonconstant closed integral curves of the actual Omega field. These inputs are retained as hypotheses of the abstract dynamical argument below; neither energy nor pressure is used again.

The conclusions are:

1. For area-almost every w with G(w) nonzero, both series sum over n>=1 of exp((k-1)h_n(w)) and exp((k-1)h_{-n}(w)) converge. Consequently h_t(w) tends to negative infinity in both time directions. The time-one map of Y is totally dissipative on {G nonzero}, modulo null sets.
2. For almost every z with Omega_tilde(z) nonzero, its maximal tail vortex arc has finite arclength, finite duration in Omega_tilde time, and both endpoints at zero.
3. For almost every y with Omega(y) nonzero, every connected component of its actual vortex line outside K has finite duration in Gamma time and two distinct endpoints in K. The set of times at which the line meets K is closed, null, and unbounded in both directions.
4. If D is an open Phi- and Gamma-invariant domain whose almost every point belongs to the backward-flow basin of a probability nu with nu({Omega=0})=0, the same conclusions apply almost everywhere on D. Its spherical trace sigma_D=pi(S(D minus K)) is open and Y-invariant, and Y_1 is totally dissipative there modulo area-zero sets.

The basin hypothesis in item 4 is an additional hypothesis at C2 regularity. This proof supplies no C2 basin-coverage theorem. Every conclusion is uniform in the sense that it allows every fixed real omega; no smallness or nonresonance condition occurs.

## 1. Conservative points and the planar obstruction

Let T=Y_1. This is an invertible nonsingular transformation of the finite area space S2. Its Jacobian cocycle is J_n=exp((k-1)h_n). The Hopf decomposition writes S2 as a conservative part C and a totally dissipative part D0, modulo null sets. The dissipative part is a countable union of translates of a wandering set. This statement does not require the action to be free on the conservative part.

For a wandering measurable W the sets T^n W, n in Z, are disjoint modulo null sets. Therefore

    sum_{n>=0} integral_W J_n dA <=4pi,
    sum_{n>=0} integral_W J_{-n} dA <=4pi.

Tonelli gives the two finite sums almost everywhere on W. The cocycle identity and nonsingularity transfer this conclusion to every integer translate of W, hence to D0. Since k-1>0, convergence implies h_n and h_{-n} tend to negative infinity. The estimate |h_t-h_n|<=sup|G_r| for |t-n|<=1 transfers the limit to continuous time.

On C, almost every point is positively recurrent for T. To make the topological statement precise, apply conservative recurrence to C intersected with each member of a countable base of S2, discard the countable union of exceptional sets, and choose successive return times to shrinking neighborhoods. Such a point is positively recurrent for the continuous flow Y_t. A recurrent point of a continuous flow on S2 is fixed or periodic. The primary-source check below covers continuous flows, so no unproved C1 regularity of Y is used.

If Y(w)=0, then h_t=t G_r(w). If G_r is nonzero, one time direction lies in the previously known null positive-escape set. If G_r=0, the definition of Y gives G=0. If w lies on a nonconstant Y-periodic orbit of period P, then h_{nP}=n h_P. A nonzero h_P again puts w in a positive-escape null set. If h_P=0, the X-orbit through (rho,w) closes. The tail vorticity is nonzero on this orbit: a zero of G is fixed by uniqueness and cannot lie on a nonconstant periodic Y-orbit. Its inverse image under S is a nonconstant closed orbit of a positive time change of Omega, hence a closed Omega curve. This contradicts A014.

Thus C is contained modulo null sets in {G=0}. Conversely every G-zero is fixed by Y_t, and an identity transformation on any positive-measure subset is conservative. Hence C={G=0} modulo null sets, proving item 1. Notice that exceptional fixed or periodic angular orbits are not individually excluded by the measure argument.

## 2. Finite tail length and finite vortex time

Fix a point satisfying item 1 and put rho_t=rho+h_t(w). If s denotes tail vortex time, then

    ds/dt=exp((k+2)rho_t),
    d arclength/dt=exp(rho_t)|G(Y_t w)|.

The latter equality follows from |Omega_tilde(z)|=|z|^(-k-1)|G(pi(z))|. On each unit time interval the oscillation of h_t is bounded by sup|G_r|. Therefore both integrals over the full real t-axis are bounded by constant multiples of

    sum_{n in Z} [exp((k+2)h_n)+exp(h_n)].

Only finitely many h_n are positive. Since k+2>1>k-1>0, the remaining terms are bounded by twice exp((k-1)h_n). The sum is finite. Also rho_t tends to negative infinity at both ends, so z tends to zero. Twisted polar Fubini extends the area-almost-everywhere assertion to volume-almost every initial z. This proves item 2. The word loop here means the arc with its common endpoint zero adjoined. It does not assert a smooth periodic vortex orbit through the singular origin.

## 3. Every component on almost every actual line

The conjugacy preserves the actual Omega time when Omega is compared to Omega_tilde. Thus item 2 proves that the set Bad of points off K, with nonzero Omega, whose entire component outside K has an infinite time endpoint has volume zero. This set is Borel. In twisted coordinates its image is R times

    {w: G(w) nonzero and integral_R exp((k+2)h_t(w))dt=infinity}.

The integral is a Borel function by Tonelli. Finiteness of this integral forces h_t to negative infinity at both ends because h_t is uniformly Lipschitz in t; otherwise infinitely many disjoint intervals have an integral bounded below. More directly, a finite actual endpoint exists by completeness of Gamma and must belong to K, since a point off K would allow further continuation in the same open component.

One must not saturate an arbitrary null set over uncountably many flow times. Instead set

    Bad_star=union_{q rational} Gamma_{-q}(Bad).

It remains null. Each bad component occupies an open interval of vortex time and so contains a rational time. A point outside Bad_star can therefore meet no bad component at any time. Separately, Fubini and volume preservation show that Gamma_y^{-1}(K) is a time-null set for almost every y, because K is volume-null. It is closed by continuity. If it were bounded above, the final component of its open complement would have infinite positive duration, contradicting the preceding conclusion. The negative direction is identical.

The two endpoints of a finite gap are distinct. Otherwise the complete nonstationary C1 Omega orbit would be periodic, contrary to A014. A nonstationary orbit cannot reach an Omega-zero in finite time by uniqueness. This proves item 3 without an uncountable-null-set gap.

For item 4, {Omega=0} is closed and Phi-invariant by the Cauchy formula. Any backward orbit starting in this set has every empirical measure supported there; its weak probability limit also gives it mass one. Such a point cannot belong to the stated basin of nu. Thus {Omega=0} intersected with D is null. S preserves volume, and S(D minus K) is a full twisted cone by Phi-invariance. Polar Fubini then gives area(sigma_D intersect {G=0})=0. Vortex invariance gives Y-invariance of the trace, and item 1 finishes the proof.

## 4. Primary-source verification

The actual PDFs and extracted texts are retained in verification, with retrieval times and SHA256 hashes in the team records. The following statements and their surrounding proofs were read from the manuscripts, not inferred from abstracts.

* V. A. Kaimanovich, Hopf decomposition and horospheric limit sets, arXiv:0807.0995v1, section 1.C-1.E, especially Theorem 11 and Remarks 16-17. Theorem 11 covers a general nonsingular countable-group action. For Z, conservative recurrence includes positive semiorbit recurrence. Theorem 19 has a freeness hypothesis; this audit does not apply it on the whole sphere. The direct wandering-set calculation above proves the needed summability on the dissipative part.
* J. Bochi and I. D. Morris, A Poincare-Bendixson theorem for Bebutov shifts and applications to switched systems, arXiv:2601.05863v1, Theorem 3.1, pages 17-18. A recurrent point of a continuous semiflow on a compact subset of S2 or RP2 is fixed or periodic. Taking the whole S2 and the positive half of Y_t meets these hypotheses. Its proof identifies the compact trajectory space with the original phase space and applies Theorem 2.4. The latter was also checked for its precise statement. No semiflow nonuniqueness is introduced in the application here.

The older Gutierrez smoothing reference listed by the author is not needed for this proof and has not been independently audited here. No numerical experiment or model response is evidence for the theorem.

## Verdict and scope

A360 CONFIRMED: exact conditional Theorem TB, with the above primary-source scope and null-set saturation. It adds a core-return structure under Dini gradient decay. It does not prove nonexistence, identify the angular limit sets as attractors or repellers, control every exceptional vortex line, or remove the Dini hypothesis.
