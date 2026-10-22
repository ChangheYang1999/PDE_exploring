# Smooth local sufficiency of the compatibility equation

Status: CONFIRMED by independent proof,190 exact controls,9 finite-point smooth-flat controls, and written actual claude-opus-5-5 audits196 and197, 2026-10-21. The informal proof was written before implementation. This is a local criterion for prescribed fields, not an existence or nonexistence theorem for B2.

## Statement and notation

Let k be real. Let V(x,y) and t(x,y) be smooth and even in x on a neighborhood of (0,0), with V(0,0)=0, a=V_y(0,0)>max(k,0), and t(0,y)=0. Put J=V_x. Suppose V_xx(0,0) is nonzero. Define

    M_V t=J^2 t_y-J V t_xy+[V J_y+J(k-V_y)]t_x.       (1)

If M_V t=0 on a neighborhood of0, then t=0 on a possibly smaller neighborhood of0. Conversely t=0 implies(1)=0. All functions and the equation here are local. No analyticity, sign of V_xx, or global growth assumption is needed.

For the B2 application let beta>0, k=beta-2, let Psi be smooth and odd in x, and set

    W=beta(x,y)+(-Psi_y,Psi_x)-(-Psi_y(0),Psi_x(0)),
    Omega=-Delta Psi, F=W.grad Omega+Omega,
    T(x,y)=integral_0^x F(s,y) ds,
    t=W.grad T-kT.

Assume Psi_xy(0)=1+beta/2 and Psi_xxx(0) is nonzero. Then W2 is even, W2(0)=0, W2_y(0)=1+3beta/2>max(beta-2,0). Also T and t are smooth even in x, and t(0,y)=0. Define

    J=partial_x W2, D=(k-partial_x W1)F-W.grad F,
    Z=W1 F J+W2 D,
    E=J Z_y-Z J_y-k J D.                              (2)

On a neighborhood of0, E=0 if and only if the normalized primitive T solves both B2 transport equations there. The vorticity transport already holds by T_x=F. This criterion does not assert the global relative inverse, growth, or center coefficient of an arbitrary prescribed stream.

## A one-dimensional uniqueness lemma

Let v be smooth near y0, v(y0)=0 and v'(y0)=a>max(k,0). Every bounded smooth solution h of

    v h'+(v'-k)h=0                                   (3)

near y0 is identically zero on a smaller interval. Indeed v(y0+s)=a s+O(s^2), so

    (v'(y0+s)-k)/v(y0+s)=(1-k/a)/s+O(1).

On each side of y0 a nonzero solution is a nonzero constant times

    |s|^{k/a-1} exp(O(s)).

The exponent is negative. Thus every nonzero solution is unbounded as s tends to0. Boundedness forces zero on each side, and continuity gives zero at y0. On an interval where v has this single zero, ordinary linear ODE uniqueness extends the zero solution throughout each side of the interval. This uses an actual equation and boundedness, not a formal Taylor argument.

## Proof of the local theorem

Shrink to a rectangle on which V_y>max(k,0), J=x j(x,y) with smooth j bounded away from0, and V(x,.) has exactly one zero y=r(x) in the vertical interval for every x in its horizontal interval. For a fixed small vertical half-width epsilon, shorten the horizontal interval until V(x,-epsilon)<0<V(x,epsilon) throughout; monotonicity then gives one zero in every vertical slice. Such a rectangle exists by the implicit function theorem and continuity: V(0,0)=0, V_y(0,0)>0, and j(0,0)=V_xx(0,0) is nonzero. The fundamental theorem of calculus gives

    j(x,y)=integral_0^1 V_xx(s x,y) ds.

Evenness and t(0,y)=0 similarly imply t_x=x tau for smooth tau. Hence

    B=t_x/J=tau/j

has a smooth extension across x=0. Put A=t-V B. Since t_x=J B and V_x=J, exact differentiation gives

    A_x=-V B_x.                                     (4)

For x!=0, dividing(1) by J^2 and using the quotient rule gives

    M_V t/J^2=t_y-V B_y+(k-V_y)B=A_y+kB.              (5)

All quantities on the right are smooth across the axis. Thus M_V t=0 implies A_y=-kB on the whole rectangle. Differentiate this identity in x and differentiate(4) in y. Equality of mixed derivatives gives

    V (B_x)_y+(V_y-k)B_x=0.                           (6)

For each fixed x the preceding lemma applies at y=r(x), since V_y(x,r(x))>max(k,0). Smooth B_x is bounded there, so B_x=0 throughout that vertical interval. Therefore B(x,y)=B0(y) on the rectangle.

Using t(0,y)=0 and integrating t_x=V_x B0 gives

    t(x,y)=[V(x,y)-b(y)]B0(y), b(y)=V(0,y).

Consequently A=-b B0. The identity A_y=-kB0 becomes

    b B0'+(b'-k)B0=0.                               (7)

Apply the lemma again at y=0, where b(0)=0 and b'(0)=a>max(k,0). It gives B0=0 on the smaller interval, hence t=0 on a smaller rectangle. This proves the theorem. The assumption t(0,y)=0 is used here on an interval, not just to finite order at the center.

## Verification of the B2 reduction

Odd Psi gives even W2 and odd W1, Omega and F. Thus T is even, T(0,y)=0, T_x(0,y)=F(0,y)=0 and T_y(0,y)=0. Hence t(0,y)=0. Moreover J_x(0)=Psi_xxx(0), so the nondegeneracy assumption matches that of the local theorem. The identity

    E=M_(W2) t                                      (8)

is the exact residual identity of packet137 with vorticity residual F-T_x=0; its direct derivation uses only product rules and the definitions(2). The local theorem applied to V=W2 proves sufficiency. Necessity follows either from(8) or the no-division compatibility identity of packet124.

## Dependencies and scope

The scalar uniqueness theorem is proved here from elementary one-dimensional ODE uniqueness and the implicit function theorem. The application depends on packet137 only for the algebraic identity(8), also checked independently in symbolic controls. Unlike packet138, the theorem does not infer equality from a Taylor series. It rules out smooth flat residuals under the explicit nonzero cubic stream derivative. It does not settle streams for which Psi_xxx(0)=0, nor global continuation of a locally vanishing residual in the smooth category. An analytic whole-plane continuation remains available under packet138's hypotheses. No B2 candidate or full NO result follows.

## Extension to uniform finite order in x

The scalar theorem remains true if V_xx(0)!=0 is replaced by the following explicit factorization on a neighborhood:

    J=x^m j(x,y), m a fixed positive odd integer,
    j smooth, j(0,0)!=0.                             (9)

The first theorem is m=1. This is a uniform order along an axis interval, not the weaker assertion that J is nonflat at the single point0. The other hypotheses are unchanged.

To prove the extension, shrink so j is nowhere zero, V_y>max(k,0), and every vertical slice has exactly one simple zero as above. Set h=t_x and c=J_y/J=j_y/j, which is smooth. For x!=0, M/J=0 is

    J t_y-V h_y+(V c+k-V_y)h=0.                      (10)

The left side is smooth, so(10) holds on the whole rectangle. Put b(y)=V(0,y), j0(y)=j(0,y). Integrating V_x=x^m j yields V=b+O(x^(m+1)) with a smooth remainder, and likewise V_y=b'+O(x^(m+1)). We prove, successively for ell=0,...,m-1, that

    h_ell(y)=partial_x^ell h(0,y)/ell! =0            (11)

on a fixed smaller axis interval. Suppose this is known for all lower indices. The coefficient of x^ell in(10), computed by ell differentiations at x=0, is

    -b h_ell'+[b j0'/j0+k-b']h_ell=0.               (12)

Indeed J t_y has x-order at least m>ell; the x-derivatives of V and V_y through order m vanish on the axis except order0; and every nonconstant coefficient of c multiplies a previously vanishing h index. For u_ell=h_ell/j0, equation(12) is

    b u_ell'+(b'-k)u_ell=0.

The scalar lemma gives u_ell=0 near0 and ordinary uniqueness propagates zero through the same interval on either side of b's sole zero. Thus (11) holds. There are only m steps, so one common rectangle suffices. Taylor's formula with integral remainder now gives h=x^m tau for smooth tau, hence B=h/J=tau/j extends smoothly. The remainder of the main proof, equations(4)-(7), applies without change and proves t=0.

This extension includes only streams whose Psi_xx has the exact uniform factorization(9). It does not cover arbitrary nonflat J with extra zeros approaching the center, or a flat J. It provides no global B2 endpoint. The argument was written before its additional100 exact coefficient controls and actual claude-opus-5-5 audit197, both of which confirm the stated extension.

## A scalar counterexample when the uniform order is dropped

The weaker scalar assertion with merely nonflat J is false at k=0. This is a limitation of the scalar argument, not a counterexample to the constrained B2 compatibility implication. The following calculation was checked in writing by actual claude-opus-5-5 audit198; independent symbolic controls are recorded separately.

Fix a>0 and q real. On a sufficiently small rectangle set

    b(y)=a-qy/2, A(x,y)=b(y)+x^2/2,
    V(x,y)=y A(x,y), J=V_x=xy,
    t(x,y)=A(x,y) integral_0^x s^3/A(s,y)^2 ds
          =2 A log(A/b)-x^2.                         (13)

Both A and b are strictly positive on this rectangle. Thus t is real analytic and even in x, t(0,y)=0, and its first nonzero Taylor term is x^4/(4a). In particular t is nonzero. The field V has V(0)=0 and V_y(0)=a>0=max(k,0). Although J is nonflat, it has no factorization x^m j with a fixed positive integer m and j nowhere zero near0: at m=1 the quotient is y, and larger m would give a singular quotient off the transverse zero.

Differentiating the integral in(13) gives

    A t_x-x t=x^3,
    x t_y-A t_xy-A_y t_x=0.                          (14)

Substitution of V=yA, J=xy and k=0 into(1) gives exactly

    M_V t=xy^2 [x t_y-A t_xy-A_y t_x]=0.             (15)

Consequently parity, analyticity, high-order vanishing of t, and a nonflat J alone do not imply scalar uniqueness. Uniform nonvanishing of j in(9) has substantive content.

This V can be the second B2 transport component at beta=2. Indeed

    Psi=(a-2)xy-qxy^2/2+x^3 y/6

has Psi_x(0)=0 and 2y+Psi_x=V. At a=4 its center strain is Psi_xy(0)=2=1+beta/2; also -Delta Psi=qx-xy and its center vorticity slope is q. Choosing q=2a0 matches 4a0/beta. These statements check only the local stream and center data. They do not assert that the t in(13) is the thermal residual of the normalized vorticity primitive for this stream. That primitive is fixed by F=W.grad(-Delta Psi)-Delta Psi, and cannot be chosen independently. Neither a B2 candidate nor a failure of B2 compatibility sufficiency follows from this scalar example. In particular, the beta>2 analytic result of packet138 is unaffected.

Audit198 also confirms a correction to an unused suggestion in audit197: a positive finite power at a second simple zero does not permit a C-infinity solution to be patched from zero on one side to nonzero on the other. A nonzero finite power has a derivative obstruction at some finite order. Only this zero-to-nonzero conclusion is used here; the audit's claim about equality of coefficients on both sides in an absolute-value basis requires a parity sign for odd integer powers. The main proof above uses a negative exponent at a single simple zero and is independent of either suggestion.
