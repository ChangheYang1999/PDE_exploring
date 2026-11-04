# Limits of the tail-direction and invariant-measure reductions

Status: scope correction recorded in A515. No new Euler existence or nonexistence assertion is made.

## 1. Notation and exact settings

Write A=cI-omega J, B=Ay+U, W=curl U, a=1-2c, H=P+|U|^2/2+(Ay).U and g=U.B for a full incompressible rotating Euler profile with U in C2(R3;R3), P in C1(R3). A global helicity-free profile has U.W=0 everywhere. A vortical carrier equilibrium p has B(p)=0, W(p)!=0 and a real covector rate rho defined by DB(p)^T U(p)=rho U(p). Under uniform sublinearity,0<c<1/2 and every finite omega, A496 gives rho<=-a. The lower range rho<=-2a is a necessary witness range from the separate coverage argument, not an assumption on every equilibrium.

At the additional far-field scope U->0, DU=O(sqrt r),1/3<c<1/2, A509 gives leading fields V,W_* and E(w)=-aV(w)+Aw cross W_*(w) on the unit sphere. Write Z_E={w:E(w)=0}.

## 2. A singleton zero component is not automatically excluded

A512 proves the following implication. For a tail direction w associated with the escaping or critical-saturation alternatives of a vortical equilibrium with rho<-a,

    {w} a connected component of Z_E
        implies V(w)=0 and Aw cross W_*(w)=0.              (1)

Thus (1) supplies an additional necessary condition for a singleton component. It does not exclude that component. To exclude it one also needs the two fields on the right to have no common zero at that direction. That additional hypothesis was not proved for general profiles.

Consequently the decision-packet assertion that escaping directions must belong to a non-isolated part of Z_E is stronger than A512. The correct alternatives retain directions with singleton components that satisfy the simultaneous zeros in(1). A singleton connected component can also fail to be an isolated point of the whole zero set. The confirmed hypothesis should therefore be stated as a singleton connected component, rather than weakened in prose to an isolated point.

A514 exhibits an exact kinematic leading tail with Z_E equal to the whole sphere. It neither removes the common-zero possibility in(1) for general tails nor supplies an actual smooth profile. No example here establishes that any stronger Euler implication is false; that implication remains unproved by the cited chain.

## 3. Ergodic measures do not classify every point of a compact limit set

The repaired B32 proposal concerns a forward-bounded half of the complete vortex line through p. Its compact full-B-invariant limit set K has W=0, H=H(p), g=0, grad H=-aU and grad g=rho U. The independent reconstruction is in the team records; its mathematical verdict is separate and was pending when this scope audit was recorded.

The proposed conclusion has the following quantifiers:

    Every ergodic invariant probability supported on K is either
    a mass at an irrotational carrier equilibrium,
    or a probability on a flat periodic carrier orbit.      (2)

Both kinds carry the same rate rho. If rho<=-2a, they are companion witnesses of the two kinds stated in B32. Compactness supplies an invariant probability, and ergodic decomposition supplies at least one ergodic one, so (2), once proved, does imply existence of such a companion witness.

It does not follow from (2) that every point of K lies on one of those equilibria or periodic orbits. The missing assertion is that each point of K belongs to the support of an invariant probability, with additional control of the supports under decomposition. Invariant-measure statements allow points that carry no invariant probability mass, including possible connecting or wandering points. No argument eliminating such points has been supplied for K. Even density of the union of supports would not imply membership in that union.

Accordingly, phrases saying that K consists of, or is made of, only the listed equilibria and periodic orbits should be replaced by the measure classification and its companion-existence consequence. This preserves the useful W1-vortical reduction without introducing a stronger pointwise decomposition. This audit does not construct an Euler limit set with extra points; it identifies the missing inference and leaves that stronger assertion OPEN.

## 4. Verification and scope

Read the actual decision packet, coordinator Note53 and B32 source; compare with A512's complete proof and with the independent B32 reconstruction. The configured-model coordinator packet is part of the continuing exchange. The two corrections concern exact logical scope. They require no computation, numerical examples, additional regularity, or new remote model client. The unrestricted all-omega conjecture remains OPEN.
