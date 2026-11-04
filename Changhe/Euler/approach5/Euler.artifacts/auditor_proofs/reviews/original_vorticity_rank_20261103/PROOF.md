# Exterior vorticity density, tail rank and a conditional nonexistence theorem

Status: CONFIRMED at the exact conditional or countertest scopes in A595, A598. Full independent proof postread completed. The unrestricted campaign conjecture is not proved.

## 1. Precise hypotheses and conclusions

Fix2/5<c<1/2 and finite omega. Put p=(1-c)/c in(1,3/2), a=1-2c, b0=2(1-c), beta=(p-1)/(2p), Jx=(-x2,x1,0), A=cI-omega J, L=(1-c)I+omega J, Q_t=exp(omega tJ), T_t=exp(tA). Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, LU+DU(Ay+U)+grad P=0,
    U.curl U=0 everywhere,
    |U(y)|<=C(1+|y|)^-p,
    ||DU(y)||<=C(1+|y|)^(-p-1).

The exact derivative package A498,A476,A492,A516 allows the two natural bounds to be replaced by uniform U->0 and DU=O(sqrt r). It does not remove a derivative premise.

If Omega=curl U is nonzero on a dense subset of one exterior {|y|>R0}, then the actual leading velocity V and canonical pressure P2 satisfy

    grad[(Ax).V] cross grad[P2-|V|^2/2]=0

on the entire punctured space D. Exterior real analyticity of U is an alternative: it gives the stated density unless U=0 already.

If also S=P2-|V|^2/2 is identically zero, or b=|S|^beta is locally A2 on D=R3 minus{0}, then U=0. Here local A2 means b>0 almost everywhere, b and b^-1 locally integrable, with bounded products of their ball averages on compact subdomains. The independently confirmed core theorem is in the team records (A596). Explicit sufficient cases are the controlled charts in the team records: radial surface/curve charts with eta=m beta<j, j1/2, and transverse product charts with each eta_i=m_i beta<1, covering EVERY zero. Analyticity of the original U does not establish A2, nodal geometry or analyticity of the limiting S.

Dependencies are A413 (global helicity-free rank at C2), A530-A531,A538-A539 (natural velocity and pressure limits with first derivatives), the independently reconstructed weighted removability theorem, and the elementary energy identity checked below. For S identically zero the weighted theorem is unnecessary.

## 2. Transfer rank before taking the limit

Define B=Ay+U, H=P+|U|^2/2+(Ay).U, g=U.B and R=P-|U|^2/2. Then H-g=R. Momentum makes grad P C1, hence P,H,g,R C2. A413 gives grad H cross grad g=0 on {Omega!=0}. It uses the full global sublinear helicity-free profile, not a local claim about two first integrals. Its global recurrence, vorticity completeness and C2 Sard hypotheses hold here.

Thus grad H cross grad R=0 on {Omega!=0}. Both gradients are continuous, so the original exterior-density assumption extends this identity to every point of that exterior. No statement is made in an open irrotational interior region.

Normalize pressure by its canonical limit Pinf and set

    u_t(x)=exp((1-c)t)Q_t U(T_t x),
    P_t(x)=exp(b0 t)(P(T_t x)-Pinf),
    S_t=P_t-|u_t|^2/2,
    h_t=exp(at)(H(T_t x)-Pinf),
    k_t=(Ax).u_t.

The independently confirmed limits give u_t->V and P_t->P2 in C1 on each compact subset of D. The exact identity is

    h_t=k_t+exp(-t)(P_t+|u_t|^2/2),
    S_t=exp(b0 t)(R(T_t x)-Pinf).

Here a-b0=-1. Hence h_t->k=(Ax).V and S_t->S in C1 locally. For each compact K in D, all T_t K eventually lie in the exterior where the original rank holds. Both scaled gradients are nonzero scalar multiples of the same invertible transpose T_t^T acting on their respective original gradients. Linear dependence is preserved. Thus grad h_t cross grad S_t=0 on K for all sufficiently large t. Uniform gradient convergence gives global tail rank on K, and K was arbitrary.

This argument does not divide by Omega or W=curl V. In particular it remains valid if W vanishes on an open limiting cone. Density is used before scaling, not inferred after it.

## 3. Exterior analyticity and compact vorticity

The exterior is connected. If analytic Omega vanishes on any nonempty open subset, the real analytic identity theorem, applied componentwise along chains of overlapping analytic balls, makes Omega zero on the whole exterior. Failure of density therefore makes Omega compactly supported. Only exterior analyticity is used.

Since U is bounded, B has at most linear growth and its C2 flow Phi_t is complete in both time directions. The exact Cauchy law is

    Omega(Phi_t x)=exp(-(1+c)t) DPhi_t(x) Omega(x).

The derivative matrix is invertible. Consequently O={Omega!=0} is an invariant open set for all real times. With div B=3c, its flow Jacobian is exp(3ct). A nonempty compactly supported vortical set has positive finite volume. Invariance and change of variables would give |O|=exp(3ct)|O| for t>0, impossible. Thus Omega=0. The identity Delta U=grad div U-curl Omega gives componentwise harmonic U. Boundedness and decay force U=0 by harmonic Liouville. No unique continuation theorem for smooth vorticity has been substituted for analyticity.

## 4. The pressure mean, including the identically-zero scalar branch

Write Rv=integral_S2 |V.n|^2, Tv=integral_S2 |V-(V.n)n|^2, Pm=integral_S2 P2. The actual pressure satisfies -Delta P2=partial_i partial_j(V_iV_j). Test it against a smooth radial chi supported in a compact annulus. Rotating homogeneity preserves all three angular integrals and their factor r^-2p. The Hessian of chi contracts with V tensor V as chi''|V.n|^2+(chi'/r)|V_T|^2. Therefore

    -Pm integral r^(2-2p)(chi''+2chi'/r)dr
      =Rv integral r^(2-2p)chi''dr
         +Tv integral r^(1-2p)chi'dr.

For clarity put n=2-2p. Compact-support integration by parts gives integral r^n chi''=n(n-1) integral r^(n-2)chi and integral r^(n-1)chi'=-(n-1) integral r^(n-2)chi. Cancelling n-1, and using n-2=-2p, yields

    Pm=[(2-2p)Rv-Tv]/(2p),
    integral_S2 S=-[(3p-2)Rv+(p+1)Tv]/(2p).

Both coefficients in the final numerator are positive for p>1. If S is identically zero, V=0 on the sphere and hence everywhere by homogeneity and continuity. A nonzero global tail instead has strictly negative spherical mean S. This is an integral sign, not a pointwise sign assertion. The original pressure normalization and actual Poisson equation are essential inputs to this branch.

For nonidentically-zero S with the stated local A2 property, Section2 gives the global rank required in the independent weighted proof A596. The all-zero chart versions A593-A594 imply that property by their exact power-weight estimates. The other inputs, div V=0, scalar and velocity homogeneity and W.grad S=0, are supplied by the actual tail identities. That proof gives V=0 with no velocity symmetry assumption.

## 5. Vanishing actual tail implies vanishing full profile

The confirmed pressure estimates give |grad P|<=C r^(-2p-1) and |P-Pinf|<=C r^-2p. Set q=2p+1>3 and N=DU U+grad P=O(r^-q). Along a linear spiral the exact momentum equation reads

    d/dt[exp(tL)U(T_t y)]=-exp(tL)N(T_t y).

The left expression tends to the actual V(y)=0. Integration from0 to infinity gives

    U(y)=integral_0^infinity exp(tL)N(T_t y)dt,
    |U(y)|<=C r^-q,

because ||exp(tL)||=exp((1-c)t) and (1-c)-cq=-1. Thus U is square integrable.

Taking the scalar product of momentum with U gives the exact divergence identity

    (1-5c/2)|U|^2
      +div[B|U|^2/2+(P-Pinf)U]=0.

For a radial cutoff at scale R, the dilation, cubic and pressure errors are bounded respectively by C R^(3-2q), C R^(2-3q) and C R^(2-2p-q). The omega Jy term is tangent to the cutoff spheres. All errors vanish. Dominated convergence for the bulk gives (1-5c/2) integral|U|^2=0. The coefficient is negative and nonzero in the target interval, so U=0.

## 6. Audit scope

The theorem adds global helicity freedom, a derivative bound, original exterior density or exterior analyticity, and the actual A2 scalar-weight property, or one of its explicit all-zero chart conditions. It is a full conditional nonexistence theorem at those hypotheses. It neither proves tail analyticity from original analyticity nor derives density or nodal control from decay. The S identically zero case is separately proved by pressure mean because it satisfies neither chart definition.

Existing coordinator CO33 independently checks the mean identity and scalar component law. The actual coordinator in the team records comparison and full independent weighted completion are retained with the companion A2 proof. No mathematical computation, new model client, formal build, server or cluster is used.
