# Pressure flatness and two-sided escape on regular nodal sheets

Status: CONFIRMED A878-A881 under the exact global hypotheses below. Compactness of the parallel equilibrium curve and exclusion of either nodal branch remain OPEN, A882.

## 1. Statement and dependencies

Fix 2/5<c<1/2 and omega in R. Put Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, kappa=1+c, p=(1-c)/c, lambda=2(1-c) and q=lambda/a>2. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

for a finite constant C. These are additional global helicity and natural-rate hypotheses. They have not been deduced from bare velocity decay. Normalize P by its actual limit Pinf and write

    B=Ax+U, Omega=curl U,
    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2, g=U.B=H-Q.

The equation makes P, H and Q C2. Let Phi and Gamma be the complete B and Omega flows. B has linear growth, and Omega is bounded and C1, so these completeness assertions do not require an extra assumption.

Use the already confirmed scattering and nodal constructions A810-A818: K is the compact forward-bounded B core, E its complement, Xi:E to R3 minus {0} its actual C1 scattering diffeomorphism, and K_Omega consists of complete Gamma lines contained in K. On O=R3 minus K_Omega there is a C1 function L with

    L(Phi_t y)=exp(-at)L(y), L(Gamma_s y)=L(y).

It extends k composed with Xi, where k(z)=(Az).V(z) for the actual leading velocity V. Let M be any nonempty connected component of

    {y in O:L(y)=0, dL(y)!=0, Omega(y)!=0}.

Then, locally around every point of M,

    Q=phi(H), phi in C2, |phi(h)|<=C_local |h|^q.

In particular D2Q=0 on the entire ambient closure Cbar of M. Throughout Cbar,

    2|sym DU|^2=U.curl Omega,
    grad H!=0, U!=0.

No point of Cbar satisfies both Omega=0 and D Omega=0. In the parallel case B=tau Omega on M, every vortex line through its carrier-equilibrium curve P0={B=0} intersect M escapes K in both parameter signs. The two associated regular vortical angular components are distinct and each is homeomorphic to P0.

The dependencies used below are proved in the team records, in the team records and in the team records. The last supplies the bounded-half endpoint theorem including its separately checked rho=-a boundary case. A478 supplies origin separation for actual globally helicity-free profiles. No recurrence assertion on the null surface M is used.

## 2. Finite paths compare scalar germs

We first prove a general C1 lemma. Suppose N is invariant under a complete C1 flow Phi, dL is nowhere zero on N, L Phi_t=exp(-at)L, and F in C1(N) satisfies dF wedge dL=0. Choose a C1 curve psi:(-delta,delta) to N such that L(psi(r))=r, and put f(r)=F(psi(r)).

For fixed r and t>=0, set s=exp(-at)r. The finite path

    gamma(tau)=Phi_tau psi(exp(a tau)s), 0<=tau<=t

stays in N because exp(a tau)s is between s and r. Its L value is s, hence dL(gamma')=0. Linear dependence of dF and the nonzero covector dL gives dF(gamma')=0. Its endpoints are psi(s) and Phi_t psi(r). Thus

    F(Phi_t psi(r))=f(exp(-at)r).                       (1)

No uniform spatial flowbox at infinity and no division by B are involved. In particular the argument allows psi(0) to be a carrier equilibrium.

For the application take N={y in O:dL(y)!=0, Omega(y)!=0}. It is open and Phi-invariant: the exact covector law for L and the Cauchy vorticity law preserve their nonvanishing. The ambient recurrence rank lemma in A810-A814 gives

    dH wedge dL=0, dQ wedge dL=0 on N.

Its recurrence is on open three-dimensional flowboxes. The same confirmed proof gives, on M,

    H=Q=g=0, dH=dL!=0, dQ=0, dg=dH,
    U=b grad H

with one spatial constant b!=0. M is an invariant connected C2 surface and meets E.

Choose y0 in M intersect E and a transversal psi to L whose small image lies in E intersect N, with psi(0)=y0. Set h0=H psi and q0=Q psi. Applying (1) to each scalar gives

    H(Phi_t psi(r))=h0(exp(-at)r),
    Q(Phi_t psi(r))=q0(exp(-at)r),                    (2)
    h0(0)=0, h0'(0)=1.

The last derivative is the ambient normalization dH=dL, not merely a tangential identity.

## 3. Actual decay gives a C2-flat pressure deficit

For every fixed y in E the confirmed actual scalar tail satisfies

    exp(lambda t)Q(Phi_t y) -> S(Xi(y)).

Only boundedness of this expression is needed. Equivalently, the actual bound Q(x)=O(|x|^(-2p)) and escaping-orbit growth |Phi_t y| comparable to exp(ct) suffice, since 2pc=lambda.

Fix one positive and one negative nonzero r in the transversal interval. Every sufficiently small s of the corresponding sign equals exp(-at)r for a unique t>=0. Equation (2) gives

    |q0(s)|<=C_r exp(-lambda t)
            =C_r |s/r|^q.

Thus q0(s)=O(|s|^q) from both sides. H is a C2 submersion near y0. On a smaller neighborhood its differential is nonzero and dQ wedge dH=0. Connected local fibers of H therefore carry a single value of Q, and a C2 transversal gives Q=phi(H) with phi C2. Since h0(s)=s+o(s) and h0 has a local C1 inverse, the preceding estimate yields |phi(h)|<=C_local |h|^q.

Every point of M has the same kind of local C2 representation. If two such neighborhoods overlap at a point of M, H takes a whole interval around zero in their overlap, so their scalar germs agree there. A connected manifold is path connected. A finite covering of a path in M transfers the germ from y0 to any prescribed point. This finite continuation is distinct from the infinite-time step, which was supplied by the explicit path (1).

Because q>2, the C2 Taylor formula gives phi(0)=phi'(0)=phi''(0)=0. The chain rule therefore gives D2Q=0 on M. Q is globally C2, so D2Q=0 on Cbar as well. No q-th derivative or differentiated asymptotic limit is asserted.

## 4. Closure nondegeneracy and the Poisson obstruction

Continuity extends U=b grad H, H=g=0 and dg=dH to Cbar. This closed set is Phi-invariant. Differentiate the global identity BH=-ag along its complete trajectories. The ambient relation dg=dH then gives

    Phi_t^*dH=exp(-at)dH on Cbar.

If dH vanished at a point y in Cbar, U would vanish along its entire B orbit. That orbit would be exp(tA)y and would tend to zero as t tends to negative infinity. Hence 0 would belong to Cbar and U(0)=0. The confirmed origin-separation theorem A478 gives an irrotational neighborhood of this origin under the present actual global hypotheses. This contradicts 0 being in the closure of the everywhere-vortical M. Therefore grad H and U are nonzero throughout Cbar. The proof does not assume that a whole B orbit in Cbar is bounded.

Taking the divergence of the momentum equation gives -Delta P=tr((DU)^2). The terms involving A and omega J cancel, and div U=0 removes the c term. Since Delta U=-curl Omega,

    Delta Q
      =-tr((DU)^2)-|DU|^2+U.curl Omega
      =-2|sym DU|^2+U.curl Omega.

This is a pointwise C2 identity. Section 3 makes its left side zero on Cbar.

At a point with Omega=D Omega=0, the identity forces sym DU=0, while Omega=0 forces the skew part to vanish. Thus DU=0. The Lamb identity then gives grad H=-aU, and direct differentiation of g=U.B gives grad g=A^T U. Since dg=dH on Cbar,

    A^T U=-aU.

Its scalar product with U gives (c+a)|U|^2=(1-c)|U|^2=0, contradicting U!=0. This excludes first-order-flat vorticity points on this closure only. It does not exclude all irrotational points there.

## 5. Both signs escape in the parallel case

If b=-1/a, then B=tau Omega on M and Omega.tau=kappa. Completeness implies that each vortex line crosses tau=0 exactly once. The curve P0={tau=0} is a connected C1 embedded one-dimensional manifold, and

    j:P0 times R -> M, j(q,zeta)=Gamma_zeta q

is a C1 diffeomorphism with inverse

    y -> (Gamma_(-tau(y)/kappa)y, tau(y)/kappa).

In these coordinates Omega=partial_zeta and B=kappa zeta partial_zeta. Thus

    Phi_t Gamma_zeta q=Gamma_(exp(kappa t)zeta)q.

Each nonzero-sign vortex half is one complete carrier orbit. It is either wholly in E or wholly in compact K. Suppose a half were in K. At its carrier equilibrium q, B=0, dg=dH=-aU and U!=0 give DB(q)^T U(q)=-aU(q). The covector rate is therefore rho=-a.

The complete bounded-half theorem A658-A659 applies. It requires no isolated or finite-equilibrium premise and gives convergence of this half to one carrier equilibrium qstar with Omega(qstar)=D Omega(qstar)=0. Its boundary proof checks both possible nonflat eigenvalue families at rho=-a; the remaining center-to-kappa first jet is killed by Omega=constant exp(-kappa t)B on the convergent trajectory. The point qstar belongs to Cbar, contradicting Section 4.

Consequently P_plus=P_minus=P0 in the notation of A866. For each sign, projection of Xi(Gamma_(sign 1)P0) along exp(tA) onto the unit sphere is an injective C1 local diffeomorphism onto a whole regular vortical angular component, as proved in A867. Connectedness of P0 gives one component for each sign. Their images are distinct: equal angular projections would identify a carrier orbit, whose nonzero zeta sign is preserved. Each component is homeomorphic to P0.

## 6. Scope and verification

LIT186's complete eight-section source was read. The finite-path argument, regularity of the scalar factorization, two-sided estimate, ambient closure calculation and pressure signs were independently reconstructed above. The relevant normalized-surface, parallel-product and rho=-a endpoint proofs were compared again. Exact source pins and hashes accompany this proof. No computation or formalization was needed.

This resolves the scalar-germ gap in coordinator Note70 and removes the nonescaping-sign alternative in A869 for these regular parallel sheets. P0 can still be a bounded noncompact embedded curve. A missing accumulation point in the joint core could be irrotational with a nonzero first vorticity derivative. The argument proves neither its impossibility nor compactness of P0. Neither the parallel nor nonparallel nodal branch, critical nodes, open zero regions or the general decay-only conjecture is excluded.

Comparison continues through the existing configured model working files; the provider runtime is not independently attested. No new client or agent is used.
