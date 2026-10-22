# A square identity and explicit commutator bounds for IPM coupling

Status at proof writing: independent analytic reconstruction of V24. The exact algebra audit and actual-model review are pending. All conclusions below are conditional analytic statements about specified coefficients and spaces. No actual coefficient Wiener norm or global inverse is enclosed.

## 1. Operators and hypotheses

Work on R^2 with the unitary Fourier transform fhat(xi)=(2pi)^(-1) integral exp(-i X.xi) f(X)dX. Put J^r=(1-Delta)^(r/2), ||v||_Hr=||J^r v||_2. Let R_j be the real self-adjoint multiplier xi_j/|xi|; its arbitrary value at zero is irrelevant. Then sum R_j^2=I on L2. These R_j are not the skew-adjoint convention with symbol -i xi_j/|xi|. The canonical IPM velocity for -Delta psi=h_x is

 U[h]=(R_1 R_2 h,-R_1^2 h).

For real bounded coefficients a,c define T=a R_1R_2-c R_1^2. For r>=0 and a coefficient f=f_infinity+f_0, where f_infinity is constant, put

 W_r(f)=(2pi)^(-1) integral <p>^r |fhat_0(p)| dp.

Require the indicated Wiener integrals to be finite. Initially use Schwartz test functions. The estimates extend by density to the displayed Sobolev spaces because their constants are finite. Products with bounded coefficients and R_j are bounded on L2.

Let b be a real bounded coefficient and suppose the matrix

 B=[[b+c,-a/2],[-a/2,b]]

is positive semidefinite almost everywhere. This holds if b>=b_+=(sqrt(a^2+c^2)-c)/2, since the two eigenvalues of B are b+c/2 plus or minus sqrt(a^2+c^2)/2. Define S=sum_(i,j) R_i B_ij R_j. It is self-adjoint and nonnegative: its quadratic form is the integral of (Rv)^* B(Rv). No derivative of a matrix square root is needed.

## 2. Exact square identity and the one-order remainder

Set A=sum B_ij R_i R_j=b+c R_1^2-a R_1 R_2=b-T, using sum R_i^2=I. Commuting just the left R_i in S gives S=A+sum [R_i,B_ij] R_j. Therefore the exact bounded-operator identity is

 T=b-S+sum [R_i,B_ij] R_j.                                  (1)

We now bound the displayed commutators directly. Write xi=eta+p and n(xi)=xi/|xi|. For nonzero xi,eta, the triangle inequality and reverse triangle inequality give

 |n(xi)-n(eta)|<=2 min(1,|p|/|eta|),
 |n(xi)-n(eta)|<=2 min(1,|p|/|xi|).

For d,t>=0, min(1,d/t)sqrt(1+t^2)<=sqrt(1+d^2), by treating t<=d and t>=d separately. Thus

 |n_i(xi)-n_i(eta)|<=2,
 |n_i(xi)-n_i(eta)| <eta> <=2<p>,
 |n_i(xi)-n_i(eta)| <xi> <=2<p>.                            (2)

Null frequency sets have no effect on the convolution estimate. The Fourier kernel of [R_i,f] is (2pi)^(-1)(n_i(xi)-n_i(eta)) fhat_0(p). Young's L1*L2 inequality applied to (2) proves

 ||[R_i,f]||_(L2 to L2)<=2W_0(f),
 ||[R_i,f]||_(H^-1 to L2)<=2W_1(f),
 ||[R_i,f]||_(L2 to H^1)<=2W_1(f).                          (3)

Since R_j contracts each H^r, (1) and positivity of S yield

 Re<Tv,v> <= integral b|v|^2 + C_B ||v||_2 ||v||_(H^-1),
 C_B=2 sum_(i,j)W_1(B_ij)
    =2[W_1(b+c)+W_1(a)+W_1(b)].                           (4)

There is also a two-order quadratic-form refinement. Define D=sum [R_i,[R_j,B_ij]]. Expanding four terms and using B_ij=B_ji gives D=A+A^*-2S. Its Fourier kernel has the product (n_i(xi)-n_i(eta))(n_j(xi)-n_j(eta)). Applying one input and one output bound from (2) gives

 ||D||_(H^-1 to H^1)<=4 sum_(i,j) W_2(B_ij).

Since Re<Tv,v>=integral b|v|^2-<Sv,v>-<Dv,v>/2, Sobolev duality gives the alternative upper bound

 Re<Tv,v> <= integral b|v|^2+2 sum_(i,j)W_2(B_ij)||v||_(H^-1)^2. (5)

The sign of D in this identity is negative, but the absolute-value estimate is independent of that sign.

## 3. Velocity and fractional conjugation commutators

For unit vectors of angles theta,phi, the two components of m=(n_1 n_2,-n_1^2) satisfy

 |m_j(theta)-m_j(phi)|<=|sin(theta-phi)|<=|n(theta)-n(phi)|.

In fact the vector difference has norm |sin(theta-phi)|. Hence the output version of (2) holds for either m_j, or for the whole vector, with the same factor2. Peetre's elementary inequality <xi><=sqrt(2)<p><eta> then proves, for r>=1,

 <xi>^r |m_j(xi)-m_j(eta)| <=2^((r+1)/2)<p>^r<eta>^(r-1).

Young's inequality gives

 ||[U_j,f]v||_Hr <=2^((r+1)/2) W_r(f)||v||_(H^(r-1)).       (6)

The same vector norm estimate holds with U in place of U_j.

For s>=2, the mean value theorem and convexity give

 |<eta+p>^s-<eta>^s|
 <=s2^(s-2)(|p|<eta>^(s-1)+|p|^s).

Since <eta>^(s-1)>=1, another L1*L2 estimate proves

 ||[J^s,f]v||_2<=G_s(f)||v||_(H^(s-1)),
 G_s(f)=s2^(s-2)[W_1(f)+W_s(f)].                            (7)

J^s commutes with every R_j. Also ||R_1R_2||<=1/2 and ||R_1^2||<=1. Applying (4) to J^s h and (7) to the two coefficient commutators yields

 Re<J^s Th,J^s h>
 <= integral b|J^s h|^2+(C_B+C_J)||h||_Hs||h||_(H^(s-1)),
 C_J=G_s(a)/2+G_s(c).                                      (8)

This requires global coefficient extensions with the stated positivity and finite Wiener integrals. Compact support of h does not imply compact support of J^s h. Weighted variants require their own multiplication and commutator bounds; (8) does not supply those bounds by itself.

## 4. Positive coupling near a source and the unused directional gap

Suppose grad rho(P)=(0,g), g>0, and ||D^2 rho||_op<=H on B_(3delta)(P). The integral mean-value formula along line segments gives |(a,c)-(0,g)|<=epsilon=3delta H there. For a unit frequency n and t=|n_1|, the coupling symbol is

 q=a n_1n_2-c n_1^2<=-g t^2+epsilon t,

because |(n_1n_2,-n_1^2)|=t. Maximizing this scalar quadratic on [0,1] gives

 b_+<=F_g(epsilon),
 F_g(epsilon)=epsilon^2/(4g) if epsilon<=2g,
 F_g(epsilon)=epsilon-g if epsilon>=2g.                    (9)

For a function v supported in the disc there is also an operator argument: the frozen part is -g||R_1v||_2^2, while the remaining energy is at most epsilon||Uv||_2||v||_2. The identity ||Uv||_2=||R_1v||_2 follows from n_1^2n_2^2+n_1^4=n_1^2. Thus the same quadratic bound holds without a symbol-to-operator inference in this unweighted localized L2 statement.

It is invalid to subtract F_g(epsilon) from an existing frozen margin that already used -g n_1^2. For a concrete counterexample take a transport directional rate g n_1^2-kappa. Its sum with the frozen coupling is -kappa. Replacing c=g by c=g-epsilon, with 0<epsilon<g and a=0, gives full rate -kappa+epsilon n_1^2 even though the new coupling's b_+ is zero. The increase epsilon is larger than epsilon^2/(4g).

If, instead, the full frozen rate has an independently established unused directional gap

 r_frozen(n)<=-kappa-lambda n_1^2, lambda>0,

then the gradient perturbation gives r<=-kappa-lambda t^2+epsilon t<=-kappa+F_lambda(epsilon). The denominator is lambda, not automatically g. This is a principal energy comparison; every other coefficient and localization remainder is still required.

There is a small uniform directional gap in the explicit source box already used in topic77. Set s=31/10, 10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30. The exact Fourier energy rate of

 L_0=A z_1 partial_1+mu z_2 partial_2-1-gR_1^2

is -1-(A+mu)/2+s(A xi_1^2+mu xi_2^2)/<xi>^2-g n_1^2. Since A,mu>0, it is at most

 [-1-A/2+(s-1/2)mu]+[s(A-mu)-g]n_1^2
 <=-1687/500-(449/1000)n_1^2.                              (10)

The first coefficient is maximized at A=10,mu=101/100. The second is maximized at A=51/5,mu=99/100,g=29. Taking these maxima separately gives a valid, potentially non-sharp, simultaneous bound. Formula (10) is an additional analytic fact, not a replacement for the already certified conservative local estimate.

## 5. Far-field scope

If a function has nonzero leading form r^k Theta(theta) on a fixed cone, with k real and a nonzero angular L2 coefficient, then its squared L2(r^(-2gamma)dX) tail has radial integral proportional to integral_R^infinity r^(2k-2gamma+1)dr. It is finite exactly when gamma>1+k; equality diverges logarithmically. A mere O(r^k) upper bound alone does not prove divergence. Positive weights bounded above and below by constants preserve this criterion.

For c_l=1/k>0 the negative far transport margin 1-c_l(gamma-1)>0 requires gamma<1+k. Thus that specific negative-energy weighted remainder realization cannot simultaneously contain a nonzero r^k normalization tail. This does not rule out other domains, explicit asymptotic components, or all possible inverse constructions.

Axis jet formulas requested in V24 are checked separately with the overlapping V25 analysis. Actual global Wiener norms, weighted fractional errors, phase-space localization, domain compatibility, the far asymptotic block and global invertibility remain open.
