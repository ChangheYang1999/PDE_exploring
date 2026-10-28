# Noncompact cutoff errors in the actual Holder graph

## Statement

Fix 0<alpha<1 and 4k<gamma<2. Use the common physical parity space Y=E2 intersect L2(w_gamma), its sum norm and the closed maximal actual operator L_ren=T+C_ren of proof 214. Thus

 T=V.grad-1,
 C_ren h=U[h].grad rho0+c[h]H0,
 H0=chi0 X.grad rho0/3,
 D_Y={h in Y:V.grad h belongs to Y distributionally}.

Let chi be a smooth compactly supported function even in both coordinates. Suppose there is a point Q=(x0,y0) off both axes, inside one analytic radial interval of the modal background, with

 V1(Q)!=0, a(Q)!=0, a=V.grad chi.                   (1)

Assume a neighborhood of Q and its four reflections is disjoint. Then multiplication by a, equivalently the transport commutator [T,chi], is a bounded but noncompact map D_Y, with its graph norm, into Y. The full commutator

 [L_ren,chi]=L_ren(chi h)-chi L_ren h

is also a bounded but noncompact map D_Y->Y. Noncompactness holds on graph-bounded sequences of compact smooth inputs with exact c=J=0. All their full nonlocal images belong to Y.

There is also an exact local-parametrix consequence. Take the actual-variable origin extension L_delta and its E2 inverse R_delta from topics202,212,215. Choose delta sufficiently small; take chi supported where L_delta and L_ren agree pointwise as operator expressions, with a point Q satisfying (1) in its transition region. Choose a smooth radial eta equal1 on B_delta. Then

 K=chi R_delta eta:Y->D_Y

is bounded with the graph norm, but the bounded residual operator

 E=L_ren K-chi eta:Y->Y                             (2)

is not compact. This concerns this explicit cutoff construction; it is not a theorem against every possible localization or gluing strategy. In particular neither global invertibility nor its failure follows. Smallness or invertibility of the actual assembled error remains open.

## Fixed flow-box geometry and smooth inputs

Take a smaller neighborhood of Q contained in its analytic radial interval and avoiding both axes and all its reflected copies. The finite exact angular formulas and the radial Green equations give an analytic actual transport there. The following construction only needs smoothness on this box. Let Phi_s be its local flow and set

 F(s,z)=Phi_s(x0,y0+z).

Since V1(Q)!=0, the two derivatives at (0,0), V(Q) and (0,1), are independent. On a sufficiently small rectangle F is a smooth diffeomorphism. In these coordinates

 V.grad s=1, V.grad z=0,
 F(0,z)=(x0,y0+z).                                  (3)

Choose smooth compact eta1(s),theta(z), equal1 near0, whose supports lie in this rectangle. On this single box define

 u_n(F(s,z))=n^(-alpha) eta1(s)theta(z)cos(nz),

and extend by zero, then reflect evenly in x and oddly in y. The four supports are disjoint. The resulting u_n is compact and smooth, vanishes near both axes, and has J(u_n)=0.

Splitting differences at length 1/n in these fixed smooth coordinates gives

 ||u_n||infinity<=C n^(-alpha),
 ||u_n||C^alpha<=C,
 ||T u_n||C^alpha<=C.                               (4)

For the last bound use (3): the transport differentiates eta1 only, and never differentiates cos(nz). The supports stay in a fixed compact set with |x| bounded below, so the ordinary Holder bounds imply the E2 bounds. The weighted L2 norms are at most C n^(-alpha). Hence u_n and T u_n are uniformly bounded in Y. Proof 214 gives bounded C_ren on Y and complete image membership, so u_n is bounded in the actual full graph.

The strain kernel is smooth on these supports. Changing variables by F writes its contribution as n^(-alpha) times an integral of cos(nz) against a compact smooth amplitude in (s,z). Integrate once in z, with no endpoint term, to obtain

 |c[u_n]|<=C n^(-alpha-1).                           (5)

Choose a fixed smooth physical-parity input q, compact away from both axes and from all four flow boxes, with J(q)=0 and c[q]=1. Such q is obtained by reflecting a positive bump in a sufficiently small box where the nonzero strain kernel has fixed sign, and dividing by its nonzero integral. Set

 h_n=u_n-c[u_n]q.                                   (6)

Then c[h_n]=J(h_n)=0. Its transport image is compact in Y; its full coupling image belongs to Y by proof 214. Equations (4),(5) show that h_n remains graph-bounded and ||h_n||infinity->0. On a smaller box about Q the correction vanishes identically.

## Noncompactness of the transport commutator

Multiplication by every fixed smooth compact even coefficient preserves Y. On E2 this follows from the supported-endpoint product difference, using |h(x,y)|<=||h||E2 x^2|y|^alpha for the weighted vertical term. Its weighted L2 bound is immediate. Thus multiplication by chi and a is bounded on Y. The distributional Leibniz identity proves that chi preserves D_Y and

 [T,chi]h=a h.                                      (7)

At the two vertical points Q and Q_n=(x0,y0+pi/n), equation (3) and the cutoffs give

 h_n(Q)=n^(-alpha), h_n(Q_n)=-n^(-alpha)

for all sufficiently large n. Since a(Q_n)->a(Q)!=0, the difference quotient satisfies

 |a(Q)h_n(Q)-a(Q_n)h_n(Q_n)|/(x0^2(pi/n)^alpha)
       ->2|a(Q)|/(x0^2 pi^alpha)>0.                 (8)

But ||a h_n||infinity->0. Any convergent subsequence in Y would therefore have limit0, contradicting (8). This proves noncompactness even on exact zero-strain and zero-jet smooth inputs.

## Why the nonlocal commutator does not cancel this sequence

We prove a useful estimate on inputs supported in a fixed compact set K separated from the vertical axis and the origin, with both physical parities:

 ||[C_ren,chi]h||Y<=C_K ||h||infinity.               (9)

The commutator velocity W=U[chi h]-chi U[h] has no contribution from the local multiplier term of U2. For compact parity inputs the canonical subtraction constants vanish. Thus its integral kernel is, componentwise,

 (chi(Y)-chi(X)) K_i(X-Y),                           (10)

where |K_i(Z)|<=C|Z|^(-2) and |D K_i(Z)|<=C|Z|^(-3). The diagonal singularity is reduced to |X-Y|^(-1), which is locally integrable.

For completeness (10) maps compactly supported L-infinity inputs to C^alpha with bound C_K||h||infinity for every alpha<1. Its supremum follows by integrating the |X-Y|^(-1) bound near the diagonal and the bounded separated kernel elsewhere. For a difference of length d<1/2, integrate separately over the union of the two disks of radius2d and its complement. The former contributes C||h||infinity d. On the latter the X derivative of (10) is bounded by C|X-Y|^(-2) on bounded sets, so its contribution is at most C||h||infinity d(1+|log d|). Far from K all kernels and derivatives decay and satisfy the same bound. Since d(1+|log d|)<=C_alpha d^alpha, this proves

 ||W||C^alpha<=C_K,alpha ||h||infinity.              (11)

This proof uses no derivative or Holder norm of h.

To check the stronger axis-weighted image, let dist(K,{x=0})>=b>0. On |x|<b/2 all source points in (10) are separated. Derivatives in x and y of W of every fixed order are bounded by C_K||h||infinity, uniformly in y. Multiplication by chi(X) contributes only fixed bounded derivatives. Parity gives W1(0,y)=0, so division by x gives uniformly bounded W1/x and its first y derivative there; W2 and its first y derivative are bounded as well. The actual coefficients

 a1=rho0_x/x, a2=rho0_y/x^2

have bounded supremum and bounded first y derivative globally, using the local C^(4,1) division at0, the compact radial joins, and the decaying outer modal formulas. Thus

 (W.grad rho0)/x^2=a1(W1/x)+a2 W2

has a uniformly bounded y-Holder seminorm on the axis strip. For |x|>=b/2 the same seminorm follows directly from (11), the bounded C^alpha gradient of rho0 and x^(-2)<=4/b^2. This includes every vertical pair. The ordinary x seminorm and supremum follow from (11) and the bounded C^alpha gradient. Therefore

 ||W.grad rho0||E2<=C_K||h||infinity.                (12)

The weighted L2 bound follows from proof 214's weighted multiplier bound:

 ||W||L2(w_gamma)<=C||h||L2(w_gamma)<=C_K||h||infinity.

The background gradient is bounded, so multiplication proves the weighted L2 part of (9). Finally

 [C_ren,chi]h=W.grad rho0+c[chi h]H0-chi c[h]H0.

Both strain integrals have smooth bounded kernels on K and are at most C_K||h||infinity. Their fixed columns belong to Y. This proves (9).

The sequence (6) is supported in one such fixed K, including the correction q. Thus (9) gives

 ||[C_ren,chi]h_n||Y->0.                            (13)

Together with (7),(8), this excludes compactness of the full [L_ren,chi]. There is no possible cancellation of the transport lower bound by the nonlocal commutator on this sequence. Boundedness on the entire graph also follows from the bounded C_ren and cutoff multipliers.

## The actual origin cutoff parametrix

Choose delta as in proof 215. The coefficient cutoff of L_delta is1 on B_(delta/2), and choose that disk small enough that chi0=1 there. Choose chi supported inside B_(delta/2), with a transition point off the axes. Such a point can satisfy (1): near the origin V=(-A0 x,D0 y)+O(r^3), so choose a nonzero sufficiently small x with a smaller nonzero y on a radial cutoff transition; V.grad r has a nonzero negative leading term. Move the radius slightly if needed to avoid a radial knot. The construction is then inside an analytic radial interval. Choose q in (6) inside B_(delta/2) while avoiding the four boxes and the axes.

The common-space cutoff bounds of proof 213 give K:Y->Y. More precisely R_delta eta:Y->E2 is bounded. Its E2 transport image is eta f-B_delta R_delta eta f. Multiplying this identity by chi, where actual and extended transports agree, and applying the fixed compact E2-to-Y comparison shows V.grad(Kf) belongs to Y with a bounded norm. Proof 214 supplies its complete global coupling image. Hence K:Y->D_Y is graph-bounded and the error (2) is a bounded Y operator.

For the sequence (6) define f_n=L_delta h_n. All terms of f_n are supported in B_delta: h_n and its transport image are supported in B_(delta/2), and the coupling is explicitly cut off in B_delta. Its E2 norm is bounded by the same fixed flow-box estimates and the bounded B_delta; the compact-support comparison bounds its weighted L2 norm. Thus f_n is bounded in Y, eta f_n=f_n, and exact maximal-domain inversion gives R_delta eta f_n=h_n.

On the support of chi, the two full operator expressions L_delta and L_ren agree for every E2 input, including the canonical nonlocal velocity and normalized strain column. Therefore

 E f_n=L_ren(chi h_n)-chi L_delta h_n
       =[L_ren,chi]h_n.                             (14)

The right side has no convergent subsequence by the preceding construction. This proves that E is not compact. An automatic compact-error claim for this patch is therefore false; a successful scheme must estimate or otherwise invert its actual transport error. This result does not rule out small norm, a flow-adapted partition, a different graph topology, or a direct global inverse argument.

Dependencies: topics213 and214 for Y, full mapping and maximal domains; topics202,212,215 for the actual origin extension inverse; the exact modal formulas for a regular analytic flow box. Every perturbation, image, reflection, cutoff and normalization correction is checked above. No numerical calculation or operator-inverse conclusion is made.
