# Index obstruction on the global zero-scalar tail branch

Status: independent complete proof of coordinator CO47, with the interpretation limits in Section7. This is a necessary tail configuration and a conditional nonexistence criterion, not an exclusion of that configuration.

## 1. Statement, notation and dependencies

Let 2/5<c<1/2, omega in R, a=1-2c, p=(1-c)/c, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J and X(x)=Ax. Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

for one finite C. Let V and P2 be the actual leading velocity and quadratic pressure tails supplied by the audited scattering and canonical-pressure results. On D=R3 minus {0}, put W=curl V, k=X.V and S=P2-|V|^2/2. Write R_theta=exp(theta J) and delta_s=exp(sA). The specific properties used below are

    V(delta_s x)=exp(-(1-c)s) R_(-omega s)V(x),
    W(delta_s x)=exp(-s) R_(-omega s)W(x),
    S(delta_s x)=exp(-2(1-c)s)S(x),
    div V=0, V.W=0,
    grad k=X cross W-aV,
    W.grad S=0,
    -Delta P2=tr((DV)^2).

The first identity differentiates to DV X=-((1-c)I+omega J)V. Locally V is C^(1,alpha) for every alpha<1, W is C^alpha, S is C1, and P2 is C^(2,alpha) by the last equation and local elliptic regularity. The pressure is the actual tail pressure; an arbitrary homogeneous solution of its Poisson equation is not substituted.

On the unit sphere write G=W|S2 and

    Tflat={w: V(w)=0, DV(w)=0} intersect supp G.

Two already confirmed actual-profile results are used: if U is nonzero, W is not identically zero (A730's stronger critical-mass lower bound suffices); if U is nonzero and Tflat is empty, then k is identically zero on D (A974/A984). The latter statement retains all the preceding global profile hypotheses.

Under U!=0 and Tflat empty, the following conclusions hold.

1. V=a^(-1)X cross W, and {W=0} has no open subset of D.
2. Every angular zero w of V is either an isolated nondegenerate saddle zero of its tangent projection with W(w)=0, or a zero with W(w)=lambda X(w), lambda!=0.
3. At least one zero of the second kind satisfies

       |W(w)|^2>=2|sym DV(w)|^2,
       tr((DV(w))^2)<=0, Delta P2(w)>=0.

   If every angular zero of V is nondegenerate for the tangent projection, at least two satisfy all three strict inequalities.
4. At every zero of the second kind, S=P2=0. Its entire twisted ray consists of such zeros, is an integral curve of W as an unparametrized curve in D, and has S=0. At each of its points the Hessian of S exists at that point and

       Delta S=-2|sym DV|^2.

Consequently, in the stated actual-profile class, absence both of Tflat and of a vortical zero of V implies U=0. No statement about arbitrary helicity or bare velocity decay follows.

## 2. No open irrotational region

A974 gives k=0 throughout D. Its gradient identity yields aV=X cross W. Therefore V vanishes wherever W vanishes.

Let Z be the interior of {G=0} in the sphere. If Z is nonempty, it is proper because W is not identically zero and twisted homogeneity carries every point of D to the sphere. Its boundary is nonempty by connectedness of S2. On the open twisted cone over Z, V vanishes identically, and hence DV also vanishes. At any boundary point w, continuity gives V(w)=DV(w)=0. But supp G=S2 minus Z, so w belongs to Tflat, a contradiction. Thus Z is empty. Every angular point belongs to supp G, and the same conclusion holds for W on D.

This argument uses no regularity of the boundary of Z, no unique continuation and no finite-component assumption.

## 3. Linear algebra at a velocity zero

Fix w in S2 with V(w)=0. Put X0=Aw, M=DV(w), E=X0 perpendicular and T=w perpendicular. Since w.X0=c>0, neither X0 nor its radial component vanishes.

Homogeneity and differentiation of k=X.V give respectively

    M X0=0, M^T X0=0.

Thus M annihilates X0 and maps E to itself. With the derivative convention M_ij=partial_j V_i, the curl identity is

    (M-M^T)h=W(w) cross h.

It follows that W(w) is parallel to X0. Also sym M annihilates X0 and has trace zero. Choose an oriented orthonormal basis of E in which its restriction is diag(mu,-mu). If W(w)=lambda X0, put nu=lambda|X0|/2. The restriction of M to E is

    Mbar=[[mu,-nu],[nu,-mu]],
    det Mbar=nu^2-mu^2,
    |sym M|^2=2mu^2, |W(w)|^2=4nu^2,
    tr(M^2)=2(mu^2-nu^2).

These formulas also hold when lambda=0. In that case M is symmetric. If M!=0 its two eigenvalues on E are nonzero and opposite, so det Mbar<0. If M=0, Section2 puts w in Tflat, which is excluded.

## 4. Tangent projection and the exact index factor

For every w in S2, k=0 says V(w) is perpendicular to Aw. Define the C1 tangent field

    Y(w)=pi_w V(w), pi_w h=h-(w.h)w.

Projection pi_w from (Aw) perpendicular to T_w S2 is an isomorphism: an element of its kernel is a multiple of w and its scalar product with Aw is then that multiple times c. Therefore Y and V have exactly the same angular zeros.

At a zero w, differentiation of the projection contributes no term because V(w)=0. Consequently DY(w)=pi_w M restricted to T. Let P_E be the orthogonal projection onto E. Since M=Mbar P_E,

    det DY(w)=det Mbar det(P_E pi_w restricted to E).

This determinant equality can be seen by composing the isomorphism pi_w:E->T and its partner P_E:T->E in the opposite order. For h in E,

    P_E pi_w h=h-(h.w)P_E w.

The determinant of this rank-one perturbation of the identity is

    1-|P_E w|^2=(w.X0)^2/|X0|^2=c^2/|X0|^2>0.

Thus

    det DY(w)=(c^2/|X0|^2)(nu^2-mu^2).               (1)

Every nondegenerate zero has local index sign(det DY). In particular a zero with W=0 is nondegenerate and has index -1. No angular zero with W=0 is hidden among the degenerate zeros under the current no-Tflat hypothesis.

## 5. Compactness and the Euler characteristic

If Y has a degenerate zero, (1) gives nu^2=mu^2. Section3 rules out W=0 there, so this is already a zero of the second kind satisfying the weak inequality in Section1.

Otherwise all zeros are nondegenerate and hence isolated. There can only be finitely many: infinitely many on the compact sphere have an accumulation point, which is itself a zero by continuity and could not be isolated. The Poincare-Hopf theorem for a C1 tangent field with isolated zeros on S2 gives index sum 2. The theorem also excludes an empty zero set. If n+ and n- count the positive and negative indices, then

    n+-n-=2.

Thus n+>=2. Each positive-index zero has nu^2>mu^2 and W!=0. Formula(1) and Section3 imply the desired strict inequalities. Without the nondegeneracy assumption, the preceding degenerate-zero case gives the stated single weak inequality. Finally -Delta P2=tr(M^2) supplies the pressure sign, with the sign of that Poisson equation retained.

No isolation of all vortical zeros was assumed in the weak statement. Infinite or connected zero sets are handled by the degenerate case, not by applying Poincare-Hopf to a nonisolated set.

## 6. Pressure and the vortex ray

At a zero w with W(w)=lambda X0 and lambda!=0, W.grad S=0 implies X0.grad S=0. Homogeneity also gives X.grad S=-2(1-c)S. Thus S(w)=0, and P2(w)=S(w)+|V(w)|^2/2=0.

On the twisted ray x(s)=delta_s w, the homogeneity laws give V(x(s))=0 and

    W(x(s))=lambda exp(-(1+c)s)X(x(s)).              (2)

The coefficient never vanishes. Since x'(s)=X(x(s)), (2) shows that the ray is an integral curve of W after reparametrization. With kappa=1+c its vortex time is

    tau-tau_*=exp(kappa s)/(kappa lambda).

The ray therefore has one finite vortex-time end at the deleted origin. This does not claim that the tail vorticity extends smoothly or completely through that origin. Homogeneity gives S=P2=0 throughout the ray.

The Hessian assertion requires only regularity at this zero. Since V(w)=0 and V is C1,

    V(w+h)=Mh+o(|h|), DV(w+h)=M+o(1).

Then

    grad(|V|^2/2)(w+h)=DV(w+h)^T V(w+h)
                     =M^T M h+o(|h|).

Its gradient is differentiable at w with derivative M^T M. Thus S has a Hessian at w, even without asserting S is C2 on a whole neighborhood, and

    Delta S(w)=Delta P2(w)-|M|^2
              =-tr(M^2)-|M|^2=-2|sym M|^2.

This strengthens the Peano description of A836 to the derivative-of-gradient statement at the zero using the existing C1 regularity. It does not supply derivatives of DV near the zero.

## 7. Interpretation and countertests

CO47 passes, with two limits made explicit. First, a zero with V=0 and W parallel to X has the same leading tail algebra as an escaping W1 vortex half-line (A602/A972/A981). This does not construct an original carrier equilibrium, an actual escaping half-line, its covector rate, or a lift of the tail vortex curve. The implication proved here is from an actual nonzero profile to tail data, not from tail data to a particular original dynamical object.

Second, Delta P2>=0 at a point where P2=0 is not a maximum-principle contradiction: P2 need not be nonnegative or nonpositive nearby. At a vortical zero both S and its radial twisted derivative vanish, but neither a local extremum nor a definite Hessian is supplied. Degenerate zeros and flat zeros remain possible.

The source's nonrotating kinematic test is correct. If omega=0 and V=r^(-p)v(w), where v is any smooth surface rotated gradient on S2, then div_S v=0 and V is divergence free. Its curl has radial part r^(-p-1)curl_S v and tangential part (1-p)r^(-p-1)w cross v. Hence V.W=0 and

    X cross W=-c(1-p)V=(1-2c)V=aV.

It obeys k=0, the gradient identity and homogeneity. An arbitrary such field need not satisfy the actual pressure transport equations. This test therefore blocks an inference from only the listed kinematic identities, without furnishing a counterexample to the global Euler conjecture. The nonrotating global problem is already excluded by an independent theorem.

Dependencies: A730, A836, A974/A984, A602/A972/A981; the audited tail existence, regularity, Lamb, helicity, pressure and scalar transports stated in Section1; elementary linear algebra; local elliptic regularity and the Poincare-Hopf theorem on the sphere. The source was read in full. No numerical computation, formal build or new model client was used. The received coordinator source is from existing configured model collaboration; provider runtime is not independently attested.
