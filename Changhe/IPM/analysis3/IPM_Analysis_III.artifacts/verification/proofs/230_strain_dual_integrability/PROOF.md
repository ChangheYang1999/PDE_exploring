# Exact local strain dual conditions for real product exponents

## Statement

Fix1<p<infinity, p'=p/(p-1), and real a,b. On the open unit disk B1 in R2 let w=|x|^(-ap)|y|^(-bp). The parity subspace consists of measurable functions even in x and odd in y, with the Lp(w dX) norm. Initially define the functional on smooth parity functions supported away from the coordinate axes and the origin by

 c_<(h)=(1/pi) integral_B1 sin(3theta) r^(-3) h(X)dX.

It has a bounded extension to the parity subspace if and only if all three strict inequalities hold:

 a+b>1+2/p,   a> -1/p',   b> -1-1/p'.             (1)

Its exact norm, when finite, is

 (1/pi) [Ang_p/((a+b-3)p'+2)]^(1/p'),
 Ang_p=integral_0^(2pi)|sin(3theta)|^p' |cos theta|^(ap') |sin theta|^(bp') dtheta.  (2)

The last two conditions are automatic for a,b>=0. Thus the report's radial-only criterion is valid under that additional convention, or if finiteness of Ang_p is explicitly assumed. For a box in place of the disk, (1) remains the criterion, but the exact constant in(2) changes as described below.

## Proof of the exact norm

The isometry h->h w^(1/p) sends Lp(w) to ordinary Lp. The representing kernel there is K w^(-1/p), K=(1/pi)sin(3theta)r^(-3). The usual Holder inequality gives the upper bound by its Lp' norm. Equality in the full dual norm follows by the truncated extremizers sign(K)|K|^(p'-1)w^(-1/(p-1)), with cutoffs to compact regions away from the singular sets; the kernel, weight and truncations have the physical parity, so these are admissible in the parity subspace. Smooth approximation on those compact regions proves equality already on the stated smooth core. If the dual integral diverges, the same truncations and normalization make the functional unbounded. Hence symmetry does not remove any divergence.

In polar coordinates the p'-th power of the norm is

 pi^(-p') [integral_0^1 r^((a+b-3)p'+1)dr] Ang_p.

The radial factor is finite exactly under the first condition of(1), and then equals1/((a+b-3)p'+2). Near the vertical axis sin(3theta) has a nonzero limit, so the angular singularity is |theta-pi/2|^(ap'), integrable exactly when ap'>-1. Near the horizontal axis sin(3theta) vanishes to first order, so the singularity is |theta|^((1+b)p'), integrable exactly when (1+b)p'>-1. All other angular points are regular or zeros of the numerator. These are precisely the remaining inequalities of(1), proving the claim including failure at equality.

## Why a radial condition alone is insufficient without angular hypotheses

For example p=2,a=5,b=-2 has a+b=3>2=1+2/p, but b=-2<=-3/2. Its dual kernel is not square integrable near y=0 on any fixed annulus. The norm is therefore infinite although the radial test passes.

An explicit packet confirms this. Choose a nonnegative even smooth phi(x) supported near x=3/4 and x=-3/4, and an odd smooth psi with nonnegative nonzero restriction on1<y<2. Take h_epsilon(x,y)=epsilon^(-2)phi(x)psi(y/epsilon). For small epsilon its support lies in B1 away from the axes. Since w=|x|^(-10)|y|^4, ||h_epsilon||Lp(w) is a positive constant times epsilon^(1/2). The kernel on this support is K(x,y)=3y/(pi x^4)+O(y^3), uniformly in x. Thus c_<(h_epsilon) tends to

 (3/pi)[integral phi(x)x^(-4)dx][integral z psi(z)dz]>0.

The functional is unbounded. No PDE mapping or inverse conclusion is inferred from this elementary dual example.

## The constant on a rectangle

For Q={|x|<R_x,|y|<R_y} with positive finite R_x,R_y, set R(theta)=min(R_x/|cos theta|,R_y/|sin theta|), with the natural infinite endpoint conventions before taking the minimum. This positive radial boundary is bounded above and below. With s=(a+b-3)p'+2>0, the exact p'-th power of the norm is

 pi^(-p')/s integral_0^(2pi)|sin(3theta)|^p' |cos theta|^(ap') |sin theta|^(bp') R(theta)^s dtheta.

Thus the same three integrability tests hold, while the simple factorization(2) is the disk formula. This distinction matters when a printed constant is claimed exact.

Dependencies: elementary weighted Lp duality, polar integration and the strain kernel already proved in proof 31. No numerical computation is used. This supplies explicit hypotheses for the general-p paragraph of the report and leaves the previously verified nonnegative parameters unchanged.
