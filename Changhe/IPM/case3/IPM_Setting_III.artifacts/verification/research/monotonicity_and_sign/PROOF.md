# Monotonicity subclasses, flat germs, and limits of scalar sign tests

Independent verifier derivation, 2026-10-20. These are necessary conditions for explicitly restricted subclasses, not a full-class nonexistence result. The sign of the origin slope remains open without the added monotonicities. The lead's sgn1 draft suggested these claims; its code is not used here.

## 1. Exact statement and definitions

An exact profile here means the prompt's smooth primary class: ell>1, density rho even in x and odd in y, a=rho_y(0) nonzero, canonical U=(-psi_y,psi_x)=o(r), -Delta psi=rho_x, W=ell X+U, and W.grad rho=rho, with |rho|+(1+r)|grad rho|<=C(1+r)^gamma for a gamma in(0,1). Set

    D=ell-1, A=2ell-1, B=2D, q=rho/(a y).

The quotient extends smoothly and evenly in both coordinates across y=0. All monotonicities below are on x,y>0. The conclusions are:

1. q_x<=0 implies a>0.
2. q_x<=0 and q_y<=0 imply a>D.
3. Under both coordinate monotonicities, if the first nonconstant Taylor polynomial of q has degree2k, then a>=2A+2k-2. Thus a>=2A for every nonflat germ. Global real analyticity eliminates the flat exception; plain smoothness does not.
4. q_theta>=0 implies 0<a<4D. The alternative q_theta<=0 together with q_x<=0 implies a>4D. Angular derivatives are at fixed radius.
5. On any positive x-axis interval with no zero of w=W_1(x,0), g=rho_y(x,0) satisfies w g'=(w'-A)g. If w never vanishes on x>0 then

       g(x)=C_infty x^(p-1)(1+O(x^(p-1))), p=1/ell,
       C_infty/a>0.

   No far-field derivative bound on U is needed for this assertion.

We also construct nonprofiles demonstrating that strict density sign, source compatibility, absence of other equilibria, formal Taylor solvability, or the single harmonic integral identity do not by themselves prove an unrestricted slope bound.

## 2. Canonical strain and uniform decay of the quotient

From the independent inverse and origin proofs,

    c=psi_xy(0)=(1/pi) integral xy r^-4 rho_x dX
      =-a/4+I3=-D,
    I3=integral_0^infty rho_3(r)r^-2 dr,
    rho_3=(1/pi) integral_0^(2pi) rho(r,theta)sin(3theta)dtheta.

The derivative integral is absolutely convergent: rho_x=O(r^2) at zero, while rho_x=O(r^(gamma-1)) at infinity. Integrating its kernel by parts on circular annuli yields the -a/4 inner boundary. I3 is absolutely convergent after angular projection, but the original density integral against r^-3 sin3theta is only circularly convergent.

The quotient formula q=(1/a) integral_0^1 rho_y(x,ty)dt proves smooth extension. It is 1+O(r^2) near zero. To show q=O(r^(gamma-1)) uniformly at infinity, split into |x|>=r/2 and |x|<r/2. In the first region every point (x,ty) has radius at least r/2, so the gradient bound applies to the quotient formula. In the second region |y|>=sqrt(3)r/2, and the density bound applies directly. Thus q tends uniformly to zero.

Under q_x<=0 each horizontal ray decreases to zero, so q>=0. The strain becomes

    c/a=(4/pi) integral_(Q1) x y^2 r^-4 q_x dX <0.       (1)

Strictness follows because q(0,y)>0 for sufficiently small y, whereas q(x,y) tends to zero with x. The derivative is strictly negative at some point and hence on an open set. Since c=-D<0, a>0.

For the second conclusion, define V=y^2 X/r^4 on the open quadrant. It has divergence0 away from zero and zero normal flux on the straight sides. Its outward inner-circle flux against q tends to -pi/4, while the outer flux tends to zero. Both coordinate derivatives have the same sign, so monotone convergence on expanding quadrant annuli gives

    1=S+T,
    S=(4/pi) integral x y^2 r^-4 (-q_x)=D/a,
    T=(4/pi) integral y^3 r^-4 (-q_y).

The horizontal argument gives S>0; a vertical ray starting sufficiently near zero gives T>0. Thus 0<D/a<1, proving a>D. Absolute integrability of each term follows at the same time from its nonnegative sign and finite sum.

## 3. A first nonzero monotone Taylor polynomial

Suppose q=1+Q+O(r^(2k+2)), Q=sum_(j=0)^k t_j x^(2j)y^(2k-2j), k>=1, Q nonzero. Scaling the monotonicities to zero gives Q_x,Q_y<=0 in the quadrant. Taking the y-axis limit of Q_y gives t0<=0. Dividing Q_x by x and taking x to zero with y positive gives t1<=0.

There is no stream polynomial between degrees2 and2k+2. Indeed, at each intervening degree the density correction vanishes; transport forces a partial_x psi_degree=0. Oddness in x eliminates that polynomial. At the first correction degree transport gives

    partial_x Psi=-y(Ax Q_x+y Q_y),
    Psi=-sum_(j=0)^k [d_j t_j/(2j+1)] x^(2j+1)y^(2k-2j+1),
    d_j=2jA+2(k-j).

Poisson, Delta Psi=-a y Q_x, gives for1<=j<=k

    2j(a-d_j)t_j
      =[(2k-2j+3)(2k-2j+2)/(2j-1)] d_(j-1)t_(j-1).     (2)

If a<d1=2A+2k-2, all a-d_j<0. In the j1 equation the left side is nonnegative and the right side nonpositive. Equality forces t0=t1=0. The remaining equations inductively force every coefficient to vanish, a contradiction. This proves the third conclusion. At k1 it reduces to 6e=(a-2A)b for rho=ay+b x^2y+e y^3.

If a globally real analytic density has a flat q-1 germ, then rho=ay near zero and analytic continuation on the connected plane gives rho=ay everywhere, contradicting the growth condition. This argument specifically uses global real analyticity; it does not prove that smooth exact profiles are analytic.

## 4. Angular monotonicity and the strict endpoint

On a quadrant circle let u=cos^2theta and dmu=(4/pi)sin^2theta dtheta. This is a probability measure with mean(u)=1/4. Since sin3theta=sin theta(4u-1),

    rho_3(r)/a=4r Cov_mu(q,u).                            (3)

The covariance equals half the double integral of (q(s)-q(t))(u(s)-u(t)). The function u strictly decreases with theta. Thus q_theta>=0 implies I3/a<=0; q_theta<=0 implies I3/a>=0. In the first case D/a=1/4-I3/a>=1/4 gives 0<a<=4D. In the second case horizontal monotonicity first supplies a>0, and D/a<=1/4 gives a>=4D.

Equality forces q to be constant on every circle: each radial covariance has one sign, and a nonconstant continuous monotone angular function gives strict covariance on a product of two intervals. An exact single angular mode is excluded by the independent finite-angular theorem. For a separate elementary check of that special case, write rho=yf(r), psi=xy k(r). Canonical Poisson gives

    k=-r^-4 integral_0^r s^3 f(s)ds,  f=-r k'-4k,
    a=4D.

For phi=r^-3sin3theta, the exact transport identity with circular inner truncation is

    J=integral rho U.grad phi=-pi D(D+a/4).

Angular integration for the single mode instead gives

    J=-(3pi/4) integral_0^infty f k' dr
      =(3pi/4) integral_0^infty r(k')^2 dr-3pi a^2/32.

The first identity requires J=-pi a^2/8, so integral r(k')^2=-a^2/24, impossible. Here k'=O(r) at zero and O(r^(gamma-2)) at infinity, justifying the integrations. Hence both angular bounds are strict.

## 5. Exact axis asymptotics without differentiating the far-field trace

Parity and div W=2ell imply on y=0

    w g'+(2ell-w')g=g,  w g'=(w'-A)g.

If w has no positive zero it is positive there, since w'(0)=A. A scalar linear ODE on any interval away from zero then preserves the sign of g. For x>=x0>0,

    g(x)=[g(x0)/w(x0)] w(x)
          exp(-A integral_(x0)^x ds/w(s)).                (4)

The independent far-field theorem gives U=O(r^p), so w=ell x+O(x^p) and 1/w-1/(ell x)=O(x^(p-2)). Its tail integral is O(x^(p-1)). Formula(4) gives exponent1-A/ell=p-1, the claimed relative error and C_infty/a>0. Without the no-zero condition, the same argument holds on a sufficiently remote interval: either g vanishes identically there, or the expansion holds with a nonzero constant not connected to a by this argument.

This is not differentiation of the uniform angular far-field limit. To see the distinction, let F be smooth odd compactly supported, F'(0)=1, and delta>0. Outside r2 put

    rho=r^p sin theta+r^(p-delta)F(r^delta sin theta),

and join smoothly to y inside r1. This density has the required parity and the value/gradient growth bound with exponent p. The argument of F is bounded wherever its derivatives contribute, giving |grad rho|=O(r^(p-1)). The uniform angular trace is sin theta, but rho_y(x,0)=2x^(p-1) for x>2. This nonprofile shows why the trace alone does not identify the derivative coefficient.

## 6. Sharpness for canonical test fields and the flat exception

A test field in this section has smoothness, parity, growth and the canonical inverse, but need not solve transport. Let alpha,beta>0 and F smooth nonincreasing with F0=1,F(infinity)=0 and exponential decay. For

    rho=a y F(alpha x^2+beta y^2)

both coordinate monotonicities hold, and radial integration in the derivative strain formula gives

    c/a=-alpha/(sqrt(alpha)+sqrt(beta))^2.                 (5)

To check the angular constant independently, set Q=alpha cos^2theta+beta sin^2theta. The radial integral is integral_0^infty r F'(r^2Q)dr=-1/(2Q), and hence c/a=-(alpha/pi) integral cos^2theta sin^2theta/Q dtheta. Substitution t=tan theta on each quadrant, or partial fractions after this substitution, gives that integral as pi/(sqrt(alpha)+sqrt(beta))^2. Thus any a>D is compatible with strain and both monotonicities: set beta1 and sqrt(alpha)=sqrt(D/a)/(1-sqrt(D/a)). The Gaussian choice fails transport at a nonzero extremum of rho(0,y), so this is not sharpness for exact profiles.

For a flat local countertest choose

    F(t)=1 for t<=1,
    F(t)=exp(-(t-1)exp(-1/(t-1))) for t>1.

It is smooth and flat at the join, positive, nonincreasing and exponentially decaying. Choose alpha,beta as above, allowing D<a<=B. Then rho=ay near zero and c=-D. The canonical stream has exactly its quadratic harmonic in an interior disk. Indeed its harmonic mode2n, n>=2, is proportional to

    integral sin(2n theta)cos theta sin theta Q(theta)^(n-2)dtheta
       times integral_0^infty u^(3-2n)F'(u^2)du.

Both integrals converge, since F' vanishes near zero. The first factor vanishes: its factor other than sin(2n theta) is a trigonometric polynomial with frequencies at most2n-2. Thus psi=-Dxy there. The local transport and Poisson equations hold exactly, along with every local Taylor condition. Globally the axis density tends to zero and has a nonzero extremum, so transport fails. This construction preserves the flat-germ gap in a purely local argument, including one using the exact canonical inverse.

## 7. Limits of stricter scalar and geometric premises

The positive quotient Gaussian-polynomial family

    rho=a y exp(-r^2)(1+M x^2+N y^2), M,N>=0

has c/a=-1/4+(M-N)/8. Any nonzero a and any D>0 can meet c=-D by choosing M-N=2-8D/a. All are nonprofiles because their nonzero axis density has an extremum.

Even absence of additional equilibria does not repair that inference. Set sigma=y(1+4x^2)exp(-r^2), rho=-sigma/100, ell=401/400. Then a=-1/100,c=-1/400 and q>0. With Fourier transform integral exp(-iX.k) sigma(X)dX,

    sigmahat=-i pi eta(3-xi^2)exp(-|k|^2/4)/2.

The velocity multiplier has norm at most1. Thus ||DU[sigma]||_infinity<=22, by the elementary radial bound (1/4) integral_0^infty r^3(3+r^2)exp(-r^2/4)dr=22. Since U0=0,

    X.W >= (401/400-22/100)r^2>0.

Backward trajectories contract to zero and forward trajectories escape, but this field still fails axis transport. Consequently this is a counterexample only to an intermediate implication that omits transport.

A separate construction shows insufficiency of the scalar harmonic identity together with strain and strict sign. It does not preserve the dynamical property of the preceding Gaussian example. For any a!=0,D>0 one can arrange J=-pi D(D+a/4) without satisfying transport. Here is the full construction. Let eta be a nonnegative radial smooth unit-mass bump supported in the unit disk. For Q in the open quadrant and sufficiently small delta let

    h_(Q,delta)(X)=delta^-2 sum_(sigma,tau=+/-1)
                  tau eta((X-(sigma Qx,tau Qy))/delta).

It is nonnegative on the upper half-plane, supported away from axes, has zero origin slope and

    c[h]=(4/pi)phi(Q)+O(delta^2),
    J(h)=-2 delta^-2 ||eta||_2^2 partial_y phi(Q)+O(delta^-1). (6)

The strain follows from smooth kernel integration at the four bumps. For J, radial symmetry and the exact multipliers give integral eta V1[eta]=0 and integral eta V2[eta]=-||eta||_2^2/2. Each rescaled self-interaction has size delta^-2; four reflected copies have equal sign. Variation of grad phi contributes O(delta^-1); separated cross-interactions are O(1). This proves(6).

Now partial_y phi=3r^-4cos4theta. At radius1 and theta pi/4, phi>0 and partial_y phi<0. At theta pi/12 both are positive. A fixed bump at theta5pi/12 has negative strain. Add its positive multiple to each of the first two bumps to make their strains exactly zero. The correcting coefficients remain bounded as delta tends to zero, and all cross terms remain O(1). For sufficiently small fixed deltas one obtains h_plus,h_minus, both nonnegative upstairs, with zero slope and strain and respectively J positive and negative.

Start from the Gaussian-polynomial rho0 with prescribed a,c=-D. Adding sign(a)(s h_plus+t h_minus), s,t>=0, preserves strict sign, slope and strain. J is a continuous quadratic polynomial of s,t. Its leading terms along the two axes have opposite signs, so a segment between sufficiently large axis points attains any prescribed real J. All integrals exist: added fields vanish near zero and have zero strain, so their canonical velocities are O(r^3) there; the only cross term with the base's linear singular germ is now integrable. At infinity the fields decay and the weighted kernels are integrable. The axis density was not changed, so the resulting field remains a nonprofile. This proves insufficiency of strain, strict sign and this single weighted identity together. It does not show insufficiency when absence of extra equilibria is imposed simultaneously: the added narrow bumps can destroy that dynamical property. The preceding Gaussian test and this construction have different scopes.

## 8. Quantitative moment condition and scope

If an exact profile additionally satisfies integral |rho_3(r)|r^-2 dr<=kappa |a| with0<=kappa<1/4, then

    a>0,  4D/(1+4kappa)<=a<=4D/(1-4kappa).

This is just inversion of D/a=1/4-I3/a and |I3/a|<=kappa. Its lower bound exceeds B. No estimate of that form has been proved automatic. In particular a and the far-field trace cannot control that moment for arbitrary canonical test fields: an intermediate annular r^3sin3theta bump changes I3 and leaves both quantities fixed. Scaling preserves I3,a while multiplying the far-field amplitude by lambda^(1-p), so a proposed universal bound by an unnormalized far-field amplitude needs additional hypotheses.

Dependencies: inverse, origin, finite_angular, far_field_holder and scaling proofs in this lane. Every new argument above was rederived independently. The formal code checks in verification are consistency tests, not substitutes for the proofs. No exact profile, full-class sign theorem, or full-class slope exclusion has been obtained.


## 9. Exact weighted defect of the Gaussian countertest

For the Gaussian sigma=y(1+4x^2)exp(-r^2), put t=r^2. Its only density modes are sigma1=(r+r^3)exp(-t) and sigma3=r^3 exp(-t). The canonical stream has modes

    psi2=(t/2+3/4+3/(4t))exp(-t)-3/(4t),
    psi4=(t/4+3/4+3/(2t)+3/(2t^2))exp(-t)-3/(2t^2).

The apparent poles cancel at zero. Direct substitution in the radial Poisson equations verifies the source modes (3t-2t^2)exp(-t) and -t^2 exp(-t), regularity at zero, and decay at infinity. Thus these are the canonical modes, with no harmonic strain added. Let phi=r^-3 sin(3theta) and J_sigma be the circularly truncated integral of sigma U[sigma].grad phi. Angular integration gives

    J_sigma=(3pi/4) integral_0^infinity ((1+t)exp(-t)/t^2)
                  [2psi2-4psi4-2t psi2'+2t psi4'] dt.

The bracket cancels the singular terms at zero. The integrand reduces exactly to

    (t/2-7/(2t)-12/t^2-21/t^3-12/t^4)exp(-2t)
        +(-3/t^2+9/t^3+12/t^4)exp(-t).

One may integrate after multiplying by t^z for Re z>3, use the gamma-integral formula term by term, and continue the sum to z=0. The original combined integrand is bounded at zero, so its Mellin integral is analytic there; individual poles cancel. Factoring Gamma(z), the remaining factor vanishes at zero and its derivative there is (11/2)log2-83/24. Consequently

    J_sigma=pi[(33/8)log2-83/32],
    J_rho=J_sigma/10000=0.000083403667725383257605286... .

For rho=-sigma/100, D=1/400 and a=-1/100, the necessary transport value -pi D(D+a/4) equals zero. The computed nonzero defect therefore rules out this field even at the weighted-identity level. It satisfies the canonical strain, strict sign and kinematic source-escape properties from Section7, but does not satisfy all their conjunction with the weighted transport identity. The calculation is exact; the separately implemented 55-digit integral agrees to better than 1e-40 for J_sigma. Verification/gaussian_J_and_table.json and independent_code/check_gaussian_J_and_forcing_table.py contain the checks. No exact-profile counterexample is asserted.
