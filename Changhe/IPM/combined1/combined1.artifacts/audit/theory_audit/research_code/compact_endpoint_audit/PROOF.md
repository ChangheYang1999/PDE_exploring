# The dipole constraint at the compact-correction endpoint

## Statement and hypotheses

Let c>1, gamma=1/c and 0<delta=1-gamma<1. Let R be a real smooth S1 density on R2, even in x and odd in y, with canonical velocity U_R and

    R(r,theta)=r^gamma Theta0(theta)+O_C1(r^(gamma-delta)).

Here O_C1 means that the radial derivative and r^-1 times the angular derivative are O(r^(gamma-delta-1)), uniformly in theta. Suppose the residual F=(cX+U_R).grad R-R has a convergent finite-branch expansion, with finitely many exponents above gamma-4, and a unique coefficient Fstar(theta) at exponent gamma-4. Suppose all other lower exponents are separated below gamma-4. These expansion hypotheses hold for the exact ordinary-generator candidates007,013,014 at the campaign rational c.

If a real S1 correction h in L2, supported in the disk |Y|<=A, makes R+h stationary in distributions at the same c and with velocity U_R+U[h], then

    Fstar(theta)=-(My/pi)P(theta),
    P(theta)=gamma cos(2theta)Theta0(theta)+sin(2theta)Theta0'(theta),
    My=int y h(Y)dY.                                     (1)

Every residual coefficient above gamma-4 must vanish. If P is nonzero and Fstar=lambda P, then

    ||h||2 >= 2sqrt(pi)|lambda|/A^2.                       (2)

For the finite campaign generator class, the unique endpoint sector is(ell,q)=(1,2), and Fstar=-4c Theta_(1,2). The exact coefficient calculation below independently tests T2 the review of T4-281 R2 on007,013,014. The result does not concern noncompact corrections, including the weighted C1 corrections of T4-294.

## 1. Exterior velocity and its sign

The canonical velocity has symbol (xi1xi2,-xi1^2)/|xi|^2. Off the origin its kernel is

    K(X)=(-xy,(x^2-y^2)/2)/(pi r^4).

The complete second component also has the local term-h/2. It vanishes on the exterior under consideration; it is not deleted from the global velocity. The bounded L2 multiplier and approximation by compact smooth S1 inputs justify

    U[h](X)=int K(X-Y)h(Y)dY, |X|>A.

All moments needed here are finite since h is compactly supported and in L2. Parity gives int h=0, int x h=0, while My may be nonzero. Taylor expansion for r>=2A gives

    U[h](X)=-My partial_yK(X)+O(r^-4 int |Y|^2|h(Y)|dY).

The remainder follows from the homogeneity and bounded angular part of D2K. Direct differentiation gives

    partial_yK=-(cos(3theta),sin(3theta))/(pi r^3).

It follows that the leading radial and angular components of U[h] are respectively My cos(2theta)/(pi r^3) and My sin(2theta)/(pi r^3). This fixes the sign in(1).

## 2. Matching the endpoint

Outside the support, stationarity is the smooth identity F=-U[h].grad R. The stated derivative asymptotic yields

    F=-(My/pi)r^(gamma-4)P+O(r^(gamma-4-delta)),

where delta<1 makes the kernel remainder smaller than the displayed error. The convergent finite-branch expansion now forces all larger coefficients to vanish, by taking the largest nonzero exponent and dividing by its power of r. After their removal, division by r^(gamma-4) and uniform passage to infinity gives(1).

Since int_(|Y|<=A)y^2dY=pi A^4/4, Cauchy-Schwarz gives |My|<=(sqrt(pi)/2)A^2||h||2. When Fstar=lambda P and P is nonzero, (1) says My=-pi lambda and gives(2). This is a necessary product bound, not a bound on the support radius by itself.

## 3. Exact extraction from the potential

For the campaign c=4076476460239181/2251799813685248, the potential is a finite sum

    chi=sum_(j,m,k) a_jmk (1+r^2)^p_j t^k cos(2m theta),
    p_j=(3+gamma-j delta)/2, t=r^2/(1+r^2).

For a fixed j,m, with z=r^-2, the radial part is

    r^(2p_j) sum_k a_jmk (1+z)^(p_j-k).

Thus the q-th homogeneous coefficient is A_q=sum_k a_jmk binom(p_j-k,q). At the endpoint ell=1 only branch j=0 contributes. For q=0 and2 the code obtains A_q by exact rational sums, without differentiating the peer's density polynomials.

For a homogeneous potential A r^d cos(n theta), rho=-partial_y Delta chi has sine coefficients

    n+1: -A(d^2-n^2)(d-2-n)/2,
    n-1: +A(d^2-n^2)(d-2+n)/2.                         (3)

Fold negative sine frequencies with a minus sign. Use d=3+gamma-2q and n=2m. This gives Theta0 and Theta_(1,2) exactly. For the finite set1<=ell<=16, distinct exponents at gamma-4 follow from (ell-1)delta=4-2q: direct exact arithmetic excludes integral (ell-1)delta/2 for1<ell<=16. No nonlinear product has ell=1, since each factor has ell>=1. Hence Fstar=(c(gamma-4)-1)Theta_(1,2)=-4c Theta_(1,2).

If Theta0=sum A_n sin(n theta), then P is obtained by adding A_n(gamma+n)/2 to frequency n+2 and A_n(gamma-n)/2 to frequency n-2, again with signed folding. These finite identities yield an exact coefficientwise proportionality test. When it fails, one nonzero two-coordinate determinant suffices to certify failure; the best-projection residual ratio is only a useful numerical summary.

Changing only branch j=3 leaves Theta0, Theta_(1,2), Fstar and P unchanged. Therefore the branch3 direction in T4-295 cannot remove this endpoint obstruction to an exactly compact correction. That observation does not contradict the proposed noncompact integrable-tail correction.

## Scope and dependencies

This independently checks the analytic endpoint claim in T2 the review of T4-281 R2. It uses the already audited canonical exterior kernel and distributional identity, elementary Taylor expansion, Cauchy-Schwarz and exact finite angular algebra. The existing higher-sector obstruction is not needed to prove the endpoint constraint, although it already excludes the original candidates. No FFT, finite-box argument, inverse or existence claim is used.
