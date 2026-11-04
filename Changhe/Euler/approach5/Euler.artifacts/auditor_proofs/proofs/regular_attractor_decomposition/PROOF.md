# Regular backward limits and basic hyperbolic attractors

## Statement and hypotheses

Let 0<c<1/2 and let omega be any finite real number. Let U,P be C2 on R3, with div U=0, U(y)=o(|y|) uniformly, satisfying

    (1-c)U + ((cI-omega J)y+U).grad U + omega JU + grad P = 0.

Here J(x,y,z)=(-y,x,0), B=(cI-omega J)y+U, Omega=curl U, Phi is the flow of B, and Psi_t=Phi_-t. Put b=1+c, a=1-2c, and

    Reg = {y : B(y) x Omega(y) != 0},
    V = {y : alpha_Phi(y) is contained in Reg}.

There are at most countably many distinct basic hyperbolic attractors A of Psi contained in Reg. Their basins

    Bas(A) = {y : dist(Psi_t y,A) tends to zero as t tends to infinity}

are nonempty, open and pairwise disjoint. Their union covers V up to a Lebesgue-null set. Here a basic attractor is compact, invariant under the full flow, nonsingular, hyperbolic, locally maximal, topologically transitive, with dense periodic orbits and a trapping neighborhood. It contains the full strong unstable manifold of each of its points.

Each such A has backward topological entropy a, with a unique maximizing FLOW-invariant probability. That probability is physical for continuous-time averages; its generic points fill Bas(A) up to a null set. Every periodic orbit, oriented by B and with period T, satisfies

    transverse multipliers = exp(bT), exp(-aT),
    integral_gamma U.dl = 0,
    integral_0^T |B(Phi_t x)|^2 dt = -2 omega A_xy(gamma).

A_xy is the signed area of the horizontal projection, counted with winding. In particular no such attractor exists when omega=0.

In addition, Bas(A) is exactly the union of all complete Omega-orbits meeting A. B, Omega and B x Omega have no zeros in Bas(A). The basin has infinite volume. If U is bounded, it has positive lower volume density in every sufficiently large shell {rho<|y|<C rho}, for each fixed C>1. The attractor itself has volume zero.

These conclusions refine the regular case only. They do not exclude alpha-limit sets meeting B=0 or Omega=0 and do not prove the main nonexistence conjecture.

## Dependencies and their exact use

A006 supplies complete B flow, compact backward limits and a large strictly inward ball for Psi. A048 supplies complete Omega flow. A056 supplies uniform hyperbolicity on every compact invariant subset of Reg, with backward strong stable line R Omega and rate -b, backward unstable rate a, and neutral flow line R B. A091 supplies a full backward weak unstable leaf in the maximal invariant part of a compact regular set with a positive-volume survivor set. Its source is the inspected Alves-Pinheiro Theorem A, with the neutral flow line retained in the center-stable bundle. A085 supplies the entropy and full-basin continuous-time physicality statement once BASIC has been established. A028 and A004 supply periodic multipliers and circulation. A092 supplies the large-shell density conclusion for bounded U.

The standard strong unstable manifold theorem for a nonsingular compact hyperbolic flow set is used with continuous C1 dependence of its local plaques. This is the same geometric input used in A091 and A110. For completeness the needed closing argument is described below, including why its periodic orbit belongs to the locally maximal set. No spectral decomposition for a time-one flow map is used, and no neutral direction is treated as contracting.

## 1. Smooth stable saturation

Write psi_tau for the complete Omega flow. The Cauchy identity gives the exact conjugacy

    Psi_t psi_tau x = psi_(exp(-bt) tau) Psi_t x.

Indeed both sides, viewed as functions of tau, solve the Omega flow equation at speed exp(-bt), with the same initial point. For a compact Omega segment through x, choose a large closed ball D which contains that segment and is forward invariant for Psi. Its image segment stays in D, and hence

    |Psi_t psi_tau x - Psi_t x|
      <= sup_D |Omega| |tau| exp(-bt),   t>=0.

Let K be a compact invariant subset of Reg. Suppose G is a nonempty compact invariant subset of K containing the full strong unstable leaf of each point. It also contains the weak unstable leaf, obtained by applying all flow times to the strong leaf.

At x in G choose a C1 parametrization gamma of its local strong unstable curve. The map

    (s,r,tau) -> psi_tau(Psi_s gamma(r))

is C1. At zero its three derivative columns are -B(x), gamma'(0) and Omega(x), which are independent by hyperbolicity. The inverse function theorem produces an open neighborhood O_x of x whose points are Omega shifts, of bounded parameter, of points in G. A finite collection covers G. Enlarge D to contain all the finitely many compact Omega segments used. The displayed estimate now gives an open neighborhood O of G and a constant C0 such that

    dist(Psi_t z,G) <= C0 exp(-bt),   z in O, t>=0.

Choose r>0 so that the closure of N={dist(z,G)<r} lies in O. For sufficiently large T,

    Psi_t closure(N) is contained in N,  t>=T.

The intersection of all Psi_t closure(N), t>=0, is exactly G: one inclusion follows from invariance; the other follows from the uniform distance estimate. If preferred, choose the discrete nested intersection at multiples of T. Any complete orbit contained in N lies in G, by applying the estimate to its starting point at time -t. Thus G is locally maximal. The union of backward images of N is its open basin. This proves the attracting property without a prior local-maximality assumption.

## 2. Minimal unstable saturation gives transitivity

The closure of a weak unstable leaf contained in K is compact, invariant and unstable saturated. To see saturation, approximate a point in the closure by points on that leaf; their fixed-size local unstable plaques belong to the same leaf and converge in C1 to the plaque at the limiting point. Invariance then gives the full unstable leaf.

In a nonempty compact unstable-saturated G, take the family of all nonempty compact invariant unstable-saturated subsets. Every nested chain has a nonempty compact intersection. Its plaques remain in the intersection, so it is unstable saturated. Zorn's lemma gives a minimal member A. For every x in A, the preceding closure construction and minimality give

    closure(W^wu(x)) = A.

Section 1 makes A an attracting and locally maximal hyperbolic set.

We verify positive-time transitivity; density of entire weak leaves by itself would not be sufficient. Let V1,V2 be open sets meeting A. For each y in A, density of W^wu(y) gives an integer n_y>=0 and a real s_y such that

    Psi_(s_y+n_y) W^u_epsilon(Psi_-n_y y)

meets V2. Continuous dependence gives the same assertion for all y' in a relative neighborhood O_y of y. Take a finite subcover, with associated n_i,s_i. Choose x in V1 intersect A and a small local unstable interval I through x, contained in V1 intersect A. Uniform unstable expansion gives t0 such that

    W^u_epsilon(Psi_t x) is contained in Psi_t I,  t>=t0.

Choose t so large that t-n_i>=t0 and t+s_i>=T0 for every i, where T0 is arbitrary. Select i with Psi_t x in O_i. The plaque whose image meets V2 is contained, after the indicated flow time, in Psi_(t+s_i) I. Thus Psi_(t+s_i)(V1 intersect A) meets V2 at a time at least T0.

The usual Baire construction is elementary here. For every member O_j of a countable relative base and integer m, the set of x in A whose orbit meets O_j at some t>=m is relatively open and dense by the preceding paragraph. Their countable intersection is residual and consists of points whose forward limit set is all of A. Taking V1=V2 also shows that every point of A is nonwandering for the restricted flow.

## 3. Closing and density of periodic orbits

The needed local closing fact is the following: on a nonsingular compact hyperbolic flow set K, a sufficiently close return Phi_T x to x, T sufficiently large, is shadowed by a periodic orbit in an arbitrarily prescribed neighborhood of K. If K is locally maximal, that orbit is in K.

Here is the contraction mechanism for this version. Take small two-dimensional transverse disks along the orbit segment. In an adapted norm, divide time into pieces in [t0,2t0], with t0 fixed large enough that the linear Poincare maps contract the stable line and their inverses contract the unstable line by a common number kappa<1. These line bundles are uniformly transverse on K. Flow-box coordinates and compactness make the nonlinear remainders uniformly C1-small on sufficiently small transverse disks. The final disk is slid along the flow to the initial disk. For a close return this identification is C1-close to the corresponding hyperbolic identification, because the flow is nonsingular and the invariant bundles are continuous. Its translation error tends to zero with the return distance.

More explicitly, in the transverse stable/unstable coordinates the finite cyclic system has the form

    v_(i+1) = A_i v_i + R_i(v_i) + e_i,  i modulo n.

Choose A_i block diagonal on the one-dimensional stable/unstable coordinates; absorb the small final identification error into R_i. The stable factors have norm at most kappa and the unstable inverse factors have norm at most kappa. The cyclic linear operator L(v)_i=v_(i+1)-A_i v_i has an inverse with norm bounded independently of n. This follows by summing the stable equation forwards and the unstable equation backwards: the geometric series bounds are at most 1/(1-kappa), up to the fixed norm equivalence for the splitting. Cyclicity is harmless, since one full product contracts in the relevant summation direction; summing the corresponding geometric series over cycles gives the same bound. Call the resulting common inverse bound C1.

Shrink the transverse radius until every R_i has Lipschitz constant less than 1/(2C1). Then choose the return distance so small that C1 sup|e_i| is less than half this radius. The map

    v -> L^-1(R(v)+e)

is a contraction of the closed product ball in the maximum norm. Its fixed point is a cyclic sequence of local Poincare transitions. Their positive flow times give a periodic orbit; all intermediate flow segments remain as close to K as desired, by the uniform flow-box bounds. This proves the stated closing fact. It uses the transverse hyperbolic directions only, not a fictitious contraction in flow time.

For any point of A and any neighborhood of it, nonwandering supplies a sufficiently long close return with both endpoints in a still smaller neighborhood. Apply closing with the shadowing neighborhood inside the isolating neighborhood N from Section 1. The resulting periodic orbit remains in N for all times and therefore belongs to A. Periodic orbits are dense. A contains a two-dimensional weak unstable disk, so it is not one periodic orbit. All the BASIC hypotheses needed in A085 have now been checked.

The published monograph Fisher-Hasselblatt, Hyperbolic Flows (2019), Chapters 5-6, is a conventional reference for these hyperbolic-flow facts. Only its public contents page was retrieved in this audit; its subscription chapter text was not inspected. No exact theorem number from that monograph is asserted here. The contraction argument above is the verification used for closing.

## 4. Disjointness and countability

Let A1,A2 be basic attracting sets as above. If z belongs to both basins, its nonempty forward limit set for Psi lies in A1 intersect A2. Thus A2 meets the open basin of A1. Take a point of A2 whose forward limit is all of A2, as supplied by transitivity and Baire. Its forward orbit meets that open basin and stays in it thereafter. Its limit set A2 is contained in A1. Interchanging the sets proves equality. Distinct basins are therefore disjoint. Each contains an ambient open ball and hence a point with rational coordinates, so the family is countable.

## 5. Almost-everywhere exhaustion of regular limits

Fix a sufficiently large closed absorbing ball D for Psi. For positive integers k,m set

    R_k = {x in D : |Omega(x)|>=1/k, |B(x)xOmega(x)|>=1/k},
    T_(k,m) = {x : Psi_t x in R_k for all t>=m}.

Each T_(k,m) is closed. Compactness of backward limit sets, their distance convergence, and strict absorption into D show

    V = union_(k,m) T_(k,m).

Let V' be V with all the basic-attractor basins removed. This is a Borel, full-flow-invariant set. Suppose it has positive measure. For some k,m, choose a compact positive-measure E1 contained in V' intersect T_(k,m). Let E0=Psi_m E1, still compact and positive measure. Put

    C = closure(union_(t>=0) Psi_t E0).

It is a compact forward-invariant subset of R_k with positive measure. A091 applies to its survivor set and gives a full weak unstable leaf in the maximal full-invariant subset K_C of C. Its closure G is nonempty, compact, invariant and unstable saturated. Sections 1-3 give a basic attractor A contained in G and hence in C.

The open basin Bas(A) meets C, since it contains A. By the definition of C it therefore contains a point Psi_t e with e in E0. Basin invariance gives e in Bas(A), contrary to E0 being contained in V'. This contradiction proves that V' is null. Notice that C itself need not remain in V'; using its closure is valid precisely because the basin is open.

## 6. Geometry and periodic restrictions

If z lies in Bas(A), it eventually enters O from Section 1. There Psi_t z=psi_tau w for some w in A. Conjugating backwards gives

    z = psi_(exp(bt) tau)(Phi_t w),

so z lies on an Omega-orbit meeting A. Conversely the exponential estimate in Section 1 puts every finite Omega shift of any w in A in Bas(A). Completeness supplies the whole Omega-orbit. This proves the exact basin description.

The three zero sets B=0, Omega=0 and B x Omega=0 are closed and invariant under Phi. A point in one of them has its backward limit there, and therefore cannot lie in Bas(A). Positive divergence of B multiplies volume by exp(3ct). An invariant open basin consequently cannot have finite positive volume; it has infinite volume. For bounded U, A092 gives the stated shell-density bound. Invariance and finite volume of the compact A give |A|=exp(3ct)|A|, hence |A|=0.

Finally A085 applies to each A with all hypotheses now established. Its unique maximizing measure is a flow measure, not a claim of uniqueness among every time-one invariant measure. Periodic multiplier and circulation identities give the displayed restrictions. Since integral_gamma cy.dl=0 and B=cy+U-omega Jy,

    integral_gamma B.dl = -omega integral_gamma Jy.dl = -2 omega A_xy.

The left side is the positive integral of |B|^2 over a nonstationary B-periodic orbit. This proves the orientation assertion and the omega=0 exclusion.

## Audit scope

This verifies coordinator CO9 and Corollary 12.6. In the submitted inverse-function calculation, the column for Psi_s is -B rather than B; its sign does not affect invertibility. In the exhaustion argument the absorbing ball must be fixed large enough for all orbits eventually to enter it, as above. Neither detail changes the result. The general main theorem is still OPEN, since existence of these regular attractors has not been excluded and the singular/irrotational alternatives remain.

## Additional restriction: no compact regular invariant set contains a stable-sheet plaque

Let L be a compact full-Phi-invariant subset of Reg. It cannot contain any nonempty plaque

    Pi(z)={Phi_s psi_tau z : |s|,|tau|<eta}

of the two-dimensional foliation span(B,Omega). This plaque is a local center-unstable plaque for Phi. Saturate a sufficiently small portion by the local strong stable curves of Phi. These curves vary continuously and meet the plaque only once in a sufficiently small product box. Their parametrization gives a continuous injective map from an open three-dimensional box. Invariance of domain makes its image open. Every point of that image has bounded forward orbit, by exponential tracking of L. This contradicts the nullity of the compact forward-bounded core from A006. Thus L cannot contain Pi(z).

If A is one of the basic backward attractors and z in Bas(A), choose eta so that closure(Pi(z)) is compactly contained in Bas(A). Its negative-Phi-time orbit converges uniformly in distance to A. To justify uniformity, each point eventually enters the strictly trapped neighborhood from Section 1; continuity and a finite cover make the entrance times uniformly bounded, after which the local exponential estimate applies. If the positive-Phi-time orbit closure of Pi(z) were a compact subset of Reg, adjoining the negative-time part and A would therefore give a compact full-invariant subset of Reg containing Pi(z), a contradiction.

In particular, let p in A lie on a B-periodic orbit of period T. Its complete Omega line l(p) satisfies Phi_T l(p)=l(p), since its Omega parameter is multiplied by exp(bT). If C=closure(l(p)) were compact and contained in Reg, then

    L=union_(0<=s<=T) Phi_s C

would be compact, full-Phi-invariant and contained in Reg. It would contain the required plaque. Hence l(p) is either unbounded or its closure meets the complement of Reg. This is coordinator Lemma 12.7, added after the original CO9 audit. The assertion does not rule out a recurrent unbounded Omega line, or a bounded line whose closure reaches a zero set.
