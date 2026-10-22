# What three reduced-mismatch samples establish

Status: CONFIRMED complete informal proof, 287 exact controls and actual Opus5.5 review352 following the partial written review351. This note supplies the interpretation rules for an independent audit of the three fixed-lambda numerical states; it does not prove a turning point of B2 or of a continuum forced branch.

## Objects and exact statements

For one saved forced state let beta and lambda be its stored parameters, c_self the center strain of its own full-plane relative inverse, and c_seed the strain of the separately represented fixed source. Define

    m_saved=c_self+lambda c_seed-(1+beta/2).

The values of this expression for specified finite binary coefficients are exact rational numbers under the explicitly reconstructed binary knot convention of packets160 and163. They are quantities of those saved fields. They are not by definition the values of a smooth reduced function m(beta,lambda) obtained by solving the inner infinite-dimensional equations exactly.

For the derivative statements only, suppose a real function f is defined on [b-h,b+h], h>0. Given three observations v_-,v_0,v_+ at b-h,b,b+h, define

    D1=(v_+-v_-)/(2h),
    D2=(v_--2v_0+v_+)/h^2.                                        (1)

1. If |v_j-f(b+jh)|<=delta at all three nodes, then the errors in D1 and D2 relative to the same finite differences of f are at most delta/h and4delta/h^2 respectively. These constants are sharp for arbitrary independently bounded node errors.

2. If f is C3, then

    |D1-f'(b)| <= delta/h+(h^2/6)||f'''||_infinity.                  (2)

   If f is C4, then

    |D2-f''(b)| <= 4delta/h^2+(h^2/12)||f''''||_infinity.            (3)

   Thus4delta/h^2 alone is a bound for the error of a sampled second difference, conditional on delta. It is not an error bound for the derivative at b.

3. Even with zero node errors, the three node values determine neither f'(b) nor f''(b). If q(t) is the quadratic through those values with t=beta-b, then the polynomials

    q(t)+A t(t^2-h^2)+B t^2(t^2-h^2)                              (4)

   take the same three values for all A,B. Their derivatives at0 are q'(0)-A h^2 and q''(0)-2B h^2. Each of these two derivatives may therefore be prescribed arbitrarily while retaining all three observations.

4. If f is C2, its exact central second difference obeys

    [f(b-h)-2f(b)+f(b+h)]/h^2
       = (1/h^2) integral_-h^h (h-|t|) f''(b+t)dt.                  (5)

   In particular a negative exact second difference implies a negative second derivative somewhere in the interval, not necessarily at b. The same conclusion holds if D2+4delta/h^2<0 under the error hypothesis of item1. No negative derivative at every point follows.

5. For three distinct, not necessarily exactly equispaced, nodes b_-<b_0<b_+, put h_-=b_0-b_-, h_+=b_+-b_0 and

    s_-=(v_0-v_-)/h_-,      s_+=(v_+-v_0)/h_+,
    a=(s_+-s_-)/(h_-+h_+), d=s_-+a h_-,
    q(t)=v_0+d t+a t^2,      t=beta-b_0.                           (6)

   This is their exact quadratic interpolant. If a<0 it has a maximum at t_v=-d/(2a) with value v_0-d^2/(4a). These are properties of the interpolating polynomial. They do not supply a root, derivative bound or fold of a function that has only been sampled.

All interval norms here are over [b-h,b+h]. No error delta is inferred from an inner fixed-point residual or from disagreement between a last-iteration diagnostic and an exact saved coefficient evaluation. Such an implication requires a separate stability estimate for that inner problem.

## Proof

Write v_j=f(b+jh)+e_j with |e_j|<=delta. The linear weights in D1 are(-1,0,1)/(2h), whose absolute values sum to1/h; those in D2 are(1,-2,1)/h^2, whose absolute values sum to4/h^2. The triangle inequality proves item1. Choosing the errors with the signs of the respective weights attains equality, so the constants are sharp.

Taylor's formula with integral remainder gives the difference between each of f(b+h), f(b-h) and its second-order Taylor polynomial an absolute bound ||f'''|| h^3/6. Subtracting the two expansions and dividing by2h gives h^2||f'''||/6, since the constant and quadratic terms cancel. Adding the node error bound proves (2). Expanding to order three instead gives remainder at most ||f''''|| h^4/24 on each side. In the sum minus2f(b), the linear and cubic terms cancel, leaving f''(b)h^2 and a total remainder at most ||f''''|| h^4/12. This proves (3).

Each added polynomial in (4) vanishes at -h,0,h. Its first two derivatives at0 are computed directly: t(t^2-h^2) has derivative -h^2 and second derivative0; t^2(t^2-h^2) has derivative0 and second derivative -2h^2. Since h is nonzero, choosing A and B sets the two derivatives independently. This proves item3. It does not assert that the second derivative can be nonnegative throughout the interval when the observed second difference is negative.

Twice applying the fundamental theorem of calculus yields

    f(b+h)-f(b)-h f'(b)=integral_0^h (h-t) f''(b+t)dt,
    f(b-h)-f(b)+h f'(b)=integral_-h^0 (h+t) f''(b+t)dt.

Their sum is (5). The kernel is nonnegative with integral h^2. If f'' were nonnegative throughout the interval, the integral could not be negative. This proves item4, including its conditional observed-data version using item1.

For item5 the two slopes of q between its central point and its endpoints are d-a h_- and d+a h_+. Substitution of (6) gives s_- and s_+. Hence q interpolates all three values; uniqueness follows because a degree-at-most-two polynomial with three distinct roots vanishes. Completing the square gives its critical point and value when a is nonzero. A negative a makes that point the maximum. Nothing in this algebra identifies the true underlying function with q.

## Exact unequal-node error bounds

Let h_-,h_+>0, H=h_-+h_+, and let d and a be (6). If |v_j-f(b_j)|<=delta at the actual three nodes, the error in d relative to the derivative of the quadratic interpolating the exact f-values is at most delta L1, where

    L1=h_+/(h_- H)+h_-/(h_+ H)+|h_+-h_-|/(h_-h_+).                 (7)

The analogous error in2a is at most4delta/(h_-h_+). Both bounds are sharp under separately bounded node errors. Indeed the weights of d on (v_-,v_0,v_+) are

    (-h_+/(h_-H), (h_+-h_-)/(h_-h_+), h_-/(h_+H)),

and those of2a are (2/(h_-H),-2/(h_-h_+),2/(h_+H)). Their absolute sums give these bounds. Formula(7) is not exactly2/H+|h_+-h_-|/(h_-h_+); the omitted nonnegative difference would be(h_+-h_-)^2/(h_-h_+H).

For f in C3, expansion on each side to degree2 gives

    |d-f'(b_0)| <=delta L1+(h_-h_+/6)||f'''||_infinity.              (8)

For f in C4, expansion through degree3 gives

    |2a-f''(b_0)| <=4delta/(h_-h_+)
             +|h_+-h_-| |f'''(b_0)|/3
             +(h_-^3+h_+^3)||f''''||_infinity/(12H).                (9)

For(8), the two Taylor remainders have bounds M3 h_-^3/6 and M3 h_+^3/6. Their absolute derivative weights are h_+/(h_-H) and h_-/(h_+H), yielding M3 h_-h_+/6. For(9), the quadratic and cubic coefficients of2a are f''(b_0) and(h_+-h_-)f'''(b_0)/3. The fourth-order remainders, weighted by2/(h_-H) and2/(h_+H), give the last term. These proofs retain the exact binary spacings, so no transfer between distinct evaluation nodes is assumed.

The same-node nonidentifiability also holds at unequal nodes. Put P(t)=t(t+h_-)(t-h_+) and add A P(t)+B t P(t) to q(t). Its changes to the first and second derivatives at0 are -A h_-h_+ and2A(h_--h_+)-2B h_-h_+. The coefficient map is triangular with nonzero diagonal, so arbitrary derivatives are possible with the same three observations. These are unrestricted smooth interpolation examples, not B2 solution branches. Finally,2a=f''(xi) for some point between the outer nodes when f is C2 and its values are exact: f-q has three zeros, so two applications of Rolle's theorem produce a zero of f''-2a. A negative exact2a thus forces negative curvature somewhere, not at the center.

A finite-dimensional reduced map at fixed discretization and a continuum reduced map are different f's. An error bound relative to the latter also needs discretization control. A positive lambda secant likewise establishes a derivative sign somewhere on its interval under C1 hypotheses, not its value or a neighborhood lower bound at a proposed fold. No such derivative bounds have been established here.

## The distinction needed for the B2 audit

A scalar reduction would first need a well-defined inner solution F(beta,lambda), together with sufficient differentiability of the map

    m(beta,lambda)=c[F(beta,lambda)]+lambda c_seed-(1+beta/2).

An invertible inner linearization plus suitable Banach-space hypotheses is one route to such a map, but it is not established merely by successful iteration at three parameter values. A small iteration residual also does not bound |m_saved-m(beta,lambda)| without a quantified inverse or another error estimate. An exact evaluation of m_saved removes evaluation error for that represented state; it does not remove inner-solve error.

The usual nondegenerate scalar turning-point conditions at a specified parameter pair are

    m=0, m_beta=0, m_lambda!=0, m_beta_beta!=0,

together with whatever inner-solution hypotheses justify the reduction. Finite secants in lambda and a central second difference in beta may suggest these conditions. They do not establish them. A positive central m_saved and a nonzero first difference at a nominal vertex are not literal zero conditions. A nonzero D1 is not itself proof that m_beta is nonzero; item3 explicitly permits m_beta=0 with that same D1. The phrase 'at the sampled tolerance' must identify the error model and which quantities are bounded, rather than equate small displayed numbers with these equalities.

For h=0.01 and the assumed node error delta=2e-6, item1 gives0.0002 for D1 and0.08 for D2. These are arithmetic consequences of that assumed error. There is no automatic error bound on f'(b) or f''(b), and the assumptions do not make a central value exceeding2e-6 equal to zero. Item3 gives explicit smooth counterexamples to a derivative inference even when the node values are exact.

There is also a positive conditional conclusion: if a specified continuous f differs from these three saved m-values by at most2e-6 at the actual nodes, its center value is positive and its two endpoint values are negative. The intermediate value theorem then gives a zero in each open adjacent interval. With C2 regularity the negative exact second divided difference also gives negative curvature somewhere. These conclusions remain conditional on the same unestablished node-error bound and a common function f. They give no location or nondegeneracy of a fold and are not certified root brackets for an actual computed inner branch.

Stored beta values are binary rationals and their spacings need not equal the decimal number0.01 exactly. The audit will report both (1) with its stated nominal h and the exact unequal-node quadratic (6). This distinguishes a negligible representation difference from the much larger missing inner-error and derivative-remainder bounds.

Dependencies: packets160 and163 supply the exact center certificate definitions for the saved representations. All finite-difference results above are proved here. They are independent of any NUM source code, and need no numerical experiment for validity. Formal sources and finite controls are recorded alongside this proof; no Lean or Lake execution is claimed.
