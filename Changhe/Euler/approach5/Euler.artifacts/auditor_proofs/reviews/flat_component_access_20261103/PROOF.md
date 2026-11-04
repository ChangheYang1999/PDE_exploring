# Flat-point access through components with nonzero k

## 1. Exact hypotheses and conclusions

Fix 0<c<1/2 and any finite real omega. Let Jx=e3 cross x, A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), q=b/a>2 and p=(1-c)/c>1. On an open neighborhood U of x0!=0, let V,S be smooth, put W=curl V, k=X.V, E=|V|² and P=S+E/2, and assume

    div V=0, V.W=0,
    X.grad V=-(1-c)V-omega JV,
    grad k=X cross W-aV,
    -Delta P=tr((DV)^2).                                (1)

For the component statements assume S=D_C|k|^q on each connected component C of {W!=0,k!=0} under consideration, with a finite real D_C. This is an explicit input supplied for actual tails by the confirmed rank law. It is not inferred from(1) alone.

Assume first that V and S are infinitely flat at x0. A region on which P>=delta E, for a fixed delta>0, cannot contain the chain of interior balls in Section4 if V is nonzero in the first ball. In particular a fixed nonzero-k component cannot approach x0 through an interior cone. The lower-bound criterion for the negative parts of D_C is proved in Section6. Section5 shows that, for a single component with its exact power law, velocity flatness alone suffices for the cone conclusion.

The separate global nonrotating result is stated with all its inputs in Section8, including the nodal-interior property. Its purely geometric proof applies for 1/3<c<1/2. The actual-profile derivation A963 of that property was verified in the campaign interval 2/5<c<1/2 under global zero helicity and natural velocity and gradient bounds. No new extension of A963 to an abstract larger class is asserted here. Actual nonrotating decaying profiles are already excluded independently by Theorem2.

## 2. The exact nonzero-k potential

Taking X and W products with the gradient identity yields

    X.grad k=-ak, W.grad k=0.

Thus k is transported with weight -a under X; it is not an X first integral. Using V.W=0,

    grad k cross V=(X cross W-aV) cross V=kW.

Therefore curl(V/k)=0 where k!=0. On any sufficiently small simply connected neighborhood in that set there is a smooth phi with

    V=k grad phi, X.phi=1, div(k grad phi)=0.             (2)

Only a local potential is claimed. In particular neither boundedness of grad phi near x0 nor a global zero period on an arbitrary component follows. Taking divergence of the gradient identity also gives Delta k=-2omega W3+X.Delta V, which is only a product-rule identity, not a closed scalar elliptic equation.

## 3. Virial identity and doubling

Let T=V tensor V+PI. Equation(1) gives partial_i partial_j T_ij=0. On B_r(y), integrate against f(x)=(r²-|x-y|²)/2. The function f vanishes on the sphere, grad f=-r n there and D²f=-I. Two integrations by parts give

    integral_(B_r(y))(E+3P)
        =r integral_(boundary B_r(y))(P+(V.n)²).        (3)

All boundaries are contained in U. There is no boundary at infinity and no unchosen pressure normalization: the scalar P in(1) is exactly the one used in(3).

On a region where P>=delta E with delta>0, put h=E+3P and L=3+1/delta. Then 0<=h<=LP. For each ball contained in this region define M_y(r)=integral_(B_r(y))h. By(3),

    M_y(r)>=r integral_(boundary B_r(y))P
            >=(r/L) M_y'(r).

Consequently r^(-L)M_y(r) is nonincreasing, and

    M_y(R)<= (R/r)^L M_y(r), 0<r<=R.                   (4)

One can integrate the differential inequality without dividing by M_y, so it remains valid when a small-radius mass is zero. If V is nonzero somewhere in a ball, h is positive on a set of positive measure there and that ball has positive mass.

## 4. Cone exclusion with a complete chain

Suppose a region satisfying P>=delta E contains

    B(x0+s e,4epsilon s), 0<s<=s0,
    |e|=1, 0<epsilon<1/8,

and V is not identically zero on B(x0+s0 e,epsilon s0). All sufficiently late balls lie in each fixed neighborhood used by the flatness estimates. Put lambda=1-epsilon, s_j=lambda^j s0, y_j=x0+s_j e, r_j=epsilon s_j and m_j=M_(y_j)(r_j). Then |y_j-y_(j+1)|=r_j and r_(j+1)=lambda r_j. Since 2<4lambda,

    B(y_j,r_j) is contained in B(y_(j+1),4r_(j+1)).

The latter is an assumed interior ball. Nonnegativity of h and(4) at y_(j+1) give m_j<=4^L m_(j+1). Therefore

    m_j>=4^(-Lj)m_0=m_0(s_j/s0)^gamma,
    gamma=L log4/(-log lambda)<infinity.                 (5)

On the other hand, flatness of h=(5/2)E+3S gives, for every integer N, m_j<=C_N s_j^(N+3). Choose N+3>gamma and let j tend to infinity. This contradicts(5). This argument uses positive mass in the first ball, not a presumed positive lower bound on the field along a ray.

## 5. Application to one component and a weaker flatness premise

On a fixed C with k!=0, E>0 and |k|<=K|V|, where K=sup_U|X| after shrinking U to be relatively compact. Thus

    |S|/E<=|D_C| K^q |V|^(q-2) ->0

as x approaches x0 through C. If the component contains the cone balls, choose s0 small enough that P>=E/4 throughout them. Section4 applies with delta=1/4 and L=7. No uniform bound on constants from other components is used.

For this single-component application the assumption that S is infinitely flat on the whole neighborhood is unnecessary. If V alone is infinitely flat at x0, then on C the exact relation S=D_C|k|^q and |k|<=K|V| give |S|=O(|x-x0|^N) for every N. Hence h is flat in size on every ball in the chain, which is the only scalar-flatness input in Section4. This extension still assumes the same smooth pressure equation on U and a fixed finite D_C. It does not allow arbitrary varying constants along the chain.

## 6. Component constants with control of the complement

Let G=U intersect {W!=0,k!=0}; closures are relative to U. Suppose

    S>=0 on U minus closure(G),
    sup_(y in G cap B_r(x0)) (D_(C(y)))_- |V(y)|^(q-2) ->0.        (6)

Here D_-=max(-D,0), and the supremum is zero if the set is empty. For a sufficiently small ball around x0, (6) and |k|<=K|V| give S>=-E/4 on G. Continuity extends this inequality to its closure, and the complement hypothesis supplies it elsewhere. Thus P>=E/4 on a full ball centered at x0.

For that ball(4) gives M_(x0)(R)<=(R/r)^7 M_(x0)(r). Common flatness bounds the latter mass by C_N r^(N+3). Choose N+3>7 and let r decrease to zero. Then M_(x0)(R)=0. Since h>=E there, V=0 on the ball. This proves the conclusion directly from the local virial identity, without importing a further unique-continuation assertion.

A sufficient special case is a uniform lower bound D_C>=-M, because V(x0)=0 and q>2. If G is dense, the complement condition is vacuous. In that dense case either all D_C>=0 or only finitely many relevant components suffice. Density, the complement condition, or an alternative source of the same pressure bound cannot be silently deleted.

## 7. Necessary negative-constant blowup

Retain only the complement condition in(6), and suppose x0 is in the support of W and the common-flat germ is nontrivial. Every neighborhood contains a point with S<-E/4. Otherwise the full-ball argument in Section6 would make V=0 near x0, contradicting support. Such points belong to closure(G); since the strict inequality is open, they may be approximated by points of G satisfying the same strict inequality. Choose y_j in G tending to x0 with S(y_j)<-E(y_j)/4. Then

    (D_(C(y_j)))_- |V(y_j)|^(q-2)>1/(4K^q).             (7)

For every M>0, choose an integer N with N(q-2)>M. Flatness of V and(7) imply

    (D_(C(y_j)))_- |y_j-x0|^M
       >=c_N |y_j-x0|^(M-N(q-2)) ->infinity.

Thus the negative constants diverge faster than every fixed inverse spatial power along a suitable sequence. This does not contradict smoothness of V,S: their componentwise representation is singular at k=0. The component containing y_j may change with j.

## 8. Global nonrotation and its precise nodal hypothesis

Assume now omega=0 and V is C1 on all of R3 minus{0}, with the homogeneity, divergence, gradient and helicity identities in(1). Assume also

    W(x)!=0 and k(x)=0 imply that k=0 on a neighborhood of x.     (N)

For 1/3<c<1/2, equivalently 1<p<2, we prove k=0 everywhere. Smoothness beyond that needed for the C1 spherical flow may be imposed as in the source.

Write V(rtheta)=r^(-p)(f(theta)theta+v(theta)), with v tangent to S2. Then div_S v=-(2-p)f and k=c r^(1-p)f. Let D_+={f>0}. At a boundary point of D_+, property(N) forces W=0. The gradient identity there, and f=0, yield

    v=-(c/a) grad_S f=-(1/(p-1))grad_S f.              (8)

The smooth or C1 vector field v has a complete unique flow F_t on the compact sphere. The backward flow preserves D_+. Indeed, at a proposed first exit with grad_S f!=0, (-v).grad_S f>0 by(8), contradicting exit from a positive set. If grad_S f=0, equation(8) gives v=0. Uniqueness prevents a nonconstant trajectory from reaching this equilibrium in finite time. This argument does not assume regularity of the whole boundary of D_+.

The Jacobian of F_(-t) on D_+ is

    exp((2-p) integral_0^t f(F_(-s)(theta)) ds)>1.

If D_+ is nonempty it has positive finite area. The area formula and invariance then give |D_+|>=|F_(-t)(D_+)|>|D_+|, a contradiction. For D_-={f<0}, the forward flow preserves D_- by(8) and has Jacobian greater than1 because div_S v>0 there. The identical finite-area contradiction makes D_- empty. Hence f=0 and k=0.

The proof requires the entire sphere, not a proper angular patch, and requires(N), not just pointwise zero helicity. For actual tails in the campaign HF/natural class, (N) is A963-A964, with exact scope in the team records, Section1. For the enlarged abstract interval 1/3<c<1/2, (N) remains a stated hypothesis of this geometric theorem. The independent full-profile nonrotating exclusion makes no need to claim a larger abstract derivation of(N).

## 9. Why the same area argument is not a rotating argument

For any omega, on the unit sphere put f=theta.V and Y=V-(f/c)X. Then Y is tangent to the sphere. The radial component of the twisted homogeneity identity gives partial_r f=-p f+(omega/c)(Jtheta).grad_S f. Since div_S(Jtheta)=0 and Y=v+(omega/c)f Jtheta,

    div_S Y=(p-2)f=((1-3c)/c)f.                         (9)

At a regular boundary point of {k>0} where(N) holds, W=0, grad k=-aV, and Y.grad k=-aE<=0. Consequently Y points out of {k>0}. Integrating(9) over a regular such domain gives integral_(k>0) f<=0 when c>1/3. For omega=0, k=cf, but for omega!=0 the relation is k=cf-omega(Jtheta).V. Thus the divergence has no required sign on {k>0}; this calculation gives no area contradiction.

There is also no smooth local surface perpendicular to X in R3 minus{0} when omega!=0. To justify the assertion even on the plane x3=0, note that curl X=-2omega e3 and X.curl X=-2omega c x3. On a C2 surface with normal parallel to X, the normal component of curl X is zero, by Stokes on every small surface patch. Therefore such a surface would lie in x3=0. Its tangent plane would then be that plane, so its normal would be parallel to e3. But X is nonzero and horizontal on x3=0 away from0, a contradiction. This is a geometric obstruction to that proposed choice of section, not a theorem excluding every possible rotating proof.

## 10. More general chains and the cusp limitation

The cone is only one sufficient geometry. The same proof applies to balls B(y_j,r_j) in any positive-pressure region if there are constants Lambda>1, C0>0 and 0<lambda<1 such that

    B(y_j,r_j) is contained in B(y_(j+1),Lambda r_(j+1)),
    B(y_(j+1),Lambda r_(j+1)) lies in the region,
    |y_j-x0|+r_j<=C0 lambda^j,

and the first ball has positive mass. Doubling gives m_j>=Lambda^(-Lj)m0, while common flatness gives m_j<=C_N lambda^((N+3)j). Choosing N sufficiently large contradicts these bounds. This allows curved approaches with a bounded number of admissible steps at each geometric scale.

For a path whose available ball radius is comparable to s^N with N>1 at distance s from x0, successive admissible steps of comparable relative radius can instead number on the order of s^(1-N). A bounded-factor doubling estimate then gives only an exponential lower bound of type exp(-C s^(1-N)), which is compatible with infinite-order flatness. This describes the limitation of this chain method. It does not construct an Euler cusp or prove that every cuspidal component is possible.

## 11. Verdict and remaining scope

CO58(a)-(c) are confirmed under their displayed local hypotheses. CO58(d) is confirmed as the full-sphere theorem in Section8, with(N) explicit. No automatic extension of the actual-profile nodal theorem beyond its checked hypotheses is used. The velocity-only flatness refinement in Section5 and the general chain criterion in Section10 are independent additions.

Unrestricted cuspidal access, uncontrolled negative constants, irrotational complementary regions without a pressure sign, and the arbitrary-omega analogue of Section8 remain unresolved. So do the unrestricted common-flat and bare-decay campaign problems. The full coordinator note, the full nested proof, all cited nodal hypotheses and all eleven independent sections were read. No numerical computation, formal build or external job was used. This is continued comparison with the configured model coordinator; its nested model consultation was unavailable and provider runtime remains unattested.
