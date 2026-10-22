# Arbitrary exact disks, whole-axis flatness and smooth angular tails

Written 2026-10-21T05:08:48.259496+00:00 before packet127 computations. Status: CONFIRMED by independent proof and exact controls 2026-10-21T05:11:24.502518+00:00. Actual Opus169 returned claude-opus-5-5 but NO_AUDIT_TEXT (max_tokens) after160.003245s; focused170followup is running. No model endorsement is claimed. This is a compatibility construction and an exclusion of its own fields as full profiles, not an endpoint for the B2 problem.

## Statement and conventions

Let beta>2, a0>0, R>0 and a cone aperture epsilon0>0 be prescribed. There are smooth full-plane fields Psi, Omega=-Delta Psi, U=(-Psi_y,Psi_x), V=U-U(0), W=beta X+V and Theta such that:

* Psi and Omega are odd in x, Theta is even, Theta(0,y)=0, Omega>0 on x>0 and Theta>0 off the axis.
* V is the canonical relative full-plane inverse, Psi_xy(0)=1+beta/2, Omega_x(0)=4a0/beta and Theta=a0x^2 near the origin.
* Every backward W orbit converges to0, and W.grad Theta=(beta-2)Theta globally.
* Both profile PDEs hold exactly on B_R. Every Cartesian derivative of R_Omega=W.grad Omega+Omega-Theta_x is zero at every point (0,y).
* For alpha=1/beta and every integer k>=0, |D^k U|<=C_k<X>^(1-alpha-k) and |D^k Omega|<=C_k<X>^(-alpha-k). There is a smooth nonzero angular function A with r^alpha Omega(r theta)->A(theta) in C^infinity(S1). Also 0<=Theta<=C<X>^(1-2alpha).
* Outside a compact set the changes to an anisotropic analytic base are confined to cones of the prescribed aperture around the two y directions. Every constructed finite-parameter field fails to be a full B2 profile.

All constants may depend on R, beta, a0, epsilon0 and the finite parameters chosen in the construction. No uniform estimate as R tends to infinity, no convergence to a full profile, and no open neighborhood of the entire axis on which the PDE holds are claimed.

Write lambda=(beta-2)/2, mu=1+3beta/2, c=1+beta/2, q=4a0/beta, alpha=1/beta, m=1-2alpha, D=2-alpha, H(y)=sqrt(1+y^2). For a function of y, S^s means all derivative estimates |f^(j)(y)|<=C_j H(y)^(s-j). A leading term at either infinity includes a remainder in S^(s-alpha), separately on the two ends.

## 1. Reference input and preservation of the prescribed disk

Packet126 proves the following explicit input, using the sign of its Cartesian Laplacian and a quantified C3 cutoff. Put p=(1-alpha)/2, kappa=9c^2/(beta q^2), eta=kappa/L^2 in (0,1], h=3c/(q eta), S0=(1+beta)L^2, B=q S0^(1-p)/(6p) and

    Psi_L=-Bx[L^2+x^2+eta(y-h)^2]^p.

Its cubic Taylor polynomial is P=ell x+cxy-qx^3/6, ell=-qS0/(6p). Choose D0>2R+qR^2/[2(mu-2lambda)]+1. By taking finite L sufficiently large, a smooth compact replacement Psi0 equals P on B_D0, equals Psi_L outside B_(2D0), and has

    Omega0/x>0, W0,1/x>=lambda/2, b'=d_y W0,2(0,y)>=lambda/2,
    b(0)=0, b'(0)=mu, ||DU0||_infinity<infinity.

These are the only compact-cutoff facts needed here. The proof in126 controls every derivative through order3 before imposing the cutoff, so it does not infer signs from pointwise convergence.

For fixed eta>0, the analytic base and the compact replacement obey |partial^nu Psi0|<=C_nu<X>^(D-|nu|). Its coefficients g_n^0=partial_x^n Psi0(0,y)/n! for odd n satisfy g_n^0 in S^(D-n), with leading powers and remainder gaining alpha. The base has a homogeneous smooth limit -Bx(x^2+eta y^2)^p on every compact annulus. Its first relative error is O(r^-1), including derivatives; compact changes disappear there. On the axis qref=Omega0,x(0,y) is positive, comparable to H^(-1-alpha), and has differentiated leading powers. Moreover b=beta y+S^(1-alpha), b'=beta+S^(-alpha).

All later changes will vanish in the full horizontal band |y|<D0. This is enough to retain the prescribed disk, even though B_D0 itself need not be backward invariant. From any X0 in B_R the polynomial backward orbit is

    x(t)=e^(-lambda t)x0,
    y(t)=e^(-mu t)y0+k x0^2(e^(-2lambda t)-e^(-mu t)),
    k=q/[2(mu-2lambda)].

Its norm is bounded by |x0|+|y0|+k x0^2<2R+kR^2<D0 for all t>=0. It therefore remains an actual orbit after every change supported outside the band. It approaches0 and has e^(lambda t)x(t)=x0. This explicit orbit argument is what permits an arbitrary prescribed R.

## 2. Scalar ODE with symbol control

If b=y B0(y), B0(0)=mu>0, yb(y)>0 away from0 and d(0)>0, then b u'+du=f has exactly one solution bounded at0. To see all smoothness at0, set nu=d(0)/mu and

    j(y)=exp int_0^y [d(s)/B0(s)-nu]/s ds.

The integrand extends smoothly, and

    u(y)=j(y)^(-1) int_0^1 t^(nu-1) j(ty) f(ty)/B0(ty) dt.

Differentiate under this integrable formula. Every nonzero homogeneous solution is proportional to |y|^(-nu)/j and is unbounded. Ordinary ODE continuation extends the bounded solution across both remaining half-lines.

Suppose, on either tail, d=beta d_inf+S^(-alpha) and f in S^(-d_inf-alpha). With t=|y|, b_pm(t)=pm b(pm t), the equation has positive leading drift beta t and

    d(pm t)/b_pm(t)=d_inf/t+S^(-1-alpha).

An integrating factor E=t^d_inf exp[-int_t^infinity(d/b_pm-d_inf/s)ds] equals t^d_inf(1+S^(-alpha)). Then (Eu)'=Ef/b_pm lies in S^(-1-alpha). Its integral to infinity is in S^(-alpha), with every differentiated estimate. Thus u=C_pm |y|^(-d_inf)+S^(-d_inf-alpha). This argument requires alpha>0 and has no logarithmic resonance.

Fix g1=g1^0, b=beta y+g1-g1(0), A1=2beta-b', Lambda=3beta+2 and M=2beta+1. Define

    a2=a0 exp int_0^y (2b'-Lambda)/b ds,
    b Q'+(M-b')Q=2a2.

The apparent quotient singularity is removable since 2b'(0)=Lambda. Thus a2>0 and a2=A_pm|y|^(-1-2alpha)(1+S^(-alpha)), with A_pm>0. The bounded solution Q is positive by its integrating-factor formula on each half-line. Its factor E has exponent 1+alpha; EQ is positive and strictly increasing outward, and its derivative is integrable. Hence Q=Q_pm|y|^(-1-alpha)+S^(-1-2alpha), with Q_pm>0. Consequently K^-1<=Q/qref<=K globally for some finite K and f=Q-qref belongs to S^(-1-alpha).

## 3. All axis coefficients and absence of a symbol obstruction

For formal Taylor coefficients, no convergence of their power series is assumed. Set Psi~sum_{n odd}x^n g_n, Omega~sum_{n odd}x^n w_n and Theta~sum_{k even,k>=2}x^k a_k. Direct Cartesian multiplication of W and gradients gives

    w_n=-g_n''-(n+1)(n+2)g_(n+2),
    b a_k'+[k A1-(beta-2)]a_k
      =sum_{j odd,3<=j<=k-1}[(k-j+1)g_j'a_(k-j+1)-j g_j a_(k-j+1)'],
    b w_n'+(n A1+1)w_n
      =(n+1)a_(n+1)+sum_{j odd,3<=j<=n}[(n-j+1)g_j'w_(n-j+1)-j g_j w_(n-j+1)'].

Start with normalized a2, then w1=Q and g3=-(Q+g1'')/6. Successively solve for a_(n+1), w_n and g_(n+2) for n=3,5,... . At0 the two new zeroth-order coefficients are (n-1)lambda and n lambda+1, both positive. The ODE lemma gives unique global smooth coefficients.

Their symbol orders are a_k in S^(m-k), w_n in S^(-n-alpha) and g_n in S^(D-n), with leading terms and remainders gaining alpha. Inductively the two product forcings have orders m-k-alpha and -n-2alpha, respectively. The temperature term a_(n+1) has the latter order as well. The ODE coefficients at infinity are beta(k-m)+S^(-alpha) and beta(n+alpha)+S^(-alpha), so Section2 applies. Differentiating g_n twice in the Laplacian relation gives the same order as w_n, closing the induction. This proof covers every derivative, and no summation of a divergent formal Taylor series is used.

In the interval |y|<D0, uniqueness identifies a2=a0, Q=q, g3=-q/6 and all the higher target coefficients with zero: those polynomial coefficients satisfy every displayed equation, and the unique bounded solutions at0 extend throughout that interval. Each target-minus-reference stream coefficient therefore vanishes identically throughout |y|<D0.

## 4. Positive conic correction for the first axis equation

Use the moment-balanced cutoff proved in packet122: for every delta>0 there is smooth even compactly supported gamma, equal1 near0 and |gamma|<=1, such that M_gamma(t)=(t^3 gamma(t))''/(6t) lies in [-delta,1]. One construction chooses three separated smooth bumps with signs +,-,+ and coefficients cancelling int_0^infinity t M_gamma and int_0^infinity t^2 M_gamma; taking the two outer bumps sufficiently far makes the negative amplitude arbitrarily small. Twice integrating F''=6t M_gamma, with F=t^3 near0, gives a compact odd F. Its two moment cancellations make F=0 past its support and its bounds give -delta t^3<=F<=t^3. Then gamma=F/t^3. These are the two moments required for a compact stream correction.

Take delta(K-1)<=1/2. For f=Q-qref,

    qref+f M_gamma>=cK qref, cK=min(1/2,1/K)>0.

This follows separately for f>=0 from the lower cutoff bound, and for f<0 from its upper bound. Let T be a support radius of gamma and put

    delta3=-(f(y)x^3/6) gamma(x/[epsilon H(y)]).

Set t=x/(epsilon H), v=H'/H. An exact differentiation gives

    partial_y^2(f gamma(t))
      =f''gamma-(2vf'+v'f)t gamma'+v^2 f(t gamma'+t^2 gamma'').

On its support this is O(H^(-3-alpha)), uniformly for epsilon<=1. Also the reference symbol bound and oddness give

    |Omega0(x,y)/x-qref(y)|<=C x^2 H^(-3-alpha).

Indeed Omega0/x=int_0^1 Omega0,x(tx,y)dt, whose second x derivative is O(H^(-3-alpha)); its first x derivative is0 at0. Therefore with kappa0=epsilon T sufficiently small,

    Omega1/x=Omega0/x+f M_gamma(t)+(x^2/6)partial_y^2(f gamma(t))
             >=c H^(-1-alpha) on |x|<=kappa0 H.

Outside this cone the reference stays positive. The change in W1/x is O(kappa0^2 H^(-alpha)), preserving its positive lower bound. g1, b and U(0) are unchanged; the cubic coefficient becomes precisely g3, while higher axis coefficients remain g_n^0. This correction is a two-dimensional symbol of order D with constants depending on its fixed width. It vanishes throughout |y|<D0.

## 5. Weighted conic Borel realization

For odd n>=5 put d_n=g_n-g_n^0. Choose smooth even chi0, one on [-1,1] and zero outside [-2,2], and form

    F_n=x^n d_n(y) chi0(x/[epsilon_n H(y)]).

For every k<n and epsilon_n<=1, direct product differentiation gives

    max_{|nu|<=k} sup H^(|nu|-D)|partial^nu F_n|
       <=C_(n,k) epsilon_n^(n-k).

To verify the power, write x=epsilon_n H z on the support. An x derivative costs (epsilon_n H)^(-1), a y derivative costs H^(-1), and d_n has order D-n. A derivative with i x differentiations and total order j<=k is bounded by C epsilon_n^(n-i) H^(D-j), which implies the displayed estimate.

Choose epsilon_n decreasing to0, 2epsilon_n<=kappa0, so all these seminorms with k<=n-1 are at most tau 2^(-n). Then Delta=sum F_n converges in every weighted C^k seminorm; for each fixed k only finitely many terms have n<=k. In particular its derivatives through3 are bounded by tau H^(D-|nu|). Oddness and a horizontal mean-value estimate give

    |Delta_X Delta/x|<=2tau H^(-1-alpha),
    |Delta_y/x|<=tau H^(-alpha).

Take tau small relative to the first correction's positive bounds and the flow margin. The final Psi=Psi0+delta3+Delta retains Omega/x>0, W1/x>=gamma>0, unchanged b'>=lambda/2, bounded DU and all required center data. Its changes vanish on |y|<D0. Each cutoff is constant near each axis point, and convergence in C^k for every k identifies the actual stream coefficients with all target g_n.

The cone can be arbitrarily narrow because epsilon and then epsilon_n are chosen arbitrarily small. On its support H and <X> are comparable. Thus the global symbol bounds for U and Omega follow from those of the reference and the displayed weighted estimates.

## 6. Angular limit, full temperature and the residual jets

Every fixed correction has a smooth homogeneous limit on compact annuli, from its coefficient's leading tail and H(ry)/r->|y|. For example r^(-D)F_n(rX) tends on each half-plane to

    x^n d_(n,pm)|y|^(D-n) chi0(x/[epsilon_n|y|]),

extended by zero off its cone. On the cone in an annulus, |y| is bounded away from0, so this extension is smooth. For each fixed derivative order k the tail n>=k+1 is uniformly summable in r by tau sum 2^(-n). First remove that tail, then pass to the limit in the remaining finite sum. This proves C^infinity convergence on annuli to a smooth homogeneous stream Psi_infinity. Consequently A=-Delta Psi_infinity on S1 is the asserted angular vorticity limit. At the x directions all corrections vanish and the anisotropic base has positive right-axis coefficient 2Bp(1+2p+eta); thus A is not zero. Symbol bounds alone would not have justified this angular limit; the coefficient asymptotics and uniform summation do.

The smooth globally Lipschitz W has a complete flow. Its backward trajectories obey |x(-t)|<=e^(-gamma t)|x0|. Since |W2(x,y)-b(y)|<=C|x| and yb(y)>=gamma y^2, they also obey |y(-t)|<=e^(-gamma t)(|y0|+Ct|x0|), after reducing gamma if necessary. All tend to0. Inside a sufficiently small backward-invariant disk the field is polynomial and set xi=x. Extend by finite backward entry: xi(X)=e^(lambda t)(phi_-t X)_1 for any sufficiently large t. Independence of t follows from the polynomial x equation. The same finite t works on a neighborhood of each X, giving smoothness. Reflection and sign preservation give xi odd and zero exactly on the axis.

Set Theta=a0xi^2. It satisfies the global temperature equation and all signs and normalization. The actual Taylor coefficients satisfy the equations in Section3; normalized a2 and uniqueness of every higher bounded coefficient identify them successively with the target a_k. Hence every transverse coefficient of R_Omega is identically zero along the whole axis, and differentiating in y gives all mixed derivatives. Section1's explicit trajectories show xi=x on B_R and retain both exact PDEs there.

At large r the radial drift is at least beta r-Cr^(1-alpha). Backward entry time to a fixed large sphere is at most int ds/[beta s-Cs^(1-alpha)]<=(log r)/beta+C because the difference from 1/(beta s) is O(s^(-1-alpha)). Transport then gives Theta<=C<X>^((beta-2)/beta), the stated sharp polynomial bound. The canonical relative inverse is unique for the obtained slow tail: the subtracted integral is absolutely convergent and sublinear, and its difference from U is an entire harmonic vector field of sublinear growth, hence constant by the growing-ball gradient estimate. Relative normalization at0 removes this constant.

## 7. Why these configurations are not full profiles

Packet126 rederives the necessary local identity for any C2 temperature. Put k0=beta-2, F=W.grad Omega+Omega, J=W2_x, D1=(k0-W1_x)F-W.grad F, Z=W1 F J+W2 D1 and E=J Z_y-Z J_y-k0D1J. Differentiating the temperature equation in x gives J Theta_y=D1; multiplying transport by J gives k0JTheta=Z. Differentiating the latter in y and eliminating Theta_y proves E=0 without division.

For the analytic pair generated by Psi_L, E is analytic on the connected plane. Its coefficient [x^2 y] is q(2beta+4)mu(2beta+1)q_L'(0), where

    q_L'(0)=c[3(beta+1)+2eta]/[beta(beta+1)L^2]>0.

Therefore E cannot vanish on any nonempty open set. The compact and conic stream corrections have zero gradient at0 and vanish on an exterior open cone about the positive x direction. On that open set the relative W and Omega still equal the analytic base. A global solution would violate the necessary identity there. Thus every constructed finite-L field is a nonprofile, despite all its exact disk and axis properties.

A compact vorticity perturbation by itself does not imply that the relative velocity changes on every open set. For a compact smooth stream perturbation delta odd in x, the raw correction is grad_perp delta and the relative correction is grad_perp delta-grad_perp delta(0). The latter is supported in the same compact set when gradient delta(0)=0. For example delta=x^3 chi with a smooth compact radial chi has this property. In contrast, delta=x chi with chi=1 near0 gives the nonzero constant relative correction (0,-1) outside the support. Thus the obstruction's scope must be phrased as exact agreement of the relative velocity and vorticity on an open set, not as a categorical exclusion or inclusion of all compact vorticity perturbations.

## Dependencies and verification scope

This proof uses packet126's fully quantified compact construction, packet122's two-moment cutoff, elementary regular-singular ODEs, weighted smooth series, complete-flow uniqueness and the analytic identity theorem. Each extension step and the arbitrary-disk preservation have been proved above. The lead's astra/axisflat proof suggested the symbol/conic version; it was read in full and its code was not used. Independent exact checks are supplementary, not a proof of any infinite-order assertion. No full YES or NO follows.

## Model follow-up independently checked, 2026-10-21T05:17:55.234304+00:00

Actual Bedrock model claude-opus-5-5 returned written audits in opus170_disk_conic_followup (49.911977881 s) and opus171_axis_symbol_followup (43.259021880 s). Opus169 used its output budget without an audit, and is not counted as endorsement. The first follow-up checked the explicit disk orbit and weighted conic summation; its qualifications q>0, local finite-entry definition of xi, all mixed derivatives, and epsilon_n<=1 are already explicit above. The second checked the ODE integrating factor, induction order, and forcing powers. I independently recomputed: the a_k force has order m-k-alpha, the w_n force including a_(n+1) has order -n-2alpha, and their transformed integrands have order -1-alpha. The model equation beta t u'+beta d u=c t^(-d-alpha) has particular solution -c/(beta alpha)t^(-d-alpha), so the leading forcing is not resonant. No model statement is used as a proof. Verdict remains CONFIRMED for the construction; each finite-L configuration is REFUTED as a full profile by Section7.
