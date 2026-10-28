# A linear remainder for the diagonal sharp norm

## Statement and scope

Use the real homogeneous Holder space modulo constants, the seminorm
[f]_a=sup_{p!=q}|f(p)-f(q)|/|p-q|^a, and the normalized operators of
../../01_setup/PROOF.md. In particular R_1^2=T_xx-I/2 and K_xy(u)=
u_1 u_2/(pi |u|^4). Singular-integral increments use circular principal
values at their two poles and the kernel difference at infinity. The
norm D_a is also the supremum over real smooth compactly supported
inputs, by the compact approximation theorem in the setup.

With C0=1/2+(log(2)-1)/pi, the proposed conclusion is

    D_a = 2/(pi a)+2C0+O(a) as a -> 0+.                    (1)

This is a quantitative asymptotic statement: the O(a) constant is finite
and independent of sufficiently small a. No numerical value for that
lower-error constant, no third-term limit, and no exact finite-exponent
norm is asserted. The explicit upper error is already supplied by
../../08_improved_upper_bounds/explicit_second_term/linear_remainder/PROOF.md.
The new content here is the matching lower error.

Status when written: independent cross-read requested. The argument below
is complete but is not entered as a confirmed theorem until that review.

## Fixed-radius preliminary witness

Put x=(1/2,0), y=-x, H={X>0}, and

    nu(z)=K_xy(z-x)-K_xy(z-y).

The zero-set calculation and circular finite part in
../../06_small_alpha_second_term/diagonal/PROOF.md give, on H,

    sign(nu(X,Y))=sign(Y(X-b(Y))),
    b(Y)^2=[1/4-Y^2+2sqrt(Y^4+Y^2/4+1/16)]/3,
    b(Y)=1/2+O(Y^4),   b'(Y)=O(Y^3).

Let s be signed distance to the graph Gamma={X=b(Y)}, positive on its
right, and put V(z)=(s(z),Y), S(u)=2u_1u_2/|u|, S(0)=0. Choose a fixed
rho>0 sufficiently small that all the local geometric assertions below
hold on B(x,40rho). Rho does not depend on a. For 0<a<=1/4 define

    g_a(u)=(|u|^a+sign(S(u))|S(u)|^a)/2,
    G_a(u)=(min(|u|,rho)^a+sign(S(u))|S(u)|^a)/2,
    W_a(z)=-1/2+G_a(V(z)),
    h_a(z)=(2X)^a/2,   c_a(z)=-1/2+|z-x|^a,
    F_a(z)=max(-h_a(z),min(h_a(z),c_a(z),
                           max(-1/2,min(1/2,W_a(z))))).    (2)

All signed powers are zero when their base is zero. Extend F_a to the
left half-plane by central oddness, and put F_a=0 on X=0. On H,

    -1/2 <= F_a <= 1/2,
    |F_a| <= h_a,
    F_a(x)=-1/2,
    F_a(z) <= -1/2+|z-x|^a.                                (3)

For the last two bounds, the only point requiring a check is the lower
clamp: -h_a(z)<=c_a(z), because [h_a]_a<=1 and h_a(x)=1/2.
Thus the maximum with -h_a does not break the cone bound. Its other
argument is at least -1/2, so the lower range bound is also preserved.

We use the following pair estimates established, with full proofs, in
../local_projection_profile/PROOF.md and ../projection_assembly/PROOF.md.
Write L_a=1+2a^2. The flat profile has [g_a]_a<=L_a. The frozen profile is
the minimum of g_a and rho^a/2+sign(S)|S|^a/2, the second of which has
seminorm at most one. On B(x,R), for R<=40rho,

    Lip(V) <= 1+C R^3,
    |W_a(p)-W_a(q)| <= L_a(1+C R^3)^a |p-q|^a.             (4)

Here and below C denotes a finite geometric constant, not a proposed
numerical coefficient for (1). The derivative bound follows from
b'(Y)=O(Y^3): the two rows of DV are a unit normal and (0,1), with inner
product O(R^3). The ball is convex.

Every pair with at least one point outside B(x,20rho) satisfies

    |W_a(p)-W_a(q)| <= |p-q|^a.                            (5)

For clarity, this assertion does not require rho=a. On the frozen
region the curved signed outer profile has seminorm at most one:
Pi=|S(V)|<=2dist(z,Gamma union {Y=0}); opposite signs use a crossing of
that set, and equal signs use Lip(S o V)<=2sqrt(2) and
(2sqrt(2))^a/2<=1. The unfrozen region |V|<rho lies in B(x,2rho).
For a mixed pair with the other radius R>=20rho, the one remaining
direction of its quotient is at most

    [18^(-a)+(20/9)^a]/2 <= 1  (0<=a<=1/2).

The last inequality follows by convexity in a and checking its endpoints.
All the new entries in the min/max formula (2) have seminorm at most one.
Minima and maxima preserve a common two-point bound. Consequently both
(4) and (5) also hold for F_a on H.

## A Holder envelope whose repair vanishes at the pole

Define, for p in H,

    E_a(p)=inf_{q in H} [F_a(q)+L_a |p-q|^a].              (6)

The infimum is finite. The snowflake triangle inequality proves
[E_a]_a<=L_a; also -1/2<=E_a<=F_a. At p=x, (3) gives E_a(x)=-1/2.
For fixed p, let r=|p-x|. If |p-q|>=r, (3) implies

    F_a(q)+L_a|p-q|^a >= -1/2+r^a >= F_a(p).

Only q with |p-q|<r can lower the envelope below F_a(p). For such q,
both p and q lie in B(x,2r). If r<=20rho, (4) therefore gives

    0 <= F_a(p)-E_a(p)
       <= L_a[(1+8C r^3)^a-1]r^a
       <= 8C L_a a r^(a+3).                              (7)

The last step is the concavity inequality (1+t)^a<=1+at. If
p is outside B(x,20rho), (5) gives E_a(p)=F_a(p).

Set f_a=max(E_a,-h_a) on H, extend centrally oddly, and put f_a=0 on
X=0. Since E_a<=F_a<=h_a, the new function still satisfies |f_a|<=h_a.
It has seminorm at most L_a on each half-plane. Across the two
half-planes, writing X_p>0>X_q,

    |f_a(p)-f_a(q)| <= [(2X_p)^a+(2|X_q|)^a]/2
                    <= (X_p+|X_q|)^a <= |p-q|^a.

The same bound gives continuity at the boundary. Thus

    [f_a]_a<=L_a,
    f_a(x)=-1/2,   f_a(y)=1/2.                            (8)

Moreover 0<=F_a-f_a<=F_a-E_a on H. The repair is supported in the two
radius-20rho pole disks and, by (7), is bounded there by C a r^(a+3).
As |nu|<=C(r^-2+1) in these disks,

    |integral nu(F_a-f_a)| <= C a.                        (9)

This integral is absolutely convergent. The pole values are unchanged,
so the identity contribution to the operator is unchanged as well.

## The fixed-radius value, with a linear error

Let F_0(z)=sign(nu(z))/2 off the zero set. For every fixed such point,
F_a(z)->F_0(z): every positive fixed base raised to a tends to one,
and (2) tends to the stated sign. Choose a fixed 0<delta<rho/4, small
enough for |V(x+u)|<=2|u| and all the geometric comparisons below.
On B(x,delta), freezing is inactive and

    W_a(x+u)=-1/2+g_a(V(x+u)),
    V(x+u)=u+O(r^4),   r=|u|.                             (10)

The clamps added in (2) change W_a by at most

    C a r + C a r^(a+3).                                 (11)

Indeed 0<=g_a(V)<=|V|^a<1, so the constant range clamps are inactive.
The upper h clamp is inactive since W_a<=|V|^a/2<=h_a after choosing
delta with 2delta<1-2delta. The lower h clamp costs at most
(1/2-h_a)_+<=C a r. The pole cone costs at most
(|V|^a-r^a)_+<=C a r^(a+3), by (10) and the mean value theorem.
These bounds remain valid when the clamps are composed.

We claim that the integral of the difference between the curved and flat
profiles, after subtracting its limit at a=0, is O(a):

    integral_(|u|<delta) K_xy(u)
      {F_a(x+u)-[-1/2+g_a(u)]
                    -[F_0(x+u)-sign(K_xy(u))/2]} du = O(a).            (12)

Every bracketed correction here is absolutely integrable. We supply the
logarithmic domination which is needed for the stronger O(a) assertion.
The radial part of (10) costs O(a r^(a+3)) pointwise. For the signed part,
put q(theta)=sin(2theta), t_r(theta)=S(V(x+r e^(i theta)))/r. Then

    t_r=q+O(r^3).

The horizontal roots are unchanged. At each vertical root, the simple
root is displaced by O(r^3), its derivative stays bounded away from
zero, and the associated smooth nonzero factors have logarithmic ratio
O(r^3). Therefore

    integral |q| |log(|t_r|/|q|)| dtheta <= C r^3.          (13)

One direct proof uses u=cos(theta) near a vertical root. The shifted
root is u_r=O(r^3); t_r is a nonzero bounded smooth factor times u-u_r.
On |u|>=C_1 r^3, the logarithm is bounded by C r^3/|u|. On the remaining
interval, substitute u=r^3 v. The weighted logarithmic integral is
O(r^6), uniformly for bounded u_r/r^3, because logarithmic singularities
have uniformly bounded integrals on fixed intervals. Away from these
root neighborhoods, the logarithm is O(r^3). This is the same elementary
weighted-log argument as in ../../06_small_alpha_second_term/linear_lower/PROOF.md.

Where t_r and q have the same sign, the inequality

    |(v^a-w^a)/a|<=|log(v/w)|   (0<v,w<1)

and (13) bound the angular correction divided by a by C r^3.
Where their signs differ, both angles lie in intervals of length
O(r^3) around a vertical root, with |q|<=C r^3. Subtracting the limiting
sign jump leaves an absolute bound

    a[2|log(r)|+|log|t_r||+|log|q||].

Its integral against |q| is at most C a r^6(1+|log(r)|), by the same
rescaling. Division by the kernel's radial factor r and integration
in r proves (12), together with (11). This argument also proves
absolute convergence of the limiting sign correction: its weighted
angular size is O(r^6).

Let k_delta be the own local increment kernel, K_xy(z-x) on B(x,delta),
-K_xy(z-y) on B(y,delta), and zero elsewhere. Put mu_delta=nu-k_delta.
This density is integrable and decays as O(|z|^-3). We also have

    integral mu_delta F_a = integral mu_delta F_0 + O(a).             (14)

To verify the rate, minima and maxima are Lipschitz in their entries.
For each positive base v, uniformly for 0<a<=1/4,

    |(v^a-1)/a| <= (1+v^(1/4))|log(v)|.

On compact sets outside the two pole disks, all logarithms occurring in
(2) are integrable: they are logarithms of distance to the smooth graph,
the horizontal line, or the half-plane boundary, with nonzero smooth
factors. The only intersection of the first two sets in H is the
excluded pole. Inside the pole disks mu_delta is smooth, and logarithms
of r and the same transverse distances remain integrable.
At infinity, Pi=|S(V)| lies between sqrt(2) and 2 times
min(|s|,|Y|). The graph has asymptotes X=|Y|/sqrt(3), with slopes tending
to their nonzero limits. The angular integrals of
|log(Pi/r)| and |log(X/r)| are uniformly bounded on large right
half-circles, using the simple angular crossings of the graph and lines.
The radial majorant is C r^(-7/4)(1+log(r))dr. It is integrable.
This proves (14) by integration of the displayed difference-quotient
bound, with central reflection for the other half-plane.

The two exact flat own integrals add to 2A(a)delta^a/a, where

    A(a)=Gamma(1+a/2)/(2sqrt(pi) Gamma(3/2+a/2)).

Adding (12) at the two poles and (14) gives

    integral_PV nu F_a = 2A(a)delta^a/a+V(delta)+Delta(delta)+O(a),     (15)

where

    V(delta)=(1/2)integral_outside |nu|,
    Delta(delta)=(1/2)integral_disks (|nu|-|own kernel|).

The constant correction in (12) is essential here; it must not be
replaced by a discarded O(delta^6) term. Indeed its sum with
integral mu_delta F_0 is exactly V(delta)+Delta(delta), by splitting
over the two disks and their complement. The finite-part identity is
exact at fixed delta:

    V(delta)+Delta(delta)=1/2-(2/pi)log(delta).             (16)

Finally, the identity term of T_xy-I/2 contributes 1/2, and

    2A(a)delta^a/a
      =2/(pi a)+(2/pi)[log(delta)+log(2)-1]+O(a).

Equations (15)-(16) therefore show

    [(T_xy-I/2)F_a](x)-[(T_xy-I/2)F_a](y)
       =2/(pi a)+1+2(log(2)-1)/pi+O(a).                   (17)

By (9), the same formula holds with f_a. Division by L_a=1+2a^2 costs
only O(a), since (17) is O(1/a). Equation (8), the unit pole separation,
rotation conjugacy, and compact smooth approximation now give the lower
half of (1). The independently proved J_D upper bound gives the other
half. No limit in delta or rho is taken after choosing these two fixed
geometric radii.
