# A transported field cannot approach its zero set inside a locally maximal hyperbolic set

## Statement

Let O be an open subset of R3, B a C2 vector field on O and Psi the flow of -B. Suppose div B=d>0 is constant. Let W be C1 and obey

    W(Psi_t y)=exp(kappa t) DPsi_t(y) W(y), kappa>0,          (1)

whenever the flow is defined. Let Lambda be a compact, locally maximal, uniformly hyperbolic Psi-invariant set in O with B nowhere zero. If a component has two stable dimensions, assume kappa>=d on it. No such additional inequality is needed for stable dimension one.

(A) If Lambda is topologically transitive, W either vanishes everywhere on Lambda or is nowhere zero on Lambda. In the latter case W lies in the stable bundle. In stable dimension one, it spans that bundle, and every periodic orbit of period T has stable multiplier exp(-kappa T) and unstable multiplier exp((kappa-d)T).

(B) Let a have a forward Psi orbit with compact closure in O, and suppose its omega-limit K lies in Lambda. If K contains even one zero of W, then W(a)=0. Thus W(a)!=0 forces W to be nowhere zero on K. Transitivity of Lambda is unnecessary for (B).

For an Euler profile, d=3c, kappa=1+c and 0<c<1/2 meet all rate conditions. This excludes the proposed mixed zero/nonzero-vorticity limits only when the limit lies inside a nonsingular locally maximal uniformly hyperbolic set. It says nothing about arbitrary nonhyperbolic limits or limits containing carrier zeros.

## 1. Hyperbolic inputs and the zero stable-leaf lemma

The standard local product theorem says that for close x,y in Lambda there is a point

    z in W^cs_loc(x) intersect W^u_loc(y), with z in Lambda,

and uniform C,lambda>0 give

    dist(Psi_-t z,Psi_-t y)<=C exp(-lambda t) dist(z,y), t>=0. (2)

Here W^u is the strong unstable manifold and W^cs the weak stable manifold; the latter includes the flow direction. A second standard input is the local stable-set characterization: an orbit tending in distance to Lambda belongs to W^cs(q) for some q in Lambda. In particular, after a constant phase correction its orbit approaches that of q exponentially, so their omega-limit sets agree. These are the local-product and stable-set inputs already used in A185, not a claim that every hyperbolic set is locally maximal.

Put Z={W=0}. It is closed and flow invariant by (1). The zero stable-leaf lemma of A185 applies to the compact hyperbolic subset Lambda intersect Z, without requiring that subset itself be locally maximal:

    x in Lambda intersect Z implies W^cs(x) is contained in Z. (3)

Here and below leaves are restricted to their domain of flow in O. For completeness, the essential proof is given next.

In stable dimension one, local W-flow conjugacy shows that W is tangent to a stable leaf: a short W shift of a point on the leaf stays exponentially close under Psi, since its W time contracts by exp(-kappa t). On a stable arc I joining x in Z to y, the C2 stable-manifold theorem and exponential contraction give bounded leafwise distortion of J_n=|D Psi_n| on the stable tangent. Therefore

    length(Psi_n I)<=C J_n(y) length(I).

Local Lipschitz continuity of W and its zero at Psi_n x bound |W(Psi_n y)| by L times that length. Tangency and (1) instead give |W(Psi_n y)|=exp(kappa n)J_n(y)|W(y)|. Cancellation and n->infinity force W(y)=0. Flow saturation and iteration prove (3).

In stable dimension two, a local stable disk saturated by a short flow interval is open. On every forward orbit in this neighborhood the derivative norm is bounded, because the stable plane contracts and the nonzero flow direction is uniformly bounded. Since det DPsi_t=exp(-dt), the conorm is at least C^(-1)exp(-dt). Thus

    |W(y)|<=C exp((d-kappa)t)|W(Psi_t y)|.

The last factor tends to zero as the orbit approaches the zero hyperbolic set. The rate condition kappa>=d gives W(y)=0. This proves a zero neighborhood and (3). Stable dimension zero is impossible with positive d: two expanding directions and a bounded nonzero flow direction contradict the decaying full determinant.

## 2. Density on a transitive set

For any x in a transitive Lambda, W^cs(x) intersect Lambda is dense in Lambda. To prove this, fix a target o in Lambda and a small radius r. Choose the local product radius so that the right side of (2) at t=0 is less than r. Transitivity provides v within r of o and T>=0 such that Psi_T v is within that product radius of x. Let z be the local intersection of W^cs(x) with W^u(Psi_T v). Then Psi_-T z belongs to W^cs(x) intersect Lambda and is within r of v by (2), hence within 2r of o. This proves density.

If W vanishes at x in Lambda, (3) and this density make it vanish on Lambda. Otherwise compactness gives min_Lambda |W|>0. Equation (1) gives

    DPsi_t W(y)=exp(-kappa t)W(Psi_t y).

Its norm decays exponentially. Uniform hyperbolic splitting and a flow direction bounded above and away from zero force W(y) into the stable bundle. In dimension one it spans that bundle. At a period-T point the multiplier is exactly exp(-kappa T), with positive sign. The neutral multiplier is one and the full determinant is exp(-dT), so the remaining multiplier is exp((kappa-d)T). This proves (A).

## 3. Direct limit-set proof

First take q in Lambda and assume Psi_(t_n)q tends to x in Lambda intersect Z for t_n->infinity. For large n, local product structure gives

    z_n in W^cs_loc(x) intersect W^u_loc(Psi_(t_n)q),
    z_n in Lambda.

Equation (3) gives W(z_n)=0, and zero-set invariance gives W(Psi_(-t_n)z_n)=0. The points z_n and Psi_(t_n)q are within a uniform bounded local plaque size. Equation (2) therefore yields

    dist(Psi_(-t_n)z_n,q)<=C exp(-lambda t_n) times that size ->0.

Closedness of Z gives W(q)=0. This argument does not require q to be recurrent, a dense orbit, a finite spectral decomposition, or a chain-recurrence theorem.

Now take the a in (B). The stable-set characterization supplies q in Lambda with a in W^cs(q), after absorbing its constant phase, and omega(q)=K. If K meets Z, the preceding paragraph gives q in Z. Apply (3) once more to obtain a in Z. This proves (B).

## 4. Source and scope audit

The actual primary manuscript V. Climenhaga, SRB and equilibrium measures via dimension theory, arXiv:2009.09260v1, Definitions 2.5-2.7, equation (2.9), and Definition 2.11 with its following paragraph, gives the strong/weak convention, backward contraction and local product equivalence used above. The local stable-set characterization and the C2 leafwise distortion input are exactly the hyperbolic inputs explicated in the team records.

This confirms the zero/nonzero dichotomy and vorticity conclusion proposed as CO20. The separate clause that every such limit lies in one basic spectral component is unnecessary here and is not an additional conclusion of this audit. No claim about the general non-locally-maximal case or about the existence of a gamma model is made. The continuity-only Livsic alternative in coordinator Remark20.3 is also outside this verdict.
