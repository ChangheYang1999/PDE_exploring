# Mixed vortex-line endpoints and escaping periodic-witness traces

Audit status: independent reconstruction of B55 and the corrected W2 Remark (xlvii), with a further pressure-gradient consequence. The unrestricted profile problem remains open.

## 1. Exact class and notation

Let U in C^2(R^3;R^3), P in C^1(R^3) satisfy

    (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    div U=0, U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p),
    |DU(y)|<=C(1+|y|)^(-p-1),

where 2/5<c<1/2, omega is any finite real number, Jx=(-x2,x1,0), A=cI-omega J, p=(1-c)/c and C is finite. Set a=1-2c, b0=2(1-c), kappa=1+c, B=Ay+U, Omega=curl U and L=(1-c)I+omega J. We write b0 for the scalar exponent to avoid confusing it with a unit tangent below. Put

    H=P+|U|^2/2+(Ay).U, g=U.B,
    k(x)=(Ax).V(x), S=P2-|V|^2/2,

where V, W=curl V and P2 are the actual tails, with the canonical pressure constant Pinf. Xi is the C^1 scattering diffeomorphism of the forward escaping set onto D=R^3 minus {0}. The bounded original velocity makes B complete in both time directions. The natural estimates, rather than an unproved derivative consequence of bare decay, are the hypotheses here. Previously confirmed sufficient derivative screens may supply them, but are not needed in the statements below.

## 2. A mixed vortex line has a flat bounded endpoint

Suppose p0 is a vortical carrier equilibrium, B(p0)=0 and Omega(p0)!=0, and its vortex line has one forward escaping half and one forward bounded half. Then the bounded half converges to an irrotational carrier equilibrium q0 with

    q0!=0, U(q0)!=0, D Omega(q0)=0,
    DB(q0)^T U(q0)=-b0 U(q0).

Its two level eigenvalues are real and satisfy

    lambda_-<=0<lambda_+,
    lambda_-+lambda_+=2+c.

At p0 the spectrum is {kappa,-b0,1}.

Proof. The line has a single covector rate rho, determined at p0 and transported along both halves. The escaping half has rho=-b0 by A1022/A1041. The bounded-half convergence theorem A657-A659 gives one irrotational endpoint q0 of that same rate, with the displayed level eigenvalue sign structure and sum 3c-rho. A nonflat endpoint would require -2kappa<=rho<-kappa. But

    -b0-(-kappa)=3c-1>0

in the campaign range. This contradicts rho<-kappa, so D Omega(q0)=0. The other conclusions follow from the confirmed endpoint theorem and 3c+b0=2+c. This proves B55. The comparison uses c>1/3 algebraically, but the exact-rate input audited here has the stated 2/5<c<1/2 scope. No extension of its hypotheses to the whole interval c>1/3 is asserted.

Flat means D Omega(q0)=0. It does not mean DU(q0)=0, does not specify higher jets, and does not exclude the connection. If both halves are bounded, there is no escaping-half argument pinning rho=-b0.

## 3. Time origins in vortex-line asymptotics

The sharpened Theorem VL(2) copied the limit e^(-ct)|y(t)|->1 from A1044 without copying its time-origin normalization. For an arbitrary chosen y0 on an escaping half and y(t)=Phi_t y0, the correct limit is

    e^(-ct)|y(t)| -> |Xi(y0)|>0.                 (3.1)

It equals one only when Xi(y0) lies on S^2. There is a unique finite carrier time shift making its length one, since Xi(Phi_s y0)=e^(sA)Xi(y0) and the length is e^(cs)|Xi(y0)|. This shift also rotates the unit representative. A1044 explicitly chooses y0=Xi^(-1)(w0) with w0 in S^2 and is correct as stated.

Thus the unqualified numerical limit one in the assembled VL statement needs this normalization. The positive decay rates and the spectra are unaffected. Likewise the vorticity limit expressed using lambda Aw0 must use lambda at that same normalized representative.

The B54 cleanup has otherwise repaired the earlier local swirl scope: the full carrier has the axial component c z e_z, pairwise orthogonality occurs at the crossing radius only when z=0, and the model is singular on the axis. Its local existence does not decide global sign control.

## 4. The precise escaping W2 trace assumptions

Now suppose Gamma is a lower-window periodic W2 witness and z(t)=Phi_t z0 is one of its escaping irrotational trace orbits. We use the confirmed trace conclusions A820-A822, A830 and A870-A871, written explicitly:

    Omega(z(t))=0, U(z(t))!=0, g(z(t))=0,
    H(z(t))=Hinf=Pinf,
    (B.grad)U=rho U-DB^T U on the trace,
    rho<=-b0,
    V(w)=W(w)=0, w in supp W,

where we choose z0 so that w=Xi(z0) belongs to S^2. The support conclusion refers to the sphere, by homogeneity. It comes from the trace's membership in the vortical closure and the scattering diffeomorphism, not from its own zero vorticity. The periodic witness is nonconstant, in the vortical closure, irrotational with D Omega=0 on Gamma, with the same covector rate rho and Floquet exponents {0,rho,3c-rho}. These are the existing W2 hypotheses, not assertions that every periodic orbit has this structure.

Write

    u(t)=U(z(t)), E(t)=DU(z(t)), n(t)=u(t)/|u(t)|,
    R_t=e^(omega tJ), x_t=e^(-tA)z(t),
    v_t(x)=e^(tL)U(e^(tA)x), T=DV(w).

The natural bounds and the exact logarithmic covector law imply

    E=E^T, tr E=0, |E(t)|=O(e^(-t)),
    |u(t)| e^(-(rho-c)t) -> C_u in (0,infinity).

Indeed d_t log|u|=rho-c-n.En, and n.En is absolutely integrable at infinity. The scattering equation gives

    x_t'=e^(-tA)u(t),
    x_t-w=O(e^((rho-2c)t)),
    z(t)-e^(tA)w=O(e^((rho-c)t)).                (4.1)

Since rho<=-b0, rho-2c<=-2. Uniform C^1 convergence of v_t on compact subsets of D gives

    M_t:=Dv_t(x_t)=e^t R_t E(t)R_t^T -> T.      (4.2)

This uses convergence at moving points in a fixed compact neighborhood. Positional closeness alone would not justify it.

## 5. Full transverse matrix and both coefficients

At every actual V zero with W=0, T is symmetric and trace free. Twisted homogeneity gives DV(x)Ax=-LV(x), so TAw=0. Thus T is either zero or a symmetric planar saddle on (Aw)-perp.

For large t let b(t)=B(z(t))/|B(z(t))| and q(t)=b(t) cross n(t). These are well defined and form an orthonormal frame because g=0. The covector law gives

    E(Az+2u)=(rho-c)u-omega Ju,
    n'=-omega Jn-En+sigma n,
    sigma=n.En.                                (5.1)

Therefore (R_t n)'=-R_t En+sigma R_t n=O(e^(-t)), and R_t n converges to a unit vector m_inf with error O(e^(-t)). By (4.1),

    R_t b(t)=Aw/|Aw|+O(e^(-2t))=:b_inf+O(e^(-2t)).

Consequently R_t q converges to q_inf=b_inf cross m_inf with error O(e^(-t)); the limiting frame is orthonormal. Taking the matrix limit (4.2) in that frame yields

    T = [[0,0,0],[0,C_n,C_s],[0,C_s,-C_n]],
    C_n=lim e^t n.En=m_inf.T m_inf,
    C_s=lim e^t q.En=q_inf.T m_inf.              (5.2)

In particular

    |T|_op=sqrt(C_n^2+C_s^2)=lim e^t|En|,
    T=0 if and only if C_n=C_s=0.               (5.3)

The old assertion using only C_n is false as a matrix inference. The matrix with C_n=0,C_s=1 satisfies symmetry, zero trace and TAw=0 but is nonzero. This is an algebraic counterexample, not an actual global W2 profile. A further argument forcing C_s=0 would be needed to recover the old criterion. The corrected source now retains both coefficients and withdraws the claim that one is freely prescribable.

## 6. Pressure Hessian, Riccati equation and remainders

The pressure Hessian bound is available under the stated full profile hypotheses. Define

    pi_t(x)=e^(b0 t)(P(e^(tA)x)-Pinf).

A533 gives v_t convergence in C^(1,alpha) on compact subsets of D for every alpha<1. The canonical pressure convergence and the rescaled Poisson equation

    -Delta pi_t=tr((Dv_t)^2)

then give uniform C^(2,alpha) bounds on smaller balls by the interior Schauder estimate; A539 proves convergence to P2 in these spaces. Under the coordinate change,

    D^2 pi_t(x)=e^(2t)R_t D^2P(e^(tA)x)R_t^T.

Evaluation at x_t in a fixed compact ball proves |D^2P(z(t))|=O(e^(-2t)). A finite cover of the unit sphere gives |D^2P(y)|=O(|y|^(-2p-2)) at infinity. This is a local elliptic estimate after justified velocity regularity. It is not differentiation of a gradient big-O estimate. The W^(2,q) route A538 also supplies that regularity, but is not necessary once A533 is available.

Differentiating the original profile equation along the irrotational trace gives

    E'+E^2+E+omega[J,E]=-D^2P.                  (6.1)

Differentiate sigma=n.En using (5.1). The rotation terms cancel and the exact scalar equation is

    sigma'+sigma=-3|En|^2+2sigma^2-n.D^2P n
       =-sigma^2-3|(I-nn^T)En|^2-n.D^2P n.    (6.2)

Omitting the shear-square term is incorrect. The actual estimate is sigma'+sigma=O(|E|^2)+O(|D^2P|)=O(e^(-2t)). Integration to infinity gives

    sigma=C_n e^(-t)+O(e^(-2t)),
    C_n=e^(t0)sigma(t0)
        +integral_(t0)^infinity e^s[-3|En|^2+2sigma^2-n.D^2P n] ds. (6.3)

The integral converges. No sign or vanishing follows just from this representation.

For the whole matrix, (6.1) gives

    M_t'=-e^t R_t(E^2+D^2P)R_t^T=O(e^(-t)).

Therefore M_t=T+O(e^(-t)). Combine this with the frame convergence in Section 5 to obtain

    q.En=C_s e^(-t)+O(e^(-2t)).                 (6.4)

These bounds justify both remainders in the revised source. They do not show that either coefficient can be specified independently of the profile.

## 7. Interpretation as derivatives of speed

Because U is nonzero along the trace, |U| is differentiable on a neighborhood of every trace point, and grad|U|=DU^T n=En there. Thus

    n.En=d_n|U|, q.En=d_q|U|, b.En=d_b|U|.

The tangential component is small: dot the first identity of (5.1), or its EB form, with n to get

    b.En=(rho-c-sigma)|u|/|B|
         =O(e^((rho-2c)t))=O(e^(-2t)).         (7.1)

Hence T=0 is equivalent to

    e^t |(I-bb^T)grad|U|(z(t))| ->0.

The two coefficients describe the normal and shear components of this speed gradient. This is an exact criterion on the specific trace, not an independent hypothesis known to follow from W2.

## 8. Scalar values and a further pressure-gradient dichotomy

The natural bounds and p>1 give H-P=|U|^2/2+(Ay).U ->0. The canonical P limit is Pinf, so Hinf=Pinf. Algebraically

    Q:=H-Hinf-g=P-Pinf-|U|^2/2.

The trace has H=Hinf and g=0, hence Q=0 identically. The locally uniform scalar tail limit at the moving points x_t gives

    e^(b0 t)Q(z(t)) -> S(w),

so S(w)=0. Since V(w)=0, also P2(w)=0. Thus w belongs to T0 exactly when T=DV(w)=0. No derivative premise is needed for the two scalar values.

There is an additional pressure-gradient consequence. The full tail correction A539 states, locally uniformly on D,

    e^t(v_t-V) -> DV V+grad P2.                 (8.1)

At x_t, V(w)=0 and (4.1) give

    e^t |V(x_t)|<=C e^t|x_t-w|
                =O(e^((rho-2c+1)t)) ->0.

Consequently (8.1) at x_t yields

    grad P2(w)=lim e^t v_t(x_t)
              =lim e^((2-c)t)R_t u(t).         (8.2)

Use the positive speed constant C_u and R_t n->m_inf. Since rho<=-b0,

    rho=-b0 implies grad P2(w)=C_u m_inf!=0,
    rho<-b0 implies grad P2(w)=0.              (8.3)

The same statements hold for grad S(w), since V(w)=0. Formula (8.3) does not pin rho for W2. It distinguishes the pressure gradient in its allowed range. Unlike the W1 actual vortical zero, this W2 point has W(w)=0; the W1 resonance classification cannot simply be copied to it.

## 9. What dense vorticity would imply at the W2 point

Let Z=int{k=0}. If w lies in Z, the actual nilpotence consequence A1107 gives T=0 because V(w)=W(w)=0. If w is on boundary Z, A973 gives T=0. If w is outside closure Z and W!=0 is dense in some full neighborhood, A1095/A1122 gives T=0. It follows that a nonflat escaping W2 direction must be outside closure Z and must have an open irrotational patch in every neighborhood.

In particular, if vorticity is dense in some full neighborhood of the escaping direction, that direction is in T0. If additionally it is outside Z, A1122 gives grad P2(w)=0, and (8.3) forces rho<-b0. Thus the case rho=-b0 at a densely vortical direction can occur only inside Z under the present arguments. These are conditional restrictions, not a proof of density.

## 10. Source comparison, provenance and scope

B55 in Theorem VL(13), the corrected W2 Remark (xlvii), the accompanying source notes and all 460 lines of the external referee (a second model) w2dv response were read. The matrix and scalar corrections agree with the independent derivations above. The pressure-Hessian argument agrees with A533/A539, whose exact regularity statements and pressure proof were reread. The source response states that its model consultation failed credential retrieval. It is not a model review, and no replacement model is counted.

B55's source is the configured model agent. The same agent's nested w2dv response is an the external referee (a second model) source. Existing configured model agents have received the auditor's matrix correction through agent notes; a focused response to the additional pressure-gradient dichotomy and the dense-vorticity restriction is pending. No new agent, client or remote computation was started here.

The proof does not exclude mixed W1 connections, W2 periodic witnesses, flat T0 points, nonflat directions with accumulating open irrotational patches, or general bare-decay profiles. It does not claim logical undecidability of the coefficients from all possible along-orbit arguments. It records only what these checked estimates establish. Every statement retains arbitrary finite omega, with constants allowed to depend on it.

Confirmed dependencies are A657-A659, A1022/A1041, A820-A822, A830, A870-A871, A533/A539, A973, A1107 and A1122. The separate time normalization correction does not alter any of those theorems. No numerical calculation or formal build was needed.
