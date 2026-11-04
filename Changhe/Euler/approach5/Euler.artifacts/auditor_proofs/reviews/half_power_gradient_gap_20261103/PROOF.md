# Half-power gradient growth and uniform derivative decay

Status: PROVED at the exact A498 CONFIRMED scopes in Section1. The focused configured-model comparison is read in full, and its remaining local-estimate questions are resolved explicitly in Section11. No gradient-growth hypothesis is derived from velocity decay alone.

## 1. Two exact statements

Let0<c<1 and let omega be any finite real number. Set J(y1,y2,y3)=(-y2,y1,0),A=cI-omega J,L=(1-c)I+omega J. Suppose U in C2(R3;R3),P in C1(R3) satisfy

    div U=0, LU+DU(Ay+U)+grad P=0.

Either of the following hypotheses suffices for DU(y)->0 uniformly:

(A) U is bounded and DU(y)=o(|y|^(1/2)) uniformly.
(B) U(y)->0 uniformly and ||DU(y)||<=C0(1+|y|)^(1/2) for some finite C0.

Under(A), the actual grad P is bounded. Under(B), grad P tends uniformly to0. No smallness restriction is imposed on C0 in(B). Constants may depend on c,omega and the profile. No pressure gauge, helicity, symmetry, finite energy or vorticity integrability is assumed. The rotation is arbitrary and no estimates uniform over omega are asserted.

After DU->0 is proved, A476 and A492 give Dini derivative decay and DU=O(1/r). If U tends uniformly to0 and1/3<c<1, A477 gives DU=O(r^-1/c). These corollaries are not used to prove(A) or(B). No nonexistence in2/5<c<1/2 or unconditional C2 basin coverage follows.

Write G=DU,W=curl U,B=Ay+U,M=sup|U|. In both cases M<infinity and G=O(sqrt r). If M=0 all conclusions are immediate, so assume M>0. The actual equation makes grad P C1. All asymptotics below are uniform on spheres and balls with radius a fixed small fraction of their distance to0.

## 2. A single pressure-gradient field and its growth barrier

Divergence of momentum, with exact cancellation of the two skew contributions, gives

    f=Delta P=-tr(G^2)=-partial_i partial_j F_ij,
    F_ij=U_i U_j.

Here F is bounded,f=O(1+r), and momentum initially gives grad P=O((1+r)^(3/2)). Let N=-1/(4pi|x|),Delta N=delta0, and N_d=chi(x/d)N with a fixed smooth cutoff equal to1 near0 and supported in radius2. Define for every d>0

    Q_d=grad N_d*f-partial_i partial_j grad(N-N_d)*F_ij. (1)

The first kernel is compactly supported and locally integrable, of L1 norm at most C d. The second is smooth near0 with integrable O(|x|^-4) tail and L1 norm at most C/d. Thus both convolutions are continuous. Let a_d=Delta N_d-delta0, a compact smooth annular kernel. Distributional differentiation and the equation for f give

    div Q_d=f+a_d*f+partial_i partial_j a_d*F_ij=f,
    curl Q_d=0.

For curl, commute the derivatives on the kernel; the differentiated far kernels remain L1. No convolution of a nonintegrable potential kernel is invoked. For two cutoffs, N_d-N_e is smooth and compactly supported away from0; integrating by parts against it and using f=-partial_i partial_j F_ij gives Q_d=Q_e. Denote this one field by Q.

At |y|=R choose d=R^-1/2 to obtain Q=O(sqrt R). Under(A), for every epsilon>0 and large R use d=epsilon^-1 R^-1/2 and |f|<=C epsilon^2 R on the sampled ball to get |Q(y)|<=C(1+M^2)epsilon sqrt R. The threshold may depend on epsilon, while C does not. Thus Q=o(sqrt R) under(A).

By the zero divergence and curl above, grad P-Q is an entire harmonic vector distribution. Interior second-derivative estimates on growing balls give O(R^-1/2), so it is affine, Ky+b. Evaluate momentum at y=Rz and divide by R on a fixed annulus. Bounded U implies G(Rz)=D_z(U(Rz)/R)->0 in distributions, hence G(Rz)Az->0 distributionally. The other nonlinear term GU/R is O(R^-1/2), as is Q/R, and the bounded linear terms divided by R vanish. Therefore K=0. We have established

    grad P=b+Q,
    p(R):=sup_(|y|<=R)|grad P(y)|<=C(1+sqrt R).       (2)

Under(A), grad P=o(sqrt r). The constant b has not been discarded. The finite growth barrier(2) is crucial to the outward iteration later.

## 3. The actual carrier direction and a bounded quadratic source

Outside a sufficiently large sphere, |B|>=cr/2. Define

    e=B/|B|, P_e=I-e tensor e,
    T=P_e G P_e, g=P_e G^T e, h=Ge, sigma=W.e.

The letter T here denotes the tangential block, not time. Exact differentiation and momentum give

    h=-(LU+grad P)/|B|,
    |h|<=C(1+p(r))/r,
    De=P_e(A+G)/|B|.                                (3)

Initially |g|=O(sqrt r),|h|=O(r^-1/2),|De|=O(r^-1/2) with fixed finite constants. The algebra is

    G=T+e tensor g+h tensor e,
    W=g cross e+e cross h+sigma e,
    g.W=(P_e W).h, e.GW=W.h,
    tr(G^2)=tr(T^2)+2g.h+(e.h)^2.                   (4)

To check every sign, take e=e3 and

    G=((a,b,h1),(d,f,h2),(g1,g2,h3)),
    W=(g2-h2,h1-g1,d-b).

Then g.W=g2 h1-g1 h2=(P_e W).h, and e.GW adds h3(d-b), exactly W.h. The fixed initial g,h bounds imply the noncircular estimate

    |f(y)|<=C(1+|T(y)|^2).                          (5)

The coefficient C is fixed before any later small epsilon is chosen. Compact sets can be absorbed in finite constants.

Along B, D_B e=-omega Je+P_e h. Vorticity transport and skewness give

    B sigma=-sigma+e.GW+W.P_e h,
    |e.GW+W.P_e h|<=C|G||h|.                       (6)

A second consequence of(4), stronger than an additive forcing bound, is

    B|W|<=-[1-|T|-2|h|]|W|.                        (7)

Indeed W.GW=W.TW+(W.e)(g.W)+(W.h)(W.e), and each last term is bounded by |h||W|^2. Zeros are invariant by the linear vorticity ODE; comparison applies on every characteristic including zero data.

## 4. Complete exterior segments and estimates for sigma

The C1 carrier has linear growth and is complete. With r=|Y(t)|, cr-M<=r'<=cr+M. Every sufficiently exterior point has a finite backward crossing of a fixed sphere S>2M/c, since backward radial decay is at least exponential while it stays outside. Write k=M/c. On a forward segment from that sphere,

    k+(S-k)e^(ct)<=r(t)<=(S+k)e^(ct)-k,
    r(t)/r(s)<=3e^(c(t-s)), 0<=s<=t.               (8)

The number3 is independent of S>2k. Integrating(6) and using monotonicity of p gives under(B), and initially in either case,

    |sigma(y)|<=C(1+p(R))R^-1/2, |y|=R.            (9)

This follows because the source is at most C(1+p(R))r^-1/2 and1>c/2. The bounded sphere data contribute O(R^-1/c), which is smaller.

Under(A), for any epsilon>0 choose S sufficiently large that |G|<=epsilon sqrt r outside it. The same convolution with its uniform constant3 gives

    |sigma(y)|<=C_epsilon R^-1/c
                 +C epsilon(1+p(R))R^-1/2.

For all sufficiently large R, the first term is at most epsilon R^-1/2. Increasing that threshold also gives from(3)

    |sigma|+|h|<=C epsilon(1+p(R))R^-1/2,
    |De|<=C epsilon R^-1/2.                        (10)

The coefficient C is independent of epsilon; the thresholds and initial-data constants need not be. More generally, if a source is o(r^-theta) and damping beta>c theta, the same argument yields a uniform o(r^-theta) bound: choose a large sphere with source coefficient epsilon, bound the convolution by C epsilon r^-theta, let the sphere term decay faster, then send epsilon to0 after the limsup.

## 5. Local Holder control with the correct exponential coefficient

Both hypotheses imply

    log(2+[G]_(1/2,B(y,R/8)))<=C sqrt R.             (11)

Under(A), its left side is o(sqrt R). We give the common proof with its coefficient dependence. Put tau=1-t,s=-log tau,Q_s=exp(omega sJ),y=exp(sA)x. The physical fields

    u=tau^(-(1-c))Q_s U(y), xi=tau^-1 Q_s W(y)

satisfy Euler, |u|<=M tau^(-(1-c)), and on1/16<|x|<16 have

    |grad u|<=l(t), |xi|<=w(t),
    l(t),w(t)<=C_e tau^(-1-c/2).                   (12)

Under(B), C_e is fixed. Under(A), for each epsilon>0 a late initial time t0 makes C_e=C epsilon, with C independent of epsilon and t0. Every finite preterminal physical flow is complete, since velocity is bounded and locally C1.

For a ball E near the unit sphere and a margin0<d<=1/16 within the inner annulus, the local estimate is

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
       +Cw d^-1/2(1+log(1/d))+CZ,
    Z=M tau^(-(1-c))+w.                            (13)

Here is a direct justification. Subtract BS(chi0 xi), with a fixed cutoff supported in the annulus of(12) and equal to1 on1/8<|x|<8. Its degree-minus-two kernel bounds the field by Cw. Since -Delta u=curl xi, the remainder is harmonic on the smaller annulus, even though chi0 xi need not be divergence free; its first two derivatives are bounded by CZ. A second cutoff within E+d gives a degree-minus-three derivative kernel of zero spherical mean. Subtraction of values in its near part yields C[xi]_(1/2,E+d)+Cw d^-1/2 by integrating r^-1/2. For the exterior part at distance d/2, the supremum is Cw(1+log(1/d)) and its Lipschitz constant is Cw/d. Interpolation gives the remaining term of(13). No global gradient or vorticity bound enters.

Take t0 still later so(2M/c)(1-t0)^c<=1/8. For every |xstar|=1 put r0(t)=1/4+(2M/c)(1-t)^c,Theta(t)=[xi(t)]_(1/2,B(xstar,r0(t))). Paths ending there lie at earlier q in the ball enlarged by

    d(q,t)=(M/c)((1-q)^c-(1-t)^c),
    M(t-q)<=d(q,t)<=1/16,
    r0(q)=r0(t)+2d(q,t).

All those balls and joining line segments stay in the fixed annulus. Let E0(t)=exp(integral_(t0)^t l). Backward Gronwall bounds earlier pair separation by E0(t)/E0(q) times its terminal value. Integrating the difference of xi'=(grad u)xi along the pair and using(13) with the remaining margin gives

    Theta(t)<=E0(t)^1/2 Theta(t0)
      +integral_(t0)^t (E0(t)/E0(q))^1/2
          [(l+Cw)Theta+Cw^2 ell(t-q)+CwZ](q)dq,
    ell(v)=v^-1/2(1+|log v|).                       (14)

The ell term is evaluated at t-q. Its kernel is integrable. The actual finite Holder seminorms are locally bounded and Borel before t=1, and their initial values are uniformly finite by compact C2 regularity. Divide by E0^1/2. The inhomogeneous term is at most C_(epsilon,t0)tau^-4, since2+c<3<4. Integral Gronwall and integral(l+Cw)<=C_c C_e tau^-c/2 give

    Theta(t)<=C_(epsilon,t0)tau^-4
                       exp(C_* C_e tau^-c/2).      (15)

C_* does not depend on epsilon or t0. Initial norms enter only the prefactor. Apply(13) at a fixed margin on B(xstar,1/8) and rescale with tau=R^-1/c. The exact seminorm factor is tau^(1+c/2), proving(11). Under(A), divide the logarithm by sqrt R, take its limsup, obtain at most C epsilon, then let epsilon->0. This proves the little-o version without requiring control of the initial prefactor uniform in epsilon.

The projected velocity V=U-e(e.U) is C2 outside the sphere. DV is algebraic and linear in G with coefficients from U,e,|B|^-1. On B(y,R/8), the bounds |B|>=cR/4, bounded U and G=O(sqrt R) control these coefficients and their Holder seminorms by polynomial factors times1+[G]_(1/2). The same logarithmic bounds(11), including its little-o version, therefore hold for [DV]_(1/2) and for the divergence and antisymmetric derivative data of smooth cutoffs of U or V. No pressure seminorm is used.

## 6. Projection eliminates the large shear

Let q=U.e,V=U-qe. Differentiation, with(4), gives exactly

    grad q=G^T e+(De)^T U,
    div V=-e.h-U.(D_e e)-q div e,
    curl V=e cross h+sigma e-((De)^T U) cross e-q curl e.

The large g cross e term cancels. Hence

    |div V|+|curl V|<=C(|h|+|sigma|+|U||De|).       (16)

This is an identity in Euclidean coordinates with e=B/|B|; it assumes no integrability of an orthogonal plane distribution.

For a C2 field v cut off inside a radius2ell ball with cutoff1 in radius ell, let F collect its divergence and antisymmetric derivatives. Put K=[F]_(1/2),epsF=||F||infinity. The compact-support vector Laplacian formula yields

    |Dv(0)|<=C[K eta^1/2+epsF(1+log(2ell/eta))],
    0<eta<=1.                                     (17)

Indeed second Newtonian derivatives have a bounded local term and a degree-minus-three kernel with zero spherical mean. Subtract F(0) inside radius eta to obtain CK eta^1/2 and use its supremum between eta and2ell. Compact support removes the harmonic ambiguity.

Take ell=R/32 and eta=(R^2 max(1,K))^-2. The first term is at most R^-2. Under(B), (3),(9),(16) and cutoff error O(M/R) give epsF<=C(1+p(2R))R^-1/2; (11) bounds the logarithm by C sqrt R. Thus |DV|<=C(1+p(2R)). Projecting the exact derivative gives

    P_e(DV)P_e=T-q P_e(De)P_e,
    |T(y)|<=C(1+p(2R)) under(B).                  (18)

Under(A), (10) supplies epsF<=C epsilon(1+p(2R))R^-1/2. After a larger threshold, the logarithm in(17) is at most C epsilon sqrt R by the little-o version of(11) and log R<=epsilon sqrt R. The qDe term tends to0 independently. Therefore

    |T(y)|<=1+C epsilon^2(1+p(2R)) under(A).        (19)

All C in(19) are independent of epsilon, whereas its validity threshold may depend on epsilon.

## 7. Two pressure contractions and the same noncircular iteration

For a sufficiently exterior y of radius R put K_y=1+sup_(|z-y|<=2)|T(z)|. In(A), choose d=1/K_y<=1 in the same field(1). Equation(5) gives |f|<=C K_y^2 on its near support. The two L1 bounds imply

    |grad P(y)|<=|b|+C d K_y^2+C M^2/d<=D0 K_y.

Use(19) in the radius2 ball, with p(2|z|)<=p(4R). It follows that |grad P(y)|<=C1+C2 epsilon^2 p(4R), with constants independent of epsilon. Taking a ball supremum and absorbing the compact inner region yields

    p(R)<=C_epsilon+q p(4R), q=C2 epsilon^2.        (20)

Choose one epsilon with q<1/2.

For(B), instead let m(R)=sup_(|z|>=R)|U(z)|->0 and mu_R=m(R/2)+R^-1. For large R choose d=mu_R/K_y<=1. The near contribution in(1) is at most C d K_y^2. Split the far convolution at |y-z|=R/2. On its inner part |U(z)|<=m(R/2), giving C mu_R^2/d. On its outer part the kernel is O(|y-z|^-4) and F is bounded, giving C M^2/R. Thus

    |Q(y)|<=C mu_R K_y+C M^2/R.                    (21)

There is no change to Q or its harmonic ambiguity. By(18), K_y<=C(1+p(4R)), so the actual pressure obeys |grad P(y)|<=|b|+C mu_R(1+p(4R))+C M^2/R. Choose a sphere S so C mu_R<=q<1/2 for every R>=S, and take the ball supremum. Compact values inside S are finite, giving

    p(R)<=C_S+q p(4R), R>=S.                       (22)

In either case iterate the established inequality n times. Its remainder q^n p(4^n R) is bounded, by the prior growth barrier(2), by Cq^n+C(2q)^n sqrt R, which tends to0. Hence p(R)<=C_*/(1-q) globally after compact adjustment. No supremum of p at infinity was assumed. Equations(18)-(19) and(5) now give bounded T and bounded f in both cases.

## 8. The actual pressure limit in(B)

Under(B), F tends uniformly to0 and f is now bounded. For any fixed d>0, the near convolution(1) has supremum at most Cd||f||infinity, while its far L1 kernel convolved with bounded F tending to0 also tends uniformly to0. Thus limsup_(r->infinity)|Q|<=Cd||f||infinity. Let d decrease to0: Q->0. Equation(2) gives grad P->b.

Choose an exterior B orbit, which escapes by(8). Its actual momentum equation is dU(Y(t))/dt=-LU(Y(t))-grad P(Y(t)). Integrate from t to t+1. Since U tends uniformly to0 along this escaping segment, the left difference tends to0 and the right integral tends to-b. Therefore b=0, proving grad P->0. It follows from(3) that h=o(1/r). This proves the pressure gradient limit without choosing a gauge or claiming a scalar pressure limit.

Under(A), only boundedness of grad P is needed, giving h=O(1/r).

## 9. Tangential decay, homogeneous damping and full derivative decay

Under(A), |G|=o(sqrt r) and h=O(1/r), so the source in(6) is o(r^-1/2). Under(B), |G|=O(sqrt r) and h=o(1/r), giving the same source. The little-o characteristic argument of Section4 gives sigma=o(r^-1/2) in both cases.

Under(A), De=o(r^-1/2) and U is bounded. Under(B), De=O(r^-1/2) and U->0. Thus |U||De|=o(r^-1/2) in either case. Equation(16) gives div V,curl V=o(r^-1/2); cutoff errors are O(1/R), smaller. The common logarithmic Holder bound is O(sqrt R). Estimate(17) with its adaptive eta therefore yields DV->0. The projected identity in(18) and qDe->0 give T->0.

For every fixed beta with0<beta<1, sufficiently far out(7) now gives B|W|<=-beta|W|. The finite exterior segments(8) imply

    |W(y)|<=C_beta r^(-beta/c).                    (23)

For clarity, v(t)<=v(0)e^(-beta t) and r(t)<=C e^(ct) imply this power bound, with bounded initial sphere data; no infinite-time backwards boundary condition is used.

Choose beta>c/2, possible because c<1. A3D cutoff of U on B(y,R/16), equal to1 on B(y,R/32), has divergence and curl supremum at most C[R^(-beta/c)+R^-1], and Holder logarithm at most C sqrt R by(11). Applying(17) gives

    |G(y)|<=R^-2+C[R^(-beta/c)+R^-1]sqrt R->0.

This proves both exact statements. Only now apply A476,A492 and, at its extra decay and parameter scope,A477. Neither proposed main conclusion from LIT121,LIT122,LIT123,LIT124 or LIT125 was imported into the proof.

## 10. Verification status and remaining issue

The full LIT124 and LIT125 sources were read, their pressure and projection identities were independently expanded, and the common proof above records all thresholds and the initial growth barrier needed for the outward iteration. The stronger homogeneous estimate(7) was independently found in the earlier LIT123 audit and checked again in the exact matrix(4). The actual pressure constant in(B) is determined from momentum.

Focused existing configured-model comparison is requested, especially for(20)-(22), the local Holder prefactor dependence, and the absence of an unstated global gradient bound. Coordinator/theory configuration is the primary model, without independent provider runtime attestation. No new model client or computation is used. Faster growth than O(sqrt r) for a decaying profile remains outside these statements and the main conjecture remains open.

## 11. Follow-up on the local Holder estimate

The complete initial coordinator review of LIT125 was read at its133-line version. It agrees with the pressure split, harmonic ambiguity, projection algebra, outward iteration and final homogeneous damping. It leaves the local Holder estimate and its cutoff product estimate only partly checked. Here are the remaining details needed to verify those steps directly.

In(14), put Zeta=Theta/E0^(1/2). Since E0>=1, after division the inhomogeneous integral is bounded above by

    C integral_(t0)^t [w(q)^2 ell(t-q)+w(q)Z(q)]dq.

On q<=t, w(q)^2<=C_(epsilon,t0)tau^(-2-c). The integral of ell over(0,1) is finite. Also wZ is at most a constant times tau^(-2-c)+tau^(-2+c/2). Thus this whole integral, and the finite initial seminorm, are bounded by the nondecreasing function F(t)=C_(epsilon,t0)tau^-4. Ordinary integral Gronwall gives Zeta(t)<=F(t)exp(integral(l+Cw)). Restoring E0^(1/2) changes only the constant multiplying the same integral. Its coefficient C_* in(15) is independent of the initial time and epsilon. No initial seminorm enters that exponential coefficient.

For the pair-separation step, two physical trajectories ending in B(xstar,r0(t)) each move by at most d(q,t). Their earlier positions, and the segment joining them, lie in B(xstar,r0(t)+d(q,t)). This ball has remaining margin d(q,t) inside B(xstar,r0(q)). On it the difference equation uses [grad u] on the inner ball and(13) uses [xi] on the outer ball, which is exactly Theta(q). Backward Gronwall for the pair gives the factor (E0(t)/E0(q))^(1/2). This explains both the moving-ball closure and the exponent in(14).

For the product claim, e=B/|B| has derivative P_e(A+G)/|B|. Every coefficient in DV is a finite sum of products of U,B,|B|^-1 and fixed matrices; all denominators are bounded below by a fixed multiple of R on the ball. B and U have polynomial supremum and Lipschitz bounds from G=O(sqrt R). The product and reciprocal Holder inequalities therefore give [DV]_(1/2)<=C R^N(1+[G]_(1/2)) for some finite N, and the same estimate holds after either specified cutoff. Taking logarithms adds only O(log R). The claimed O(sqrt R), and under(A) o(sqrt R), follow from(11).

The configured-model review is interim only with respect to the later request to read this reconstruction. Its initial list of unchecked details is resolved by the explicit argument above; the follow-up is requested through the existing file exchange. This paragraph does not claim that the reviewer checked material it had not yet read.

## 12. Final comparison and verdict

The complete coordinator review, including its response to all three challenge points, has been read. It agrees with the localized far split, the epsilon-independent constants in(A), and determination of b=0 in(B). It read the full independent reconstruction for those questions; it did not separately read the LIT124 source. Its still-unchecked pair-separation and product details are proved explicitly in Section11 and were independently checked after writing. The initial barrier is used twice, both to bound g.h and to kill the outward iteration remainder; neither use is omitted here.

A498 CONFIRMED certifies both exact statements and their stated downstream consequences. It certifies no unconditional bound on DU from U->0. Precisely, a decaying profile that fails derivative decay must have limsup_(r->infinity)|DU(y)|/sqrt(|y|)=infinity. This necessary growth concerns failure of derivative decay, not every nonzero profile in the target conjecture. No nonexistence conclusion in2/5<c<1/2 is established.
