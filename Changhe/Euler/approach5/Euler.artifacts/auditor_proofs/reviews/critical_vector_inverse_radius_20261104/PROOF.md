# Independent audit of the critical vector inverse-radius constant

Status: independent reconstruction complete; existing configured model comparison and designated verdict pending. Source: in the team records, SHA256 ef352f05733813c5ca2727cd5aaed46f845aa451eddc278c9b01a043c25b9558. All six source sections and35 manual checks were read. No mathematical computation is needed.

## 1. Precise positive statement

Let O be a connected open subset of C containing0 and N a positive integer. Assume

    u in L2_loc(O;C^N) intersect H1_loc(O minus {0};C^N),
    |dbar u(z)| <= |u(z)|/(4|z|) almost everywhere off0,
    lim_(r->0) r^(-L) integral_B(0,r)|u|^2 =0 for every L>0,

where dbar=(partial_x+i partial_y)/2. Then u=0 almost everywhere on O. If a continuous representative exists, it is zero at every point. No value of an arbitrary measurable representative at the single point0 is determined.

For the local conclusion on a disc it suffices to assume only

    ||r dbar u(r exp(i phi))||_(L2_phi)
       <=(1/4)||u(r exp(i phi))||_(L2_phi)

for almost every radius in that disc. For the global conclusion we retain the pointwise inequality away from0 to permit propagation. Dependencies are circle Fourier spectral theory, Hilbert-valued H1 absolute continuity, the elementary product rule for a bounded operator, and the weighted integrability proved next. No strict Carleman absorption is invoked.

## 2. Cylinder regularity, equation and weighted decay

Choose B(0,R) compactly contained in O and put t=-log r, T0=-log R, U(t,phi)=u(exp(-t)exp(i phi)). On every compact t interval, the smooth coordinate transformation and equivalence of its bounded positive weights give

    U in H1_t(H) intersect L2_t(Domain(D)),
    H=L2(S1;C^N), D=-i partial_phi on periodic H1(S1;C^N).

Use the common locally absolutely continuous H-valued representative. The self-adjoint operator D has integer eigenvalues, including all positive and negative angular modes. The polar identity dbar=exp(i phi)(-partial_t+i partial_phi)/(2r) gives

    U_t+D U=G,    G=-2r exp(-i phi)dbar u,
    ||G||_H <=(1/2)||U||_H

almost everywhere. The angular-average hypothesis gives exactly the same last inequality.

For every lambda>0, integral flatness implies

    integral_(T1)^infinity exp(2lambda t)||U(t)||_H^2 dt<infinity.

Indeed this is the integral of |z|^(-2lambda-2)|u(z)|^2 in the small disc. On exp(-(j+1))<|z|<=exp(-j), the weight is at most exp((2lambda+2)(j+1)). Integral flatness bounds the unweighted mass of this annulus by exp(-Lj) for all sufficiently large j, where choose L>2lambda+2. The resulting geometric series converges. The finitely many remaining compact annuli have finite mass. This argument makes no pointwise claim about decay on every circle.

## 3. Bounded signed energy

Fix m>=0 an integer, lambda=m+1/2, and let P_+ and P_- be the orthogonal projections onto modes k>=m+1 and k<=m. Set S=P_+-P_- and W=exp(lambda t)U. Thus S is a bounded self-adjoint involution, of norm1, and

    Q(t)=<SW(t),W(t)>_H
        =||P_+W(t)||_H^2-||P_-W(t)||_H^2

is real and locally absolutely continuous. The equation yields W_t=-(D-lambda)W+exp(lambda t)G. At almost every t, W belongs to Domain(D), so differentiation of this bounded quadratic form gives

    Q'=-2<|D-lambda|W,W>
           +2 Re<SW,exp(lambda t)G>
       <=-||W||_H^2+2||W||_H exp(lambda t)||G||_H
       <=0.

The first inner product is legitimate: sum_k |k-lambda||W_k|^2 is finite by Cauchy-Schwarz from sum_k |k-lambda|^2|W_k|^2<infinity and W in H. The spectral bound uses |k-lambda|>=1/2 for every integer k. We never differentiate the unbounded form <DW,W>; the differentiated form contains only bounded S.

The final inequality allows equality. Its usefulness is monotonicity, not strict negative dissipation.

## 4. Two limits and the full spectral conclusion

For this fixed lambda, the weighted integrability in Section2 gives W in L2 on a half-line. Thus there are times t_j tending to infinity with ||W(t_j)||_H->0. They may be chosen from intervals whose integrals tend to0, within the full-measure set where the representative agrees with the Sobolev function. Its continuity then makes the same Q available at these times. Hence Q(t_j)->0.

For every fixed finite t, monotonicity gives Q(t)>=Q(t_j) for all sufficiently large j. Therefore Q(t)>=0. Cancelling the positive scalar exp(2lambda t) gives

    ||P_(k<=m)U(t)||_H^2<=||P_(k>=m+1)U(t)||_H^2.

This holds for every m>=0 and every t>T0, using the same continuous representative; alternatively the countably many m permit a common full-measure set and continuity. Fix t, then let m tend to infinity. Square summability of the full Fourier series makes the left side converge to ||U(t)||_H^2 and the right side to0. Thus U(t)=0. The order is fixed m, t_j to infinity, then fixed t, m to infinity. Neither a finite-mode approximation nor an assumed uniform bound in m is needed.

This proves local vanishing for the punctured-H1 class, with no derivative estimate at0. The center itself is a null set for the almost-everywhere conclusion.

## 5. Connected propagation

Let Z be the open set of points with an almost-everywhere zero neighborhood. It contains a neighborhood of0. If p were a relative boundary point, then p!=0. Choose B(p,2r) compactly contained in O minus {0}, with the original coefficient bounded there by K, and shrink r until Kr<=1/4. Take a in Z with |a-p|<r/4. On B(a,r),

    |dbar u|<=K|u|<=(Kr)|u|/|z-a|<=|u|/(4|z-a|).

The function has integral infinite order at a because it is zero in a neighborhood. Applying Sections2-4 on B(a,r) gives zero throughout that disc. It contains a neighborhood of p, a contradiction. Thus Z is relatively closed and connectedness gives Z=O. This proof only uses local changes of coordinates and bounded coefficients; no complete trajectory or flow at infinity is assumed.

## 6. Counterexample with asymptotically critical majorant

Choose smooth nondecreasing chi:[0,1]->[0,1], constant0 and1 near the endpoints, and M=sup chi'. Put t_n=1+n(n-1)/2 for n>=1. On [t_n,t_(n+1)] of length n define

    theta_n(t)=(pi/2)chi((t-t_n)/n),
    F'(t)=n+sin^2(theta_n(t)),    F(1)=0.

Let j_n alternate between2 and1. For t=-log r>=1 define

    u(r exp(i phi))=exp(-F(t))[
         cos(theta_n)exp(in phi)e_(j_n)
        +sin(theta_n)exp(i(n+1)phi)e_(j_(n+1))].

The vector has norm exp(-F)>0. At each seam, F' is identically n+1 on both sides, and both formulas become the same constant times z^(n+1) in the same component on a whole annular neighborhood. This proves smooth seam compatibility. The amplitude calculation in Section3 of the adjacent strict-threshold audit, or direct differentiation, gives

    |dbar u|/|u|=(theta_n'+sin(theta_n)cos(theta_n))/(2r)
               <=[1/4+pi M/(4n)]/r.

This identity is checked directly from (F'I-diag(n,n+1))w-w' for w=(cos theta,sin theta); it does not depend on that adjacent audit being promoted.

## 7. All-order extension and exact tail

For t in the n-th interval, t<(n+1)^2, so F'(t)>=sqrt(t)-1. Integration from1 gives

    F(t)>=(2/3)t^(3/2)-t+1/3.

Also n<=sqrt(2t)+1, so F' has polynomial growth. Higher derivatives are uniformly bounded, since each theta derivative costs a power of1/n and seams have constant F'. Angular derivatives cost polynomial powers of n+1. Iterating the Cartesian derivatives as above gives, for each k,

    |D^k u(z)|<=A_k(1+t)^(p_k)exp(-F(t)+kt).

The t^(3/2) term dominates every fixed linear term and logarithmic term. Thus |D^k u|=o(r^q) for every k and q>0. Extension by zero, with the difference-quotient induction of the strict-threshold audit, is smooth and flat in every derivative. The same estimate implies integral infinite order.

Set b(r)=[1/4+pi M/(4n)]/r on the n-th annulus and b(0)=0, choosing either adjacent value at a seam. It is measurable, bounded on every closed punctured annulus, and bounded globally by (1/4+pi M/4)/r. Hence it is weak-L2. Moreover r b(r)->1/4. Given0<delta<1/4, on a sufficiently small disc,

    (1/4-delta)/r <= b(r) <= (1/4+delta)/r.

Outside that disc b is bounded. For large level s the entire superlevel set lies inside it, and the two radial bounds give

    pi(1/4-delta)^2 <= s^2 area{b>s} <= pi(1/4+delta)^2.

Let s tend to infinity, then delta to0. The high-tail limit is exactly pi/16. This is a calculation for the chosen majorant; it is not a claim that the actual quotient has this distribution.

## 8. Scope and consistency checks

The exact pointwise coefficient1/(4r) forces vanishing, but the majorant in Section7 is strictly larger at every positive radius and only tends to that coefficient asymptotically. The constructed nonzero vector therefore does not satisfy the positive theorem. Indeed the theorem itself shows that its actual quotient must exceed1/(4r) somewhere in every sufficiently small disc. This deduction is not circular: the positive theorem was independently proved before constructing the example.

Together with the strict examples, the positive statement identifies the full inverse-radius threshold: continuation holds for constants at most1/4, while every larger constant admits a smooth two-complex-component counterexample. The exact high-tail value pi/16 alone is insufficient for vector continuation. No optimal threshold for arbitrary weak-L2 norms is established.

The actual Pan-Zhang2024v1 Theorem6.1, printed page19 and its proof through page23, was checked in the adjacent audit; it supplies the known strict precedent, not this endpoint proof. No novelty claim is made. The scalar continuation theorem is unaffected: a vector inequality gives no inequality with each component's own modulus. C67 has one complex unknown from two real components. Nothing here constructs a real carrier, Euler profile, pressure, vorticity compatibility or global decay. The missing Euler majorant and the unrestricted rotating conjecture remain open.

## 9. Existing model comparison and diagnostic limits

The complete Theory Agent C comparison dated2026-11-04T04:43:19Z was read, along with its entire LIT349 script and log. Items1-7 agree with the mathematical proof. In particular, the differentiated form uses bounded S; the endpoint gives monotonicity without strict decay; the tail sequence is chosen for each fixed half-integer before the spectral split tends to infinity. The variable-width construction has n tending to infinity because t lies between t_n and t_(n+1), a sequence of bounded finite endpoints for every bounded n. The upper estimate n<sqrt(2t)+1 alone would not establish that limit, but the interval definition does. The independent proof already uses both facts.

The retained script reports15 passing conditions:10SYM,1FIN,1FORMULA,2SAMPLE,1EX, and exits nonzero on a failed predicate. The finite half-integer grid is the FIN item; the six truncated ODE runs are one SAMPLE item. The note incorrectly calls the ODE experiment FIN. Its finite differences test ten points, eight in transitions, and its negative control uses the exact integer spectral collision. None proves the Hilbert-space theorem. The displayed symbolic positivity identity needs the stated n>=1 hypothesis for its strict sign; that sign is immediate by hand.

The note abbreviates the source hash as ef352f05...fce63e80d. That suffix belongs to neither the actual349 file nor its retained submitted hash, which ends01a043c25b9558. The exact source copied in this review has the hash in the opening paragraph. The mismatch is a provenance typo, not a change of mathematical source. The reported save time is not independently attested by this comparison.

The existing configured model exchange is through files; actual provider execution is independently unattested. The diagnostic scripts were read but not rerun. No new mathematical computation or model client was used.


## 10. Confirmed-source status revision

The exact current source has SHA256 b6340e5f266bee5a3082d3cd7e5a28b44ee363a00dc84330efabe33e9d9a9c29. The full difference from the retained submission has been read: one opening status line changes, and one final comparison section is added. The status now cites A2930-A2931, and an added final section describes the actual existing-model and designated comparisons. Its A2929 hash and diagnostic correction is accurate. It retains the distinct pointwise theorem and asymptotic-majorant counterexample and their scalar/Euler limits. No displayed equation, mathematical hypothesis or proof argument changes. The old pending sentences belong to the dated original submission and are superseded by the new status section. The capture and complete difference are retained in verification.
