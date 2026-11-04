# Vortex half-lines leave a regular carrier trapping region

## Exact statement

Assume the full rotating Euler profile equation with U in C2(R3;R3), P in C1(R3), uniform U=o(|y|), 0<c<1/2 and arbitrary finite omega. Let Phi be the complete carrier flow of B=(cI-omega J)y+U, Psi_t=Phi_-t and psi_tau the complete flow of Omega=curl U.

Let N be compact, with Psi_t N contained in N for t>=0, and let

    A=intersection_(t>=0) Psi_t N

be nonempty and contained in Reg={B cross Omega!=0}. Then for every x in A there is a positive tau with psi_tau x outside N, and a negative tau with psi_tau x outside N. Strict trapping, hyperbolicity and transitivity need not be assumed separately for this assertion. In the target application N is a compact trapping neighborhood of a regular basic backward attractor.

## Proof

The nested compact sets defining A make it compact and invariant under the full carrier flow. Let

    A_plus={x in A: psi_tau x belongs to N for every tau>=0}.

It is closed, since each map psi_tau is continuous, and thus compact. The commutation identity

    Psi_t psi_tau = psi_(exp(-(1+c)t)tau) Psi_t

shows that A_plus is forward invariant under Psi for t>=0: the image of the entire positive half-line is the entire positive half-line through Psi_t x, and it lies in Psi_t N, hence in N.

Suppose A_plus is nonempty. Define

    K_plus=intersection_(t>=0) Psi_t A_plus.

These are nonempty nested compact sets. Their intersection is nonempty, compact and invariant under Psi_s for every real s. For s>=0 this follows by shifting the nested intersection from t>=0 to t>=s; invertibility gives the negative times. We do not assert that A_plus itself is invariant under negative Psi times.

The union

    V_plus={psi_tau x: x in K_plus, tau>=0}

lies in N and is invariant under the full carrier flow by the same positive rescaling of tau. Any full invariant subset of N lies in A: if y is in that subset, then Psi_-t y belongs to N, so y belongs to Psi_t N for every t>=0. Thus V_plus is contained in A.

Take x in K_plus and a sufficiently small tau0>0. At z=psi_tau0 x, both B and Omega are nonzero and independent, because z is in A. For small |s| and small |h|<tau0, the points

    Phi_s psi_(tau0+h) x

lie in V_plus. They form a nonempty open plaque of the two-dimensional leaf spanned by B and Omega. This contradicts A118: no compact full carrier-invariant subset of Reg contains such a plaque. Hence A_plus is empty. Replacing tau>=0 by tau<=0 proves that A_minus is empty as well.

For completeness, A118 uses the hyperbolic splitting forced by the bracket and constant divergence on a compact regular invariant set. Saturating the presumed B/Omega plaque by local strong stable curves for Phi yields an open set of forward-bounded carrier orbits. Such an open set is impossible: positive constant divergence and outward radial transport make the whole forward-bounded core compact and of Lebesgue measure zero. The detailed proof is in the team records.

## Uniform finite-time consequence

There is a finite T_plus such that every x in A leaves N at some tau in (0,T_plus], and similarly a finite T_minus for negative times. For each x choose one exit time. The exit persists on a neighborhood of x because N is closed. A finite cover of compact A bounds those chosen times. This consequence makes no assertion that a half-line stays outside N after its first exit.

## Correction and scope

This confirms B21 with a repaired proof. Its original equivalence proves only that Phi_s x in A_plus implies x in A_plus; it does not prove forward-Phi invariance of A_plus. The compact invariant subset K_plus removes that gap. The result states exit from this trapping region. It does not prove unboundedness of a vortex half-line, escape to infinity in vortex time, or absence of later returns. No extra pressure hypothesis is used. Completeness comes from A006 and A048; the other substantive dependency is A118.

Audit written: 2026-11-02T20:39:22Z
