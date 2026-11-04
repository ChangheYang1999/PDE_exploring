# A localized logarithmic vorticity bound and equivalent decay conditions

Status: independent reconstruction of Theory Agent A C36. Full postwrite check is complete; the existing configured-model response is pending. The proof uses the confirmed local kernel and transport estimates of A476. No velocity-decay-only conclusion is obtained.

## 1. Exact statements

Let U in C2(R3;R3), P in C1(R3) solve the full rotating incompressible Euler profile equation

    div U=0, (1-c)U+(Ay+U).grad U+omega JU+grad P=0,
    A=cI-omega J, 0<c<1, omega in R.

Assume M0=sup|U|<infinity and C1=sup||DU||<infinity, using the operator norm. Put W=curl U and

    v(r)=sup_(|y|>=r)|W(y)|, m(r)=sup_(|y|>=r)||DU(y)||.

Then v is nonincreasing, finite and at most2C1. There are constants C,R>0, depending on the profile as specified below, such that

    ||DU(y)||<=C[v(|y|/16)(1+log|y|)+|y|^(-1)],
    |y|>=R.                                           (1)

In addition to c,M0,C1, the constant may depend on a C2 norm of U on one fixed compact annulus corresponding to the chosen physical initial time. No bound in terms of only c,M0,C1 is asserted. No decay of U, pressure normalization, helicity hypothesis or restriction on omega is imposed.

Under these hypotheses the following conditions are equivalent:

(a) DU tends uniformly to zero at infinity;
(b) v(r)log r tends to zero;
(c) integral_1^infinity v(r)dr/r is finite;
(d) |W(y)|<=C'(1+|y|)^(-theta) for some C'<infinity,theta>0.

They are also equivalent to all five conditions of A476, including the derivative Dini condition integral m(r)dr/r<infinity. Moreover

    limsup_(r->infinity) v(r)log r is either0 or at least1/C,   (2)

where C is any fixed valid constant in (1). The value infinity is allowed.

For the physical self-similar field u from this profile and every fixed rho>0, these conditions are equivalent to finiteness of

    integral_(T-1)^T ||curl u(t)||_(Linfinity(|x|>=rho))dt,     (3)

and to the limit

    (T-t)log(1/(T-t))||curl u(t)||_(Linfinity(|x|>=rho))->0.   (4)

They are equivalent to Sigma_I=Sigma_S being empty, with the joint-spacetime singular sets of A475-A476. No claim about equality with Sigma_L is made without A477's additional hypotheses.

## 2. Physical bounds and the imported local estimate

If M0=0, all conclusions are immediate. Otherwise put tau=T-t, s=-log tau, Q_s=exp(omega sJ), y=exp(sA)x. Then

    u=exp((1-c)s)Q_s U(y), xi=curl u=exp(s)Q_s W(y),
    ||grad u||<=C1/tau, |u|<=M0 tau^(-(1-c)).          (5)

Choose t0 in[T-1,T) so that L(T-t0)^c<=1/8, L=2M0/c. Define

    w(t)=sup_(|x|>=1/16)|xi(x,t)|
        =tau^(-1)v(tau^(-c)/16)<=2C1/tau.             (6)

The equality follows because the rotating dilation maps the complete exterior of one sphere bijectively to the complete exterior of another. The function w is Borel. It need not be time-integrable.

The local estimates proved in A476, Sections4-5, apply for every t<T. Their hypotheses are exactly a pointwise bound |xi|<=w outside the fixed inner sphere, the global velocity bound (5), a finite gradient bound on preterminal intervals, and compact C2 regularity at t0. In particular their derivation does not require time-integrability of w. For a ball E centered near the unit sphere and margin0<d<=1/16, they give

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
       +C w d^(-1/2)(1+log(1/d))+C Z,
    sup_E||grad u||<=C epsilon^(1/2)
       ([xi]_(1/2,E+d)+w d^(-1/2))
       +Cw(1+log(1/epsilon)+log(1/d))+CZ,             (7)
    Z=tau^(-(1-c))+w, 0<epsilon<=1.

For clarity, the decomposition behind (7) is u=BS(chi xi)+BS((chi0-chi)xi)+h, where BS f=curl((4pi|.|)^(-1)*f), chi0 is fixed on a large annulus, and h is harmonic in the inner annulus. It need not be curl-free because chi0 xi need not be solenoidal. The local part uses degree-minus-three kernel cancellation, the distant part uses its distance d from E, and the harmonic bound uses only |u| and the integrable degree-minus-two BS kernel. This explains why the right side depends on w pointwise, without assuming integral w finite.

## 3. Polynomial Holder growth without integrable vorticity

For |xstar|=1 put

    r(t)=1/4+L(T-t)^c, Theta(t)=[xi(t)]_(1/2,B(xstar,r(t))).

For two backward particle paths ending in this ball at t, their displacement between q and t is at most

    delta(q,t)=(M0/c)((T-q)^c-(T-t)^c).

Their containing ball enlarged by delta is precisely the ball at time q. Also delta>=M0(t-q) and delta<=1/16 for t0<=q<t<T. The paired-path Lipschitz factor is ((T-q)/(T-t))^C1. Applying vorticity transport and (7), as proved in A476, gives

    Theta(t)<=((T-t0)/(T-t))^(C1/2)Theta(t0)
      +integral_(t0)^t ((T-q)/(T-t))^(C1/2)
       [(C1/(T-q)+Cw(q))Theta(q)
           +Cw(q)^2 ell(t-q)+Cw(q)Z(q)]dq,          (8)

where ell(r)=r^(-1/2)(1+|log r|) is integrable on(0,1]. This is an estimate on earlier-time seminorms with an integrable same-time margin cost; it does not require a bound on a larger future-time domain.

Let Y(t)=tau^(C1/2)Theta(t). By (6) and c<1, w(q),Z(q)<=C/(T-q). The inhomogeneous term in the inequality for Y is bounded by the nondecreasing function

    a(t)=C(1+Theta(t0))tau^(-2).

The coefficient of Y is bounded by

    beta(q)=C1/(T-q)+Cw(q)<=C6/(T-q),
    C6=C1+2C C1.

Before T all seminorms are finite and locally bounded, by compact C1 regularity of xi. They are Borel by the difference-quotient characterization on continuously varying open balls. Integral Gronwall therefore gives

    Y(t)<=a(t)((T-t0)/(T-t))^C6,
    Theta(t)<=C4 tau^(-N), N=2+C1/2+C6>=2.           (9)

The same compact initial annulus bounds Theta(t0) uniformly over xstar. The only change from A476 is the larger finite exponent C6 in place of treating integral w as a bounded constant. No step has assumed time-integrability of w.

## 4. The logarithmic bound and profile conversion

In (7) take E=B(xstar,1/8), d=1/16 and epsilon=tau^(2N). Its enlarged ball lies inside the ball defining Theta(t). Equations (6) and (9) imply

    epsilon^(1/2)([xi]_(1/2,E+d)+4w)
      <=C4+8C1 tau^(N-1)<=C.

Consequently, uniformly on the unit physical sphere,

    ||grad u(xstar,t)||<=C[1+w(t)(1+log(1/tau))
                              +tau^(-(1-c))].       (10)

For large y set s=(log|y|)/c, tau=|y|^(-1/c), xstar=exp(-sA)y. Then |xstar|=1, ||DU(y)||=tau||grad u(xstar,t)||, and tau w(t)=v(|y|/16). Equation (10) gives

    ||DU(y)||<=C[|y|^(-1/c)
       +v(|y|/16)(1+c^(-1)log|y|)+|y|^(-1)].

Since c<1, the first power is bounded by the last for |y|>=1. Increasing C and R proves (1). Every estimate used fixed finite omega; no uniform constant as omega varies is claimed.

## 5. Decay equivalences and the quantitative gap

By A476, (a) implies some positive power decay of DU, which implies (d) because |W|<=2||DU||. A positive power gives (c). To prove (c) implies (b), monotonicity gives

    v(r)(log r)/2<=integral_(sqrt(r))^r v(q)dq/q ->0.

If (b) holds, v(r)->0 and v(|y|/16)(1+log|y|)->0. Thus (1) gives (a). This proves the cycle and hence every stated equivalence.

For (2), put L=limsup v(r)log r. If L is infinite there is nothing to prove. If finite, then v(r)->0 and (1), with the fixed change of radius16, gives limsup||DU||<=CL. If L<1/C, A476's gradient gap forces DU->0. The already proved equivalences then give L=0. This proves (2), including its non-strict endpoint. The number1/C is profile-dependent; it is not a universal positive constant.

## 6. Physical BKM form

The exact scaling gives

    (T-t)||xi(t)||_(Linfinity(|x|>=rho))
        =v(rho(T-t)^(-c)).

With s=-log(T-t), r=rho exp(cs), dt=exp(-s)ds, Tonelli and the change of variables yield the extended-real identity

    integral_(T-1)^T ||xi(t)||_(Linfinity(|x|>=rho))dt
       =integral_0^infinity v(rho exp(cs))ds
       =c^(-1)integral_rho^infinity v(r)dr/r.        (11)

The finite interval between rho and1 contributes finitely since v<=2C1. Thus (3) is equivalent to (c). Also log(1/(T-t))=(log r-log rho)/c. Equation (4) is therefore exactly the condition v(r)(log r-log rho)->0, equivalent to (b). Finally A475 gives Sigma_I empty iff DU->0, and A476 gives Sigma_I=Sigma_S. This proves the physical statements with their exact singular-set convention.

## 7. Limits and dependencies

The main dependencies are the fully confirmed localized kernel and shrinking-ball inequalities of A476, its derivative gap, and the exact scaling theorem A475. Their hypotheses are all present here. The finite-energy and pressure hypotheses of some external BKM theorems are not imported, because (7)-(11) are proved from the local kernel decomposition and exact transport.

This does not prove v(r)log r->0 from U->0. It also does not show that W tending0 alone suffices, or that DU is bounded for every decaying profile. A profile in the unresolved bounded-gradient class could have vorticity tending0 too slowly for (b). No Euler example of that class is constructed. The source's additional quantitative Hessian remarks are not needed and are not part of this reconstruction. No computation is needed or used.
