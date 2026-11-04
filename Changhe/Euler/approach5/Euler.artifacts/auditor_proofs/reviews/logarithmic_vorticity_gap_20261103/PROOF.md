# A logarithmic vorticity estimate and its superseded bounded-gradient gap

Status: A584-A586 CONFIRMED after complete independent reconstruction and source/proof postreads. The inequalities and equivalences below are valid. A492 already proves all their favorable conditions under the stated bounded-gradient hypotheses, so they do not leave a new bounded-gradient obstruction.

## 1. Exact hypotheses and statement

Let U in C2(R3;R3), P in C1(R3), 0<c<1 and omega any finite real number. Put A=cI-omega J, where J rotates about the third axis, and assume the full profile system

    (1-c)U+DU(Ay+U)+omega JU+grad P=0, div U=0,
    M=sup |U|<infinity, L=sup ||DU||_op<infinity.

Let W=curl U, S=sym DU, and define the nonincreasing envelopes

    wstar(r)=sup_(|y|>=r)|W(y)|,
    mstar(r)=sup_(|y|>=r)||DU(y)||,
    Lambda=limsup_(|y|->infinity)lambda_max(S(y)).

There are finite C>0,R>=e such that

    ||DU(y)||<=C[wstar(|y|/16)(1+log|y|)+|y|^-1], |y|>=R.  (1)

The constant may depend on c,M,L, a chosen positive preterminal time gap and the C2 norm of U on one corresponding compact annulus. It is not asserted to be uniform over all profiles or over omega; dependence through those data is allowed. No helicity, velocity decay, natural tail or pressure normalization is assumed.

Within this exact class, each of the following is equivalent:

1. DU->0 uniformly at infinity.
2. Lambda<1, equivalently Lambda=0.
3. integral_1^infinity mstar(r) dr/r<infinity.
4. ||DU(y)||<=C(1+|y|)^(-theta) for some theta>0.
5. wstar(r)log r->0.
6. integral_1^infinity wstar(r) dr/r<infinity.
7. |W(y)|<=C(1+|y|)^(-theta) for some theta>0.

Moreover theta_star=limsup wstar(r)log r belongs to {0} union[C^-1,infinity], with C a fixed positive constant for which(1) holds. A492 and A476 in fact give theta_star=0 and all seven properties in this entire class, as explained in Section5.

## 2. Local Holder control without time-integrable vorticity

The cases M=0 or L=0 are immediate. Fix a terminal time T and set q(t)=T-t, s=-log q, Q_s=exp(omega sJ). The exact physical variables are

    u(x,t)=q^(-(1-c))Q_s U(exp(sA)x),
    xi(x,t)=curl u=q^-1 Q_s W(exp(sA)x),
    grad u=q^-1 Q_s DU(exp(sA)x)Q_s^T.

They satisfy Euler and (partial_t+u.grad)xi=(grad u)xi. In particular

    |u|<=Mq^(c-1), ||grad u||<=L/q,
    w(t):=sup_(|x|>=1/16)|xi(x,t)|
         =q^-1 wstar(q^-c/16)<=2L/q.               (2)

The last inequality follows from the skew part of DU, whose operator norm is |W|/2. The function w is Borel. It need not be time integrable through T.

Choose t0 in[T-1,T) so(2M/c)(T-t0)^c<=1/8. For every center |xstar|=1 let

    r(t)=1/4+(2M/c)q^c,
    Theta(t)=[xi(t)]_(1/2,B(xstar,r(t))).            (3)

We detail the spatial estimates and the same-time margin that close this seminorm. With Gamma=1/(4pi|x|) let BS f=curl(Gamma*f). It obeys curl BS f=f+grad Gamma*div f, div BS f0. For a cutoff chi0 supported in1/16<|x|<16 and equal1 on1/8<|x|<8, h=u-BS(chi0 xi) is harmonic on the latter annulus. It need not be curl free. The degree-minus-two kernel gives |BS(chi0 xi)|<=Cw. Interior harmonic estimates therefore give |Dh|+|D2h|<=C Z on the smaller fixed annulus, with Z=q^(c-1)+w.

For a ball E with its concentric enlargement E+d contained in1/2<=|x|<=3/2 and0<d<=1/16, introduce a cutoff chi supported in E+d and equal1 on E+d/2. The compactly supported Holder singular-integral estimate and the distant-kernel estimate give

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
           +Cw d^-1/2(1+log(1/d))+CZ,             (4)
    sup_E||grad u||<=C epsilon^1/2
       ([xi]_(1/2,E+d)+w d^-1/2)
          +Cw(1+log(1/epsilon)+log(1/d))+CZ,        (5)

for0<epsilon<=1. Here is the needed kernel argument. D BS is a contact term plus a homogeneous degree-minus-three kernel of mean zero on spheres. For its pointwise bound, split at epsilon, subtract the center value on the inner ball and integrate r^-1/2 there, and r^-1 outside. For its Holder bound at points distance h apart, split at2h; the inner contribution is C[f]_(1/2)h^1/2, while the outer kernel difference has size Ch r^-4 and integrates against [f]_(1/2)r^1/2 to the same bound. Cutoff multiplication contributes Cw d^-1/2. The complementary source is at distance>=d/2 from E; its derivative has supremum Cw(1+log(1/d)) and Lipschitz constant Cw/d, whose minimum bound gives the Holder term in(4). These arguments justify(4)-(5) without any assumed global Holder bound.

Physical particles exist on every finite interval before T, because u is globally bounded and Lipschitz there. A path ending in B(xstar,r(t)) has backward displacement over[rho,t] at most

    delta(rho,t)=(M/c)[(T-rho)^c-q(t)^c].

At time rho it lies in E(rho,t)=B(xstar,r(t)+delta), with

    E(rho,t)+delta=B(xstar,r(rho)),
    M(t-rho)<=delta(rho,t)<=1/16.                   (6)

For rho<t the margin is strictly positive. The lower bound uses0<c<1 and T-rho<=1. The upper bound and the radius inclusion follow from the choice of t0. Two backward paths satisfy

    |X1(rho)-X2(rho)|
          <=[(T-rho)/(T-t)]^L |X1(t)-X2(t)|.       (7)

Integrate vorticity transport along both paths, subtract, and apply(4) at that same time rho, with d=delta. Put ell(h)=h^-1/2(1+|log h|), whose integral from0 to1 is6. The product rule gives

    Theta(t)<=[(T-t0)/q]^(L/2) Theta(t0)
       +integral_(t0)^t [(T-rho)/q]^(L/2)
        [(L/(T-rho)+Cw(rho))Theta(rho)
                +Cw(rho)^2 ell(t-rho)+Cw(rho)Z(rho)]d rho.  (8)

The endpoint rho=t is irrelevant to the integral. Constants absorb the fixed positive M. Every seminorm is finite and locally bounded before T because xi is C1 on compact cylinders, and Borel as a supremum of continuous difference quotients on the continuously varying open balls.

Set F(t)=q^(L/2)Theta(t). Since w,Z<=C/(T-rho), multiplying(8) gives

    F(t)<=C(1+Theta(t0))q^-2
              +integral_(t0)^t C6/(T-rho) F(rho)d rho,
    C6=L+2CL.                                      (9)

The inhomogeneous integral is bounded by the displayed q^-2 majorant because (T-rho)^(L/2)<=1, (T-rho)^-2<=q^-2 and ell is integrable. Gronwall on each compact preterminal interval applies to the nondecreasing majorant and yields

    Theta(t)<=C q^-N, N=2+L/2+C6>=2.               (10)

Uniformity over xstar follows from Theta(t0)<=sup_(1/2<=|x|<=3/2)|Dxi(x,t0)|; the initial balls are convex and have diameter<=3/4. The logarithmically divergent integral of w has only enlarged N. No finite integral of w through T was silently used.

Take E=B(xstar,1/8),d=1/16 in(5), so its enlargement lies inside the ball of(3), and choose epsilon=q^(2N). The small-scale term is bounded by C+8L q^(N-1). Hence

    ||grad u(xstar,t)||
          <=C[1+w(t)(1+log(1/q))+q^(c-1)].          (11)

For any sufficiently large y, put q=|y|^(-1/c) and xstar=exp(-sA)y. Then |xstar|=1 and multiplying(11) by q gives

    ||DU(y)||<=C[|y|^(-1/c)
              +wstar(|y|/16)(1+c^-1 log|y|)+|y|^-1].

Since c<1, this proves(1). All balls, particle segments and time integrals were on finite preterminal intervals.

## 3. Equivalences and the exact threshold

A476 supplies the equivalence of the first four conditions, with the full proof in the team records. The new implications can also be checked directly. Condition4 gives7 because |W|<=2||DU||. Condition7 gives6. Monotonicity gives

    (log r)wstar(r)/2
          <=integral_(sqrt r)^r wstar(v)dv/v,

so6 gives5. Condition5 and the fixed shift r=|y|/16 in(1) give1. This proves the full cycle. In particular no implication from5 to6 for arbitrary monotone functions is being asserted. The eventually decreasing function1/(log r log log r) disproves that standalone implication.

If theta_star is finite then wstar(r)->0, and(1) gives limsup||DU||<=C theta_star. If C theta_star<1, A476 forces DU->0 and therefore7, so theta_star=0. This proves the stated dichotomy, including its extended-infinity case. Its threshold is tied to the chosen C and is not universal or sharp.

For U->0, the elementary continuity statements in C36 are also valid. For L0 equal to D or curl, a unit-supported smooth mollifier psi_epsilon gives by integration by parts

    |(L0 U)*psi_epsilon(y)|
          <=C epsilon^-1 sup_(B(y,1))|U|.

If L0 U has a uniform modulus mu, its difference from this mollification is at most mu(epsilon). First send |y| to infinity at fixed epsilon, then epsilon to0. Conversely, a continuous function tending to0 at infinity is uniformly continuous by compact uniform continuity and the exterior bound. Hence DU->0 iff DU is uniformly continuous, and W->0 iff W is uniformly continuous, for a C2 decaying field. These two separate equivalences are purely kinematic; they do not equate uniform continuity of W with that of DU.

## 4. Physical interpretation and its limits

For a fixed rho>0 put b_rho(t)=sup_(|x|>=rho)|xi(x,t)|. Orthogonality and dilation give exact identities, allowing infinite nonnegative integrals,

    b_rho(t)=q^-1 wstar(rho q^-c),
    integral_(T-1)^T b_rho(t)dt
                =(1/c)integral_rho^infinity wstar(r)dr/r,  (12)
    q log(1/q)b_rho(t)
                =(1/c)wstar(r)(log r-log rho),
         r=rho q^-c.                                 (13)

Boundedness of wstar makes the choice of positive lower radius irrelevant to convergence. Thus finiteness in(12), convergence to0 in(13), and all seven conditions of Section1 are equivalent.

Define Sigma_I by a positive joint space-time limsup of q||grad u(x,t)|| at(xstar,T), with xstar!=0. Define Sigma_S by a joint limsup of q lambda_max(sym grad u) at least1. A476 proves Sigma_I=Sigma_S. Their emptiness is equivalent to DU->0: if derivative decay fails, choose |y_n|->infinity,||DU(y_n)||>=epsilon and set s_n=log|y_n|/c, x_n=exp(-s_n A)y_n,t_n=T-exp(-s_n). Then |x_n|=1 has a convergent subsequence and the joint limsup at its limit is positive. The converse follows from the exterior envelope. These statements concern joint limits, not a fixed point at all late times.

No ordinary velocity continuation follows. For omega0, U=Vconstant!=0 and P=-(1-c)V.y form an exact full profile with W=DU0, while u=q^(c-1)V diverges at T. Its vorticity integral is0 everywhere. This checks the stated limitation without invoking any external continuation theorem or any literature attribution.

## 5. What is now known and the circularity audit

The independent A492 theorem applies to exactly the hypotheses of Section1, for every 0<c<1 and every finite omega. It proves |W|<=C/r and ||DU||<=C(1+log r)/r. Its complete proof, including its inline local Holder estimate, was reread for this audit. Its logical chain is A485 directional bounds, then polynomial local Holder control from bounded U and DU, then a frozen-plane div-curl estimate, then vorticity damping, then full derivative decay. It does not use C36 or an assumed Dini estimate.

A476 then improves the gradient rate to C/r by choosing kappa in(c,1) after Lambda=0. Consequently all seven conditions hold here and theta_star=0. In particular both old hypothetical C36 R2 classes, nondecaying W and W->0 with positive limsup wstar log r, are empty under bounded DU. R4 of the actual source acknowledges this; its earlier answer paragraph must not be presented as an unresolved bounded-gradient gap.

The remaining open question is whether bare U->0 in the target interval forces a sufficient gradient-growth bound. Neither C36 nor A492 removes bounded DU from their hypotheses. These results therefore do not prove the campaign's unrestricted nonexistence conjecture.

## 6. Verification evidence

The entire C36 source, its actual inner referee answer, GD Steps2-5, the original independent A476 proof, the full A492 proof and the precise physical joint-limsup definitions were read. The inner referee reported a failed attempt to contact model; it is not counted as a successful model consultation. The existing Theory Agent A author and the actual configured-model A476/A492 reviews supply the ongoing model collaboration. Their runtime provider identity is not independently attested. Every estimate here was checked analytically; no computation was needed. External bibliography suggestions in the referee are not certified by this audit.
