# Targeted Liouville proof and dependency corrections

Status: the four Note A79 findings and Note A80 notation point are CONFIRMED A2672-A2676 after independent comparison. The exact report checked is SHA256 7e9d6811504f4529a7fcb812d7746202ba8a3f0e89b2be4ef28782206a338750. This is not a new full review of Sections 2B or 2D or their external references.

## 1. Correct inputs to the covector identity

Let B(y)=(cI-omega J)y+U(y), with 0<c<1/2, J skew-symmetric, bounded C2 velocity U, M=sup|U|, and div U=0. Assume a C1 pressure P solves (1-c)U+(B.grad)U+omega J U+grad P=0. Put Phi_t for the complete flow of B, Psi_t=Phi_-t, Omega=curl U, kappa=1+c, a=1-2c, and F=B cross Omega. The already established Cauchy identity and determinant identity give, for L=D Psi_t(x),

    B(Psi_t x)=L B(x),
    Omega(Psi_t x)=exp(kappa t)L Omega(x),
    det L=exp(-3ct).

The first two are Lemma 2(d); the third is Lemma 1(c). Applying (Lv) cross (Lw)=det(L)L^(-T)(v cross w),

    F(Psi_t x)=exp((kappa-3c)t)L^(-T)F(x),
    L^T F(Psi_t x)=exp(at)F(x).

Thus the proof of Lemma 2(e) uses its own part (d) and Lemma 1(c). The printed reference to parts (d) and (c) of Lemma 1 is inaccurate, since Lemma 1(d) is a radial bound. The formula itself is correct for every finite omega.

## 2. The missing reverse inclusion of unstable sets

Let Q be the closed ball of radius R1>=2M/c+1 and K=intersection_(t>=0)Psi_t(Q). Let f be the compactly supported cutoff model in Lemma 11, so f=Psi_1 and f^-1=Phi_1 on K. The printed proof establishes W^u_f(x) contained in K and then the inclusion in the unstable set of Psi_1. Here is the reverse inclusion.

Suppose y belongs to the unstable set of Psi_1 at x in K. Then Phi_n y approaches Phi_n x as n tends to positive infinity, at the required exponential rate. The latter sequence lies in the compact K. Thus sup_(n>=0)|Phi_n y|<infinity. The variation-of-constants upper bound

    |Phi_t z|<=exp(ct)(|z|+M/c), 0<=t<=1,

implies that the full positive-time orbit of y is bounded. For any fixed s>=0, the lower bound gives

    |Phi_(t+s)y|>=exp(ct)(|Phi_s y|-M/c)+M/c, t>=0.

If |Phi_s y|>M/c its right side tends to infinity, a contradiction. Hence |Phi_s y|<=M/c for every s>=0. In particular Phi_s y lies in Q, so y belongs to Psi_s(Q) for every s, and y is in K. On K all backward iterates of f and Psi_1 coincide, and their metrics are equivalent on this compact set. Their exponential asymptotic condition is the same. This proves the reverse inclusion and equality.

At Oseledets regular x the existing manifold theorem identifies these sets with the stated unstable manifolds. At nonregular points this argument identifies only the exponential asymptotic sets; it does not create a smooth manifold. Only W^u_f is used downstream in the displayed proof, so inserting this argument repairs an omitted justification without changing those conclusions.

## 3. The stronger same-orbit interval conclusion

Use the stated classes of Corollary L.4: smooth profiles with the established basin family, the stated growth-conditioned class with its family, or a C2 profile with a separately given family satisfying all of (CI). The already confirmed localization argument says that h=U.Omega vanishing on every essential domain D_nu forces U=0. Thus a nonzero profile in these classes has some D_nu on which h is nonzero.

On this open invariant domain the complete vortex flow Gamma has almost-everywhere recurrence and d/dt H(Gamma_t x)=-a h(Gamma_t x). Choose a recurrent point in a nonempty strict-sign open subset. Negate (H,h) if necessary to arrange h(x)>0. For some delta>0 the function g(t)=H(Gamma_t x) decreases strictly on [0,delta]. Choose g(delta)<ell<u<g(0). Recurrence provides an integer N>delta with g(N)>u. Let t_u be the first time in [delta,N] with g(t_u)=u and t_ell the last time in [delta,t_u] with g(t_ell)=ell. Then ell<g(t)<u between them. The mean value theorem gives t* in that interval with g'(t*)>0, and thus h(Gamma_(t*)x)<0.

There is a unique s* in (0,delta) with g(s*)=g(t*); there g'<0 and h>0. The inverse function theorem at these two times supplies a common nonempty open interval of H values, each attained on the same orbit with the two strict helicity signs. The chosen base point is recurrent and remains in D_nu by invariance.

This stronger interval conclusion is correct, but is obtained from Lemma 18 and the proof. The literal contrapositive of the levelwise statement alone only asserts the existence of a domain and a level having both signs. Replace the introductory word "Equivalently" by "The proof gives more" or equivalent proof-based wording. This is a logical exposition correction, not a refutation of the stronger conclusion.

## 4. Exact dependency-list repairs

Lemma 13(vi) concerns the whole family F. Its proof is

    O minus union D_nu is contained in O minus union Bas(nu),

and the latter is null by (CI-5). Therefore the plan saying all of Lemmas 9-14 concern only one measure with (CI-1)-(CI-4) needs an explicit exception for Lemma 13(vi). The other local arguments are not promoted into a family coverage theorem.

The dependency diagram for Corollary L.4 needs Lemma 4, which supplies recurrence for the invocation of Lemma 18. The printed proof of L.4 already names Lemma 4; the diagram alone omits it. Neither correction supplies missing general C2 coverage.

## 5. The local Z convention and review scope

Note A80 identifies a genuine cross-section notation collision. Section 2B explicitly defines Z={Omega!=0}; the front notation and Sections 2C and 2D use O for that set, while 2C and 2D define Z={Omega=0}. The displayed local definitions have been checked. Either a mechanical rename within 2B or a clear local-convention sentence resolves the issue. An explicit notice is enough to avoid mistaking the two sets; it changes no theorem.

Notes A79 and A80 are from the existing agent configured as model; actual provider runtime is independently unattested. This independent check covers the four A79 findings and A80's notation point against the pinned report passages. It does not newly certify A80's entire D4-D6 review or its literature claims. No mathematical computation, new client, formal build or external source retrieval was needed.
