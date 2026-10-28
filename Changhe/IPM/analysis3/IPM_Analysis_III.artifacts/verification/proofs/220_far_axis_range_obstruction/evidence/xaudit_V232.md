# Independent audit of V232 / proof 220 (far-axis range obstruction in the common Holder target)

Audited file: verification/proofs/220_far_axis_range_obstruction/PROOF.md
sha256: d906b7a274338389c89bf550100256e398df6f7df0ca11901226928d85b6f41f
Evidence: evidence/check.json only (dependency hashes, "computation: none"). I recomputed the seven dependency
hashes (topics 35, 117, 50, 213, 214, 217, 204); all match the current PROOF.md files.
Context read: topics 213, 214, 217 (with their AUDIT_CLARIFICATIONS), 117, 35 (first part), 204 (q construction),
Note81, and the theory author note Far_Y_obstruction.md. Small exponent checks were run in python (no heavy computation).

VERDICT: PASS WITH REMARKS

Summary. The argument is correct. The obstruction mechanism is genuine: the far flow is a dilation at the exact rate
ell=1/k, the bounded solution is forced to be the forward characteristic integral, and the integral of the admissible
strip forcing x^2 phi(x) y^(-b) produces x^(k+b) at a fixed height, while E2 forces O(x^2) there. The nonlocal terms are
controlled along the whole future orbit by O(x^2 log(1/x)) using the exact relation ell k=1. I found no gap. The
remarks below concern justification that is sketched in the text but available from the cited topics, plus typos.

## Findings

1. (remark) Background bound (1). The prose paragraph in the proof is a sketch, but (1) holds rigorously from
   proof 117. There the canonical outer velocity is a finite modal sum, U_r/r=-sum_n P_n cos(2n theta) and
   U_theta/r=sum_n Q_n sin(2n theta), with P_n,Q_n=O(r^(k-1)) and termwise cylinder derivatives. Then exactly
   U1/x=-sum P_n cos(2n theta)-sum Q_n sin(theta) sin(2n theta)/cos(theta) and
   U2/y=-sum P_n cos(2n theta)+sum Q_n cos(theta) sin(2n theta)/sin(theta). Both quotients are trigonometric
   polynomials (sin(2n theta)=sin(theta) U_(2n-1)(cos theta), and U_(2n-1) is odd). Since there are finitely many modes,
   (1) follows uniformly up to both axes. An equivalent route: proof 217 gives U[rho0]=O(r^k) with one cylinder
   derivative, and the mean value theorem in theta from the vanishing axis gives the same division. "No growing
   harmonic velocity" is justified. Proof 117 states that the canonical inverse admits no growing exterior harmonic
   term. Proof 35 and the proof 217 clarification give nonresonance of the homogeneous modal solution at q=k, so
   U[r^k Theta] is exactly homogeneous of degree k and no degree-one linear field can appear. Compact differences
   give decaying multipoles. Suggested repair (editorial): replace the prose with these two citations. Note also
   that along the actual orbits y_t is comparable to r_t, so the U2/y division near the x-axis is needed only to make
   V2/y>=ell/2 on the whole region y>=R, not along the orbits themselves.

2. (remark) Forward characteristics (2). Verified. On y>=R, V2/y>=ell/2 and V1/x>=ell/2. A standard continuation
   argument gives invariance of {y>=R, x>0} (x=0 is invariant by uniqueness, since V is C^1). Global existence follows
   from linear growth. Using r_t>=y_t>=Y exp(ell t/2), the drift errors integrate to at most
   delta_Y=2C Y^(k-1)/(ell(1-k)), uniformly in 0<x<1. So a_Y=exp(-delta_Y) and B_Y=exp(delta_Y), with
   r_t<=x_t+y_t<=2B_Y Y exp(ell t) because x<1<=Y. The exact rate ell is retained, as claimed.

3. (remark) Forcings. F_b is smooth, even in x, odd in y, zero on x=0 and on |y|<=2R. Its sup and x-Holder norms are
   finite. [F_b]_(y,2)=sup phi(x)[g_b]_alpha is finite. The weighted L2 integral needs only 2b+gamma>1, which holds
   for b>1/2 and any gamma>=0. c[F_b] is defined by proof 213 (|c|<=4/pi on E2). D_Y membership is correct:
   T F_b=x^2 G with G=(2V1/x-1)phi g_b+V1 phi' g_b+V2 phi g_b', and G=O(y^(-b)). It does use differentiated
   bounds (d_y(U1/x)=O(r^(k-2)), DU[rho0]=O(r^(k-1))) that are not displayed in (1). These follow from the termwise
   differentiation in proof 117 and proof 217. D_Y membership is a bonus; the cokernel claim needs only f_b in Y. J is
   defined in proof 214 only on C_c^infinity intersect E2, and f_b is not compactly supported. J(f_b)=0 should be read
   as the local jet at 0. That jet vanishes because near 0 we have f_b=-c[F_b]q, and proof 204's q is x^2 y beta(r)
   with beta supported in an annulus inside B_(delta/2). This also makes "q supported below radius R" automatic.

4. (remark) Growth (13) and the contradiction. Verified: Q_b/ell=2-b-k by ell k=1, so
   x^2 exp(Q_b tau_x)=B_Y^(-(2-b-k)) x^(k+b). phi(x_t)=1 for t<=tau_x, and f_b>=0 on the whole orbit with q=0 there
   (r_t>=Y>=3R). The comparison at a fixed height is valid: (15) holds for every x at the same fixed Y, with constant
   M Y^alpha, by oddness in y (h(x,0)=0). So d x^(k+b-2)<=C(1+log(1/x)) fails as x->0. The margin is
   2-(k+b)>1-k>0.82. As a sanity check, a pure-dilation model integral gave fitted exponents 0.7793 (b=0.6) and
   1.0789 (b=0.9), against the predicted k+b=0.7794 and 1.0794.

5. (remark) All-future coupling bound (8),(10). Verified, including the citations. (4) is proof 214 (3)-(4) for E2
   inputs. (5) is proof 214 (10) with rho0_x=x a1 and rho0_y=x^2 a2, |a1|<=C r^(k-2), |a2|<=C r^(k-3), at all
   angles. The divided identity B/x^2=a1(U1/x)+a2 U2 gives the first bound in (6). The log term is absorbed by
   r^(k-3)(1+log r)<=C r^(k-2). Bookkeeping:
   exp(-t) x_t^2 r_t^(k-2)<=C_Y x^2 exp((ell k-1)t)=C_Y x^2 (marginal, exactly because ell k=1), and
   exp(-t) r_t^(k-1)(1+log r_t)<=C_Y(1+t)exp(-ell t). The split at t_x=2 log(1/x)/ell (so that exp(-ell t_x)=x^2)
   gives O(x^2(1+log(1/x))). M0 equals m0 outside supp H0. Proof 217 (6) gives |m0/x^2|<=C r^(2k-3)(1+log r), which
   yields the integrand C_Y M x^2(1+t)exp((1-ell)t) and an O(x^2) contribution. |c[h]|<=4M/pi is from proof 213.
   The proof also notes that small output tails alone would not suffice. That is correct: a generic bound
   min(1, x_t^2 y_t^alpha) only gives an orbit integral of order x^(2k/(2+alpha)), far larger than x^2.

6. (remark) Independence and the three operators. Verified. For a finite combination with least exponent b_*, the
   tail sum dominates for y>=Y_0, so the combined forcing is nonnegative on every orbit from height
   Y>=max(3R,Y_0), and (13) holds with b_*. For L_ren, H0 is compact and zero on the orbits. For T, C=0. The
   algebraic cokernel in fact has dimension at least that of the continuum (all b in (1/2,1)); "infinite" is correctly
   conservative.

7. (remark) Representation (3). Correct. For h in D_Y, Th=V.grad h-h lies in Y and is therefore continuous and bounded
   automatically. The appeal to topics214/217 for continuity of f-C[h] is correct but unnecessary. The flow-box step
   needs V in C^1 (proof 214) and V nonzero on the orbit (V2>=ell y/2>0). Both hold. The endpoint term vanishes
   because h is bounded, and the sign in (14) is right.

8. (remark) Scope and label. The non-claims are accurate and adequate: nothing about F0 being outside the range, no
   nonexistence, no closed-range claim, no statement about other spaces or condition (I). The Fredholm and
   domain-restriction consequences are correct. Recommended label: PROVED (given topics 117, 204, 213, 214, 217):
   "on the common target Y, the actual T, L_ren and A0 on D_Y have infinite-dimensional algebraic cokernel, hence are
   neither onto Y nor Fredholm". Downstream summaries should say "the common target Y is not a valid global target",
   not "no inverse exists". Optional strengthening: the same proof works for any b with max(0,(1-gamma)/2)<b<2-k,
   and for every alpha in (0,1).

9. (typo) Missing spaces: "reaches1", "topics35 and117", "topics213/214" and similar. In (2), "after enlarging B_Y"
   would read better as "with r_t<=x_t+y_t". In (12), the phrase "The bounded strain of (11) is well defined" should
   cite proof 213 statement 1. The phrase "Exact exponent ell is retained" could cite (2) explicitly as the source of
   the marginal factor exp((ell k-1)t)=1 in (7).

## Comparison with Far_Y_obstruction.md

The theory author note proves a different, dual obstruction. Vertical oscillations near the x-axis at large |x| are admissible
in Y with uniformly bounded norm, because the weight x^2 is weak there. The transport carries them back to a fixed
radius with amplification X0^(2+alpha-k). Via closedness and the open mapping theorem, this excludes a bounded
inverse (a bijection) for any T+B where B has small output tails. Proof 220 instead uses a single fixed forcing on a
vertical strip at large heights, where the same weight x^2 is too strong for the dilation. It obtains the stronger,
purely algebraic conclusion of infinite cokernel, with no open mapping argument. However, it needs the specific
pointwise structure of the actual coupling (the x^2 r^(k-2) bound and the M0 decay), not just small tails. The two
results are consistent and point to the same remedy: dilation-scaled far seminorms in place of the global x^2 weight.
