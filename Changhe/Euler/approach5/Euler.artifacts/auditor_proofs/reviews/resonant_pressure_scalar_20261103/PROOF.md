# The pressure correction at the resonant exponent

Status: CONFIRMED A653-A655, independent audit of LIT167-LIT168. The exact borderline pressure expansion, its necessary scalar, and the ordinary correction limit are proved below under the stated global zero-helicity and natural bounds. No unrestricted nonexistence result is asserted.

## 1. Exact hypotheses and conclusions

Let c=3/7, p=4/3, a=1-2c=1/7, b=2(1-c)=8/7, nu=1+b=15/7, Jx=(-x2,x1,0), A=cI-omega J, Q_t=exp(omega tJ), and D=R3 minus{0}. Let omega be any finite real number. Suppose U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, [(1-c)I+omega J]U+DU(Ax+U)+grad P=0,
    U.curl U=0 everywhere,
    |U(y)|<=C(1+|y|)^(-4/3),
    |DU(y)|<=C(1+|y|)^(-7/3).                              (1)

The finite constant may depend on U and omega. These natural bounds follow from uniform U tending to0 and DU=O(sqrt r) by A498/A601 in the stated full-profile class; bare decay does not supply them.

Let Pinf be the canonical pressure constant, V and P2 the actual leading velocity and canonical leading pressure. Write

    u_t=e^((1-c)t)Q_t U(exp(tA)x),
    p_t=e^(bt)[P(exp(tA)x)-Pinf],
    q_t=e^t(p_t-P2), z_t=e^t(u_t-V),
    W=curl V, k=(Ax).V, S=P2-|V|2/2,
    Z=DV V+grad P2, M1=V tensor Z+Z tensor V.

For omega!=0 set T=2pi/|omega|. Sections2-7 prove that period averages of q_t converge locally uniformly to a selected pbar1 with

    pbar1(exp(sA)x)=e^(-nu s)pbar1(x),
    -Delta pbar1=partial_i partial_j(M1)_ij=2tr(DV DZ) on D,
    tau=pbar1-2V.grad P2 in C1,alpha_loc(D), every alpha<1,
    W.grad tau=0 on D, dk wedge d tau=0 on{W!=0}.           (2)

Section8 proves the stronger ordinary convergence q_t->pbar1 by eliminating its nonconstant rotation-periodic coefficient. The equation and homogeneity alone do not uniquely specify pbar1: r^-5 P4(x3/r) is a nonzero admissible homogeneous harmonic addition. The actual limit fixes that ambiguity.

For omega=0, the already confirmed nonrotating theorem A010, re-audited in A197, gives U0 under(1), and all conclusions hold with zero fields. No limiting argument in T is used at omega0.

## 2. A summable renormalized second stress moment

A623 gives Theta_0=Theta_1=0 at c3/7. Their harmonic contractions vanish, not necessarily their full moment tensors. A550, including its endpoint treatment, then gives for every fixed 0<gamma<1

    Du_t-DV=O(e^(-gamma t)),
    S_t-S=O_(C1)(e^(-gamma t)), S_t=p_t-|u_t|2/2,
    u_t-V=O(e^-t)                                           (3)

locally on D. The kinetic difference and its derivative obey the same required bounds. Thus grad p_t-grad P2=O(e^(-gamma t)), and n_t=Du_t u_t+grad p_t satisfies n_t-Z=O(e^(-gamma t)). The exact terminal integral

    z_t=integral_0^infinity e^-s n_(t+s) ds

gives z_t-Z=O(e^(-gamma t)) locally uniformly. Uniformity on an annulus and the twisted homogeneities of V and Z yield

    U(y)=V(y)+Z(y)+O(r^(-11/3-epsilon)), epsilon=gamma/c>0.  (4)

Here epsilon<7/3. The vector Z has scaling exponent 2-c=11/7 and ordinary size r^-11/3. Rotations preserve norms, so the error is uniform in direction.

Put m=U tensor U-V tensor V, as one difference integrand. Equation(4) gives m-M1=O(r^(-5-epsilon)) at infinity. Indeed VZ has order r^-5, its error has order r^(-5-epsilon), and Z tensor Z is O(r^-22/3), faster because epsilon<7/3. At0, m=O(1+r^-8/3). Define

    R(y)=m(y)-1_(r>=1)M1(y),
    E=integral_R3 y tensor y tensor R(y)dy.                 (5)

This fourth-order tensor is absolutely convergent. Its radial absolute integral is bounded by r^(4-8/3)dr near0 and r^(-1-epsilon)dr at infinity. The sharp cutoff is never differentiated. No ordinary second-moment convergence for m is asserted.

## 3. The exact local pressure split

Let f_t=e^t(u_t tensor u_t-V tensor V). A539 and the factorization (u_t-V) tensor u_t+V tensor(u_t-V) give

    |f_t(y)|<=C|y|^-5 for every y!=0,t>=0,
    f_t->M1 in C^alpha_loc(D), every alpha<1.               (6)

The factorization controls the shrinking core; a separated z_t tensor z_t estimate would be inadequate there.

Fix an annulus r1<=|x|<=r2. Choose a radial chi0 equal1 for |y|<=r1/4 and0 for |y|>=r1/2, and d<r1/8. Let N=-1/(4pi r), N_d a radial cutoff equal to N at radius<=d and0 at radius>=2d, T_d F=(D2N_d)*F with tensor contraction, and K_d=D2(N-N_d). The canonical formula is

    q_t=-T_d f_t-integral K_d(x-y):f_t(y)dy.                (7)

T_d includes its distributional trace term. On the chi0 support, K_d(x-y)=D2N(x-y). Taylor expansion gives

    D2N(x-y)=F0+F1+F2+R3,
    Fj=((-1)^j/j!)D^(j+2)N(x)[y^j], |R3|<=C|y|3.

The full j0 and j1 moment contractions equal e^((1-r_j)t)Theta_j(Q_t^T x)=0, where r_j=(j+5)c-2. Subtract them in(7). This gives

    q_t=A_t-(1/2)D4N(x):I_t,
    I_t=integral chi0(y)y tensor y tensor f_t(y)dy,          (8)
    A_t=-T_d f_t-integral(1-chi0)K_d(x-y):f_t(y)dy
        +sum_(j=0,1) integral(1-chi0)Fj:f_t
        -integral chi0 R3:f_t.

Every term in A_t converges uniformly on the annulus to Ainf. The inner remainder has radial majorant r3 r^-5 r2 dr=dr at0. The outer compensated moments have majorants r^(j-3)dr at infinity, integrable for j0,1. The other outer kernel avoids0 and has faster decay. The local singular operator converges by positive Holder convergence in(6), subtracting f_t(x) at its singularity and integrating r^(alpha-1)dr. All majorants are uniform over the fixed annulus. No unrenormalized integral of M1 through0 is used.

## 4. Exact rotation of the borderline tensor

The change Y=exp(tA)y in I_t gives

    I_t=Q_t^(tensor4) integral chi0(e^(-ct)|Y|)
                              Y tensor Y tensor m(Y)dY.    (9)

The scalar factor is1: f_t contributes e^(nu t), y tensor y contributes e^(-2ct), and dy contributes e^(-3ct), with nu=5c. The R part in(5) contributes Q_t^(tensor4)E+o(1), uniformly in tensor norm.

Let Rho_s=Q_s^(tensor4), G its skew-adjoint generator, and

    T4=integral_S2 theta tensor theta tensor M1(theta)dtheta.

For Y=e^(cs)Q_s^T theta, s>=0, homogeneity gives M1(Y)=e^(-nu s)Q_s^T M1(theta)Q_s. The radial second-moment measure becomes c ds, since 5c=nu. Thus the cutoff M1 part of(9) equals

    c integral_(-t)^infinity chi0(e^(cu))Rho_(-u)T4 du
       =c integral_0^t Rho_v T4 dv+Cchi                     (10)

for all sufficiently large t. The second equality subtracts 1_(u<=0); its difference from chi0(e^(cu)) has compact support. Cchi is a fixed tensor.

Rho has period T, and its average is orthogonal projection onto ker G. Write T4=T0+Tperp and E=E0+Eperp. G is invertible on the finite-dimensional orthogonal complement of its kernel and commutes with Rho there. Hence

    c integral_0^t Rho_v T4 dv=ct T0+cG^-1(Rho_t-I)Tperp.

Equations(8)-(10) yield the locally uniform expansion

    q_t=t Psi+Pstar+Theta(Q_t^T x)+o(1),                    (11)
    Psi=-(c/2)D4N:T0,
    Theta=-(1/2)D4N:[Eperp+cG^-1 Tperp],
    Pstar=Ainf-(1/2)D4N:[Cchi-cG^-1 Tperp+E0].

Newtonian rotation covariance gives the indicated rotation of x. Psi is harmonic, axisymmetric and ordinarily homogeneous of degree -5. Theta is harmonic of degree -5 with zero rotation average. Only fully symmetric trace-free tensor parts survive D4N, so scalar vanishing does not imply full tensor vanishing. Pstar is continuous on D. Different annular definitions agree since Psi and Theta are global and the limit of q_t-tPsi-Theta(Q_t^T x) is unique on overlaps. Constants in G^-1 may depend on omega. This proves an exact possible logarithmic term, not its nonvanishing.

## 5. The logarithmic coefficient vanishes

Set H=P+|U|2/2+(Ay).U, H_t=e^(at)[H(exp(tA)x)-Pinf], h_t=e^t(H_t-k), s_t=e^t(S_t-S), and w_t=curl u_t. Exact rescaling and A539 give

    H_t=(Ax).u_t+e^-t(p_t+|u_t|2/2),
    h_t->H2=(Ax).Z+P2+|V|2/2=V.grad k-aS,
    s_t=q_t-V.z_t-e^-t|z_t|2/2.                             (12)

Thus h_t is locally bounded, s_t/t->Psi uniformly, S_t->S in C1 and w_t->W uniformly. A539 bounds z_t in W1,q_loc for every finite q>3.

On any compact subset of{W!=0}, the full A413 rank holds at late times. Its exact primitive is

    (e^t/t)[dH_t wedge dS_t-dk wedge dS]
       =d[(h_t/t)dS_t-(s_t/t)dk].                          (13)

The left side is zero. The right-hand one-form tends uniformly to -Psi dk. Its exterior derivative converges distributionally, giving dk wedge dPsi=0 on{W!=0}. A510 separately gives the divergence-free flux difference

    (e^t/t)(S_t w_t-SW)=(s_t/t)w_t+(S/t)curl z_t.

The first term tends uniformly to Psi W; the second tends to0 in local Lq norm. Thus W.grad Psi=0 on D. The final identities are pointwise by continuity.

If Psi were nonzero, harmonic degree and axisymmetry give Psi=C r^-5 P4(z), C!=0, P4(z)=(35z4-30z2+3)/8. This polynomial has four simple roots in(-1,1) and no pole root. Its inverse power |Psi|^(-1/15) is locally integrable on D. Since a/nu=1/15, the scalar symmetry theorem A622 applies and forces V axisymmetric. The actual-tail theorem A570 then gives U0 under(1), making M1=T4=Psi=0, a contradiction. Consequently

    Psi=0.                                                (14)

Only the pressure contraction has been shown to vanish. Traceful parts of T0 may remain, so no ordinary second tensor-moment convergence follows.

## 6. The selected averaged scalar and its regularity

Equations(11),(14) make q_t locally bounded and give

    (1/T) integral_t^(t+T) q_s ds ->Pstar=:pbar1             (15)

locally uniformly. The error in(11) is uniformly small over every entire late period, and Theta has zero period average. The exact covariance

    q_t(exp(sA)x)=e^(-nu s)q_(t+s)(x)

passes through(15) for any fixed real s, proving the homogeneity in(2). Average -Delta q_t=partial_i partial_j(f_t)_ij against compactly supported smooth tests and use(6) to obtain the distributional Poisson equation on D.

A539 supplies V in W2,q_loc and C1,alpha_loc, and Z in W1,q_loc, for all finite q>3 and alpha<1. Both are divergence free, since div Z=tr((DV)2)+Delta P2=0. Interior divergence-preserving mollification proves

    partial_i partial_j(M1)_ij=2 sum_(i,j)(partial_j V_i)(partial_i Z_j).

The right side is Lq_loc. Interior Poisson regularity gives pbar1 in W2,q_loc and hence C1,alpha_loc after choosing q large. V.grad P2 and tau have the same C1,alpha regularity. Everything is local away from0, without an origin boundary term or an arbitrary harmonic normalization.

## 7. Weak averaged rank and transport

Let a bar denote a late-period average. Equations(12),(15) give bar h_t->H2 and bar s_t->S1=pbar1-V.Z. Local boundedness and dS_t->dS imply

    bar[h_t dS_t-s_t dk] ->H2 dS-S1 dk

uniformly. Its exact exterior derivative vanishes on any fixed vortical compact set for all late times. Hence dH2 wedge dS+dk wedge dS1=0 there. The Sobolev Lie derivative of leading rank along V is legitimate because V,k,S are in W2,q_loc with bounded first derivatives. It gives

    d(V.grad k) wedge dS+dk wedge d(V.grad S)=0.

Subtract using H2=V.grad k-aS. Since S1-V.grad S=pbar1-2V.grad P2, this proves dk wedge d tau=0.

For transport average the exact divergence-free field

    e^s(S_s w_s-SW)=s_s w_s+S curl z_s.

Here s_s is the scalar correction at time s. Its boundedness and w_s->W give uniform convergence of the first averaged term to S1 W. The second tends weakly in Lq_loc to S curl Z, using uniform W1,q bounds and z_s->Z. Thus W.grad S1=-(curl Z).grad S. Since curl Z=[V,W]=DW V-DV W and W.grad S=0,

    W.grad(V.grad S)=-[V,W].grad S.

Subtract to obtain W.grad tau=0. These are Sobolev identities before continuity makes the final equations pointwise. This proves(2) without a differentiated asymptotic remainder or a raw pressure limit.

## 8. Additional deduction: the periodic pressure term vanishes

Fix theta in[0,T]. Along t_n=nT+theta, equation(11) after(14) gives q_(t_n)->pbar1+Theta(Q_theta^T x) uniformly locally. Equations(12) give s_(t_n)->S1+Theta(Q_theta^T x), while h_(t_n)->H2 and curl z_(t_n) converges weakly to curl Z. Repeat the exact unaveraged primitive and flux limit on this sequence, then subtract the averaged identities from Section7. This yields

    dk wedge d[Theta(Q_theta^T x)]=0 on{W!=0},
    W.grad[Theta(Q_theta^T x)]=0 on D.                       (16)

No derivative of a convergent remainder is taken. Both final equations are pointwise because Theta is smooth, and every fixed phase is allowed.

A harmonic function of ordinary degree -5 is r^-5 times a degree4 spherical harmonic. Decompose Theta into rotation modes. Its zero average removes mode0. Integrating(16) against a complex exponential in theta shows each possibly nonzero mode Phi_m, 1<=|m|<=4, separately satisfies both equations. If one is nonzero, then

    Phi_m=C_m r^-5 (1-z2)^(|m|/2) P4^(|m|)(z) e^(im phi),

where P4^(j) denotes ordinary j-th differentiation and a nonzero normalization is absorbed in C_m. Put sigma=|Phi_m|2. It is smooth, axisymmetric, nonnegative, twisted homogeneous with rate2nu, and nonzero almost everywhere. Equation(16) gives W.grad sigma=0 and dk wedge d sigma=0 on{W!=0}.

Up to nonzero constants, the derivatives of P4 are

    first: z(7z2-3), second: 7z2-1, third: z, fourth: 1.

Every interior root is simple and no derivative vanishes at the poles. Thus sigma has order2 on each interior nodal cone and order2|m| at the axis. The exponent a/(2nu)=1/30 gives inverse behavior |distance|^(-1/15) at a cone and rho^(-|m|/15) transversely to the axis. These exponents are below the codimensions1 and2. Hence sigma^(-1/30) is locally integrable on D, including the poles.

A622 applies to sigma and forces V axisymmetric. A570 gives U0, making m,R,E,M1 and Theta all zero by definition, contrary to a nonzero Phi_m. Thus every nonzero mode vanishes; the zero mode was absent. Consequently Theta=0 and(11) gives the ordinary locally uniform limit

    q_t->pbar1.                                            (17)

This is convergence of the correction selected by the actual profile. The axisymmetric harmonic ambiguity in the homogeneous Poisson problem still exists; the local equation alone does not select its coefficient.

## 9. Consequence and verification scope

Combining(2) with A647-A648 supplies a C1 next scalar of the required degree for every target c and finite omega in the global HF/natural class. A650's one-germ algebra needs only that existence and rank. It therefore excludes the specified LIT158/A617 positive analytic pair as an actual leading pair also at c3/7. No symmetry is assumed outside that band. General interfaces, arbitrary scalar nodes, bare-decay derivative bounds, and both unrestricted regularity classes remain OPEN.

The entire LIT167 source and precise A550/A539/A575 pressure-split ingredients were read. Sections2-7 independently reconstruct LIT167. Section8 was independently deduced here and compared with the complete LIT168 proof, which reaches the same conclusion by extracting two real angular quadratures. Both sources and this complete proof were postread. No computation is needed. Continuing configured-model collaboration uses existing coordinator/theory files, with the primary model configured and no independent provider-runtime attestation.
