# Nested logarithmic estimates with a retained initial constant

Status: independent reconstruction of LIT110. The full submitted proof, actual source theorem, all Section5 and AppendixA have been read. A717 and A719 confirm the scalar result and differentiated transport formula below. A718 refutes the specified printed formulas, and A720 leaves independent certification of the entire external theorem open. Focused configured-model comparison remains pending. The external BMO localization theorem is not certified here.

## 1. Exact scalar theorem

Fix finite t0<T. Let a be nonnegative and Lebesgue integrable on(t0,T), let C0>0 and D>=1, and let Z_m:[t0,T) to[0,infinity), m=0,1,..., be measurable. Assume that for every T'<T there is H(T')<infinity with Z_m(s)<=H(T') for all m and almost every s<=T'. Also assume, for every m and almost every t,

    Z_m(t)<=C0 D^m+integral_(t0)^t a(s)Z_m(s)log(e+Z_(m+1)(s))ds.   (1)

Set A(t)=integral_(t0)^t a(s)ds and c0=log(C0+e). Then, almost everywhere,

    log(e+Z_0(t))<=[c0+(log D)A(t)]exp(A(t)).                       (2)

The same conclusion holds at any additional time where(1) for m=0 holds. Thus the result is an essential uniform bound in the almost-everywhere formulation and an everywhere uniform bound if(1) is everywhere valid for m=0. It does not promote arbitrary point values of measurable functions to continuous ones. The bound depends on C0,D and ||a||_1; the preterminal H(T') is needed only to justify the iteration, and is absent from the final bound.

## 2. Complete proof of the scalar theorem

Define

    X_m(t)=C0 D^m+e+integral_(t0)^t a(s)Z_m(s)log(e+Z_(m+1)(s))ds.

The local bound makes this integral finite before T. Each X_m is locally absolutely continuous, X_m>=e, and e+Z_m<=X_m almost everywhere. Since there are countably many indices, these inequalities and their derivative statements hold simultaneously outside one null set. Set beta_m=log X_m. Monotonicity of the logarithm gives

    beta_m'=a Z_m log(e+Z_(m+1))/X_m<=a beta_(m+1)

almost everywhere. Since C0D^m+e<=(C0+e)D^m,

    beta_m(t)<=c0+m log D+integral_(t0)^t a(s)beta_(m+1)(s)ds.      (3)

This holds at every t<T by absolute continuity.

Fix t<T and choose t<T'<T. For every s in[t0,t] and every m, the integral definition and the local essential bound imply

    X_m(s)<=D^m[C0+e+A(T')H(T')log(e+H(T'))].

Therefore for one finite c_t independent of m,

    0<=beta_m(s)<=c_t+m log D, t0<=s<=t.                          (4)

Iterate(3) N+1 times from m=0. Nonnegativity permits Fubini and gives

    beta_0(t)<=sum_(k=0)^N (c0+k log D)A(t)^k/k!+R_N(t),
    0<=R_N(t)<=[c_t+(N+1)log D]A(t)^(N+1)/(N+1)!.

The simplex integral is A(t)^k/k!: the product of the k copies of a is symmetric, the diagonals have measure zero, and the k! ordered simplices partition the cube. Integrability supplies absolute convergence as well. The remainder tends to zero by factorial domination. Summing the two exponential series gives

    beta_0(t)<=[c0+(log D)A(t)]exp(A(t)).

Combine e+Z_0<=X_0 with this everywhere estimate for beta_0. Where(1) fails the value of Z_0 is uncontrolled; where it holds the same comparison applies. Finally A(t)<=||a||_1. This proves every stated conclusion without assuming that the local envelope H remains bounded up to T.

## 3. Differentiation of the transformed vorticity equation

For t<0 let

    h(t)=(-t)^(-1/2)/(2(1+(-t)^(1/2))), b(t)=1/(1+(-t)^(1/2)),
    W(y,t)=h(t)y+b(t)V(y,t), Omega=curl V.

Assume first smooth fields satisfying

    partial_t Omega+h Omega+(W.grad)Omega=b(Omega.grad)V.        (5)

With Q_i=partial_i Omega, differentiate(5). The derivative of W is h e_i+b partial_i V. Therefore the exact identity is

    partial_t Q_i+2h Q_i+(W.grad)Q_i
       =b[(Q_i.grad)V+(Omega.grad)partial_i V
                         -((partial_i V).grad)Omega].            (6)

The added h Q_i and the last commutator both come from differentiating the transport coefficient. They cannot be omitted in an equality. Under the source's W2,q spatial regularity, q>3, the identity can instead be interpreted in distributions by the local Sobolev product rule, or obtained by spatial mollification on a smaller ball; it does not assert pointwise third derivatives of V. On compact preterminal cylinders W is locally Lipschitz, Q belongs to Lq and the right side is locally Lq, so the usual transport energy argument is justified by that same mollification and commutator limit.

For the immediate formal q-energy identity, multiply by Q_i |Q|^(q-2), sum i and integrate with a nonnegative cutoff. The extra last term has absolute value at most C b |grad V||Q|^q, using the Frobenius norm and Cauchy-Schwarz. The added h Q_i contributes an additional favorable qh|Q|^q damping since h>=0. Incompressibility of V gives div W=3h, so the total uncut damping coefficient becomes(2q-3)h, positive for q>3. The extra term therefore alters the dimensional energy constant and improves the damping. This verifies this specific correction, not all remaining cutoff and BMO estimates.

## 4. The actual source and its printed scalar steps

The source is D.Chae and J.Wolf, Localized non blow-up criterion of the Beale-Kato-Majda type for the 3D Euler equations, arXiv1711.06415v2, dated10 October2020,26 pages. Its Theorem1.1 assumes (v,p) in C1 on B(rho) times(-rho,0), with v in C([-rho,0);W2,q(B(rho))) and uniformly bounded local L2 velocity, q>3. The additional hypothesis is time integrability of the local mean-oscillation seminorm of curl v. It asserts a uniform W2,q bound on every strictly smaller ball. Remark1.2 permits the stronger time-integrable local L-infinity vorticity assumption. No statement here replaces that local energy or preterminal regularity premise by profile decay.

Printed pages20-21 contain these specific errors in the closing scalar calculation:

1. A fixed initial or cutoff constant cannot be absorbed into D^m at m=0. After Y_m=Z_m+e, displayed(5.17) at t0,m=0 asserts e+Y_0(t0)<=1, although its left side is at least2e. A retained C0 D^m repairs this issue.
2. Differentiating displayed(5.18) gives aY_m log(e+Y_(m+1)). The first equality in(5.19) prints aY_m[log Y_(m+1)+1], a different expression. The inequality X_m'<=aX_m log X_(m+1) follows directly from the correct expression once X bounds e+Y; it does not need that false equality.
3. The printed beta_m=log X_(m+1) is shifted by one index relative to the written initial value m log D and to the comparison with Y_0. Defining beta_m=log X_m and retaining c0 gives the consistent chain above. As written, the right side of(5.20) vanishes at t0 while the left side is positive.
4. AppendixA's remainder estimate uses sup K(s) on a compact time interval, although its hypothesis gives only pointwise finiteness of K(s). Pointwise finiteness alone does not justify that step. The scalar theorem in Sections1-2 proves the needed application under an explicit local uniform bound, supplied there by preterminal W2,q regularity and cutoffs bounded by1. This is a repair of the application and does not assert a counterexample to the appendix lemma's conclusion.

Printed page17 equation(5.6) omits the two terms displayed explicitly in(6). The exact differentiation above repairs that step. The source's velocity transformation and definitions have been retained; this is not a change of similarity convention.

## 5. Scope, evidence and dependencies

If the preceding source localization estimates produce(1), with a in L1, geometric cutoff constants and the locally uniform Z_m bound, Section2 gives the needed inner-ball second-derivative bound. Those localization estimates have not all been independently checked here. Thus this audit proves a scalar lemma and an exact transport identity, and identifies repairable printed steps. It does not certify or refute the whole external theorem. Nor does it establish a new Liouville theorem or an unconditional shortcut for the rotating Euler conjecture.

The full submitted proof, actual PDF, its text extraction and relevant rendered pages are pinned in verification. No numerical computation is necessary or used. Existing configured-model review is requested through files only, with actual-model evidence limited to the existing configuration; no new client or external communication is used.
