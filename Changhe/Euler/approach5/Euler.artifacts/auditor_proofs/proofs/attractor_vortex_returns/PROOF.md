# Repeated vortex intersections with a regular backward attractor

## Statement

Assume the full rotating profile equation with U in C2, P in C1, uniform U=o(|y|), 0<c<1/2 and any finite omega. Let Lambda be a compact regular basic hyperbolic attracting set for the backward carrier flow Psi_t=Phi_-t. Its basin W is assumed in the sense established in A115: open, invariant under the complete vorticity flow psi, and the union of complete vortex lines through Lambda. Then for Lebesgue-almost every y in W,

    T(y)={tau in R: psi_tau y belongs to Lambda}

is a nonempty closed set, unbounded in both directions, with empty interior and one-dimensional Lebesgue measure zero. This confirms CO12's principal assertion and adds the null-time conclusion. It does not assert anything about every exceptional vortex line, or classify DA and Plykin boundary leaves.

## Uniform local access to the attractor

At each z in Lambda, the attractor contains a C1 local weak-unstable disk D through z for Psi. Indeed it contains the unstable manifold of each of its points and is invariant under the carrier flow. Its tangent space is E^u plus the flow direction. The vorticity spans the complementary strong stable line, so D is transverse to Omega. The local Omega flow of D therefore fills an open neighborhood of z.

Fix y in W and one time tau0 with z=psi_tau0 y in Lambda. By the preceding flow box and continuity, there are a neighborhood V_y of y and a finite constant L_y such that every y' in V_y has some vortex hitting time sigma with |sigma|<=L_y. More precisely sigma can be chosen continuously close to tau0 using the local transverse disk. This proves the local bounded-hitting assertion needed below. If tau0 is the first positive hit and y is not in Lambda, it also proves the upper-semicontinuity assertion in Lemma 14.1 of the coordinator draft.

## Recurrence gives intersections in both directions

A049 gives a full-measure set of points recurrent under psi in positive and negative time. For such a y in W, choose t_n tending to infinity with psi_tn y tending to y. For large n the point psi_tn y belongs to V_y, so there is sigma_n with |sigma_n|<=L_y and

    psi_(t_n+sigma_n) y in Lambda.

These hitting times tend to positive infinity. Negative recurrence gives hitting times tending to negative infinity. No selection at an endpoint of a complementary interval is needed.

T(y) is closed by continuity and compactness of Lambda. If it contained an open interval, carrier invariance and transversality of B and Omega would put an open B/Omega leaf plaque in Lambda, contradicting A118. Thus it has empty interior for every y in W.

Finally Lambda has three-dimensional Lebesgue measure zero: it is compact and invariant, while Phi_t multiplies volume by exp(3ct). For every bounded measurable K and integer N>0, volume preservation by psi and Tonelli give

    integral_K integral_-N^N 1_Lambda(psi_tau y) d tau dy=0.

Exhaust W by bounded sets and take all integers N. It follows that T(y) has one-dimensional Lebesgue measure zero for almost every y. This conclusion needs no additional decay of vorticity.

## Scope

The result forbids a positive-volume family of vortex lines having only finitely bounded hitting times on one side. A particular boundary periodic line may remain exceptional. Descriptions of free branches in named hyperbolic models and the kinematic realizability of a regular attractor are separate topology questions, not consequences audited here. The proof uses the complete conservative curl flow, hyperbolic weak-unstable disks, and the A115 basin representation; it does not itself exclude the attractor.
