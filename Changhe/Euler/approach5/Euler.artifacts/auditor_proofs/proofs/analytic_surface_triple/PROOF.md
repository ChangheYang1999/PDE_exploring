# A smooth exact surface triple for every ratio greater than one

## Statement and scope

Let K=(3+sqrt(5))/2, let r>1, and set a=K^(-r). There exist a smooth torus M, an orientation-preserving smooth diffeomorphism F of M, a smoothly embedded closed disc D, and smooth tensors Y and eta on M with the following properties. Put S=M\int(D) and f=F|S.

1. F^(-1)(D) is compactly contained in int(D), so f embeds S into int(S).
2. Y and eta are nowhere zero, d eta=0, eta(Y)=0, and on all of S,
   f*eta=K eta and Df(Y)=a Y composed with f.
3. Lambda=intersection over n>=0 of f^n(S) is a nontrivial transitive hyperbolic attractor. Its stable and unstable dimensions are one each; its local unstable arcs belong to Lambda. It has local product structure Cantor set times interval.
4. F acts on integral first homology by A=[[2,1],[1,1]], after choosing a basis. The complementary open disc M\Lambda is the backward basin of one hyperbolic source p in int(D), and intersection F^(-n)(D)={p}.

This is a kinematic surface construction. It supplies neither a three-dimensional Euclidean curl relation nor an Euler profile. It uses no numerical inequality or computer certificate. The proof below independently checks the team construction; its relative source link is listed under Dependencies.

## 1. The smooth shear torus

Choose eigen-coordinates (u,s) for A, so A(u,s)=(Ku,s/K). Let L be the image of the integer lattice. Write gamma=(U_gamma,S_gamma). Each coordinate projection of L is injective and dense; AL=L.

Define chi(t)=exp(-1/(1-t^2)) for |t|<1, and zero otherwise. Let

    w(t)=(t^2+chi(t))^(-r/2),    d(t)=w(Kt)-a w(t).

The function w is positive and smooth. For |t|>=1 it equals |t|^(-r), and its j-th derivative is O(|t|^(-r-j)). The function d is smooth, supported in [-1,1], and strictly positive on (-1,1). Indeed chi(Kt)<=chi(t)<K^2 chi(t) there, and the negative power reverses the resulting strict denominator inequality.

For each u, define the measure

    m_u=sum over gamma in L of w(u-U_gamma) delta_(S_gamma).

On every bounded s-interval this series, and every series of u-derivatives, converges absolutely and locally uniformly in u. A translate of a fixed bounded rectangle contains uniformly finitely many lattice points. Summing over unit U-strips therefore reduces the assertion to sum (1+|n|)^(-r)<infinity. This is where r>1 is used.

The measure has full support. It also has infinite mass on each half-line: a lattice covering-radius argument supplies infinitely many distinct lattice points with bounded |u-U_gamma| and separated positive, or negative, stable coordinates. Each has a uniformly positive weight.

Use the left-continuous cumulative function

    V(u,s)=m_u([0,s)) if s>0,
           0 if s=0,
           -m_u([s,0)) if s<0.

At S_gamma the jump is w(u-U_gamma); denote its closed jump interval by I_gamma(u), with lower endpoint l_gamma(u)=V(u,S_gamma). On an ordinary smooth (u,v)-plane let P collapse each I_gamma(u) to (u,S_gamma), and use the inverse cumulative value at the remaining points. Full support makes this inverse single-valued and continuous; the two infinite half-line masses make it globally defined. For joint continuity, bracket a stable value by fixed nearby cuts and use continuity of their cumulative functions in u. The same argument works at both ends of each jump.

The map P is proper. For bounded u and s, all corresponding jump endpoints and cumulative values are uniformly bounded by the local convergence estimate. Thus inverse images of compact sets are closed and bounded.

Translation of the measures gives

    V(u+U_gamma,s+S_gamma)=V(u,s)+H_gamma(u),
    H_gamma(u)=V(u+U_gamma,S_gamma).

Consequently T_gamma(u,v)=(u+U_gamma,v+H_gamma(u)) is a smooth lattice action and P T_gamma=P+gamma. The action is free because U_gamma=0 only for gamma=0. Properness of the ordinary lattice action and equivariance imply proper discontinuity. The inverse image of a closed ordinary fundamental parallelogram is compact and meets every orbit, so the quotient is compact. The quotient M is a connected oriented smooth surface with universal cover R^2 and fundamental group Z^2, hence a torus.

The shear transition maps preserve Y=partial_v, eta=du and nu=dv wedge du. In particular i_Y nu=eta. These tensors descend smoothly to M, with Y and eta nowhere zero.

The jump interiors project to one open embedded ribbon

    B={(t,z): t in R, 0<z<w(t)}.

It is an open disc. Injectivity follows because a deck map carrying the zero-stable-coordinate gap to itself must have S_gamma=0. Write C=M\B. The induced P maps C onto the old torus, with one preimage off the unstable leaf of zero and two preimages on that leaf.

## 2. A locally finite smooth formula

Take the smooth increasing transition Phi obtained by integrating and normalizing

    beta(q)=exp(-1/((q-1/4)(3/4-q))) on (1/4,3/4),

and putting beta=0 elsewhere. Thus Phi=0 below 1/4, Phi=1 above 3/4, Phi(1-q)=1-Phi(q), Phi(q)<q for 0<q<1/2, and Phi(q)>q for 1/2<q<1. Strict convexity on (1/4,1/2) gives Phi'(1/2)>2.

Define a lift by

    F_1(u,v)=Ku,
    F_2(u,v)=a v + sum_gamma d(u-U_gamma)
       [Phi((v-l_gamma(u))/w(u-U_gamma))-1_(S_gamma<0)].

This sum is locally finite. On a compact (u,v)-set, P_2(u,v) is bounded. A nonzero bracket confines S_gamma between that bounded set and zero, including the possible current gap. A nonzero d additionally requires |u-U_gamma|<1. There are only finitely many such lattice points. Thus F is smooth even on C; no differentiability of P is claimed or needed.

Moreover partial_v F_2>=a>0. At most one interpolation term has nonzero v-derivative at a given point. For fixed u, the second coordinate is increasing and onto R; with F_1=Ku this proves that the lift is a global smooth diffeomorphism.

At a non-atomic cumulative value or lower gap endpoint, direct summation gives

    F(u,V(u,s))=(Ku,V(Ku,s/K)).

At upper endpoints add the corresponding target jump. On the central ribbon the formula reduces to

    F(t,z)=(Kt, a z+d(t) Phi(z/w(t))).                 (1)

These formulas show F T_gamma=T_(A gamma) F, so F descends to M, acts by A on homology, and satisfies PF=AP, F(B)=B, F(C)=C, and F*eta=K eta. Furthermore DF(Y)=aY outside the compact ribbon subset

    N={|t|<=1, w(t)/4<=z<=3w(t)/4}.

## 3. A disc containing all failures of exact contraction

Choose 0<epsilon<(1/8) min_(|t|<=K) w(t), and set

    D0={|t|<=K, epsilon<=z<=w(t)-epsilon}.

If F(t,z) belongs to D0, then |t|<=1. Equation (1) gives F_2(t,epsilon)=a epsilon<epsilon and
F_2(t,w(t)-epsilon)=w(Kt)-a epsilon>w(Kt)-epsilon. Strict monotonicity implies F^(-1)(D0) is compactly contained in int(D0). Also N is compactly contained in int(D0).

In coordinates x=t/K and y=(z-w(t)/2)/(w(t)/2-epsilon), choose a sufficiently large integer m and put D={x^(2m)+y^(2m)<=1}. These smooth discs exhaust int(D0) from within in the sense of containing every compact subset for large m. Choose m so that both F^(-1)(D0) and N are in int(D). Then F^(-1)(D) is compactly contained in int(D). Restriction to S gives all exact tensor identities, including at its boundary.

## 4. The attractor and source

Certainly C is contained in Lambda. Every point of B has backward coordinates t_n=K^(-n)t_0 tending to zero. With q=z/w(t), equation (1) becomes

    q'=b(t)q+(1-b(t))Phi(q),
    b(t)=a w(t)/w(Kt) in (0,1].                       (2)

The middle line q=1/2 and its two sides are invariant. If a backward orbit never enters D0, then eventually it stays below epsilon or above w(t)-epsilon. In the lower case z_(n-1)=a z_n, forcing unbounded positive backward growth despite z_n<epsilon. In the upper case the same contradiction applies to w(t_n)-z_n. A middle-line point enters D0 once t_n is small. Thus every B point enters D0 and then int(D) backward, proving Lambda=C. Nested compactness proves attraction to C.

Equation (2) also proves convergence of every B backward orbit to p=(0,w(0)/2): in either half the normalized backward coordinate moves monotonically toward 1/2, and b(t_n) tends to a<1, so no other interior limit can satisfy Phi(q)=q. At p the two eigenvalues are K and a+(1-a)Phi'(1/2), both greater than one. Finally any point whose full forward orbit stays in D has t=0; equation (2) then forces q=1/2. Therefore intersection F^(-n)(D)={p}, with uniform shrinking by nested compactness.

## 5. Hyperbolicity and transitivity

At each non-atomic stable label s, the graph u -> (u,V(u,s)) lies in C. At an atomic label use its lower and upper endpoint graphs separately. Vertical C-sections are perfect and nowhere dense: one-sided cumulative convergence gives non-isolation, and nearby atomic labels give gap interiors in every neighborhood. Transport along these graphs gives a local product with a Cantor set. Joint continuity follows by bracketing with fixed stable cuts.

The graph tangents vary continuously on C. Their slopes are cumulative sums of w'(u-U_gamma); the corresponding signed measures have locally uniformly summable total variations. At an endpoint, convergence in C necessarily takes the appropriate side, since the open gap has positive width. These observations prove the required continuity also at endpoints.

Let X be the tangent vector normalized by eta(X)=1. Differentiation of the cumulative identities gives DF(X)=K X composed with F. Together with DF(Y)=a Y this is a hyperbolic splitting: compactness controls norms and the angle, and eta distinguishes the two directions. Graph arcs contract backward at rate K^(-1), so they are local unstable arcs and lie in C.

For transitivity, the old linear A is Haar ergodic. Indeed invariance makes Fourier coefficients constant along infinite A^T-orbits of every nonzero integral frequency, and square summability forces these coefficients to vanish. The set of forward dense points has full Haar measure, by a countable basis argument. Choose such a point b outside the measure-zero unstable leaf of zero, and let x be its unique C-preimage.

Any nonempty relatively open O in C contains all C-preimages of a sufficiently small old open rectangle. To see this, choose two nearby non-atomic stable cuts whose cumulative graphs lie in a small chart rectangle inside O, then shrink its u-width. The dense orbit of b enters the old rectangle, so PF=AP forces the orbit of x into O. Thus F|C is transitive. Since P(C) is the whole old torus, C is nontrivial.

## 6. Necessary ratio and dependencies

For any exact triple of this type, the unique area form nu with i_Y nu=eta satisfies f*nu=Ka nu. Strict trapping gives Ka integral_S nu=integral_(fS) nu<integral_S nu, hence r>1. The construction attains every such r for the chosen homology eigenvalue K.

The audit source is the full construction. The only general inputs are compact oriented-surface classification, elementary covering-space theory, smooth calculus, and the local unstable-manifold characterization by uniform hyperbolic contraction. The convergence, trapping, tensor, and dense-orbit arguments above are explicit. No numerical test is part of this proof. See in the team records for the inspected source version.
