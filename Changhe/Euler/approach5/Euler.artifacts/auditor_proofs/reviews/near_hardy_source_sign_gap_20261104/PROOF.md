# Source stability near the logarithmic Hardy minimum

## 1. Exact statement and scope

Let U be a real C1 divergence-free field on R3 and suppose E(R)=integral_(|y|<R)|U|^2 has E(R)/(L R^beta)->1 for L>0 and0<beta<1. Set

    t=(beta-3)/2, k=(beta+1)/2=t+2, m=2-beta,
    D=k^2+2, K0=D/2, H=t^2(k^2+4)/D.

For r=|y|, sphere measure4pi and q=tr((DU)^2), define

    G(R)=integral_(1<r<R)r^(2-beta)|DU|_F^2,
    I(R)=integral_(1<r<R)r^(2-beta)[q]_+,
    N(R)=integral_(1<r<R)r^(2-beta)[-q]_+,
    Q(r)=integral_S2 q(rn)dn,
    J(R)=integral_1^R r^(4-beta)[Q(r)]_+dr.

Assume limsup G/(beta L log R)<=H+delta with0<=delta<=beta. Put

    C_s=mt^2/D,
    C_n=2kt^2 sqrt(k/(k+3))/D, C_p=C_s+C_n,
    e(delta)=sqrt(10delta/beta)[sqrt(H+delta)+sqrt(H)].

For (V,C) equal to (I,C_p), (N,C_n) or (J,C_s),

    C(1-delta/beta)-e(delta)
       <=liminf V/(beta L log R)
       <=limsup V/(beta L log R)<=C+e(delta).

The lower bound may be replaced by its positive part. In particular delta<=beta/10000 implies liminf N/(beta L log R)>=1/16. Let zeta_beta be the unique root in(0,beta) of

    C_n(1-zeta/beta)
        =sqrt(10zeta/beta)[sqrt(H+zeta)+sqrt(H)].

Then zeta_beta>beta/10000. If liminf N(R)/log R=0, then limsup G/(beta L log R)>=H+zeta_beta. These results hold at every fixed center. Pointwise q>=0 outside a compact set supplies the negative-source hypothesis; Q>=0 alone does not.

This reconstructs the eight sections,48analytical obligations and support note of source bef4f78, retained in `verification`. The argument is kinematic until the final Euler application. No finite angular truncation, symmetry or derivative decay is assumed.

## 2. Full mode identity and C1 localization

Write z=log r, U(rn)=r^t v(z,n), A=r^(1-t)DU(rn), and F(R)=integral_0^(log R)integral_S2|v|^2. Stieltjes integration gives F=beta L log R+o(log R), and every fixed-width logarithmic velocity strip is O(1). The divergence relation is (partial_z+k)(v.n)+div_S v_T=0. Zero flux excludes a degree-zero radial mode.

For a normalized real harmonic Y with lambda=ell(ell+1), ell>=1, the poloidal mode is fY n+g grad_S Y, g=(f'+kf)/lambda, and the toroidal mode is h n cross grad_S Y. Their integrated energies are

    K_pol=f^2+(f'+kf)^2/lambda,
    D_pol=(f'+tf)^2+[f''+(k+t)f'+tkf]^2/lambda
               +(lambda+2)f^2-4f(f'+kf)+(f'+kf)^2,
    K_tor=lambda h^2,
    D_tor=lambda[(h'+th)^2+lambda h^2].

The angular part follows by differentiating the moving normal and using integral|grad Y|^2=lambda and integral|Hess_S Y|^2=lambda(lambda-1). The gradient acts on Cartesian components. All cross terms between different harmonics and between poloidal and toroidal families integrate to zero.

For smooth compactly supported eta>=0, define b_lambda=2+(k^2+t^2-H)/lambda, d_lambda=(t^2-H)(1+k^2/lambda)+lambda+t^2-2 and gamma=t^2+2-H=4beta/D. Expansion and integration by parts give

    integral eta(D_pol-HK_pol)
      =integral eta[f''^2/lambda+b_lambda f'^2+d_lambda f^2]
       -(k+t)/lambda integral eta'f'^2
       -[2t+((k+t)tk-Hk)/lambda]integral eta'f^2
       +tk/lambda integral eta''f^2,
    integral eta(D_tor-HK_tor)
      =lambda integral eta[h'^2+(lambda-2+gamma)h^2]
       -t lambda integral eta'h^2.

One has b_lambda>=1, d_2=0, d_lambda>=4lambda/9 for lambda>=6, and0<gamma<2 with gamma>=4beta/3. The higher-degree bound follows from d_lambda>=lambda-3-2/lambda and the increasing difference5lambda/9-3-2/lambda, zero at6. Let Q_eta be the sum of these nonnegative main integrals. Then

    |Q_eta-(G_eta-HF_eta)|
       <=C_beta integral(|eta'|+|eta''|)|v|^2.

The derivative cutoff term is controlled by f'^2/lambda<=2lambda g^2+2k^2f^2/lambda. For C1 U the coefficients are C1, and divergence makes f C2. Prove the identities on finite harmonic sums and pass by local H1 and radial derivative L2 convergence, with nonnegative main sums and uniform cutoff errors. This establishes the full-field inequality. Interior cutoffs also give liminf G/(beta L log R)>=H.

## 3. Quantitative matrix and low-energy control

For Y_i=sqrt(3/(4pi))n_i let a(z) be the degree-one radial coefficient vector. Define

    v0(a,n)=sqrt(3/(4pi))/2[k a-t(a.n)n],
    M0(a,n)=D_y[|y|^t v0(a,y/|y|)] at y=n,

holding a fixed while differentiating. Their squared sphere norms are K0|a|^2 and H K0|a|^2.

For a low coefficient f the exact squared matrix error is2f'^2+[f''+(k+t)f']^2/2. The first radial component contributes f'^2, the tangential radial component contributes the displayed half-square, and the angular derivative of f'grad_S Y/2 contributes f'^2. Since |k+t|<1, this is at most3[f''^2/2+b_2 f'^2].

For lambda>=6 let q_pol=f''^2/lambda+b_lambda f'^2+d_lambda f^2. Then K_pol<=q_pol and D_pol<=10q_pol. Indeed K_pol<=(4/3)f^2+(1/3)f'^2, and the exact simplification

    D_pol=2(f'+tf)^2+[f''+(k+t)f'+tkf]^2/lambda
                                 +(lambda-2)f^2

bounds D_pol by3f''^2/lambda+7f'^2+(lambda+16)f^2. Use lambda+16<=40lambda/9. For q_tor=lambda[h'^2+(lambda-2+gamma)h^2], one has K_tor<=3q_tor/(4beta) and D_tor<=5q_tor/beta. The derivative bound follows from D_tor<=2lambda h'^2+lambda(lambda+2t^2)h^2: at lambda=2 compare2+2t^2<13/2<20/3<=5gamma/beta, then compare the positive slopes for lambda>=2.

Orthogonality of the matrix families gives

    integral eta integral_S2|A-M0|^2<=(10/beta)Q_eta.

The exact low velocity identity is

    integral eta K_low=K0 integral eta|a|^2
       +(1/2)integral eta|a'|^2-(k/2)integral eta'|a|^2.

The final term is O(1) for fixed-width cutoff transitions. Distinct families contribute distinct nonnegative summands of Q_eta, so taking the largest coefficient, at most1/beta, gives

    F_eta-Q_eta/beta-C<=K0 integral eta|a|^2<=F_eta+C.

## 4. The frozen source and its two signs

Rotate coordinates so a=|a|e3, put mu=n.e3 and sigma=sqrt(1-mu^2). The frozen matrix in a meridional orthonormal frame is

    M0=sqrt(3/(4pi))|a|t/2
            [[2mu,-sigma,0],[k sigma,-mu,0],[0,0,-mu]].

Consequently tr(M0^2)=3t^2[(k+3)(a.n)^2-k|a|^2]/(8pi). It is negative when |mu|<s0=sqrt(k/(k+3)). Integrating with dn=2pi dmu gives

    integral_S2 tr(M0^2)=mt^2|a|^2/2=C_sK0|a|^2,
    integral_S2[-tr(M0^2)]_+=kt^2s0|a|^2=C_nK0|a|^2,
    integral_S2[tr(M0^2)]_+=C_pK0|a|^2.

The signed integral is positive, so its own positive part equals C_sK0|a|^2. These identities include a=0 and require no fixed direction for a(z).

For any real matrices A,M,

    |tr(A^2)-tr(M^2)|<=|A-M|_F(|A|_F+|M|_F).

The scalar positive-part maps are1-Lipschitz. The positive part after sphere integration is also1-Lipschitz with respect to the sphere L1 difference. Thus this single trace error controls I,N and J separately. No interchange of the positive part and angular integration is made.

## 5. Two cutoffs give both sides without a gradient-strip assumption

Let Z=log R. A lower cutoff eta^- is supported in(0,Z), equals1 on(log2,Z-log2), and lies in[0,1]. An upper cutoff eta^+ is supported in(0,Z+log2), equals1 on(log2,Z), and also lies in[0,1]. Both have uniformly bounded first two derivatives. For either family the velocity error is O(1), hence

    F_eta/(beta L Z)->1,
    limsup Q_eta/(beta L Z)<=delta,
    1-delta/beta<=liminf K0 integral eta|a|^2/(beta L Z)
       <=limsup K0 integral eta|a|^2/(beta L Z)<=1.

In the upper estimate use G_eta<=G(2R) and log(2R)/log R->1. No derivative trace or bounded gradient strip is assumed. The normalized squared norms of A, M0 and A-M0 have limit superior at most H+delta, H and10delta/beta. Weighted Cauchy-Schwarz therefore gives

    limsup integral eta integral_S2 |tr(A^2)-tr(M0^2)|
                     /(beta L Z)<=e(delta).

For any V from Section1, its lower localized moment is at most V(R), because V has nonnegative density. Its upper localized moment is at least V(R) minus the fixed contribution from1<r<2. This contribution is finite for C1 U. Substitute the three frozen integrals from Section4 and the energy bounds above. This proves all the lower and upper limits in Section1, including delta=0.

## 6. Uniform negative-source mass and the exact root

Since1/2<k<1, kt^2=k(2-k)^2>=1: the difference from1 factors as(k-1)(k^2-3k+1), with both factors nonpositive. Also D<3 and k/(k+3)>1/7. Hence C_n>2/(3sqrt(7))>1/4. Moreover H<17/4. For delta<=beta/10000,

    e(delta)<5/sqrt(1000)<1/6.

Thus the negative-source lower coefficient is strictly greater than

    (1/4)(1-1/10000)-1/6=9997/120000>1/16.

This yields the stated nonstrict1/16 lower bound with room to spare.

The function C_n(1-zeta/beta)-e(zeta) is continuous and strictly decreasing on[0,beta], positive at0 and negative at beta. It has one root zeta_beta. The last estimate makes its value positive at beta/10000, so zeta_beta>beta/10000. Write M=limsup G/(beta L log R). If M is infinite or at least H+beta, the asserted gap follows immediately. Otherwise M>=H and the stability inequality applies with delta=M-H. If liminf N/log R=0, its lower coefficient cannot be positive. Hence delta>=zeta_beta. Eventual pointwise q>=0, or finite N(infinity), implies this vanishing liminf. Nonnegative spherical Q does not control the pointwise negative part and supplies no such inference.

## 7. Centers and conditional pointwise amplitude

Ball inclusions preserve the energy ratio at any fixed center a. For every epsilon>0 and sufficiently large |y|, the weights |y-a|^(2-beta) and |y|^(2-beta) differ by factors within1+-epsilon. Domain inclusions then give G_a(R)<=(1+epsilon)G_0(R+|a|)+C, and the reverse comparison. Taking normalized limsups and then epsilon to zero proves invariance of that limsup. Reapply the argument about each center. This is a translation statement about the functionals, not about the Euler equation.

If D_inf=limsup r^((5-beta)/2)|DU|_F is finite, then G(R)<=4pi(D_inf+epsilon)^2 log R+C_epsilon. Thus the vanishing negative-source liminf implies

    D_inf^2>=beta L(H+zeta_beta)/(4pi).

The same bound is immediate if D_inf is infinite. This amplitude bound retains its negative-source hypothesis.

## 8. Full-profile application and review status

For U,P in C1 satisfying div U=0 and the complete rotating profile equation

    (1-c)U+[((cI-omega J_rot)y+U).grad]U
                       +omega J_rot U+grad P=0,
    J_rot(y1,y2,y3)=(-y2,y1,0),

assume U is bounded, U(R.) tends to zero distributionally on compact sets, and2/5<c<1/2. A3053 supplies the energy ratio with beta=5-2/c and L>0 for a nonzero profile. All conclusions then hold for every finite omega, with their additional gradient or negative-source hypotheses unchanged. Uniform velocity decay supplies the bounded distributional assumptions, not those extra hypotheses. The scalar moment J(R) is distinct from J_rot.

The upper cutoff is essential for the upper stability bound. The pointwise source sign is distinct from its spherical mean. No optimal stability constant, automatic source sign, automatic finite gradient bound or unrestricted Euler nonexistence is claimed. The proof rederives its quantitative mode estimates and uses no unconfirmed LIT382-LIT385 theorem. All source sections and48obligations are read. The existing configured model C comparison of10:17:17Z has now been read in full and compared as described below; actual provider execution is independently unattested. No mathematical computation, root evaluation, formal build or fresh retrieval was used.

## 9. Existing C comparison, center invariance and evidence boundary

The complete eight-point C comparison of10:17:17Z is retained as in the team records. Its analytical arguments agree with Sections1-8. In particular, the identity for d_lambda as (1+k^2/lambda)(M_lambda-H) gives another check of nonnegativity. Orthogonality follows from the rotation-invariant integrated quadratic forms: distinct irreducible harmonic degrees are orthogonal, each fixed-degree form is scalar on its real harmonic representation, and opposite parities separate poloidal and toroidal families. The Cartesian derivative reverses both parities, so their distinction persists for matrices. This argument concerns integrated inner products, not pointwise orthogonality.

The quantitative bounds in Section3 and the upper cutoff in Section5 were checked analytically; the C comparison's diagnostic values and claimed29checks are not used as evidence. Its suggested improvements to the constants are not included in the theorem. The comparison's remark about the previously unsubmitted high-degree fraction belongs to the separate LIT388 audit.

The center argument in Section7 yields a useful general refinement. For any C1 field with E(R)/(LR^beta)->1, the extended-real number limsup G_a(R)/(beta L log R) is independent of the fixed center a. Indeed, outside a sufficiently large ball the two weights have ratio in[1-epsilon,1+epsilon], while the fixed omitted regions have finite gradient integral. Ball inclusions give each upper inequality with R shifted by the fixed distance between centers. Since log(R+d)/log R tends to1, take limsups and then epsilon to0 in both directions. The argument includes infinity. Thus the fixed-center finite gradient premise in the earlier LIT379,381and383 bounds automatically transfers to every fixed center with the same M and L. The Euler equation itself is not being translated.

The negative-source condition is retained for the root and amplitude consequences. Eventual pointwise q>=0 and a finite negative moment are sufficient conditions, whereas nonnegative spherical mean is not. The full Euler application remains conditional and covers every finite rotation parameter. Neither the source nor this comparison establishes optimal stability constants, an automatic finite gradient budget, an automatic negative-source condition, or the unrestricted nonexistence conjecture.
