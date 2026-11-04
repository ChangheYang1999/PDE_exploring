# The exceptional family of identically zero-helicity vortex lines

## Statement

Let U in C2(R3) be divergence free, uniformly sublinear, and solve the rotating Euler profile equation with 0<c<1/2 and any finite real omega. Put a=1-2c, kappa=1+c, A=cI-omega J, B=Ay+U, Omega=curl U,

    H=P+|U|^2/2+(Ay).U, g=U.B, h=U.Omega.

Let Gamma be the complete vortex flow and D an open Gamma-invariant set. Define

    Z={z in D: h(Gamma_tau z)=0 for every real tau}.

Then Z is relatively closed and invariant. For almost every z in D, either z belongs to Z, or its vortex line meets both strict signs of h arbitrarily far in both time directions. H is constant along the lines in Z. For almost every z in Z, g is constant along the entire vortex line as well.

If U is C^{k+1}, every derivative of h through order k vanishes at almost every point of Z. For smooth U all derivatives vanish there almost everywhere. If U is real analytic on a connected component D0 and h is not identically zero there, Z intersect D0 has zero volume. Thus the two-sign alternative holds on almost every vortex line in such an analytic component, with 'almost every' measured by ambient starting points.

These are C30's claims. They do not establish carrier invariance of Z, zero volume of Z in the smooth class, or absence of a nonzero decaying profile.

## 1. Recurrence gives the exhaustive alternative

The equations imply

    Omega.H=-a h, B.H=-a g,
    B.h+kappa h=Omega.g.

The complete, volume-preserving vortex flow and its two-sided conservativity are A048-A049 dependencies. A283 proves that a recurrent vortex point where h!=0 has both signs arbitrarily far in both time directions. Its recurrent set is invariant under every Gamma_tau, since any return sequence for z is also a return sequence for Gamma_tau z by commutation and continuity.

The definition of Z is an intersection of relatively closed sets, and continuity allows restriction to rational tau. If a recurrent z is outside Z, move to a point of its orbit where h!=0, apply A283, and translate time back. If z belongs to Z, the first scalar equation gives constancy of H along its orbit. This proves the claimed almost-everywhere dichotomy.

## 2. Density points and the second scalar observable

A C1 function f vanishing on a measurable set E has df=0 at every density point of E that belongs to E. To see this, approach the point through E inside arbitrarily narrow cones about any fixed direction. Differentiability and these directional approaches force every directional derivative to vanish.

Apply this to h on Z. On a full-measure subset Z0 of Z, both h and dh vanish. The transport equation therefore gives Omega.g=0 on Z0. The exceptional set Z minus Z0 is null. For each finite T, volume preservation and Fubini imply that for almost every z in Z its orbit spends zero time in this exceptional set on [-T,T]. Apply this on bounded pieces of Z, then take the countable union over bounds and integer T. Because Omega.g is continuous along every orbit, vanishing at almost every time makes it vanish at every time. Hence g is constant along the entire orbit of almost every z in Z.

For higher derivatives, repeat the density argument on the full-measure subset of Z where all lower derivatives already vanish. The derivatives to which the argument is applied are C1. There are finitely many of them at each finite order and countably many altogether. This proves the stated almost-everywhere flatness. A further Fubini argument, followed by continuity at each finite order, gives flatness at every point on almost every such vortex line when U is smooth.

This conclusion is solely about H and g along Gamma. The five basin-level equivalences in A320 must not all be transferred to an individual exceptional line: no carrier invariance of Z or carrier periodicity of g on Z has been proved.

## 3. The analytic subclass

On a connected open set, a nonzero real-analytic h cannot have all its derivatives zero at any point, by its convergent power series and analytic continuation. At each zero choose a derivative of least positive order that is nonzero there. Some derivative one order lower vanishes there and has nonzero gradient. Thus the zero set of h is contained in the countable union, over multi-indices, of the regular zero sets of derivatives of h. Each is locally a smooth hypersurface by the implicit function theorem, and is null. Therefore the whole zero set is null.

Since Z intersect D0 is contained in that zero set, it is null as claimed. Connected components of D are invariant under Gamma, since an orbit is a continuous path in D. Part1 then applies within each component. This proof does not assume or establish analytic regularity of all smooth Euler profiles.

## 4. Exact local freedom at a helicity crossing

For the additional local-jet remark in P1_C, take an admissible nonstagnating point with b=B(y)!=0, u=U(y)!=0, w=Omega(y) independent of b and u.w=0. Let M=DU(y) and K=DOmega(y). The second-jet compatibility condition is

    K b=(A+M-kappa I)w, tr K=0.

Every trace-free K is the curl of a divergence-free homogeneous quadratic velocity field, by the polynomial surjection proved in the team records. Specifying K b leaves K w arbitrary: in a vector basis whose first two vectors are b,w, assign the first two columns as desired and adjust the third diagonal entry to fix the trace. Hence

    Omega.h=w.(M w)+u.(K w)

takes every real value as the admissible second jet varies. The local analytic realization theorem A090 realizes each of these jets. This confirms either direction of a local helicity crossing. It constructs no decaying entire profile and says nothing about a compact invariant basin.

## Verification and scope

The full P1_C note was read. Its recurrence, density-point, Fubini and analytic-zero-set arguments were reconstructed; the jet freedom was checked using an exact linear-algebra argument. No computation was needed. Source snapshots and hashes are retained. The proof uses no pressure normalization, boundary integration, finite-energy assumption or angular truncation. It is uniform in omega and preserves the open status of the general positive-volume Z question.
