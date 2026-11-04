# Closed endpoint of the nonlinear vorticity threshold

## 1. Exact statement and dependencies

Let 0<c<2/3, omega be any real number, Jx=e3 cross x and A=cI-omega J. Let U in C2(R3;R3), P in C1(R3) solve

    (1-c)U+DU(Ax+U)+omega JU+grad P=0,    div U=0.

Assume Hb: U is bounded and U(R.) tends to zero in distributions as R tends to infinity. Let h_c be the unique C1 solution, including its initial endpoint, of

    h_c(0)=0,
    h_c'(t)=(3/(2t))(1-sqrt(1-t/3-2c h_c(t)))

up to the first time t_c>0 at which t/3+2c h_c(t)=1. The existence, uniqueness, C1 extension at t_c and 0<t_c<3 were proved in A1720-A1721. Put T(c)=sqrt(t_c).

Then

    sup_R3 |curl U| <= T(c)

implies U=0 and P is constant. Equality in this bound is included. No helicity condition, symmetry, pressure normalization, derivative-decay hypothesis or finite-enstrophy hypothesis is added.

The analytic inputs are the Hb energy theorem A040/A052 as composed in A1530, the compact-cutoff identities of A1584, and the bounded-U, bounded-DU derivative-decay theorem A492. The last theorem requires the full profile equation, 0<c<1, U in C2 and P in C1, with both U and DU bounded. It gives |DU(x)|<=C(1+log|x|)/|x| for large |x|, for every omega. Its proof uses the actual pressure and exterior flow, not a helicity hypothesis or the conclusion below. Sections2-5 verify that all these premises are met before that input is applied. Section6 gives the independent weighted-enstrophy boundary argument on 2/5<=c<=1/2.

## 2. The nonnegative cutoff density still vanishes at equality

Write B=Ax+U, W=curl U, G=DU, S=(G+G^T)/2 and t=|W|^2. The curl of the profile equation gives

    B.grad t=2(W.SW-t),    div B=3c.

For a smooth nonnegative radial cutoff phi_R=chi(|x|/R), with chi nonincreasing, one on [0,1] and zero on [2,infinity), the rotation is tangent to its level surfaces. Once R>2||U||_infinity/c, B.grad phi_R<=0.

Let g=h_c on [0,t_c]. It is C1, g(0)=0 and g'>0. Its derivative is positive also at both endpoints: g'(0)=1/[4(1-3c/2)] and g'(t_c)=3/(2t_c). A C1 extension beyond the closed interval justifies the chain rule at an attained endpoint. Integrating the scalar transport identity gives

    integral phi_R T_R = F_R >=0,
    T_R=2g'(t)W.SW-2g'(t)t+3cg(t),
    F_R=-integral g(t) B.grad phi_R.

Here T_R is independent of R; the notation only distinguishes it from the threshold T(c). Two integrations by parts using div U=0 give

    integral phi_R (|S|^2-t/2)=E_R,
    E_R=integral U_i U_j partial_i partial_j phi_R.

The energy theorem gives E_ball(R)=integral_(|x|<R)|U|^2 <= C R^beta, where beta=max(5-2/c,0). For c<2/5 it already gives U=0; at c=2/5 it gives finite energy. In every case beta<2 for c<2/3. Thus

    |E_R|<=C R^(-2)E_ball(2R) ->0.

The exact square completion, using tr S=0, is

    D=|S|^2-t/2-T_R
      =|S-g'(t)(W tensor W-tI/3)|^2+H[g,1](t),
    H[g,1]=2tg'-3cg-t/2-(2/3)t^2(g')^2.

The ODE says H[g,1]=0 on all of [0,t_c]. Therefore D is continuous and nonnegative, and integral phi_R D=E_R-F_R<=|E_R|. Monotone convergence proves integral D=0, without first assuming integrability of its separate terms. Hence D=0 everywhere.

## 3. Equality fixes the strain and makes a cubic nonnegative

Put phi(t)=h_c'(t). It is continuous and strictly positive on the compact interval [0,t_c], with 0<phi_min<=phi<=phi_max<infinity. From D=0,

    S=phi(t)(W tensor W-tI/3).                                      (1)

In particular |S|^2=(2/3)phi(t)^2 t^2 is bounded. Since the skew part K=(G-G^T)/2 satisfies Kv=(W cross v)/2 and W is bounded, G is now bounded. Bounded DU has been obtained here, before A492 is used.

We have K^2=(W tensor W-tI)/4. By symmetry and skew symmetry, tr(S^2K)=tr(K^3)=0, and tr(SK^2)=W.SW/4. Expanding under the trace gives

    tr G^3=tr S^3+(3/4)W.SW.

The eigenvalues of S in (1) are 2phi t/3 in the W direction and -phi t/3 twice. The formula extends continuously through W=0. Consequently

    tr S^3=(2/9)phi^3 t^3,
    W.SW=(2/3)phi t^2,
    tr G^3=(2/9)phi^3 t^3+(1/2)phi t^2
           >=(1/2)phi_min t^2 >=0.                              (2)

## 4. The cubic identity and its exact boundary term

For any C2 incompressible U, with G_ij=partial_j U_i, define

    Q_j=sum_(i,k) U_i G_jk G_ki,
    F=Q-(1/2)U tr G^2.

Then

    div F=tr G^3.                                                (3)

Indeed, differentiating Q gives the cubic plus a term containing partial_j G_jk=partial_k div U=0 and a remaining term U_i G_jk partial_j G_ki. Commuting the second derivatives of U turns the last factor into partial_i G_kj. Summing j,k gives (1/2)U.grad tr G^2, which is div((1/2)U tr G^2). This proves (3) using only C2 regularity.

With Frobenius norms, |Q|<=|U||G|^2 and |tr G^2|<=|G|^2. Thus, for A_R={R<|x|<2R},

    |integral phi_R tr G^3|
       <=(3/2)||chi'||_infinity R^(-1) integral_(A_R) |U||G|^2.   (4)

All integrals so far are compactly supported. No global integration of a possibly nonintegrable unsigned cubic is used.

## 5. Boundary control for every 0<c<2/3

Section3 supplies bounded G. Bounded U is part of Hb, so the exact A492 hypotheses listed in Section1 hold. Hence on A_R at large R,

    |G|<=C(1+log(2R))/R.

Cauchy-Schwarz and the energy estimate of Section2 give

    R^(-1) integral_(A_R)|U||G|^2
       <=C R^(-3)(1+log(2R))^2 |A_R|^(1/2) E_ball(2R)^(1/2)
       <=C'(1+log(2R))^2 R^((beta-3)/2) ->0.

Here beta<2<3. Dependence of C on omega is allowed; no uniform bound in omega is required to conclude vanishing for each finite omega.

Equations(2)-(4) and monotone convergence now give integral tr G^3=0. Its continuity and nonnegativity imply tr G^3=0 everywhere, so (2) forces W=0. Equation(1) gives S=0 as well. Thus DU=0, Hb removes the constant velocity, and the profile equation gives grad P=0. This proves the theorem, including its closed endpoint.

## 6. Independent boundary control in the campaign interval and a new exact bracket

The confirmed weighted-enstrophy theorem A1530 says that, with bounded W and Hb, if m>3-2/c and

    w_inf:=limsup_(|x|->infinity)|W(x)| < sqrt(3)[1-(3-m)c/2],

then integral <x>^(-m)(|W|^2+|DU|^2)<infinity. At m=1 the threshold is sqrt(3)(1-c). If T(c) is below this threshold, the endpoint premise implies the required strict inequality. Then

    R^(-1) integral_(A_R)|U||DU|^2
       <=3||U||_infinity integral_(|x|>=R)<x>^(-1)|DU|^2 ->0,

which proves (4) tends to zero without A492.

The new c=2/5 polynomial certificates, with all exact coefficients retained in the team records, give

    1.004 < T(2/5) < 1.01272.

The independent exact check verifies the lower polynomial's H/t and derivative are positive on the full closed interval, and the upper polynomial's H/t and lower-root branch polynomial are negative while k/t is positive. Every sign follows from a zero Sturm root count and nonzero endpoint signs. The upper barrier excess is strictly positive and the quoted upper bound is rounded outwards. The previous twenty certificates are unchanged, as checked by equality of the extracted JSON numbers; their arithmetic was not repeated.

For each consecutive pair c_k,c_(k+1) from 0.40 through 0.50, the exact upper endpoint tau_k obeys

    tau_k < 3(1-c_(k+1))^2.

The last singleton c=0.50 obeys the same strict inequality. Monotonicity of T then gives T(c)^2<=tau_k<3(1-c)^2 throughout that interval. Thus the independent route applies on all of [2/5,1/2]. The eleven positive rational gaps are in the team records.

The exact run was 2026-11-03T17:06:06.540370+00:00 to 2026-11-03T17:06:07.134862+00:00, elapsed 0.5944845820777118 seconds, CPU55, nice19, one thread. The reversed-sign negative control was rejected. Initial preflight container-shape and missing-input failures are recorded in the supplementary manifest; no certificate arithmetic ran in those failed invocations. No numerical ODE integration was used.

## 7. Strict parameter monotonicity and Lipschitz scalar weights

The revised claim that T(c) is strictly decreasing is correct. Let c<d<2/3. The initial slopes satisfy h_d'(0)>h_c'(0), hence h_d>h_c for small positive t. Before either first barrier, a first equality would have a positive derivative of h_d-h_c, because F_d(t,h)>F_c(t,h) at their common positive value. This contradicts first contact from above. Thus h_d>h_c before the earlier barrier. If t_d>=t_c, continuity would imply

    t_c/3+2d h_d(t_c)
      >=t_c/3+2c h_c(t_c)+2(d-c)h_c(t_c)>1,

contradicting the d-domain condition. Therefore t_d<t_c.

For the scalar condition alone, let h be Lipschitz on [0,L], h(0)=0, h'>=0 almost everywhere, and H[h,1]>0 almost everywhere on (0,L). The square completion gives x_h=t/3+2ch<=1 everywhere by continuity. Moreover x_h increases at least at rate 1/3, so x_h<1 on [0,L). The singular comparison proof applies to these absolutely continuous functions: h-h_c=O(t), the linearized coefficient is (3c/2+O(t))/t near zero, and an integrating factor excludes a negative difference. On every compact positive subinterval its equation has a strictly positive forcing almost everywhere. Hence h-h_c is strictly positive and increasing there. If L>=t_c, this forces x_h(t_c)>1, a contradiction. Thus L<t_c.

Conversely the rescaled C1 weights already give every L<t_c. Nonnegative H allows L=t_c via h_c. Therefore Lipschitz scalar weights do not improve the threshold. This does not assert a new Lipschitz version of the PDE lemma: composition on positive-measure level sets still needs its own chain-rule analysis.

## 8. The Emden representation, including its regular branch

The new change of variables is also valid, with the regular branch specified. Set d=2-3c in (0,2). There is a unique local continuous fixed point of

    psi(r)=integral_0^r u^(1-d) integral_0^u v^(d-1)exp(-psi(v)) dv du.

For small r this map contracts on a fixed sup-norm ball, since its Lipschitz constant is O(r^2/d); it maps that ball into itself. Differentiation for r>0 gives

    psi''+(d-1)psi'/r=exp(-psi),
    psi(r)=r^2/(2d)+O(r^4).

The integral formula gives psi'>=0 and psi>=0. It then gives psi'<=r/d, so the branch extends across every finite positive radius. Put y=r psi'. Its equation is

    y'=(2-d)y/r+r exp(-psi)>0.

For any r0>0, y(r0)>0 and y(r)>=y(r0)(r/r0)^(2-d) for r>=r0. Therefore y reaches 2 at a finite first radius r_c.

Define t=(3/2)r^2 exp(-psi), s=1-y/2. Direct differentiation gives

    dt/dr=2st/r,
    ds/dr=-[3c(1-s)+t/3]/r.

Thus t is strictly increasing until r_c, and

    s ds/dt=(3c/(2t))(s-1)-1/6.

The function h=(1-s^2-t/3)/(2c) then solves h'=F_c(t,h). The regular expansion gives h/t ->1/(2d)=1/[4(1-3c/2)], so uniqueness at zero identifies it with h_c. At r_c, s=0 and the first barrier is reached. Consequently

    t_c=(3/2)r_c^2 exp(-psi(r_c)).

Finally q=1-s satisfies

    dt/dq=6(1-q)t/(t+9cq),    t(q)/q ->6-9c as q->0.

This is the positive regular branch, and t_c=t(1). The condition t(0)=0 alone would also allow the identically zero branch on q>0, so the branch asymptotic must be retained in any standalone formulation. No numerical comparison of ODE solvers is used here.

## 9. Audit limits and remaining wording repair

C59's closed endpoint, both boundary routes at their stated scopes, the new c=2/5 bracket, strict monotonicity, the scalar Lipschitz statement and the regular Emden representation are confirmed by the arguments above. The threshold remains a global vorticity smallness condition. No such bound follows from bare decay in this audit, and no larger-threshold or full-class Liouville theorem is established.

The pinned Remark R2 still omits the required normalization and infers failure of nonnegativity merely from H<=0. This is the same defect recorded at A1726; it does not invalidate C59. Use the repair A1727: retain g in C1, g(0)=0 and a>0; if H>=0 past t_c, its first contact with x_h=1 has x_h'=1/3+3c/t>0, which is impossible. Thus H is strictly negative somewhere when M>T(c). Remark6.1 must cite this stronger argument rather than obtain strict negativity from NW.3(b) alone.

The current source is from the existing configured model agent. Configuration is known, but actual provider runtime is not independently attested. This audit returns the detailed proof and outstanding correction through working files.
