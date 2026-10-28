# Uniform control of all angular moments near a pole

## Statement and notation

Put

    q(z)=z/[pi(z^2-1/4)^2]
        =(1/(2pi))[(z-1/2)^(-2)-(z+1/2)^(-2)].

For an integer n>=1 define the complex angular-moment density

    H_n(z)=|q(z)| exp(2in arg q(z)).

The exponential is independent of the branch of arg. At either pole p=1/2 or p=-1/2, for 0<r<=1/4,

    |integral_0^(2pi) H_n(p+r exp(it)) r dt| <= (16/3)r.       (1)

The constant is independent of n. Consequently, for 0<r_1<r_2<=1/4, the absolute value of the moment over the annulus about either pole is at most

    (8/3)(r_2^2-r_1^2).                                      (2)

For the union of the two annuli the bound is twice this. In particular, the circularly regularized moments exist and their convergence near the poles is uniform in n. This supplies the uniformity used in Theorem 5.4 of the team report; it does not rely on bounding the derivative of exp(2in arg q), which would introduce a factor n.

## Proof

First take p=1/2 and write h=r exp(it). Then

    q(p+h)=(1/(2pi h^2))u(h),   u(h)=1-h^2/(1+h)^2.

On |h|=r<=1/4,

    |u-1| <= r^2/(1-r)^2 <= (16/9)r^2 <= 1/9,
    |d u/dt| <= 2r^2/(1-r)^3 <= (128/27)r^2,
    |u| >= 8/9.

Thus u has a single-valued periodic argument eta(t) chosen near zero, and

    |eta'(t)| <= |u'(t)|/|u(t)| <= (16/3)r^2.

Set s(t)=t-eta(t)/2. It obeys s(t+2pi)=s(t)+2pi and

    |s'(t)-1| <= (8/3)r^2 <= 1/6.

It is therefore an orientation-preserving diffeomorphism of the angular circle. Since 2 arg q=-4t+2eta=-4s modulo 2pi, change variables from t to s. The angular moment in (1) becomes

    (1/(2pi r)) integral a_r(s) exp(-4in s) ds,
    a_r(s)=|u(h(t(s)))|/s'(t(s)),

where the integration interval has length 2pi. Its constant-density part is zero for every integer n>=1. The remaining density satisfies

    |a_r-1|
      <= ( ||u|-1| + |s'-1| )/min s'
      <= ((16/9+8/3)/(5/6))r^2
      = (16/3)r^2.

The modulus of the integral is thus bounded by (16/3)r, proving (1).

At p=-1/2 the corresponding expression is

    q(p+h)=-(1/(2pi h^2))[1-h^2/(1-h)^2].

The same bounds hold. The minus sign contributes exp(2in pi)=1 and changes nothing. Integrating (1) in r gives (2).

Away from the two pole disks, H_n is locally integrable. At infinity |H_n|=|q|=O(|z|^(-3)), so the exterior integral is absolutely convergent. The Cauchy estimate (2), uniform in n, proves the final assertion.

## Relation to the Fourier argument

The elementary Fourier coefficients of |cos t| are O(n^(-2)). Their sum is absolutely convergent. The uniform annular estimate above therefore permits the circular-cutoff limit to pass through the angular Fourier series after subtracting the constant term. Alternatively, one may first subtract the leading homogeneous kernels and pass to the limit in the phase variable, as in the parent proof. Both arguments yield the same circular moments.

## Dependencies and scope

This is a direct local calculation from the displayed rational q, ordinary one-variable change of variables, and absolute integration. It does not require a literature theorem. The parent PROOF.md evaluates the moments and proves positivity of the resulting sine series; those are separate steps. The companion rational check verifies the finite coefficient identity for finitely many n only and is a diagnostic, not a proof for all n.
