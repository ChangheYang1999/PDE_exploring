# An explicit optimized complex Beurling upper bound

## Statement

For 0<a<1 let M_a be the complex homogeneous Holder norm of
S=T_xx+i T_xy, with kernel1/(2 pi conjugate(z)^2), circular principal
values and convergent increments modulo constants. Define

    Q_1=1,
    Q_2=2/sqrt(2-a)*((1-a)/(2-a))^((1-a)/2),
    Q_3=6/(3-a)*(3(1-a)/(4(3-a)))^((1-a)/2),
    b_n=2^(a-1)/Q_n, n=1,2,3,
    c_a=min((b_3+b_1)/2, 2^a/pi),
    B_a=2b_3/(1-a)+c_a,
    s_a=(1-a)B_a/(2b_2),
    F_a=2b_2 s_a^a/[a(1-a)].

Then

    M_a<=F_a.

The conventional complex Beurling norm is2M_a and is therefore at
most2F_a. All constants are elementary explicit functions. No claim
of exact finite-a sharpness is made. The proof uses the exact angular
functional established in ../exact_angular_modes/PROOF.md.

## Proof

Start with a complex compact smooth f. Split the kernel into the disk
|z|<R and its complement, S=N_R+H_R. Circle cancellation removes the
constant f(x) in the disk. The n=2 exact complex angular estimate gives

    |N_R f(x)|<=b_2 R^a [f]_a/a.

For e=(cos beta,sin beta), direct differentiation gives

    partial_e K_S(r exp(i theta))
       =-exp(i(3theta-beta))/(pi r^3).

Differentiating the exterior cutoff distribution also adds the sphere
term with density K_S(z) e dot z/|z|. The bulk derivative has absolute
value at most

    2b_3 [f]_a integral_R^infinity r^(a-2)dr
       =2b_3 R^(a-1)[f]_a/(1-a).

The sphere density satisfies
exp(2i theta) cos(theta-beta)
   =[exp(i(3theta-beta))+exp(i(theta+beta))]/2.
The two exact angular estimates therefore bound the sphere term by
(b_3+b_1)R^(a-1)[f]_a/2.

Alternatively the sphere density changes sign under theta -> theta+pi.
Subtract the antipodal input values and use their distance2R. The
integral of |cos(theta-beta)| over a full circle is4, giving the bound
2^a R^(a-1)[f]_a/pi. Taking the smaller of these two valid sphere
bounds gives

    |partial_e H_R f(x)|<=B_a R^(a-1)[f]_a.

Every angular density here has zero mean. For h=|x-y|, integrate the
far derivative along the line segment and use the two near estimates:

    |Sf(x)-Sf(y)|<=[f]_a[2b_2 R^a/a+B_a h R^(a-1)].

Put R=sh. Differentiation shows that the positive expression
2b_2 s^a/a+B_a s^(a-1) has its unique minimum at s=s_a, with minimum
F_a. The approximation argument in ../PROOF.md passes the inequality
to every complex homogeneous Holder input.

As a tends to zero, b_2 tends to1/2 and s_a has a finite positive limit,
so a F_a tends to1. As a tends to one, b_3 tends to1/3 and
s_a tends to b_3/b_2, so (1-a)F_a tends to2/3. Thus this single closed
formula has both already proved sharp complex endpoint coefficients.
The minimum with any other valid upper bound, including2C_a, is valid.
