# Arbitrarily many projected equations and exact transport on a disc

Independent reconstruction, 2026-10-21 UTC. Written before the new checker.
The frozen external proposal is recorded in verification/MANIFEST.json.
The theorem below is a local construction with a canonical compact extension.
It is not a global IPM profile or a nonexistence theorem for such profiles.

## Statement, notation and exceptional slopes

Fix c>1, put D=c-1 and A=2c-1, and choose H>0. For a density rho,
write R=(cX+U) dot grad rho-rho, U=(-psi_y,psi_x), -Delta psi=rho_x.
The canonical velocity is the parity-preserving full-plane velocity with
U=o(r). For each odd p let R_p(r)=integral_0^(2pi) R(r,theta) sin(p theta)
dtheta. Thus R_p is pi times its sine-series coefficient.

For each integer N>=2, and also for N=infinity, there is a locally finite
exceptional set E_c^N in the real a-line, defined explicitly below, such
that the following holds. Given

    a>=4c+20, a not in E_c^N, and a prescribed finite R0>0,

there exists a real smooth compactly supported density on R^2, even in x
and odd in y, with its canonical stream, satisfying

    rho_y(0)=a, psi_xy(0)=-D,
    q=rho/(a y)<1 at every point other than zero, q(0)=1,
    R_1=R_3=...=R_(2N-1)=0 on r<=R0, if N is finite,
    R=0 on r<=R0, if N=infinity.

The quotient is extended smoothly across y=0. Its cubic density
coefficients b and e in rho=ay+b x^2 y+e y^3+O(r^5) are both nonzero and
negative. For finite N the only allowed global sine modes are
1,3,...,max(2N-1,5). The construction with N=infinity may have infinitely
many modes. None is a global profile, because a nonzero compact density
has a positive maximum at which its transport residual is negative.

For integer c>=2, every noninteger rational a>=4c+20 avoids all the
exceptional sets, including E_c^infinity. This gives explicit arbitrarily
large slopes. No existence assertion is made at an exceptional slope.
The N=1 case with an exceptional set defined from a one-dimensional
matrix is not asserted: the given forcing construction uses both cubic
modes 1 and 3.

## Polynomial inverse with fixed harmonic moments

Put S_(n,p)=r^n sin(p theta), where n>=3 is odd and p=1,3,...,n.
This is a Cartesian polynomial. Define a linear map on homogeneous
polynomials with the density parity by

    P S_(n,p)=-S_(n+1,p+1)/(2(n+p+2))
               -1_(p>1) S_(n+1,p-1)/(2(n-p+2)).        (1)

The stream is odd in both Cartesian variables. The identities

    Delta S_(d,m)=(d^2-m^2) r^(d-2) sin(m theta),
    d_x S_(n,p)=[(n-p)sin((p+1)theta)
                    +(n+p)sin((p-1)theta)]r^(n-1)/2

give -Delta Ph=d_x h, term by term. If p=n, the first term of (1)
is harmonic, but it is retained. This choice is a fixed convention;
it is not permission to add a free global strain.

To verify its moment meaning, write a local density as
rho=r sum_(k>=0) F_k(r) sin((2k+1)theta), F_0(0)=a and F_k=O(r^(2k)).
For m>=1 put

    J_(m-1)=r^(-2m-2) integral_0^r s^(2m+1)F_(m-1)(s)ds,
    T_m=r^(2m-2)[M_m-integral_0^r F_m(s)s^(1-2m)ds],
    M_1=a/4-D, M_2=H, M_m=0 for m>=3.                 (2)

The stream is r^2 sum_m (T_m-J_(m-1))sin(2m theta)/2.
For a single degree-n mode, evaluating these power integrals gives
exactly (1). The base density ay contributes -a r^2 sin(2theta)/8;
M_1 contributes (a/4-D)r^2 sin(2theta)/2. Their sum is -Dxy.
The remaining prescribed datum contributes

    psi_H=(H/2)S_(4,4).

Consequently the local stream of rho=ay+h is
psi=-Dxy+psi_H+Ph. In particular a top harmonic in Ph can cancel
part of psi_H; H is an upper density moment, not the literal coefficient
of S_(4,4) in another choice of particular inverse.

## Linearized matrices and high-degree control

On degree n=2j+1>=3 define

    L_n h=(A x d_x+y d_y-1)h+a d_x Ph.

The transport part follows from the base stream -Dxy. For the first d
sine modes, 1<=d<=j+1, let B_d(lambda) be the projected matrix of L_n,
where lambda=2j. Its entries are

    B_00=(c+1)lambda/2-a/4,
    B_ii=c lambda+D-a/2 for i>=1,
    B_(i,i+1)=(lambda+2i+4)[2D(lambda-2i)-a]/[4(lambda-2i)],
    B_(i+1,i)=(lambda-2i)[2D(lambda+2i+4)-a]/[4(lambda+2i+4)]. (3)

Indices start at zero; only adjacent off-diagonal entries are present.
The denominators in (3) are nonzero for this physical range of d.
For example, the diagonal correction in the first row uses
sin(-theta)=-sin(theta), which matters for the coefficient of lambda.
Formula (3) follows by differentiating (1) and using

    (x d_x-y d_y)S_(n,p)
       =[(n-p)S_(n,p+2)+(n+p)S_(n,p-2)]/2.

Set P_0=1, P_1=B_00, and for k>=2 set

    P_k=(c lambda+D-a/2)P_(k-1)-Q_(k-2)P_(k-2),
    Q_i=([2D(lambda+2)-a]^2-16D^2(i+1)^2)/16.          (4)

Multiplying the adjacent entries of (3) gives Q_i; expansion of a
tridiagonal determinant gives det B_d=P_d. Thus the apparent poles
cancel in the determinant. Induction in (4) gives the leading
coefficient (-1/4)^d as a polynomial in a. Each P_d is nonzero.

Let w_i=binom(2j+1,j-i). Since
w_(i+1)/w_i=(lambda-2i)/(lambda+2i+4), the conjugated matrix
Btilde=diag(w)^(-1)B diag(w) has off-diagonals

    [2D(lambda-2i)-a]/4, [2D(lambda+2i+4)-a]/4.        (5)

At a=0 its diagonal minus the nonnegative off-diagonal row sum is
lambda, except at a truncated last row, where it is
lambda+D(lambda-2d+2)/2>=lambda. The absolute row sum of its coefficient
of a is at most one. For lambda>|a|, evaluating Btilde v at an index
of maximum |v_i| therefore yields

    ||Btilde v||_infinity >=(lambda-|a|)||v||_infinity,
    ||Btilde^(-1)||_infinity <=1/(lambda-|a|).         (6)

This proof uses the triangle inequality and works for complex vectors;
no assertion about real eigenvalues is needed. The same row estimates
for full d=j+1 give Re(mu)>=n-1-a and |mu|<=An-1+a for a>=0.

For finite N let d_j=min(N,j+1); for N=infinity let d_j=j+1. Define

    E_c^N=union_(j>=1) {a real:P_(d_j)(2j,a,c)=0}.     (7)

On |a|<=B, (6) excludes roots with 2j>B. Only finitely many polynomials
remain, each with finitely many roots. This proves local finiteness,
including when N=infinity; it is stronger than a finite-order check.
If c is an integer and lambda=2j, then 4^d P_d is a monic integer
polynomial up to sign. Indeed its recurrence has integer coefficients
4B_ii and 16Q_i, and its leading coefficient is (-1)^d. A rational root
of a monic integer polynomial is integral: clearing the denominator of
a root r/s in lowest terms shows s divides r^d. Hence any noninteger
rational a avoids (7).

For N=3 the matrix B_3(2j) is exactly C_j of the independently proved
three-projection result, and P_3(2j)=Delta_j, with no factor. At j=1
the physical matrix is B_2(2). A pole in a formal B_3(2) is not an
additional cubic equation.

## Why unreduced moment resonances do not obstruct the construction

For finite N use F_0,...,F_(N-1), J_0,...,J_(N-1), and T_1,...,T_(N-1).
When N=2 prescribe T_2=Hz; when N>=3 prescribe T_N=0. Here z=r^2.
The dot derivative r d/dr gives

    dot J_i=F_i-(2i+4)J_i,
    dot T_m=(2m-2)T_m-F_m.                              (8)

Writing V_m=(T_m-J_(m-1))/2, direct polar transport gives the coefficient
E_i of R/r as

    c dot F_i+D F_i
    +sum_(m,k) coeff_sin((2i+1)theta) of
      [-2m V_m(F_k+dot F_k)cos(2m theta)sin((2k+1)theta)
       +(2k+1)(2V_m+dot V_m)F_k sin(2m theta)cos((2k+1)theta)]. (9)

After (8) is inserted this is Mat(Y)dot F+G(Y,z). The base derivative
matrix is the sine compression of multiplication by c+D cos(2theta):
its first diagonal is (c+1)/2, other diagonals c, and off-diagonals D/2.
It is positive definite with smallest eigenvalue at least c-D=1, as
seen by integrating (c+Dcos(2theta)) times the square of a sine sum.
Thus the equations define an analytic regular singular system zY'=Phi.

For its full Jacobian B0 at the base, scalar moment elimination gives

    det(jI-B0) = [product_(i=0)^(N-1)(j+i+2)
                     product_(m=1)^(N-1)(j-m+1)]
                  P_N(2j)/(2^N det Mat0).             (10)

One proves it first away from the scalar pivots, then extends as a
polynomial identity. In particular j=1,...,N-2 are structural resonances
in the unreduced system. They are not removed by excluding slopes a.

Cartesian smoothness requires F_i=O(z^i); equation (2) fixes the
coefficient z^(m-1) in T_m to M_m. At order j only d_j density
coefficients are allowed. The degree 2j+1 residual is a Cartesian
polynomial and has no sine frequency exceeding 2j+1; all forbidden
higher-frequency equations vanish identically. The remaining matrix is
B_(d_j)(2j), so (7) supplies exactly the needed inversions. The convergence
argument below works in the physical polynomial space directly and never
inverts a structural resonance of the larger moment system.

## A polynomial norm that closes the nonlinear equation

Use independent complex coordinates w=x+iy and v=x-iy. For
h_n=sum_(k=0)^n h_k w^k v^(n-k), define

    ||h_n||_n=max_k |h_k|/binom(n,k).                   (11)

Vandermonde's identity gives ||fg||_(p+q)<=||f||_p||g||_q.
For each derivative, the identities
(k+1)binom(n,k+1)=n binom(n-1,k) and
(n-k)binom(n,k)=n binom(n-1,k) give

    ||d_x h_n||_(n-1), ||d_y h_n||_(n-1)<=2n||h_n||_n. (12)

Each sine coefficient contributes to a distinct conjugate pair of complex
monomials. Hence sine projection decreases (11), and on the parity
subspace (11) is half of the weighted maximum norm using w_i above.
The constant one half is common to every mode and degree.

For clarity, the velocity bound can be proved directly. The polynomial
particular inverse P0 with both pure-power coefficients set to zero has
coefficients, 1<=k<=n,

    (P0 h)_k=-[h_k/(n-k+1)+h_(k-1)/k]/4.

Dividing by binom(n+1,k) bounds its norm by ||h||_n/[2(n+1)].
The difference P-P0 has only the top sine term
-h_top S_(n+1,n+1)/[4(n+1)], of norm at most ||h||_n/[4(n+1)].
Using (12),

    ||d_x Ph||_n, ||d_y Ph||_n<=3||h||_n/2<=2||h||_n. (13)

This degree-independent estimate includes the top harmonic in the correct
moment convention. It avoids an unweighted coefficient estimate that
would incorrectly lose a factor of degree.

Let

    K=max(2,max_(1<=j<=ceil(a)) 2j ||Btilde_(d_j)(2j)^(-1)||_infinity).

This is finite by (7); (6) controls all omitted j. In norm (11) every
physical inverse L_(2j+1)^(-1), with projection when N is finite, has
norm <=K/(2j).

Write h=sum_(j>=1)h_(2j+1), with the allowed parity and angular modes,
and use ||h||_t=sum_j ||h_(2j+1)||_(2j+1)t^j. This is a complete
weighted sum of finite-dimensional coefficient spaces. Define

    Gamma h=-L^(-1) Pi_N [a d_x psi_H
                          +U_H dot grad h+U[h] dot grad h],
    U_H=(-d_y psi_H,d_x psi_H), U[h]=(-d_y Ph,d_x Ph). (14)

The two components of U_H have degree-three norm H. Products and (12)-(13)
give, with no radius loss,

    ||Gamma h||_t<=alpha t+beta t||h||_t+gamma||h||_t^2,
    alpha=KaH/2, beta=4KH, gamma=8K.                  (15)

For the quadratic term of input degrees p,q>=3, the output degree is
n=p+q-1, and the inverse cancels the derivative using q/(n-1)<=1.
For the U_H term the ratio is q/(q+1)<=1. The forcing is degree three
and its inverse costs at most K/2. These observations establish every
constant in (15).

Take

    t=min(1,1/(4beta),1/(16gamma alpha)), S=2alpha t.   (16)

On ||h||_t<=S, the three bounds in (15) are at most S/2,S/4,S/8.
The Lipschitz constant is at most beta t+2gamma S<=1/2. Banach's
contraction theorem supplies a fixed point. Reality is preserved by all
maps. Since |h_n(w,v)|<=||h_n||_n(|w|+|v|)^n, its series converges
normally on smaller complex neighborhoods with |w|+|v|<sqrt(t), and
all derivatives converge there. In particular it is real analytic for
r<sqrt(t)/2. Equations (1) and (14) imply Poisson and the requested
projected or full transport equation on that disc. This is convergence
of a function, not merely formal Taylor solvability.

## Strict sign from a controlled cubic term

At degree three both allowed modes are present for every N>=2. Their
coefficients f_1,g_1 solve

    B_2(2)(f_1,g_1)^T+(0,2aH)^T=0.

Put F=a^2-(4c+20)a+128c-64. Direct solution gives

    f_1=-24Ha(a-4c+4)/F, g_1=8Ha(a-4c-4)/F,
    b=f_1+3g_1=-192Ha/F,
    e=f_1-g_1=-32Ha(a-4c+2)/F.                       (17)

For a>=4c+20, F=a(a-4c-20)+128c-64>0, so b,e<0. In this
range the cubic matrix is automatically invertible. Set m=min(-b,-e)>0
and

    r1^2=min(t/16,m t^2/(1280 S)).                    (18)

Every homogeneous term is divisible by y. Integrating its y derivative
from (x,0) to (x,y), using (12), bounds the higher terms by

    |(h-h_3)/y|<=2S sum_(j>=2)(2j+1)(4r^2/t)^j
                  <=640 S r^4/t^2

when 4r^2/t<=1/2. The sum identity is
sum_(j>=2)(2j+1)x^j=x^2(5-3x)/(1-x)^2<=20x^2.
Equations (17)-(18) therefore imply

    q<=1-m r^2/(2a)<1 on 0<r<=r1.                    (19)

This includes y=0 by smooth extension. The origin slope is a and the
origin stream strain is -D by (2).

## An exact compact extension of all moments

Let r2=r1/8, r3=r1/4, r4=r1/2, r5=3r1/4. Take a smooth radial
0<=chi<=1 equal to one for r<=r2 and zero for r>=r3. All radii lie
strictly inside the convergence disc. The cutoff chi rho still has q<1
away from zero: multiplying a number less than one by a number in [0,1]
cannot raise it to one.

Define eta(u)=exp(-1/[u(1-u)]) for 0<u<1 and zero elsewhere, and
phi(r)=eta((r-r4)/(r5-r4)). For k>=1 define

    I_k=integral_0^infinity phi(s)s^(1-2k)ds>0,
    C_k=[M_k-integral_0^infinity chi(s)F_k(s)s^(1-2k)ds]/I_k. (20)

For finite N, F_k=0 for k>=N, so C_k=0 for k>max(N-1,2).
The finite mode count follows. For N=infinity we need an actual
convergence estimate for the extension; formal moment assignments alone
would not suffice.

The coefficient bound in (11) and |binom(2j+1,j-k)|<=2^(2j+1)
show, for s<=r3,

    |F_k(s)|<=8S(4/t)^k s^(2k).

Indeed each sine coefficient is at most twice the corresponding complex
coefficient, and the remaining geometric series has ratio 4s^2/t<1/2.
On the middle third of the bump interval phi>=exp(-9/2), the length is
r1/12, and s<=2r1/3. Thus

    I_k>=exp(-9/2)(r1/12)(2r1/3)^(1-2k).

For k>=3, M_k=0. The numerator of (20) has magnitude at most
4S(4/t)^k r3^2. Dividing yields

    |C_k|<=Cstar bstar^k,
    Cstar=(9/2)exp(9/2) S,
    bstar=16r1^2/(9t)<=1/9.                           (21)

Consequently sum_k C_k sin((2k+1)theta), together with every angular
derivative, converges uniformly. Multiplication by the single fixed
smooth radial bump gives uniform convergence of every Cartesian
derivative on its annulus, which is bounded away from zero.

Take a smooth 0<=zeta<=1 supported in r3<r<r1 and equal to one on
[r4,r5]. Put

    B=1+3|C_1|+5|C_2|
          +Cstar bstar^3(7-5bstar)/(1-bstar)^2,
    rho_ext=chi rho-B r zeta sin(theta)
                      +r phi sum_(k>=1) C_k sin((2k+1)theta). (22)

The rational expression is the exact sum
sum_(k>=3)(2k+1)bstar^k. The inequality
|sin((2k+1)theta)/sin(theta)|<=2k+1 follows by the finite geometric
series for complex exponentials and extends to the axes. On the bump
annulus chi=0,zeta=1,phi<=1, so rho_ext/y<=-1. Elsewhere outside the
cutoff density rho_ext/y<=0. Together with (19) this proves q<1 off
zero. Standard explicit cutoffs are obtained from e(u)=exp(-1/u) for
u>0, zero otherwise, and s(u)=e(u)/(e(u)+e(1-u)); take
chi=1-s((r-r2)/(r3-r2)) and
zeta=s((r-r3)/(r4-r3))[1-s((r-r5)/(r1-r5))].

The constructed density is C-infinity and compactly supported. Every
upper density moment equals the assigned M_k by (20). On r<=r2 all
lower moments equal the local ones; the extra first-mode negative bump
changes only a lower moment, and has no interior contribution. Thus the
canonical density-moment Green formula

    psi_(2m)=r^2/2 [r^(2m-2) integral_r^infinity F_m(s)s^(1-2m)ds
                  -r^(-2m-2) integral_0^r s^(2m+1)F_(m-1)(s)ds] (23)

agrees with the constructed local stream in every mode. The global
canonical inverse exists for the smooth compact density, as proved in
research/inverse/PROOF.md; it is also obtained by the smooth Newton
potential of rho_x. The geometric decay in (21) and local analyticity
justify mode identification and termwise differentiation. Equivalently,
apply that inverse to the uniformly C-infinity convergent density sum.
Formula (23) follows by integration by parts in the radial Poisson Green
formula, so its sign and strain convention are fixed. Its velocity is
sublinear and has the stated parities; no harmonic strain can be added.
Uniqueness follows from the harmonic difference and expanding-disc
interior estimates, which make that difference constant and then zero
by parity. Therefore transport on the interior disc is preserved exactly.

Finally use ell=R0/r2 and rho_ell(X)=ell rho_ext(X/ell),
psi_ell(X)=ell^2 psi_ext(X/ell). This is the actual normalized spatial
symmetry. It preserves a and the strain, sends q to q(X/ell), and sends
R to ell R(X/ell). It proves the stated conclusion on r<=R0. Its cubic
coefficients are b/ell^2,e/ell^2, still strictly negative.

## Scope and independent verification

The construction is compact and nonzero, so it attains a positive global
maximum: positivity near the positive y-axis follows from a>0. At such
a maximum grad rho=0 and R=-rho<0. Thus this theorem cannot count as a
global profile, even when every point of an arbitrarily large prescribed
disc satisfies transport. If the same compact construction is dilated
with ell tending to infinity, on every fixed compact set it tends to
rho=ay and psi=-Dxy; that limiting global strain violates canonicity and
the density violates sublinear growth. No admissible global limit is
established by increasing the disc.

The finite checker to be written separately will use Cartesian rational
polynomials to reconstruct (1)-(3), independent dense determinants and
signed Fourier multiplication for (10), and actual polynomial products
for the norm and formal-solution tests. Those finite tests will support
but not replace the preceding all-degree estimates and convergence proof.
No external verification.py or numerics-lane implementation is reused.
