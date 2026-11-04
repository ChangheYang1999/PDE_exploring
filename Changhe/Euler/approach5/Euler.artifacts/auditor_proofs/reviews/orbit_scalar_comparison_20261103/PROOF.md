# Orbit-coordinate comparison for finite scalar order

Status: the full coordinator note in the team records was read and its calculations independently reconstructed. This is a received focused comparison with the existing coordinator configured as the primary model. Provider-side runtime remains unattested. The cited nested answer is the external referee (a second model) and did not complete its requested second-model consultation.

## 1. Exact local hypotheses

Let 2/5<c<1/2, omega be any finite real number, A=cI-omega J, X=Ax, a=1-2c, b=2(1-c), and beta=a/b in (0,1). Near a twisted ray through x0!=0, suppose smooth V,S satisfy

    DV X=-[(1-c)I+omega J]V, div V=0, X.V=0,
    X.grad S=-bS, (curl V).grad S=0,
    Delta S=-tr((DV)2)-|DV|2-V.Delta V.

If V is flat at x0, S(x0)=0, and S has a finite nonzero Taylor jet at x0, then V vanishes near x0. This is the same conclusion as A1263. We verify the different coordinate reduction; the full nodal frequency proof is A1260-A1262.

## 2. Forms and the drift

Take an orthonormal basis e1,e2 of X(x0)-perp and coordinates

    F(t,y)=exp(tA)(x0+y1 e1+y2 e2).

The derivative at (0,0) is invertible. The Euclidean metric pulls back to exp(2ct)g0(y). Put G=sqrt(det g0). The one-form nu=V.dx has i_X nu=0 and Lie_X nu=-a nu, because A^T-[(1-c)I+omega J]=-aI. Hence

    nu=exp(-at)n(y), S=exp(-bt)s(y).

The three-form dS wedge dnu vanishes precisely when

    a ds wedge n-b s dn=0.

Thus d(|s|^-beta n)=0 separately on every nodal sector. A potential phi(y) exists there, with n=|s|^beta dphi. Raising the index with the metric gives

    sqrt(det g) V^mu
        =exp((c-a)t)G|s|^beta g0^(mu j) phi_j.

Taking divergence therefore yields exactly

    partial_i(|s|^beta B^ij phi_j)+|s|^beta d^j phi_j=0,
    B^ij=G g0^(ij), d^j=(c-a)G g0^(tj).

Both the exponent and drift coefficient agree with the source. B is smooth positive definite. At the center g0 is diag(|X(x0)|2,1,1), so B(0)=|X(x0)|I. Divide the whole equation by that positive scalar before writing the normalized frozen matrix as I. This harmless normalization is implicit in the source.

## 3. Scalar jet and the boundary data

Flatness of V makes Delta S flat. The first scalar polynomial S_l obeys X(x0).grad S_l=0 by scalar homogeneity and Delta S_l=0 by the pressure equation. It is a nonzero planar harmonic polynomial on the slice. Thus s has finitely many simple nodal arcs near the puncture, as used in A1260.

On each regular nodal arc, ds wedge n=0 makes n tangent component zero. Smoothness makes it vanish linearly in distance from the arc. Consequently the potential's tangent derivative is O(distance^(1-beta)), its normal derivative is O(distance^-beta), and it has a constant one-sided continuous trace. Since beta<1, the inverse angular weight is integrable. Flatness of n makes the angular oscillation of phi on a radius-r curve O(r^N) for every N, after fixed losses depending on l beta. A radial direction away from the arcs supplies a limit at the vertex; the oscillation estimate makes the limit common to every sector and arc. Normalize each sector potential by that limit. All side traces are then zero, and every sector potential is flat in value.

The potential flux across an arc need not vanish. For s=x and n=dx, phi=sgn(x)|x|^(1-beta)/(1-beta) has weighted normal flux1. The proof correctly uses zero Dirichlet trace after normalization, not a false zero-flux condition.

## 4. Full frequency comparison

The nodal map and B-normal coordinate of A1244 send the arcs to harmonic rays and make the transformed positive matrix M satisfy tau.Mnu=0 on each ray. M is Lipschitz and I+O(r). Its inverse formulation in the source, T^T B^-1 N=0, is equivalent. The transformed drift is bounded and remains in the equation.

With w=|H_l|^beta, gamma=l beta, use the notation of A1261:

    D=int w grad u.M grad u, J=int w u d1.grad u, I=D-J,
    H=int_circle w mu u2, B1=int_circle w (nu.M grad u)2/mu.

The zero side trace gives the weighted angular Poincare inequality, hence |J|<=CrD and I comparable to D. Integration by parts gives I=int_circle w u nu.M grad u. The exact mass and Rellich identities proved in A1261 are

    H'=(1+gamma)H/r+2I+O(H),
    D'=gamma D/r+2B1+O(D).

All side terms tend to zero: tangency of the Rellich field to the ray adds a distance factor to the energy singularity distance^-beta. Inner boundary terms tend to zero by flatness. The drift gives O(D), rather than being omitted.

For N=rI/H, direct differentiation leaves gamma J/H, which is O(N) by |J|<=CrD. Also

    |J'|<=C sqrt(H D'),
    B1/H-I2/H2>=0.

Cauchy-Schwarz and absorption give N'>=-C(N+1), exactly as in A1261. Integrating towards zero bounds N above, and the mass identity then gives a fixed power lower bound for H unless u is zero. Flatness gives arbitrary power upper bounds, a contradiction. Thus V=0 on every sector near the point, then everywhere nearby by continuity and the twisted flow.

The coordinator's frequency expression uses different letters for energy and drift. After this relabeling it agrees with the independent proof, including the scalar-order drift term and every boundary type. No model substitution or computational evidence is used.

## 5. CO55 and its exact quantifiers

In the actual HF/natural class, take x0 in T0 with V smooth and flat to infinite order there. If S is not flat, it has finite order since S(x0)=0. Suppose some neighborhood has no nonempty irrotational open subset. Continuity of W then says W!=0 is dense there. A1198 gives k=0 on a neighborhood of x0. Sections1-4, or A1263, give V=0 near x0, contradicting x0 in supp W.

Therefore either S is flat, or every neighborhood of x0 contains a nonempty open subset on which W=0. This confirms CO55 and is the already independently recorded A1271. Mere support of W does not supply density; no stronger density premise has been smuggled into the conclusion.

Neither branch is excluded. No smooth local germ with all actual tail identities is constructed here, and neither the general bare-decay conjecture nor arbitrary helicity is settled.
