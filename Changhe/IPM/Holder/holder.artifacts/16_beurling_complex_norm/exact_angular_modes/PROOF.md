# Exact Holder seminorms of constant-modulus angular modes

## Statement, normalization and dependencies

Let 0<a<1, let n be a positive integer, and identify the Euclidean plane
with C. Define F_(a,n)(0)=0 and

    F_(a,n)(r exp(i theta))=r^a exp(i n theta), r>0.

The Holder seminorm uses the Euclidean distance and complex modulus.
Then

    [F_(a,n)]_a = 2^(1-a) Q_(a,n),
    Q_(a,n) = max_(0<=t<=pi/(2n)) sin(nt)/(sin t)^a.

The ratio at t=0 is its continuous limiting value zero. Complex
conjugation gives the same norm for the negative angular mode. In
particular,

    Q_(a,2)=2/sqrt(2-a) * ((1-a)/(2-a))^((1-a)/2),
    Q_(a,3)=6/(3-a) * (3(1-a)/(4(3-a)))^((1-a)/2).

If M_a denotes the norm of S=T_xx+i T_xy on complex-valued homogeneous
Holder space, in the normalization of ../PROOF.md, then

    M_a >= (a+3)/(2(1-a) Q_(a,3)).

This uses the homogeneous-mode operator calculation proved in
../large_alpha/PROOF.md. No exact operator norm is asserted. The angular
seminorm calculation below is independent of that operator calculation.

## A radial comparison

For v>=0 and 0<=u<=1,

    (v+u)^a-u^a >= (v+1)^a-1,

because the left side decreases in u. Also log cosh is convex and
vanishes at zero. Hence cosh(a x)<=cosh(x)^a for x>=0, and

    sinh(a x)^2 <= cosh(x)^(2a)-1
                 <= (sinh(x)^2+u)^a-u^a.                 (1)

This includes u=0 by continuity.

## Reduction to equal radii

A pair with one point zero has quotient one. For two nonzero points,
common dilation and rotation reduce their radii to exp(x), exp(-x),
x>=0, and their angular separation to 2t with 0<=t<=pi/2. The square
of the Holder quotient is exactly

    2^(2-2a) [sinh(a x)^2+sin(nt)^2]
                   /[sinh(x)^2+sin(t)^2]^a.              (2)

Let L=max_(0<=t<=pi/2) sin(nt)^2/(sin t)^(2a). One has L>=1:
at t=pi/(2n), the numerator is one and the denominator is at most one.
Put u=sin(t)^2. By (1),

    sinh(a x)^2+sin(nt)^2
       <= L [sinh(a x)^2+u^a]
       <= L [sinh(x)^2+u]^a.

Thus (2) is at most 2^(2-2a)L. A pair with equal radii and an angle
maximizing L attains this value. The zero-point quotient is smaller,
since 2^(1-a)sqrt(L)>=1.

For any t in [0,pi/2] there is t' in [0,pi/(2n)] with
sin(nt')=|sin(nt)| and t'<=t: take t'=arcsin(|sin(nt)|)/n. Since sin
is increasing on [0,pi/2], replacing t by t' does not decrease the
quotient. This proves the exact stated one-dimensional maximum.

## Evaluation for the second and third modes

For n=2 set s=sin t, so 0<=s<=1/sqrt(2). The objective is
2 s^(1-a) sqrt(1-s^2). Its logarithmic derivative vanishes exactly at
s^2=(1-a)/(2-a), is positive before and negative after. Substitution
gives Q_(a,2).

For n=3 set s=sin t, 0<=s<=1/2. The objective is
3 s^(1-a)-4 s^(3-a). Its derivative has the sign of
3(1-a)-4(3-a)s^2, so its unique maximum is at
s^2=3(1-a)/(4(3-a)). Substitution gives Q_(a,3).

## Consequence for the complex Beurling lower bound

The previously proved operator identity, modulo a constant, is

    S F_(a,-3) = (a+3)/(2(1-a)) F_(a,-1).

The exact seminorms are 2^(1-a) Q_(a,3) and 2^(1-a), respectively.
Their quotient proves the displayed lower bound. Compact smooth
approximation is justified by the homogeneous-space extension proof in
../large_alpha/PROOF.md, so the result also applies when the operator
norm starts from compact smooth inputs.

As a approaches one, Q_(a,3) tends to three. This improves the
finite-exponent lower bound of the radial-power note while preserving
the sharp endpoint coefficient 2/3 for M_a.

For this specific homogeneous witness there is also a direct compact
approximation avoiding any general vector-valued extension theorem.
Let tau_R(r)=max(0,min(r,2R-r)). Its radial map is one-Lipschitz by the
squared-distance identity in ../compact_flower/PROOF.md. Composing
F_(a,-3) with this map gives a compact Holder function equal to the
original on B(0,R), with no increase in seminorm. The common global
Holder bound controls the tail of every fixed transform increment;
local convergence and then mollification prove the asserted transfer.

## Exact complex angular functional

For a complex Holder function f on the plane, r>0 and integer n>=1,

    |(1/(2 pi)) integral_0^(2 pi) exp(i n theta)
                                  f(r exp(i theta)) dtheta|
       <= b_(a,n) r^a [f]_a,
    b_(a,n)=2^(a-1)/Q_(a,n).

Indeed, subtracting the angular translate by2t gives
2|sin(nt)| times the absolute Fourier coefficient, bounded by
(2r sin t)^a[f]_a. Optimize over t. Equality is attained by the
negative homogeneous angular mode divided by its exact seminorm.
Thus this is an exact global-plane angular estimate, not only an
upper bound for arbitrary data on a circle.
