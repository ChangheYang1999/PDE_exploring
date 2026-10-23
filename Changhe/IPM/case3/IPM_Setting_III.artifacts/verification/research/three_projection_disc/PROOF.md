# Three local projections do not bound the center slope

Independent verifier argument, 2026-10-21 UTC. Written before its
associated exact algebra checker. This is a statement about projected
equations on a finite disc. It is not a solution of full-plane IPM.

## Statement

Fix c>1 and put D=c-1. There is a locally finite set E_c of real
numbers, specified below, such that for every
a>=100(c+1) outside E_c and every R0>0 there exists a smooth compactly
supported density rho on the plane with the following properties.

* rho is even in x and odd in y, and has only angular sine modes 1,3,5.
* rho_y(0)=a, and its canonical velocity has psi_xy(0)=-D.
* q=rho/(ay) extends smoothly across y=0, q(0)=1, and q<1 off zero.
* If R=(cX+U).grad rho-rho and
  R_n(r)=integral_0^(2pi) R(r,theta) sin(n theta) dtheta, then
  R_1=R_3=R_5=0 for every 0<r<=R0.

The density and its gradient satisfy the primary growth bound for every
gamma in (0,1), because they are compactly supported. The density is
not an exact global profile. In particular no bound on a depending
only on c and the finite disc radius follows from these three local
projections and the stated one-sided condition.

The fifth density mode is allowed inside the disc. No seventh exterior
density mode is needed. Neither the projected equations outside the
disc nor a nonzero residual inside the disc is part of the assertion.

## Canonical radial equations

Write z=r^2, let a dot mean r d/dr, and set

    rho=r[f sin(theta)+g sin(3theta)+k sin(5theta)].

Smoothness at zero will follow from f analytic in z, g=O(z) and
k=O(z^2). For a compactly supported such density define

    T=int_r^infinity g(s)/s ds,
    S=r^2 int_r^infinity k(s)/s^3 ds,
    J=r^-4 int_0^r s^3 f(s) ds,
    K=r^-6 int_0^r s^5 g(s) ds,
    L=r^-8 int_0^r s^7 k(s) ds,
    u=(T-J)/2, v=(S-K)/2, w=-L/2,
    psi=r^2[u sin(2theta)+v sin(4theta)+w sin(6theta)].   (1)

The moments obey

    dot T=-g, dot S=2S-k, dot J=f-4J,
    dot K=g-6K, dot L=k-8L.                            (2)

For a density mode rF_n sin(n theta), its x derivative contributes
[dot F_n+(1-n)F_n]/2 to sine mode n+1 and
[dot F_n+(1+n)F_n]/2 to sine mode n-1. Also

    -Delta(r^2 h sin(m theta))
      =[-ddot h-4dot h+(m^2-4)h] sin(m theta).

Substitution of (2) proves -Delta psi=rho_x mode by mode. At the
origin u, v/z and w/z^2 are smooth, so psi is smooth there.
Outside the compact support T=S=0 and J,K,L are constant multiples of
r^-4,r^-6,r^-8; hence U=(-psi_y,psi_x)=O(r^-3). The parities are the
required ones. A second parity-preserving sublinear velocity solving
the same divergence and curl equations differs by a harmonic
sublinear vector field. The interior gradient estimate on expanding
discs makes that field constant; its parities remove the constant.
Thus (1) is the canonical full-plane inverse, without an added strain.

Put B=-u-K+S and C=K-3L/2-S. Expanding
U.grad rho/r using the sine product identities gives

    E1=R_1/(pi r)=(c+u)dot f+B dot g+C dot k+F1,
    E3=R_3/(pi r)=B dot f+(c-3L/2)dot g-u dot k+F3,
    E5=R_5/(pi r)=C dot f-u dot g+c dot k+F5,             (3)
    F1=(D+T)f-f^2/4+fg/2+(-J+2K+4S-2T)g
                            +(-4K+6L-6S)k+gk/2,
    F3=(J+2S)f-f^2/4-fg/2+(D+3L)g
                            +(-2J-3T+f+g/2)k,
    F5=Dk+(2J+T)g+2Kf-fg-fk/2-3g^2/4.

For clarity, each pair of density mode n and stream mode m contributes

    -m h_m(F_n+dot F_n) cos(m theta) sin(n theta)
       +n(2h_m+dot h_m)F_n sin(m theta) cos(n theta).

This gives (3) by direct finite multiplication. The same formulas
were reconstructed independently in the parent two-projection audit;
the present proof includes their definitions and derivation.

## Analytic center system

Let Y=(f,g,k,T,S,J,K,L) and

    Y0=(a,0,0,a/4-D,0,a/4,0,0).

Then F1=F3=F5=0 at Y0, and u=-D/2 there. The derivative
matrix in (3) is

    M(Y)=[[c+u,B,C],[B,c-3L/2,-u],[C,-u,c]].

At Y0 it is

    M0=[[(c+1)/2,D/2,0],
        [D/2,c,D/2],
        [0,D/2,c]],
    det M0=(c^3+9c^2-c-1)/8>0.                        (4)

The positivity follows from c^3-c>0 and 9c^2-1>8. Thus (2)-(3),
with E1=E3=E5=0, define an autonomous analytic system

    zY'=Phi(Y),   Phi(Y0)=0,                            (5)

whose first three components are -(1/2)M(Y)^-1(F1,F3,F5)^t.

For a formal series Y=Y0+sum_(j>=1)Y_j z^j, the moment equations at
j=1 imply

    k_1=0, T_1=-g_1/2, J_1=f_1/6, K_1=g_1/8, L_1=0.

The coefficient S_1=H is free. Choose H>0. The first two equations
of (3) become

    [(c+1-a/4), 3D-3a/4] (f_1,g_1)^t=0,
    [D-a/12, 3c-1-a/2] (f_1,g_1)^t+2aH=0.            (6)

The z coefficient of E5 vanishes automatically: its g_1 coefficient
is D-a/4-D+a/4=0. Let

    F(a)=a^2-(4c+20)a+128c-64.

The determinant in (6) is F(a)/16. For a>=100(c+1),
a>4c+20 and F(a)>128c-64>0. Consequently

    f_1=-24Ha(a-4c+4)/F(a),
    g_1=8Ha(a-4c-4)/F(a).                             (7)

At order j>=2 the new moment coefficients are exactly

    T_j=-g_j/(2j), S_j=-k_j/(2j-2),
    J_j=f_j/(2j+4), K_j=g_j/(2j+6), L_j=k_j/(2j+8).

All products involving a new coefficient and a positive-order
coefficient have higher order. Therefore the new coefficients in
(3) have the matrix

    C_j=[[A_j,B_j,0],[C_j^*,E_j,V_j],[0,W_j,E_j]],       (8)
    A_j=(c+1)j-a/4,
    B_j=Dj+2D-a/4-a/(2j),
    C_j^*=Dj-a/4+a/(2j+4),
    E_j=2cj+D-a/2,
    V_j=(j+3)[D-a/(4(j-1))],
    W_j=(j-1)[D-a/(4(j+3))].

The right hand side is determined by lower coefficients. The symbols
C_j and C_j^* denote a matrix and a scalar respectively.
Its determinant is

    Delta_j=A_j(E_j^2-V_j W_j)-B_j C_j^* E_j.           (9)

The two products with apparent poles are polynomials:

    B_j C_j^*=D^2 j(j+2)-Da(j+1)/2+a^2/16,
    V_j W_j=D^2(j+3)(j-1)-Da(j+1)/2+a^2/16.           (10)

Thus Delta_j is a polynomial in a,c,j. Its leading coefficient in a
is -1/64, and for fixed c and bounded a,

    Delta_j=(c^3+9c^2-c-1)j^3+O(j^2)

uniformly as j tends to infinity. Define

    E_c={a real: Delta_j(a,c)=0 for some integer j>=2}.

On a bounded a interval only finitely many j can contribute, and each
polynomial in a has at most three roots. Hence E_c is locally finite.
There are arbitrarily large a>=100(c+1) outside E_c.

For integer c>=2, the polynomial 64 Delta_j in a has integer
coefficients and leading coefficient -1. This follows immediately
from (9)-(10): the only denominators are powers of two dividing 64.
A rational root of a monic integer polynomial is an integer. Indeed,
writing it as r/s in lowest terms and multiplying the cubic equation
by s^3 shows that s divides r^3, hence s=1. Thus every noninteger
rational a>=100(c+1) is outside E_c for integer c>=2. In particular,
for c=2 or 3 every a=1000+m+1/7, m a nonnegative integer, is
admissible. This is an explicit sequence, not just an avoidance
argument.

## Convergence, including the first-order resonance

Write A=D Phi(Y0) and h3=c^3+9c^2-c-1. At every integer j>=2,
the same moment elimination gives

    det(jI-A)
      =j(j-1)(j+2)(j+3)(j+4) Delta_j/h3.               (11)

Indeed multiply the first three characteristic rows by 2M0, whose
determinant is h3, and eliminate the scalar moment rows with the
listed five pivots. All are nonzero at j>=2. Thus jI-A is
invertible there when a is outside E_c. At j=1 the chosen first
coefficient given by (6)-(7) and S_1=H satisfies Y_1=AY_1
exactly. Its free H is permitted; no inversion at j=1 is claimed.
All subsequent coefficients are uniquely determined.

Here is a direct convergence argument. Choose an integer
N>||A||+1, and let P_N(z)=Y0+sum_(j=1)^N Y_j z^j. Its residual
Phi(P_N)-zP_N' has order N+1. Substituting
Y=P_N+z^(N+1)V into (5) gives

    zV'=(A-(N+1)I)V+G(z,V),

where G is analytic, G(0,V)=g0 is independent of V, and
D_V G=O(z) uniformly for bounded V. These facts follow by expanding
Phi at P_N: D Phi(P_N)-A=O(z), and each nonlinear term in V has
an additional factor z^(N+1). Let
V0=((N+1)I-A)^-1 g0. On holomorphic vector functions on a small
disc, continuous on its closure, use the integral map

    TV(z)=int_0^1 t^(NI-A) G(tz,V(tz)) dt.

Because ||t^(NI-A)||<=t^(N-||A||), the integral converges and
TV(0)=V0. On a fixed small ball about the constant function V0,
TV-V0=O(|z|) and its Lipschitz constant is O(|z|).
Shrinking the disc makes this a contraction into that ball.
Differentiating the integral shows that its fixed point solves the
V equation. The data and map are real under complex conjugation,
so the unique fixed point gives a real analytic solution of (5).
This proves convergence, rather than only formal solvability.

## Strict quotient sign and extension

The moment equations and the selected first coefficient give
g=O(z), k=O(z^2), S=Hz+O(z^2), L=O(z^2). Thus rho and psi are
Cartesian analytic near zero. Their density expansion is

    rho=ay+b x^2 y+e y^3+O(r^5),
    b=f_1+3g_1=-192Ha/F(a)<0,
    e=f_1-g_1=-32Ha(a-4c+2)/F(a)<0.

Consequently q=1+(b x^2+e y^2)/a+O(r^4)<1 on a sufficiently
small punctured disc, including the smooth extension across y=0.
Also psi_xy(0)=T(0)-J(0)=-D.

Choose nested radii 0<r2<r3 inside that disc and a smooth radial
cutoff chi equal to one for r<=r2 and zero for r>=r3, with
0<=chi<=1. Multiplication by chi preserves q<1: it decreases
nonnegative q and leaves negative q nonpositive. Write
(f0,g0,k0)=chi(f,g,k).

In a disjoint outer annulus choose nonnegative smooth compactly
supported functions phi3,phi5 with positive weighted integrals.
Finite constants A3,A5 enforce

    int_0^infinity (g0+A3 phi3)/s ds=a/4-D,
    int_0^infinity (k0+A5 phi5)/s^3 ds=H.              (12)

Choose a nonnegative smooth compactly supported zeta, supported
outside r3 and equal to one on both bump supports. Replace f0 by
f0-B0 zeta, where

    B0>3|A3| sup phi3+5|A5| sup phi5.

On those supports f0=g0=k0=0, and the bounds
|sin(3theta)/sin(theta)|<=3,
|sin(5theta)/sin(theta)|<=5 make rho/y strictly negative.
Elsewhere on the support of zeta only its nonpositive first-mode
contribution remains. Hence the final quotient remains below one
off zero. These quotients extend continuously, indeed smoothly,
to the horizontal axis.

For r<=r2, equations (12) make the canonical upper moments

    T=a/4-D-int_0^r g(s)/s ds,
    S=r^2[H-int_0^r k(s)/s^3 ds],

which are precisely the analytic moments selected above. The lower
moments are unchanged. Thus the canonical stream, density, strain,
and all three zero projections are preserved on that disc.
The extended density is smooth and compactly supported; (1)
establishes its full-plane canonical inverse.

Finally set rho_l(X)=l rho(X/l), psi_l(X)=l^2 psi(X/l).
This preserves a, center strain and the quotient inequality, and
R_n[rho_l](r)=l R_n[rho](r/l). Choosing l=R0/r2 supplies the
claimed disc. Since a>0 the density is positive somewhere and
attains a positive maximum on its compact support. At that maximum
grad rho=0, so R=-rho<0. It is therefore not an exact global
profile.

## Scope

This result defeats a slope bound from three projections imposed on
one prescribed finite disc under the stated hypotheses. The
extension annulus need not satisfy any projection. Uniform bounds
for an admissible all-radius limit are absent: dilations can approach
rho=ay and psi=-Dxy locally, violating the primary growth and
sublinear-velocity requirements. The all-radius projected problem
and the primary full-plane IPM endpoint remain open.
