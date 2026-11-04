# Dense vorticity, scalar sectors and vanishing pressure jets

Status: independent reconstruction of Theory Agent C C46, including the two strengthenings proposed in the focused LIT206 preparatory comparison. The exact conditional results below are confirmed. Interior points of the open k=0 set and points with accumulating open irrotational patches remain outside the argument.

## 1. Exact theorem class and local regions

Fix 2/5<c<1/2 and any finite real omega. Let U in C2(R3;R3), P in C1(R3), with one finite C, satisfy

    div U=0,
    (1-c)U+DU((cI-omega J)x+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1), p=(1-c)/c,
    J(x1,x2,x3)=(-x2,x1,0).

Let V,P2 be its actual leading velocity and canonical pressure tails on D=R3 minus{0}. Set

    A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J,
    a=1-2c, b=2(1-c), q=b/a>6, eta=1/q,
    W=curl V, k=X.V, S=P2-|V|^2/2, Z=int_D{k=0}.

The established regularity is V in C^(1,alpha)_loc and P2 in C^(2,alpha)_loc for every 0<alpha<1. All closures and boundaries below are relative to D. A point is called densely vortical if W!=0 is dense in some ball about it. Otherwise every ball contains a nonempty open irrotational patch. In particular every point of closure(int{V=0}) fails the density premise.

The principal strengthened conclusion is this: if x0 is a densely vortical zero of V and x0 is not in Z, then

    V(x0)=DV(x0)=W(x0)=0,
    P2(x0)=grad P2(x0)=D2P2(x0)=0,
    |P2(x0+h)|+|S(x0+h)|=O_beta(|h|^beta)
                                      for every beta<4.       (1)

In particular both scalars are o(|h|^3). This is a pointwise order statement, not an assertion that P2 or S has three continuous derivatives nearby. At points outside closure Z there is the further forced alternative: negative constants in S=D_G|k|^q on local nodal domains are unbounded below in every neighborhood. These conclusions do not apply to a general supported flat zero lying inside Z.

We first prove the submitted C46 statements, then justify the strengthening in Sections9-10. Constants are local and may depend on the fixed omega and on the point.

## 2. Confirmed actual-tail inputs

The identities used are

    div V=0, Delta P2=-tr((DV)^2),
    grad k=X cross W-aV,
    X.k=-ak, X.S=-bS, X.P2=-bP2, DV X=-LV,
    grad k cross grad S=0 on {W!=0}.               (2)

The pressure equation is obtained distributionally from div V=0 and then holds pointwise by local elliptic regularity. The actual-profile return theorem A963 implies

    k=0 implies W=0 outside closure Z.             (3)

A973 gives V=DV=W=0 on boundary Z, whose points lie in supp W. These are actual-profile theorems, not consequences of the formal leading tail identities alone.

The local pressure rigidity A1006, here used with alpha=1/2, says that if v is C^(1,1/2), div v=0, pi solves the pressure Poisson equation, v(x0)=curl v(x0)=0, and s=pi-|v|^2/2 satisfies

    s-s(x0)>=-|v|^2/8

on a full ball, then v is zero on a smaller ball. The strict constant 1/8 is below alpha/(2(1+alpha))=1/6. The proof uses a spherical stress identity; it does not assume that pi is nonnegative. The independent proof and the precise natural-tail hypotheses of the cited results are listed in Section13.

## 3. Density extends the scalar relation across vorticity zeros

On an open set B where W!=0 is dense, continuity extends grad k cross grad S=0 to all of B. For parallel vectors u,v and any X, (X.u)v=(X.v)u. Contracting with X in (2) gives

    S grad k=eta k grad S.                        (4)

Where S!=0, it follows directly that grad(k|S|^(-eta))=0. Where k!=0, grad(S|k|^(-q))=0. Thus each connected component G of B intersect {k!=0} has a single finite constant D_G with

    S=D_G|k|^q.                                  (5)

If x is not in Z, k(x)=0 and S(x)!=0, a small ball with S!=0 would have k|S|^(-eta) identically zero, forcing x into Z. Therefore k=0 implies S=0 at every point of B outside Z, including boundary Z.

When B is disjoint from closure Z, {S!=0} is contained in {k!=0}. Each component of B intersect {S<0} is exactly one component G in (5) with D_G<0. To see both inclusions, a connected negative-S component is in a single nonzero-k component, and (5) keeps all of that component negative. At an interior boundary point of such a G, continuity and local openness of {k!=0} force k=0, hence S=W=0 by (3)-(4).

## 4. Bounded negative constants are impossible at a supported zero

Suppose V(x0)=W(x0)=S(x0)=0 and W!=0 is dense near x0. There is no full neighborhood and finite C0>=0 for which

    S>=-C0|k|^q.                                 (6)

Indeed |k|<=C_X|V| on a fixed compact ball, V(x0)=0 and q>2. Shrink the ball until C0 C_X^q |V|^(q-2)<=1/8. Then (6) implies S-S(x0)>=-|V|^2/8 and the local pressure lemma forces V=0 nearby, contradicting density. This argument only needs support membership after the lower bound is known; density is needed for the scalar constants elsewhere.

Now let x0 be a densely vortical zero of V outside closure Z. Equation (3) and Section3 give W(x0)=S(x0)=P2(x0)=0. If grad S(x0)!=0, a submersion chart makes the local negative-S set connected. It carries one negative constant D_G, so S>=-|D_G||k|^q on the whole chart, contradicting (6). Consequently grad S(x0)=grad P2(x0)=0.

On any open neighborhood N of x0 disjoint from closure Z and satisfying the density premise, (6) and Section3 imply that the negative constants D_G are nonempty and unbounded below. The boundaries of their domains in N lie in {k=S=W=0}. Infinitely many distinct such domains in N meet every smaller neighborhood N' of x0. In detail, a component in N' is contained in a component in N and inherits its constant. If only finitely many components in N met N', their finite constants would give a lower bound (6) on N', a contradiction. Merely observing that the components in N' are infinite without tracking their constants would not suffice for this conclusion.

## 5. A pointwise Poisson expansion with controlled first derivative

Let u in C1(B1) solve Delta u=f in distributions, with measurable |f(y)|<=M|y|^gamma, gamma>0 and 2+gamma not an integer. Put J0=floor(2+gamma). There are homogeneous harmonic polynomials Q_j of degrees j=0,...,J0 such that

    |u(h)-sum Q_j(h)|<=C|h|^(2+gamma),
    |grad u(h)-sum grad Q_j(h)|<=C|h|^(1+gamma).   (7)

Here Q0=u(0) and Q1=grad u(0).h. No global Holder estimate for f or derivatives of f is needed.

Write G(z)=-1/(4 pi |z|) and w(h)=integral_B1 G(h-y)f(y)dy. Boundedness of f gives w in C1 and Delta w=f. Thus u-w is harmonic. Its Taylor expansion has homogeneous harmonic parts and has value and gradient remainders O(r^(J0+1)), O(r^J0), respectively, which are within (7).

For w set r=|h| and split |y|<2r from its complement. On the near set, |f|<=C r^gamma and the integrals of |G| and |grad G| over |h-y|<3r are O(r^2) and O(r), giving the required remainders. On the far set, Taylor expand G(h-y) in h to degree J0. Its remainder is bounded by C r^(J0+1)|y|^(-J0-2). Integration against |f| gives

    C r^(J0+1) integral_(2r)^1 t^(gamma-J0)dt
                                      <=C r^(2+gamma).

The exponent gamma-J0 lies strictly between -2 and -1. Every coefficient integral of order j<=J0 converges absolutely at zero, since its radial bound is t^(gamma+1-j), integrable exactly for j<2+gamma. Restoring the omitted near coefficient integrals costs O(r^(2+gamma)). For the gradient, expand grad G to degree J0-1. The same argument gives remainder O(r^(1+gamma)) and polynomial equal to the gradient of the previous polynomial. For each fixed y!=0, every homogeneous Taylor part of G(h-y) is harmonic in h. Absolute coefficient convergence permits integration of this finite polynomial identity, so the resulting Q_j are harmonic. This proves (7).

The exclusion of integer 2+gamma matters: the displayed integral otherwise has a possible logarithmic remainder at the critical degree. We make no assertion at that endpoint.

## 6. Finitely many scalar sign sectors

Let sigma be C1 on a planar disk and suppose, uniformly in theta,

    sigma(r,theta)=r^j g(theta)+o(r^j),
    partial_theta sigma=r^j g'(theta)+o(r^j),      (8)

where g is C1 periodic and all its zeros are simple. It has finitely many zeros. Around each zero choose a small arc on which g' is bounded away from zero, and on the complement use a positive lower bound for |g|. For small r, (8) supplies exactly one zero on each selected arc and none elsewhere. The implicit function theorem for r>0 gives continuous graphs theta_i(r). The intervening sets theta_i(r)<theta<theta_(i+1)(r) are connected, parametrized by (r,t) with 0<t<1. Their signs alternate. If g has no zeros, sigma has its constant sign on the punctured disk, which is connected.

This proves an exact finite sign-sector count, not just a bound along individual circles. For a homogeneous nonzero planar harmonic polynomial of degree j>=1, g is a nonzero sine-cosine of frequency j and has exactly 2j simple zeros.

At x0 let E=X(x0)^perp and use the smooth chart

    Phi(s,xi)=exp(sA)(x0+xi), xi in E.            (9)

Its derivative at (0,0) sends (s,xi) to sX(x0)+xi and is invertible. In a product neighborhood it is a diffeomorphism. Since S(Phi(s,xi))=exp(-bs)S(x0+xi), planar sign sectors on the transverse disk lift to exactly the full local sign components. Their complement has empty interior. This chart uses only the smooth linear carrier X and does not require a differentiable vorticity flow.

## 7. Pressure orders outside closure Z

Retain the hypotheses of Section4 at x0, and assume in addition

    |DV(x0+h)|<=C |h|^(gamma/2),                 (10)

where gamma>0 is not an integer. Apply (7) to P2, since |Delta P2|<=|DV|^2<=C|h|^gamma. The value and linear terms vanish by Section4. Suppose Q_j is the first nonzero term, so 2<=j<=J0<2+gamma. In the homogeneity identity

    (X(x0)+Ah).grad P2(x0+h)+bP2(x0+h)=0,

the only possible term of degree j-1 is X(x0).grad Q_j. The controlled gradient remainder has strictly higher order. Hence X(x0).grad Q_j=0. The polynomial Q_j is therefore a nonzero planar harmonic polynomial on E, constant in the X(x0) direction.

Integrating (10) from x0 gives V=O(|h|^(1+gamma/2)), and

    |V|^2=O(|h|^(2+gamma)),
    grad(|V|^2/2)=O(|h|^(1+gamma)).

Thus sigma(xi)=S(x0+xi) has leading term Q_j|E with the first-derivative control in (8). Sections3 and6 yield finitely many negative-S components, each with a finite constant D_G. This gives the forbidden bound (6). All Q_j must consequently vanish, proving

    |P2|+|h||grad P2|+|S|+|h||grad S|
                                       <=C|h|^(2+gamma).     (11)

At a flat velocity zero, local C^(1,alpha) regularity supplies (10) for gamma=2alpha and every alpha<1, excluding alpha=1/2 if the noninteger statement is used. This proves every order below four, including D2P2(x0)=0 and o(|h|^3), without claiming a C3 pressure neighborhood.

## 8. Submitted boundary and nonflat alternatives

For a densely vortical x0 in boundary Z, A973 gives V=DV=W=0, and Section3 gives S=P2=0. On every connected nonzero-S component the number k|S|^(-eta) is constant. Such a component either lies in Z (constant zero) or is disjoint from closure Z (constant nonzero).

If grad S(x0)!=0, the two sign sides are connected. At least one is in Z because x0 is a boundary point. Both cannot be in Z by continuity. The negative side cannot be the nonzero-constant side, since its single negative constant gives (6). Hence the submitted C46(e1) follows conditionally: the negative side is precisely Z locally, the positive side has k=C_+ S^eta with C_+!=0, and the boundary is the regular S=0 surface. Section9 below shows that this alternative actually has empty hypotheses.

If grad S(x0)=0 and a nonzero quadratic or cubic harmonic pressure term is first, the same expansion and transverse reduction give finitely many sign sectors. Some negative sector lies in Z, or (6) would hold; some sector is outside closure Z, or all of the neighborhood would have k=0. This proves the submitted C46(e2), again as a conditional alternative. Section9 also excludes its nonzero leading term.

For completeness the submitted C46(f) computation is correct. At a nonflat V zero outside closure Z, write M=DV(x0). Then M is symmetric, trace free, annihilates X0 and has eigenvalues 0,mu,-mu, mu>0. With H_P=D2P2(x0), the pointwise derivative of grad S is H_S=H_P-M^2. Homogeneity and grad P2=0 give H_P X0=H_S X0=0. On E, tr H_P=-2mu^2 and tr H_S=-4mu^2. If H_S were negative definite or indefinite, its leading quadratic on E would have respectively no angular zeros or four simple zeros. The sector argument and (6) exclude both. Thus H_S has eigenvalues 0,-4mu^2 on E, and H_P has eigenvalues mu^2,-3mu^2. Section10 independently excludes the nonflat case altogether under these hypotheses.

## 9. Stronger boundary conclusion from C1 regularity of k

The following elementary strengthening is useful. Suppose x0 is densely vortical, k(x0)=0 and S(x0)=0, and the transverse scalar S has a finite leading homogeneous term of degree j<q with simple angular zeros, including the nonzero linear case. Each connected sign sector has

    k=C_sector |S|^(1/q).                         (12)

Choose a fixed transverse ray strictly inside the limiting angular sector. Along it |S(x0+r e)| is comparable to r^j and the ray lies in that sector for all sufficiently small r. But k in C1 and k(x0)=0 give |k(x0+r e)|<=C r. If C_sector!=0, (12) contradicts this as r tends to zero, because j/q<1. Hence every sector constant is zero. Their union is dense in a full neighborhood by (9), so continuity gives k=0 throughout it. Thus x0 belongs to Z.

Apply this to a densely vortical boundary point. If grad S!=0, the restriction to E has a nonzero linear term, since X0.grad S=-bS=0. It has two simple angular zeros, so the preceding argument contradicts x0 not in Z. Thus grad S=grad P2=0 there. Use (7) with 1<gamma<2 at the flat velocity zero. Any first nonzero Q2 or Q3 reduces to a planar harmonic polynomial as in Section7, has simple angular zeros and degree j<q. The same argument again forces x0 into Z. Hence both terms vanish.

It follows that every densely vortical boundary point has the full conclusion (1). The provisional regular-boundary and finite-pressure-jet alternatives of C46(e1)-(e2) are vacuous. This proof uses no global nodal hypothesis N and no extra smoothness of the actual tail.

## 10. Stronger nonflat exclusion from the exact k saddle

At a densely vortical V zero outside closure Z, condition (3) holds locally. If DV(x0)!=0, the already confirmed local theorem A832 gives C1 transverse coordinates (u,v) such that

    c0|uv|<=|k(u,v)|<=C0|uv|                     (13)

for positive finite c0,C0. There are exactly four nonzero-k sectors and no extra nodal curve. The proof uses the C^(1,alpha) angular velocity one-form, its hyperbolic saddle, stable/unstable graphs, the transport C.k=k div C, and a uniform passage estimate; it does not presume a C2 k function.

Shrink to the product chart along X. Homogeneity preserves k=0 and its sign, so (13) gives exactly four local three-dimensional nodal domains. Density extends (5) to all four. With their finitely many constants and S=0 on the nodal set by Section3, one has |S|<=C|k|^q on a full neighborhood. This contradicts Section4. Therefore DV(x0)=0.

Together with Section7 this proves (1) outside closure Z. Section9 proves it on boundary Z. These two disjoint regions exhaust D minus Z, since Z is open. This proves the theorem stated in Section1. The nonflat pressure-Hessian configuration in C46(f) has empty hypotheses in the actual dense class, although its conditional algebra is valid.

## 11. Scope corrections for team summaries

LIT197/A1005 gives differentiability of W at every zero, with

    DW(x0)=DXi(y0) D(curl U)(y0) DXi(y0)^(-1),
    y0=Xi^(-1)(x0).

It gives DW=D(curl U)=0 at V zeros only outside closure Z, not at every T0 point. The general statement in coordinator Note76 assigning DOmega=0 at an arbitrary T0 point is not licensed by that theorem. On an open k=0 neighborhood at a flat zero, differentiation gives only

    X0 cross DW=0, DW X0=0,
    DW=X0 tensor ell, ell(X0)=0.

A rank-one nilpotent derivative is algebraically allowed. This is an algebraic possibility, not an actual profile construction. Neither density alone nor the new pressure orders prove vanishing of that derivative inside Z.

Likewise the instruction that excluding index +1 at each isolated T0 zero would by itself close a Poincare-Hopf count is incomplete: index +2 or larger would remain, and isolation of all zeros must be justified. A nonpositive index bound together with isolation gives the needed contradiction. LIT205 supplies one conditional such bound with explicit extra finite-jet hypotheses; it does not cover all actual T0 points.

C46's heuristic spherical-average discussion is an obstruction comparison, not a new existence or impossibility theorem. A local steady swirl can test the Poisson and deficit argument but fails the negative homogeneity of an actual tail. Therefore that example cannot establish consistency of the entire leading-tail system at a T0 point. The region inside Z, accumulation of open irrotational patches, and unbounded constants in infinitely many nodal domains remain open. No conclusion reaches the original bare-decay arbitrary-helicity conjecture.

## 12. Verification and model comparison

All ten source sections of C46 were read. Its pointwise Poisson expansion was reconstructed by splitting the Newtonian kernel, including derivative remainders and the integer exclusion. The sign-sector argument was checked as a connected-component statement in a genuine product chart. The complete A832 independent proof was reread, including its C1 coordinate and uniform-passage estimates. No numerical experiment or formal build was used.

The existing Theory Agent C agent is configured with the primary model; provider runtime is not independently attested. The received LIT206 preparatory comparison agrees on the C46 core and proposes exactly the strengthenings proved in Sections9-10. Its full submitted proof, if subsequently supplied, must be compared before its own source is promoted. The analysis here does not count the preparatory note as a completed separate theorem audit. Feedback is transmitted through the agent notes; no new client, agent or remote compute is invoked.

## 13. Dependencies

- Primary C46 source: in the team records; exact snapshot in the team records.
- Focused preparatory comparison: in the team records; exact snapshot in the team records.
- A832: in the team records, especially Section2, read again in full.
- A963, A973 and the actual-tail scope: in the team records and in the team records.
- A1005-A1008 and the exact local pressure lemma: in the team records.
- Explicit elementary dependencies: local elliptic regularity, Weyl's lemma, Newtonian potential and kernel derivatives, implicit/inverse function theorems, and the already confirmed local stable-manifold passage theorem used only through A832.

Source hashes and the full post-read record are retained.

## 14. Full LIT206 source comparison

The complete nine-section LIT206 manuscript, in the team records in the literature agent, has now been read and checked. Its exact class is the global helicity-free C^2/C^1 profile class with both natural bounds, 2/5<c<1/2 and every finite omega. Its local premise is that V(x0)=0, x0 is outside Z itself, and W!=0 is dense on some full ball about x0. Its conclusions agree with Sections 1-13 above: V=DV=W=0, pressure and scalar values and first and second pointwise derivatives vanish, and for every 0<beta<4,

    |P2|+|S|+r(|grad P2|+|grad S|)<=C_beta r^beta

near x0. This includes a zero cubic Peano polynomial, without a C^3-neighborhood assertion. The separate derivative-of-vorticity conclusion is correctly limited in LIT206 to points outside closure Z. The extension under N is proved separately in A1109, not supplied by density alone.

There is an additional valid shortcut in LIT206 Section 3. At a supposed nonflat zero outside closure Z, set M=DV(x0). The exact four-sector theorem gives one finite scalar ratio on each sector, and continuity gives |S|<=C|k|^q on a full neighborhood. Since k is C^1, k(x0)=0 and q>2, this implies S=o(r^2). With P2(x0)=0, V(x0)=0 and H=D^2P2(x0), the expansion

    S(x0+h)=grad P2(x0).h
              +(h.Hh-|Mh|^2)/2+o(|h|^2)

forces grad P2(x0)=0 and H=M^T M. Here M is symmetric because W(x0)=0. The pressure equation also gives tr H=-tr(M^2)=-|M|^2, whereas H=M^TM gives tr H=|M|^2. Thus M=0, a contradiction. This establishes the same nonflat exclusion without the full-ball pressure lemma used in Section 10 above. It still requires the complete four-sector theorem, including exclusion of additional zero curves; an eigenvalue calculation alone does not provide that premise.

The regular scalar-zero step in LIT206 applies directly at every point outside Z: the two connected sides S>0 and S<0 have k=C_+ S^(1/q) and k=C_- |S|^(1/q). A transverse line and k=O(r), S comparable to r force both constants to vanish. This agrees with the separate outside-closure and boundary treatments above. The pointwise Newtonian remainder, angular simple-zero argument, finite connected flow-box sectors and power-versus-C^1 contradiction in Sections 5-7 also match the independently checked calculations here.

The full LIT206 statement is therefore confirmed. No conclusion is added at points inside Z or where open irrotational patches accumulate in every neighborhood. Actual-tail smoothness or a nonexistence theorem is not inferred from pressure flatness through order three.
