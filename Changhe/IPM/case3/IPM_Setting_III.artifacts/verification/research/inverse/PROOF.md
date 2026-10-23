# The canonical inverse

Status: independently derived. Exact analytic statement below. Numerical implementation and tests are separate evidence in verification/.

## Statement and notation

Let rho be smooth on R^2, even in x and odd in y, and suppose for some 0<gamma<1 that

    |rho(X)| + (1+|X|)|grad rho(X)| <= C(1+|X|)^gamma.

Put e2=(0,1) and, for Z=(z1,z2)!=0, define

    K(Z) = (-z1*z2/pi, (z1^2-z2^2)/(2*pi)) / |Z|^4.

Then the disk-truncated singular integral

    U(X) = -rho(X)e2/2 + lim_{R->infinity} PV integral_{|Y|<R} K(X-Y)rho(Y)dY

exists. The principal value removes a circle centered at X. The limit at infinity uses circles centered at 0. It defines a smooth field satisfying div U=0, curl U=-rho_x, the required velocity parities, and |U(X)|<=C'(1+|X|)^gamma. This is the unique smooth field satisfying those equations, parities and U=o(|X|). There is a unique stream function odd in both variables with U=(-psi_y,psi_x), and it satisfies -Delta psi=rho_x.

## Proof of convergence and the growth bound

The angular mean of K on a circle is zero. In a disk centered at X, replace rho(Y) by rho(Y)-rho(X). The resulting integrand is locally bounded in absolute value by C_X/|X-Y|, so the principal value exists. Smoothness of rho permits further local Taylor subtraction when differentiating; alternatively the local Poisson equation below gives interior smoothness.

Central oddness rho(-Y)=-rho(Y) and K(-Y)=K(Y) give integral K(-Y)rho(Y)dY=0 on every centered annulus. For |Y|>2|X|,

    |K(X-Y)-K(-Y)| <= C_K |X| |Y|^-3.

Thus the exterior integral can be replaced by the absolutely convergent integral of [K(X-Y)-K(-Y)]rho(Y). Its absolute radial majorant is a constant times |X| integral r^(gamma-2)dr. This also proves that the prescribed disk truncation has a limit. It does not claim absolute convergence of the unsubtracted exterior integral.

For r=|X|>=2, split the integral into |Y-X|<r/2, the remainder of |Y|<2r, and |Y|>2r. On the first region the local gradient bound gives |rho(Y)-rho(X)|<=C r^(gamma-1)|Y-X|. Integrating against |K| gives O(r^gamma). On the second region the kernel is O(r^-2), rho is O(r^gamma), and the area is O(r^2). On the last region the preceding difference bound gives O(r integral_{2r}^infinity s^(gamma-2)ds)=O(r^gamma). The contact term is also O(r^gamma). Bounded X are treated by the same local subtraction and an exterior radius fixed above 2. Therefore U=O((1+r)^gamma)=o(r).

The tail of any positive-order derivative of the subtracted kernel is locally uniformly integrable. The usual distributional differentiation identity for log|Z| can also be verified directly by integrating over an annulus and retaining the small-circle boundary:

    d_i d_j log|Z| = PV(delta_ij/|Z|^2 - 2 z_i z_j/|Z|^4) + pi delta_ij delta_0.

For G(Z)=-(2*pi)^-1 log|Z|, one has -Delta G=delta_0. The two distributions -d_y d_x G and d_x^2 G are exactly K1 and K2-delta_0/2. Applying div and curl gives div U=0 and curl U=-rho_x. The parity statements follow by reflection in the integral. A smooth curl equation and div U=0 imply a smooth stream function locally. Since the plane is simply connected, these local stream functions agree after constants are chosen, giving a global psi. Its two odd parities follow from those of U and determine its constant. The Poisson equation follows from curl U=Delta psi.

For completeness, smoothness of U can be proved without making a global assertion about higher derivatives of rho: split off a compactly supported smooth density agreeing with rho near a given compact set. Its logarithmic potential is smooth there by local elliptic regularity, or by repeated Taylor subtraction. The remaining kernel is smooth on that compact set and all its positive-order derivatives have convergent tails. This gives C-infinity regularity on every compact set.

## Uniqueness and the gauge

The difference V between two canonical velocities has div V=curl V=0. Each component is an entire harmonic function. If an entire harmonic scalar h satisfies h=o(r), its gradient at any fixed point vanishes: the interior gradient estimate on a disk of radius R gives |grad h(X)|<=C R^-1 sup_{B(X,R)}|h|, which tends to zero as R tends to infinity. The estimate itself follows by differentiating the Poisson formula at the disk center. Hence each component of V is constant. Oddness of V1 in x and of V2 in y forces both constants to vanish.

Adding kappa xy to psi would add kappa(-x,y) to U. For kappa!=0 this is not o(r), so it is excluded. An additive stream-function constant changes no velocity, and oddness fixes it to zero.

## Angular Green formula

Write rho=sum_{k odd>=1} b_k(r)sin(k theta). For m=2n>=2, the sin(m theta) coefficient of rho_x is

    f_m = (b_(m-1)'-(m-1)b_(m-1)/r + b_(m+1)'+(m+1)b_(m+1)/r)/2.

The radial Poisson equation is -h_m''-h_m'/r+m^2 h_m/r^2=f_m. Variation of constants gives

    h_m(r) = [r^-m integral_0^r s^(m+1)f_m(s)ds
               +r^m integral_r^infinity s^(1-m)f_m(s)ds]/(2m).

Smoothness removes the singular homogeneous solution at zero; the canonical sublinear velocity removes the growing harmonic solution. The displayed tails converge since f_m=O(r^(gamma-1)). Integrating by parts gives the derivative-free alternative

    h_m(r) = [r^m integral_r^infinity s^-m b_(m+1)(s)ds
               -r^-m integral_0^r s^m b_(m-1)(s)ds]/2.

Boundary terms cancel at r and vanish at the other endpoints. These formulas are comparisons for the direct evaluator, not its implementation.

## Scope and dependencies

This proves the inverse and its gauge for the stated density class, independently of whether the transport equation has a nonzero solution. The proof uses elementary singular-kernel cancellation, the fundamental solution of the plane Laplacian, the Poisson disk formula, and simple connectedness of R^2. No positivity, analyticity, finite critical-point hypothesis or numerical input is used.
