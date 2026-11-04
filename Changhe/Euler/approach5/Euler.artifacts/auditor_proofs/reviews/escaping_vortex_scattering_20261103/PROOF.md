# The scattering direction of an escaping equilibrium vortex half-line

Status: CONFIRMED as A602 after complete independent reconstruction and source/proof postreads of B31 Proposition2(d), with its exact transport dependencies and no regularity assumption on the projected sphere field. The case in the campaign interval is included in the slightly larger range below.

## 1. Exact statement and notation

Let 1/3<c<1/2 and omega be any finite real number. Put J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, Q_t=exp(omega tJ), T_t=exp(tA)=exp(ct)Q_t^T, a=1-2c, kappa=1+c and p=(1-c)/c. Suppose U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    U.curl U=0 everywhere,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1).

All constants are finite and may depend on this profile, c and omega. Define B=Ay+U, W=curl U and let Phi_t be the complete B-flow. Let q be a vortical carrier equilibrium, B(q)=0, W(q)!=0. Write rho for the real number DB(q)^T U(q)=rho U(q). Parametrize its complete vortex line as gamma'(tau)=W(gamma(tau)), gamma(0)=q. Choose tau0!=0, y0=gamma(tau0), and assume the forward B-orbit y(t)=Phi_t(y0) is unbounded.

The confirmed A210 tails are continuous fields V and Wstar on D=R3 minus{0}, with curl V=Wstar distributionally, and

    u_t(x):=exp((1-c)t)Q_t U(T_t x) -> V(x),
    w_t(x):=exp(t)Q_t W(T_t x) -> Wstar(x)

uniformly on compact subsets of D. Their homogeneities are V(T_s x)=exp(-(1-c)s)Q_s^T V(x) and Wstar(T_s x)=exp(-s)Q_s^T Wstar(x). Put

    F(w)=V(w), G(w)=Wstar(w), G_r(w)=w.G(w), w in S2,
    sigma(z)=log|z|/c, pi(z)=T_(-sigma(z))z,
    Y(w)=G(w)-(G_r(w)/c)Aw.

The conclusions are:

1. v=lim_(t->infinity) T_(-t)y(t) exists and is nonzero. For the global continuous scattering map Xi(z)=lim T_(-t)Phi_t(z), its image of this forward orbit is Xi(y(t))=T_t v. In coordinates (ell,w)=(log|Xi|,pi(Xi)) it is exactly (log|v|+ct,pi(v)).
2. With w=pi(v),

       Wstar(v)=Av/(kappa tau0),
       G(w)=|v|^(1+1/c)Aw/(kappa tau0),
       Y(w)=0, G_r(w)=c|v|^(1+1/c)/(kappa tau0).

   Thus the radial tail vorticity is strictly positive on the escaping tau>0 half and strictly negative on the escaping tau<0 half. In particular the tail vorticity at w is nonzero.
3. There is a finite constant C_*>0 such that exp(-(rho-c)t)|U(y(t))| tends to C_*. Therefore rho<=-a; F(w)=0 if and only if rho<-a. In particular every lower-window equilibrium with rho<=-2a and an escaping half-line supplies a simultaneous zero of F and Y, with G_r of the stated nonzero sign.
4. If Y is C1 in a neighborhood of this w, its divergence there satisfies div_S2 Y=(p-1)G_r. Hence its divergence at w is positive on the plus half and negative on the minus half. Without that additional regularity the identity is distributional, and no pointwise divergence or hyperbolic type is claimed.

The natural bounds can be replaced by uniform U->0 and any one of A601's sufficient derivative premises. The statement is conditional on an escaping half-line; it does not rule out bounded half-lines or their companions. If both halves escape, their opposite nonzero radial signs force different directions, as follows immediately from conclusion2.

## 2. Exact covector transport on the line

The confirmed identities give H=P+|U|^2/2+(Ay).U, g=U.B and

    grad H=B cross W-aU, BH=-ag, WH=0, [B,W]=-kappa W.

A048 gives complete W-flow under the present global hypotheses. Differentiating its bracket relation at B(q)=0 yields

    B(gamma(tau))=kappa tau W(gamma(tau)).

W cannot vanish at a finite vortex parameter by uniqueness, and each half is a forward B-orbit with tau(t)=tau0 exp(kappa t). A468,A478 give U(q)=-Aq!=0 and the real covector eigenvalue rho. On the entire vortex line,

    U!=0, g=0, grad H=-aU, grad g=rho U,
    (B.grad)U=rho U-DB^T U.                         (1)

Here is the role of the global rank input. On the connected regular vortical H-level through q, A413 gives locally g=f(H); the derivatives f'(H(q)) agree on overlapping submersion neighborhoods and equal -rho/a. Differentiating BH=-ag transports dH with covector rate rho. Initially U is nonzero on the vortex line near q. The resulting homogeneous linear equation(1) prevents its vanishing at a finite B-time. Every finite nonzero vortex parameter is reached in finite B-time from a nearby point on that same half, while q itself has U(q)!=0. This proves(1) along both full halves. These are the exact line identities audited in A540 Section2; no boundedness of the half-line enters that section.

With n=U/|U| and S_U=(DU+DU^T)/2, scalar multiplication of(1) gives

    d(log|U(y(t))|)/dt=rho-c-n.S_U(y(t))n.          (2)

The skew rotation cancels identically. No covector identity away from this line is substituted for(1).

## 3. Escape and the continuous scattering limit

Bounded U gives complete B-flow, since B is locally Lipschitz with linear growth. Write M=sup|U| and r(t)=|y(t)|. Outside the origin,

    cr-M<=r'<=cr+M.

Once an unbounded orbit crosses a radius R>M/c, it stays exterior and grows at least as exp(ct) times a positive constant. Upper comparison gives r(t)<=C exp(ct). Thus r(t) is comparable to exp(ct) for all sufficiently large t.

For any z in R3,

    T_(-t)Phi_t(z)=z+integral_0^t T_(-s)U(Phi_s(z))ds.

The integrand has norm at most M exp(-cs), so the limit Xi exists uniformly on all R3 and is continuous. A time shift in this formula, or in the defining limit, proves Xi(Phi_s z)=T_s Xi(z) for every fixed real s. On the escaping orbit, the positive radial lower bound above gives |v|>0 for v=Xi(y0). Consequently x_t=T_(-t)y(t) tends to v in a compact annulus. The ray description follows from pi(T_s z)=pi(z) and |T_s z|=exp(cs)|z|. This proof does not require differentiability of Xi.

## 4. Direct vorticity limit and its sign

Use the exact line relation from Section2, evaluated at y(t):

    exp(t)Q_t W(y(t))
      =exp(-ct)Q_t(Ay(t)+U(y(t)))/(kappa tau0)
      =[A x_t+exp(-ct)Q_t U(y(t))]/(kappa tau0).

The second term tends to0, already by bounded U. The first tends to Av/(kappa tau0). On the other hand, the left side is w_t(x_t). Uniform convergence on a compact annulus and continuity of Wstar show that it tends to Wstar(v). This proves the first formula in conclusion2 without invoking a flow of Y or a differential of Xi.

Set s=log|v|/c, so w=T_(-s)v=Q_s v/|v|. Homogeneity, and commutation of A with Q_s, give

    G(w)=exp(s)Q_s Wstar(v)
        =|v|^(1+1/c)Aw/(kappa tau0).

Since w.Aw=c, its radial component has the exact value stated above. The elementary derivative D pi(w)z=z-(w.z/c)Aw gives Y(w)=D pi(w)G(w)=0. All conclusions are pointwise consequences of continuous tails. The nonzero signs imply that two escaping halves cannot have the same w.

## 5. The velocity coefficient

By the natural derivative estimate and r(t) comparable to exp(ct), |DU(y(t))|<=C exp(-t) for all sufficiently large t, since c(p+1)=1. Hence the integral of |n.S_U n| over the forward orbit is finite. Integrating(2) yields

    exp(-(rho-c)t)|U(y(t))|
      -> |U(y0)| exp(-integral_0^infinity n.S_U(y(s))n ds)=C_*>0.

Uniform convergence of u_t at x_t->v gives

    |u_t(x_t)|=exp((1-c)t)|U(y(t))|
              =(C_*+o(1))exp((rho+a)t) -> |V(v)|.

The finite limit excludes rho>-a. If rho=-a it equals C_*>0; if rho<-a it is0. Homogeneity relates V(v) to F(w) by a nonzero scalar and an orthogonal map, so their zeros agree. This proves the equivalence in conclusion3. It strengthens the one-way source sentence without requiring a pressure estimate. The stricter rate rho<=-2(1-c) in the campaign interval follows separately from A518 and is not needed for the directional result.

## 6. The divergence clause and its limits

For completeness, div Wstar=0 distributionally and the twisted coordinates z=T_s w have volume element c exp(3cs)ds dA(w). Test against alpha(s)phi(w) with smooth compactly supported alpha. The homogeneity of Wstar and the derivative of pi give

    0=integral_R integral_S2 exp(-as)
         [alpha'(s)G_r phi+c alpha(s)Y.grad_S2 phi]dA ds.

Integration by parts in s gives c integral Y.grad phi=-a integral G_r phi. Thus div_S2 Y=(a/c)G_r=(p-1)G_r in distributions. Where Y is C1 both sides are continuous and this is pointwise. Positive trace at a zero of a two-dimensional field does not imply that both eigenvalues have positive real parts; no repeller or nondegeneracy conclusion is included.

Dependencies: A048,A413,A468,A478 and the line part of A540; A210 uniform actual tails; A601 only for the alternative premises. A533 supplies the same limits with additional regularity in the target interval but is unnecessary for this argument. Source passages: Theory Agent B W1_FARFIELD Proposition1 and Proposition2(d), and Theory Agent A SCATTERING_TAIL TheoremsS,T and CorollaryT.6. The argument does not rely on the more elaborate reduced-flow theorem in VORTEX_RETURN. No computation or formal build is used.
