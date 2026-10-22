# Type I tests and the scope of two boundary-profile papers

Date:2026-10-20. Status: independent mathematical audit of the lead's draft notes/lit_C.md, with independently retrieved primary texts. The Type I conclusions are conditional necessary diagnostics for a class A profile. No profile is constructed or excluded.

## Exact hypotheses and notation

Assume a smooth B2 profile in class A, with beta>=2, nu=1/beta, nonzero a0, V=U-U(0), W=beta X+V and c=1+beta/2. The previously proved class A consequences used here are

    U=O(1+r^(1-nu)), DU=O(r^-nu),
    grad Theta=O(r^-2nu),
    Omega=r^-nu(a(theta)+o(1)) uniformly in angle,

where a is continuous and not identically zero. Smoothness supplies bounds on compact sets. The temperature jet is Theta=a0*x^2+O(r^3), the center gradient is A=DU(0)=diag(-c,c), and W(0)=0. Here DU acts on column tangent vectors. The primary paper writes its gradient indices in the transposed order; at the center the diagonal matrix is the same.

The physical fields use the moving material center and tau=T-t:

    u=tau^(beta-1) U(X), theta=tau^(beta-2)Theta(X),
    X=(z-z_c(t))/tau^beta,
    z_c(t)=z_*-(U(0)/beta)tau^beta.

Additive constant observer choices do not affect the gradient, Hessian, or unboundedness statements below. In the conventional momentum equation with buoyancy +theta e2, replace theta by -theta to match the prompt's negative-curl convention. Reversing theta reverses both direction vectors below and leaves every scalar tested here unchanged.

## 1. Center pressure and quantitative Type I conditions

The momentum profile equation has the form

    (1-beta)U+W.grad U+grad Pi = -Theta e2.

Indeed its curl vanishes exactly by the vorticity profile equation with Omega=-curl U, so the simply connected full plane admits such a scalar pressure. A possible time-dependent spatially uniform gradient also leaves its Hessian unchanged.

Differentiate at0. The term involving D2U times W vanishes there; the buoyancy derivative vanishes since grad Theta(0)=0. Thus

    D2Pi(0)=-(1-beta)A-A(beta I+A)=-(A+A^2)
           =diag(c-c^2,-c-c^2).                         (1)

Put q=grad^perp Theta=(-Theta_y,Theta_x), xi=q/|q|, zeta=A(X)q/|A(X)q|, alpha=xi.A(X)xi and rho=xi.D2Pi(X)xi. These are defined on all sufficiently small points X=s(1,1), s>0: q=(O(s^2),2a0*s+O(s^2)), and Aq is nonzero. As s decreases to0,

    xi -> sign(a0)e2, zeta -> sign(a0)e2,
    zeta.D2Pi xi -> -c(c+1),
    |A xi|^2-2alpha^2-rho -> c.                       (2)

Physical gradient and pressure Hessian scale as tau^-1 and tau^-2, respectively. Every fixed ball about z_* contains these moving-center ray points for t sufficiently close to T. Continuity on their punctured neighborhoods implies the same lower bounds for essential suprema, even though xi is undefined exactly at0. Therefore the two Chae-Constantin quantities in Theorem2.1(2.3),(2.4), and their local Theorem2.2 counterparts(2.7),(2.8), have scaled limsups at least c(c+1)>=6 and c>=2. Both strict upper thresholds2 fail, including the equality case beta=2 for the second quantity.

The integral conditions fail as well. For either nonnegative norm Q(t) in those conditions, (2) gives Q(t)>=c/(T-t)^2 for t>=t1. For tau1=T-t1,

    integral_t1^t integral_t1^s Q(v)dv ds
      >=c[log(tau1/tau)+tau/tau1-1]
      >=c log(tau1/tau)-c.

Hence their outer integrand is bounded below by exp(-c)*tau1^c*tau^(1-c). Its integral diverges for every c>=2. Enlarging the inner integration region only improves this lower bound.

The printed local Theorem2.2 on p10 of arXiv:2103.10672v1 says system(E), although it is in the Boussinesq section and uses Boussinesq quantities and thresholds; equation(2.5) also prints zero lower limits in its two inner integrals, unlike(2.6). The nonapplication above holds even when reading it as the intended local Boussinesq result with all inner lower limits T-r. It does not rely on silently treating the typographical labels as a theorem about this profile.

## 2. Other Type I tests and their data spaces

For all tau>0,

    tau ||grad u||_infinity >= ||A|| >= c>=2,
    ||grad theta||_infinity=tau^-2 ||grad Theta||_infinity,

where the latter profile norm is finite and strictly positive. Consequently the strict bound in Chae-Wolf Theorem1.2(i) fails. The weighted time integral in(ii) diverges logarithmically. Theorem1.4's logarithmically strengthened quantity tends to infinity.

The vorticity is smooth, bounded, decaying and nonzero. Its homogeneous Besov Bdot^0_(infinity,infinity) seminorm is finite and positive. Boundedness gives finiteness by the uniformly integrable Littlewood-Paley kernels. If every annular Fourier block vanished, the Fourier transform would be supported at0, so Omega would be a polynomial; boundedness and decay would then make it zero, a contradiction. Arbitrary spatial dilations preserve this seminorm up to constants uniform in the dilation factor. To see this, a rescaled dyadic annulus intersects only a fixed number of neighboring annuli after choosing the nearest integer dyadic shift; the partition of unity and uniformly bounded convolution kernels give both inequalities by interchanging the two decompositions. Translation has no effect. It follows that

    ||omega(t)||_Bdot^0 >= C^-1 tau^-1 ||Omega||_Bdot^0.

Its time integral diverges, so both alternatives(iii),(iv) fail already in their vorticity terms. For a fixed dyadic definition the seminorm is exactly invariant only under dyadic dilations; literal invariance for every dilation is not needed and is not claimed.

The global Sobolev hypotheses are unavailable independently of these quantitative failures. Theta is in no finite Lp by the previously established transported-temperature result. U is unbounded: choose a closed angle interval I on which the continuous nonzero tail a has one strict sign. On its annular sector D_R={R<r<2R,theta in I}, uniform tail convergence gives

    |integral_D_R Omega| >= C R^(2-nu).

Stokes' theorem gives the same magnitude for the oriented circulation of U. Since length(partial D_R)<=C_I R,

    sup_(partial D_R)|U| >= C'R^(1-nu) -> infinity.

Thus the inhomogeneous W2q(R2) velocity assumption in Chae-Constantin also fails, since q>2 implies bounded velocity. No cancellation from a different tail sector enters this local contour argument.

The qualitative local velocity hypotheses of Chae-Constantin Theorem2.2 do hold. Smoothness gives C([T-r,T);W2q(B)) away from the final time. On a fixed ball B(z_*,rho), the moving-center formula and sublinear bound give

    |u| <= C(tau^(beta-1)+rho^(1-nu)),

after increasing C for the bounded center displacement. This gives a uniform local L2 bound and time-integrability of the local Linfinity velocity. The quantitative conditions still fail by section1. These facts neither admit nor exclude a profile. Conditional on its existence, both gradient quantities have Type I upper bounds and the velocity-gradient constant is at least c.

## 3. Zhang: exact conditions and exponent translation

Primary source: Qi S. Zhang, arXiv:2306.09515v5, Proposition2.3, pp20-22, and Remark2.6, p25. Proposition2.3 concerns the upper half-plane, with a no-penetration condition on its horizontal base. Its buoyancy is H^2. To avoid the conflicting beta notation, denote its parameters by alpha_Z,b_Z. It assumes alpha_Z<0, 0<b_Z<|alpha_Z| and

    2b_Z=1-alpha_Z.

Its physical ansatz is v=(1-t)^(-alpha_Z)V(z/(1-t)^(1-alpha_Z)) and h=(1-t)^(-alpha_Z-b_Z)H, with buoyancy h^2. For the B2 scaling the translation is

    alpha_Z=1-beta, b_Z=beta/2.

The exponent relation is exactly the Boussinesq balance, and 0<b_Z<|alpha_Z| is equivalent to beta>2. Thus the exponent relation is not an additional obstruction in the beta>2 regime, provided the temperature admits the required squared representation. At beta=2 its strict parameter inequality fails. A global smooth signed square root of a general class A temperature is not established; in subclass G with a0>0 it is supplied by sqrt(a0)*xi.

Part(i) additionally assumes first-quadrant signs V1<0,V2>0,partial_1(H^2)>0, sublinear V, bounded angular coefficients in the stated vorticity/radial-velocity tails, and a strict inequality between sup_r W(r,theta2) and sup_r W(r,theta1). The latter is not pointwise angular monotonicity. It also requires W>=0 and a strict maximum over the entire closed sector, together with W(z0)>partial_1(H^2)(z0). The statement does not itself label z0 an interior sector point. Part(ii) supplies a different set of rectangle, maximum, forcing-dominance and transport-sign assumptions.

The horizontal wall, tangential oddness of H and velocity component, and these sign/maximum assumptions do not follow from B2. The B2 invariant axis is the vertical x=0 line; treating it as the wall after a rotation changes which coordinate is tangential and does not supply Zhang's symmetry and forcing hypotheses. Accordingly this proposition does not decide the full B2 class. Remark2.6 explicitly limits its scope with respect to asymptotically self-similar solutions. No claim that the theorem's proof is false is made here.

## 4. Reported numerical boundary profiles

Primary source: Wang et al., arXiv:2509.14185v1, Figure2f, Figure3b, Methods equation(2), pp12-13, and the lambda-inference formula on p16. Their ansatz gives beta=1+lambda. Their reported lambda values translate as follows:

| family | lambda as printed | beta |
|---|---:|---:|
| stable |1.9205599746927|2.9205599746927|
| first unstable |1.3990961221852|2.3990961221852|
| second unstable |1.2523481636489|2.2523481636489|
| third unstable |1.1842500861997|2.1842500861997|
| fourth, labelled unvalidated |1.1448833556188|2.1448833556188|

The printed inference lambda=-3-2partial_1U1(0), with partial_1U1(0)=-c, becomes c=(lambda+3)/2=1+beta/2. Their vorticity exponent1/(1+lambda) is nu. These parameter translations do not depend on the sign used to name scalar vorticity.

Figure3b reports log10 maximum Boussinesq residuals from -8.178 to -7.020, including the separately unvalidated fourth case. These are the authors' numerical diagnostics, not independently reproduced bounds. The paper describes boundary profiles. Neither the boundary inverse nor small residuals for that boundary problem validate a whole-plane B2 profile. Nothing here validates or refutes the numerical files in that paper, which were not run.

## Audit verdict

CONFIRMED: center pressure Hessian, direction limits, the failure of strict and integral Type I tests, Stokes unboundedness, local qualitative velocity hypotheses, numerical parameter translations, and nonapplication of these cited results to the full B2 class.

REFUTED as literal source descriptions: all-scale exact invariance of the fixed dyadic Besov norm; angular monotonicity and an explicitly interior maximum in Zhang's part(i); the claim that its exponent relation is unavailable for beta>2. Replacing these phrases as above preserves the intended literature conclusion.

OPEN: the underlying class A existence/nonexistence question. The primary PDF files, text extractions and SHA256 metadata are in verification/. No code or numerical source from another lane was executed.

Dependencies: established class A tail and temperature transport results; local profile identities; elementary differentiation, Stokes' theorem, Littlewood-Paley partition arguments and explicit integration. No formal proof build was run.
