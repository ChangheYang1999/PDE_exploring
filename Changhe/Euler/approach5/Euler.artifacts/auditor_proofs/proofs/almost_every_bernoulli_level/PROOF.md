# Opposite helicity signs on almost every attained Bernoulli level

Auditor verdict: CONFIRMED (A387), 2026-11-03T01:52:02Z. The complete argument below has been independently checked at its exact written scope.

## 1. Exact profile statement

Let U in C2(R3;R3), P in C1(R3), 0<c<1/2 and omega in R satisfy

    div U=0,
    (1-c)U+(B.grad)U+omega JU+grad P=0,
    B=(cI-omega J)y+U, J(y1,y2,y3)=(-y2,y1,0),
    U(y)=o(|y|) uniformly as |y| tends to infinity.

Put W=curl U, a=1-2c>0, h=U.W, and

    H=P+|U|^2/2+((cI-omega J)y).U.

Let D be any open set invariant under every time of the complete W flow Gamma. Define the open subsets of R

    J_plus=H(D intersect {h>0}),
    J_minus=H(D intersect {h<0}).

Then J_plus and J_minus differ by a Lebesgue-null set. Their intersection is open and has full Lebesgue measure in their union. In particular they have the same closure, unless both are empty, in which case that assertion is also true. No helicity integrability, Dini condition, basin coverage, bounded H or vortex-flow ergodicity is assumed.

For each value in their intersection there are regular local level-surface patches inside D on which h has either strict sign. These are two-dimensional patches; a regular exact level is not asserted to have positive three-dimensional volume.

There is also an orbitwise statement. On every two-sided recurrent nonconstant vortex orbit in D, for almost every value in the interior of the range of H on that orbit, both strict signs of h occur at that exact value at vortex times arbitrarily far in both directions. The exceptional null set of values may depend on the orbit. The recurrent set has full ambient volume by the established recurrence theorem, but no claim is made for a vortex orbit on which H is constant.

## 2. Inputs already confirmed in the campaign

The exact Lamb identity gives W.grad H=-a h. A048-A049 give completeness and two-sided conservative recurrence of Gamma under the stated uniform sublinearity. A328 gives, for every Borel I contained in R,

    integral_(D intersect H^-1(I)) h_plus dy
      =integral_(D intersect H^-1(I)) h_minus dy,         (1)

as equality in [0,infinity]. Here h_plus=max(h,0) and h_minus=max(-h,0). The complete proof is in the independent auditor's helicity-level result, Section5. In particular (1) remains available when both total helicity integrals on D are infinite. The deductions below from these inputs are elementary and are written in full.

## 3. The images of the two strict-sign sets agree modulo null values

At any x with h(x) nonzero, W.grad H(x) is nonzero, hence grad H(x) is nonzero. The C1 submersion theorem supplies local coordinates (v,z1,z2) in which H=v. Therefore H maps a neighborhood of x in its strict-sign set onto an open interval. It follows that J_plus and J_minus are open.

Fix x with h(x)>0. Shrink a coordinate box to a product I times Z with compact closure in the strict-positive region and D. Its inverse coordinate map F is C1 with positive absolute Jacobian. There are constants b,j>0 such that h(F(v,z))>=b and |det DF(v,z)|>=j on this product. The two-dimensional rectangle Z has finite positive area. Consequently for every Borel E contained in I,

    integral_(D intersect H^-1(E)) h_plus dy
      >= b j |Z| Leb(E).                                (2)

Let E0=J_plus minus J_minus. It is Borel. There are no points with h<0 and H in E0, so the right side of (1), with I=E0, is zero. The left side is therefore zero too. Apply (2) to E0 intersect I. It follows that Leb(E0 intersect I)=0. The local intervals obtained in this way cover J_plus, and this open cover has a countable subcover because R is second countable. Thus Leb(E0)=0. Reversing signs proves Leb(J_minus minus J_plus)=0.

The intersection is open because each sign image is open. Its complement in their union is the just-proved null symmetric difference. Every nonempty open interval contained in either sign image therefore intersects the other. This proves equality of their closures. At a point with h nonzero the same submersion chart gives a regular two-dimensional exact level patch with that sign. No global Sard theorem for H:R3 to R is used; C2 is sufficient here.

## 4. A one-dimensional critical-value lemma

If q is C1 on R, the set q({t:q'(t)=0}) has Lebesgue measure zero. Here is the elementary proof needed below. Fix a compact interval [-n,n] and epsilon>0. Uniform continuity of q' on [-n-1,n+1] permits a grid of sufficiently small mesh such that on any grid interval meeting {q'=0} intersect [-n,n], |q'|<epsilon throughout that interval. The image of each such interval is an interval of length at most epsilon times its length, by the mean value theorem. There are finitely many disjoint grid intervals, with total length at most 2n+2. Their images cover all critical values from [-n,n], and have total length at most epsilon(2n+2). Let epsilon decrease to zero, then take the countable union over n. This proves the lemma. Endpoint choices do not change the estimate.

## 5. Both crossing directions on one recurrent orbit

Fix a two-sided recurrent x whose vortex orbit stays in D and along which q(t)=H(Gamma_t x) is nonconstant. It is C1 and q'(t)=-a h(Gamma_t x). Recurrence of x implies recurrence of every Gamma_s x: if Gamma_(t_n)x tends to x, continuity gives Gamma_(t_n+s)x tending to Gamma_s x. This holds in each time direction.

Let v be in the interior of q(R) and outside its critical-value set. Choose points on the orbit where q is strictly below and strictly above v. By the preceding recurrence, both inequalities recur at times arbitrarily far in each direction. Given any T>0, choose l1<u1<l2, all larger than T, such that

    q(l1)<v, q(u1)>v, q(l2)<v.

There is a crossing of v in [l1,u1] and another in [u1,l2]. Every root of q-v in these compact intervals has nonzero derivative by the choice of v. Hence the roots are isolated and finite: an infinite collection would have an interior accumulation root with derivative zero, while the interval endpoints are not roots. The signs of q-v at the endpoints now force at least one crossing with q'>0 in the first interval and at least one with q'<0 in the second. Equivalently h<0 and h>0 occur at exactly H=v after time T. Choose three such recurrent visits before -T for the negative direction. The one-dimensional lemma makes the excluded set of values null.

This proves the orbitwise assertion without requiring H bounded, a compact orbit, a finite invariant measure, or any derivative of H beyond C1.

## 6. Consequence for a uniformly one-signed far field

Under the additional Dini tail hypotheses of A363, suppose D is nonempty and the angular tail helicity has a uniform positive lower bound on its spherical trace. A363 supplies R and a nonempty one-sided interval J0 adjacent to the normalized pressure limit such that h>0 on D outside B_R, and every v in J0 is attained there with h>0. Thus J0 is contained in J_plus. Section3 gives J0 contained in J_minus modulo a Lebesgue-null set. Since every negative point is in the fixed ball, for almost every exact v in J0 there is a point inside D and that ball with H=v and h<0. Increase R if necessary so the containing ball is open. Each such point lies on a negative-helicity regular level patch.

This strengthens the previously confirmed statement about every open band to an almost-every-exact-level statement. It still does not establish a strict negative point at every exceptional value, and gives no contradiction to a one-signed tail with a sign-changing core. The conclusion for a uniformly negative tail follows by reversing signs.

## 7. Sharp logical limitation

The analytic periodic scalar q(t)=sin(t)(1-cos(t)) has q'=0 at the upward crossing of level zero at t=0, while q'(pi)=-2. With h=-q'/a on the circle, the value zero has h>0 at its downward crossing and has no h<0 at any point of that exact level. The flow is complete and recurrent; each Borel-band identity holds by the chain rule for an antiderivative over one period. Thus neither recurrence nor equality of the two weighted pushforwards implies both strict signs on every exact level, even for analytic scalar data. This is a reduced scalar illustration, not an Euler profile; its closed orbit is excluded for nonzero actual Euler vorticity by A014.

## Dependencies and scope

The profile result uses A048-A049 and A328; the far-field application additionally uses A363. Independent source files are referenced relative to this agent in the verification manifest. This lemma strengthens a necessary sign condition only. It proves no basin coverage, no global Liouville theorem, no new pressure estimate, and no existence result. Adding a pressure constant translates all value sets and does not affect any conclusion.


## Independent audit checks

The submersion argument uses C1 H only on the strict-sign region; W.H=-a h makes the derivative nonzero there. The zero negative integral over J_plus minus J_minus is legitimate even if the total helicity integrals are infinite, because A328 is equality in [0,infinity]. One may choose each product box with compact closure and positive lower bounds for both h and the coordinate Jacobian. A countable subcover of the open value image suffices. On an individual recurrent orbit, regular roots on a compact crossing interval are finite because an accumulation root would have zero derivative; this proves the crossing signs without a higher-dimensional Sard theorem. The null set is orbit-dependent. The analytic scalar illustration has zero-level roots at integer multiples of pi, with q'=0 at the even multiples and q'=-2 at the odd multiples. It demonstrates precisely the exceptional-level limitation, not an Euler counterexample.

The adjacent verification manifest identifies the exact full input read. This record makes no numerical or formal verification claim.
