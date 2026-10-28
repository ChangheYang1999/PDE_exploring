# A rough weighted inverse and conditional nonlinear theorem

Status: independently audited in V078. This is a conditional theorem. The accepted state satisfies its background and forcing-membership hypotheses, but fails the certified residual-smallness test in V079.

## 1. Spaces, hypotheses and theorem

Use the exact weights and norm of PROOF.md, namely R=2^35, w=(1+r2/R2)^(-11/10), omega0=<r>^-6/5, omega1=<r>^-1/5, omega2=(1+4r2)^2/5, and

    L(g)=||wg||Hminus,
    E(g)^2=P2(g)^2+2^22 P1(g)^2+2^53 L(g)^2,
    Pj(g)=||omegaj D^j g||2,
    N(g)=N_s^w(g)=E(J^s g), J=(1-Delta)^1/2.

All density inputs have even-x, odd-y parity, and all tensors use ordered Cartesian derivatives. The spaces are the compact smooth parity-core completions. The Fourier convention and the canonical velocity are those of PROOF.md.

Assume a smooth sublinear reference rho, canonical u=U[rho], normalized by c+c[rho]=1, with center slope a0>=1. Suppose its fixed-c operator L0=(cX+u).D-1+U[.].D rho has consistent low and E generator realizations, with energy decay at least1/5 and1/20, respectively. Suppose also

    |c|<=2, |Du|_F<=14/5, |D rho|<=16,
    <r>|D2u|_F<=3, <r>|D3u|_F<=16,
    <r>|D2rho|_F<=8, |D2rho|_F<=3,
    <r>2|D3rho|_F<=32, <r>2|D4rho|_F<=512.

Exact state131 satisfies every hypothesis by V073-V074 and their dependencies. For another reference the hypotheses must be certified anew. All fractional estimates below are asserted for0<s<=2^-96.

For k in N define A_k=L0+U[k].D. The semigroup estimate is

    ||exp(t A_k)||_(N->N)
       <=exp[-t(1/20-2^92 s-2^19 N(k)/sqrt(s))].           (1)

The domain is the maximal distributional domain in N. Every positive rate yields a bijective inverse with reciprocal-rate bound. In particular put

    s=2^-104, r0=2^-78, eta=r0/24.                        (2)

On N(k)<=r0 the rate exceeds1/24. If c[k]=0, the inverse takes f_y(0)=0 exactly to c[h]=0. If the actual reference residual belongs to N and N(F(rho))<=eta, there is a unique h in the normalized N ball of radius r0 with F(rho+h;c)=0. This is conditional: no residual-smallness assertion is included.

The rest of this file proves each bound and realization needed for this theorem. It is not permitted to identify this norm with the unweighted-bottom N_s of09_quasilinear.

## 2. Kernel estimates with relative weights

Write the positive fractional kernel as

    J^s f=f+int kappa_s(z)(f(X)-f(X-z)) dz,
    kappa_s=s/[2 Gamma(1-s/2)] int_0^infinity e^-t p_t(z)t^(-1-s/2)dt.

The heat kernel p_t=(4pi t)^-1 exp(-r2/(4t)) has radial moments E(r)=sqrt(pi t), E(r2)=4t and E(r3)=6sqrt(pi)t^(3/2). The established bounds in09_quasilinear/PROOF.md give

    int r kappa_s<=13s, int r2 kappa_s=2s,
    int r(1+2r) kappa_s<=17s,
    int r2(1+2r)|D kappa_s|<=54s.                         (3)

Also int r3 kappa_s<=30s. Indeed its exact value is3sqrt(pi)s Gamma((3-s)/2)/Gamma(1-s/2). Splitting the numerator integral at1 gives Gamma((3-s)/2)<2, while Gamma(1-s/2)>e^-1; sqrt(pi)<2 and e<3 give the stronger bound36s, which by itself is insufficient for30s. A sharper elementary numerator bound is at most5/3: the integral over(0,1) is at most4/5, and the tail is at most2/e, whose sum is below5/3. Thus the stated30s follows. Consequently

    int r(1+2r)^2 kappa_s <256s,
    int 2r(1+r2) kappa_s <128s.                          (4)

The two derivative weights v=omega1 or omega2 satisfy v(X)/v(Y)<=1+2|X-Y| and |v(X)/v(Y)-1|<=2|X-Y|. Their positive Bessel-kernel bound is ||v J^-s f||2<=3||vf||2. Therefore

    ||[J^s,v]f||2<=34s||vf||2,
    ||J^s(vf)||2<=(1+102s)||vJ^s f||2.                   (5)

The small constant is not obtained from an absolute bound on Dv. It is a relative-weight estimate and remains valid for the decreasing weight omega1.

For multiplication by a smooth scalar coefficient d, let C bound the sum of the suprema of the relevant entries of (v_out/v_in) Dd. For every cross pair used below, the product of the two weight moderation factors is at most(1+2r)^2. Indeed the moderation exponents for omega0, omega1 and omega2 are6/5,1/5,4/5, respectively, and every cross pair has exponent sum at most2. This also handles the input omega0, whose individual moderation is not bounded by1+2r. The segment integral and(4) give

    ||v_out[J^s,d]f||2<=256s C||v_in f||2.                (6)

For the same weight and bounded Dd, the sharper17s bound applies. The input weight omega0 has moderation (1+r)^(6/5)<=2(1+r2), so its same-weight commutator obeys128s||Dd||_infinity. These assertions also hold for Euclidean tensor contractions, using the stated sums when components are separated.

Taylor expansion of a smooth vector field d, with the derivative integrated off the input in the quadratic remainder, gives for v=omega1,omega2

    ||v[J^s,d.D]J^-s H||2
      <=s(28||Dd||_(Sigma,infinity)+132||D2d||_(Sigma,infinity))||vH||2. (7)

The linear Taylor term is -s sum_(i,j) d_(i,j) partial_ij J^-2. Its weighted norm is at most28s||Dd||_Sigma. The remainder uses(3), the positive J^-s bound3, and3(54/2+17)=132. The relative commutator of v with partial_ij J^-2 is bounded by its first kernel moment; its delta term commutes with v. The small-circle boundary is O(epsilon^(1-s)). Thus(7) loses no derivative.

## 3. Low negative-order estimates and the radius factor

For a vector P of the correct induced parity,

    L(div P)<=16/5 ||wP||2.                              (8)

Indeed pair with a centrally odd homogeneous H1 test phi, integrate by parts, and use ||phi/r||2<=||Dphi||2 and r|Dlog w|<=11/5. Also

    w/omega0<=R^(6/5)=2^42.                              (9)

This conversion is retained throughout. It is the source of the large background constant.

The following additional estimate supplies the inclusion N into L:

    L(J^-s H)<=L(H)+2^50 s P0(H).                        (10)

To prove it, write J^-s-I=div K_s*, where K_s is the gamma mixture of int_0^t Dp_v dv. The omega0-moderated L1 norm of K_s is at most64s. In fact the integrand moment is bounded by sqrt(pi)v^-1/2+6sqrt(pi)v^1/2; integration gives2sqrt(pi)t^1/2+4sqrt(pi)t^3/2. Put a=s/2. The gamma mixture is

    2sqrt(pi) Gamma(a+1/2)/Gamma(a)
      +4sqrt(pi) Gamma(a+3/2)/Gamma(a).

Splitting at1 gives numerator bounds3 and2, and1/Gamma(a)<=e a. Hence the expression is at most7sqrt(pi)e s<42s<64s. Apply(8)-(9), and(10) follows. Since P0(H)<=E(H), for s<=2^-96 this gives L(g)<=N(g). Here L(H)<=2^(-53/2)E(H), so the last claim follows from2^(-53/2)+2^(-46)<1.

Likewise ||omega0 D J^-2 H||2<=16 P0(H), because its heat integral is4pi<16. Thus

    L((I-J^-2)H)<=2^48 P0(H),                            (11)

using I-J^-2=-Delta J^-2 and(8)-(9). These arguments are valid on the core, and pass to the completions in the stated norms.

## 4. Complete smooth-reference commutator

Let H=J^s g, T=[J^s,u.D], Qg=U[g].D rho. The exact identities are

    D2 T g=T D2g+2[J^s,Du]D2g+[J^s,D2u]Dg,
    D T g=T Dg+[J^s,Du]Dg,
    D2[J^s,Q]g=[J^s,D rho]U[D2g]
                    +2[J^s,D2rho]U[Dg]+[J^s,D3rho]U[g],
    D[J^s,Q]g=[J^s,D rho]U[Dg]+[J^s,D2rho]U[g],
    T g=div([J^s,u]g), [J^s,Q]g=div([J^s,rho]U[g]).        (12)

Every ordered multiplicity is included. The tensor hypotheses give the safe sums

    ||Du||_Sigma<=12, ||D2u||_Sigma<=24,
    ||<r>D3u||_Sigma<=256,
    ||D rho||_Sigma<=32, ||D2rho||_Sigma<=12,
    ||<r>2 D3rho||_Sigma<=256,
    ||<r>2 D4rho||_Sigma<=8192.                           (13)

These use the number of entries times the global Frobenius bound, not the square root of that number; different entries may have different maximizing points. The ratios omega2/omega1<=2<r>, omega2/omega0<=2<r>2 and omega1/omega0=<r> are explicit.

Apply(6)-(7), the weighted J^-s bounds4,2,3, and the velocity bounds8/3,3/2,9/5 on omega0,omega1,omega2, respectively. The top transport bound is

    s[(28*12+132*24+2*17*24*3)P2(H)
                       +256*512*2 P1(H)].

The top Q commutator is bounded by

    s[17*12*(9/5)*3 P2(H)
      +2*256*512*(3/2)*2 P1(H)
      +256*16384*(8/3)*4 P0(H)].                          (14)

Their sum is below2^26 s E(H). The first-derivative transport and Q sum is below

    s[(28*12+132*24+17*24*2+17*12*(3/2)*2)P1(H)
                        +256*256*(8/3)*4 P0(H)]
       <2^20 s E(H).                                    (15)

For the low component,(8)-(9),(12) and the omega0 same-weight commutator give

    L(Tg+[J^s,Q]g)
      <=(16/5)2^42*128s[12*4+32*(8/3)*4]P0(H).            (16)

After multiplication by2^(53/2), this is below2^87 s E(H). The dilation commutator is sc(I-J^-2). Its top and first derivative weighted norms are at most6s|c|Pj(H), and its weighted-low norm follows from(11). All three contributions together are below2^77 s E(H). Summing the square-root component estimates, including the first derivative coefficient2^11, yields

    E([J^s,L0]J^-s H)<2^92 s E(H).                       (17)

No multiplication by the unbounded density was used in the low norm; only its exact divergence commutator was used.

## 5. Rough transport without a third derivative

Set n=N(k), W=U[k], A=(2pi)^-1 int |xi||W_hat|. PROOF.md gives A<=2^11 n/sqrt(s) and d=||DW||infinity<=A. The exact Fourier multiplier inequality

    |eta| |<xi>^s-<eta>^s|<=|xi-eta|<eta>^s

implies ||[J^s,W.D]F||2<=A||J^s F||2. The relative weight commutator, for v=omega1,omega2, is

    [v,[J^s,W.D]]F
       =int D kappa_s(z).(W(X)-W(X-z))(v(X)-v(X-z))F(X-z)dz.

This is absolutely integrable. Its norm is at most108s d||vF||2. Using(5) and the positive J^-s bound gives

    ||v[J^s,W.D]F||2<=(1+426s)A||vJ^s F||2
                         <=2A||vJ^s F||2.               (18)

The derivative product theorem in PROOF.md, followed by(5), also gives

    ||vJ^s(Dg f)||2<=2^15 N(g)/sqrt(s)||vJ^s f||2.        (19)

Indeed commute v across J^s at both ends: the first contribution is at most2^14(1+102s)N(g)/sqrt(s); the second is at most102s||Dg||infinity. Their sum is below2^15N(g)/sqrt(s). The same estimate holds with DU[g].

For H=J^s g the top identity is

    D2J^s(W.Dg)=W.D D2H+[J^s,W.D]D2g
                       +2J^s(DW D2g)+J^s(D2W Dg).       (20)

Since W(0)=0, |W.Dlog omega2|<=(4/5)d and |W.Dlog omega1|<=(1/5)d. The top energy loss, using(18)-(20) and the9/5 velocity bound for D2k, is at most

    (n/sqrt(s))[(14/5)2^11 P2(H)^2
                 +2*2^15 P2(H)^2+(9/5)2^15 E(H)P2(H)].  (21)

The first derivative component, including its factor2^22, has loss at most

    (n/sqrt(s))[(11/5)2^11+2^15] 2^22 P1(H)^2.           (22)

For the low component split J^s(W.Dg)=W.DH+div([J^s,W]g). The first term has absolute weighted negative-order energy loss at most12d L(H)^2, by the weak integration-by-parts calculation in07_weighted/LOW_INVERSE_PROOF.md. The second has, by(8)-(9),(4),

    2^(53/2)L(div([J^s,W]g))<2^80 s d E(H)
                                      <=2^91 sqrt(s)n E(H). (23)

As s<=2^-96, its normalized loss is below(1/32)nE(H)^2/sqrt(s). The first low loss is at most12*2^11(n/sqrt(s))2^53L(H)^2. Since each square-root energy component is bounded by E(H), direct addition of(21)-(23) is below

    2^19(n/sqrt(s))E(H)^2.                               (24)

This is a core energy-form estimate. It does not assert that W.D maps the entire high space boundedly to itself. No third derivative of W occurs. Combining the base E decay, (17) and(24) gives(1) on the core.

## 6. Realization, maximal domain and inverses

The map J^s:N->E is an isometric bijection by PROOF.md. Approximate k by compact smooth k_m in N. Then W_m=U[k_m] converge in their gradients uniformly, and W_m(0)=0 implies |W_m-W_l|<=d_ml r with d_ml tending to zero. Every smooth W_m has bounded higher derivatives with the weighted decay needed for the E flow. Equation(17), with finite constants depending on m when necessary, makes the J^s-conjugated operator a bounded perturbation of that smooth E generator. Thus it gives a C0 semigroup on N; (1) supplies bounds uniform in m.

Use P0 as the common lower topology. The complete Lipschitz transport field defines a C0 group on L2(omega0^2); its finite-time norm is bounded from its divergence and the logarithmic derivative of omega0. The fixed coupling Q is bounded there by16*(8/3). For the difference of two high solutions, the forcing is (W_m-W_l).D h_l, with

    P0((W_m-W_l).D h_l)<=d_ml P1(h_l)<=2d_ml N(h_l).

The weighted L2 energy estimate and Gronwall make these solutions Cauchy in C_t P0 on finite intervals. Their weak high limits agree with the P0 limit, giving a semigroup with(1). At zero, weak high convergence and the limsup norm bound imply strong convergence. Uniqueness of the P0 transport-plus-bounded-coupling equation gives the semigroup law.

The weighted L2 transport generator has exactly its maximal distributional domain. Here are the details needed for this identification. If h and b.Dh belong to P0, first multiply h by radial cutoffs at radius R. The additional term b.Dchi_R h tends to zero in P0 because b grows at most linearly and h has a vanishing P0 tail. On a fixed compact set mollify. The Friedrichs commutator b.D(h*eta_epsilon)-(b.Dh)*eta_epsilon tends to zero in local L2: its integral kernel contains [b(X)-b(Y)]Deta_epsilon and the bounded divergence correction; the Lipschitz bound gives a uniform local L2 operator bound, and convergence follows first for smooth h and then by L2 density. The smooth approximations satisfy the characteristic integral identity. Passing to the limit in P0, using the bounded finite-time transport group, gives T_t h-h=int_0^t T_v(b.Dh)dv. Thus every maximal distributional domain element is in the strong generator domain. The reverse inclusion follows by testing the strong difference quotients against compact smooth functions. Adding the bounded Q-1 term preserves this domain characterization. The high semigroup is the part of this generator in N. The Duhamel identity for h with A_kh in N then identifies its strong high derivative. This proves the asserted high maximal domain.

For a positive rate, the Bochner integral -int_0^infinity exp(tA_k)f dt converges in N. The finite-integral generator identity and closedness show A_k h=f. A kernel element would have a constant orbit, contradicting decay. This proves surjectivity and injectivity.

The low semigroup has rate1/5-12d. It is consistent with the P0 semigroup on L intersect P0: radial inner and outer cutoffs are uniformly bounded on Hminus by angular Hardy and converge there by core density; they also converge in P0. Compactly supported P0 functions are L2 and can be mollified to the common smooth core in both norms. For smooth approximating velocities the two semigroups agree on this core by the identical characteristic formula and bounded-coupling Duhamel series. The flows for W_m converge locally in C1 to the W flow, with uniform distortion bounds, since DW_m converge uniformly. On compact core data the transport groups therefore converge in both lower norms; their uniformly convergent Duhamel series retain this agreement. Density then gives agreement on the intersection. By(10) the high space is included in both lower spaces. Whenever the high rate is positive, d<1/5120 and the low rate is positive as well, so the two convergent inverse integrals agree. A further domain point is needed for the nonlinear difference equation. If h belongs to N and A_k h belongs to L intersect P0, the maximal P0 realization gives S_t h-h=int_0^t S_v A_k h dv in P0. Consistency makes every term an element of L and makes the same identity hold there. Strong continuity in L then proves that h is in the low generator domain with generator value A_k h. For the differences used below the additional source (U[k1]-U[k2]).D h belongs to P0 since its norm is bounded by ||D U[k1-k2]||infinity P1(h); it belongs to L by(26). Therefore the low inverse estimate applies to those differences without assuming a maximal-domain theorem on arbitrary negative-order distributions.

## 7. Low bilinear estimate on this high space

For a centrally odd homogeneous H1 test phi and q=4/s,

    ||phi/omega2||_q<=2^9 s^-1/2||Dphi||2.                (25)

To prove this, partition into dyadic annuli t<=r<=2t for all integer powers t of2. A radial cutoff equals one on that annulus, is supported on t/2<=r<=4t, and has rescaled gradient at most16. Angular Poincare gives the rescaled L2 bound4e_t and gradient bound65e_t, where e_t=||Dphi|| on the larger annulus. The H1 norm is at most69e_t. Fourier Hausdorff-Young followed by Holder gives ||f||q<=2s^-1/2||f||H1. In fact its constant is (2pi)^(-1+s/2)[pi(2-s)/s]^((2-s)/4), which is at most s^-1/2 for0<s<=1/2: the bracket exceeds1, its exponent is at most1/2, and (2pi)^(-1+s/2)<=(2pi)^(-1/2). The rescaling and reciprocal weight cost at most t^(s/2) for t<=1, and t^(s/2-4/5) for t>=1; both are at most1. The larger annuli overlap at most four times. Since q>=2, the lq norm is bounded by the l2 norm, proving(25) with276<512.

Let p=2/(1-s/2). The same Fourier proof gives ||f||p<=||f||Hs, with the explicit smaller constant (4pi)^(-s/4): the Holder weight integral is int <xi>^-4 dxi=pi. By(5), ||omega2 D2g||Hs<=2N(g). Hence Holder and(25) give

    ||D2g phi||2<=2^10 s^-1/2 N(g)||Dphi||2.

Combining with ||Dg||infinity<=2^11s^-1/2N(g), the dual multiplier norm is below2^12s^-1/2N(g). Pair with wU[h] and use its13/2 low bound. The resulting continuous bilinear map is

    L(U[h].Dg)<=2^15 s^-1/2 N(g)L(h).                    (26)

Density defines the product; when g is high and h is high or smooth it agrees with the ordinary distributional product.

## 8. Normalization, phase and nonlinear contraction

The C1 representatives of h and U[h], whose first derivatives are bounded, give directly at the origin,

    (A_k h)_y(0)=c[k]h_y(0)+a0 c[h].                     (27)

Only first-order expansion is used. Since a0 is nonzero, c[k]=0 makes the forcing hyperplane f_y(0)=0 exactly equivalent to c[h]=0 in the domain. The reference residual has F_y(0)=a0(c+c[rho]-1)=0.

At(2), the high decay is

    1/20-1/4096-1/128=859/20480>1/24.

Also d<=2^11r0/sqrt(s)=2^-15, so the low decay is at least1/5-12/32768>1/6, with inverse at most6. The map T(k)=-A_k^-1F(rho) preserves the closed normalized N ball if N(F)<=eta. For two inputs, its difference solves an equation with right side -(U[k1-k2]).D T(k2), which is in L by(26). The consistent low inverse gives the contraction constant

    6*2^15*r0/sqrt(s)=3/1024<1/100.                      (28)

The high ball is closed in L: bounded high sequences have weak subsequences, and low convergence identifies their distributional limit; weak lower semicontinuity retains the bound. The functional c is continuous in N, so its zero hyperplane is also retained by that weak convergence. The resulting metric space is complete. Banach contraction gives the unique fixed point. Every normalized solution in the ball is such a fixed point by the high inverse uniqueness. The corrected center slope remains positive since its change is at most2^-15.

The high correction has growth O(r^1/5) by PROOF.md. If the reference has a full nonzero leading r^gamma angular profile with1/5<gamma<1, fixing that profile therefore excludes its scaling tangent and exponent-logarithm variations. These parameters are frozen; no theorem about free leading angular or exponent variations is claimed.

## 9. Direct Holder control, strain and a local moment

Put alpha=s/2, p0=8/s and kappa=p0+4. Define the adapted Holder norm by the B2 C^alpha norm plus

    sup_(j>=0)2^(-j/4)[||h||Linfinity(Aj)
                            +2^(j alpha)[h]C^alpha(Aj)].

The growth and gradient estimates of PROOF.md, with the elementary Holder interpolation between the supremum and Lipschitz bounds, show that this norm is at most2^16s^-1/2N(h). Indeed on an annulus t<=r<=2t the supremum is at most10240 t^(1/5)N, and the Holder interpolation bound is at most20480 s^(-1/2)t^(1/5+(4/5)alpha)N after inserting the rescaling t^alpha. Both radial exponents are below1/4. The same two constants bound the center ball contributions. Twice their sum is61440<2^16. For the center remainder, Taylor integration and the gradient Holder estimate give

    M(h)=[int_(r<1)r^-kappa|h-h_y(0)y|^p0 dX]^(1/p0)
          <=2^13s^-1/2N(h),

because p0 alpha+2-4=2. The exact strain formula includes its local term,

    c[h]=-h_y(0)/4+(1/pi)PV int sin(3theta)h/r3 dX.

The near part is bounded by4[D h]C^alpha/[pi alpha(1+alpha)], and the far part by C P0(h), with C<2 from polar integration on r>1. Thus |c[h]|<=2^15s^-3/2N(h). Together with(10), all four target quantities obey

    L(h)+C_ad(h)+M(h)+|c[h]|<=2^18s^-3/2N(h)
                                   <=2^23s^-3/2 N(A_kh). (29)

This proves a direct Holder estimate for h in a compatible space. The primary variable is h; no Holder norm of h_x is used as an independent unknown. The additional regularity is quantified by the same high norm that defines the generator.

## 10. Remaining numerical task

A smooth parity function f satisfying |D^j f(X)|<=C_j<r>^(q-j) for0<=j<=3 and q<1/5 belongs to N when q>=0. Indeed D^j commutes with J^s, and the mean-value theorem with the Peetre weight inequality gives

    |D^j(J^s-I)f(X)|
      <=C_(j+1)<r>^(q-j-1)
           int |z|(1+|z|)^(j+1-q) kappa_s(z)dz,
    0<=j<=2.

Each kernel integral is finite: near zero s<1 suffices, and at infinity every polynomial moment is finite by the Gaussian-mixture formula. Thus |D^j J^s f|<=C'_j<r>^(q-j). The three majorants for P1, P2 and ||r w J^s f||2 have radial squared integrand O(r^(2q-7/5)), integrable since q<1/5. Parity Hardy bounds the low norm by the last quantity. To prove membership in the core completion rather than mere finiteness, truncate f smoothly at radius R. All three symbol bounds remain uniform for f-f_R, the derivatives tend locally to zero, and dominated convergence in the kernel formula gives D^j J^s(f-f_R) tending pointwise to zero with the same integrable majorants. Weighted L2 dominated convergence and parity Hardy give N(f-f_R) tending to zero.

The original residual has precisely such symbol bounds, with q=2/c-1 in(0,1/5): this follows by differentiating its finite exact regularized-power potential and the quadratic residual. Its original linear leading term cancels because c*gamma=1, and V005 identifies the first nonzero residual power. Therefore its weighted fractional forcing membership is proved. Its actual norm exceeds eta by more than24*2^60; the independent pointwise certificate is in RESIDUAL_GAP_PROOF.md and V079. No existence near the accepted state is asserted by the conditional theorem.

## General-rate qualification, V086

The four-output estimate with numerical inverse factor2^23 is asserted on the specified parameter ball (2), whose high inverse is at most32. For an arbitrary positive decay rate beta supplied by the general semigroup bound, the corresponding estimate is

    L(h)+C_ad(h)+M(h)+|c[h]|
             <=2^18 s^(-3/2) beta^(-1) N(A_k h).

No uniform bound on beta^(-1) is claimed when beta tends to zero. The embeddings themselves retain their stated constants.
