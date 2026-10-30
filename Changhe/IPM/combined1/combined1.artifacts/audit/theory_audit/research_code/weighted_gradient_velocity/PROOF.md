# The S1 velocity estimate in a weighted gradient norm

Status: new theorem, OPEN pending independent theory review. This answers
the derivative-row question in T2 the review of T4-177, Remark R1. It is an
operator estimate, not an inverse or nonlinear closure theorem.

## Statement

Fix R>0 and

    w_p(X)=(1+|X|²/R²)^(p/2),
    D_p(h)=||w_p grad h||_2.

All tensor norms sum over the two derivative directions and both velocity
components. Let h be real, smooth, compactly supported and centrally odd.
In particular h may be S1, even in x and odd in y. Use the canonical
Fourier velocity U[h]=(-R1 R2 h,R1² h).

A finite constant in

    ||w_p grad U[h]||_2 <= C_p D_p(h)                 (1)

exists on the S1 test class if and only if

    -1 < p < 3.                                     (2)

For 0<=p<3, the following explicit constant works:

    A(p)=(9+p²)/(3-p)²,
    B(p)=(1+p)²/(1+p²)  for 0<=p<=1,
    B(p)=2              for 1<=p<3,
    C_p=[1+sqrt((1+A(p)B(p))/2)]/2.                 (3)

For -1<p<0, one valid, less sharp constant is

    C_p=[1+max(7,1+4/(1+p))]/2.                     (4)

The constants are independent of R. Formula (3) gives C_0=1,
C_1=(1+sqrt(3))/2 and C_(3/2)=(1+sqrt(11/2))/2.
No claim of sharpness of these constants is made. The interval (2) is
sharp. The estimate extends by completion in D_p from the stated test
class. It does not assert the same interval on arbitrary even functions
treated as unrelated gradient components.

## 1. Angular reduction and the radial equation

Let B denote the complex Beurling multiplier

    m_B(xi)=(xi1-i xi2)²/|xi|².

With partial=(partial_x-i partial_y)/2 and
barpartial=(partial_x+i partial_y)/2, the identity
barpartial B=partial holds on the compact test class. For

    h_m=f(r) exp(i m theta),   B h_m=g(r) exp(i(m-2)theta),

put t=log r and a dot for d/dt. Then

    dot g-(m-2)g = dot f+m f.                       (5)

Indeed partial h_m has radial coefficient (f_r+m f/r)/2
and barpartial B h_m has (g_r-(m-2)g/r)/2.
Oddness of h means m is odd, so no zero angular frequency occurs.

The weighted gradient energies of these two modes, divided by 2pi, are

    E_f=integral w²(|dot f|²+m²|f|²)dt,
    E_g=integral w²(|dot g|²+(m-2)²|g|²)dt.         (6)

Here w(t)=(1+exp(2t)/R²)^(p/2). Angular orthogonality
allows these energies to be summed over m.

For m>=3, the solution selected by the canonical multiplier is

    g=f-2(m-1) integral_t^infinity exp((m-2)(t-s))f(s)ds.

For m<=-1, it is

    g=f+2(m-1) integral_-infinity^t exp((m-2)(t-s))f(s)ds.

Both formulas solve (5). Regularity at the origin and the decay of the
canonical multiplier fix the homogeneous solution. The m=1 equation
g-f=C exp(-t) has C=0 by regularity at the origin, so g=f.

For compact smooth f, the negative modes have at worst the exterior
tail g=O(r^-3); the positive modes vanish outside the input support.
At the origin g=O(r^|m-2|). Thus all integrations below have vanishing
boundary terms when 0<=p<3. For a general compact smooth odd h, apply
the calculation to finite angular sums first. Angular truncation
converges in the input gradient norm; the resulting uniform bound
identifies the output limit with the canonical distribution.

## 2. Positive weights: keep the relation between gradient components

Set q=dot w/w. For 0<=p<3,

    0<=q=p exp(2t)/(R²+exp(2t))<=p,
    dot q=2p R² exp(2t)/(R²+exp(2t))²>=0.

Squaring (5) and integrating by parts gives the exact identity

    E_g = E_f - 2 integral q [m|f|²+(m-2)|g|²]w² dt. (7)

Consequently E_g<=E_f for every m>=3. It also holds with equality for
m=1, since g=f and the angular magnitudes are equal.

For a negative mode m=-M, M>=1, put F=w f and G=w g. Multiplication of
(5) by w and integration of the cross terms gives

    integral [|dot G|²+((M+2-q)²+dot q)|G|²]dt
      = integral [|dot F|²+((M+q)²+dot q)|F|²]dt.    (8)

The original energies in the same variables are

    E_g=integral [|dot G|²+((M+2)²+q²+dot q)|G|²]dt,
    E_f=integral [|dot F|²+(M²+q²+dot q)|F|²]dt.    (9)

All potentials in (8) are positive because q<3<=M+2.
For 0<=q<=p and dot q>=0,

    ((M+2)²+q²+dot q)/((M+2-q)²+dot q)
       <= ((M+2)²+q²)/(M+2-q)² <= A(p).            (10)

The first inequality follows because the numerator without dot q is
at least the denominator without dot q. The second follows since
(1+x²)/(1-x)² increases on 0<=x<1, and x=q/(M+2)<=p/3.
Likewise

    ((M+q)²+dot q)/(M²+q²+dot q)
       <= (M+q)²/(M²+q²) <= B(p).                 (11)

For p<=1, q/M<=p and (1+x)²/(1+x²) increases on [0,1].
For p>=1 this ratio is at most 2 for every x>=0.
The derivative terms in (8)-(9) have coefficient1 and A,B>=1.
Thus (8)-(11) prove

    E_g <= A(p)B(p) E_f                            (12)

on each negative mode.

For real h, the coefficients of modes m and -m are conjugates and
their input gradient energies are equal. One member of each pair
satisfies E_g<=E_f and the other satisfies (12). Therefore

    ||w grad B h||_2² <= (1+A(p)B(p))/2 ||w grad h||_2². (13)

Finally the exact identity

    U2[h]+i U1[h]=-(h+B h)/2

retains the local identity term in U2. Differentiate it and use the
triangle inequality in the weighted tensor L2 norm. Equation (13)
gives (3), proving (1) for 0<=p<3.

## 3. Negative weights

Suppose -1<p<0. Now p<=q<=0. For m>=3, the future integral in Section1
conjugated by w is dominated by convolution with
exp(-(m-2+p)s) on s>=0. Its L1 norm is 1/(m-2+p).
For m=-M<=-1, the past integral is dominated by convolution with
exp(-(M+2)s), since w(t)/w(t-s)<=1. Its L1 norm is 1/(M+2).

The radial operators commute with dot differentiation on the compact
test class, as their kernels depend only on t-s. The same estimates
therefore apply separately to f and dot f. Young's inequality and
the triangle inequality imply

    sqrt(E_g/E_f) <= 1+2(m-1)/(m-2+p)
                      <= 1+4/(1+p),              m>=3,

    sqrt(E_g/E_f) <= [(M+2)/M][1+2(M+1)/(M+2)]
                      =3+4/M<=7,                 m=-M<=-1.

The factor (M+2)/M in the second line accounts for the changed angular
frequency in (6); the first line needs no factor because m-2<m.
For m=1 the ratio is1. Summing angular energies gives the Beurling
gradient bound max(7,1+4/(1+p)), and the same velocity identity proves
(4).

## 4. Necessity of p<3

Let h(x,y)=y eta(r), where eta is nonzero, nonnegative, smooth, radial
and compactly supported. This is an S1 test. Put M=int y² eta dX>0.
The off-support kernel of U2 is

    K2(X)=(x²-y²)/(2pi |X|⁴).

The differentiated multipole expansion gives, uniformly in angle,

    U2[h]=M sin(3theta)/(pi r³)+O(r^-4),
    grad U2[h]=grad[M sin(3theta)/(pi r³)]+O(r^-5).

The derivative of the leading term has nonzero angular norm and size
proportional to r^-4. Thus the squared weighted gradient norm contains
a positive multiple of integral r^(2p-7)dr and diverges for p>=3,
including logarithmic divergence at p=3. The input gradient norm is
finite for every p. No finite constant in (1) is then possible.

## 5. Necessity of p>-1

Choose a nonzero nonnegative smooth chi supported in 1<r<2 and put
h_*(r,theta)=chi(r)sin(3theta). This is smooth and S1. Its support is
away from the origin, so no contact term occurs in its central strain.
Direct differentiation of K2 gives

    a=partial_y U2[h_*](0)
      =(1/pi) integral sin(3theta)r^-3 h_*(X)dX
      =integral_1^2 chi(r)r^-2 dr>0.               (14)

For L>=1 let h_L(X)=L h_*(X/L). Scale covariance gives
grad U[h_L](X)=grad U[h_*](X/L). On a fixed small ball its y,2
component therefore tends uniformly to a, while

    D_p(h_L) <= C L^(p+1)                         (15)

for p<0, by the support L<r<2L and direct change of variables.
If p<-1, the right side tends to zero and the output gradient norm
on the fixed ball stays positive. This contradicts (1).

At p=-1, take L_j=4^j and H_n=sum_(j=1)^n h_(L_j).
The supports of their gradients are disjoint, so (15) gives
D_-1(H_n)<=C sqrt(n). Smoothness of U[h_*] near zero gives

    partial_y U2[H_n](X)=n a+O(sum_j |X|/L_j)

uniformly on a fixed small ball. The error is bounded independently
of n. The output gradient norm is therefore at least c n-C', while
the input is O(sqrt(n)). This also contradicts (1). Thus p>-1 is
necessary.

## Completion, dependencies and scope

Angular Poincare on any centered ball controls the local L2 norm of
an odd function by its gradient. The input completion therefore has
an unambiguous local H1 representative; the same holds for the odd
velocity components. The bounded extension in (1) is the canonical
extension from compact smooth tests. No independent choice of a
harmonic velocity field is allowed.

Dependencies: the Fourier multiplier identity for B, polar
differentiation, integration by parts, one-dimensional Young's
inequality, and the displayed multipole kernel. The proof does not use
a claimed A2 bound outside its range. The gain comes from the exact
compatibility relation between both gradient components.

This resolves only the first derivative row. Higher derivative
tensors, the background multiplier costs and the forcing-space tail
requirements remain separate. In particular (1) alone supplies no
common high inverse, no contraction, and no profile certificate.
