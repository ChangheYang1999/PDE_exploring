# A one-sided affine defect cannot be flat

Status: CONFIRMED. Independently derived complete informal proof; actual Claude Opus 5.5 lead hand audit at 2026-10-20T21:00Z found no gap. The additional external audit is pending. Date: 2026-10-20.

## Statement

Let rho,psi be a smooth exact primary IPM profile with ell>1, a=rho_y(0)!=0, the specified parities, strictly sublinear density growth and canonical U=o(r). Put

    D=ell-1, A=2ell-1, W=ell X+U,
    H=y-rho/a, V=U2+D y.

Assume the EXTRA one-sided condition

    y H(X)>=0 for all X,

or equivalently rho/(a y)<=1 off y=0. No positivity of this quotient is required. Then H is not flat at the origin. In particular an exact profile with a flat affine defect must have rho/(a y)>1 somewhere.

No global strain or radial-compression cap is assumed. This does not imply the all-degree slope threshold: that separate theorem still requires the strain cap.

## The two moment identities

The exact origin identity and parity give W=(A x,y)+O(r^3) near zero. Exact transport and Poisson give

    W.grad H-H=V,                  Delta V=a H_xx.             (1)

If H is flat, V is flat by the first identity. Both fields are O(r) at infinity; near zero their fixed-order derivatives vanish to arbitrarily high order. For every m>2, define the absolutely convergent moments

    I_m=int H y r^(-2m) dX,   J_m=int V y r^(-2m) dX.

The sign assumption and the exclusion of rho=a y give I_m>0. The independently derived moment identities from ../strain_cap_flat_exclusion/PROOF.md hold:

    J_m=a/[2(m-2)] int H y r^(-2m)(2m x^2/r^2-1) dX,         (2)
    J_m=2m int H y r^(-2m) B dX -(2ell+1)I_m
                                      -int H W2 r^(-2m) dX, (3)
    B=X.W/r^2.

For clarity, no globally bounded DU is necessary to justify (2). Test the distributional elliptic identity against y r^(2-2m) times inner and outer smooth radial cutoffs, then place both derivatives on that test function. The cutoff errors are bounded using only |H|+|V|=O(r) at infinity and flatness at zero. At the outer cutoff they are O(R^(4-2m)); at the inner cutoff they tend to zero faster than a prescribed power. Transport is handled similarly using W=O(r). All retained volume integrals in (2)-(3) are absolutely convergent. The term involving W2 is kept without dividing by y outside compact sets.

Since H y r^(-2m)dX is nonnegative, (2) gives the uniform-in-large-m upper bounds

    J_m/I_m <= a(2m-1)/[2(m-2)]   if a>0,
    J_m/I_m <= |a|/[2(m-2)]      if a<0.                     (4)

It remains to show that (3), without a cap, instead tends to positive infinity.

## Where the weighted measure concentrates

Let

    r_* = inf { |X| : H(X)y>0 }.

This is finite and nonnegative. If r_*>0, the sign assumption and continuity imply H=0 on the entire open ball B_(r_*), including the horizontal axis. Equation (1) gives V=0 there. With phi=psi+Dxy, one has phi_x=V; oddness of phi in x then gives phi=0 in that ball. Consequently W=(A x,y) throughout it. By continuity at its boundary, there is R>r_* on which

    B(X)>=b>0 whenever 0<|X|<R.                             (5)

For r_*=0 the same conclusion follows directly from W=(A x,y)+O(r^3) near zero. One may choose b=1/2 in both cases by shrinking the extra annulus if necessary. This handles an exactly affine open core as well as a nonzero defect at arbitrarily small radii.

Choose r0 with r_*<r0<R such that

    c0=int_(|X|<r0) H y dX>0.

Such a choice exists by the definition of the infimum and continuity. Positivity then gives

    I_m>=c0 r0^(-2m).                                       (6)

For r>=R, choose fixed constants with |H|<=C_H r, |W|<=C_W r. These exist because H=O(r), W=O(r) at infinity and the intervening annulus is compact. In particular |B|<=C_W there. Elementary radial integration gives

    int_(r>=R) H y r^(-2m) dX
           <=2pi C_H R^(4-2m)/(2m-4),
    int_(r>=R) |H W2| r^(-2m) dX
           <=2pi C_H C_W R^(4-2m)/(2m-4).                  (7)

After division by (6), either bound is at most a fixed constant times

    (r0/R)^(2m)/(2m-4).                                    (8)

Thus the outer mass and its first transport coefficient vanish exponentially relative to I_m. Their products with m also vanish. This is a proof of concentration of these moments, not a pointwise inference from flatness.

On the compact ball B_R, smooth parity makes W2/y a smooth bounded quotient. Let C_R be an upper bound for its absolute value there. From (5)-(8),

    [int H y r^(-2m) B dX]/I_m >= b-o(1),
    [int H W2 r^(-2m) dX]/I_m <= C_R+o(1),                 (9)

where m times the first error tends to zero. Equations (3) and (9) yield

    J_m/I_m >= 2mb-(2ell+1)-C_R-o(1) -> +infinity.           (10)

This contradicts (4), proving that H is nonflat.

## Scope and dependencies

The proof uses smoothness, the exact transport and Poisson equations, the origin source relation, parity, the canonical sublinear growth and the advertised extra sign of H y. It does not prove that sign for every exact profile. It does not assume that a small sampled gradient or strain maximum is a global bound. Smooth flat defects with sign oscillations remain outside this exclusion.

The cutoff identities are shared with the independently checked positive-moment argument, but the concentration estimate (5)-(10) is new here. Both cases r_*=0 and r_*>0 are needed; omitting an exactly affine open core would leave a gap. Under spatial scaling the radii r_*,r0,R scale together and all moment ratios are invariant, so the statement has no normalization exception.
