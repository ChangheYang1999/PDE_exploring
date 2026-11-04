# Zero carrier work on compact degenerate-Lamb supports

Status: CONFIRMED A470 at the exact hypotheses below after independent reconstruction, full postwrite inspection and the complete focused configured-model review. The global decay-only conjecture remains open.

## 1. Statement and dependencies

Let 0<c<1/2, omega in R, U in C2(R3;R3), P in C1 solve the full rotating incompressible profile equation

    (1-c)U+B.grad U+omega JU+grad P=0, div U=0,
    A=cI-omega J, B=Ay+U, W=curl U.

Assume uniform U=o(|y|) and U.W=0 everywhere. Put a=1-2c>0,

    alpha=B cross W, O={W!=0},
    H=P+|U|^2/2+(Ay).U, g=U.B.

Let S be compact, invariant under the carrier flow for every real time, and contained in closure(O) intersect {W=0,Dalpha=0}. Then g<=0 on S. If S is the support of an invariant probability, then g=0 on S. Neither ergodicity nor nonvanishing of B,U or DW is assumed.

The exact Lamb identities are grad H=-aU+alpha and BH=-ag. They make H C2, and g is C2 directly. The only global theorem needed is A413: dH wedge dg=0 on O in this global helicity-free sublinear class. Since this tensor is C1 and zero on the open set O, its values and first derivatives vanish on closure(O). This closure statement concerns the full ambient derivative, not only directions tangent to S. Completeness follows from at most linear growth of B.

## 2. The full Hessian identity at a positive-work point

Fix p in S with g(p)>0. Then U and B are nonzero there. Write M=DU(p). Since W=0, M is symmetric, and div U=0 gives tr M=0. Since alpha=Dalpha=0,

    grad H=-aU, Hess H=-aM.

The rank identity gives grad g=rho U, with the C1 local quotient rho=(U.grad g)/|U|^2. Differentiating grad H cross grad g=0 in an arbitrary ambient direction v at p, using the vanished derivative from Section1, gives

    U cross ((Hess g-rho M)v)=0.

The symmetric matrix R=Hess g-rho M has image in R U. A symmetric rank-at-most-one matrix with this image has the form

    Hess g-rho M=tau U tensor U.                      (1)

This is a full ambient matrix equality. The scalar tau is continuous on the positive-work part of S by this formula; no extension of S to a smooth surface is assumed.

To determine its sign, put K=DW(p). At W=0, Dalpha(v)=B cross Kv. Thus image K is in R B, and K=B tensor ell for a covector ell. The derivative of global U.W=0 gives K^T U=0. But K^T U=g ell, so g>0 implies ell=0 and K=0. The vector identity Delta U=grad div U-curl W then gives Delta U=0 at p.

Directly differentiating g=U.(Ay+U) yields

    Delta g=(B+U).Delta U+2 sum_i partial_i U.partial_i B
           =2|M|_F^2.                                (2)

The cI term is c tr M=0, the skew part of A pairs to zero with the symmetric M, and Delta U=0. Taking the trace of(1) and using tr M=0 gives

    tau |U|^2=2|M|_F^2>=0.                            (3)

Only positive-work points have been used; no sign for Delta g is asserted elsewhere.

## 3. Convexity on the maximal positive interval

Suppose an orbit in S has positive g at time t0. Let I be its maximal open time interval on which g>0. On I all preceding identities hold and rho is C1. Along y(t)=Phi_t x,

    g'=grad g.B=rho g.

Differentiate grad g=rho U along this orbit, an equality valid at every orbit point. Its two sides are C1 in t even if S is not a manifold. Comparing the derivative with(1) gives

    Hess g B=rho' U+rho M B,
    Hess g B=rho M B+tau U g,
    rho'=tau g.

Thus l(t)=log g(y(t)) is C2 and l''=tau g>=0. Its tangent-line lower bound is

    l(t)>=l(t0)+l'(t0)(t-t0), t in I.                 (4)

If I had a finite endpoint, continuity of the complete orbit and maximality would give g tending to zero there, hence l tending to minus infinity, contrary to(4). Therefore I=R. Compactness of S bounds g from above, so l is convex on R and bounded above. A nonzero derivative anywhere would force an unbounded tangent lower bound in one time direction. Hence l is constant and g=g0>0 on the whole orbit.

The Bernoulli equation now gives H(y(t))=H(y(0))-a g0 t, contradicting boundedness of H on S. No point of S can have positive work, proving g<=0.

Both time directions matter. The proof is not a statement about a merely bounded forward semiorbit. Division by U or g is restricted to I; the tangent-line argument prevents a finite endpoint, including one where either velocity vanishes.

## 4. Invariant integration and support

Let S=supp mu for an invariant probability. For small nonzero t, the quotient (H(Phi_t x)-H(x))/t is bounded uniformly on S by sup_S|BH|, using the integral along the invariant orbit. Invariance makes its integral zero. Dominated convergence gives integral BH dmu=0, hence integral g dmu=0 since a>0.

The continuous g is nonpositive on S, so it vanishes mu-almost everywhere. Every relatively open nonempty part of supp mu has positive measure. Continuity therefore gives g=0 everywhere on S. Ergodicity and recurrence are unnecessary. If mu is supported on only a proper part of a larger compact invariant set, equality is asserted on supp mu; the nonpositive inequality still holds on the larger set.

## 5. Scope and verification

This proves zero work for compact invariant probability supports in closure(O) with W=Dalpha=0, by the argument above. It includes first-vorticity-flat supports because DW=0 implies Dalpha=0 on W=0. It does not cover arbitrary irrotational open regions outside closure(O), nonzero helicity, noncompact support, or positive work where Dalpha is nonzero. It does not exclude a flat periodic measure or a carrier-equilibrium atom.

The full informal argument precedes any computation. None is needed. The submitted source is pinned in the team records. The focused challenge independently inspected the closure extension of the C1 rank tensor, the ambient Hessian, the implication g>0 gives DW=0, differentiating along a nonsmooth support, both maximal-interval endpoints and invariant integration. The measure classification A471 and surface argument A465 are separate results; this proof does not depend on either.
