# Final check of the strain gap and the scattering interface

Status: CONFIRMED in A3249 after the complete existing A and C comparisons. This is a final-phase reconstruction of the three derivative conclusions of A476-A477, with every hypothesis retained. No new nonexistence theorem or singularity-set verdict is claimed.

## 1. Statements and dependencies

Let J(y1,y2,y3)=(-y2,y1,0), fix any finite real omega and 0<c<1, and put A=cI-omega J. Assume U in C2(R3;R3) and P in C1(R3) satisfy pointwise

    (1-c)U+(Ay+U).grad U+omega JU+grad P=0, div U=0,
    M=sup_R3 |U|<infinity.

Write B=Ay+U, Omega=curl U, S=(DU+DU^T)/2 and use the operator norm for matrices. Set

    Lambda=limsup_(|y|->infinity) lambda_max(S(y)),
    m(r)=sup_(|y|>=r)||DU(y)||.

The precise existing conclusions checked here are these.

1. If Lambda<1, then DU is globally bounded. For every 0<kappa<1-Lambda there are finite profile-dependent C,R such that, for |y|>=R,

       |Omega(y)|<=C |y|^(-kappa/c),
       ||DU(y)||<=C (|y|^(-kappa/c) log|y|+|y|^(-1)).

2. The following conditions are equivalent: DU tends uniformly to zero; Lambda<1; Lambda=0; integral_1^infinity m(r)dr/r is finite; and DU has some positive power rate at infinity. In particular neither Lambda nor limsup infinity ||DU|| can lie strictly between zero and one.
3. If also 1/3<c<1 and U(R .) tends to zero in distributions, those conditions are equivalent to the natural rate ||DU(y)||<=C(1+|y|)^(-1/c).

All constants are allowed to depend on c, omega, U and a C2 norm on a fixed compact annulus. No bound uniform in the size of omega is asserted. No pressure normalization, helicity sign, symmetry or finite-energy assumption is used.

The analytic dependency for item1 is the localized proposition in the captured gradient proof, Sections3-6: a bounded C2 profile with globally bounded gradient and |Omega(y)|<=C|y|^(-kappa/c), 0<kappa<=1, has the stated gradient rate. Those four sections were reread completely, including the kernel sign, the non-solenoidal cutoff, the moving-ball estimate and the final conversion. Sections2-3 below reproduce the critical steps rather than assuming decay of the gradient from decay of vorticity alone. The dependencies for item3 are scattering conjugacy A209 and scattering tail A210, both reread completely. They retain the Dini hypothesis.

## 2. Exterior transport, bounded gradient and the gap

The curl of momentum gives, without differentiating P beyond its distributional mixed derivatives,

    B.grad Omega=DU Omega-Omega-omega J Omega,
    B.grad|Omega|^2=2 Omega.(S-I)Omega.

Trace zero implies lambda_max(S)>=0. Hence Lambda>=0. Fix kappa as in item1. Outside a sufficiently large ball, lambda_max(S)<=1-kappa. If lambda1>=lambda2>=lambda3 are the eigenvalues of S, then lambda3>=-2lambda1; therefore ||S||<=2 there. Along a B characteristic in that region,

    d_s |Omega(Phi_s y)|^2<=-2kappa |Omega(Phi_s y)|^2.

B has at most linear growth, so its C1 flow is complete in both time directions. Choose R1 larger than the strain radius and 2M/c. At r=|Phi_s y|>=R1,

    cr-M<=r'<=cr+M.

The reverse radial derivative is at most -cr/2. Every exterior point has a finite backward crossing of r=R1, and the forward orbit cannot cross that sphere inward. If t is the elapsed time from the crossing, then r(t)<=(R1+M/c)exp(ct). Integrating the vorticity inequality gives the first bound in item1, uniformly over the crossing sphere. The skew part of DU has norm |Omega|/2. The strain bound and vorticity bound thus bound DU outside; continuity bounds it on the remaining compact set.

The localized proposition now gives the second bound. Absorbing the logarithm into a smaller positive power gives item2 in one direction. Conversely, a positive power bound gives the Dini integral. Finiteness of the Dini integral forces m(r) to tend to zero because m is nonnegative and nonincreasing. Gradient decay gives Lambda=0, and Lambda=0 gives Lambda<1. This proves all equivalences. If either stated limsup were in (0,1), the equivalences would force it to be zero, proving the gap. Infinite limsup values are allowed.

## 3. Why the local gradient estimate closes

Put tau=T-t, s=-log tau, Q_s=exp(omega sJ), and y=exp(sA)x. The physical Euler field and vorticity satisfy

    u(x,t)=tau^(-(1-c))Q_s U(y),
    grad u=tau^(-1)Q_s DU(y)Q_s^T,
    xi=tau^(-1)Q_s Omega(y),
    (partial_t+u.grad)xi=(grad u)xi.

On a fixed annulus away from x=0, the hypotheses just obtained give

    |u|<=M tau^(-(1-c)), ||grad u||<=C1/tau,
    |xi|<=w(t)=C tau^(-(1-kappa)).

Both velocity and w are integrable in time at T. A smooth fixed-annulus cutoff chi0 gives v=BS(xi chi0) and h=u-v, where

    BS f=(1/(4pi)) integral f(z) cross (x-z)/|x-z|^3 dz.

With N(x)=1/(4pi|x|), this sign means BS f=curl(N*f) and curl BS f=f+grad(N*div f). Thus h is harmonic where chi0=1. It need not be curl free. Interior harmonic estimates bound Dh and D2h by C Z(t), with Z=tau^(-(1-c))+w. This accounts explicitly for the cutoff's divergence and the remote part of the velocity.

The derivative of BS has degree -3, zero spherical mean and a local constant matrix term. Splitting its integral at epsilon and radius1, subtracting f(x) in the inner ball, gives

    |D BS f|<=C(epsilon^(1/2)[f]_(1/2)
                      +||f||_infinity(1+log(1/epsilon))+||f||_1).

The difference of kernels at distance q is O(q r^-4). Its integral against a Holder-1/2 difference on r>=2q is O(q^(1/2)); the near balls obey the same bound. Consequently [D BS f]_(1/2)<=C[f]_(1/2). For nested balls E and E+d, a cutoff supported in E+d supplies the local estimates with additional cost Cw d^(-1/2)(1+log(1/d)). Extension by zero is legitimate because the cutoff vanishes at the boundary.

For |xstar|=1 use B(t)=B(xstar,1/4+L tau^c), L=2M/c, beginning sufficiently close to T. If M=0 then U=0 and there is nothing to prove. Backward paths ending in B(t) move at most

    delta(rho,t)=(M/c)((T-rho)^c-(T-t)^c).

Their earlier-time ball E(rho,t)=B(xstar,1/4+L tau^c+delta) satisfies the exact relation E(rho,t)+delta=B(rho). Also delta>=M(t-rho) after T-rho<=1. Thus the local cutoff cost has the integrable time kernel ell(q)=q^(-1/2)(1+|log q|), rather than an uncontrolled future-domain seminorm.

Writing Theta(t)=[xi(t)]_(1/2,B(t)), paired-path transport and the convexity of these balls give

    Theta(t)<=((T-t0)/tau)^(C1/2)Theta(t0)
      +integral_(t0)^t ((T-rho)/tau)^(C1/2)
       [(C1/(T-rho)+Cw)Theta(rho)+Cw^2 ell(t-rho)+CwZ]drho.

Theta is finite on compact time intervals and Borel, being the supremum of continuous difference quotients over moving open balls. Multiply by tau^(C1/2). The inhomogeneous term is bounded by C tau^-2, while the remaining coefficient is C1/(T-rho)+Cw(rho). Gronwall and integral w<infinity give Theta<=C tau^-N for a finite N (the captured proof takes N=2+3C1/2). Its initial constant is uniform in xstar by one compact-annulus C2 norm.

On a smaller fixed ball set epsilon=tau^(2N). The local logarithmic estimate and harmonic bound give

    ||grad u(xstar,t)||<=C[1+tau^(-(1-kappa))(1+log(1/tau))
                            +tau^(-(1-c))].

Every sufficiently large y corresponds to such a unit xstar with tau=|y|^(-1/c). Multiplying by tau proves item1. The extra tau term is bounded by |y|^-1 because c<1. This confirms the critical dependency without replacing vorticity control by an invalid L-infinity singular-integral estimate.

## 4. Scattering and removal of the logarithm

Under the Dini condition, A209 supplies a proper continuous scattering map Ssc with |Ssc(y)-y|<=M/c, zero fiber K compact and null, and a C1 volume-preserving diffeomorphism off K. Its intertwining law and DSsc->I are valid for every fixed finite omega. Differentiability or injectivity without the Dini condition is not used. For injectivity, if two normalized trajectories had equal nonzero scattering limits, their difference D(t) would approach zero but satisfy |D'|<=m(C exp(ct))|D| for large t; the integrable coefficient gives a contradictory positive lower bound.

A210 pushes vorticity forward by W(Ssc y)=DSsc(y)Omega(y). The transport identity gives exact rotated homogeneity and |W(z)|<=C|z|^(-1/c). The extension of div W=0 across the collapsed fiber is essential: for a test constant near zero its composition with Ssc is constant on a neighborhood of K; for the remaining test vanishing at zero the cutoff error is O(epsilon^(3-1/c)). It tends to zero because c>1/3. No point source is removed without proof.

Here 1<1/c<3. The Biot-Savart integral converges both at zero and infinity, and the small-o comparison between Omega and W gives the velocity tail. The harmonic constant in recovering U is eliminated by boundedness and distributional dilation decay. These arguments, with exactly the stated range, yield

    |Omega(y)|<=C |y|^(-1/c),
    |U(y)|<=C |y|^(-(1-c)/c).

Therefore the physical u and xi are uniformly bounded on every fixed exterior annulus close to T. No global physical bound near x=0 is asserted. In the local estimates of Section3, w and Z can now be chosen constant. Moreover

    G(t)=sup_(|x|>=1/2)||grad u(x,t)||,
    integral_(t0)^T G(t)dt
      =(1/c) integral_(exp(cs0)/2)^infinity m(r)dr/r<infinity.

The same shrinking balls and connecting path segments lie in this controlled annulus. Paired-path distances now have a uniform factor exp(integral G). Repeating the Holder transport estimate gives

    Theta(t)<=C Theta(t0)+C integral_(t0)^t
                     [(G(rho)+1)Theta(rho)+ell(t-rho)+1]drho.

Integrability of G and ell and Gronwall give a uniform Theta. The local elliptic bound with fixed epsilon=1 gives a uniform physical gradient on the unit sphere. Conversion to y gives ||DU(y)||<=C|y|^(-1/c). Conversely that rate gives a positive power rate, so item3 follows.

## 5. Scope and audit exclusions

This is a recheck of the bounded-profile strain theorem and its conditional natural-rate corollary. Uniform decay of U implies boundedness and the required distributional blow-down, but no step here proves Lambda<1, gradient decay or the Dini condition from uniform velocity decay. No result here makes a gradient budget automatic or proves U=0. The physical singularity-set identities in the old proof are not needed for these three statements and receive no new verdict in this focused recheck. No computation, numerical fitting, pressure normalization or restriction to small omega is part of the argument.
