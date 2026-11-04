# The next actual scalar and its weak rank extraction

Status: A647,A648 CONFIRMED at the exact hypotheses below, after complete source and independent proof postreads.

## 1. Exact hypotheses and statement

Let 2/5<c<1/2, c!=3/7, omega in R, p=(1-c)/c, a=1-2c, b=2(1-c), nu=3-2c, A=cI-omega J and L=(1-c)I+omega J. Here J(x1,x2,x3)=(-x2,x1,0). Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, LU+DU(Ay+U)+grad P=0,
    U.curl U=0 everywhere,
    |U(y)|<=C(1+|y|)^-p, |DU(y)|<=C(1+|y|)^(-p-1).    (1)

C is finite and may depend on the profile,c,omega. The exact derivative screens A498,A601 allow uniform U->0 together with DU=O(sqrt r) in place of the last line. Bare decay alone does not supply it or zero helicity.

On D=R3 minus{0}, let V and P2 be the actual leading velocity and canonical pressure, Pinf the pressure constant, and define

    W=curl V, k=(Ax).V, S=P2-|V|^2/2,
    Z=DV V+grad P2,
    -Delta p1=partial_i partial_j(V_i Z_j+Z_i V_j),
    p1(exp(sA)x)=exp(-nu s)p1(x),
    tau=p1-2V.grad P2.                                 (2)

The continuous p1 exists and is unique by A575 under c!=3/7; it is the actual first pressure correction described below. Then tau belongs locally to C1,alpha for every alpha<1, has scalar twisted degree -nu, and obeys

    W.grad tau=0 on D,
    dk wedge d tau=0 on {W!=0}.                         (3)

On every connected component O of {W!=0,k!=0},

    tau=C_O |k|^(nu/a)                                  (4)

for some real constant C_O, which may be zero. No density, symmetry, nonvanishing or weight premise is used. No global rank on an open irrotational set is concluded.

## 2. Actual limits and regularity

Put Q_t=exp(omega tJ), T_t=exp(tA), and

    u_t=exp((1-c)t)Q_t U(T_t x),
    p_t=exp(bt)(P(T_t x)-Pinf),
    S_t=p_t-|u_t|^2/2, z_t=exp(t)(u_t-V),
    Pi=P2+|V|^2/2, S1=p1-V.Z.                           (5)

A538,A539 give, locally on D, u_t->V in C1,alpha, p_t->P2 in C2,alpha and z_t->Z in C^alpha for every alpha<1. There are uniform local W2,q bounds for u_t and W1,q bounds for z_t for every finite q>3. Thus V is W2,q, Z is W1,q, and

    curl z_t -> curl Z weakly in Lq_loc.                (6)

Indeed every weak subsequential limit is identified by distributional convergence from z_t->Z, and reflexive compactness proves convergence against every fixed local dual test for the whole family. It is not convergence of these derivatives in C0.

A575 supplies the uniform expansion of p_t after subtraction of finitely many slow harmonic pressure multipoles, indexed by n>=0 with r_n=(n+5)c-2<1. A623 makes every one identically zero under (1), without density or scalar A2. Consequently

    exp(t)(p_t-P2)->p1,
    exp(t)(S_t-S)->S1                                   (7)

locally uniformly. At c=3/7 A575 does not give (7); the harmonic scalar r^-5 P4(x3/r) has exactly the required degree for every omega. That exponent is excluded throughout this proof.

The Poisson equation and div V=0 imply div Z=0. The divergence-free product identity gives

    partial_i partial_j(V_i Z_j+Z_i V_j)
       =2 sum_(i,j)(partial_j V_i)(partial_i Z_j).        (8)

These are distributional identities on D. To check the product rules, mollify V and Z in the interior of a slightly larger open set. Their mollifications remain divergence free there. They converge locally in their Sobolev spaces; DV also converges uniformly because V is C1. The products on the right of (8) converge in Lq, and the stress converges as a distribution. The same argument proves div Z=0 from its definition. No boundary or origin term enters a compactly supported local test.

The right side of (8) lies in Lq_loc. Interior Poisson regularity therefore gives p1 in W2,q_loc; its known continuity supplies the local Lq bound for the estimate. Choosing q>3/(1-alpha) gives p1 in C1,alpha_loc. The same is true of V.grad P2, so tau has the claimed regularity. In addition k,S belong to W2,q_loc and S1,H2 below belong to W1,q_loc. All ensuing differentiated products are thus ordinary Sobolev products, not undefined products of distributions.

## 3. A convergent primitive for the next rank

Use the exact full-profile scalar

    H=P+|U|^2/2+(Ay).U,
    H_t=exp(at)(H(T_t x)-Pinf),
    k_t=(Ax).u_t, Pi_t=p_t+|u_t|^2/2.

The scaling factors give exactly

    H_t=k_t+exp(-t)Pi_t.

Hence, with h_t=exp(t)(H_t-k) and s_t=exp(t)(S_t-S),

    h_t->H2=(Ax).Z+Pi,
    s_t->S1                                             (9)

locally uniformly. The unscaled dS_t converge uniformly to dS. Direct differentiation and homogeneity yield

    V.grad k=c|V|^2+(Ax).DV V,
    (Ax).grad P2=-bP2,
    H2=V.grad k-aS.                                    (10)

A413 gives dH_t wedge dS_t=0 on {curl u_t!=0}. Its leading limit is dk wedge dS=0 on O0={W!=0}. For every compact subset of O0, curl u_t is nonzero on a neighborhood for sufficiently large t. There the exact difference of two-forms has the following especially short primitive:

    exp(t)[dH_t wedge dS_t-dk wedge dS]
       =d[h_t dS_t-s_t dk].                            (11)

For verification, d(h_t dS_t)=exp(t)(dH_t-dk) wedge dS_t and -d(s_t dk)=exp(t)dk wedge(dS_t-dS). Adding gives (11), with exactly the displayed signs.

By (9), (7) and unscaled C1 convergence of S_t, the one-form in (11) converges uniformly on compact sets to H2 dS-S1 dk. Its exterior derivative therefore converges in distributions. The left side vanishes identically on each such neighborhood, giving

    d(H2 dS-S1 dk)=0,
    dH2 wedge dS+dk wedge dS1=0 on O0.                 (12)

This argument uses neither exp(t)D(u_t-V) convergence nor differentiated convergence in (7). In particular a possible slow derivative error is not silently discarded.

## 4. Subtract the transported leading rank

The locally W1,q two-form dk wedge dS is zero on O0. Its Lie derivative along the C1 field V is therefore zero as a distribution. The coordinate formula and Sobolev product rule give

    d(V.grad k) wedge dS+dk wedge d(V.grad S)=0.         (13)

For completeness, the coefficient of dx_i wedge dx_j on the left expands into V applied to the coefficient k_i S_j-k_j S_i, plus the two terms multiplying that zero two-form by derivatives of V. This is the coordinate definition of its Lie derivative. The derivatives of k,S through order two lie in Lq, so the calculation is legitimate almost everywhere and then distributionally. It uses no third derivatives and no invariant global V-flow.

Subtract (13) from (12), use H2=V.grad k-aS and dS wedge dS=0, and obtain

    dk wedge d(S1-V.grad S)=0.

The cancellation

    S1-V.grad S
      =p1-V.(DV V+grad P2)-V.grad(P2-|V|^2/2)
      =p1-2V.grad P2=tau                               (14)

uses V.DV V=V.grad(|V|^2/2). Thus the rank part of (3) holds distributionally. Its coefficients are continuous by Section2, so it holds pointwise.

## 5. The next transported scalar

The exact scalar flux is div(S_t curl u_t)=0 by A510. The leading flux satisfies div(SW)=0. Write w_t=curl u_t. The exact difference can be grouped as

    exp(t)(S_t w_t-SW)=s_t w_t+S curl z_t.               (15)

The first term converges uniformly to S1 W and the second weakly in Lq_loc to S curl Z by (6). Passing divergence through compactly supported tests gives

    div(S1 W+S curl Z)=0,
    W.grad S1=-(curl Z).grad S.                        (16)

The curls are divergence free. These products are locally Sobolev, so the second equality is justified without a boundary integral.

The incompressible curl identity is

    curl Z=curl(DV V)=DW V-DV W=[V,W].                  (17)

Interior mollification of V proves it at W2,q regularity. The leading scalar identity W.grad S=0 belongs to W1,q_loc. Apply V to it and expand, or subtract the two Hessian terms by symmetry, to obtain

    W.grad(V.grad S)=-[V,W].grad S.                     (18)

Every term is in Lq_loc: DW and D2S are in Lq, while V,W,DS,DV are bounded on compact subsets. Subtract (18) from (16) and use (14),(17). This gives W.grad tau=0 almost everywhere on all D. Continuity again upgrades it to pointwise equality, completing (3).

## 6. Degree and componentwise constants

The two factors in V.grad P2 transform by rotations Q_s^T and scalar factors exp(-(1-c)s), exp(-(b+c)s). Their product has factor exp(-nu s), the same as p1. This proves tau's twisted degree.

On a connected component with W and k nonzero, (Ax).grad k=-ak implies grad k!=0. Rank makes grad tau proportional to grad k. Contracting with Ax identifies the coefficient:

    grad tau=(nu tau/(a k))grad k.

The derivative of tau |k|^(-nu/a) is zero. Connected open subsets of R3 are path connected, so it is constant and (4) follows. This does not divide by tau and includes C_O=0. The same calculation gives S=D_O |k|^(b/a). If D_O!=0, eliminate k to express tau as a constant multiple of |S|^(nu/b). No continuity argument connects constants across distinct vortical components or an irrotational open region.

A576 already makes tau zero on its particular escaping zero-g sheets. That is consistent with (3); neither statement makes tau nonzero or excludes it from vanishing identically. Applying a scalar-symmetry Liouville theorem to tau would require its own additional symmetry and inverse-integrability premises. They have not been established.

## 7. Dependencies and comparison

The complete LIT165 source, A539 reconstruction, A575 pressure proof and the relevant A413/A510/C40 rescalings were read. Sections3 and5 use independent shorter exact primitives; Sections2,4 and5 explicitly check the source's weak product rules. The actual configured-model LIT158 comparison motivated the formal rank coefficient. The resulting full necessary theorem is supplied for continuing focused model comparison through the existing agents. Configured identifier the primary model is not an independent provider-runtime attestation.

All arguments are local on D after importing the confirmed actual global coefficients. There is no origin integration, unproved pressure normalization, finite-mode truncation, convergence of a differentiated correction, or symmetry reduction of the global profile. Every finite omega is covered; c=3/7 is explicitly not. No computation or formal build is used. A separate exact germ audit is required before the new theorem can exclude any of the leading-order local examples.
