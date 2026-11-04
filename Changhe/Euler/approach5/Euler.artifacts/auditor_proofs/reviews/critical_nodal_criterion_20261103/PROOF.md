# Critical vortical nodes and the remaining concentration set

Status: CONFIRMED for the conditional criteria below. The absence of critical vortical nodes and flat velocity zeros is not proved.

## 1. Hypotheses and notation

Fix 2/5<c<1/2 and omega in R. Let Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax, a=1-2c and p=(1-c)/c. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1).

The two rates can be replaced by U tending to zero and DU=O(sqrt(|x|)), by A498 and A476-A477 in this c range. Let V,W=curl V,P2 be the actual velocity, vorticity and canonically normalized pressure tails. These are actual-profile limits, not arbitrary local homogeneous fields. Set k=X.V, S=P2-|V|^2/2 and, on the unit sphere, K=k, G=W, h=S. The tail is C^(1,alpha) for each fixed 0<alpha<1.

For an angular open set O put

    M(O,tau)=integral_(O intersect {|K|<tau})|G|dA.

Let Sigma be the set of points with no neighborhood O satisfying M(O,tau)=o(tau). Let Z_flat be the angular set V=DV=0, where DV denotes the ambient derivative of the tail. Let CVN be the angular set grad k=0,W!=0. The twisted cone over O is the union of exp(tA)O over real t. The nodal premise N on a cone is {k=0} contained in {W=0} there.

The conclusion is

    Sigma subset closure(CVN) union (Z_flat intersect supp G).

In particular, if CVN is empty and there is no flat velocity zero in supp G, then U=0. A separate criterion is: U=0 if V has no angular zero and W is parallel to X at every critical vortical node with S=0. All statements hold for every finite real omega.

## 2. Exact identification of the remaining nodal premise

The tail identities are

    X.grad k=-ak,
    grad k=X cross W-aV.

Since a>0, grad k=0 implies k=0. Thus

    CVN={k=0,grad k=0,W!=0}
       ={W!=0,X cross W=aV} on the sphere.

A897 excludes every regular vortical actual tail node under Section 1's hypotheses: k=0 and grad k!=0 imply W=0. Therefore N on an open twisted cone is equivalent to absence of CVN on that cone. One implication is the definition; for the converse, a vortical zero of k without a critical node would be a forbidden regular node. Twisted homogeneity propagates these properties between the cone and its angular cross-section.

This excludes regular nodes only. Interior zeros of k with W!=0 are critical, and critical zeros on the boundary of a zero region remain possible in the present argument.

## 3. Localization of the critical mass

A731-A732 give, if U is nonzero, constants C0,tau0>0 such that

    M(S2,tau)>=C0 tau for 0<tau<tau0.

They also show Sigma is closed, nonempty and contained in {K=0} intersect supp G. Nonemptiness follows directly from a finite angular cover: if every point had a neighborhood of o(tau) mass, finitely many such neighborhoods would cover the sphere and contradict this bound.

Take w in Sigma outside closure(CVN). Choose an angular neighborhood O whose cone has no critical vortical node. Section 2 gives N on that cone. If the tangential gradient of K at w is nonzero, regular level coordinates have bounded area Jacobian. On their local zero curve G=0 by N. Holder continuity then gives |G|<=C|K|^alpha in a smaller chart, hence

    M(O',tau)<=C tau^(1+alpha)=o(tau).

This contradicts w in Sigma.

Suppose instead grad_S2 K(w)=0. Since K(w)=0, X.grad k=0. A purely radial ambient gradient would have nonzero product with X unless it vanished, because X(w).w=c. Therefore grad k(w)=0. Absence of CVN gives W(w)=0. The gradient identity now gives V(w)=0.

If DV(w)!=0, the local saddle estimate A832 applies using N only on this cone. It provides C1 coordinates u,v with |K| comparable to |uv| and G bounded by C min(|u|,|v|)^alpha. Integrating in the four quadrants gives

    M(O'',tau)<=C tau^(1+alpha/2)=o(tau),

again impossible. Thus DV(w)=0, and w belongs to Z_flat intersect supp G. This proves the stated containment. The argument assumes no Hessian of k at w.

If CVN is empty and Z_flat intersect supp G is empty, the containment makes Sigma empty. The lower bound then forces U=0.

## 4. Joint-scalar variant

A838 gives the following actual-profile criterion: if V has no angular zero and

    {K=h=0,G!=0} subset {V=0},

then U=0. Its proof uses the joint sublevel lower bound with |h|<tau^(2p/(p-1)); it does not require N everywhere.

By A897 every point of {K=h=0,G!=0} is now critical. At such a point the gradient identity says aV=X cross W. Since X is nonzero away from the origin, V=0 is equivalent to W being parallel to X. Hence the stated condition at critical vortical nodes with S=0 is exactly the hypothesis needed by A838. This proves the second criterion, with its absence-of-velocity-zeros premise retained.

## 5. Scope and source comparison

The coordinator's CO46(a)-(e) follow at the stated global helicity-free, natural-tail scope. The source's informal reference to its regular-node estimate can use either the weaker o(tau) A733 or the Holder refinement explicitly checked in A832-A838; both suffice. The set closure(CVN), rather than CVN itself, is needed in the localization.

These criteria do not show CVN is empty. The local common-zero and open-zero constructions are tests of the local tail equations, not global actual-profile examples. The specific all-rotation family A875 fails the full momentum equation by A876. This should not be read as saying every local open-node construction fails that equation: the omega=0 azimuthal example in A840 is a local exact profile with an axis singularity. Neither example changes the global conditional criteria.

Global zero helicity and the derivative premise remain separate from the original bare-decay conjecture. No completeness of the partial tail-vorticity flow is assumed here; the lower bounds used above were proved by stopping that flow before arrival at the removed origin.
