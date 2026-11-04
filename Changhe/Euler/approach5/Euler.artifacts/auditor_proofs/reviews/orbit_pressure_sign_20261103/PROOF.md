# Work and pressure signs on a supported irrotational orbit

## 1. Exact class, normalization and previously verified inputs

Fix 2/5<c<1/2 and any finite real omega. Let U in C^2(R^3;R^3), P in C^1(R^3) satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1),
    p=(1-c)/c, Jx=(-x2,x1,0), A=cI-omega J.

Put a=1-2c>0, b=2(1-c), kappa=1+c, B=Ax+U and Omega=curl U. Use the constant pressure limit Pinf already established in this exact natural class, and normalize

    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2,
    g=U.B=H-Q.

The verified C47 inputs are used without weakening their hypotheses: the complete C^2 carrier flow Phi_t; compact forward-bounded core K with open complement E; the C^1 scattering diffeomorphism Xi:E->D=R^3 minus {0}; actual tails V,W=curl V,P2; and

    W(Xi y)=DXi(y)Omega(y), DXi(y)B(y)=A Xi(y),
    grad H=-aU+B cross Omega, BH=-ag.

H,Q,g are C^2, bounded and tend to zero at infinity. Every backward half orbit is bounded and every orbit in E escapes to infinity forward. The rank tensor T=grad H cross grad g vanishes on the open invariant set E intersect {Omega!=0}. At a zero of Omega, N=DOmega is nilpotent, NB=0, N^T U=0, and

    DOmega(Phi_t y)=exp(-kappa t)DPhi_t(y)N DPhi_t(y)^(-1).

At a zero x of W, W is differentiable and DW=DXi N DXi^(-1). The tail expansions, with X=Ax, k=X.V and S=P2-|V|^2/2, are

    exp(at)H(Phi_t y)->k(Xi y),
    exp(bt)[H(Phi_t y)-exp(-at)k(Xi y)]->-aS(Xi y).

These are A1005, A1106 and A1180-A1188 at their established scope. The classification A1186 also gives DV(x)=0 and DW(x)=X tensor l whenever V(x)=W(x)=0 and DW(x)!=0. No smoothness of W away from its zeros is assumed here.

## 2. Exact sign theorem and support transport

Let x0 in D intersect supp W satisfy W(x0)=0 and range DW(x0) contained in R X0, where X0=Ax0. Put y0=Xi^(-1)(x0), y_t=Phi_t y0. Then

    g(y_t)<=0, H(y_t)<=0 for every real t,
    H(y_t)=a integral_t^infinity g(y_s)ds,
    k(x0)<=0, and k(x0)=0 implies S(x0)>=0.

To transfer the hypothesis, DXi(y0) conjugates N0=DOmega(y0) to DW(x0) and sends B(y0) to X0. Therefore range N0 is contained in R B(y0). The Cauchy law keeps Omega zero along the entire orbit, and the derivative transport keeps range DOmega(y_t) contained in R B(y_t). Also B(y_t)!=0, since DXi B=X0!=0 initially and flow derivatives are invertible.

The exact push-forward and invertibility identify Xi(E intersect {Omega!=0}) with {W!=0} in D. Thus y0 belongs to the closure of that original vortical open set. Its closure is invariant, so every y_t does as well. Since T is C^1 and is identically zero on the open set, both T and DT vanish on the entire orbit. This first-derivative conclusion is essential.

## 3. The second-derivative identity at a nonzero velocity point

At an orbit point with DOmega=0 and U!=0, let M=DU. Since Omega=0 and div U=0, M is symmetric and trace free. For alpha=B cross Omega, Dalpha=0 there. Hence grad H=-aU and Hess H=-aM.

From T=0, grad g=rho U, where rho=(U.grad g)/|U|^2 is C^1 near the point. Differentiating T in an arbitrary direction h and using DT=0 yields

    U cross (Hess g-rho M)h=0.

The symmetric matrix Hess g-rho M has range contained in R U, so it equals tau U tensor U for a real tau. The trace fixes its sign. Since Delta U=-curl Omega=0 and M is symmetric and trace free,

    Delta g=Delta U.(Ax+2U)+2<M,A>+2|M|_F^2=2|M|_F^2,
    tau |U|^2=2|M|_F^2>=0.                                  (1)

The skew rotational matrix contributes zero to <M,A>. No sign is assigned to an uncomputed pressure Hessian.

On any time interval satisfying these point hypotheses, differentiating grad g(y_t)=rho(t)U(y_t) gives

    g'=rho g, rho'=tau g, tau>=0.                             (2)

The second equality follows by applying Hess g=rho M+tau U tensor U to B and cancelling rho M B. All derivatives used are available at C^2 velocity regularity.

## 4. Positive work is impossible

Suppose g(y_t0)>0 and take its maximal positive time interval I. At every point of I, range DOmega is contained in R B, so DOmega=B tensor l. The helicity derivative gives

    0=DOmega^T U=g l.

Thus DOmega=0 on I and U!=0 there. Equation (2) applies and f=log g satisfies f''=tau g>=0. Convexity gives a tangent-line lower bound at t0 throughout I. A finite endpoint of I would have g approaching zero, hence f approaching minus infinity, contradicting that lower bound. Therefore I is all of R.

The global boundedness of g makes f bounded above on R. A convex differentiable function on R bounded above is constant: a nonzero slope would make its tangent line unbounded in one time direction. Hence g is a positive constant on the orbit. But H'=-ag would then make H unbounded, contradicting the bounded H in this class. Equivalently, forward escape and g tending to zero give the contradiction. Thus g<=0 at every time.

Integrate H'=-ag from t to T and let T tend to infinity. H(y_T) tends to zero. Since g has one sign, the improper integral exists and

    H(y_t)=a integral_t^infinity g(y_s)ds<=0.

H is nondecreasing. This proves the work and Bernoulli parts without requiring the orbit to lie in a compact invariant set.

## 5. Tail signs and the backward limit set

The first tail expansion and H<=0 give k(x0)<=0. If k(x0)=0, the second gives -aS(x0)<=0, hence S(x0)>=0. At V(x0)=0 this is P2(x0)>=0.

The backward orbit is bounded, so its alpha-limit set A0 is nonempty, compact and invariant. Invariance and compactness imply that every point of A0 has a bounded forward orbit, hence A0 is contained in K. Along y_t, Omega=0 and range DOmega is contained in R B, so D(B cross Omega)=0. These closed conditions and membership in the vortical closure pass to A0.

The nondecreasing bounded H has a limit H_- as t tends to minus infinity. H equals H_- on A0 by continuity. Since A0 is invariant, BH=0 and consequently g=0 on A0; Q=H there. Monotone integration gives

    H_-=a integral_(-infinity)^infinity g(y_s)ds<=0.

The whole-line integral is absolutely convergent because g<=0. This does not show H_-=0.

## 6. Zero or negative work and the rank alternatives

If DW(x0)!=0 and its range is contained in R X0, then that range equals R X0. Consequently B(y_t) belongs to range DOmega(y_t). The verified C47 argument gives g=H=Q=0 on the whole orbit. It can also be recovered from DOmega^T U=0, which gives g=0, and H tending to zero forward.

If DW(x0)=0, then DOmega=0 on the whole orbit. On each maximal open interval where U(y_t)!=0, equation (2) holds. Linear uniqueness makes g either identically zero or nowhere zero on that interval. In the second case g<0, and

    (log(-g))''=tau g<=0.

No conclusion is asserted across a time at which U vanishes.

At any x0 in D intersect supp W with V(x0)=W(x0)=0, either DW=0 and the sign theorem applies, or A1186 gives DW=X0 tensor l!=0 and S(x0)=0. Thus P2=S>=0 at every such common zero, and equals zero when DW!=0. In particular this holds at every supported T-flat point.

If instead W(x0)=0 and either k(x0)>0 or k(x0)=0,S(x0)<0, the sign theorem shows that range DW is not contained in R X0. The common-zero result forces V(x0)!=0. Nilpotence gives rank one or two. In rank two, a three-dimensional nilpotent matrix has a one-dimensional kernel contained in its range; since DW X0=0, X0 lies in the range, and C47 would give k=S=0, a contradiction. Therefore DW=w tensor m has rank one, with w not parallel to X0 and m(X0)=m(w)=0.

## 7. Consequences, comparisons and limits

The negative-sign analytic common-zero germs of A1079 have supported T-flat axis points and S<0 there. They therefore cannot be actual tails of profiles in this exact class. Positive-sign germs are not eliminated by this argument. The previously open pressure sign at supported common V/W zeros is partially resolved: negativity is excluded, while strict positivity with DW=0 remains unresolved.

At a supported infinite-order T0 point, the C^1 scattering argument already transfers size flatness of original vorticity along the carrier orbit. When U is only C^2 on the compact core, continuity gives Omega=DOmega=0 on the backward limit set; it does not supply all higher derivatives there. Under exterior smoothness and the stated all-order natural bounds, higher flatness holds at the exterior orbit points. The present signs and the tail expansion give H(y_t)=o(exp(-bt)) at T0, but allow g=H=0 everywhere. They give no contradiction at such a point.

The full C49 manuscript has been read, including all remarks. Its comparison with A470 is accurate: that earlier compact-invariant argument obtains boundedness from compactness, whereas here the natural decay bounds provide global boundedness of g and H. The rotation contribution cancels in (1), so the proof works for each arbitrary finite omega. The pressure gauge Pinf, support requirement, range condition, C^2 core and both natural bounds remain explicit.

## 8. Verification evidence

The complete seven-section C49 source is pinned with capture time and hash. Its setting was compared with the current C47 statement, and its new work-sign argument, all tail signs, backward limit assertion and rank alternatives were independently reconstructed above. No computation, numerical approximation, additional flow completeness assumption, or formal build was used. No bare-decay or arbitrary-helicity conclusion follows.
