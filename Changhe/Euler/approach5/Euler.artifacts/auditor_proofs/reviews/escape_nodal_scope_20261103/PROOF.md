# Escaping endpoints and the local nodal premise

Status: CONFIRMED for the corrected implications below. The latest W1 saddle application is invalid and the W2 saddle application requires an additional local premise. These are audits of conditional configurations, not counterexamples to the global conjecture.

## 1. Exact hypotheses and notation

Fix 2/5<c<1/2, omega in R, Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, kappa=1+c and p=(1-c)/c. Suppose U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

Let B=Ax+U, Omega=curl U. Let Xi:E->D, D=R3 minus{0}, be the actual C1 scattering diffeomorphism on the escaping set, with D Xi Omega=W composed with Xi, where V is the actual velocity tail and W=curl V. Set X(x)=Ax, k=X.V, K=k restricted to S2, G=W restricted to S2,

    A0=int_S2{K=0},
    Tflat={w:V(w)=0,DV(w)=0} intersect supp_S2 G,
    Y(w)=G(w)-(w.G(w)/c)Aw.

For an angular open set O the local nodal premise N means {k=0} subset {W=0} on its twisted cone. Define M(O,tau)=integral_(O intersect {|K|<tau})|G|dA. The confirmed local saddle estimate A832 requires N on a neighborhood, not merely W=0 at one point. A963 says every vortical k-zero is interior; A973 gives boundary A0 subset Tflat.

Consider the two escaping lower-window witness types of A972: W1 is a vortex half-line through a vortical carrier equilibrium, with B=kappa tau Omega and nonzero initial vortex parameter tau0; W2 is an irrotational trace in the closure of {Omega!=0} from a flat periodic witness. Both have constant Bernoulli value and covector rate rho<=-2a. These are extra conditional configurations. Put v=Xi(y0), s=log|v|/c and w=exp(-sA)v in S2.

## 2. W1 is helical and lies inside the open scalar-zero region

A602/A972 give

    V(w)=0,
    G(w)=Cw Aw, Cw=|v|^(1+1/c)/(kappa tau0)!=0,
    G_r(w)=w.G(w)=c Cw!=0, Y(w)=0.

The correct direction of G is Aw=cw-omega Jw. It is parallel to the Euclidean radial vector w only when omega Jw=0. In general the corresponding twisted ray is a logarithmic spiral. Projected angular stationarity Y(w)=0 does not remove this rotation.

Since V(w)=0, K(w)=0; since G(w)!=0, A963 gives w in A0. Thus N fails at w itself and cannot hold on any neighborhood of w. In particular A832/CO45(a) cannot classify this W1 endpoint as a saddle or give o(tau) mass there. Its curl is nonzero, so DV(w)!=0, but DV is not symmetric; the irrotational-zero linear algebra behind the saddle lemma is unavailable.

More quantitatively, choose a sufficiently small angular disk O containing w, with closure in A0 and |G|>=m>0 on O. For every tau>0,

    M(O,tau)=integral_O|G|dA>=m area(O)>0.

Thus this endpoint has positive mass on the exact zero set, and any assertion of M(O,tau)=O(tau^(1+alpha/2)) there is false under the stated conditional configuration. This does not show the configuration exists, or contradict an implication whose explicitly assumed N has an empty antecedent.

## 3. W2 is a supported common zero; the nonflat case still needs a local split

A830/A871/A972 give V(w)=W(w)=0. The closure hypothesis on the physical trace also gives w in supp G. Indeed y0 belongs to E, an open set, and is the limit of vortical points y_n in E. Their images Xi(y_n) converge to v; invertibility of D Xi gives W(Xi(y_n))!=0. Hence v is in supp_D W. Twisted homogeneity transfers this support property to w on S2.

If DV(w)=0, it follows that w belongs to Tflat. If DV(w)!=0, A973 implies w is not in boundary A0. There are then two possibilities:

* w belongs to A0, and K vanishes on an angular neighborhood of w;
* w lies outside closure A0, and some angular neighborhood O is disjoint from A0.

In the second case A963 implies N on O: a vortical zero in O would be an interior zero and thus lie in A0. The nonflat common zero is then covered by the local saddle theorem A832, with its o(tau) estimate. In the first case that theorem has not been justified. Since w is in supp G and A0 is open, every sufficiently small disk about w contains a smaller positive-area disk on which K=0 and |G|>0. Consequently its zero-set mass is positive, and it cannot have an o(tau) estimate. Nonflatness at w alone does not distinguish these two cases.

No claim that the first case is actually realized by a global Euler profile is made. The point is that the cited saddle proof does not exclude it and cannot be invoked without N.

## 4. Verdict and source comparison

The Theory Agent B note dated 12:21Z calls the W1 tail vorticity radial and invokes N near its endpoint. The radial formula requires the qualification omega Jw=0; at arbitrary rotation the exact formula is G=(G_r/c)Aw. The hypothetical N case at this W1 endpoint is empty, so its ensuing unconditional saddle/concentration narrative is unsupported. The W2 assertion that every nonflat common zero carries no concentration omits the same local N premise. Section3 supplies a precise replacement using A973.

Dependencies are the exact A602/A972 escape formulas, A963, A973 and the A832 local saddle estimate. The actual scattering diffeomorphism supplies the W2 support statement. Completeness and pressure normalization are inherited from these independently checked actual-profile theorems. No boundary integral or new pressure equation is used.

The source is from the existing configured model Theory Agent B agent; provider runtime is not independently attested. Corrections are communicated through this agent's own files. No new client, numerical computation or formal build was used.
