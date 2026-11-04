# Smooth finite-order supported zeros force a local k-zero region

Status: independent reconstruction of the completed coordinator the external referee (a second model) finite-order argument, with two explicit local extensions and a conditional global conclusion. Smoothness and finite order are extra tail hypotheses. The unrestricted campaign remains open.

## 1. Exact local and global hypotheses

Let x0!=0, X(x)=Ax, A=cI-omega J, Jx=(-x2,x1,0), a=1-2c, b=2(1-c), q=b/a. The global application fixes 2/5<c<1/2 and arbitrary finite omega; the local proof only needs a>0, q>2 and X(x0)!=0. Assume V and Pi are smooth on a neighborhood of x0, W=curl V, k=X.V, S=Pi-|V|^2/2, and

    div V=0, -Delta Pi=tr((DV)^2),
    grad k=X cross W-aV,
    DV X=-[(1-c)I+omega J]V,
    X.grad k=-ak, X.grad S=-bS,
    grad S cross grad k=0 on {W!=0}.            (1.1)

Assume x0 belongs to supp W, V(x0)=DV(x0)=0, and the first nonzero Taylor term V_m has degree m>=2. No density of {W!=0} near x0 is assumed. No S value is required for the first local conclusion:

    every Taylor coefficient of k at x0 is zero. (1.2)

For the second conclusion additionally suppose V_m(y)!=0 for every nonzero y in E=X(x0)-perp. Then k vanishes on a full neighborhood of x0, and that neighborhood is in supp V. If x0 is on S^2, it is an interior point of E0=supp((1_Z V)|S^2), Z=int{k=0}.

For the actual-profile global application assume U in C^2(R^3;R^3), P in C^1(R^3), finite C, and

    div U=0, (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1),
    p=(1-c)/c, 2/5<c<1/2.

Let V,Pi=P2 be the actual tails. Assume at every point of T0={V=DV=P2=S=0 on S^2} intersect supp W that V is smooth nearby and its first nonzero Taylor term V_m, m>=2, is nonzero at all nonzero vectors in E. Then U=0. Pi smooth need not be added independently in this application: smooth V makes tr((DV)^2) smooth, and local interior regularity for its Poisson equation gives smooth Pi. Concretely, on a smaller ball subtract a Newton potential of a smooth compactly supported extension of the right hand side; the difference is harmonic and smooth.

## 2. A nonzero finite pressure-scalar term

Use positively oriented coordinates (y1,y2,z) centered at x0, with e3=X(x0)/|X(x0)|. The degree m-1 homogeneity equation gives partial_z V_m=0. Divergence supplies homogeneous planar polynomials u of degree n=m+1 and w of degree m such that

    V_m=(-u_y2,u_y1,w).

Write u=r^n F(theta), w=r^m G(theta). The third column of DV_m is zero, so

    tr((DV_m)^2)=-2 det D_y^2u.

The degree 2m-2 part of Delta S is

    Q=2det D_y^2u-Delta_y((|grad_y u|^2+w^2)/2). (2.1)

At r=1 the polar Hessian of u is

    [[n(n-1)F, (n-1)F'],[(n-1)F', nF+F'']].

Integrating FF''=-(F')^2 on the circle gives

    integral det D_y^2u
       =m integral [n^2 F^2-(2m+1)(F')^2].

The energy is homogeneous of degree2m. Its averaged Laplacian is

    integral Delta_y((|grad u|^2+w^2)/2)
       =2m^2 integral [n^2F^2+(F')^2+G^2].

Consequently

    integral Q=-2m integral [(m-1)(m+1)^2F^2
                                  +(3m+1)(F')^2+mG^2]<0. (2.2)

Strictness uses m>=2 and V_m!=0. The calculation includes a possibly nonzero normal component w; it does not silently assume k=0.

If S(x0)=0 and all its Taylor terms of degrees1 through2m were zero, then Q would be zero, contradicting (2.2). Therefore S has a first nonzero term H_l with 1<=l<=2m. Its leading homogeneity equation gives partial_z H_l=0. In particular its restriction to E is nonzero. If S(x0)!=0, take l=0 and H_0=S(x0); the following argument works without (2.2). Thus in all cases 0<=l<=2m is finite and H_l is nonzero on E.

## 3. A smooth defect is flat at the supported point

Contract the rank identity with X and use (1.1):

    (grad S cross grad k) cross X
        =ak grad S-bS grad k.

Hence the smooth vector field R=k grad S-qS grad k vanishes on the open set {W!=0}. Every derivative of R vanishes on that same open set. Since x0 is in its closure and every derivative is continuous, every derivative of R vanishes at x0. This uses support, not neighborhood density; it is precisely where smoothness is essential.

If k had a first nonzero term K_s, then s>=m because k=X.V. The first possible term of R would give

    K_s grad H_l-qH_l grad K_s=0.

Dot with the displacement and apply the homogeneous polynomial identities:

    (l-qs)H_l K_s=0.

But l<=2m<qm<=qs. The polynomial ring has no zero divisors, so this contradicts both H_l and K_s nonzero. Thus k is flat at x0. In particular X(x0).V_m=0, which makes the normal component w zero. The proof of this flatness does not require an isolated leading velocity term.

## 4. The isolated leading term supplies a vortical punctured disk

Assume now the nonvanishing condition on V_m|E. Its norm has a positive minimum on the transverse unit circle, so for small y in E,

    |V(x0+y)|>=d|y|^m, y!=0.

Flatness of k gives |grad k(x0+y)|=o(|y|^m). Therefore

    |X cross W|=|grad k+aV|>=ad|y|^m/2>0

on a small punctured transverse disk. This proves W!=0 there. The exact equation R=0 consequently holds on that whole plane disk after filling its center by continuity. Its restricted scalars satisfy

    k dS=qS dk.                                (4.1)

No second derivative of a scattering map or complete vortical flow is used.

## 5. Smooth scalar lemma: flatness implies local vanishing

Let f,g be smooth on a neighborhood of0 in R^d, let q>0, and suppose f dg=qg df. If f is flat at0 and g has a finite first nonzero Taylor term, then f vanishes on a neighborhood of0.

If g(0)!=0, the derivative of f|g|^(-1/q) is zero on a connected small ball; its value at0 is zero. Otherwise let G_l be the first term of g, with l>=1, and choose a unit v with G_l(v)!=0. In a narrow connected cone around the positive v-ray, Taylor's theorem makes g nonzero and comparable to |x|^l. On this cone f|g|^(-1/q) is constant. Along the central ray, flatness of f forces the constant to zero, so f vanishes on the cone.

Also partial_v^l g(0)=l!G_l(v)!=0. Shrink to a ball on which this derivative never vanishes. Choose a thin cylinder parallel to v, containing a neighborhood of0, whose positive end and a small adjacent slab lie in the zero cone. This is possible by choosing the end at a small fixed positive distance and its transverse radius much smaller than that distance.

On each parallel closed line segment, repeated Rolle's theorem bounds the number of distinct g zeros by l. At each zero the first nonzero one-dimensional derivative has order d0<=l, since the lth derivative never vanishes. Between consecutive zeros, f=C|g|^(1/q). Starting in the positive slab the constant is zero. At the next zero t*, smoothness makes all derivatives of f zero there, because f vanishes on one side. A nonzero constant on the other side would give |f(t)| comparable to |t-t*|^(d0/q), incompatible with flatness. Thus that constant is also zero. Cross the finitely many zeros to prove f=0 on the whole segment. Varying the segment proves the lemma.

The argument controls every parallel segment, rather than assuming finitely many connected components of {g!=0} in a ball. Finite order at0 alone would not directly give that component count.

## 6. Full local region and the exact strengthened scope

Apply Section5 on E with f=k|E and g=S|E. Sections2-4 verify finite order of g, flatness of f and the exact differential identity. Thus k=0 on a transverse disk. The map (tau,y)->e^(tau A)(x0+y) is a local diffeomorphism by the inverse function theorem. Since X.grad k=-ak, its image is a full k-zero neighborhood. The velocity lower bound and its invertible scalar-rotation transport show V is nonzero off the central X orbit in this neighborhood. Thus the whole neighborhood is in supp V, and on the sphere x0 lies in the interior of E0.

The original submitted theorem assumes S(x0)=0. Sections2-3 also prove the stated extension to S(x0)!=0; in that case g is already nonzero and Section5 is immediate. The local flatness result (1.2) applies even when the leading velocity polynomial has extra zero directions.

There is a second useful local weakening of the isolated-leading premise. Keep smoothness, support and finite first velocity order, but suppose only that for some finite M and d>0,

    |V(x0+y)|>=d|y|^M

on a small punctured transverse disk. Because grad k is flat to every order, Section4 works with M in place of m; the rest of the proof is unchanged. This supplies the same local k-zero conclusion. Such a polynomial lower bound is an additional premise and is not implied here by isolation of a smooth zero alone.

## 7. Conditional global theorem and all three support branches

Use the actual-profile class of Section1 and the extra finite isolated-leading condition at every T0 point. A1053 puts boundary E0 inside T0. Section6 makes every T0 point an interior point of E0, so E0 cannot have boundary. A closed subset of connected S^2 with empty boundary is either empty or the whole sphere.

If E0 is empty and U!=0, the confirmed common-zero theorem A1057 supplies a T0 point, contradicting its interior membership in E0. Equivalently, the more specific N/T2 theorem supplies one, but is unnecessary here. Thus the empty branch gives U=0 without estimating local nodal mass.

If E0=S^2, its definition implies closure Z=S^2. By continuity k vanishes on the sphere and by twisted homogeneity it vanishes on all D. The confirmed finite-index theorem A1119 then excludes a nonzero profile with these same local hypotheses. Its pressure regularity follows from smooth V as explained in Section1. Explicitly, the angular velocity zeros outside T0 have negative index by the actual vortical saddle and the local elliptic argument; at T0 their isolated-leading index is at most zero. All zeros are isolated and hence finite on compact S^2, contradicting Poincare-Hopf total index2. This exhausts the support branches and proves the conditional theorem.

An alternative verified assembly uses A1119 in the full branch, LIT209 in the proper branch, and LIT210's o(tau) flux in the empty branch. That longer route gives the same conditional conclusion. It does not remove any tail hypothesis.

## 8. A sufficient smooth-tail assumption on the original profile

Suppose additionally that the original U is smooth and, for every integer j>=0, has a finite constant C_j with

    |D^j U(y)|<=C_j(1+|y|)^(-p-j).

For v_t(x)=e^((1-c)t)e^(omega tJ)U(e^(tA)x), its jth spatial derivative on a compact subset of D is bounded independently of large t: the exponential factor is e^((1-c+jc)t)e^(-c(p+j)t)=1. Uniform bounds for derivative j+1 give compactness in C^j on smaller compacts. Every subsequential limit is the unique established C^1 tail V; a diagonal argument therefore gives smooth V and convergence in every fixed C^j norm. The Poisson equation then gives smooth P2. No separate derivative estimates on P were assumed.

These all-order natural estimates supply smoothness only. They do not prove finite order or a leading polynomial nonzero off the X direction. Original smoothness without these decay estimates does not supply the stated compactness argument. Original analyticity is not transferred through a merely C^1 scattering map.

## 9. Source comparison, model provenance and open cases

All178 lines of the coordinator the external referee (a second model) answer, all228 lines of its separate proof and its full question were read. The negative mean identity, flat-defect argument, transverse lower bound, scalar lemma and three global branches were checked independently above. The source's exact symbolic check was not used; the circle calculation was derived directly. Its nested model consultation failed credentials, so this source is an the external referee (a second model) derivation, not a successful model review. The existing coordinator is configured with the primary model, but focused follow-up to this completed proof must be received and checked before it is recorded as such. No new model client or agent is launched.

The proof is local and conditional before its explicitly marked global assembly. Constants can depend on finite omega. The unrestricted bare-decay, arbitrary-helicity Euler conjecture remains open. Infinite flatness, general C^(1,alpha) tails, and degenerate leading directions without a polynomial lower bound are not excluded locally. Even with that lower bound, the global k-zero index problem for a degenerate leading term is not settled by this proof. No formal build or numerical experiment was needed.
