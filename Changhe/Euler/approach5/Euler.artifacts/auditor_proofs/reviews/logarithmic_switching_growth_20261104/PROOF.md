# Growth of the logarithmic switching clock

## 1. Exact statement and dependencies

Fix a>1/4. Let h:R->R be smooth, nondecreasing, equal to 0 for s<=1 and equal to pi/2 for s>=1+3pi/4, with 0<=h'<=1. Assume h'=1 whenever pi/8<h<3pi/8. Put L=2+3pi/4. For t0>=1 solve

    s'=1/2+a/t^2-sin(h(s))cos(h(s)),  s(t0)=0.

Let T(t0) be its first hitting time of L. The LIT352 construction gives constants d>0 and K>1, depending only on a and h, such that

    d<=T(t0)-t0,   T(t0)<=K t0.

These two bounds are imported from the independent LIT352 audit A2952. For t0>8/pi we additionally have

    T(t0)>=lambda t0,  lambda=1+2/(1+a)>1.

Define t1=1 and t_(n+1)=T(t_n). On [t_n,t_(n+1)] define theta_n(t)=h(s(t)) and define F by F(1)=0 and F'=n+sin^2(theta_n). Then there are constants 0<c<C<infinity and t*>1, depending only on a,h, such that, if n(t) is the interval index,

    c log t <= n(t) <= C log t,
    c t log t <= F(t) <= C t log t,  t>=t*.

The constants in the two lines may be enlarged or decreased to use the same c,C. No exact limiting ratio of successive times is asserted.

## 2. Lower passage estimate

Set phi=h(s)-pi/4. Since s'>=a/t^2>0 and h passes continuously from 0 to pi/2, the passage crosses phi=-1/t0 and phi=1/t0 in that order. For t0>8/pi, both levels lie in the middle region |phi|<pi/8, where h'=1. There

    phi'=sin^2(phi)+a/t^2.

Between those two levels, t>=t0 and |phi|<=1/t0. Therefore

    0<phi' <= phi^2+a/t0^2 <= (1+a)/t0^2.

If the crossing times are t_minus and t_plus, integration yields

    2/t0 <= [(1+a)/t0^2](t_plus-t_minus).

Thus T(t0)-t0 >= t_plus-t_minus >= 2t0/(1+a), proving the lower bound. This argument uses only the actual central passage and does not replace the smooth switching function by a limiting Riccati model.

## 3. Counting passages

The fixed spacing d implies t_n>=1+(n-1)d, so some index N satisfies t_N>8/pi. For n>=N, iteration of the upper and lower multiplicative bounds gives

    t_N lambda^(n-N) <= t_n <= t_N K^(n-N).

If t_n<=t<t_(n+1), the left inequality and t_n<=t imply

    n <= N+log(t/t_N)/log(lambda).

The right inequality for t_(n+1), together with t<t_(n+1), implies

    n > N-1+log(t/t_N)/log(K).

At a joining time choose the interval on its right; the same estimates hold up to an irrelevant additive 1. Thus n(t) is bounded above and below by positive multiples of log t for all sufficiently large t.

## 4. Envelope and scope

Because n(t)<=F'(t)<=n(t)+1, the upper passage-count bound integrates to F(t)<=C t log t for large t, after absorbing the finite initial interval. For the lower bound, integrate only over [t/2,t] once t/2>=t*: then F(t)>=c(t/2)log(t/2), since F>=0. This gives the claimed lower multiple of t log t.

The result strengthens the growth description for the particular smooth two-component counterexample of LIT352. Its original lower bound already suffices for all-order flatness, so no earlier theorem depends on this refinement. It gives no scalar or Euler counterexample and no exact asymptotic passage constant. The existing coordinator comparison W6, dated 2026-11-04T05:20:34Z, independently reconstructs the lower crossing estimate. The comparison is configured as model; actual provider execution is independently unattested. No mathematical computation or formal build was used.


## 5. Weaker entry threshold and complete C comparison

The full existing Theory Agent C  comparison dated 2026-11-04T05:27:56Z has now been read, together with its 62-line Python script and 63-line retained log. Its threshold improvement is correct: the lower passage bound already holds for t0>4/pi.

Indeed, the equation on the entire passage is

    phi'=h'(s)[sin^2(phi)+a/t^2].

The bracket is positive and 0<=h'<=1. Thus 0<=phi'<=sin^2(phi)+a/t^2 everywhere. When t0>4/pi, the levels -1/t0 and 1/t0 lie strictly between -pi/4 and pi/4, so continuity and monotonicity give a crossing interval. Between the last crossing of the lower level and the first subsequent crossing of the upper level, |phi|<=1/t0. Integrating the upper bound (1+a)/t0^2 again gives a duration at least 2t0/(1+a). The unit-speed middle is unnecessary for this inequality. Sections 3-4 therefore remain valid with the weaker threshold.

The log contains 62 PASS entries: 57 SAMPLE, two EX, one QUAD, one GRID and one FORMULA. All are numerical diagnostics. In particular, FORMULA tests a few floating-point values around the thresholds; it is not symbolic algebra. The angle h is approximated by a cumulative trapezoid table and interpolation, and the passage times use a numerical ODE solver. The two EX controls replace a/t^2 by constant forcing. The analytic crossing proof above and in the C comparison establishes the universal bound without those samples. The script was not rerun.

LIT355, submitted subsequently, proposes an exact limiting-ratio theorem by a separate tangent-phase argument. The statements here that no exact ratio is proved describe the scope of this growth proof; they do not prejudge that later submission. The new argument is audited separately in exact_switching_asymptotics_20261104. No scalar or Euler conclusion is added. Actual execution of the configured model provider remains independently unattested.
