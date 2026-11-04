# Adjoint moments and the scattering profile

## Statement

Let 2/5<c<1/2 and omega be any finite real number. Write A=cI-omega J, k=(1-c)/c, alpha=3-2k=5-2/c and

    L U=(1-c)U+(Ay.grad)U+omega J U.

Assume U,P are C1 on R3, div U=0, LU+(U.grad)U+grad P=0, U is bounded, and U(R dot) tends to zero in distributions as R tends to infinity. These are the H0(C1), Hb hypotheses of the audited energy theorem. Let Phi be C1 away from zero and satisfy

    div Phi=0, L^T Phi=(1-4c)Phi-omega J Phi-(Ay.grad)Phi=0.

Set Psi=Phi restricted to S2. Then N_Phi=int_R3 U_i U_j partial_j Phi_i is absolutely convergent, and

    N_Phi=lim_(R->infinity) (c/R) int_(R<|y|<2R) |y| U.Phi dy.       (1)

If additionally ell=(curl U) cross U belongs to Lp(R3) for one 1<p<3/k, let F in Lp(S2) be the profile of the A251 semigroup tail. Then

    N_Phi=c int_S2 F.Psi dS.                                      (2)

The Dini hypotheses of A210/A250 imply the additional integrability in this range, so (2) applies to their continuous tail. No assumed pressure normalization is needed. These are identities, with no asserted sign or nonexistence conclusion.

## 1. Exact transpose kernel

Integration by parts using tr A=3c and J^T=-J gives precisely the displayed L^T. Put Q_s=exp(omega J s), sigma(y)=log|y|/c and pi(y)=Q_sigma(y)y/|y|. Solving L^T Phi=0 along e^(sA)y gives

    Phi(e^(sA)y)=exp((1-4c)s) Q_s^T Phi(y),
    Phi(y)=|y|^(k-3) Q_sigma(y)^T Psi(pi(y)).                        (3)

Thus |Phi(y)|<=C0 |y|^(k-3) and |D Phi(y)|<=C1 |y|^(k-4), with finite constants given by the norms on S2. Rotations are isometries, so the derivative estimate is obtained by differentiating (3), not by assuming that angular derivatives disappear.

Write Psi=Psi_r w+Psi_t on S2 and orient longitude phi so that exp(theta J) increases it. Direct spherical divergence gives

    div Phi=r^(k-4)[(k-1)Psi_r+(omega/c)partial_phi Psi_r
                    +div_S2 Psi_t](pi(y)).                        (4)

Therefore the kernel description in Theory Agent A T.9 is correct. In particular its radial part has zero integral, since k!=1. The toroidal fields Psi=w cross grad_S2 chi, chi in C2(S2), satisfy (4). If Psi_r is smooth with zero mean, solve the sphere Poisson equation with right side -(k-1)Psi_r-(omega/c)partial_phi Psi_r and set Psi_t=grad_S2 h. Its solvability follows from zero mean. These give the claimed infinite-dimensional family.

The axis field Phi_J=|y|^(k-4)Jy is one such element, obtained from chi=-w3. If omega=0, the same is true with J replaced by the cross-product matrix of any fixed vector e. The latter extension is not asserted for arbitrary e when omega is nonzero.

## 2. The inner boundary and absolute convergence

On the annulus r<|y|<rho, integrate the momentum equation against Phi. All functions are classical there. The adjoint and divergence identities give

    M(rho)-M(r)=int_(r<|y|<rho) U_i U_j partial_j Phi_i,

where

    M(t)=ct int_S_t U.Phi + int_S_t (U.n)(U.Phi) + int_S_t P Phi.n.

Near zero U and P are bounded. The three boundary terms are respectively O(r^k), O(r^(k-1)), O(r^(k-1)). Because 1<k<3/2 they all tend to zero. The bulk integrand is locally bounded by C r^(k-4), whose volume integral near zero is finite exactly when k>1. Thus

    M(rho)=int_(|y|<rho) U_i U_j partial_j Phi_i                    (5)

for every rho>0. The flux of Phi through S_rho is independent of rho and is O(r^(k-1)) near zero, hence vanishes. One may replace P in (5) by P minus any constant.

The audited energy theorem gives E(R)=int_B_R |U|^2<=C R^alpha for R>=1. On a dyadic annulus,

    int_(R<|y|<2R) |U|^2 |D Phi|
        <=C R^(k-4+alpha)=C R^(-1-k).

Summing proves global absolute convergence. This argument needs energy growth, not a pointwise decay rate of U or DU.

## 3. The outer boundary without pointwise pressure decay

Average (5) over rho in [R,2R], dividing by R. Its first boundary term becomes the expression in (1). The convection boundary is bounded by

    C R^(-1) R^(k-3) E(2R)<=C R^(-1-k),

which tends to zero.

Use the canonical pressure decomposition proved in the audited energy report. On the annulus write P-p_R=Pi1+Pi2+Pi3, where

    ||Pi1||_2<=C ||U||_infinity E(4R)^(1/2),
    |Pi2|+|Pi3|<=C R^(alpha-3)=C R^(-2k).

The first estimate can retain the smaller exterior supremum of U, but boundedness alone is enough here. Since ||Phi||_L2(annulus)<=C R^(k-3/2), its contribution to the averaged boundary is at most

    C R^(-1) R^(alpha/2+k-3/2)=C/R.

The other two contributions are at most C R^(-1) R^(-2k) R^k=C R^(-1-k). The arbitrary pressure constant has zero flux by Section 2. All pressure boundaries therefore vanish. Dominated convergence for the absolutely convergent bulk integral proves (1). In particular no pointwise pressure limit has been inserted.

## 4. The profile pairing

A251 gives U=V+W, W in Lp(R3), with

    V(y)=|y|^(-k)Q_sigma(y)^T F(pi(y)).

Dotting with (3) cancels the simultaneous rotations and yields V.Phi=|y|^(-3)(F.Psi)(pi(y)). Rotation invariance of spherical measure now gives exactly

    (c/R) int_(R<|y|<2R) |y| V.Phi=c int_S2 F.Psi.

For the remainder, Holder's inequality gives

    (c/R) int_(R<|y|<2R) |y| |W| |Phi|
       <=C R^(k-3/p) ||W||_Lp(annulus) ->0,

because p<3/k. This proves (2). Under Dini, the sufficient Lamb-vector estimates in A251 hold in the entire present c range. The abstract semigroup tail and the continuous Dini tail coincide by their already audited homogeneity and remainder comparison.

## 5. Angular momentum and radial vorticity

For Phi_J the derivative is

    partial_j(Phi_J)_i=r^(k-4)J_ij+(k-4)r^(k-6)(Jy)_i y_j.

The skew term contracts to zero against U_i U_j. Hence

    N_Phi_J=(k-4) int r^(k-6)(U.Jy)(U.y).

This is the claimed angular momentum moment, and it equals c int_S2 F.Jw when (2) applies.

If V is C1 near S2 and chi in C2(S2), Stokes applied to chi V gives

    int_S2 chi w.curl V=-int_S2 V.(w cross grad_S2 chi).

Thus the toroidal family in (2) determines the distribution w.curl V, and in the stated C1 case determines its classical radial trace. The sign in T9.1 is correct. No differentiability of F beyond that explicitly stated is silently inferred from its Lp or continuous membership.

## Dependencies and limits

The only analytic inputs beyond integration by parts are the already audited natural energy growth, canonical-pressure annular bounds and A251 semigroup decomposition. They are recorded in the team records and in the team records, with the underlying energy-report references. The proof uses 2/5<c<1/2. At c>=1/2 the inner boundary and its absolute majorant no longer have the required decay; no extension to that range is claimed. The endpoint comparison in T9.3 is only a formal observation under its additional smooth-tail conditions, not an application of the present theorem at c=2/5.

## Supplement: continuous curl traces and a positive finite-mode moment

Under the Dini hypotheses above, both V and curl V=Omega_tilde are continuous on an annular neighbourhood of S2. Mollify on a slightly smaller annulus. The mollified fields and their curls converge uniformly near S2. Stokes on the closed sphere gives

    integral_S2 chi w.curl V_e = -integral_S2 V_e.(w cross grad chi).

Uniform convergence passes this identity to V, for every chi in C2(S2). Thus T9.1's radial-vorticity moment needs no C1 regularity of V beyond its continuous distributional curl. The sphere identity is local to its annular neighbourhood and presumes no smoothness at the singular origin.

Under the general hypotheses of part(2), F may be only in Lp(S2), with p>1. Its divergence constraint is, distributionally,

    (2-k)F_r+(omega/c)partial_phi F_r+div_S2 F_t=0.          (10)

Let F_N be its projection onto the finite vector spherical-harmonic blocks of degrees at most N. Each block consists of radial harmonics, their tangent gradients, and their tangent rotations. The scalar longitude derivative preserves each degree, as do the divergence and gradient maps between the corresponding scalar and vector blocks. Hence F_N satisfies (10). This finite projection is well-defined by integration against smooth harmonics even when F is not globally L2. If F!=0 as an Lp field, at least one F_N is nonzero by completeness of smooth spherical harmonics.

Integrating (10) shows integral F_r=0, since 2-k>0. Therefore integral F_(N,r)=0. Solve the finite-dimensional sphere Poisson equation

    Delta_S2 h=F_(N,r), integral h=0,

and set Psi=F_N+alpha grad_S2 h. Its radial part is unchanged. Using (10), alpha=3-2k and (4) gives

    (k-1)Psi_r+(omega/c)partial_phi Psi_r+div_S2 Psi_t
       =(2k-3+alpha)F_(N,r)=0.

Thus the smooth field Phi defined by (3) is an admissible adjoint test. Since Psi lies in the same finite harmonic space, integration against F equals integration against F_N. Moreover

    integral F_N.grad h
       =(2-k)integral h Delta h
          +(omega/c)integral h partial_phi Delta h
       =-(2-k)||grad h||_2^2.

The last rotation term vanishes because partial_phi is skew-adjoint and commutes with the sphere Laplacian. The first nonzero sphere eigenvalue is2, so

    ||grad h||_2^2 <= ||F_(N,r)||_2^2/2 <= ||F_N||_2^2/2.

Consequently part(2) gives the positive moment

    integral U_i U_j partial_j Phi_i
       =c integral F.Psi
       >=c[1-alpha(2-k)/2]||F_N||_2^2>0.                  (11)

Here 1<k<3/2 and 0<alpha<1, so the bracket is greater than1/2. This confirms T9.4 also when F is only Lp. It is a compatibility identity, not a contradiction: the test depends on F and no independent nonpositive estimate for its bulk moment is available.
