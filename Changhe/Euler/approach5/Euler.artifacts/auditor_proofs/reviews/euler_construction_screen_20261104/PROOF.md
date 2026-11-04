# Version-specific Euler construction screen

Status: complete source comparison, awaiting the existing-agent comparison and designated verdict. This screen does not certify any of the long construction proofs.

## 1. Exact question, sources and reading scope

The target is a whole-space pair U in C2(R3;R3), P in C1(R3), with div U=0 and

    (1-c)U+[((cI-omega J)y+U).grad]U+omega JU+grad P=0,
    U(y)->0 uniformly as |y|->infinity,  2/5<c<1/2,
    J(x1,x2,z)=(-x2,x1,0),  omega any finite real number.

The question checked here is whether the inspected statements in six specified manuscripts establish an element of this class. The conclusion is limited to those statements. It is not a classification of all consequences of the papers or a proof that any construction is false.

The source submission is LIT365, hash f017f9190373a397f17d8631ba6472851f2e107b2cda62de7d160ce96d2658c5. All seven sections, all eighteen manual checks and the supporting reading record were read. The primary evidence is in the read-only directory retained manuscripts. This agent read the following PDF pages through the retained form-feed-separated text:

| Manuscript | PDF pages read here |
| --- | --- |
| arXiv:2605.19716v2 | 1,4,5,6,8 |
| arXiv:2605.19716v1 | 1,4,5 |
| arXiv:2605.04526v2 | 1,13,14,15,16,17 |
| arXiv:2605.04526v1 | 1,12,13 |
| arXiv:2605.04181v2 | 1,2,3,4,10,17,19 |
| arXiv:2605.04181v1 | 1,4,23 |

The four retained page images 19716v2 pages5 and8, 04526v2 page16, and 04181v2 page4 were also visually inspected. All three retained abstract-page texts and the two retrieval records were read. No new network retrieval was performed by this agent. The retained retrieval records report the source agent's requests and times; this agent independently hashes the actual files, without claiming to have witnessed those HTTP requests. No full reading of all255PDF pages, whole-inventory audit, or complete PDE construction verification is claimed.

## 2. Exact self-similar exponent and rotation

Shao, Wei, Zhang and Zhang, arXiv:2605.19716v2, Theorem1.1 on PDF pages4-5, state that for d>=3 and 0<alpha<1-2/d there is gamma0>1 such that the construction works for every gamma>gamma0. Its displayed velocity is

    u(t,x)=(T-t)^(gamma-1) U(x/(T-t)^gamma).

Put tau=T-t and y=x/tau^gamma. The differentiation is

    partial_t u=tau^(gamma-2)[(1-gamma)U+gamma(y.grad)U],
    (u.grad_x)u=tau^(gamma-2)(U.grad_y)U.

Writing the pressure gradient in its corresponding scale, p=tau^(2gamma-2)P(y) up to a time-only constant, gives grad_x p=tau^(gamma-2)grad_y P. Therefore the velocity profile equation has coefficient c=gamma:

    (1-gamma)U+(gamma y+U).grad U+grad P=0.

In the dimensional specialization d=3, gamma>1 is outside the campaign interval. The profile is axisymmetric without swirl. For an axisymmetric vector field, U(R_theta y)=R_theta U(y), and differentiating in theta gives (Jy).grad U=JU. Thus adding the rotating terms -omega(Jy).grad U+omega JU contributes zero for every omega. It leaves the exponent gamma unchanged.

The normalized relative-vorticity parameter on PDF page8 is mu=gamma/[1+(d-2)gamma]. It is not c in the velocity equation. In d=3, mu=gamma/(1+gamma)>1/2 anyway. Neither replacing gamma by its reciprocal nor confusing it with mu is justified.

The theorem states U in C^(1,alpha)_loc, smooth off the origin, with a growing upper bound C<y>^(1-1/gamma). Membership in C^(1,alpha) does not prove nonmembership in C2, and an upper bound allowing growth does not prove failure of decay. Neither inference is needed. The exponent mismatch alone suffices for this reported exact family. The manuscript's description of infinite energy is not independently established here.

## 3. The finite-energy theorem concerns an asymptotic solution

In 19716v2, Theorem1.3 on PDF page6 states a finite-energy axisymmetric no-swirl evolution, with initial velocity in C^(1,alpha) and L2, smooth off the origin, and optionally compactly supported initial vorticity. The exponent remains sufficiently large gamma>1. Its vorticity size is comparable to tau^-1 and its concentration scale to tau^gamma, with positive solution-dependent comparison constants.

The same page says that truncation and correction produce asymptotic self-similarity. It does not assert that the exact stationary profile in Theorem1.1 has finite energy. Transferring finite energy from this evolution to that profile would conflate two different conclusions. Version1 pages4-5 already use gamma>gamma0>1, while the finite-energy construction is announced for subsequent work. Its global C^(1,alpha) notation is not used here to infer boundedness. The retained abstract record dates version1 to May19 and version2 to July22; their cover dates are May20 and July23. These distinct kinds of dates should not be silently interchanged.

## 4. The interior paper's later version retains missing steps

Shahmurov's 2605.04526v1, titled Euler Singularities II: Interior Quadrupole Blow-Up for Smooth Axisymmetric Euler with Swirl in R3, is dated May6 in the retained arXiv record. Its Theorems11.1 and12.1, PDF pages12-13, assert propagation and finite-time gradient blow-up from smooth decaying whole-space data. The full proof is not audited here. Even the stated dynamic conclusion does not provide an exact rotating stationary profile with 2/5<c<1/2.

Version2, dated September10 and titled Source-Driven Transitions in Axisymmetric Euler Flow, states a more limited result. PDF pages13-15 distinguish three objects: a conditional contraction estimate for two fixed material labels of an exact planar solution in Theorem16.3; a terminal trace for one finite reference in Theorem16.4; and a conditional outgoing level set in Theorem16.5. They cannot be combined into an unconditional same-solution Euler singularity.

Section17, PDF pages16-17, explicitly retains global continuum defect estimates, sufficient next-block admission for the same unforced solution, planar-to-exact-cylindrical whole-space comparison, and repeated regeneration with summable physical times from a single datum. It explicitly says that neither a finite-time Euler singularity nor a regularity theorem is established. These limitations were read in the manuscript, not inferred from its abstract.

No finite-reference interval enclosure, Dini argument or PDE comparison proof was independently certified. The evidence supports a narrower current statement, not a declaration that the entire earlier proof was refuted or formally withdrawn.

## 5. The boundary paper's conditional regimes must be distinguished

Shahmurov's 2605.04181v1, titled Euler Singularities I: Boundary Blow-Up for Smooth Exact-Odd Axisymmetric Euler with Swirl, is dated May5 in the retained record. Theorems1.1 and12.19 on PDF pages4 and23 claim a boundary singularity in a periodic cylinder. This is a different domain from R3, and no statement inspected here removes that difference or supplies the target profile.

Version2, dated September10 and titled Boundary Hyperbolic Packets in Axisymmetric Euler Flow, retains a smooth axisymmetric swirl setting in 0<r<1, z in T, with u^r=0 at r=1. Its Theorem10.1 on PDF page10 is an earlier conditional formulation: it assumes an odd hyperbolic sign class for G, the listed kernel, tail, coupling and shear controls, and a preserved curvature-ratio inequality. The next Section11 introduces the exact-odd class for both Gamma and G and explicitly distinguishes it from the earlier parity formulation. Theorem1.1 and the later Theorem12.7 concern the exact-odd criteria. Thus LIT365's collective description of Theorems1.1,10.1,12.7 as exact-odd needs this qualification; Theorem10.1 must not be assigned an unstated exact-odd Gamma premise.

The inspected criteria have the form of positive comparison inequalities, such as D^+ M>=c1 B^2 and B'>=c2 M B, with positive constants and initial amplitudes, while a complete packet regime persists on one common interval. Theorem12.7, PDF page17, distinguishes initial admissibility from persistence. AppendixB on PDF page19 explicitly retains persistence as an unresolved step. A smooth initial datum entering the regime does not by itself establish its subsequent invariance. These are source-scope observations; the detailed estimates and the comparison blow-up proof are not independently certified here.

This parity precision does not affect the screen's conclusion: the domain is a periodic cylinder, the current theorem keeps persistent-regime assumptions, and neither version supplies the requested exact whole-space profile. The correction should be made before treating every sentence of the source summary as confirmed.

## 6. Exact conclusion and limits

The elementary scaling calculation is an independent proof. The remaining deductions compare the actual inspected statements and their hypotheses with the target. They establish only that these statements do not supply a target counterexample. They do not establish nonexistence, classify all current literature, certify the constructions, or exclude a different result with additional arguments. The unrestricted arbitrary-omega conjecture remains open.

The source hashes, precise page manifest and retained evidence references accompany this argument under verification. No mathematical computation or formal build was needed. Existing configured model C/coordinator comparison is requested, including the parity precision in Section5. Actual provider execution is independently unattested.


## 7. Accepted parity correction

At07:20 the source agent accepted the Section5 precision after consulting the actual pages10-11. The corrected LIT365 pin is197747f2d4043d6db697b6c895e23a1dd241bbeff6762af5403d031c494e75de. An independent complete diff against the captured f017f919 source contains exactly one paragraph replacement in Section5. It now separates Theorem10.1's earlier odd-G/curvature-ratio formulation from the exact-odd Gamma and G formulation in Section11 and the later criteria. This agrees with the primary passages read here. No other mathematical or source-scope statement changed. The historical request in Section5 is therefore resolved for this new pin; existing-agent analytical comparison is still pending.

## 8. Existing C comparison and its precise scope

The complete six-item C comparison of 2026-11-04T07:38:12Z was read and
captured under in the team records. It agrees with the exponent, the
exact/asymptotic distinction and the corrected parity summary. Its listed
primary passages were read by that agent; this agent does not enlarge its
own reading inventory merely by adopting the comparison. Here pages10
and11 of 04181v2 were additionally read in full, so page11 is added to the
inventory above.

The comparison's parameter cross-check is immediate: the map
mu=c/(1+c) is increasing for c>0, and maps the campaign interval
(2/5,1/2) to (2/7,1/3); gamma>1 gives mu>1/2. Its energy exponent
5-2/c is only a consistency check with the manuscript's stated
description, not a deduction of infinite energy from an upper bound.

The elementary wall equations can also be checked directly. Put
b=partial_z Gamma, a=partial_z G and sigma=-partial_z u^z at (1,0).
The wall condition and odd u^z give u^r=u^z=partial_z u^r=0 there.
Differentiating D_t Gamma=0 and D_t G=r^(-4)partial_z(Gamma^2)
in z gives b'=sigma b and, when Gamma(1,0)=0,
a'=sigma a+2b^2. These are the point identities on page11, and
do not establish persistence of any packet regime.

One coefficient in the comparison needs a harmless qualification.
If Gamma(1,z)=g0+bz+O(z^2), then
partial_z(Gamma^2)(1,0)=2g0 b, not 2b unless g0=1.
The parity incompatibility requires g0 b nonzero, as the manuscript's
positive value and positive slope assumptions ensure. Positivity of g0
alone is insufficient. The comparison's conclusion is accepted with
this explicit qualification, not as an unqualified coefficient formula.

Its diagnostic script, sixteen reported checks and execution log are
not certified here. No additional construction theorem or full proof in
any manuscript has been certified. The scope remains the specified
statements and versions, with the corrected source pin197747f2.
