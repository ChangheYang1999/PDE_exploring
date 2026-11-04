# Gradient growth below the one-third exponent forces boundedness

Status: A495 CONFIRMED at the exact hypotheses below after independent reconstruction and the complete focused configured-model coordinator review. This is a theorem under an explicit polynomial gradient-growth hypothesis, not a derivation of that hypothesis from decay of velocity.

## 1. Exact statement

Fix0<c<1 and arbitrary omega in R. Write J(x1,x2,x3)=(-x2,x1,0),A=cI-omega J,B=Ay+U,G=DU,W=curl U. Let U in C2(R3;R3),P in C1(R3) solve

    div U=0, (1-c)U+G B+omega JU+grad P=0.

Assume M=sup|U|<infinity and, for some0<=delta<1/3 and finite C0,

    ||G(y)||<=C0(1+|y|)^delta.                     (1)

Then G is bounded. For0<delta<1/3 the one-step improvement is

    ||G(y)||<=C(1+|y|)^(4delta-1).                 (2)

Constants depend on c,omega,delta,C0,M and a fixed compact-annulus C2 norm. They are not uniform over these quantities. The proof of boundedness does not use A492. After boundedness has been proved, A492 gives Dini gradient decay, W=O(1/r), and G=O(1/r), including its A476 corollary. If U tends uniformly to zero and1/3<c<1, A477 then gives G=O(r^-1/c). No hypothesis on pressure normalization, helicity, energy or symmetry is made.

The endpoint delta=1/3, the weaker condition G=o(r^1/3), and any inference of(1) from bounded or decaying U remain outside this result. The campaign nonexistence conjecture remains open. If M=0 the conclusion is immediate. If delta=0 boundedness is already assumed. Thus the proof below takes M>0 and0<delta<1/3.

## 2. Pressure with an unbounded but controlled source

Taking divergence of the actual equation, including the cancellation of its skew terms, gives

    f=Delta P=-tr(G^2)=-partial_i partial_j F_ij,
    F_ij=U_i U_j.                                  (3)

Thus F is bounded and |f(y)|<=C(1+|y|)^(2delta). The momentum equation first bounds |grad P(y)|<=C(1+|y|)^(1+delta). Let N=-1/(4pi|x|),Delta N=delta0, choose a fixed smooth chi equal to1 near0 with support in the radius2 ball, and let N_d=chi(x/d)N. Define

    Q_d=grad N_d*f-partial_i partial_j grad(N-N_d)*F_ij. (4)

The first kernel is compactly supported and integrable, so its convolution is defined against the locally bounded f. The second kernel is globally L1: its tail is O(|x|^-4), and its singularity is cut off. Their L1 norms are respectively at most C d and C/d. Both convolutions are continuous. Put a_d=Delta N_d-delta0, a smooth compactly supported annular function. Kernel differentiation gives

    div Q_d=f+a_d*f+partial_i partial_j a_d*F_ij=f,
    curl Q_d=0.                                   (5)

The cancellation in the first line is exactly(3) tested against the compact kernel. For the curl, mixed derivatives of the vector kernel commute; the fourth derivatives of N-N_d remain L1, so differentiation against bounded F is justified. No undifferentiated convolution of its nonintegrable potential kernel is needed.

The definition is independent of d. In fact N_d-N_e is smooth, compactly supported and zero near0; subtraction of(4) gives its gradient convolved with f plus its third derivatives convolved with F, which cancel by(3). Denote the common field by Q. At a point of radius R>=2 choose d=R^-delta. The first convolution samples only a radius2d neighborhood where f=O(R^(2delta)); therefore

    |Q(y)|<=C(d R^(2delta)+d^-1)<=C R^delta.        (6)

This is a bound on the same globally defined Q. By(5), h=grad P-Q is an entire harmonic vector distribution. It grows as O((1+|y|)^(1+delta)). Its second derivatives at any fixed point are bounded by C R^(delta-1) on balls of radius R, so h=Ky+b because delta<1. In the actual equation at y=Rz divide by R on a fixed annulus. The term G(Rz)Az tends distributionally to zero, since G(Rz)=D_z(U(Rz)/R). All other terms except Kz are O(R^(delta-1)) or O(1/R), while Q(Rz)/R=O(R^(delta-1)). Hence K=0. Equations(4)-(6) prove

    |grad P(y)|+|G(y)Ay|<=C(1+|y|)^delta.          (7)

For e(y)=Ay/|Ay|, |Ay|>=c|y| and De=(I-e tensor e)A/|Ay| give

    |G e|<=C R^(delta-1), |De|<=C/R.              (8)

The constant b in grad P is harmless and has not been discarded.

## 3. Complete characteristics and axial vorticity

The locally Lipschitz B has linear growth because U is bounded, so it is complete even though its derivative may be unbounded. Choose R0>2M/c,k=M/c. Every exterior point crosses the sphere of radius R0 in finite backward time, by r'>=cr/2 on the exterior. On the forward segment starting there,

    k+(R0-k)e^(cs)<=r(s)<=(R0+k)e^(cs)-k,
    r(t)/r(s)<=C e^(c(t-s)), 0<=s<=t.              (9)

These follow by integrating cr-M<=r'<=cr+M. The explicit direction satisfies D_(Ay)e=-omega Je. Consequently the vorticity equation W'=GW-W-omega JW gives for sigma=W.e

    B sigma=-sigma+e.GW+W.D_Ue.                    (10)

At a point with e=e3, W=(G32-G23,G13-G31,G21-G12) and e.GW=G32G13-G31G23+G33 W3. Thus |e.GW|<=C||G||||Ge||. Equations(1),(8) give forcing bounded by C R^(2delta-1) in(10). Set theta0=1-2delta>0. Since c theta0<1, integration on(9) yields

    |W(y).e(y)|<=C R^(-theta0)=C R^(2delta-1).     (11)

Explicitly multiply the forcing at time s by e^(-(t-s)), replace r(s)^(-theta0) by C r(t)^(-theta0)e^(c theta0(t-s)), and integrate the decaying exponential. Initial values are bounded on the fixed sphere; e^-t is no larger than C r(t)^(-theta0).

## 4. A local exponential Holder bound

We prove

    [G]_(1/2,B(y,R/8))<=exp(C R^delta)             (12)

for sufficiently large R=|y|. Use tau=1-t,s=-log tau,Q_s=exp(omega sJ) and y=exp(sA)x. The physical Euler variables are u=tau^(-(1-c))Q_s U(y),xi=tau^-1 Q_s W(y). Globally |u|<=M tau^(-(1-c)); on the fixed annulus1/16<|x|<16,

    ||grad u||+|xi|<=C1 tau^(-1-cdelta).            (13)

Every finite preterminal physical flow is complete, since its velocity is bounded and locally Lipschitz.

For a ball E near the unit sphere and0<d<=1/16 with E+d inside1/2<|x|<3/2, the elementary localized Biot-Savart estimate is

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
          +Cw d^-1/2(1+log(1/d))+CZ,
    w=C1 tau^(-1-cdelta), Z=tau^(-(1-c))+w.         (14)

Here E+d denotes concentric enlargement. To verify it, subtract BS(chi0 xi) with fixed chi0 supported in the annulus of(13) and equal to1 on1/8<|x|<8. The difference is harmonic there, not necessarily curl-free. The integrable degree-minus-two kernel bounds BS by Cw; interior harmonic estimates bound the first two derivatives of the difference by CZ. A second cutoff inside E+d, equal to1 on E+d/2, gives a local derivative kernel of degree minus three and zero spherical mean. Subtracting values proves its homogeneous one-half Holder bound C[xi]_(1/2,E+d)+Cw d^-1/2. For two points distance q apart, the exterior kernel difference contributes Cq integral_(2q)^infinity r^-3/2 dr=C q^1/2; the inner contribution is also C q^1/2. The remaining data vanish at distance d/2 from E, giving derivative supremum Cw(1+log(1/d)) and Lipschitz constant Cw/d. Interpolating yields(14). Cutoff zero extensions obey the same bound by their Lipschitz estimate. Thus(14) uses only local(13) and bounded u, with no global bound on grad u.

Choose t0 with(2M/c)(1-t0)^c<=1/8. For |xstar|=1 put r0(t)=1/4+(2M/c)(1-t)^c and Theta(t)=[xi(t)]_(1/2,B(xstar,r0(t))). Paths ending in this ball at time t lie at time q<t in the ball E(q,t) of radius r0(t)+d(q,t), where

    d(q,t)=(M/c)((1-q)^c-(1-t)^c),
    M(t-q)<=d(q,t)<=1/16, r0(q)=r0(t)+2d(q,t).      (15)

These convex containing balls and all joining segments stay in the annulus of(13). Put l(t)=C1 tau^(-1-cdelta) and E0(t)=exp(integral_(t0)^t l(v)dv). The mean-value theorem on those balls and backward Gronwall give path separation at q bounded by E0(t)/E0(q) times terminal separation. Integrating the difference of xi'=(grad u)xi along the two paths and using(14)-(15) gives

    Theta(t)<=E0(t)^1/2 Theta(t0)
       +integral_(t0)^t (E0(t)/E0(q))^1/2
          [(l+Cw)Theta+Cw^2 ell(t-q)+CwZ](q)dq,
    ell(v)=v^-1/2(1+|log v|).                      (16)

In the last expression ell depends on t-q, not on q alone. It is integrable on(0,1]. Initial seminorms are uniformly finite over xstar by compact C2 regularity. Set Y=E0^-1/2 Theta. Since E0>=1, the inhomogeneous part is bounded by C(1+Theta(t0))tau^(-2-2cdelta), a nondecreasing majorant. The coefficient l+Cw integrates to at most C tau^(-cdelta)/(c delta). Integral Gronwall gives Y<=C tau^(-2-2cdelta)exp(C tau^(-cdelta)), and hence Theta<=exp(C' tau^(-cdelta)) at late times. These are finite locally bounded Borel seminorms, so Gronwall applies to actual functions. Apply(14) on B(xstar,1/8) with d=1/16. At R=|y| choose tau=R^-1/c; the profile image is B(y,R/8) and the exact seminorm factor is tau^(1+c/2). This proves(12).

## 5. Frozen planar ellipticity and its exponent

For n=2 or3, a compactly supported C2 cutoff of a vector field v on B(0,2ell) satisfies

    |Dv(0)|<=C[K eta^1/2+epsilon(1+log(2ell/eta))], (17)

where the cutoff is1 on B(0,ell), the supremum of all its divergence and antisymmetric derivative data is at most epsilon, their one-half Holder seminorm is at most K, and0<eta<=1. The vector Laplacian identity represents Dv by second derivatives of the Newtonian kernel applied to those data. The kernel has degree -n and zero spherical mean, plus a constant local term. Subtraction in the radius-eta ball gives CK eta^1/2, and the remaining annulus gives Cepsilon log(2ell/eta). This exact compact-support identity has no uncontrolled harmonic term, also in dimension2.

Fix y,R=|y| and freeze n=e(y),P0=I-n tensor n. Put ell=R^((1-delta)/2) and restrict V(v)=P0 U(y+v) to the affine plane n-perp, |v|<2ell. For large R the disk lies in B(y,R/8). Its projection is constant, so

    div_2 V=-n.G(y+v)n, curl_2 V=W(y+v).n.

The direction error is O(ell/R). Equations(1),(8),(11) bound the data by C[R^(delta-1)+R^(2delta-1)+R^delta ell/R]. The cutoff adds CM/ell. Since delta<1/3, all these terms are at most C R^((delta-1)/2). By(12), restriction, constant projections and cutoff product estimates give K<=exp(C2 R^delta); all other terms grow only polynomially. Choose eta=exp(-4C3 R^delta) with C3>C2 and C3>=1. The near term in(17) is exponentially small and the logarithm is O(R^delta). Therefore, at each point with its own e,

    ||PGP||<=C R^((3delta-1)/2)->0.                (18)

No derivative of the frozen projection has been omitted. The full tangential matrix, not merely its trace, is controlled.

## 6. Full vorticity and the improved gradient

Use the exact block decomposition G=H+e tensor g+h tensor e, where H=PGP,g=PG^T e,h=Ge. Equations(1),(8),(11),(18) give

    ||H||<=C R^((3delta-1)/2), |g|<=C R^delta,
    |h|<=C R^(delta-1), |W.e|<=C R^(2delta-1).

For q=|W|>0 the vorticity equation and skewness of J imply

    q'<=-[1-||H||-C R^(delta-1)]q+C R^(3delta-1). (19)

Indeed the middle block contributes at most |W.e||g| to q', and the final block at most |h|q using |W.e|<=q. Put theta=1-3delta>0 and beta=(1+c theta)/2, so c theta<beta<1. Outside a fixed radius(18) makes the damping coefficient at least beta. Integrating on the finite exterior segments of(9), exactly as in Section3, proves

    |W(y)|<=C R^(3delta-1).                       (20)

Zero trajectories are covered by uniqueness, and initial sphere values are bounded. A3D cutoff on B(y,R/16), equal to1 on B(y,R/32), has div-curl data of supremum at most C R^(3delta-1), because the velocity cutoff terms are O(M/R). Its Holder seminorm is bounded by exp(C R^delta). Apply(17) with the same exponential choice of eta. Its logarithm multiplies the data by at most C R^delta, proving ||G(y)||<=C R^(4delta-1). The exponentially small remainder is smaller than this fixed power. Compact boundedness gives(2) globally.

## 7. Finite iteration, not a limiting argument

If0<delta<=1/4, (2) already gives bounded G. Otherwise delta1=4delta-1 lies in(0,1/3) and is strictly smaller than delta. Repeat the same complete argument with the new exponent. Its formal sequence is deltan=1/3+4^n(delta-1/3), which reaches at most1/4 after finitely many steps. One more application proves boundedness. Each step uses only finite constants and a compact initial annulus. No convergence of constants or infinite iteration is assumed.

A492 can now be applied, giving the Dini and power decay conclusions stated in Section1. It was not used in Sections2-7. At delta=1/3 the decay exponent in(18) vanishes and the exponent iteration has a fixed point; nothing in this proof handles that endpoint or a bare little-o bound there. No computation is needed. The full submitted source was read before reconstruction. Existing configured-model file challenge of the pressure cancellation, local paired paths and exponent arithmetic is requested; no new remote client is used.

## 8. Independent review and final scope

The complete220-line coordinator review in the team records was read, including its limitations and all seven precision points. It independently agrees with the pressure cancellation, every exponent, the local-only paired paths and finite iteration. Its undefined-potential warning is already corrected in Section2: curl is taken on the integrable differentiated kernel. Section4 above supplies the full local singular-integral argument that the reviewer checked only by reference, and Section5 explicitly proves the compact-support estimate. The source's pending-LIT120 wording is obsolete; A492 is already confirmed and is used only after boundedness. The reviewer reports a subagent without separate model runtime attestation; coordinator configuration is the primary model. No new model client or computation was used.
