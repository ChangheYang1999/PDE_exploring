# Exact strain and power-swirl solutions: scope audit

## Statement

Fix nonzero real a,k, let q=-1-1/a, s=T-t>0, and use the standard cylindrical frame. The field

    v = s^-1 (a r e_r + k r^q e_theta - 2 a z e_z)

solves incompressible Euler away from the axis. It extends as C2 across the axis exactly when q=1 or q>2, and smoothly exactly when q is a positive odd integer. Every member fails uniform sublinearity and decay, and has infinite whole-space kinetic energy. Within the fixed-center isotropic rotating similarity ansatz with positive spatial exponent c, it is stationary exactly when q=1, equivalently a=-1/2. That affine member works for all c and all rotations about this axis but still fails decay.

## Full equation, including pressure

Put F_q(r)=r^(2q)/(2q) for q!=0 and F_0(r)=log r. A pressure is

    p=s^-2 (-(a+a^2)r^2/2 + (a-2a^2)z^2 + k^2 F_q(r)).

Divergence is s^-1(2a-2a)=0. The radial, angular and axial components of material acceleration are respectively

    s^-2 ((a+a^2)r-k^2 r^(2q-1)),
    s^-2 k r^q (1+a(q+1)) = 0,
    s^-2 (-2a+4a^2)z.

They equal -grad p. In the C2 cases the pressure term r^(2q) has sufficient regularity across the axis, and continuity extends the equation there. This checks the momentum equation itself, not only a vorticity reduction.

## Sharp regularity

The Cartesian swirl is s^-1 k r^(q-1)(-y,x,0). For q>2 every derivative of order j<=2 is bounded by C_j r^(q-j), so it extends with zero derivatives at the axis. For q=1 it is linear. For q<=0 it has no continuous axis extension. For 0<q<1 its first difference quotient on the x-axis diverges; for 1<q<2 the second difference quotient diverges. For q=2 its second component on that axis is k s^-1 x|x|, with different one-sided quadratic coefficients. This proves exactly the stated C2 range.

A smooth homogeneous function of positive degree is a homogeneous polynomial: Taylor expansion through the degree, or through the next integer for a nonintegral degree, together with rescaling proves this directly. The x-axis restriction sign(x)|x|^q excludes positive even degrees. Positive odd q give the explicit polynomial (x^2+y^2)^((q-1)/2)(-y,x,0). Hence the smoothness classification is exact.

## Decay and similarity exponent

The axial component grows linearly in z at fixed positive r, and its square has infinite integral on any radial annulus times the whole z-axis. Uniform sublinearity and decay both fail because a!=0.

Rotation about the z-axis acts trivially on this axisymmetric vector field. Substituting x=s^c y into v=s^(c-1)W(y), and writing y in cylindrical coordinates (rho,theta,zeta), gives

    W_r=a rho,  W_z=-2a zeta,
    W_theta=k rho^q s^(c(q-1)).

For c>0 and k!=0, stationarity requires q=1. Conversely q=1 makes W affine and supplies the exact profile for every c and omega. For q!=1, the written family has the amplitude-only exponent c=0. This statement does not classify moving-center or anisotropically scaled ansatzes.

## Source check

The actual source is Weiping Yan, arXiv:1807.05426v1, Theorem 1.1, retained in the literature agent as in the team records from this proof's directory. The title page and pages 2-3 containing the field, angular convention and Cartesian version were independently inspected. The author's angular unit vector is opposite the convention here; changing the arbitrary k to -k reconciles them. The claimed whole-space domain requires the regularity qualification above. The displayed page-3 gradients in the source include spurious z derivatives for components independent of z; they are not used in this audit. Direct momentum differentiation above is decisive.

This confirms LIT25. Smooth polynomial blow-up examples exist within this family, but none satisfies the campaign's decay condition.
