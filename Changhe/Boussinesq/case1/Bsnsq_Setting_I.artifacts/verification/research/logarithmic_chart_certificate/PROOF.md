# A global positivity certificate for the logarithmic generating chart

Written 2026-10-20T23:44:24.368809+00:00 before implementation. Status: CONFIRMED as the conditional theorem below. Exact J48 certificate and independent source-pinned replay completed before 2026-10-21T00:00:54.680538+00:00. This result concerns a coordinate chart, not the remaining vorticity equation or an A1 existence endpoint.

## Exact statement

Fix alpha>0 and s_e>0. Let P(t,w) be a polynomial with real coefficients. For real x,e define

    E=1+x^2+(e/s_e)^6, T=E^(-1/6),
    t=1-alpha^(-1) log(1+(1-T)(exp(alpha)-1)),
    w=(e/s_e)^2 E^(-1/3), G=x e E^(1/3) P(t,w).

All powers are the positive real powers of E. Put y=G_x and A=G_xe. The compact set

    D = {(t,w): 0<=t,w<=1, T(t)^6+w^3<=1},
    T(t)=(1-exp(-alpha t))/(1-exp(-alpha)),

contains the image of every finite (x,e), with t>0 there. Define

    v=w^3, z=1-T(t)^6-v,
    l=-(exp(alpha t)-1)/(6alpha),
    l2=exp(alpha t)(exp(alpha t)-1)/(36alpha).

For the following coefficients, with all polynomial derivatives taken at(t,w), set

    C0 = 1+(2z+6v)/3-8zv/3,
    Cw = w(2-2z/3-2v+8zv/3),
    Cww = -(4/3)z(1-v)w^2,
    Ct = (2z+6v-4zv)l+12zv l2,
    Ctw = 4zw l(1-2v),
    Ctt = 12zv l^2,
    Q = C0 P+Cw P_w+Cww P_ww+Ct P_t+Ctw P_tw+Ctt P_tt.  (1)

Then the exact identity A=E^(1/3) Q(t,w) holds at every real(x,e). If a finite certificate establishes Q>=delta>0 on D, then(x,e)->(x,G_x(x,e)) is a global smooth diffeomorphism of R^2. In fact A>=delta everywhere. It preserves the relevant reflection symmetries: G is odd in each variable, y is even in x and odd in e, and the unique inverse e(x,y) is even in x and odd in y. The theorem permits any s_e>0 with the same coefficient polynomial P; its positivity certificate is independent of that scale. It makes no assertion about the remaining vorticity PDE or the canonical inverse.

## Derivation of the compact formula

For E treated as an independent variable with e fixed, write L=E partial_E. Then

    L t=l, L l=l2, L w=-w/3.

The first identity follows by direct differentiation of the logarithm; solving its defining equation gives the displayed T(t). Substituting exp(alpha t) then gives l and l2. Put H=P/3+l P_t-w P_w/3. Direct differentiation in x gives

    G_x=e E^(1/3) J, J=P+2zH,

since z=x^2/E at a physical mixed-coordinate point. At fixed x, logarithmic e differentiation satisfies

    e partial_e E=6vE,
    e partial_e z=-6zv,
    e partial_e t=6vl,
    e partial_e w=2w(1-v).

The scale s_e is constant and cancels from each displayed dimensionless identity. Differentiating the prefactor e E^(1/3) therefore gives

    A/E^(1/3)=(1+2v)J+e partial_e J,
    e partial_e J=6vl P_t+2w(1-v)P_w-12zvH+2z e partial_e H,
    e partial_e H=6v[(l/3+l2)P_t+l^2 P_tt-lw P_tw/3]
                   +2w(1-v)[l P_tw-w P_ww/3].

Expansion and collection of the six derivatives of P yields(1). The formulas at e=0 follow by continuity of the original smooth functions. Since x^2/E+(e/s_e)^6/E+1/E=1, z=1-w^3-T^6. Conversely, at every(t,w) in D with t>0, E=T(t)^(-6), x=sqrt(zE), and e=s_e sqrt(w E^(1/3)) give a nonnegative mixed point with exactly those compact coordinates. Sign reflection supplies the other quadrants.

## From positivity to the global chart

The functions E,t,w,G are smooth on the whole mixed plane. Their displayed parities follow because E,t,w are even in both x and e. If Q>=delta on D, then A=E^(1/3)Q>=delta. For fixed x, y(x,0)=0 and

    y(x,e)=integral_0^e A(x,s) ds.

Consequently y(x,e)>=delta e for e>=0, and y(x,e)<=delta e for e<=0. It is strictly increasing, tends to positive infinity as e tends to positive infinity and to negative infinity as e tends to negative infinity. Thus it is bijective for each x. The ordinary implicit function theorem, applied at each point where A>0, gives a smooth local inverse; uniqueness identifies the local inverses on their overlaps and gives a smooth global inverse. Reflection of the defining equation and uniqueness prove the inverse parities. The map and its inverse fix x, completing the diffeomorphism proof.

## Exact finite certificates

Here alpha and P's coefficients are rational. Any binary64 coefficient array can be interpreted exactly as dyadic rational data; no decimal rounding is needed. A certificate partitions[0,1]^2 into finitely many dyadic rectangles, by repeatedly bisecting either coordinate. Each leaf is justified in one of two ways:

1. A rational lower bound on T(t_left)^6+w_left^3 is strictly greater than1. Monotonicity of T and w^3 proves the rectangle is outside D.
2. Exact rational interval arithmetic applied to(1), with valid bounds for P and its derivatives on that rectangle and for the exponential factors, gives a lower endpoint at least delta>0.

For the second test, z can be intersected with[0,1], since only the part of the rectangle in D matters. A positive result on each such intersection proves Q>=delta on D. Empty intersections may instead be discarded under test1. No positive conclusion follows from incomplete coverage, finite samples, or an interrupted tree.

Polynomial bounds can be obtained from tensor Bernstein coefficients. On a rectangle with side lengths h_t,h_w, the first t derivative has coefficients n(b_(i+1,j)-b_(i,j))/h_t, the second has n(n-1)(b_(i+2,j)-2b_(i+1,j)+b_(i,j))/h_t^2, and the mixed derivative has nm(b_(i+1,j+1)-b_(i+1,j)-b_(i,j+1)+b_(i,j))/(h_t h_w). The w formulas are analogous. Each tensor Bernstein basis is nonnegative and their sum is one, so each derivative lies between the least and greatest corresponding coefficients. These identities follow by differentiating b_(n,i)(s)=binomial(n,i)s^i(1-s)^(n-i) and telescoping. A derivative of order exceeding the polynomial degree in that variable is identically zero. The declared tensor degrees must be at least the two degrees of P.

The initial Bernstein array is obtained exactly from P. For a power monomial t^r in degree n its coefficients are binomial(i,r)/binomial(n,r) for i>=r and zero otherwise. To prove this, use binomial(n,i)binomial(i,r)=binomial(n,r)binomial(n-r,i-r), factor out t^r, and sum the binomial expansion of(t+1-t)^(n-r). Apply the identity in both variables. Shifted Chebyshev polynomials may first be expanded with C0=1,C1=2t-1,C_(j+1)=2(2t-1)C_j-C_(j-1), so no transcendental conversion is involved. Repeated midpoint de Casteljau averaging gives the exact child coefficients: the subdivision identity follows from substituting s/2 or(1+s)/2 into the Bernstein basis and applying the same binomial formula.

For a nonnegative rational u, exp(u) lies in the rational interval

    [S_N(u), S_N(u)+a_(N+1)/(1-u/(N+2))],
    S_N=sum_(j=0)^N u^j/j!, a_(N+1)=u^(N+1)/(N+1)!,

provided u<N+2. Every later ratio of consecutive Taylor terms is at most u/(N+2), so the geometric majorant proves the upper bound. Reciprocal intervals give exp(-u). Since alpha>0, the denominator1-exp(-alpha) has a positive enclosure once the chosen N proves it; otherwise the procedure must increase N or return OPEN. Interval addition, multiplication, division by nonzero intervals and positive integer powers are inclusion-preserving. One may replace any rational interval [a,b] with [floor(2^k a)/2^k,ceil(2^k b)/2^k] for a fixed positive integer k. Integer floor and ceiling enlarge the interval, so this directed dyadic rounding preserves inclusion while limiting denominator growth. Together these facts prove soundness of every leaf test above. The certificate states a single rational delta and the replay must check that every positive leaf has lower bound at least delta. It is valid to choose delta after constructing the finite tree, provided the claimed bound is then checked on every leaf; this is an exact inequality, not statistical inference. A replay must independently check the rational inputs, transformations, leaf bounds and complete dyadic coverage.

## Dependencies and scope

The proof uses elementary differentiation, the one-variable fundamental theorem of calculus, the implicit function theorem, finite polynomial identities and a geometric Taylor-remainder bound. Numerical sampling does not prove positivity. Positive far-chart Q alone does not provide this finite-radius certificate. A certificate for a stored function also does not certify that a nearby corrected profile exists. Formal compilation is not permitted in this run; any computer certificate will be exact rational data with a separately written replay.

## Verified application to the frozen J48 data

The file candidate_audits/lead_snap48/sources/snap_J48K26.npz has SHA256 9bce8206006c6541a460045691580ef09c63d7e3952b0e1dcf4de913ed4bfca0. Its 1323 real binary64 coefficients define the exact dyadic polynomial P with tensor degrees 48 and 26, full c0 convention and flat C-order index n*27+k. Take alpha=3 and s_e=1. Exponent fractions and exp(3) in this statement denote exact real numbers, not the rounded floating-point constants used during evaluation.

The completed tree has 705 leaves: 10 outside the physical domain and 695 with positive bounds. A separately implemented exact replay proves Q>=1/100000 everywhere on D and verifies all 1323 polynomial coefficient identities against the pinned NPZ. Thus A>=1e-5 E^(1/3) and the global chart theorem applies. The source-bound replay, complete certificate, rational inputs, manufacture records and hash chain are identified in AUDIT.md. No bound on robustness under coefficient perturbations has been computed.

The archived lead model interprets this file using these basis conventions and absent-parameter defaults. The archived gsolve.py is a later version which also writes se and gam; it is not claimed to be the historical producer of this NPZ. Direct source reading and ten raw high-precision comparisons establish the current interpretation. The exact-center PDE audit uses this same rational-beta3 mathematical interpretation. The finite source-link evaluations corroborate the interpretation but are not the proof of the convention. The chart certificate does not change that file's nonzero center PDE defect.
