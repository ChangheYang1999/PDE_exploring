# Bernoulli normalization in the formal Lyapunov classification

## 1. Exact statements and verdicts

Let 0<c<1/2, let omega be real, let J(y1,y2,y3)=(-y2,y1,0), and put A=cI-omega J and a=1-2c>0. On a connected open spatial set G, use formal values u in R3, M in sl(3), and p in R. Set b=Ay+u. The report's Section 0.2 defines the unshifted quantity

    H=p+|u|^2/2+(Ay).u.

Define instead

    K_omega=H-ca|y|^2/2,
    H0=K_0=p+|cy+u|^2/2+c(c-1)|y|^2/2.

Let Psi in C1(G x R3 x sl(3) x R). Suppose its formal carrier derivative is nonpositive at every admissible formal second jet, as defined below. Then Psi is constant for omega!=0. For omega=0 it is exactly f(H0), with f in C1(R) and f'>=0. This classification is CONFIRMED. It does not classify functions tested only on globally decaying solutions.

The literal use of unshifted H in Theorem 3(g) and Appendix A of the pinned report is REFUTED. Replace H by H0 there, consistently with the already correct definition in Theorem 2. Also specify nonpositive formal derivative, rather than the directionally ambiguous word monotone. The reversed inequality gives f'<=0 at omega=0.

## 2. Direct countertest for the literal H statement

Take omega=0, a nonzero constant vector u, U(y)=u and P(y)=-(1-c)u.y on all R3. These solve the profile equation, since DU=0 and (1-c)u+grad P=0. They are smooth and uniformly sublinear, though not decaying. Their jets are admissible at every point. Here

    H=|u|^2/2-a u.y,
    B.grad H=-a u.(cy+u).

At y=-2u/c, B=-u!=0 and B.grad H=a|u|^2>0. At y=0 this derivative equals -a|u|^2<0. Thus even the identity function of unshifted H has neither universal monotonicity direction. This is a countertest for the formal classification, not a counterexample to the decaying-profile conjecture.

For the corrected quantity,

    B.grad H0=-a|cy+u|^2<=0.

Moreover H0 cannot be a function of H on the full formal space: with u fixed, varying y perpendicular to u leaves H fixed but changes the quadratic term in H0. The two classifications are different, not alternative names for the same functions.

## 3. Formal second jets and elimination of strain

An admissible formal second jet consists of g in R3, T_ijk=T_ikj with sum_i T_iik=0, and symmetric Pi, satisfying

    (1-c)u+Mb+omega Ju+g=0,
    (Tb)_ij=sum_k T_ijk b_k=-M-M^2-omega[J,M]-Pi.

The formal derivative is

    Psi_y.b+Psi_u.Mb+Psi_p(g.b)+Psi_M:(Tb).

When b!=0, T -> Tb maps the indicated tensor space onto sl(3). After an orthogonal change of coordinates, write b=t e1. For N in sl(3), set T_i11=N_i1/t and T_i1j=T_ij1=N_ij/t for j=2,3; additionally set T_222=-N_12/t, T_333=-N_13/t, with other independent entries zero. These assignments give Tb=N and all three divergence constraints. Therefore the trace-free symmetric part of Pi is arbitrary; its trace is fixed as -tr(M^2).

Varying that part in both signs forces Psi to have zero derivative in every symmetric trace-free M direction. Continuity extends the conclusion through b=0. Write M=S+K(w), with S symmetric trace-free and K(w)v=(w x v)/2, and write Psi=psi(y,u,w,p). The axial part of the differentiated equation gives

    b.grad w=-w-omega Jw+Sw.

With a0=psi_u-psi_p b and k=psi_w, the coefficient of freely variable S in the formal derivative is

    C=sym(b tensor a0)+sym(w tensor k).

Consequently C=mu I. Each symmetric rank-two form sym(v tensor z) has at most one positive and at most one negative eigenvalue. Their sum has at most two of each, so mu=0 in dimension three.

## 4. Elimination of vorticity dependence

For independent b,w, the identity C=0 means

    (b.v)(a0.v)+(w.v)(k.v)=0 for every v.

The independent linear polynomials b.v and w.v are coprime. Hence k=beta b and a0=-beta w. Continuity extends k parallel to b to every w when b!=0. Thus

    psi(y,u,w,p)=Phi(y,u,p,sigma),   sigma=b.w.

Differentiation and the relation a0=-beta w give

    Phi_u-Phi_p b=-2 Phi_sigma w.

The left side is fixed when sigma is fixed. Varying w in its two-dimensional plane forces Phi_sigma=0. Thus Psi is independent of w and therefore of M on b!=0, and by continuity everywhere. Every first jet with b!=0 extends to a second jet by Section 3. At b=0 a zeroth-order carrier derivative is zero. We may therefore apply the zeroth-order argument directly.

## 5. Zeroth-order classification and the correct normalization

Varying trace-free M in the remaining formal derivative forces Psi_u=Psi_p b. Integration along the level sets of p+|b|^2/2 gives Psi=f(y,K_omega), with f C1. Put X=cy+u. Direct substitution of the pointwise equation gives

    d_B K_omega=-a X.(X-omega Jy).

As p is free, K_omega can be fixed independently of X. Nonpositivity for every X therefore becomes

    f_y.(X-omega Jy)-a f_h X.(X-omega Jy)<=0.

The quadratic coefficient forces f_h>=0. If f_h=0, varying X gives f_y=0. If f_h>0, maximizing over X gives |f_y-a omega f_h Jy|^2/(4a f_h)<=0. Hence in both cases

    f_y=a omega f_h Jy.

For omega=0 this gives f_y=0, and connectedness of G yields f=f(h). Conversely f(H0) has derivative -a f'(H0)|b|^2, so every f'>=0 works.

For omega!=0, set q=a omega. The C1 function f is constant along the flows of

    Y1=partial_y1+q y2 partial_h,
    Y2=partial_y2-q y1 partial_h,
    Y3=partial_y3.

A sufficiently small rectangular composition of the first two flows translates h by a nonzero multiple of its signed area while fixing y. Thus f_h=0 without requiring second derivatives of f; then f_y=0. Connectedness gives a constant function.

## 6. Scope and effect on the assembly

The current source Section 5.1 and the old independent first-order proof use the symbol H for the corrected H0 at omega=0. The report reuses H for a different quantity. This notation collision affects Theorem 3(g) and the two omega=0 occurrences in the formal-method row of Appendix A. The report's Theorem 2 already specifies H0 correctly. The full Section 2B independently defines its own corrected Bernoulli quantity and was audited at that definition; its identities are not changed by this finding.

Higher-order classifications cited in the same appendix row are not newly reconstructed here. Their omega=0 references must use the same corrected H0; their earlier nonstagnating-jet scope restrictions remain necessary. No local formal result proves that arbitrary global constraints on a decaying solution cannot produce a Lyapunov function. No pressure-at-infinity or complete-flow premise is used in this algebraic audit. The unrestricted rotating nonexistence conjecture remains OPEN.

All quoted report passages, the source classification, the old independent proof and this complete argument were read. No numerical computation, formal build or new model client was used.
