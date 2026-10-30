# Finite logarithmic tails are forced to be pure powers

Status: proposed theorem, OPEN independent Opus review. This extends the
finite-power classification in T4-234 and T4-249. It is a necessary
far-field classification and gives no inverse or existence result.

## Exact statement

Fix c>1, gamma=1/c, delta=1-gamma and a with

    -2<a<=1+gamma.

Let E_a=L2(R2,(1+|X|2)^(-a)dX), with real S1 densities, meaning even
in x and odd in y. Let E be a finite subset of [a-1,1). For each e in E
let P_e(L,theta) be a polynomial in L whose coefficients are smooth S1
angular functions. Combine equal exponents first. Let chi be a smooth
radial cutoff, zero for r<=1 and one for r>=2, and put

    R(r,theta)=sum_(e in E) chi(r) r^e P_e(log r,theta).

The canonical velocity U_R is constructed below. On S1 E_a define U[h]
by the continuous extension of the Fourier multiplier with symbol
(xi1 xi2/|xi|2,-xi1^2/|xi|2). Suppose h in S1 E_a and rho=R+h satisfies

    c div(X rho)-(2c+1)rho+div((U_R+U[h])rho)=0          (1)

as a distribution. Then every P_e is independent of L. Every nonzero
P_e has exponent

    e=e_j=1-(j+1)delta, 0<=j<N_a,
    N_a=floor((2-a)/delta).

Writing P_(e_j)=Theta_j and supplying zero coefficients for absent powers,
the profiles obey, for 1<=j<N_a,

    Theta_j=1/[j(c-1)] sum_(l+m=j-1)
       [-e_m Psi_l' Theta_m+(e_l+1)Psi_l Theta_m'],      (2)
    [partial_theta2+(e_j+1)^2]Psi_j
       =-e_j cos(theta)Theta_j+sin(theta)Theta_j'.      (3)

Here Psi_j is the unique smooth sum of positive even sine harmonics.
If E has a nonzero profile, its largest exponent is gamma and Theta_0
is nonzero. If every profile vanishes, the conclusion includes this
trivial tail. Conversely, the smooth reference residual belongs to E_a
if and only if these pure-power relations hold.

In particular, finitely many polynomial powers of log r add no independent
far-field coordinates in this class. This does not treat inverse powers
of log r, fractional logarithmic powers, infinite asymptotic series,
oscillations in log r, or remainders outside E_a.

## 1. Canonical velocity of one logarithmic sector

For e in [a-1,1), one has -2<e+1<2. On positive even sine harmonics,

    A_e=partial_theta2+(e+1)^2

has nonzero eigenvalues (e+1)^2-m^2 for m=2,4,... . Dividing rapidly
decaying Fourier coefficients by these eigenvalues defines a smooth
inverse. It gains two angular derivatives.

Seek the stream function r^(e+1)Q_e(L,theta), L=log r, where Q_e is a
polynomial of degree at most deg P_e in L. The equation
Delta psi=-partial_x(r^e P_e) is equivalent to

    [A_e+2(e+1)partial_L+partial_L2]Q_e
       =-cos(theta)[e P_e+partial_L P_e]
          +sin(theta)partial_theta P_e.               (4)

This follows from the polar Laplacian and the chain rule. The right side
has the odd-x, odd-y stream parity. Write its coefficients as H_k and
Q_e=sum_k Q_k L^k. Starting from the highest degree and setting missing
higher coefficients to zero, define

    Q_k=A_e^-1[H_k-2(e+1)(k+1)Q_(k+1)
                         -(k+2)(k+1)Q_(k+2)].         (5)

This gives the unique polynomial Q_e solving (4). No logarithmic
resonance is hidden in this inversion: the only relevant angular
frequencies are m=2,4,..., and |e+1|<2.

Put V=grad-perp sum_e chi r^(e+1)Q_e, with
 grad-perp=(-partial_y,partial_x), and define

    g=curl V+partial_x R, G(X)=log|X|/(2pi),
    W=grad-perp(G*g), U_R=V-W.                        (6)

Equation (4) makes g smooth and supported in 1<=r<=2. It is odd in both
x and y, so int g=int xg=int yg=0. Subtracting the constant and linear
Taylor terms of grad G(X-Y) in the convolution gives

    W=O(r^-3), grad W=O(r^-4)                         (7)

uniformly in angle. All fields are smooth across the cutoff region.
Consequently U_R is divergence-free, has curl -partial_x R and S1
velocity parity. Outside r=2 its homogeneous-logarithmic components are

    (U_R)_r=-sum_e r^e partial_theta Q_e+O(r^-3),
    (U_R)_theta=sum_e r^e[(e+1)Q_e+partial_L Q_e]
                       +O(r^-3).                    (8)

Let e_max=max E when E is nonempty. For any beta with
max(e_max,0)<beta<1, the finite logarithmic factors give
U_R=O(r^beta), R=O(r^beta), grad R=O(r^(beta-1)).

The already audited odd weighted multiplier estimate and reciprocal-weight
duality give ||U[h]||_E_a<=2/(2-|a|)||h||_E_a for |a|<2. The identity
part in U2+iU1=-(I+B)h/2 is retained. This includes the full stated range.
The construction and this extension are independent of the cutoff:
the difference has zero divergence and curl and belongs to
O(r^beta)+E_a. Its harmonic interior gradient is bounded at a fixed point
by C L^(beta-1)+C L^(max(a,0)-2), tending to zero. It is constant and then
zero by parity. Products in (1) are locally integrable because E_a is
locally L2 and the reference fields are smooth.

## 2. Residual polynomial coefficients

For two exponents e,f define the angular-logarithmic polynomial

    B_(e,f)=-partial_theta Q_e [f P_f+partial_L P_f]
             +[(e+1)Q_e+partial_L Q_e] partial_theta P_f.

The corresponding transport product is exactly r^(e+f-1)B_(e,f).
The dilation and zeroth-order part is

    (cX.grad-1)(r^e P_e)
      =r^e[(ce-1)P_e+c partial_L P_e].                 (9)

There are finitely many powers in the residual. Terms of exponent q<a-1
are in E_a even with any fixed nonnegative logarithmic degree, because
int r^(2q-2a+1)(log r)^(2k)dr converges. The W.grad R term is also in
E_a: its size is O(r^(e_max-4)(log r)^d), with e_max-4<-3<a-1.
Compact terms belong to E_a. Thus, modulo an E_a remainder, the residual
is a finite sum of r^q times polynomials in log r, with q>=a-1.

## 3. Weighted weak necessity includes the logarithmic endpoint

Suppose a residual coefficient is nonzero. Choose its largest exponent
q, and then the largest nonzero logarithmic degree k at that exponent.
Let A(theta) be that nonzero angular coefficient. Choose a smooth
nonnegative nonzero eta supported in (1,2), and test with

    phi_L=L^-1 eta(r/L) A(theta).

On this annulus log r=log L+log(r/L), so direct radial scaling gives

    int F[R] phi_L
       =L^(q+1)(log L)^k [C+o(1)],
    C=(int_1^2 s^(q+1)eta(s)ds)(int_0^(2pi) A(theta)^2dtheta)>0. (10)

Lower logarithmic degrees and lower exponents are negligible. Pairing
the E_a remainder with phi_L is o(L^a), hence negligible as well because
q+1>=a and k>=0.

Write m_L=||w_a h||_(L<r<2L) and n_L=||w_a U[h]||_(L<r<2L), where
w_a=(1+r2)^(-a/2). Both tend to zero. Subtracting the reference residual
from (1), weighted Cauchy-Schwarz on the annulus gives respectively

    O(L^a m_L),
    O(L^(a+beta-1) m_L),
    O(L^(a+beta-1) n_L),
    O(L^(2a-2) m_L n_L)                               (11)

for dilation/zeroth order, reference advection, velocity acting on R,
and quadratic advection. The third term is integrated by parts using
div U[h]=0. The last uses ||grad phi_L||infinity=O(L^-2).
Divide (11) by L^(q+1)(log L)^k. Since q+1>=a, beta<1, a<2 and k>=0,
each quotient tends to zero. This contradicts (10). It follows that
every retained residual polynomial is identically zero. No derivative
or pointwise decay of h was assumed. The borderline power q=a-1 is
included, for every nonnegative integral logarithmic degree.

The same leading-term argument shows that the reference residual belongs
to E_a exactly when all retained polynomial coefficients vanish: a
nonzero top coefficient yields a divergent weighted radial integral,
including int r^-1(log r)^(2k)dr at the endpoint.

## 4. Descending induction removes every logarithm

Adjoin gamma to E with zero profile if absent. Set
D={1-e:e in E}; every element is positive. Form all finite nonempty sums
of elements of D that are at most 2-a, and let Ebar be one minus those
sums. This is a finite set, because each sum has at most
floor((2-a)/min D) terms. It contains E and is closed under e+f-1 whenever
the result is at least a-1. Supply zero polynomials for newly adjoined
powers. All exponents still lie in [a-1,1), so (4)-(8) apply to them.

By Section 3, at each q in Ebar,

    (cq-1)P_q+c partial_L P_q
         +sum_(e+f-1=q) B_(e,f)=0.                    (12)

Every product on this line uses e>q and f>q, since e,f<1. Order Ebar
from largest to smallest. Above gamma, all previously treated profiles
are zero. The equation is then (cq-1)P_q+c P_q'=0 with cq-1 nonzero.
Looking at the highest logarithmic coefficient forces P_q=0.

At q=gamma the products again vanish and c P_gamma'=0. Thus P_gamma is
a constant angular profile Theta_0. Below gamma, suppose the larger
profiles are independent of L and supported on the ladder e_j.
Equation (4) then makes their Q_e independent of L, so the forcing
in (12) is independent of L. Because cq-1 is nonzero, the highest-degree
coefficient once again excludes every positive logarithmic degree in
P_q. If q is off the ladder, no two larger nonzero profiles can produce
q, because e_l+e_m-1=e_(l+m+1). Hence P_q=0 there. On the ladder,
(12) is precisely (2), since ce_j-1=-j(c-1).

This proves the complete classification and the converse residual
membership statement. If Theta_0 is zero, the same induction makes
every profile zero. There is no free logarithmic coefficient at any
level and no free additional pure-power coefficient.

## Dependencies and limits

Analytic dependencies: polar calculus, Fourier inversion on smooth
angular functions, the compact-curl construction and harmonic uniqueness
of T4-234/249, the audited odd weighted multiplier theorem and its
reciprocal-weight duality, and elementary weighted Cauchy-Schwarz.
No numerical input, large table, external computation or formal build is
needed. The theorem concerns compatibility of an assumed exact weak
solution with finite tails; it supplies neither that solution nor a
linearized inverse. Candidate-specific negative-weight applications
must retain every regularization-generated power above their threshold.
