# A quantitative gap above the averaged Hardy derivative amplitude

## 1. Statement and evidence

Let U be a real C1 divergence-free field on R3, and suppose E(R)=integral_(|y|<R)|U|^2 satisfies E(R)/(L R^beta)->1, where L>0 and0<beta<1. Set

    t=(beta-3)/2, k=t+2=(beta+1)/2, K0=(k^2+2)/2,
    H=t^2(k^2+4)/(k^2+2),
    D_inf=limsup_(|y|->infinity)|y|^((5-beta)/2)|DU(y)|_F.

The limsup is over all spatial points and may be infinite. Define s=1-1/sqrt(2) and B^2=3t^2(7+k^2)/[4(k^2+2)]. There is exactly one epsilon_beta in(0,beta) with

    B sqrt(1-epsilon_beta/beta)
        =sqrt(H+epsilon_beta)+sqrt(10epsilon_beta/(beta s)).

Then epsilon_beta>beta/10000 and

    D_inf^2>=beta L(H+epsilon_beta)/(4pi)
             >beta L(H+beta/10000)/(4pi).

These statements hold about every fixed center with the same L and D_inf. No symmetry, pressure, momentum equation, pointwise velocity decay or homogeneous expansion is assumed. This reconstructs all eight sections, forty analytical obligations and the support note of source fce67f51, retained in `verification`. The proof below restates the needed mode identity. The only external result used for the final Euler consequence is the confirmed energy theorem A3053.

## 2. Logarithmic variables and exact mode energies

Put r=|y|, n=y/r, z=log r, U(rn)=r^t v(z,n), and A=r^(1-t)DU(rn). Sphere measure is4pi. With Z=log R,

    F(R)=integral_0^Z integral_S2 |v|^2
         =integral_(1<r<R)r^(-beta)|U|^2,
    G(R)=integral_0^Z integral_S2 |A|_F^2
         =integral_(1<r<R)r^(2-beta)|DU|_F^2,
    |A|^2=|v_z+tv|^2+|grad_S v|^2.

The last derivative acts on Cartesian components. Divergence gives (partial_z+k)(v.n)+div_S v_T=0. The degree-zero radial mode vanishes by zero flux through every sphere. Stieltjes integration gives

    F(R)=R^(-beta)E(R)-E(1)+beta integral_1^R r^(-beta-1)E(r)dr
         =beta L log R+o(log R).

A logarithmic strip of width a has velocity energy bounded by r^(-beta)E(e^a r)=O_a(1). No energy remainder is differentiated.

For a real normalized harmonic Y of degree ell>=1, write lambda=ell(ell+1). The poloidal mode fY n+g grad_S Y has g=(f'+kf)/lambda; a toroidal mode is h n cross grad_S Y. Their sphere energies are

    K_pol=f^2+(f'+kf)^2/lambda,
    D_pol=(f'+tf)^2+[f''+(k+t)f'+tkf]^2/lambda
                +(lambda+2)f^2-4f(f'+kf)+(f'+kf)^2,
    K_tor=lambda h^2,
    D_tor=lambda[(h'+th)^2+lambda h^2].

Differentiating n, integrating |grad Y|^2=lambda and |Hess_S Y|^2=lambda(lambda-1), gives the angular terms. Spherical integration by parts makes distinct harmonic families, and poloidal versus toroidal families, orthogonal for both full energies. No pointwise orthogonality is asserted.

## 3. The nonnegative localized gap

For smooth compactly supported eta>=0 put

    b_lambda=2+(k^2+t^2-H)/lambda,
    d_lambda=(t^2-H)(1+k^2/lambda)+lambda+t^2-2,
    gamma=t^2+2-H=4beta/(k^2+2).

Expansion and integration of the mixed derivatives give

    integral eta(D_pol-H K_pol)
      =integral eta[f''^2/lambda+b_lambda f'^2+d_lambda f^2]
       -(k+t)/lambda integral eta'f'^2
       -[2t+((k+t)tk-Hk)/lambda]integral eta'f^2
       +tk/lambda integral eta''f^2,
    integral eta(D_tor-H K_tor)
      =lambda integral eta[h'^2+(lambda-2+gamma)h^2]
       -t lambda integral eta'h^2.

Here d_2=0, b_lambda>=1, and d_lambda>=lambda-3-2/lambda>=4lambda/9 for lambda>=6. Indeed H-t^2<2, k^2<1 and t^2>1 give the first bound, and the last difference is zero at6 and has derivative5/9+2/lambda^2>0. Also0<gamma<2 and gamma>=4beta/3.

Let Q_eta be the sum of the displayed nonnegative main integrals. The total error is bounded by C_beta integral(|eta'|+|eta''|)|v|^2. For the only derivative error, f'^2/lambda<=2lambda g^2+2k^2f^2/lambda<=C_beta K_pol. C1 U gives C1 coefficients and the divergence relation upgrades f to C2. Finite harmonic sums converge in local angular H1 and radial derivative L2; the nonnegative main terms pass monotonically. Thus the identity and error bound hold for the whole C1 field, with no angular cutoff assumption.

Choose eta_R supported inside(0,Z), equal to1 on(log2,Z-log2), with first two derivatives uniformly bounded. Velocity strip bounds give

    0<=Q_R<=G(R)-H F(R)+C.

In particular liminf G/(beta L log R)>=H.

## 4. Explicit matrix and missing-energy constants

Let a(z) be the degree-one radial coefficients for Y_i=sqrt(3/(4pi))n_i. Freeze a when defining

    v0(a,n)=sqrt(3/(4pi))/2 [k a-t(a.n)n],
    M0(a,n)=D_y[|y|^t v0(a,y/|y|)] at y=n.

Their sphere norms are K0|a|^2 and H K0|a|^2. For a single low coefficient f the exact squared matrix error is

    2f'^2+[f''+(k+t)f']^2/2
        <=3f'^2+f''^2<=3[f''^2/2+b_2 f'^2].

The radial column is f'Y n+[f''+(k+t)f']grad_S Y/2. Its normal and tangent parts are orthogonal. The remaining angular derivative of f'grad_S Y/2 has squared sphere norm f'^2. This verifies the entire error formula.

For lambda>=6 let q_pol=f''^2/lambda+b_lambda f'^2+d_lambda f^2. Then K_pol<=(4/3)f^2+(1/3)f'^2<=q_pol. A useful exact simplification is

    D_pol=2(f'+tf)^2+[f''+(k+t)f'+tkf]^2/lambda
                       +(lambda-2)f^2.

Using |t|<3/2, k<1 and |k+t|<1, this is at most

    3f''^2/lambda+(4+3/lambda)f'^2
                 +(lambda-2+4t^2+3t^2k^2/lambda)f^2
     <=3f''^2/lambda+7f'^2+(lambda+16)f^2<=10q_pol.

The last inequality uses lambda+16<=40lambda/9 for lambda>=6. For q_tor=lambda[h'^2+(lambda-2+gamma)h^2],

    K_tor<=3q_tor/(4beta), D_tor<=5q_tor/beta.

For the derivative estimate use D_tor<=2lambda h'^2+lambda(lambda+2t^2)h^2. At lambda=2, 2+2t^2<13/2<20/3<=5gamma/beta. For larger lambda the right-hand coefficient grows with slope5/beta>1, and2<=5/beta handles h'. Matrix orthogonality therefore gives

    integral eta_R integral_S2 |A-M0|^2<=(10/beta)Q_R.

The low velocity identity is

    integral eta_R K_low=K0 integral eta_R|a|^2
       +(1/2)integral eta_R|a'|^2-(k/2)integral eta_R'|a|^2.

The last term is O(1). The low derivative cost, high poloidal cost and high toroidal cost occupy disjoint gap families; their largest coefficient is at most1/beta. Consequently

    K0 integral eta_R|a|^2>=F(R)-Q_R/beta-C.

## 5. Finite spatial amplitude and the cap inequality

The case D_inf=infinity is immediate. Otherwise set h0=4piD_inf^2/(beta L) and delta=h0-H. For each epsilon>0, |A|<=D_inf+epsilon uniformly in n once z is large. Therefore G(R)<=4pi(D_inf+epsilon)^2 log R+C_epsilon. Section3 and then epsilon decreasing to zero imply delta>=0. The same pointwise estimate gives bounded gradient energy on every fixed-width far strip. The corresponding M0 strip is bounded by the velocity projection. The omitted strips in Section4 cost O(1), so

    limsup Q_R/(beta L Z)<=delta,
    limsup (beta L Z)^(-1)integral_0^Z integral_S2|A-M0|^2
                                           <=10delta/beta,
    liminf Z^(-1)integral_0^Z|a|^2
                          >=(beta L/K0)(1-delta/beta).

These follow first with D_inf+epsilon and then by epsilon decreasing to zero. Only0<=delta<beta requires further argument.

Rotational covariance and direct differentiation give

    |M0|_F^2=3t^2|a|^2/(16pi)
                     [1+k^2+(5-k^2)mu^2],
    mu=n.a/|a|.

For rho=1/sqrt(2), the caps |mu|>=rho have area4pi s regardless of the direction of a. On them |M0|>=c_rho|a|, where c_rho^2=3t^2(7+k^2)/(32pi) and4pi c_rho^2/K0=B^2. Hence

    4pi s[c_rho|a|-D_inf-epsilon]_+^2
                          <=integral_S2 |A-M0|^2.

The case a=0 is trivial. Apply the L2 triangle inequality in z to c_rho|a|<=D_inf+epsilon+[c_rho|a|-D_inf-epsilon]_+, divide by sqrt(Z), and use the preceding liminf and limsup bounds. Sending epsilon to zero yields

    B sqrt(1-delta/beta)
           <=sqrt(H+delta)+sqrt(10delta/(beta s)).

The cap direction can vary arbitrarily with z. No fixed angular limit is used.

## 6. The strict explicit gap and the unique exact root

Direct subtraction gives B^2-H=t^2(5-k^2)/[4(k^2+2)]>1/3. Also B<5/2 and sqrt(H)<5/2: indeed B^2<6 and H<17/4. Thus B-sqrt(H)>1/15. Suppose0<=delta<=beta/10000. The inequalities sqrt(1-x)>=1-x and sqrt(H+delta)<=sqrt(H)+delta/(2sqrt(H)), together with H>1, would give

    B-sqrt(H)<3/10000+sqrt(1/(1000s)).

Since s>1/4, the right side is less than3/10000+1/sqrt(250), which is less than3/10000+8/125=643/10000<1/15. Each comparison follows by squaring positive quantities or comparing rational numbers. This contradiction includes delta=beta/10000, so the final explicit bound is strict.

The function B sqrt(1-delta/beta)-sqrt(H+delta)-sqrt(10delta/(beta s)) is continuous and strictly decreasing on[0,beta]. It is positive at0 and negative at beta, hence has one root epsilon_beta in(0,beta). The preceding contradiction shows epsilon_beta>beta/10000. The cap inequality forces delta>=epsilon_beta if delta<beta; this is immediate if delta>=beta. This proves the stronger implicit bound without computing any numerical root.

## 7. Centers and the full-profile consequence

Ball inclusions give E_a(R)/(LR^beta)->1 at every fixed center a. The ratio |y-a|^((5-beta)/2)/|y|^((5-beta)/2) tends uniformly to1 as |y| tends to infinity, so D_inf is unchanged, even if infinite. Apply the kinematic proof to U(a+.). This is not a claim of translation invariance of the Euler profile equation.

For U,P in C1 solving the complete rotating profile equation, with bounded U, U(R.) tending to zero distributionally on compact sets and2/5<c<1/2, A3053 gives the energy ratio with beta=5-2/c and L>0 unless U=0. Therefore every nonzero such profile obeys the displayed amplitude lower bounds with exponent(5-beta)/2=1/c, for every finite omega. Uniform velocity decay supplies the bounded distributional premises. An upper bound at or below the explicit threshold forces U=0, with L interpreted as the nonzero profile's energy coefficient. No upper derivative bound follows from velocity decay in this proof.

## 8. Review scope

The larger degree-one endpoint amplitude is not applied to this entire class. The constants above are necessary lower bounds and are not asserted optimal. The positive-source controls submitted as LIT384 are not a dependency. The argument does not establish unrestricted rotating-Euler nonexistence.

All source sections, forty obligations and the formal-source note have been read. The existing configured model coordinator retains the independent comparison; actual provider execution is independently unattested. The comparison is reconciled in Section9. No mathematical computation, numerical root, formal build or fresh external source was used.

## 9. Independent comparison and adversarial reconciliation

The coordinator comparison retained as in the team records, SHA25649b24b417caec7292bb867088708cc26a25a4f57048caf8d3c9db3ce3bfc5eb7, contains235 newline-terminated lines,23 checked items and remarks R1-R7. All were read. Note241 announces the same hash with a different line count; the count discrepancy is not evidence of a changed version. The source remains fce67f51. The existing coordinator is configured as model; actual provider execution is independently unattested.

There is no mathematical disagreement. For R1, Section5 now derives the uniform gradient integral bound before concluding delta>=0. For R2, rotational orthogonality gives the sum of the scalar low-mode errors for the three coefficients, with no cross term. R3 permits smaller constants: t^2 k^2<1, |k+t|<1 and lambda>=6 give

    D_pol<=3f''^2/lambda+(9/2)f'^2+(lambda+15/2)f^2.

Indeed the coefficients before simplification are4+3(k+t)^2/lambda and lambda-2+4t^2+3t^2k^2/lambda. They are less than9/2 and lambda+15/2. The looser bounds in Section4 suffice. The toroidal spectral gap is strictly greater than4beta/3; no uniform endpoint improvement is needed.

R4 correctly distinguishes the minimum of |M0| over each cap from its maximum at the pole. The former, used here, is c_rho|a|. Neither the cap argument nor its L2 averaging fixes the direction of a(z). The projection and strip estimates apply to the complete harmonic expansion with constants independent of truncation. There is no pressure or flow-completeness assumption in this kinematic theorem.

The grids, decimal root values and soft-maximum optimization in items19,22,23 and R5-R6 are not part of this verification. In particular a sampled maximum is not an upper bound for the true spherical maximum, so the comparison's proposed improvement of a family optimum is not certified here. No optimality assertion is needed for the exact root theorem. R7 is essential: the Euler corollary uses A3053 only to supply the energy ratio and does not supply any upper gradient bound. Every finite omega is covered, with constants independent of omega, under the hypotheses in Section7.
