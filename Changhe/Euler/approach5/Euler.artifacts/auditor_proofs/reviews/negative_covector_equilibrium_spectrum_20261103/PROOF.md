# Spectra at nonzero equilibria in an exceptional support

Status: independent reconstruction of LIT101, checked against the focused configured-model review. The final verdict is recorded in the auditor's ledger (AUDIT_LEDGER.md). This is a necessary condition, not a realization or exclusion theorem.

## 1. Hypotheses and statement

Assume U in C2(R3;R3), P in C1 solve the full rotating incompressible profile equation, uniformly U=o(|y|), and U.curl U=0 globally, with 0<c<1/2 and omega arbitrary. Write

    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, kappa=1+c, d=3c, D=d+kappa,
    H=P+|U|^2/2+(Ay).U, g=U.B.

Let mu have compact support S and be invariant and ergodic for the whole B flow. Assume B!=0,W=0,DW!=0,D(B cross W)=0 almost everywhere. The confirmed A444-A445 conclusions give H=h and W=g=0 on S, grad H=-aU, and grad g=-kappa U wherever U!=0. Any zero of U in S is the spatial origin and a carrier equilibrium.

For p in S with B(p)=0 and p!=0 put u=U(p)=-Ap, N=DB(p), K=DW(p). Then u!=0,

    N^T u=-kappa u, T=u^perp is N-invariant,
    spec(N|T)={lambda,D-lambda}, lambda<=0,
    spec N={-kappa,lambda,D-lambda}.                      (1)

All these eigenvalues are real, counted with multiplicity. The largest Lyapunov exponent of the backward equilibrium atom is max(kappa,-lambda). If K!=0, then

    lambda=0, spec N={-kappa,0,D},
    K=v tensor u for a nonzero v in ker N intersect T.   (2)

In particular a nonflat nonzero equilibrium in S is nonhyperbolic. A hyperbolic nonzero equilibrium in S must instead have K=0 and lambda<0. The origin with U=0 is outside this theorem.

## 2. Covector and trace

A is invertible because c>0. At B(p)=0, differentiating g=U.B gives grad g(p)=N^T u. The A444 identity proves N^T u=-kappa u. Thus T is invariant and the one-dimensional quotient has eigenvalue -kappa. Since div B=d,

    tr(N|T)=d+kappa=D>0.                                (3)

This argument does not assume DW(p)!=0.

## 3. The tangential linearization cannot be a forward source

Since grad H(p)=-a u!=0 and H is C2, near p the level H=h is a C2 surface M. The field

    Btilde=B-(BH)grad H/|grad H|^2

is C1, tangent to M, and agrees with B on the nearby portion of S. At p, BH=0 and d(BH)=-a dg=-kappa dH, so its tangent derivative is L=N|T. These assertions differentiate the correction once only. Its backward surface linearization is -L.

Suppose both eigenvalues of L had positive real part. Set

    Q=integral_0^infinity e^(-t L^T)e^(-t L) dt.

The integral converges, Q is positive definite, and L^T Q+QL=I. In a C2 surface chart the backward projected field is x'=-Lx+o(|x|). The derivative of x^T Qx is -|x|^2+o(|x|^2), strictly negative for small nonzero x. A sufficiently small sublevel neighborhood is forward invariant for this backward field, and the same inequality gives exponential convergence to p there.

Because p is a support point, that open surface neighborhood meets S in positive mu measure. To see the measure assertion in ambient terms, choose an ambient neighborhood whose intersection with M lies in the sublevel neighborhood; all nearby S lies in M. On S, uniqueness identifies projected and original backward trajectories. Thus a positive-mu subset has backward empirical limit delta_p. Whole-flow ergodicity makes that limit mu at almost every point, which would imply mu=delta_p, contrary to mu({B=0})=0. Hence L cannot have both eigenvalues with positive real part.

A real two-by-two matrix of trace D>0 has either a complex conjugate pair with real part D/2, or two real eigenvalues summing to D. The complex case and the case of two positive real eigenvalues are excluded. Thus the eigenvalues are lambda<=0 and D-lambda>0, proving(1). Exponents of a constant matrix are its eigenvalue real parts; possible Jordan factors contribute only polynomial growth. The backward top exponent is therefore max(kappa,-lambda).

## 4. A nonzero first vorticity derivative forces a zero tangent eigenvalue

Differentiating global U.W=0 at W(p)=0 gives u^T K=0, so image K is contained in T. Differentiating the exact Cauchy law in space at this equilibrium gives

    K e^(tN)=e^(-kappa t)e^(tN)K.

U in C2 and W in C1 suffice: the term with the second spatial derivative of the flow is multiplied by W(p)=0. Differentiation in t, not a second differentiation of W, yields

    N K-K N=kappa K.                                    (4)

Restrict to T. The map K_T:T->T satisfies L K_T-K_T L=kappa K_T. The two tangent eigenvalues are distinct, and in their real eigenbasis the output-minus-input differences are0 and plus or minus(D-2lambda). Since D-2lambda>=D>kappa, none equals kappa. Thus K_T=0.

This reasoning diagonalizes only L. It remains valid if -kappa is also a tangent eigenvalue, so the ambient N may have repeated eigenvalues. If K!=0, it annihilates T and has image in T; therefore K=v tensor u for a nonzero v in T. Substitution in(4), using u^T N=-kappa u^T, gives Nv=0. The nonpositive tangent eigenvalue is then lambda=0, proving(2). Also K^2=0 and rank K=1.

## 5. Scope

No existence of an equilibrium in S is needed for this conditional theorem. The separate LIT100 support conclusion supplies an equilibrium but does not alone exclude the origin. For any nonzero equilibrium actually in S, its atom witnesses a backward exponent at least kappa, even though mu itself gives equilibria measure zero. If S is contained in the component core K_E used to define Gamma_E, this atom is an admissible measure there. The exceptional measure itself already witnesses exponent kappa; the atom improves that lower bound only if -lambda>kappa, which requires DW(p)=0. No approximation of mu by atoms is asserted.

The flat case permits lambda<0 without an upper bound on -lambda. The nonflat case gives the nonhyperbolic spectrum(2), not its impossibility. The proof uses A444-A445, exact Lamb and Cauchy identities, C1 flow uniqueness and the explicit elementary Lyapunov argument. No compact-surface classification, simulation or formal build is used.
