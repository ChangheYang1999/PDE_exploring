# Exact joint spectral region and higher-degree energy fraction

## 1. Statement, notation and dependencies

Let U be C1 on R3, divergence-free, with E(R)=integral_(|y|<R)|U|^2 satisfying E(R)/(L R^beta)->1, where L>0 and0<beta<1. Put t=(beta-3)/2, k=t+2=(beta+1)/2, m=2-beta, and lambda_ell=ell(ell+1) for ell>=1. Define K_ell=1+k^2/lambda_ell, x_ell=k^2/(lambda_ell+k^2), M_ell=t^2+lambda_ell(lambda_ell+t^2-2)/(lambda_ell+k^2), C_ell=t^2+lambda_ell, and H=M_1.

All sphere integrals use area4pi and Cartesian derivatives. About any fixed center a let F_a,T_a,G_a integrate, respectively, r_a^(-beta)|U|^2, r_a^(-beta)|U_tan,a|^2 and r_a^(2-beta)|DU|_F^2 over1<r_a=|y-a|<R. With q=tr((DU)^2), let Q_a(r)=integral_S2 q(a+rn) and J_a(R)=integral_1^R r^(4-beta)[Q_a(r)]_+dr. Let d(M) interpolate the points(M_ell,x_ell) affinely, and u(M)=min(1,x_1+(M-H)/(2beta)).

The dependencies A3152-A3153, proved in the team records, show that limsupG_a/(beta L log R)<=M<infinity implies M>=H and

    d(M)<=liminf T_a/(beta L log R)
          <=limsup T_a/(beta L log R)<=u(M).             (1)

We prove that every pair M>=H, tau in[d(M),u(M)] is realized by a smooth solenoidal uniformly decaying field with E_0(R)=L R^beta for R>=2, E_a(R)=LR^beta+O_a(R^(beta-1)), and

    T_a=beta L tau log R+O_a(1),
    G_a=beta L M log R+O_a(1),
    J_a=beta L m(1-beta+beta tau)log R+O_a(1).           (2)

Every exterior derivative of order h is O(r^(t-h)). The field admits a smooth Poisson pressure but solves full rotating Euler momentum for no realc,omega. In particular the gradient coefficient in(2) is exactly M, not just bounded by M.

Let Pi_(>=ell0) be the L2 sphere projection onto radial, poloidal and toroidal vector harmonics of degrees ell>=ell0, and let F_(>=ell0),a be its velocity energy with the same radial weight as F_a. For every ell0>=2 we also prove

    limsup F_(>=ell0),a/(beta L log R)
      <=min(1,(M-H)/(M_ell0-H)),                        (3)

under the same-center gradient premise. Each right side is attained by another field satisfying the same smooth completion, pressure and non-Euler conclusions, at exact gradient coefficient M. Source LIT388 has SHA256 a475107b07f24e45d1de7e7a3337f6aceaa849df777957f9c1c08962fe93803b.

## 2. Full-mode identities with uniform errors

Translate the chosen center to0 for the kinematic proof, and write z=log r, U(rn)=r^t v(z,n). The weights give F=integral|v|^2dz dn and G=integral[|v_z+tv|^2+|grad_S v|^2]dz dn. Divergence is (partial_z+k)(v.n)+div_S v_T=0. The degree-zero radial coefficient vanishes: its sphere flux is zero by the divergence theorem on every ball, since U is C1 on allR3.

For a normalized real spherical harmonic Y of eigenvalue lambda, a poloidal mode is fY n+g grad_S Y with g=(f'+kf)/lambda. A toroidal mode is h n cross grad_S Y. The velocity and gradient densities are

    K_pol=f^2+(f'+kf)^2/lambda,
    D_pol=2(f'+tf)^2+[f''+(k+t)f'+tkf]^2/lambda
                               +(lambda-2)f^2,
    K_tor=lambda h^2,
    D_tor=lambda[(h'+th)^2+lambda h^2].                (4)

The poloidal simplification uses t-k=-2. It is equivalent to the radial-derivative square plus(lambda+2)f^2-4f(f'+kf)+(f'+kf)^2 in the source. These identities follow from integral|grad Y|^2=lambda and integral|Hess_S Y|^2=lambda(lambda-1), using integration by parts on the unit sphere. Distinct orthonormal harmonics, and the poloidal and toroidal families, are orthogonal for both integrated densities. This is spherical orthogonality, not pointwise matrix orthogonality.

For smooth eta>=0 of compact support in z, expanding(4) and integrating cross derivatives gives

    integral eta(D_pol-M_lambda K_pol)
      =integral eta[f''^2/lambda+b_lambda f'^2]
       -(k+t)/lambda integral eta'f'^2
       -[2t+((k+t)tk-M_lambda k)/lambda]integral eta'f^2
       +tk/lambda integral eta''f^2,                  (5)

where b_lambda=2+(k^2+t^2-M_lambda)/lambda
=1+k^2/lambda+2beta/(lambda+k^2)>1. The zero-order term is zero because(t^2-M_lambda)(1+k^2/lambda)+lambda+t^2-2=0. For toroidal modes the identity is

    integral eta(D_tor-M_lambda K_tor)
      =lambda integral eta[h'^2+(t^2+lambda-M_lambda)h^2]
       -t lambda integral eta'h^2.                   (6)

Here t^2+lambda-M_lambda=2beta lambda/(lambda+k^2)>0. All main terms are nonnegative. All error coefficients are uniformly bounded after measuring f'^2/lambda, f^2 and lambda h^2. Indeed M_lambda/lambda<=1+t^2/2 and

    f'^2/lambda<=2lambda g^2+2k^2f^2/lambda<=C_beta K_pol.

Thus the sum of all errors is at most C_beta integral(|eta'|+|eta''|)|v|^2. C1 regularity gives C1 coefficients f,g,h and divergence gives f in C2. Apply the identities first to finite sums. Local angular H1 and radial L2 Parseval convergence control their left sides; nonnegative main terms pass by monotone convergence. This proves

    G_eta>=sum_ell M_ell F_(ell,eta)
                       -C_beta integral(|eta'|+|eta''|)|v|^2. (7)

The weighted sum itself is bounded by the finite left side plus the uniform error, so no unproved summability of angular weights is inserted.

## 3. Higher-degree bound and the boundary strips

Stieltjes integration gives F(R)=beta L log R+o(log R). The energy ratio also gives a uniform O(1) bound for velocity energy on every fixed-width far logarithmic strip. Choose eta between0and1, supported in(0,log R), equal to1 on(log2,log(R/2)), with two uniformly bounded derivatives. Then the error in(7) is O(1).

Since M_lambda=t^2+lambda-2beta lambda/(lambda+k^2), its derivative is1-2beta k^2/(lambda+k^2)^2>0 for lambda>=2. Consequently, before removing any strips,

    sum M_ell F_(ell,eta)
       >=H F_eta+(M_ell0-H)F_(>=ell0),eta.

Only the two unweighted velocity energies on this last line are now compared with their uncut counterparts. Projection is an L2 contraction, so each omitted strip has O(1) energy. As G>=G_eta,

    G(R)>=H F(R)+(M_ell0-H)F_(>=ell0)(R)-C.           (8)

This proves(3) on dividing by beta L log R and using0<=F_(>=ell0)<=F. In particular no weighted angular boundary-strip estimate is needed for the source proof. The denominator is positive. More quantitatively,1/2<=dM_lambda/dlambda<=1 gives

    (lambda_ell0-2)/2<=M_ell0-H<=lambda_ell0-2,

so it grows quadratically in ell0. The constants in the O(1) term of(8) may depend on ell0; ell0 is fixed before R tends to infinity. No uniform simultaneous limit ell0=ell0(R) is asserted.

There is also a direct way to check the stronger raw weighted comparison suggested in C's original remark. Formula(4) gives the exact pointwise radial identity

    D_pol-lambda K_pol
      =[f'+(2t-k)f]^2-10f^2
                  +[f''+(k+t)f'+tkf]^2/lambda.        (9)

Since lambda-M_lambda>=-t^2 and t^2<9/4, (9) implies D_pol-M_lambda K_pol>=-(49/4)K_pol. For toroidal modes D_tor>=lambda K_tor gives the same bound. Sum and integrate(7), then apply this bound on the omitted strips. This proves G>=sum M_ell F_ell-C, with no assumption on the weighted angular energies of those strips. For finite sums the assertion is immediate; the same inequality bounds the increasing weighted sum by G+(49/4)F on each finite interval, so the full sum is legitimate. This stronger comparison is not needed for(8).

## 4. Exact joint realization at infinity

Choose real zonal harmonics Y_ell of sphere norm1 about e3. Define p_ell=[Y_ell n+(k/lambda_ell)grad_S Y_ell]/sqrt(K_ell) and w_ell=(n cross grad_S Y_ell)/sqrt(lambda_ell). Their triples(velocity,tangential,gradient) are(1,x_ell,M_ell) and(1,1,C_ell). This follows from(4) with constant coefficients. Sphere orthogonality separates all distinct atoms. Zonal poloidal and toroidal velocities are also pointwise perpendicular.

For fixed M the lower pair(M,d(M)) is the convex mixture of the adjacent poloidal atoms bracketing M. For H<=M<=C_1 the upper pair is the mixture of p_1,w_1 with poloidal energy weight(C_1-M)/(C_1-H). The identity C_1-H=4beta/(k^2+2)=2beta(1-x_1) gives exactly u(M). For M>=C_1 choose adjacent toroidal costs C_j<=M<=C_(j+1) and interpolate their weights; both tangential coefficients are1, so this has exact costM and shareu(M)=1.

For M>H the lower share is strictly below the upper share: d decreases from x_1 while u increases until reaching1. Given tau in between, put theta=(tau-d(M))/(u(M)-d(M)) and mix the two atom-weight lists with weights1-theta andtheta. The resulting energy weights are nonnegative, sum to1, have costM and sharetau. Combine repeated identical atoms by adding their energy weights before taking square roots. There are at most four distinct atoms. At M=H the single p_1 handles the degenerate interval.

The tail is sqrt(beta L)r^t times the sum of each atom multiplied by the square root of its energy weight. It has sphere velocity norm squared beta L r^(2t), tangential norm squared beta L tau r^(2t), and derivative norm squared beta L M r^(2t-2). All desired homogeneous coefficients are therefore exact.

## 5. Exact higher-degree attainments

For H<=M<=M_ell0, mix p_1 and p_ell0 with high-degree energy weight(M-H)/(M_ell0-H). This has exact costM and the desired fraction. For M>=M_ell0 choose adjacent poloidal costs M_j<=M<=M_(j+1) with j>=ell0 and interpolate. All its energy is then in degrees at leastell0 and its cost is exactlyM. Endpoint weights may be zero. These tails use the same completion as the joint construction.

## 6. Smooth completion, energy fill and all-omega momentum obstruction

For a poloidal atom with tail coefficient c_ell=sqrt(beta L a_ell/K_ell), use

    V_ell=f_ell Y_ell n+(rf_ell'+2f_ell)grad_S Y_ell/lambda_ell.

Take f_ell=c_ell r^t for r>=2 and f_ell=c_ell2^(t-ell+1)r^(ell-1) for r<=2-epsilon. Interpolate smoothly. The endpoint functions agree at2 and differ by O(epsilon) in the transition, so f and f' remain bounded and the transition velocity energy tends to0. Inside it is(c_ell2^(t-ell+1)/ell)grad(r^ell Y_ell), hence smooth and irrotational. Since its sphere norm factor is(2ell+1)/ell, radial integration gives limiting energy inB2 equal to2^beta c_ell^2/ell=L2^beta a_ell beta/(ell K_ell), strictly smaller thanL2^beta a_ell.

Cut each toroidal atom smoothly to0 for r<=2-epsilon. Its divergence remains zero because it is tangential with zero spherical divergence. Its bounded transition velocity has vanishing energy as epsilon tends to0. Derivatives need not be uniform in epsilon; fix one positive epsilon<1. Distinct degrees remain orthogonal with arbitrary radial coefficients, and zonal poloidal/toroidal velocities stay perpendicular. The finite collection therefore leaves a strictly positive total deficit Delta fromL2^beta.

Choose a smooth nonnegative radial psi supported inB_(1/2), equal to1 near0. Let W=psi Jy, J(y)=e3 cross y. Every toroidal completion vanishes onB1, while every zonal poloidal velocity is perpendicular toW. Thus the added energy of a0W is exactlya0^2 integral|W|^2, with zero cross term. Taking a0=sqrt(Delta/integral|W|^2)>0 gives E(2)=L2^beta. Exterior shell energy beta L r^(beta-1) then gives E_0(R)=LR^beta for R>=2. Smoothness and derivative decay follow.

Near0, U=grad Phi+a0Jy with Phi a finite sum of solid harmonics; hence Omega=curl U=2a0e3 is constant on a whole neighborhood, even if a degree-one potential supplies nonzero U(0). Only the degree-two potential contributes to the symmetric part of DU(0). Choose its harmonic sign so S=diag(s,s,-2s), s>=0, and put S=0 if absent. For the full nonpressure residual F_c,omega, direct curl gives

    curl F_c,omega=Omega+B.grad Omega-(Omega.grad)U+omega JOmega.

Here B=(cI-omega J)y+U. At0 the transport and J terms vanish, so curl F_c,omega(0)=2a0(e3-DU(0)e3)=2a0(1+2s)e3, nonzero for every realc,omega. No C1 pressure can remove it, since a distributional gradient has zero curl. Higher-degree potentials do not alter this calculation because their vorticity is identically zero, not merely zero at the origin.

## 7. Source, pressure and centers

Let K,T0 be the homogeneous tail's sphere velocity and tangential energies after removing r^(2t). Testing q=partial_i partial_j(U_iU_j) against a compactly supported radial function psi in the exterior gives

    integral r^2 Q(r)psi(r)dr
       =(K-T0)integral r^(beta-1)psi''dr
                          +T0 integral r^(beta-2)psi'dr.

Two integrations by parts in the first term and one in the second show Q(r)=m[(1-beta)K+beta T0]r^(beta-5). For the constructed tail K=beta L,T0=beta L tau; the coefficient is strictly positive. Therefore J has precisely the coefficient in(2). This does not establish pointwise q>=0.

The smooth completion has q=O(r^(beta-5)). Its Newton potential integral q(x)/(4pi|y-x|)dx converges absolutely, since the remote radial integral is O(integral r^(beta-4)dr), and the local kernel is integrable against smooth q. It solves -Delta P=q distributionally and is smooth by local elliptic regularity. This remains a Poisson solution only.

For fixed a, the inclusions B_(R-|a|)(0) subset B_R(a) subset B_(R+|a|)(0) and the exact origin energy give E_a(R)=LR^beta+O_a(R^(beta-1)). Taylor estimates for the homogeneous tail give U(a+rn)-U(rn)=O_a(r^(t-1)) and DU(a+rn)-DU(rn)=O_a(r^(t-2)). Their squared-norm differences with the respective critical weights have radial size O_a(r^-2), hence integrate to O_a(1). This applies to tangential projections, gradient norms and source terms. Positive part is1-Lipschitz before or after spherical integration. The higher-degree projection is an L2 contraction, so its squared-norm difference has the same estimate. All coefficients persist at every fixed center without requiring inversion parity.

## 8. Euler application and audit status

By A3053, a nonzero full profile with U,P inC1, bounded U, U(R.)->0 distributionally, and2/5<c<1/2 has the energy ratio used here with beta=5-2/c and L>0. Under the additional finite-gradient premise at a specified center it therefore obeys(1)and(3) for every realomega, with no symmetry assumption. There is no automatic finite M, radiuswise modal vanishing, finite-mode reduction of Euler, or optimal pointwise-positive-source claim. The finite tails demonstrate exact kinematic attainments and explicitly fail momentum.

The eight source sections, fifty manual obligations and formal-source note were read in full. All new algebra, cutoff passages, completions and scope claims are reconstructed above. The additional raw weighted comparison(9) and the quadratic denominator estimate were derived independently. The existing C comparison of 10:31:54Z has now been read completely and reconciled in Section 9. No mathematical computation or formal build was used. The main arbitrary-omega conjecture remains OPEN.

## 9. Independent comparison and the pointwise constant

The full eight-point C comparison of 10:31:54Z is retained as in the team records. Its analytical conclusions agree with Sections 1-8. The zero-order cancellation in (5), uniform cutoff errors, order of removing the strips, exact atom-weight mixing, core deficit and curl, and translation estimates have each been checked against the formulas above. None of the reported symbolic tests, grids, decimal values or sampled mixtures is used as proof.

C adds that 49/4 is the best constant uniform in beta and lambda for the pointwise radial inequality used after (9). This narrower algebraic optimality statement is also valid. Set f=1, f'=k-2t and f''=-(k+t)f'-tk at a chosen radius. Both squares on the right of (9) vanish, and K_pol=1+16/lambda because k-t=2. Hence

    (D_pol-M_lambda K_pol)/K_pol
      =-10/(1+16/lambda)-t^2+2beta lambda/(lambda+k^2).

For fixed beta and lambda=ell(ell+1) tending to infinity this tends to -10-t^2+2beta. Letting beta decrease to zero gives -49/4. Thus a smaller constant cannot hold for every admissible beta, degree and radial jet. The bound already proved supplies the reverse inequality. This proves optimality only of that uniform pointwise algebraic constant; it does not identify an optimal global cutoff constant or a full-profile extremum.

The exact high-degree fraction is attained for each fixed cutoff ell0 and finite M. Its sharpness is not a claim that high modes vanish at individual radii or that a cutoff may grow with R without an additional argument. C's separate SECTION6 text and its numerical outputs are not collectively certified by this reconciliation.
