# Source and derivative rigidity at the logarithmic Hardy endpoint

## 1. Statement and dependencies

Let U be a real C1 divergence-free field on R3 and suppose E(R)=integral_(|y|<R)|U|^2 satisfies E(R)/(LR^beta)->1 for L>0 and 0<beta<1. Put t=(beta-3)/2, k=(beta+1)/2=t+2, m=2-beta=3-2k, K0=1+k^2/2 and H=t^2(k^2+4)/(k^2+2). For r=|y| and n=y/r define

    F(R)=integral_(1<r<R) r^(-beta)|U|^2,
    T(R)=integral_(1<r<R) r^(-beta)|U-(U.n)n|^2,
    G(R)=integral_(1<r<R) r^(2-beta)|DU|_F^2.

Let q=tr((DU)^2), I and N be the same weighted integrals with |DU|_F^2 replaced by [q]_+ and [-q]_+, and let J(R)=integral_1^R r^(4-beta)[Q(r)]_+dr, Q(r)=integral_S2 q(rn)dn. The sphere measure is 4pi. Assume the additional endpoint condition limsup G(R)/(beta L log R)<=H. Then

    G/(beta L log R)->H, T/F->k^2/(k^2+2),
    J/(beta L log R)->C_s, I/(beta L log R)->C_p,
    N/(beta L log R)->C_n,
    C_s=mt^2/(k^2+2),
    C_n=2kt^2 sqrt(k/(k+3))/(k^2+2), C_p=C_s+C_n.

If D=limsup_(|y|->infinity) r^((5-beta)/2)|DU(y)|_F, allowing infinity, the endpoint also implies

    D>=D_*=sqrt(9 beta L t^2/[4pi(k^2+2)])
      >D_H=sqrt(beta L H/(4pi)).

Under the energy ratio alone, D>D_H still follows. No uniform positive gap above D_H or optimal general value of D is asserted. The endpoint condition transfers between fixed centers. The smooth kinematic control of A3125 attains all endpoint constants, including D_*, but fails the full Euler equation for every c and omega.

This reconstructs source a62a3fde, retained in the team records, all eight sections and its 66 analytical checks read. The dependencies are the already confirmed logarithmic Hardy lower bound and smooth control A3125, and the separate energy theorem A3053 for the final profile consequence. The present argument restates the modal identity it uses; no finite-norm Hardy theorem is applied directly to U.

## 2. Logarithmic coordinates and energy errors

Write z=log r, U(rn)=r^t v(z,n) and A(z,n)=r^(1-t)DU(rn). Then

    F(R)=integral_0^(log R) integral_S2 |v|^2,
    G(R)=integral_0^(log R) integral_S2 |A|^2,
    |A|^2=|v_z+tv|^2+|grad_S v|^2.

The last derivative acts on Cartesian components. Divergence freedom gives (partial_z+k)(v.n)+div_S(v_tan)=0. Zero flux through every sphere excludes a degree-zero radial mode. Direct Stieltjes integration by parts gives

    F(R)=R^(-beta)E(R)-E(1)+beta integral_1^R r^(-beta-1)E(r)dr
        =beta L log R+o(log R).

A fixed-width logarithmic strip has bounded velocity integral, since it is at most r^(-beta)E(e^h r)=O_h(1). No derivative of the energy remainder is used. A3125 and the endpoint limsup give the full limit G/(beta L log R)->H, so G-HF=o(log R).

## 3. The complete modal gap

For a real normalized spherical harmonic Y of degree ell>=1 let lambda=ell(ell+1). A poloidal mode is fY n+g grad_S Y with g=(f'+kf)/lambda; a toroidal mode is h n cross grad_S Y. Their spherical velocity energies are f^2+lambda g^2 and lambda h^2. Their angular derivative energies are

    (lambda+2)f^2-4lambda f g+lambda^2g^2,
    lambda^2h^2,

respectively. These follow from integral|grad Y|^2=lambda and integral|Hess_S Y|^2=lambda(lambda-1), with the moving normal differentiated. Integration by parts makes the cross terms between distinct harmonics and the poloidal and toroidal parts vanish, both for the velocity and the full derivative integral.

Set K=f^2+(f'+kf)^2/lambda. The full poloidal derivative density is

    D_lambda=(f'+tf)^2
       +(f''+(k+t)f'+tkf)^2/lambda
       +(lambda+2)f^2-4f(f'+kf)+(f'+kf)^2.

For compactly supported smooth eta>=0, expansion followed by integration of f'f, f''f' and f''f yields

    integral eta(D_lambda-HK)
      =integral eta[f''^2/lambda+B_lambda f'^2+d_lambda f^2]
       -(k+t)/lambda integral eta' f'^2
       -[2t+((k+t)tk-Hk)/lambda]integral eta' f^2
       +tk/lambda integral eta'' f^2,
    B_lambda=2+(k^2+t^2-H)/lambda,
    d_lambda=(t^2-H)(1+k^2/lambda)+lambda+t^2-2.

Here d_2=0, B_lambda>=1, and for lambda>=6,

    d_lambda>=lambda-3-2/lambda>=4lambda/9.

Indeed H-t^2<2, k^2<1 and t^2>1 imply the first inequality; the second holds at6 and its difference increases thereafter. Each cutoff coefficient is uniformly bounded, and f'^2/lambda<=2lambda g^2+2k^2 f^2/lambda<=C_beta K. Thus the cutoff errors summed over all modes are bounded by C_beta integral(|eta'|+|eta''|)|v|^2.

For a toroidal mode the identity is

    integral eta(D_tor-Hlambda h^2)
      =lambda integral eta[h'^2+(lambda-2+delta)h^2]
       -t lambda integral eta' h^2,
    delta=t^2+2-H=4beta/(k^2+2), 0<delta<2.

Since lambda-2+delta>=(delta/2)lambda, this gap controls both the toroidal velocity and derivative energies. The higher poloidal gap controls both energies as well, because D_lambda<=C_beta(f''^2/lambda+f'^2+lambda f^2). At degree one it controls the squares of the first and second derivatives of the radial coefficients.

For C1 U, each f,g,h is C1 on compact z intervals. The divergence relation makes f C2. Apply the identities first to finite harmonic sums. Parseval convergence in the local angular H1 and radial derivative L2 spaces passes the original energies and bounded cutoff terms to the limit. The nonnegative gap sums pass monotonically. This proves the estimates without an angular truncation hypothesis.

## 4. Approximation by a degree-one matrix

Choose eta_R supported inside 0<z<log R, equal to1 on log2<z<log(R/2), with uniformly bounded first two derivatives. The nonnegative total modal gap is at most G(R)-HF(R)+O(1)=o(log R). Let a(z) be the three real degree-one radial coefficients for Y_i=sqrt(3/(4pi))n_i. For a fixed vector a define

    v0(a,n)=sqrt(3/(4pi))/2 [k a-t(a.n)n],
    M0(a,n)=D_y[|y|^t v0(a,y/|y|)] at y=n,

holding a constant when differentiating. The radial coefficient is a_i and the tangential coefficient is k a_i/2, whereas the actual latter coefficient is (a_i'+ka_i)/2. Hence their velocity difference is controlled by |a'|, and their derivative-matrix difference by |a'|+|a''|. The modal gap proves

    integral_(log2)^(log(R/2)) integral_S2
       (|A-M0(a(z),n)|^2+|v-v0(a(z),n)|^2)=o(log R).

This extends to the whole interval 0<z<log R. The fixed inner strip has finite energy. On the outer strip, G(R)-G(R/2)=o(log R) follows from the full gradient limit, not from an assumed derivative trace estimate. The a-projection and v0,M0 there have O(1) integral by the velocity strip bound. Consequently

    integral_0^(log R) integral_S2 (|A-M0|^2+|v-v0|^2)=o(log R).

Direct integration gives integral_S2|v0|^2=K0|a|^2 and integral_S2|M0|^2=HK0|a|^2. Also integral|a|^2<=F(R)=O(log R). Cauchy-Schwarz applied to the squared-norm differences now yields

    integral_0^(log R)|a(z)|^2 dz=(beta L/K0)log R+o(log R).

There need be no pointwise limit or fixed direction for a(z). The tangential norm of v0 is (k^2/2)|a|^2, giving the claimed limit T/F.

## 5. Both source signs and the spherical positive part

By rotational covariance, take a=|a|e3, mu=n.e3 and sigma=sqrt(1-mu^2). In a suitable orthonormal meridional frame,

    M0=sqrt(3/(4pi))|a|t/2
         [[2mu,-sigma,0],[k sigma,-mu,0],[0,0,-mu]].

Its radial column is the radial derivative of r^t v0; the remaining columns differentiate the moving frame. Squaring gives

    tr(M0^2)=3t^2/(8pi)[(k+3)(a.n)^2-k|a|^2],
    |M0|_F^2=3t^2|a|^2/(16pi)
                 [(1+k^2)+(5-k^2)mu^2].

Put s0=sqrt(k/(k+3)). The source is negative for |mu|<s0. Integrating this quadratic, with dn=2pi dmu, gives

    integral_S2 tr(M0^2)=mt^2|a|^2/2,
    integral_S2[-tr(M0^2)]_+=kt^2s0|a|^2,
    integral_S2[tr(M0^2)]_+=t^2(m+2ks0)|a|^2/2.

For arbitrary real matrices A,M, |tr(A^2)-tr(M^2)|<=|A-M|_F(|A|_F+|M|_F). The matrix approximation and G=O(log R) imply an o(log R) L1 error for the trace. The positive-part map is1-Lipschitz. Thus the same error bound holds for the two pointwise signs, and also for the positive part after spherical integration. In logarithmic variables these three expressions are exactly I,N,J. Applying their separate frozen-matrix integrals and the average of |a|^2 proves C_p,C_n,C_s. In particular no exchange of spherical integration and positive part has occurred.

## 6. The stronger derivative amplitude

Assume D<infinity; otherwise the bound is immediate. For each epsilon>0, |A(z,n)|_F<=D+epsilon for every n and all sufficiently large z. The matrix approximation then gives

    integral_0^Z integral_S2 [|M0(a(z),n)|_F-D-epsilon]_+^2=o(Z).

For any fixed 0<rho<1, the two caps |n.a/|a||>=rho have total measure4pi(1-rho), regardless of the changing direction of a. On these caps |M0|_F>=c_rho|a|, where

    c_rho^2=3t^2[(1+k^2)+(5-k^2)rho^2]/(16pi).

The assertion is trivial when a=0. Therefore integral_0^Z[c_rho|a|-D-epsilon]_+^2=o(Z). Write |a|<=(D+epsilon)/c_rho+[c_rho|a|-D-epsilon]_+/c_rho, square and use Cauchy-Schwarz. This bounds limsup Z^(-1)integral_0^Z|a|^2 by (D+epsilon)^2/c_rho^2. Using its known limit and sending epsilon to0 and rho to1 gives

    D^2>=9t^2/(8pi) * beta L/K0=D_*^2.

Since D_*^2/D_H^2=9/(k^2+4)>1, this strictly exceeds the old averaged lower bound. Finally, if the energy ratio alone held with D<=D_H, the eventual uniform derivative bound would give limsup G/(beta L log R)<=4pi D^2/(beta L)<=H. The endpoint argument would force D>=D_*>D_H, a contradiction. Thus D>D_H without an endpoint hypothesis. This exclusion of equality does not prove a uniform gap for the entire class.

## 7. Fixed centers and an attaining control

For a fixed center b, ball inclusions give E_b(R)/(LR^beta)->1. Under the endpoint, G(R)=O(log R). Outside a fixed ball the two radial weights differ by a relative O_b(1/r). This error is integrable against the positive measure dG, since Stieltjes integration by parts gives integral_(r0)^infinity r^(-1)dG(r)<infinity when G(r)=O(log r). The shifted outer-boundary difference is at most G(R+|b|)-G(R-|b|)=o(log R). The inner-domain difference is finite. Therefore G_b(R)=G(R)+o(log R), and the endpoint transfers to b. Apply the argument there to get all three source limits and the tangential fraction. D itself is unchanged by the asymptotically unit ratio of the radial weights. This is a kinematic translation argument, not an assertion that the profile equation is translation invariant.

For the previously confirmed smooth A3125 control, a(z)=b0 e3 outside radius2 with b0^2=beta L/K0. Its exterior field is b0 r^t[Y n+(k/2)grad_S Y], Y=sqrt(3/(4pi))n3. The compact construction has exactly E(R)=LR^beta for R>=2. Its frozen matrix attains the maximum at mu=+-1, so D=D_*; the three integrals above give all endpoint coefficients. The core is a constant axial field plus a0 Jy, a0!=0, with J(y1,y2,y3)=(-y2,y1,0). Its full momentum residual has curl2a0e3 independently of c and omega. The smooth Poisson pressure certified in A3125 cannot cancel that curl.

## 8. Full-profile scope

For U,P in C1 solving (1-c)U+[((cI-omega J)y+U).grad]U+omega JU+grad P=0, with div U=0, U bounded, U(R.)->0 in distributions and 2/5<c<1/2, A3053 supplies the energy ratio with beta=5-2/c and L>0 unless U=0. Consequently every nonzero such profile has limsup r^(1/c)|DU|_F>sqrt((5-2/c)LH_(5-2/c)/(4pi)). The endpoint condition, if additionally imposed, gives the sharper D_* bound and the three source coefficients. Uniform decay implies the bounded distributional hypotheses. No condition here is proved automatic beyond the energy law, and the main arbitrary-omega conjecture remains open.

This reconstruction uses analytical identities only. The existing configured model coordinator comparison is checked in Section9; actual provider execution is independently unattested. No numerical diagnostic, formal build or new external source was used.


## 9. Independent comparison and exact scope

The complete thirteen-item coordinator comparison, with remarks R1-R3, is retained in the team records. It compares the same source a62a3fde and the earlier eight-section reconstruction f1ef3798. Its analytical assertions agree with Sections2-8. In particular the gap after lambda=6 is justified by the increasing difference 5lambda/9-3-2/lambda, whose derivative is 5/9+2/lambda^2>0. This clarifies the source wording without changing the bound. The coordinator did not read the source checklist or support note; those were read independently here. Its twenty-two symbolic checks and sampled grid have not been rerun or certified by this audit.

The comparison correctly keeps the outer gradient strip o(log R) separate from the velocity strip O(1), and it applies the positive-part Lipschitz estimate both before and after spherical integration. It also keeps the moving cap direction in the derivative-amplitude proof, so no fixed direction for a(z) is needed. These are essential to the C1 and all-angular-mode scope.

The endpoint source and derivative conclusions are confirmed under their stated endpoint condition. The strict inequality D>D_H follows from the energy ratio alone by contradiction, but neither this argument nor the comparison establishes an explicit uniform gap, an optimal general amplitude, or an automatic endpoint condition for Euler. The smooth attaining field is a kinematic control with Poisson pressure, and its nonzero core momentum curl excludes it from the profile class for every real c and omega. The arbitrary-omega Euler conjecture remains open.
