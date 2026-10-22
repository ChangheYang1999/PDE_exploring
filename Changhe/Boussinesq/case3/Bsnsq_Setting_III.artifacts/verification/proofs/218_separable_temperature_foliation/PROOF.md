# A beta=2 obstruction for globally separable temperature level sets

## Exact statement

Let a be a strictly positive C2 function on the entire real line and let H be a C1 real function. Assume there exists a sequence k_j tending to positive infinity with H'(k_j) nonzero. Define
Theta(x,y)=H(x/a(y)).
There is no C1 vector field W on R2 satisfying all three conditions
(i) W.grad Theta=0,
(ii) div W=4,
(iii) for every fixed y, W_1(x,y)/x tends to2 as x tends to positive infinity.
Condition(iii) follows in particular from the B2 beta=2 requirement W=2X+U(X)-U(0) with U(X)=o(|X|). Thus no smooth B2 beta=2 profile has this global temperature representation under these hypotheses. No vorticity equation, sign assumption, inverse formula or y reflection is used in the obstruction.

A B2-compatible temperature trial in this class can be obtained by taking H even, H(0)=H'(0)=0 and H''(0) nonzero, with sufficient smoothness. Its leading coefficient is a0=H''(0)/(2a(0)^2), and it vanishes on x=0. Such a trial is excluded as a component of a B2 solution by the theorem. For example H(k)=k^2/(1+k^2) and any smooth positive a obey the derivative hypothesis, even though H' tends to zero. One may choose a without any y parity. The theorem concerns this restrictive global foliation, not arbitrary x-even temperatures x^2F(x^2,y).

## Change of variables and divergence

Set k=x/a(y). Since a>0, (k,y) maps globally to (x,y)=(k a(y),y) with Jacobian a(y)>0. In these coordinates write
V(k,y)=W_2(k a(y),y),
Q(k,y)=W_1(k a(y),y)-k a'(y)V(k,y).
Then k'=Q/a and y'=V. Direct differentiation, or the Jacobian formula, gives
 div W=(1/a) [partial_k Q+partial_y(a V)],
where partial_y on the right fixes k. For completeness, partial_k Q=a partial_x W_1-a' V-k a' a partial_x W_2 and partial_y(aV)=a' V+a[k a' partial_x W_2+partial_y W_2], so their sum is a div W. The terms cancel without any asymptotic argument.

The transport equation is H'(k) Q/a=0. By continuity of H', each k_j lies in an open interval I_j on which H' is nonzero. Therefore Q=0 on I_j times R. It follows that partial_k Q=0 there and
partial_y(a V)=4a.
Let A(y)=integral_0^y a(s) ds. For each j, integration in y on the whole line gives
 a(y)V(k_j,y)=4A(y)+C_j,
where C_j=a(0)V(k_j,0). The integration constant may depend on j, and no common interval containing all k_j is assumed. Also Q=0 gives, at x_j=k_j a(y),
 W_1(x_j,y)/x_j=[a'(y)/a(y)^2][4A(y)+C_j].

## Fixed-height limit and contradiction

If a'(y0)=0 at any height, the last equation makes W_1(x_j,y0)/x_j=0 for every j, contradicting condition(iii). Thus a' is nowhere zero.

Fix an arbitrary reference height y0. Since x_j=k_j a(y0) tends to infinity, condition(iii) and the last identity imply
 C_j tends to C_infty=2a(y0)^2/a'(y0)-4A(y0).
The same sequence C_j occurs at every other fixed y. Passing to its limit in the identity gives
 4A(y)+C_infty=2a(y)^2/a'(y)  for every y in R.
All terms are C1 because a is C2 and a' has no zero. Differentiate:
 4a=4a-2a^2 a''/(a')^2.
Consequently a''=0 everywhere. Hence a(y)=c y+d is affine. An affine function strictly positive on the entire real line has c=0, contrary to the already proved a' nowhere zero. This contradiction proves the theorem.

## Scope, dependencies, and possible escape routes

The proof uses only calculus, the global positive scale a, the stated temperature transport equation and the fixed positive divergence. The vorticity and whole-plane inverse equations are not relaxed in any claimed B2 solution; they simply are unnecessary for this necessary-condition obstruction. The coordinate k is an analysis variable, not an observer-frame shift or a new physical boundary.

The assumption on H' permits infinitely many zeros and intervals of constancy, provided nonzero derivative values occur at arbitrarily large positive k. It is enough to use the corresponding sequence and its individual neighborhoods. It does not cover H that is exactly constant for all sufficiently large positive k. Constant H with W=2X is a counterexample if the derivative hypothesis is removed, for any positive nonaffine a. That counterexample has no nonzero temperature center jet and is stated only to check the logical hypothesis, not as a profile candidate.

The proof does not claim that a general B2 temperature can be represented as H(x/a(y)). It does not allow a to vanish or be defined only on a half-line; the final positivity contradiction uses the entire real y domain. For instance a(y)=c y+d positive on only an interval is compatible with the differentiated identity on that interval, so this argument supplies no local exclusion. It gives no conclusion at beta other than2, where temperature transport has a nonzero eigenvalue. No bounded-temperature norm, global analyticity or reflection in y was assumed.

This result is an independently derived restricted theorem and cannot constitute the prompt's full NO endpoint. Formalization is not attempted because Lean/Lake builds are prohibited. The verification plan is a symbolic check of the coordinate divergence identity and the scalar differentiation, plus an adversarial actual Opus5.5 review. Those checks support this complete informal proof; no numerical sample is used to prove nonexistence.
