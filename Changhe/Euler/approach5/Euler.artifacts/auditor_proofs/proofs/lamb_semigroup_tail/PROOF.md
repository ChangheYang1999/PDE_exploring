# A twisted homogeneous tail from an integrable Lamb vector

## Exact statement

Let J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, and

    Lf=(1-c)f+(Ay.grad)f+omega Jf.

Assume 0<c<1, any finite real omega, U in C^1(R^3;R^3), P in C^1(R^3),

    div U=0, LU+(U.grad)U+grad P=0,
    U is bounded and U(R .) tends to zero in distributions as R tends to infinity.

Put Omega=curl U, ell=Omega cross U, k=(1-c)/c, p_star=3/k. Suppose ell belongs to L^p(R^3) for some 1<p<p_star. This last condition is extra; it is not proved from velocity decay alone. Let Pi be the bounded Leray projection on L^p, and set delta=3c/p-(1-c)>0.

There is a uniquely determined decomposition

    U=V+W,
    W=integral_0^infinity S_s Pi ell ds in L^p,
    S_s f(y)=e^{(1-c)s} Q_s f(e^{sA}y), Q_s=exp(omega sJ),
    LW=-Pi ell, LV=0, div W=div V=0

in distributions on all of R^3. Moreover

    ||W||_p <= ||Pi||_{p->p} ||ell||_p/delta,
    V(e^{sA}y)=e^{-(1-c)s} Q_s^T V(y) for almost every y,
    V(y)=|y|^{-k} Q_{sigma(y)}^T F(pi(y)) almost everywhere,
    sigma(y)=c^{-1}log|y|, pi(y)=Q_{sigma(y)}y/|y|,
    F in L^p(S^2),
    ||S_s U-V||_p=e^{-delta s}||W||_p.

The assertion involving the norm means that the difference belongs to L^p. U and V need not individually belong to global L^p. For nonzero U and 2/5<c<1, F is nonzero.

For p=2, which is permitted exactly when c>2/5, put alpha=5-2/c>0. Then

    (5c-2)||W||_2^2=2 integral W.ell,
    ||W||_2 <= 2||Pi ell||_2/(5c-2),
    lim_{R->infinity} R^{-alpha} integral_{B_R}|U|^2
        =||F||_{L^2(S^2)}^2/alpha.

This confirms Theory Agent A Proposition T.8. No pressure normalization or decay condition on P is added.

## The group and the pressure term

Changing variables by e^{sA}, whose determinant is e^{3cs}, gives

    ||S_s f||_p=e^{-delta s}||f||_p.                        (1)

The operators form a strongly continuous group on L^p. Strong continuity first holds for compactly supported smooth fields and then for all L^p fields by density and (1). They also act continuously on distributions by

    <S_s f,phi>=<f,e^{(1-4c)s}Q_s^T phi(e^{-sA} .)>.

Direct differentiation proves

    div(S_s f)=e^s (div f)(e^{sA} .),
    div(Lf)=(1+Ay.grad)div f,
    L^T phi=(1-4c)phi-omega Jphi-(Ay.grad)phi.              (2)

All these equations extend distributionally. The transpose commutes with normalized spatial dilation phi_R(y)=R^{-3}phi(y/R).

The vector identity (U.grad)U=grad(|U|^2/2)+ell gives

    LU+ell+grad(P+|U|^2/2)=0.

Define h=LU+Pi ell. Because (I-Pi)ell is curl-free, h is curl-free. It is divergence-free by (2). Hence every component is harmonic in distributions. It is tempered, since U is bounded, Ay DU is a derivative of a linearly growing tempered field, and Pi ell is in L^p. Fourier transformation of Delta h=0 shows that its transform is supported at the origin; therefore h is a polynomial.

For every compactly supported smooth test vector phi,

    |<Pi ell,phi_R>| <= C_phi R^{-3/p}||Pi ell||_p ->0,
    <LU,phi_R>=<U,(L^T phi)_R> ->0

by the prescribed weak blow-down of U. A nonzero polynomial cannot have all these pairings tending to zero: divide by R^d for its highest homogeneous degree d and choose a test vector detecting that homogeneous component. Thus h=0, proving

    LU=-Pi ell.                                           (3)

This proves pressure elimination without assuming that P, grad P, or P+|U|^2/2 belongs to a global function space.

## Constructing the remainder and the angular profile

By (1), integral_0^infinity ||S_s Pi ell||_p ds is finite. The Bochner integral W is therefore defined and obeys the asserted bound. It is divergence-free by (2). Differentiation after pairing with a compact test vector, followed by integration in s, gives

    LW=integral_0^infinity d_s(S_s Pi ell)ds=-Pi ell.

The boundary at infinity vanishes in L^p by (1), and the boundary at zero is Pi ell. Thus V=U-W satisfies LV=0 and div V=0 on all R^3. Distributional differentiation of S_s V now gives d_s(S_s V)=S_s LV=0, so S_s V=V for every real s.

Since V belongs to L^p on compact sets, its logarithmic polar representative

    G(t,w)=e^{(1-c)t}Q_t V(e^{tA}w)

is locally L^p on R times S^2. Its translation invariance in t, interpreted distributionally or by mollification in t, implies G(t,w)=F(w) almost everywhere. This supplies a simultaneous measurable representative and avoids an unjustified uncountable intersection of exceptional sets. The change of variables on the unit annulus gives

    integral_{1<|y|<2}|V|^p
        =[integral_1^2 r^{2-pk}dr] integral_{S^2}|F|^p.

It follows that F is in L^p(S^2). The same computation at zero is consistent because pk<3. The exact convergence assertion follows from S_s U-V=S_s W and (1).

Uniqueness in the stated class is immediate. If V1+W1=V2+W2 and both V_i are invariant under S_s while both W_i are in L^p, their difference f is in L^p and satisfies ||f||_p=e^{-delta s}||f||_p for every s. Therefore f=0.

If F=0, then U=W belongs to L^p with p<p_star. For 2/5<c<1 the already checked energy Liouville corollary A052/A229 applies under exactly the present C^1 and weak blow-down hypotheses and gives U=0. This is the only energy-Liouville input in the angular nonvanishing assertion.

## The L2 identity without a spectral-theory shortcut

For p=2, delta=(5c-2)/2. The integral formula itself places W in the generator domain:

    S_h W=integral_h^infinity S_s Pi ell ds,
    (S_h W-W)/h -> -Pi ell in L^2 as h ->0.

This identity holds for positive and negative h, with the usual signed integral over [0,h]. Differentiate

    ||S_h W||_2^2=e^{(2-5c)h}||W||_2^2

at zero. The left derivative is -2<Pi ell,W>. Thus

    (5c-2)||W||_2^2=2<Pi ell,W>=2<ell,W>.

The last equality uses the self-adjointness of Pi on L^2 and div W=0. The integral is absolutely convergent by Cauchy-Schwarz. The norm bound follows immediately.

The angular formula gives integral_{B_R}|V|^2=||F||_2^2 R^alpha/alpha. Also

    |integral_{B_R}V.W| <= ||F||_2 R^{alpha/2}||W||_2/sqrt(alpha).

Expand |U|^2=|V|^2+2V.W+|W|^2 and divide by R^alpha. This proves the energy limit directly. It agrees with the already proved energy theorem. No surface integration and no unproved pressure boundary estimate is needed here.

## Explicit sufficient conditions and agreement with the Dini tail

If, for every R>=1,

    ||Omega||_{L^p({R<|y|<2R})} <= C R^{3/p-1/c},
    max(1,3c)<p<p_star,

then boundedness of U gives integral_{A_R}|ell|^p<=C R^{3-p/c}. This dyadic series is summable since p>3c, and ell is bounded on the unit ball. Thus ell is in L^p. For p=2 the resulting range is 2/5<c<2/3.

Under the additional C^2 and Dini assumptions of A210, with 1/3<c<1, the uniform natural vorticity bound implies this condition for every 3c<p<p_star. In addition, the natural velocity bound gives

    integral_{A_R}|ell|^2 <= C R^{1-4k},

so ell belongs to L^2 whenever 2/5<c<4/5. Let V_tilde be the continuous scattering tail of A210. Both V and V_tilde have the same exact twisted homogeneity. On annuli,

    ||V-V_tilde||_{L^p(A_R)}
      =R^{3/p-k}||V-V_tilde||_{L^p(A_1)}.

But V-V_tilde=(U-V_tilde)-W. The first term on the right has annular norm o(R^{3/p-k}) by the uniform scattering expansion; the second has norm tending to zero by W in L^p. Since 3/p-k>0, divide by this power and let R tend to infinity. This proves V=V_tilde almost everywhere. The argument applies either for the general p range or for the enlarged L^2 range.

Finally, in the enlarged L^2 range, the cutoff div-curl estimate gives ||DU||_{L^2(A_R)}<=C R^{1/2-k}. Multiplying by the natural bound for U shows both (U.grad)U and grad(|U|^2/2) belong to L^2. The latter gradient is L^2-orthogonal to divergence-free W, so integral W.ell=integral W.(U.grad)U. This extends that finite-energy identity up to c<4/5. It does not extend absolute convergence of integral U_i U_j partial_j V_i, or the vanishing unweighted renormalized energy, beyond the separately justified c<3/5 range.

## Audit conclusion

The projection, harmonic-polynomial removal, group signs, generator-domain assertion, almost-everywhere angular representation, sufficient exponents and all-omega scope are verified. The theorem is conditional on Lamb-vector integrability. In the campaign's interval this hypothesis has not been obtained from smooth velocity decay alone. The decomposition does not prove that the nonlinear fixed-point problem has or lacks a smooth global solution.
