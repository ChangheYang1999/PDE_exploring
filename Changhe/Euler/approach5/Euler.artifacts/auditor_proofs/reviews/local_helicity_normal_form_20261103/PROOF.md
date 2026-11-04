# Local helicity-free normal form

Status: CONFIRMED as A482 after the complete independent reconstruction and postwrite read. This is a local equivalence and conditional geometric consequences, not nonexistence or existence near a flat periodic orbit.

## 1. Exact hypotheses and notation

Let O be an open subset of Euclidean R3, 0<c<1/2, omega any finite real number, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, a=1-2c, d=3c and kappa=1+c. Let U be C2 and P be C1 on O, with div U=0 and

    DU (Ay+U) + ((1-c)I+omega J)U + grad P = 0.

Write B=Ay+U, W=curl U, M=DU, g=U.B and H=P+|U|^2/2+(Ay).U. Assume U.W=0. The momentum equation implies grad P is C1, so P and H are C2. On the smaller open box in question assume grad H is nonzero, g is nonzero, and dH wedge dg=0 THROUGHOUT the box. Set h=H-H0 for an arbitrary constant H0. No decay, completeness or pressure normalization is needed locally.

After shrinking to a contractible submersion box, there are a nonvanishing C2 scalar function G, a positive C3 function f of h with f'/f=1/G, and a C2 function psi such that

    g=G(h),
    U=f(h) grad psi-grad h/a,
    B=Ay+f(h) grad psi-grad h/a,
    B psi=0,      B h=-a G(h),
    Delta h=a div(f(h) grad psi).                       (NF)

Conversely, suppose h and psi are C2, G is nonvanishing C2, f is positive C3 with f'/f=1/G, and (NF) holds classically. ADDITIONALLY require the resulting U=f(h)grad psi-grad h/a to be C2. Then P=H0+h-|U|^2/2-(Ay).U is C1 and the resulting pair satisfies the full momentum equation, div U=0, U.W=0 and dH wedge dg=0. Merely assuming h and psi C2 does not by itself give U C2.

## 2. Proof of the equivalence

The Euclidean identities, with M_ij=partial_j U_i, are

    grad H=grad P+M^T B+A^T U,
    B cross W=(M^T-M)B.

Subtracting the momentum equation yields the Lamb identity

    grad H=-a U+B cross W.

Its dot product with B gives Bh=-ag. Crossing with U and using U.W=0 gives

    gW=grad h cross U.

For alpha=U.dy, this is g d alpha=dh wedge alpha. In C2 submersion coordinates (h,x,z), d h wedge d g=0 says partial_x g=partial_z g=0. On a product box, g=G(h), with G C2 and nonzero. Connectedness of a larger open set alone would not ensure one such branch over all its h fibers.

Integrate f'/f=1/G, choosing positive initial value. Then

    d(alpha/f)=d alpha/f-(f'/f^2)dh wedge alpha=0.

On a smaller contractible box the closed C2 one-form alpha/f has a C3 potential q. Let T'=1/f and psi=q+T(h)/a. Thus alpha=f dpsi-dh/a, which proves the representation of U. Moreover Bq=g/f=G/f and BT(h)=Bh/f=-aG/f. Hence Bpsi=0. The last equation of (NF) is exactly div U=0.

For the converse, curl gives

    W=(f/G) grad h cross grad psi.

It follows that U.W=0 and U.B=f Bpsi-Bh/a=G. The vector triple product gives

    B cross W=(f/G)((Bpsi)grad h-(Bh)grad psi)
             =a f grad psi=aU+grad h.

Therefore the Lamb identity holds. Inserting the two Euclidean identities at the start of this section gives

    grad P+MB+(A^T+aI)U=0.

Since A^T+aI=(1-c)I+omega J, this is exactly momentum. Divergence is already in (NF), and g=G(h) proves the rank identity. This proves both directions without assigning a carrier independently of U.

## 3. Vorticity zeros and a tangent cylinder

Where this same box exists, W=0 if and only if grad psi=0. The forward implication follows from B cross W=a f grad psi. The reverse implication follows directly from the displayed curl formula. At such a point,

    Hess psi B=0,
    Delta h=a f Delta psi,
    DW(v)=(f/G) grad h cross (Hess psi v).            (Z)

The first follows by differentiating Bpsi=0, the second by expanding the last equation of (NF), and the third by differentiating the curl formula; all terms containing grad psi vanish. These are necessary jet identities, not free choices of a realizable jet.

Suppose a C2 surface S in the box has both B and W tangent to it. The one-form

    f dpsi=(B cross W).dy/a

annihilates TS. Thus psi is constant on each connected piece of S. Suppose also H restricted to S is a submersion. On an H-level surface choose coordinates (s,n) so S intersects it in n=0. Then psi(s,0) is constant. At a critical point of psi the restricted Hessian has matrix

    [0 b; b k].

Its determinant is -b^2. If b is nonzero the point is a saddle; if b=0 it is degenerate. Thus no nondegenerate maximum or minimum is forced by the mere existence of a zero on this level curve. The coordinate second derivative represents the intrinsic Hessian at a critical point, so no missing curvature term occurs.

If the rank identity is known only on the vortical set and its closure, it need not hold throughout a surrounding box containing an open irrotational region. This theorem requires the full box assumption. Density of the vortical set in a box is one sufficient condition, by continuity.

## 4. Conditional flat-orbit consequences

Assume Gamma is a compact periodic B orbit, U is nonzero on Gamma, and W=DW=g=0 there. Choose H0 to be the constant value of H on Gamma; constancy follows from BH=-ag=0. Assume a C2 stable cylinder S with H restricted to S a submersion, and the following on-orbit identities with one nonzero constant rho:

    grad H=-aU, grad g=rho U, Hess H=-aM,
    Hess g=rho M+(2|M|_F^2/|U|^2) U U^T.             (F)

These are additional hypotheses, supplied in the source by previously audited flat-law and cylinder results. In coordinates (theta,h) on S with Gamma={h=0}, compactness and Taylor's theorem give uniformly

    g(theta,h)=-(rho/a)h+O(h^2).

Consequently g is nonzero on every sufficiently small loop h!=0. A single G on a full tubular neighborhood is not needed for this conclusion.

Now add the distinct hypothesis that one branch g=G(h) extends C2 to h=0, with its derivative identities extending to the specified point of Gamma. Then

    G(0)=0, G'(0)=-rho/a,
    G''(0)=2|M|_F^2/(a^2|U|^2).                     (T)

Indeed the gradient comparison gives G', and Hess g=G'Hess H+G''grad H grad H^T compared with (F) gives G''. If the same branch applies along all Gamma, the last quotient must be constant along Gamma.

On a one-sided interval approaching zero, G(h)=gamma h+O(h^2), gamma=-rho/a. Therefore 1/G(h)-1/(gamma h) is bounded, and integration of f'/f=1/G yields

    f(h)=C |h|^(-a/rho)(1+O(|h|)), C>0.

For rho<=-2a the exponent is in (0,1/2], so f tends to zero. For rho>=2-c it is negative, so f diverges. The representation degenerates at g=0, and neither limit is a contradiction for a regular physical U. Extending the coupled equations through this degeneracy remains open.

## 5. Dependence and collaboration

The argument uses classical local differential calculus, a submersion box and the Poincare lemma. The full Euclidean momentum equation is retained in the converse. The conditional flat-law and cylinder inputs are stated explicitly in Section4; they are not inferred from the local normal form. Every finite omega is allowed, and no constant is claimed uniform as omega varies.

Pinned files in verification contain the complete originating proof, its exact question, and the separate coordinator review. The originating inner consultation failed. The coordinator's existing configuration specifies the primary model; this is configuration evidence, not independent provider attestation. That separate review checked the identities and explicitly found no exclusion or local Euler construction. The present reconstruction agrees, with the explicit converse regularity qualification above. No new model client or computation was used.
