# Component constants at a supported nonflat W2 direction

## 1. Exact conditional setting

Fix2/5<c<1/2, every finite omega, A=cI-omega J, X=Ax, a=1-2c, b=2(1-c), q=b/a>6. Retain the actual C2 globally zero-helicity Euler profile, natural velocity/derivative bounds and escaping lower-window W2 trace of A1254-A1259. Let V,P2 be its actual tails, W=curl V, k=X.V and S=P2-|V|²/2. Suppose its supported direction w is nonflat: V(w)=W(w)=S(w)=0 and M=DV(w)!=0. At the equality covector rate rho=-b, the established inputs give

    ell=grad S(w)!=0, k(w)=grad k(w)=0,
    k(w+h)=-(a/2)h.Mh+o(|h|²),
    w outside closure(int{k=0}),
    bS grad k=ak grad S on supp W.                  (1)

Here S,k are C1 near w. The point derivative of grad k is -aM; no C2 neighbourhood bound is asserted. M is a transverse planar saddle annihilating X(w), and every vortical approach direction on a transverse section lies on the one allowed line from A1256. These are genuine premises. The conclusions below do not apply unchanged to rho<-b, where ell=0.

Shrink to a ball B(w,r0) on which |grad S|>=|ell|/2 and which contains no open subset of {k=0}; this is possible by(1).

## 2. Componentwise power relations

On each connected component C of {W!=0,k!=0}, the rank relation gives

    grad(S|k|^(-q))=0,
    S=D_C|k|^q                                    (2)

for one finite real D_C. An open connected subset of Euclidean space is path connected, so zero gradient indeed gives a single constant there. No bound common to different components follows.

On an open connected box with W!=0 and S!=0, the same equation gives

    grad(k|S|^(-1/q))=0,
    k=kappa|S|^(1/q).                             (3)

This second formula is valid even if k vanishes. Its exponent lies strictly between zero and one. It is the useful formula at a possible nodal point.

## 3. Both nodal sets are irrotational near w

Suppose x0 in B(w,r0) is vortical and S(x0)=0. A smaller C1 coordinate box lies wholly in {W!=0}, and S is one of its coordinates by grad S!=0. Each of its two sides is connected. Equation(3) holds there with constants kappa_+ and kappa_-. Along a transverse coordinate curve, |S| tends to zero with nonzero derivative. A nonzero kappa would give |grad k|=|kappa| |S|^(1/q-1)|grad S|/q tending to infinity. This contradicts k in C1. Thus both constants vanish and k=0 on the whole box by continuity, contrary to(1).

If instead S(x0)!=0 but k(x0)=0 at a vortical point, equation(3) on a connected smaller box gives kappa=0 immediately and the same contradiction. Therefore

    {W!=0} intersect B(w,r0) subset {k!=0,S!=0}.    (4)

This proof does not choose a component whose closure contains x0. The original14:48 argument made that unjustified choice; the corrected14:49 argument above is valid even with infinitely many accumulating components. Both nodal sets lie in {W=0} locally. Their twisted-flow saturations do also by the exact homogeneity of W,k,S, wherever that flow remains in the domain.

## 4. Divergence of the constants along supported approach

On the set in(4), equation(1) and nonzero S,k imply grad k!=0 and

    |S|/|k|=|grad S|/(q|grad k|).                  (5)

As a vortical point tends to w, the numerator tends to |ell|>0 and the denominator tends to zero. Thus this ratio tends to infinity along every such sequence. Since k tends to zero and q>1,

    |D_C|=(|S|/|k|)|k|^(1-q)->infinity.            (6)

Support ensures that such sequences exist. No one component with a fixed finite constant can have w in its closure. No finite family of such components can supply a sequence approaching w, since their finitely many constants have a finite maximum. Hence infinitely many distinct components accumulate and their constant magnitudes become unbounded. This is a necessary condition, not a construction of components or an exclusion of their possibility.

## 5. Componentwise distance estimate and its limit

On a fixed component in the ball, S has the nonzero sign of D_C. Equation(1) gives |k(w+h)|<=C|h|² with C independent of that component. Thus

    |S(w+h)|<=|D_C| C^q |h|^(2q)                 (7)

at its points near w. The C1 submersion S makes |S| comparable, with fixed positive constants, to the distance to its local zero hypersurface Sigma after shrinking the box. Equation(7) therefore bounds that distance by a constant depending on C times |h|^(2q).

There is no uniform cusp bound over all components: the factor |D_C| is unbounded by(6). Moreover no individual fixed component approaches w arbitrarily closely. Thus the phrase that each component approaches Sigma to order2q means exactly the pointwise component-dependent inequality(7), not a uniform asymptotic description of one component ending at w. The one-line transverse restriction is separately A1256 and must not be restated as a restriction to one line for every three-dimensional displacement.

## 6. The proposed original-profile power relation is not established

The final parenthetical suggests an exact original-side formula

    H-Hinf-g=D_C|g|^q

on the corresponding vortical component. This does not follow from the original rank relation dH wedge dg=0 or from the Bernoulli law BH=-ag. These only give a local function g=G(H) and its scalar characteristic ODE. For a direct test of that inference, on a coordinate region h>0 set H=h, g=2h, Hinf=0 and B=-2ah partial_h. Then dH wedge dg=0 and BH=-ag, but

    (H-Hinf-g)/|g|^q=-2^(-q)h^(1-q)

is not constant. Extra transverse components can be appended to B without changing either identity. This is an exact scalar inference countertest, not an Euler profile or a counterexample to the global conjecture.

What the actual tail expansion does give at an escaping orbit whose limiting k is nonzero is the asymptotic identity

    Q(y_t)/|g(y_t)|^q -> S(x)/|k(x)|^q=D_C,
    Q=H-Hinf-g,

because e^(bt)Q tends to S, e^(at)g tends to k and aq=b. This is a limit, not constancy of the original ratio at finite time. Any proposed original-side uniform bound should be stated for these asymptotic constants, or proved by an additional argument. The existence of such a bound remains open.

## 7. Evidence and unresolved scope

The full current3f-bis(a)-(e), the corrected team note and the complete independent A1254-A1259 proof were read. The nodal argument, signs, component topology and every limit above were reconstructed without computation. No pressure normalization beyond the explicitly stated Q limit is used. The source agent is configured model; the earlier nested the external referee (a second model)'s failed model credential lookup was not a completed model review. Comparison continues through the existing configured model agents, with actual provider runtime unattested and no new client.

The supported nonflat W2 configuration remains open. C2 regularity of S, if supplied, is not shown here to exclude it; the geometric suggestion at the end of the source is not a proof. In the globally smooth decaying zero-helicity class A309 already gives exclusion, so these conditional obstructions must retain their finite-regularity scope and not be advertised as solving the campaign's arbitrary-helicity conjecture.
