# A Holder inverse for an extension of the actual source operator

## Statement and scope

Fix 0<alpha<1. Use the exact joined and scalar-normalized modal source P=(p,0), the actual field V=ell X+U[rho0], and its source rates A,mu and g=rho0_y(P) from proof 15. In source coordinates X=(s,y), proof 209 constructs smooth global diffeomorphisms Phi_delta, equal to an exact transport-linearizing map near0 and to the identity outside B_delta. Put

 V_delta(X)=[DPhi_delta(X)]^(-1)diag(A,mu)Phi_delta(X),
 chi_delta(X)=chi(X/delta),
 X_alpha=C^alpha_b(R2) intersect L2(R2),
 ||h||X=||h||2+||h||infinity+[h]_alpha.

The fixed cutoff chi is smooth, equal1 on B_(1/2), and supported in B1. Define

 L_delta h=V_delta.grad h-h-gM h
    +chi_delta{rho0_x(P+X)U1[h]+(rho0_y(P+X)-g)U2[h]}, (1)

where M has multiplier xi^2/(xi^2+eta^2), U1 has multiplier xi eta/(xi^2+eta^2), and U2=-M. Its domain is

 D_delta={h in X_alpha:V_delta.grad h belongs to X_alpha distributionally}.

For every sufficiently small delta>0, L_delta:D_delta->X_alpha is a closed bijection. Its inverse is bounded X_alpha->X_alpha, with norms uniformly bounded as delta tends to0. All constants here are qualitative, depending on alpha, the certified source parameters, the local smooth background and the chosen cutoff. No numerical radius or inverse bound is certified.

Inside B_(delta/2), (1) equals the actual variable expression

 V(P+X).grad h-h+U[h].grad rho0(P+X).                 (2)

Outside B_delta its transport and coupling are the frozen source ones. Its velocity is still the full-plane L2 Riesz velocity of h. Thus this is a whole-plane auxiliary inverse with actual coefficients locally, not a boundary-value inverse on a disk or the original global operator. It has no fixed-support condition on the forcing. It is an unnormalized inverse: full central strain is not a bounded functional on X_alpha by proof 208, so c[h](P+X).grad rho0/3 is not included as an everywhere-defined bounded perturbation.

More generally the proof applies to any smooth source field and C2 background satisfying proof 209's spectral conditions and the source inequality a mu>1, a=g/(A-mu), with alpha<min(1,1/mu). The actual certified modal source has mu<1 and satisfies these hypotheses. This result makes no stationarity assumption mu=1. The source's analytic neighborhood and all needed finite homological gaps were independently verified from the original data in proof 209.

## Riesz projections on the stated intersection space

Let P_vec be the positive orthogonal projection in L2(R2;R2) with matrix symbol

 (P_vec)_(ij)(zeta)=zeta_i zeta_j/|zeta|^2.

Equivalently P_vec=grad Delta^(-1)div. Its diagonal entries are M and I-M, and its off-diagonal entries are U1. Proof 208 proves that each is bounded on X_alpha: high annuli use a localized L1 kernel and Holder cancellation, while the low block uses its L2 kernel and the L2 input norm. Use the sum of component X_alpha norms for vector fields and a fixed corresponding matrix norm. Write C_P for a finite bound of P_vec in that norm.

If b is a bounded C^alpha scalar or matrix coefficient, product differences and the L2 supremum estimate give

 ||b f||X<=C(||b||infinity+[b]_alpha)||f||X.          (3)

Both parts of X_alpha are needed. A homogeneous Holder seminorm alone would not justify the low-frequency multiplier or these global realizations.

## Exact pullback of the weak Poisson equation

We prove the needed Riesz conjugation estimate directly. Let Phi be a smooth global diffeomorphism equal to the identity outside a compact set, with positive determinant and small ||DPhi-I||infinity. Set

 C_Phi h=h composed Phi^(-1),
 A(Y)=DPhi(Phi^(-1)Y), j(Y)=1/det A(Y),
 a_k(Y)=A(Y)e_k, G(Y)=j(Y)A(Y)A(Y)^T.                (4)

Suppose, in the bounded C^alpha norm,

 ||A-I||C^alpha<=epsilon<=epsilon0.                 (5)

For fixed alpha and sufficiently small epsilon0, determinant formulas, reciprocals bounded away from0 and product differences imply

 ||j-1||C^alpha+||G-I||C^alpha
       +sum_k||j a_k-e_k||C^alpha<=C epsilon.       (6)

The inverse matrix and A^(-T) have uniformly bounded C^alpha norms. The determinant and derivative bounds give uniform bounds on C_Phi and its inverse on X_alpha, by change of variables for L2 and the Lipschitz difference bound for C^alpha. These bounds depend on alpha and the small derivative bound, not on the support size of Phi-id.

For h in X_alpha, first put f=C_Phi^(-1)h. Let q be the weak homogeneous-H1 potential with

 grad q=P_vec(e_k f),
 integral grad q.grad phi=integral f partial_k phi  (7)

for compact smooth tests phi. This realization can be defined by its L2 gradient: the Fourier projection is curl-free, so it has a local H1 potential, unique up to a constant, and its Fourier divergence gives(7). The gradient is also in X_alpha by the projection bound, giving a C1 local representative of q. No arbitrary harmonic gradient can be added, since the specified gradient is the L2 Fourier projection.

Write q_tilde=q composed Phi^(-1) and w=grad_Y q_tilde. The gradient chain rule and the change of variables dx=j(Y)dY in(7) give

 integral G w.grad phi=integral j a_k h.grad phi.    (8)

In particular

 C_Phi (P_vec)_(ik) C_Phi^(-1)h=a_i.w.              (9)

This proves the direction of both Jacobian factors and identifies the physical output component. The metric is G=j A A^T, not j A^T A. The forcing vector is j a_k h. These formulas follow from the transformed weak equation, including its full local multiplier contribution.

The field w belongs to L2 and to X_alpha. Indeed

 w=A^(-T) C_Phi[P_vec(e_k C_Phi^(-1)h)],

and composition, P_vec and multiplication by A^(-T) are all bounded in the stated norms. Uniformly under(5),

 ||w||X<=C_alpha||h||X.                              (10)

This is a membership and crude norm estimate, not yet the small commutator estimate.

Equation(8) now gives an exact projection identity:

 w=P_vec[j a_k h-(G-I)w].                            (11)

To verify it, w is an L2 gradient, hence P_vec w=w. The distributional divergence of w-[j a_k h-(G-I)w] is zero by(8), so its Fourier projection is zero. Since all terms are L2, frequency0 contributes no undetermined distribution. This argument both proves(11) and identifies its solution with the actual transformed Poisson potential. One could also invert I+P_vec(G-I) for smaller epsilon; no separate solvability assumption is needed here.

Subtract P_vec(e_k h) in(11). Equations(3),(6),(10) give

 ||w-P_vec(e_k h)||X
 <=C_P{||(j a_k-e_k)h||X+||(G-I)w||X}
 <=C_alpha epsilon||h||X.                           (12)

Since a_i-e_i is O(epsilon) in C^alpha, (9),(10),(12) imply the full operator-norm estimate

 ||C_Phi (P_vec)_(ik) C_Phi^(-1)-(P_vec)_(ik)||_(X->X)
                         <=C_alpha epsilon.        (13)

This proves the small Riesz error by exact elliptic covariance. It does not infer smallness from C_Phi-I, which need not tend to0 in operator norm on this space. There is no unproved singular-integral change-of-coordinates estimate in(13).

## Size of the source-coordinate error

For Phi=Phi_delta from proof 209,

 ||DPhi_delta-I||infinity<=Cdelta,
 [DPhi_delta-I]_alpha<=C_alpha delta^(1-alpha).

Its inverse has uniformly bounded Lipschitz constant. Composition in(4) therefore gives

 ||A-I||C^alpha<=C_alpha delta^(1-alpha).            (14)

For sufficiently small delta this meets(5). Applying(13) to the (1,1) entry yields

 ||C_delta M C_delta^(-1)-M||_(X->X)
                         <=C_alpha delta^(1-alpha). (15)

All matrix products, coefficients and multipliers in this estimate act on the complete global space X_alpha. The compact support of the coordinate modification is not being mistaken for compact support of its nonlocal image.

## Inversion with actual source coefficients

Let B=diag(A,mu), and let L0=B X.grad-1-gM on D_alpha of proof 208. Its inverse R0 is bounded on X_alpha for every alpha<1 at the actual modal source. The absence of a forcing-support restriction in that theorem is needed here: the output of the Riesz commutator in(15) is generally noncompact.

Write the localized coefficient term in(1) as E_delta. Proof 208 proves

 ||E_delta||_(X->X)<=C delta^(1-alpha),               (16)

because rho0_x(P)=0, rho0_y(P)=g and rho0 is C2 on the fixed source neighborhood. The product estimate checks the complete range, including low frequencies and cutoff-boundary differences.

By the exact transport identity of proof 209,

 C_delta L_delta C_delta^(-1)=L0+Q_delta,
 Q_delta=-g(C_delta M C_delta^(-1)-M)
                         +C_delta E_delta C_delta^(-1). (17)

Equation(17) holds on exactly D_alpha, which is the pullback of D_delta. All remaining terms are bounded on X_alpha by(15)-(16), with

 ||Q_delta||_(X->X)<=C_total delta^(1-alpha).        (18)

Here C_total depends only on the fixed alpha, source parameters, background, conjugacy construction and cutoff. For sufficiently small delta,

 q_delta=C_total delta^(1-alpha)||R0||<1.

The factorization L0+Q_delta=(I+Q_delta R0)L0 on D_alpha gives

 L_delta^(-1)=C_delta^(-1) R0
                    (I+Q_delta R0)^(-1) C_delta,
 ||L_delta^(-1)||_(X->X)
 <=||C_delta^(-1)|| ||C_delta|| ||R0||/(1-q_delta).  (19)

The series in(19) converges in operator norm. It proves injectivity and surjectivity onto X_alpha. The inverse maps onto exactly D_delta by the graph identity, and the graph is closed by bounded conjugation of the closed bounded perturbation L0+Q_delta. Equivalently all couplings in(1) are bounded on X_alpha, so D_delta is also its maximal X_alpha domain. This verifies input membership, image membership and closedness without differentiating a C^alpha input in an uncontrolled direction.

The inverse bounds remain bounded as delta tends to0: proof 209 bounds both composition norms uniformly, R0 is fixed, and q_delta tends to0. The construction can be restricted to odd-y functions. The background, its transport reduction, the radial cutoff and the complete coupled operator preserve this parity, and the full-space unique inverse then preserves it as well. No assertion about evenness around the shifted source coordinate is required.

## Strain and the limits of this local result

For a prescribed real scalar b one may add the localized column

 b H_delta, H_delta=chi_delta(P+X).grad rho0(P+X)/3,

as a forcing. The dot product vanishes at X=0 because rho0_x(P)=0 and P_y=0. It is C1 locally, so its cutoff has X_alpha norm at most C delta^(1-alpha), by the same product estimates and compact support. Thus(19) solves L_delta h=f-bH_delta with a bound in terms of ||f||X+Cdelta^(1-alpha)|b|.

This does not impose b=c[h]. Proof 208's smooth compact case1-parity packets have bounded X_alpha norms and strains growing as epsilon^(alpha-1), and the strain integral need not exist for a general X_alpha input. A normalized source realization therefore needs origin regularity or a separate compatible scalar system. Nor does the auxiliary inverse by itself patch the source to the origin, invariant axes and far field: commutators between those localizations, their domains and global normalization are additional obligations. No unconditional profile existence or actual global inverse follows. The nonlinear graph obstruction and high-space conditions(I),(S) are unchanged.

Dependencies are proof 208 for the precise no-support frozen inverse and multiplier bounds, proof 209 for the directly proved transport reduction and its original-data hypotheses, and proof 15 for the source association. The elliptic pullback and every new norm, domain and inverse step are proved here. There is no new numerical calculation. Independent independent cross-audit of(8)-(13), the cutoff metric size and the exact maximal-domain factorization is requested before theory author integration.
