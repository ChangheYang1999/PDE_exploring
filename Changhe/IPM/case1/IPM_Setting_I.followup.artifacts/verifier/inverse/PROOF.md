# A centered real-space formula for the full-plane velocity

Status: proved formula under the stated regularity and growth assumptions. Numerical quadrature of it is evidence, not an enclosure.
Date: 2026-10-20.

## Statement and notation

Suppose $\rho\in C^2_{\mathrm{loc}}(\mathbb R^2)$ is even in $x$ and odd in $y$, and for some $0<\gamma<1$ satisfies $|\rho(Y)|+(1+|Y|)|\nabla\rho(Y)|\leq C(1+|Y|)^\gamma$. For $e_\theta=(\cos\theta,\sin\theta)$ put $k_1(\theta)=-\sin(2\theta)/(2\pi)$ and $k_2(\theta)=\cos(2\theta)/(2\pi)$. The canonical velocity in the task is

$$U_i(X)=-\tfrac12\rho(X)\,\mathbf 1_{i=2}+\int_{-\infty}^{\infty}\int_0^{2\pi}k_i(\theta)D(X,e^t e_\theta)\,d\theta\,dt,$$

where $D(X,z)=[\rho(X+z)+\rho(X-z)]/2-\rho(X)\mathbf1_{|z|<1}$. The two integrals converge absolutely. Changing the radius $1$ to any positive radius leaves the result unchanged. The formula uses the full plane and fixes the same gauge as the symmetric truncation in the task.

## Proof

Write the given kernel as $K_i(re_\theta)=r^{-2}k_i(\theta)$. Each $k_i$ has zero angular average. Thus subtracting the constant $\rho(X)$ on a centered disk changes no truncated annular integral. The kernel is even under $z\mapsto-z$, so averaging the two density values at $X+z$ and $X-z$ also changes no such integral.

For small $z$, Taylor's theorem on a neighbourhood of $X$ gives $D(X,z)=O_X(|z|^2)$. Its absolute integral against $|K(z)|\,dz$ is finite near zero. For large $z$, the two parity assumptions imply $\rho(-z)=-\rho(z)$. Hence

$$\rho(X+z)+\rho(X-z)=[\rho(X+z)-\rho(z)]+[\rho(X-z)-\rho(-z)].$$

If $|z|>2|X|+2$, the gradient bound and the fundamental theorem of calculus bound the right-hand side by $C_X|z|^{\gamma-1}$. Multiplication by $|K(z)|\,dz$ leaves the integrable radial majorant $C_X r^{\gamma-2}\,dr$. On the remaining annulus local continuity is sufficient. This proves absolute convergence of the paired, subtracted integral.

The task's outer truncation uses disks centered at the origin in the density variable. After the change $z=X-Y$, its disk differs from the centered disk $|z|<R$ only in an annulus of width at most $2|X|$ at radius comparable to $R$. The original unpaired integrand on this symmetric difference has absolute integral at most $C_X R^{\gamma-1}$, which tends to zero. Thus the outer limits agree. Polar coordinates followed by $r=e^t$ give the displayed formula, including the local term $-\rho e_2/2$ from the prescribed kernel law. The zero angular average proves independence of the subtraction radius.

## Consequences used by the checker

The integral tail outside a centered radius $R>2|X|+2$ is at most $C_XR^{\gamma-1}/(1-\gamma)$, where the constant depends on a valid gradient-growth bound. When the code has not enclosed that constant it reports truncation differences, not a rigorous tail bound.

The formula preserves the required velocity parities. At $X=0$ the paired density is identically zero and $\rho(0)=0$, so $U(0)=0$ exactly. No harmonic strain $\lambda(-x,y)$ is added. The canonical law is equivalently $U=\nabla^\perp\psi$, with $-\Delta\psi=\rho_x$. Therefore the elliptic residual can be checked as $-\operatorname{curl}U-\rho_x$, where $\operatorname{curl}U=\partial_xU_2-\partial_yU_1$. Checking this identity numerically by Cartesian finite differences checks the same elliptic equation, provided the velocity integral and its numerical errors are reported separately.

## Manufactured density

For $\rho=8x^2y\exp(-x^2-y^2)$, the canonical origin strain is $c=1$. To see this, $x^2y=r^3(\sin\theta+\sin3\theta)/4$, so the $\sin3\theta$ coefficient is $2r^3e^{-r^2}$. The origin identity $c=\int_0^\infty\rho_3(r)r^{-2}\,dr$ gives $c=2\int_0^\infty r e^{-r^2}\,dr=1$. The density is positive in the first quadrant, has exact parity and decays. It is a test of the inverse, not a stationary profile.

Dependencies: the canonical singular-integral kernel specified in TASK/PROMPT and the published report, Taylor's theorem and polar integration. The numerical implementation is newly written in code/. No teammate evaluator is imported or executed. No formalization or build was run.

## Additional manufactured inverses and origin moment convention

Let phi=y exp(-r^2), rho=-Delta phi=(8-4r^2)y exp(-r^2). Then psi=partial_x phi and U=(-phi_xy,phi_xx), giving

    U=(2x(1-2y^2), y(4x^2-2)) exp(-r^2).

This field tests the local delta term and signs. It has rho_y(0)=8 and is not of the normalized cubic class. In general the central moment formula must include the linear-jet correction

    c = -rho_y(0)/4 + integral_0^infinity rho_3(r)/r^2 dr.

For the cubic-normalized candidates rho_y(0)=0, so the simpler formula used above applies. One derivation integrates the nu=2 Green formula for rho_x by parts in r; its lower-end boundary term is precisely -rho_y(0)/4. In particular, the Gaussian potential test has only the first angular sine mode and c=-2, consistent with its analytic U. Omitting the linear-jet correction on manufactured fields would give a false test failure.

A noncompact test is phi=y(1+r^2)^p with p=(1+k)/2 and 0<k<1. Direct differentiation gives

    rho=-4p y(1+r^2)^(p-2)[2+(p+1)r^2],
    U_1=-2p x(1+r^2)^(p-2)[1+r^2+2(p-1)y^2],
    U_2= 2p y(1+r^2)^(p-2)[1+r^2+2(p-1)x^2].

These have the required parities and sublinear growth, divergence zero, curl U=-rho_x, and U(0)=0. They therefore agree with the canonical inverse: the difference is an entire harmonic vector field of sublinear growth, hence constant, and parity makes the constant zero. This tests the cancellation and truncation in a growing density, beyond the rapidly decaying Gaussian test.

For this noncompact test the leading density is C y r^(k-1), C=-4p(p+1). Expanding the paired density at large centered radius and integrating the angular kernel gives the leading discarded tail

    U-U_{R} = (C/4)(x,y) R^(k-1) + O_X(R^(k-3)).

For example integral_0^{2pi} k_1 cos(theta)sin(theta) dtheta=-1/4 and integral k_2 sin(theta)^2 dtheta=-1/4. The remaining radial integral is integral_R^infinity r^(k-2)dr. The expansion error follows by the next homogeneous density term and the third Taylor remainder of the centered pair, each O_X(r^(k-3)) before log-r integration. The formula is for a disk centered at the evaluation point, so the truncated operator itself need not be divergence free. This asymptotic is a manufactured verification device, not a tail enclosure for the numerical candidate.

## A partitioned real-space evaluation for distant points

The centered formula can be expensive at large observation points: the density core then occupies a small part of an angular panel. This is a quadrature issue, not a failure of the identity. Here is a second real-space decomposition used for an independent convergence check.

Fix an observation point X and a positive number a. Choose a smooth radial function chi(t), equal to 1 for t<=1 and 0 for t>=2, and put w=1-chi. The velocity is the sum of the same local delta term, the compact integral

    integral K(z) chi(|z|/a) ([rho(X+z)+rho(X-z)]/2-rho(X)) dz,

and the origin-centered integral

    (1/2) integral rho(Y) [K(X-Y)w(|X-Y|/a)-K(X+Y)w(|X+Y|/a)] dY.

The first integrand is absolutely integrable by the second-order Taylor remainder and compact support. The second has no kernel singularity because w vanishes on a neighborhood of each apparent singularity. Its far pair is O_X(|Y|^(-3)), while rho is O(|Y|^gamma), giving the integrable radial bound r^(gamma-2). To prove the identity, split the prescribed PV kernel with chi+w. Pair the compact term under z -> -z and subtract rho(X); its radial constant has zero angular integral. In the remaining term pair Y with -Y and use rho(-Y)=-rho(Y). These operations hold for finite outer truncations and then by absolute convergence. Thus a is an arbitrary partition parameter and supplies no harmonic freedom.

The code uses a=sqrt(1+|X|^2/64), logarithmic Gauss quadrature for each radial integral, and periodic trapezoidal quadrature for each angle. In the origin-centered part it forms the difference of the two rational kernels algebraically at large |Y|, avoiding subtraction of nearly equal numbers. It does not use a Fourier-mode Green formula or the numerics lane's inverse. Changing angle count, radial panels, angular offset, and this partition is a numerical check only; a rigorous error bound is not claimed.

For clarity, with e=Y/|Y|, t=X/|Y|, d=1+|t|^2 and b=2t.e, set m1=t1*t2+e1*e2, n1=t1*e2+t2*e1, m2=(t1^2-t2^2+e1^2-e2^2)/2, n2=t1*e1-t2*e2. The paired scaled kernels, after removing the common 1/pi, are

    (-4*m1*d*b+2*n1*(d^2+b^2))/(d^2-b^2)^2,
    ( 4*m2*d*b-2*n2*(d^2+b^2))/(d^2-b^2)^2.

These follow by placing the two fractions with denominators (d-b)^2 and (d+b)^2 over a common denominator. The implementation uses them only where both cutoff weights equal one.

Outside-source truncation and gauge: if rho is removed only outside a disk containing X and a neighborhood of X, the resulting velocity difference is divergence free and has zero curl on that neighborhood. Consequently its stream function is harmonic there. The leading allowed term near the center is a harmonic strain lambda*(-x,y). This does not make lambda an admissible free gauge for the full-plane problem: parity together with sublinear growth excludes nonzero global linear strains. A finite-box computation can nevertheless absorb a missing exterior contribution into its fitted strain. The full-plane origin moment and independent cutoff comparisons are therefore necessary checks.

## Detailed derivation of the linear-jet correction in the center strain

Suppose in addition that the density is C^(1,alpha) near0 for some alpha>0, with the preceding parity and growth hypotheses. Write f_n(r) for its physical sine-n Fourier coefficient. The only density modes contributing to sine2theta in rho_x are n=1and3. Direct differentiation in polar coordinates gives

    (rho_x)_2=(f_1'-f_1/r+f_3'+3f_3/r)/2.

For -Delta psi=rho_x, the regular, subquadratic Green solution in angular mode2 has

    lim_(r->0) psi_2(r)/r^2=(1/4)int_0^infinity (rho_x)_2(t)/t dt.

This follows by variation of constants for

    -psi_2''-psi_2'/r+4psi_2/r^2=(rho_x)_2,

whose homogeneous solutions are r^2 and r^(-2):

    psi_2(r)=(1/4)[r^(-2)int_0^r t^3(rho_x)_2(t)dt
                         +r^2 int_r^infinity (rho_x)_2(t)/t dt].

The first term divided by r^2 tends to0, because (rho_x)_2=O(r^alpha) near0. The growth bound makes the upper integral converge, and excludes an additional harmonic r^2 mode in the canonical inverse. Since r^2 sin2theta=2xy, this gives

    c=psi_xy(0)=(1/4)int_0^infinity
                         [f_1'/r-f_1/r^2+f_3'/r+3f_3/r^2]dr.

Now f_1(r)/r tends to rho_y(0) at0, while f_3(r)/r tends to0 there; both quotients tend to0 at infinity by sublinear growth. Integrating the two radial derivatives by parts, first on finite annuli and then using these limits, gives exactly

    c=-rho_y(0)/4+int_0^infinity f_3(r)/r^2 dr.

The Holder remainder makes the last integral convergent at0. This derives the correction with its sign and factor. It vanishes for every cubic-normalized field used in the center-moment certificate, where rho_y(0)=0. The manufactured Gaussian-potential field above tests the nonzero correction separately.
