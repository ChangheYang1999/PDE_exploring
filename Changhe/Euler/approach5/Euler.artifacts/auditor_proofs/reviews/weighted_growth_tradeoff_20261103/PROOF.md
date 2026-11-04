# Weighted velocity decay and gradient growth

Status: CONFIRMED in A507 after independent reconstruction, full postread and the complete focused configured-model comparison. This result explicitly assumes a gradient-growth bound and quantitative velocity decay.

## 1. Exact statement and notation

Let0<c<1,omega be any finite real number,J(y1,y2,y3)=(-y2,y1,0),A=cI-omega J,L=(1-c)I+omega J. Suppose U in C2(R3;R3),P in C1(R3) satisfy

    div U=0, LU+DU(Ay+U)+grad P=0.

Fix1/2<delta<1,alpha=2delta-1 and suppose

    |DU(y)|<=C0(1+|y|)^delta, U(y)=o(|y|^-alpha) uniformly.

Then the conclusions are grad P=o(r^-alpha) and DU->0 uniformly. There is no smallness condition on the finite C0. Constants may depend on the profile,c,omega,delta. No helicity, symmetry, finite energy, pressure normalization or uniformity over omega is assumed. The endpoint delta=1 and bare velocity decay are outside the statement.

Write G=DU,W=curl U,B=Ay+U,M=sup|U| and m(R)=sup_(|y|>=R)|U(y)|. M is finite; M=0 is immediate, so take M>0. The hypothesis says m(R)=o(R^-alpha). Actual momentum upgrades grad P to C1.

## 2. Pressure construction and initial growth barrier

The divergence of momentum gives f=Delta P=-tr(G^2)=-partial_i partial_j F_ij,F_ij=U_iU_j. Let N=-1/(4pi|x|),Delta N=delta0,N_d=chi(x/d)N with chi smooth,1 near0 and supported in radius2. Define

    Q_d=grad N_d*f-partial_i partial_j grad(N-N_d)*F_ij.

The two kernels have L1 norms at most Cd,C/d. The first is compact and locally integrable, the second smooth near0 with O(|x|^-4) tail. Both convolutions are continuous. Writing a_d=Delta N_d-delta0 gives div Q_d=f+a_d*f+partial_i partial_j a_d*F_ij=f; curl Q_d=0 by commuting derivatives of the kernels. The far differentiated kernels remain L1. For two positive cutoffs,N_d-N_e is smooth, compact and zero near0, so integration by parts using f=-partial_i partial_j F_ij gives Q_d=Q_e. Denote this single field by Q.

At radius R choose d=epsilon R^(-alpha-delta). For large R, |f|<=C R^(2delta) on the near ball. On the part of the far integral with |y-z|<R/2 use |U(z)|<=epsilon R^-alpha; on its complement the O(|y-z|^-4) kernel gives CM^2/R. Thus

    |Q(y)|<=C d R^(2delta)+C epsilon^2 R^(-2alpha)/d+CM^2/R
           <=C epsilon R^(1-delta)+CM^2/R.

C does not depend on epsilon; the threshold does. Hence Q=o(R^(1-delta)). Initially momentum gives grad P=O(R^(1+delta)). The harmonic vector grad P-Q is affine Ky+b: the interior second derivative bound is C R^(delta-1)->0. Divide momentum at y=Rz by R on a fixed annulus. G(Rz)=D_z(U(Rz)/R)->0 distributionally, so its product with Az tends to0. GU/R=O(R^-delta),Q/R=o(R^-delta), and the bounded linear term divided by R vanish. Therefore K=0 and

    grad P=b+Q, p(R):=sup_(|y|<=R)|grad P(y)|<=C(1+R^(1-delta)). (1)

The actual constant b is retained for now.

## 3. Carrier direction and local analytic estimates

B has linear growth and is complete. Outside a fixed S>2M/c, every point reaches the sphere S at a finite backward time. For forward segments from S, with k=M/c,

    k+(S-k)e^(ct)<=r(t)<=(S+k)e^(ct)-k,
    r(t)/r(s)<=3e^(c(t-s)), 0<=s<=t.                         (2)

These follow from cr-M<=r'<=cr+M; the constant3 is independent of S. Define outside that sphere

    e=B/|B|,Pi=I-e tensor e,T=Pi G Pi,g=Pi G^T e,h=Ge,sigma=W.e.

Direct differentiation and the profile equation give

    h=-(LU+grad P)/|B|, De=Pi(A+G)/|B|,
    D_B e=-omega Je+Pi h,
    G=T+e tensor g+h tensor e,
    W=g cross e+e cross h+sigma e,
    g.W=(Pi W).h, e.GW=W.h.

By(1), h=O(r^-delta), while g=O(r^delta),De=O(r^(delta-1)). Consequently

    |f|<=C(1+|T|^2),                                        (3)

since tr G^2=tr T^2+2g.h+(e.h)^2 and the initial product g.h is bounded independently of later estimates. Vorticity transport gives exactly

    B sigma=-sigma+e.GW+W.Pi h,
    |e.GW+W.Pi h|<=C|G||h|,
    B|W|<=-[1-|T|-2|h|]|W|.                                 (4)

The last bound is homogeneous; at zeros use the linear characteristic equation. For q=U.e,V=U-qe,

    div V=-e.h-U.D_e e-q div e,
    curl V=e cross h+sigma e-((De)^T U) cross e-q curl e,
    Pi(DV)Pi=T-q Pi(De)Pi.                                  (5)

Thus the large g shear cancels from the divergence and curl of the bounded field V.

We also need the explicitly local estimate

    log(2+[G]_(1/2,B(y,R/8)))<=C R^delta.                     (6)

Here is its proof, rather than assuming a derivative bound beyond the hypotheses. For tau=1-t,s=-log tau,Q_s=exp(omega sJ),y=exp(sA)x, the physical fields u=tau^(c-1)Q_s U(y),xi=tau^-1 Q_s W(y) solve Euler. On a fixed annulus around the unit sphere, |grad u|<=l(t),|xi|<=w(t),l+w<=C tau^(-1-cdelta), while globally |u|<=M tau^(c-1). Finite preterminal flows are complete. A local Biot-Savart cutoff and harmonic remainder give, on a ball E with margin d,

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
       +Cw d^-1/2(1+log(1/d))+C(M tau^(c-1)+w).

The near mean-zero kernel uses subtraction of values; the distant kernel has supremum Cw(1+log(1/d)) and Lipschitz constant Cw/d. Interpolation gives the displayed margin error. The fixed annular cutoff need not be divergence free because the remainder is harmonic by -Delta u=curl xi.

For xstar on the unit sphere take r0(t)=1/4+(2M/c)tau^c,Theta(t)=[xi]_(1/2,B(xstar,r0(t))), and late t0 so all balls stay in the annulus. Paths ending in this ball move backwards by at most d(q,t)=(M/c)((1-q)^c-tau^c), with d>=M(t-q) and r0(q)=r0(t)+2d. The remaining margin is d. Pair separation costs (E0(t)/E0(q))^(1/2),E0=exp(integral l). Subtracting xi'=(grad u)xi along pairs therefore gives, after dividing by E0^(1/2), a Gronwall coefficient l+Cw and an inhomogeneous integral bounded by

    C integral_(t0)^t [w(q)^2 ell(t-q)+w(q)(M(1-q)^(c-1)+w(q))]dq,
    ell(v)=v^-1/2(1+|log v|).

Since ell is integrable and2+2cdelta<4, this is at most C tau^-6. Thus Theta<=C tau^-6 exp(C tau^-cdelta). A fixed-margin application of the local estimate and rescaling by the exact seminorm factor tau^(1+c/2),with tau=R^-1/c, proves(6). Products in DV have polynomially controlled coefficients in U,B,|B|^-1 and fixed matrices, so(6) also holds for DV and cut-off divergence/curl data. No pressure seminorm or global vorticity bound is used.

For a field v cut off inside radius2ell, let F collect div v and its antisymmetric derivatives,K=[F]_(1/2),epsF=||F||infinity. The compact Newtonian formula gives

    |Dv(0)|<=C[K eta^1/2+epsF(1+log(2ell/eta))].              (7)

Near eta subtract F(0) in the mean-zero second derivative kernel; outside integrate epsF dr/r. The local distributional term is bounded by C epsF. Compact support removes the harmonic ambiguity. For ell=R/32 and eta=(R^2 max(1,K))^-2, the near term is at most R^-2 and(6) bounds the logarithm by C R^delta.

## 4. First outward iteration

On an exterior segment with radii at most R, (4)'s scalar source is bounded by C(1+p(R))r^(delta-1). Damping1>c(1-delta) and(2) therefore give sigma<=C(1+p(R))R^(delta-1); the initial sphere term is O(R^-1/c), smaller. Equations(5)-(7), including the smaller cutoff error O(M/R), give

    |T(y)|<=C R^alpha(1+p(2R)).                              (8)

For K_y=1+sup_(|z-y|<=2)|T(z)| and mu_R=m(R/2)+R^-1 choose d=mu_R/K_y in the same Q. For large R, d<=1. By(3), its near contribution is at most C d K_y^2. Split the far convolution at |y-z|=R/2; its inner contribution is C mu_R^2/d, its outer contribution CM^2/R. Thus

    |Q(y)|<=C mu_R K_y+CM^2/R,
    K_y<=C R^alpha(1+p(4R)).                                (9)

Because R^alpha mu_R->0, for any fixed small q>0 and all sufficiently large R, a ball supremum gives p(R)<=C_S+q p(4R), absorbing all compact values in C_S. Iteration has remainder q^n p(4^n R), which tends to0 by(1) if q4^(1-delta)<1. Therefore p is bounded. By(8), T=O(R^alpha). Substitution into(9) gives Q->0. Thus grad P->b. On an escaping B trajectory integrate dU/dt=-LU-grad P from t to t+1. Uniform U->0 makes the left difference and LU integral vanish, forcing b=0. No pressure gauge is chosen.

## 5. Weighted second iteration

Set w_*(R)=sup_(|y|<=R)(1+|y|)^alpha |grad P(y)|. Bounded p supplies the prior growth barrier w_*=O((1+R)^alpha). On an exterior segment with radii r<=R,

    |h|<=C(1+w_*(R))r^(-1-alpha)=C(1+w_*(R))r^-2delta.

The scalar source in(4) is at most C(1+w_*(R))r^-delta. Since1>cdelta, characteristic integration gives sigma<=C(1+w_*(R))R^-delta. Also |U||De|<=C R^-delta. The logarithmic estimate(7) now gives the stronger

    |T(y)|<=C(1+w_*(2R)).                                   (10)

Use(9) and b=0. Multiplying by R^alpha yields

    R^alpha|grad P(y)|<=C R^alpha mu_R(1+w_*(4R))+CM^2 R^(alpha-1).

Here alpha<1 and the first coefficient tends to0. Taking a ball supremum gives w_*(R)<=C_S+q w_*(4R). Choose q4^alpha<1; the prior growth barrier makes its outward remainder vanish. Hence w_* and T are bounded. With bounded K_y, (9) now implies grad P=Q=o(R^-alpha), since both mu_R=o(R^-alpha) and R^-1=o(R^-alpha).

Both growth barriers were proved before they were used. The second iteration is necessary: the first left T=O(R^alpha), not bounded.

## 6. Derivative decay and scope

The pressure rate and velocity hypothesis give h=o(R^-2delta). The scalar source in(4) is o(R^-delta), so sigma=o(R^-delta): start outside a sphere with source coefficient epsilon, integrate using1>cdelta and(2), then discard the faster R^-1/c sphere term and send epsilon to0. Also |U||De|=o(R^-delta). Equation(5) gives cut-off div/curl data o(R^-delta), with velocity cutoff error o(R^-2delta). Its product with the logarithm C R^delta in(7) tends to0. Thus DV->0 and T->0.

Choose cdelta<beta<1. Outside a larger sphere (4) gives B|W|<=-beta|W|. Finite exterior segments and bounded sphere data give W=O(R^-beta/c). Cutting off U itself, its div/curl data are O(R^-beta/c)+o(R^-2delta). Applying(7) gives

    |G(y)|<=R^-2+C R^(delta-beta/c)+o(R^-delta)->0.

Only after this step may one apply A476,A492 and, with1/3<c<1,A477 for the stated downstream rates. The main proof does not import the proposed main conclusions of LIT124 or LIT125. It shares explicitly proved local identities with them. A power bound U=O(r^-gamma) suffices when gamma>2delta-1; the equality requires little-o as stated. No bound on DU follows here from velocity decay alone.

## 7. Verification status

The full246-line source was read and pinned. The two pressure growth barriers, weighted supremum, actual constant b, characteristic completeness, homogeneous damping and local Holder exponent have been independently reconstructed above. No mathematical gap was found on this reconstruction. The full independent proof was read after writing with no gap found. The complete focused configured-model review, including its completed comparison to this reconstruction, was read and agrees on all exponents and both contractions. Existing coordinator/theory configuration names the primary model, without independent provider runtime attestation. No new model client or computation is used.

## 8. Details from the completed focused comparison

The inhomogeneous bound in Section3 can be sharpened to C tau^(-2-2cdelta), hence C tau^-4, before Gronwall: for q<=t, w(q)^2<=C tau^(-2-2cdelta), and ell has a finite integral on the fixed time interval. The other term w M(1-q)^(c-1) is bounded by the same larger power because w<=C(1-q)^(-1-cdelta) and c>0. The stated tau^-6 is a harmless overestimate. No initial-data constant enters the coefficient of the terminal exponential.

For the product seminorm, on the local radius-R ball,

    |B|^-1=O(R^-1), |G|=O(R^delta), |De|=O(R^(delta-1)),
    [e]_(1/2)<=C R^(delta-1/2),
    [|B|^-1]_(1/2)<=C R^(delta-3/2),
    [U]_(1/2)<=C R^(delta+1/2).

These follow from the mean-value estimate times the square root of the ball diameter. Formula (5) for DV, with De=Pi(A+G)/|B|, is linear in G and has coefficients formed from bounded U, e, |B|^-1 and fixed matrices. Their suprema and seminorms have polynomial bounds by the displayed estimates. Therefore [DV]_(1/2)<=C R^N(1+[G]_(1/2)) for some fixed finite N, as do the cut-off data. Taking logarithms gives C log R+C R^delta, which is at most C'R^delta. No pressure seminorm appears and no bounded projected gradient is assumed here.

The first iteration is used in this proof to establish b=0. Once b=0 is supplied independently by A031 or A500, the weighted envelope already has the prior bound O(R^delta) from (1), which also suffices for its contraction if q4^delta<1. Thus there is no claim that this particular pair of barriers is the only valid proof organization. LIT127 uses that observation to treat a wider range and remains a separate claim.

The original source, entire final focused review and source hashes are retained in verification. The comparison calls the reconstruction close to the source; it is a rederivation and audit of that argument, not a claimed alternative method. The two explicit estimates above complete the previously abbreviated local details.
