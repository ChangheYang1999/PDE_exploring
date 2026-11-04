# A positive extension of the nonlinear vorticity threshold

## 1. Exact hypotheses, notation and dependencies

Let 0<c<2/3, let omega be any real number, put Jx=e3 cross x and A=cI-omega J, and suppose U in C2(R3;R3), P in C1(R3) solve

    (1-c)U+DU(Ax+U)+omega JU+grad P=0,    div U=0.

Assume Hb: U is bounded and U(R.) tends to zero in distributions as R tends to infinity. Write W=curl U, G=DU, S=(G+G^T)/2, Omega=(G-G^T)/2, B=Ax+U, and t=|W|^2. Norms of matrices are Frobenius norms. The vorticity bound in each theorem below is an additional global hypothesis.

Let h be the unique solution, including both C1 endpoints, of

    h(0)=0,    h'(t)=(3/(2t))(1-sqrt(1-t/3-2ch(t)))

up to its first barrier tau, where tau/3+2ch(tau)=1. The confirmed scalar theorem A1720-A1721 gives 0<tau<3, h'(0)=1/(4-6c), h'(tau)=3/(2tau), and h'>0. Put T=sqrt(tau).

The only pressure-dependent input below is the confirmed Hb energy theorem A040/A052, in the precise composition A1530: if beta=max(5-2/c,0), then

    E_ball(R):=integral_(B_R)|U|^2 <= C R^beta,    R>=2.

Here beta<2. This statement includes c=2/5 and all 0<c<2/3; below 2/5 that theorem already implies U=0. No pressure normalization or pressure decay is added. Define q(R)=R^(beta-2), and N(R)=integral_(B_R)|W|^4. Constants denoted C may depend on the profile and on fixed c and omega. All named constants below are explicit.

The proof uses compactly supported identities and an iteration before drawing any global integrability conclusion. It does not use A492, derivative decay, helicity, symmetry, completeness of a characteristic flow, or the weighted-enstrophy theorem EH. The source snapshots and exact read coverage are in the team records and in the team records.

## 2. Exact defect and cubic boundary identities

Choose a smooth nonincreasing chi:[0,infinity)->[0,1], equal to one on [0,1] and zero on [2,infinity), and set phi_R(x)=chi(|x|/R). The scalar curl equation and incompressibility give

    B.grad t=2(W.SW-t),    div B=3c.

For any nonnegative C1 weight g defined on the attained range of t, the chain rule and integration by parts give

    integral phi_R[2g'W.SW-2g't+3cg]=F_R,
    F_R=-integral g(t) B.grad phi_R >=0

for R>=2||U||_infinity/c. The last sign follows from B.grad phi_R=chi'(|x|/R)(c|x|+x.U/|x|)/R. Rotation contributes zero. A C1 extension at a finite endpoint permits composition even when the vorticity attains its bound.

Two integrations by parts give

    integral phi_R(|S|^2-t/2)=E_R,
    E_R=integral U_i U_j partial_i partial_j phi_R,
    |E_R|<=C R^(-2)E_ball(2R)<=Cq(R).

Put S0=g'(t)(W tensor W-tI/3), Z=S-S0, and

    H(t)=2tg'-3cg-t/2-(2/3)t^2(g')^2.

Trace-freeness and |W tensor W-tI/3|^2=2t^2/3 give the exact identity

    integral phi_R (|Z|^2+H(t))=E_R-F_R.                 (1)

No sign of H was used. Therefore, with H_-=max(-H,0),

    d_R:=integral phi_R |Z|^2 <= Cq(R)+integral phi_R H_-(t).    (2)

For any C2 divergence-free U, with G_ij=partial_j U_i, define Q_j=U_i G_jk G_ki, with repeated indices summed. Differentiation, div U=0 and commutation of second derivatives give

    div[Q-(1/2)U tr G^2]=tr G^3.

Indeed, the derivative hitting U gives tr G^3, the derivative hitting G_jk vanishes, and the remaining term is (1/2)U.grad tr G^2. Thus

    |integral phi_R tr G^3|
      <=(3/2)||chi'||_infinity R^(-1) integral_(R<|x|<2R)|U||G|^2.    (3)

This uses only compact integrals. Neither the cubic nor |G|^2 has been assumed integrable on the whole space.

## 3. A shorter independent proof of the closed endpoint

Assume sup|W|<=T and take g=h. Then H=0, so (1), q(R)->0 and monotone convergence imply Z=0 everywhere. With phi=h',

    S=phi(t)(W tensor W-tI/3),
    |G|^2=(2/3)phi^2 t^2+t/2 <= A0 t,
    A0=(2/3)(max_[0,tau] phi)^2 tau+1/2.

Since Omega^2=(W tensor W-tI)/4,

    tr G^3=tr S^3+(3/4)W.SW
           =(2/9)phi^3 t^3+(1/2)phi t^2
           >=(1/2)(min_[0,tau] phi)t^2.

The minimum is positive. Equation (3) and Cauchy-Schwarz give

    N(R)<=C R^(-1)E_ball(2R)^(1/2)N(2R)^(1/2)
         <=C sqrt(q(R)N(2R))
         <=N(2R)/16+Cq(R).

Iterating k times is legitimate because N(r)<infinity for every finite r. Bounded W gives N(r)<=(4pi/3)tau^2 r^3. The final term is bounded by C(8/16)^k R^3, while q(2^j R)<=q(R). Letting k tend to infinity gives N(R)<=Cq(R). As R tends to infinity, monotonicity of N forces N=0. Hence W=0, S=0, DU=0 and Hb gives U=0. The equation then makes P constant. This confirms C60 Route C for every stated c and omega.

## 4. The extended weight and its exact defect

Continue h linearly beyond tau:

    g(t)=h(t) for t<=tau,
    g(t)=h(tau)+(3/(2tau))(t-tau) for t>=tau.

This g is C1 and nonnegative with g(0)=0. Set

    L=max{1/(4-6c),3/(2tau)}.

Then 1/4<=g'<=L everywhere. For the lower bound before tau, let x=t/3+2ch(t). Rationalizing the square root gives g'=(3/(2t))x/(1+sqrt(1-x))>=3x/(4t)>=1/4. The continuation has the same bound because tau<3.

For the upper bound, write phi=h'. Differentiation on the open interval, where h is smooth, gives

    2t(1-(2/3)t phi)phi'=(3c-2)phi+1/2+(4/3)t phi^2.

At an interior critical point of phi, a second differentiation gives

    2t(1-(2/3)t phi)phi''=(4/3)phi^2>0.

The coefficient on the left is positive. Thus phi has no interior maximum; continuity on the closed interval bounds it by its two endpoint values. No bound on phi' at tau is required.

The exact polynomial after the barrier is

    H(tau+x)=-((tau+9c)/(2tau))x-(3/(2tau^2))x^2,    x>=0.    (4)

If 0<Delta<=tau, then for 0<=t<=tau+Delta,

    H_-(t)<=delta t^2,
    delta=(tau+9c+3)Delta/(2tau^3).                 (5)

For t<=tau this is immediate. For t=tau+x, use x<=Delta, x^2<=tau x and t^2>=tau^2 in (4). This verifies the stated bound on the full interval, without a numerical approximation to tau.

## 5. The explicit L4 div-curl estimate

For compactly supported C1 real vector fields V on R3,

    ||DV||_4<=36||curl V||_4+18||div V||_4
            <=K(||curl V||_4+||div V||_4),    K=36.       (6)

Here is a derivation with the constants retained. The one-dimensional Hilbert transform satisfies Cotlar's identity (Hf)^2=f^2+2H(fHf). Its L2 isometry, Holder and the quadratic inequality give ||Hf||_4<=(1+sqrt(2))||f||_4. The identity can be checked by squaring the analytic extension of f+iHf and using H^2=-I; density extends the bound from smooth inputs. This argument and its conventions were checked against Rodrigo Banuelos, Cotlar Martingale Transforms and Related Singular Integrals, arXiv:2604.09365v2, Section2, printed pages3-5. No later result of that manuscript is used.

Directional Hilbert transforms have the same bound by Fubini. With Fourier multipliers -i xi_j/|xi|, direct spherical integration gives

    R_j=(1/(2pi)) integral_(S2) theta_j H_theta d sigma,
    integral_(S2) |theta_j| d sigma=2pi.

Indeed, the vector integral of theta sign(xi.theta) is 2pi xi/|xi| by rotation invariance and its axial component. Thus ||R_j||_(4->4)<=1+sqrt(2) and ||R_m R_j||_(4->4)<=3+2sqrt(2)<6. The Fourier identity

    partial_m V_i=-R_m R_i div V+epsilon_ijk R_m R_j(curl V)_k

has at most two nonzero curl terms in each entry. Hence each entry has L4 norm at most 6(||div V||_4+2||curl V||_4). Minkowski applied to the sum of the nine entry squares contributes sqrt(9)=3, proving (6). No sharpness of 36 or18 is asserted.

Choose eta_R=1 on B_(2R), supported in B_(4R), with |D eta_R|<=C/R. Since curl(eta_R U)=eta_R W+D eta_R cross U and div(eta_R U)=D eta_R.U, (6) and Hb imply, with n=N(4R),

    ||G||_(L4(B_2R))<=K n^(1/4)+C R^(beta/4-1).           (7)

We used ||U||_(L4(B_4R))^2<=||U||_infinity E_ball(4R)^(1/2). If sup|W|<=M, set b=sqrt(2/3)LM. Then |S0|<=b|W| and

    ||Z||_(L4(B_2R))^2<=2(K+b)^2 n^(1/2)+C R^(beta/2-2).    (8)

All cutoff errors decrease with R; no global L4 norm has been assumed.

## 6. Cubic expansion and the explicit positive margin

Define

    M0=sqrt(2tau), b0=sqrt(2/3)LM0,
    A1=L^2 M0^2+3/4, A2=2LM0^2,
    Cstar=A1+A2+2(K+b0)^2,
    delta0=min{1,(2048 Cstar)^(-2)},
    Delta=min{tau,2tau^3 delta0/(tau+9c+3)},
    epsilon=sqrt(tau+Delta)-sqrt(tau)>0.

The theorem is: if sup|W|<=T+epsilon, then U=0 and P is constant. This is an explicit positive margin for each fixed c, without a certified decimal evaluation of its very small size.

Since tr Z=0, expanding the trace and using Omega^2=(W tensor W-tI)/4 gives

    tr G^3=f0(t)+(g'^2 t+3/4)W.ZW+3tr(S0 Z^2)+tr Z^3,
    f0(t)=(2/9)g'^3 t^3+(1/2)g't^2>=t^2/8.            (9)

For clarity, S0^2=g'^2[(t/3)W tensor W+(t^2/9)I], so 3tr(S0^2 Z)=g'^2 t W.ZW. The linear term from the skew part is (3/4)W.ZW. The remaining errors in (9) are bounded in absolute value by

    A1 t|Z|,    A2 |Z|^2,    |Z|^3,

because ||S0||_operator=2g't/3. The weaker |tr Z^3|<=|Z|^3 suffices.

The vorticity hypothesis gives t<=tau+Delta<=M0^2. Equations (2) and (5) give d_R<=Cq+delta n, where delta<=delta0. Equations (3) and (7) give

    |integral phi_R tr G^3|<=C sqrt(qn)+Cq.

The second cutoff term is initially C R^(beta-3), which is at most Cq for R>=1. The three error integrals in (9) are bounded by A1 sqrt(nd_R), A2 d_R and sqrt(d_R)||Z||_4^2. Using (8), sqrt(d_R)<=C sqrt(q)+sqrt(delta n), and delta<=sqrt(delta)<=1, we obtain

    N(R)/8<=Cstar sqrt(delta)n+C sqrt(qn)+Cq.          (10)

The extra mixed term sqrt(delta n)R^(beta/2-2) is bounded by sqrt(qn), since R^(beta/2-2)=sqrt(q)/R. The other cutoff product is q/R<=q. Thus no term with a growing radial coefficient is suppressed in (10).

Now Cstar sqrt(delta)<=1/2048. Young's inequality bounds C sqrt(qn) by n/2048+C'q. Therefore

    N(R)<=N(4R)/128+Cq(R)

for every sufficiently large R. Bounded W gives N(r)<=(4pi/3)(2tau)^2 r^3; the final iterated term has factor (4^3/128)^k=2^(-k). The decreasing q terms form a convergent geometric series. Let k tend to infinity and then R tend to infinity to obtain N=0. Equation (2) now gives d_R<=Cq(R)->0, so Z=0, hence S=0. The same conclusion U=0 and constant P follows. All estimates hold for every finite omega.

## 7. The integral replacement, including its constant

Let M>=T and assume sup|W|<=M. Define

    bM=sqrt(2/3)LM, A1=L^2M^2+3/4, A2=2LM^2,
    CM=A1+A2+2(K+bM)^2,
    deltaM=min{1,(2048 CM)^(-2)},
    DeltaM=min{tau,2tau^3 deltaM/(tau+9c+3)},
    X=integral_({t>tau+DeltaM}) H_-(t).

If X<infinity, then

    integral_R3 |W|^4<=CX X,
    CX=(2048/253)(512 CM^2+A2).                      (11)

To prove this, use the same weight on [0,M^2]. Splitting the negative defect at tau+DeltaM gives d_R<=Cq+deltaM n+X. Relative to (10), the additional terms are at most

    CM sqrt(Xn)+A2 X+C sqrt(X)R^(beta/2-2).

Young's inequality with coefficient 1/2048 is exactly

    CM sqrt(Xn)<=n/2048+512 CM^2 X.

Together with the two absorptions already used, this yields

    N(R)<=(3/256)N(4R)+8(512 CM^2+A2)X
          +Cq(R)+C sqrt(X)R^(beta/2-2).              (12)

Bounded W gives cubic growth of N; the terminal factor is ((3/256)4^3)^k=(3/4)^k. Both radial error powers decrease. Their geometric sums and the constant term have multiplier at most (1-3/256)^(-1)=256/253. Sending k to infinity and then R to infinity proves (11), with the displayed CX. No assumption of finite N(infinity) was made in the iteration.

For t>=tau, (4) implies

    H_-(t)<=kc t^2,    kc=(tau+9c+12)/(8tau^2),

using x/(tau+x)^2<=1/(4tau) and x^2/(tau+x)^2<=1. Consequently

    integral_({|W|^2>tau+DeltaM}) |W|^4
       >=theta integral_R3 |W|^4,    theta=1/(kc CX)>0.    (13)

If the left side is finite, then X is finite, so (11) first proves the right side finite. If it is infinite, (13) holds as an inequality of extended nonnegative integrals. A nonzero profile under Hb cannot have W=0: each bounded harmonic component of U would be constant, then zero. Thus for a nonzero profile the total mass is positive, possibly infinite.

If limsup_(|x|->infinity)|W|^2<tau+DeltaM, the integration set in X is bounded. Continuity of W and its global bound give X<infinity, hence W in L4 by (11). This statement alone does not prove U=0. If X=0, (11) does force U=0.

## 8. Scope and wording verdicts

C60 Route C, Theorem NW.6 and Proposition NW.7 are confirmed under the hypotheses in Section1 and their additional global vorticity bounds. The endpoint does not exhaust what the cubic identity and an L4 estimate can prove. There is still no derivation here of the needed bound from bare decay, and the campaign's unrestricted conjecture remains open.

The source calls (13) an equivalent form of (11). Replace this by a consequence. The one-sided estimate H_-<=kc t^2 proves (13) from (11), but the reverse implication with the stated constant is not supplied. This wording issue does not affect either proven inequality.

The current Remark R2 is repaired: g(0)=0 is retained, and strict negativity beyond tau follows from first contact, not merely from a failure of strict positivity. Indeed H>=0 implies x_h=t/3+2ch<=1 and comparison with h_* before first contact. A first contact occurs no later than tau; there h'=3/(2t), so x_h'=1/3+3c/t>0, contradicting x_h<=1 immediately afterwards. This confirms the repair of A1726/A1790.

No new numerical arithmetic or formal build was used in this audit. The tiny decimal margins in the source are floating-point illustrations, not part of this verdict. The Hilbert-transform primary text was obtained and its actual Section2 read; the remaining estimates were reconstructed above. Existing configured model collaborators receive this independent audit through working files; provider runtime is not independently attested.
