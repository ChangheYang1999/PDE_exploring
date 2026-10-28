# A uniform inverse for rough perturbing velocities and a conditional existence theorem

## Exact statement and scope

All functions on R^2 are real, even in x and odd in y. The canonical velocity is U[h]=(-R1 R2 h,R1^2 h), with Rj=partial_j(-Delta)^(-1/2). Let H be the homogeneous H^-1 completion of smooth compactly supported functions with this parity. Its norm is ||(-Delta)^(-1/2)h||_2. Use all ordered derivatives in tensor norms and set

    omega=(1+4|X|^2)^(2/5), b0=20/21, B=2^14,
    E2(h)^2=||omega D^2h||_2^2
             +B||Dh||_2^2+16B||h||_2^2+16Bb0||h||_H^2.

For use below define also E3(h)^2=||omega D^3h||_2^2+2^173 E2(h)^2 on the same compact core, and take its completion. The singular functional is c[h]=partial_y U_2[h](0)=psi_xy[h](0), with psi=partial_x(-Delta)^-1 h; its local and principal-value representation is proved in04_singular/PROOF.md. For N_s inputs it is defined by the bounded C1 velocity representative. Write lambda=2c-1.

The space E2 is the completion of that smooth compact core. Set J=(1-Delta)^(1/2), and let N_s be its core completion for the norm

    N_s(h)=E2(J^s h),                 0<s<=1/2.

Let a smooth reference density rho_bar have the prescribed parity, canonical velocity u, exponent c, sublinear growth and bounded first derivatives. Assume c+c[rho_bar]=1, a0=partial_y rho_bar(0) !=0, and the following two explicit hypotheses.

1. The fixed-exponent operator

       Lh=(cX+u).Dh-h+U[h].D rho_bar

   has its consistent transport-plus-bounded-coupling realization on E2, with energy decay1/10. The coefficient conditions sufficient for this hypothesis are listed in 07_weighted/SHARP_ROUTE_U_PROOF.md: M>=19I/5, A>=-I/20, N<=I, M1>=9I/10, M2>=I/2 and its five derivative bounds. Its low realization on H has energy decay19/5.

2. Writing ||T||_(Sigma,infinity)=sum_I ||T_I||_infinity, where I ranges over all ordered tensor indices, the finite quantity

       Mstar=|c|+||Du||_(Sigma,infinity)
          +||omega D^2u||_(Sigma,infinity)+||omega D^3u||_(Sigma,infinity)
          +||D rho_bar||_(Sigma,infinity)
          +sum_(j=2)^4 ||omega D^j rho_bar||_(Sigma,infinity)

   is at most4096.

These hypotheses hold for exact accepted state131. The additional D^3u and D^4rho certificates are audited in 07_weighted/SHARP_COEFFICIENT_PROOF.md. They do not automatically hold for a numerical refit.

For k in N_s define A_k=L+U[k].D. Its maximal distributional domain in N_s is the generator domain of a strongly continuous semigroup, and

    ||exp(t A_k)||_(N_s->N_s)
       <=exp[-t(1/10-1024 s Mstar-128 N_s(k)/sqrt(s))].          (1)

Whenever the rate beta in (1) is positive, A_k is bijective from its domain to N_s, with inverse norm at most1/beta. If c[k]=0, its inverse takes precisely the forcing hyperplane f_y(0)=0 to the solution hyperplane c[h]=0.

In particular choose

    s=2^-28, r=2^-27, eta=2^-27/20.                           (2)

For every k with N_s(k)<=r the rate is at least11/160>1/20, and the inverse norm is at most20. If the actual reference residual R=F(rho_bar) belongs to N_s and N_s(R)<=eta, then there is a unique h in

    {h in N_s: N_s(h)<=r, c[h]=0}

such that F(rho_bar+h)=0 with the same exponent c. This is a conditional a posteriori theorem. The original accepted residual fails the H component and does not satisfy its hypotheses. No existence near that original state is asserted.

## 1. Fractional kernels and weights

Use the unitary Fourier convention in dimension2, so multiplication gives a convolution factor1/(2pi). The weight obeys

    omega(x)/omega(y)<=m(x-y),  m(z)=(1+2|z|)^(4/5)<=1+2|z|,
    ||D omega||_infinity<=2, ||D log omega||_infinity<=4/5,
    |X| |D log omega(X)|<=4/5.                                (3)

The first inequality follows by applying the triangle inequality to (1,2x). The other inequalities follow by differentiating. In particular |W.D log omega|<=(4/5)||DW||_infinity if W(0)=0.

For 0<s<1,

    J^s f=f+int kappa_s(z)(f(x)-f(x-z)) dz,
    kappa_s(z)=s/[2 Gamma(1-s/2)]
       int_0^infinity exp(-t) p_t(z) t^(-1-s/2) dt,
    p_t(z)=(4pi t)^(-1) exp(-|z|^2/(4t)).                    (4)

This follows by applying the scalar Laplace integral for a positive fractional power to 1+|xi|^2 and separating its value at xi=0. Direct Gaussian moments yield

    int |z| kappa_s = (s sqrt(pi)/2) Gamma((1-s)/2)/Gamma(1-s/2),
    int |z|^2 kappa_s=2s.                                   (5)

The second identity is 2s, not4s. With A=Gamma((1-s)/2)/Gamma(1-s/2), the weighted bounds are

    int |z| m(z) kappa_s <=s(sqrt(pi) A/2+4)<=17s,
    int |z|^2 m(z)|D kappa_s| <=s(3sqrt(pi) A/2+16)<=54s.     (6)

Indeed Gamma((1-s)/2)<5, from splitting its integral at1, and Gamma(1-s/2)>exp(-1). Thus A<5e for 0<s<=1/2, which proves the rounded constants.

The Bessel kernels of J^-s and J^-2 are positive probability kernels with second moments2s and4. Equations(3) and Cauchy-Schwarz imply

    ||omega J^-s f||_2<=3||omega f||_2,
    ||omega J^-2 f||_2<=5||omega f||_2.                      (7)

Also

    ||omega partial_i partial_j J^-2 f||_2<=28||omega f||_2. (8)

Here is an independent check including the singular local term. Away from zero the kernel is q_ij=int exp(-t) partial_ij p_t dt. Its unweighted operator norm is at most1. The bound |partial_ij p_t| <= (|z|^2/(4t^2)+1/(2t))p_t gives int |z||q_ij|<=2pi. Since |omega(x)/omega(y)-1|<=2|x-y|, the weight commutator has norm at most4pi. The local term of this particular second-derivative Bessel kernel is -(delta_ij/2)delta_0, which is multiplication by a scalar and commutes with the weight. This statement does not apply to derivatives of delta_0. Thus1+4pi<14 already suffices, and28 is safe. Alternatively int |z|m(z)|q_ij|<=2pi+20<27.

From(4), the mean-value theorem and(6),

    ||omega[J^s,d]f||_2<=17s ||omega Dd||_(Sigma,infinity)||f||_2,
    ||omega[J^s,d]f||_2<=17s ||Dd||_(Sigma,infinity)||omega f||_2,
    ||[J^s,omega]f||_2<=34s||f||_2.                          (9)

For the first bound insert the weight at each point on the segment from x-z to x and use(3). These arguments allow unbounded d with the displayed derivative bounds.

## 2. Smooth background commutator with full bookkeeping

For a smooth vector field d, Taylor-expand

    d_j(x)-d_j(x-z)=sum_l partial_l d_j(x) z_l+R_j(x,z).

The remainder satisfies |R_j|<=|z|^2||D^2d_j||_(Sigma,infinity)/2 and |D_z R_j|<=|z|||D^2d_j||_(Sigma,infinity). The linear term in [J^s,d.D]J^-s is exactly

    -s sum_(j,l) (partial_l d_j) partial_l partial_j J^-2.

For the remainder integrate the derivative off J^-s h(x-z). Equations(6)-(8) give

    ||omega[J^s,d.D]J^-s h||_2
       <=s(28||Dd||_(Sigma,infinity)+132||D^2d||_(Sigma,infinity))
          ||omega h||_2.                                  (10)

The132 is3(54/2+17). The small-circle boundary is O(epsilon^(1-s)), hence vanishes. The unweighted estimate is no larger. No derivative is lost.

Let h=J^s g, T=[J^s,u.D], and Qg=U[g].D rho_bar. Differentiation, with all ordered contractions, gives

    D^2Tg=T D^2g+2[J^s,Du]D^2g+[J^s,D^2u]Dg,
    D^2[J^s,Q]g=[J^s,D rho_bar]U[D^2g]
                 +2[J^s,D^2rho_bar]U[Dg]+[J^s,D^3rho_bar]U[g]. (11)

Both velocities are divergence free. Therefore

    Tg=div([J^s,u]g),
    [J^s,Q]g=div([J^s,rho_bar]U[g]).                       (12)

This last identity does not require bounded multiplication by rho_bar. It gives an H bound17s Mstar ||h||_2 for each commutator.

Write P=||omega D^2h||_2, a=||Dh||_2, b=||h||_2, and E=E2(h). The four square-root weights in E are1,128,512,512sqrt(b0). The following bounds use (9)-(12), ||U||_(L2->L2-vector)<=1, and the unweighted contraction J^-s. Each entry bounds the indicated output norm divided by s Mstar:

| output | T g | [J^s,Q]g |
| --- | --- | --- |
| weighted second derivative | 194P+17a | 17P+34a+17b |
| first derivative | 177a | 17a+17b |
| L2 | 160b | 17b |
| H | 17b | 17b |

For example194=28+132+2(17); no third derivative of u is used in the top transport term, only in its final multiplication commutator. After inserting the four norm weights and using P<=E, a<=E/128, b<=E/512, the first column has E2 norm at most565s Mstar E by the triangle inequality. The second has E2 norm at most(493/4)s Mstar E. These deliberately loose sums retain every ordered contraction.

Finally Fourier differentiation gives

    [J^s,X.D]J^-s=s(I-J^-2).

Its E2 norm is at most6s. Since565+493/4+6=2777/4<1024, we have proved

    ||[J^s,L]J^-s h||_E2<=1024 s Mstar E2(h).             (13)

## 3. Rough transport without third derivatives of k

For 0<s<=1 and all xi,eta,

    |eta| |<xi>^s-<eta>^s|<=|xi-eta|<eta>^s.             (14)

Divide by <eta>^s and use |t^s-1|<=|t-1| and the1-Lipschitz property of <xi>. Fourier convolution and Cauchy-Schwarz now give

    ||[J^s,W.D]F||_2<=c_s||W||_(H^(2+s))||J^s F||_2,
    c_s=1/[2sqrt(pi s(1+s))].                            (15)

The integral used here is int |xi|^2<xi>^(-4-2s) dxi=pi/[s(1+s)]. The same calculation gives ||DW||_infinity<=c_s||W||_(H^(2+s)). Euclidean tensor norms require no extra dimension factor.

Set T_W=[J^s,W.D]. For divergence-free W, integration by parts in(4) gives the exact, absolutely integrable commutator

    [omega,T_W]F(x)=int D kappa_s(z).(W(x)-W(x-z))
                             (omega(x)-omega(x-z))F(x-z) dz. (16)

Its norm is at most108s||DW||_infinity||F||_2. Combining(9),(15),(16) gives

    ||omega T_W F||_2
       <=c_s(1+142s)||W||_(H^(2+s))||omega J^s F||_2.    (17)

The required product estimate, including its weight, is

    ||vf||_(H^s)<=s^-1/2||v||_(H^(1+s))||f||_(H^s),
    ||omega J^s(vf)||_2
       <=(1+44s)s^-1/2||v||_(H^(1+s))||omega J^s f||_2. (18)

For completeness, the first bound follows by Fourier Cauchy-Schwarz: split the integral of <xi>^(2s)/(<eta>^(2+2s)<xi-eta>^(2s)) according to |xi-eta|>=|xi|/2. The two contributions are at most2pi/s and16pi, so their sum is at most10pi/s for s<=1/2. The convolution normalization is1/(2pi), and sqrt(10pi)/(2pi)<1. The weighted bound follows by commuting J^s past omega twice using(9), together with ||v||_infinity<=||v||_(H^(1+s))/(2sqrt(pi s)); its numerator is at most1+34s+17s/sqrt(pi)<1+44s. The proof also applies to Euclidean tensor contractions.

Take W=U[k]. Since E2 dominates H^2,

    ||W||_(H^(2+s))<=N_s(k), ||DW||_infinity<=c_s N_s(k).

For h=J^s g,

    D^2J^s(W.Dg)=W.D D^2h+T_W D^2g
                   +2J^s(DW D^2g)+J^s(D^2W Dg).         (19)

The first term has energy cost at most(4/5)c_s N_s(k)P(h)^2. Apply(17) to the second and(18) to the last two. For the last term use v=Dg and f=D^2W. Every second derivative of k is centrally odd, so the independently proved Mellin estimate gives

    ||omega J^s D^2W||_2<= (9/5)||omega D^2 J^s k||_2
                         <=(9/5)N_s(k).                (20)

Thus the full top energy cost, in units N_s(k)N_s(g)^2/sqrt(s), is at most

    (4/5)(3/10)+(3/10)(1+142s)+(19/5)(1+44s)
       <=109.24.                                       (21)

Here c_s sqrt(s)<3/10, and s<=1/2. The lower gradient and L2 components cost at most1.3 and0.3 in the same units. The H component is handled separately by

    J^s(W.Dg)=div J^s(Wg).

Equation(18) and Cauchy-Schwarz give cost at mostsqrt(b0)/2<1/2 after its norm weight is included. The total is less than111.34<128. Therefore

    |Re (J^s(W.Dg),J^s g)_E2|
       <=128 N_s(k)N_s(g)^2/sqrt(s).                    (22)

Equation(22) is initially an energy-form inequality on the smooth graph core. It does not assert that W.D is a bounded map from N_s to N_s, or that its displayed inner product is separately defined for every N_s input. The realization below passes this core inequality to semigroup bounds. This proof uses only N_s(k), not D^3W. Combining(13),(22) with the assumed E2 energy inequality proves(1) on smooth functions.

## 4. Realization, surjectivity and injectivity

First J^s extends to an isometric bijection N_s->E2. To check that its range is dense, apply J^-s to a smooth compact core function. The result is Schwartz and has the same parity. Its smooth cutoff approximations converge in Schwartz topology; applying J^s preserves that topology. Schwartz convergence implies E2 convergence, including H convergence by the parity Hardy inequality ||f||_H<=|| |X|f||_2. This proves density and then the assertion by completion. Equation(7) also yields E2(g)<=3N_s(g).

Choose k_n in the smooth compact parity core converging to k in N_s. Then W_n=U[k_n] converges to W in W^(1,infinity), by(15) and the corresponding zero-derivative embedding. Each W_n is smooth, divergence free, vanishes at zero, and has bounded derivatives with sufficient decay. Its complete transport flow acts strongly continuously on E2: the field grows at most linearly, its derivative is bounded, and its higher derivatives satisfy the weighted bounds needed by the chain rule. This is the same direct flow construction as in the E2 base theorem. The coupling Q is bounded there.

For each fixed n, conjugation by J^s gives a bounded perturbation on E2, by the smooth version of(13) applied to u+W_n. The required smooth coefficient constants are finite, although no uniform higher-derivative bounds in n are claimed. The fixed Q commutator is already covered by(11)-(13). Hence A_(k_n) generates a strongly continuous semigroup S_n on N_s. Smooth cutoff approximation justifies the integrations above on a graph core, so(1) bounds S_n with its stated rate.

On any finite time interval and for fixed initial f in N_s, S_n(t)f is Cauchy in C_t L2. Indeed the difference equation has forcing (W_n-W_m).D S_m(t)f. Its L2 norm tends uniformly to zero: the velocity difference converges uniformly and the gradient is bounded by the uniform N_s estimate. The ordinary L2 transport estimate has constants independent of n,m, since div W_n=0 and Q is a fixed bounded L2 operator. Gronwall proves the assertion.

The N_s bounds give weak compactness. Every weak subsequential limit equals this L2 limit, so it defines S(t)f in N_s with the same decay, by lower semicontinuity. Uniqueness of the L2 equation gives the semigroup law. At zero, L2 continuity plus the N_s bound imply weak N_s convergence to f. The bound in(1) gives limsup N_s(S(t)f)<=N_s(f), hence the Hilbert norm identity gives strong N_s continuity.

For clarity about the domain, the complete globally Lipschitz field cX+u+W defines the usual strongly continuous L2 transport group. Its generator is the maximal distributional transport operator: this follows by mollification and radial cutoff, since the field has at most linear growth and bounded first derivative. Adding the fixed bounded Q preserves that characterization. The N_s semigroup is its restriction, by the L2 uniqueness just used. Thus its generator is the part of that L2 generator with both h and A_k h in N_s, exactly the maximal distributional domain asserted above. Equivalently, apply the L2 Duhamel identity to any h with A_k h in N_s; the integral of S(t)A_k h then converges in N_s and identifies its N_s derivative.

For positive rate beta, -int_0^infinity S(t)f dt converges in N_s and solves A_k h=f on the generator domain, with norm at most beta^-1. Conversely A_k h=0 makes S(t)h constant, and exponential decay forces h=0. This proves onto and injectivity, not just an a priori inequality.

## 5. Normalization, complete ball and nonlinear contraction

The Fourier estimates give N_s subset H^(2+s) subset C^1. Write mu=partial_y(cY+u_2)(0). First-order Taylor expansion of A_k h=f at zero, using the parity and U[h](0)=0, gives

    f_y(0)=(mu-1+c[k])h_y(0)+a0 c[h].                   (23)

Only C^1 regularity is needed: the field vanishes at zero, so its product with Dh has its linear term determined by Dh(0). The background normalization makes mu=1. Therefore c[k]=0 implies f_y(0)=0 if and only if c[h]=0.

For(2), the background loss is at most2^22 s=1/64 and the rough loss is128r/sqrt(s)=1/64. This gives beta>=11/160>1/20. Also d=||DU[k]||_infinity<=c_s r<2^-13. The low H inverse has norm at most

    K_L=(19/5-d)^-1<1.

Here is a construction and consistency proof; no H solution is assumed to lie in L2. For each smooth k_n used in section4, let d_n=||DU[k_n]||_infinity. On the common smooth graph core the exact negative-order identity is

    Re <U[k_n].Dg,g>_H
       = -int D_i Phi D_i U_j[k_n] D_j Phi,
    Phi=(-Delta)^-1 g.

Thus its absolute value is at most d_n||g||_H^2. Add the background H decay19/5. The resulting low energy inequality extends to the high generator domain by graph approximation, since the inclusions N_s -> H and A_(k_n)N_s -> H are continuous in the graph norm. Differentiate the H norm of a semigroup orbit starting in that domain and integrate. Approximation of arbitrary high initial data then gives

    ||S_n(t)f||_H <= exp[-(19/5-d_n)t]||f||_H,
    f in N_s.

The uniform N_s bounds and the C_t L2 convergence from section4 identify all weak H limits. Weak lower semicontinuity and d_n -> d give this bound for S(t)f. The space N_s is dense in H, since it contains its defining compact smooth parity core. Therefore S(t) extends uniquely to a bounded semigroup S_H(t) on H with the same decay. Strong continuity at zero follows first on N_s from its strong high continuity and then on all of H by density and the uniform finite-time bound. The integral -int_0^infinity S_H(t)f dt gives a surjective inverse on its generator domain with bound K_L; an invariant orbit and decay prove injectivity.

This low semigroup agrees with the L2 semigroup on H cap L2. To justify the needed simultaneous density, first approximate the Fourier transform on annuli away from zero by smooth compact functions, preserving parity, in both weighted L2(|xi|^-2 dxi) and ordinary L2. Their inverse transforms are Schwartz. Smooth parity-preserving spatial cutoffs approximate each of them in L2 and H, the latter by ||g||_H<=||r g||_2. Hence a common core is dense in the intersection with the sum norm. The two semigroups agree on that core by their high construction, and their bounds pass this agreement to the intersection. Limits in H and L2 represent the same distribution because pairing with a compact smooth test function is continuous in either topology.

In particular, suppose w in N_s and A_k w=f in H cap L2 distributionally. The maximal L2 realization places w in its generator domain. Its integrated orbit identity reads

    S_2(t)w-w=int_0^t S_2(tau)f dtau.

By the intersection consistency, both sides equal the corresponding H expressions as distributions; the H integral exists by strong continuity. Thus this identity holds in H. Dividing by t and taking t down to zero shows w belongs to the low generator domain with A_(k,H)w=f. This is exactly the domain statement needed for the contraction difference below.

Let B_r={k:N_s(k)<=r,c[k]=0} with the H metric. This metric space is complete. A Cauchy sequence converges in H; weak compactness of its bounded N_s ball identifies the same limit in N_s, lower semicontinuity retains its radius, and continuity of c on N_s retains c=0. Define T(k)=-A_k^-1 R. The exact reference normalization gives R_y(0)=0, so(23) puts T(k) in c=0. The high inverse and N_s(R)<=r/20 put T(k) in B_r.

For k,l in B_r,

    A_k(T(k)-T(l))=-U[k-l].D T(l).

The streamfunction identity U[z].Dv=-div(psi[z] D^perp v), and ||psi[z]||_2<=||z||_H, imply

    ||U[z].Dv||_H<=||z||_H ||Dv||_infinity.

The difference w=T(k)-T(l) belongs to N_s. Its forcing belongs to H by this bilinear estimate and to L2 since U[k-l] is bounded and D T(l) is in L2. The low-domain argument above therefore applies to w. Consequently T is a contraction with constant at mostK_L c_s r<2^-13. Its fixed point h satisfies Lh+U[h].Dh=-R and c[h]=0. Since c remains fixed, this is precisely F(rho_bar+h)=0. Conversely any solution in B_r is a fixed point, which proves the stated uniqueness.

## 6. One compatible estimate for density, moment and strain

The same space, without an extra regularity assumption, controls the requested quantities. For the explicit s in(2), put delta=s/2=2^-29, p=2^31 and kappa=p+4, and define

    Mloc(h)=[int_(|X|<1) |X|^-kappa |h(X)-h_y(0)y|^p dX]^(1/p).

Fourier Cauchy-Schwarz gives ||h||_(C^(1/2))<=N_s(h), where the norm is supremum plus seminorm. Indeed the supremum constant is at most1/(2sqrt(pi)), and the half-Holder constant is at most1/2. Similarly

    [Dh]_(C^delta)<=2^-delta sqrt(Beta(2+delta,s-delta)/pi) N_s(h)
                   <=s^-1/2 N_s(h).

The last inequality uses Beta(2+delta,s-delta)<=1/(s-delta)=2/s and2/pi<1. Taylor's integral remainder is at most[Dh]_(C^delta)|X|^(1+delta)/(1+delta). Since p delta=4, the moment integral is2pi/(p delta-2)=pi, and pi^(1/p)<2. Thus Mloc(h)<=2s^-1/2 N_s(h). Also |c[h]|<=c_s N_s(h)<s^-1/2 N_s(h), and ||h||_H<=N_s(h). Hence

    ||h||_H+||h||_(C^(1/2))+Mloc(h)+|c[h]|
       <=2^16 N_s(h)<=20*2^16 N_s(A_k h).               (24)

The first inequality in(24) holds for every h in N_s. The second is asserted for N_s(k)<=r and h in the maximal N_s generator domain D(A_k), with parameters(2). This controls h itself in a direct Holder norm. The very large p records the small fractional regularity used by this conservative closure argument. It is a finite, explicit exponent. It is compatible with the local transport moment window: kappa-p-lambda-1=3-lambda>0 for the certified state, and p(1+delta)+2-kappa=2>0.

## 7. Scaling and tail scope

If the reference has the nonzero uniform leading profile r^gamma Theta0(theta), gamma=1/c<1, corrections in N_s tend uniformly to zero at infinity, by uniform continuity and L2 integrability. They preserve c and the entire Theta0. The scaling transformation t rho(X/t) changes Theta0 to t^(1-gamma)Theta0. Hence no nontrivial scaling stays in the same affine correction class. This also excludes the infinitesimal direction without differentiating an unproved tail remainder: if K=rho-r partial_r rho belonged to N_s, then K would tend uniformly to zero. Sublinear growth and integration of partial_r(rho/r)=-K/r^2 give rho(r,theta)=r int_r^infinity K(t,theta)/t^2 dt, which would tend uniformly to zero, contrary to the nonzero growing leading profile.

For a precise optional augmented phase, fix a radial smooth cutoff chi_inf, zero on r<=1 and one on r>=2, and a number0<gamma<1. The leading-tail coordinate space is L2 of the parity angular functions on the circle. Form the direct sum Z_gamma={chi_inf r^gamma theta(theta_angle)+h: theta in L2(S1), h in N_s} with norm ||theta||_L2+N_s(h). The decomposition is unique because a nonzero growing homogeneous angular term is not in L2(R2). The coordinate functional P(theta)=<theta-Theta0,Theta0>_L2 is bounded on this space, and its derivative along the explicit scaled leading coordinate is(1-gamma)||Theta0||_2^2>0. This establishes only the phase-coordinate transversality; no nonlinear inverse or differentiable scaling action on every rough Z_gamma element is asserted. The nonlinear theorem above uses the fixed coordinate Theta0, not this enlarged space.

This theorem freezes the exponent and leading angular function. It does not claim to allow their logarithmic or functional variations inside N_s. A tail-completed reference can be treated if its actual residual belongs to N_s and all the explicit background hypotheses are independently reverified. The finite-family nonexistence theorem and the original growing residual remain fully consistent with this conditional result.

## 8. A certified route from ordinary derivative residual norms to N_s

No uniform replacement of N_s(f) by E2(f) is asserted merely because s is small. The following quantitative bound is sufficient. If E=E2(f) and Q=||omega D^3f||_2 are finite, then

    N_s(f)<=E^(1-s)(2Q^2+16410E^2)^(s/2)+34sE.            (25)

For E=0 the assertion means f=0. To prove it for E>0, introduce the Hilbert-valued function

    T f=(omega D^2f,128Df,512f,512sqrt(b0) Lambda^-1 f).

Its L2 norm is E. Its H1 norm squared is E^2 plus the squared L2 norms of the derivatives of these four entries. Since ||D omega||_infinity<=2,

    ||D(omega D^2f)||_2^2<=2Q^2+8||D^2f||_2^2.

The other three derivative contributions are B||D^2f||_2^2,16B||Df||_2^2 and16Bb0||f||_2^2. Hence

    ||Tf||_H1^2<=2Q^2+(B+25+b0)E^2<2Q^2+16410E^2.

Fourier Holder interpolation gives ||J^s Tf||_2<=||Tf||_2^(1-s)||Tf||_H1^s. The only commutator between T and J^s is its first entry, bounded by34s||D^2f||_2<=34sE. This proves(25), first on the core and then by completion. It also proves that E3 membership implies N_s membership for every 0<s<=1/2.

In terms of the earlier E3, the weaker convenient bound is

    N_s(f)<=2^(s/2) E2(f)^(1-s) E3(f)^s+34sE2(f).         (26)

If Q<=2^(173/2)E2(f), then E3(f)<=2^87E2(f), so the multiplier in(26) is at most2^(175s/2)+34s. Any numerical use must certify the stated Q bound or use(25) with actual certified E,Q; finite-point comparisons of an evaluator do not certify these norms.

For0<s<1/34, the same commutator also gives the useful reverse comparison

    N_s(f)>=(1-34s)E2(f).                                  (27)

Indeed unweighted Bessel expansion gives ||Tf||_2<=||J^s Tf||_2. The sole commutator between T and J^s is again its weighted Hessian entry, so

    E2(f)<=||J^s Tf||_2<=N_s(f)+34s||D^2f||_2
            <=N_s(f)+34s E2(f).

This proves(27) on the smooth core, and it extends by completion using the already established E2<=3N_s inclusion. It also applies directly to every smooth residual with finite E,Q. In particular, certified lower bounds for any square sum of ordinary E2 components give a rigorous N_s lower bound after multiplication by1-34s. Equality of E2 and N_s is not asserted.
