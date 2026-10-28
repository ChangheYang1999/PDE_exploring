# Exact raw X3 strain and a certified compact quadrature

## Mathematical object and status

The raw X3 density in this topic is defined by the exact binary64 values in the original file

    case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz.

Its MD5 is 15f8095f7e79dbfa0c50d75e5fe8997a. The source manifest in this team identifies the matching read-only original and local copy. All scalars, knots and coefficients are interpreted as exact dyadic rationals, not uncertainty intervals. The published report explicitly identifies X3 as the candidate, and the follow-up README states that it supplies no newer candidate. No stationarity of this formula is assumed.

Let k=z_0, L be the stored length, r0 the stored origin radius, d=7, m=0,...,200. Let b_m(q) be the clamped degree-seven spline whose first coefficient is zero and whose remaining 375 coefficients are z_(1+375m+i), i=0,...,374. Let T be the Chebyshev polynomial with the final six entries of z as coefficients, in increasing degree. Define

    u=r/L, q=1-(1+u^2)^(-(1-k)/2),
    s=u^2/(1+u^2), chi=u^2/(u^2+r0^2), p=6+2k/(2-k),
    S(q,theta)=sum_(m=0)^200 chi^max(m-1,0) b_m(q) cos(2m theta)
       +s^(p/2)|cos theta|^(p-2) sin^2 theta T(2q-1),
    rho=x^2 y (1+u^2)^((k-3)/2) exp(S).

This proof derives an exact scalar integral and rigorous quadrature bounds. A numerical enclosure becomes certified only after the accompanying calculation and independent output audit succeed. The raw strain is different from the exact-join modal strain of proof 04.

## Regularity and canonical-strain identity

At zero, q is an analytic function of r^2 with a simple zero. Every b_m has first coefficient zero and is a polynomial in q on its first span, so b_m(q)=O(r^2). For m>=2, chi^(m-1)b_m(q) cos(2m theta) is r^(2m) times cos(2m theta) times an analytic function of r^2. The same assertion with degrees zero or two is immediate for m=0,1. Thus these 201 summands are smooth Cartesian functions near zero, with zero constant term.

The exceptional angular factor can be written as

    L^(-p)|x|^(p-2)y^2 (1+r^2/L^2)^(-p/2)T(2q-1).

Since 6<p<7, it is at least C4 locally. After multiplication by x^2 y in the density, its first nonsmooth term is a smooth radial factor times |x|^p y^3. Expanding the exponential, or differentiating its product with x^2, shows the density is at least C^(2,alpha) for any fixed alpha<1. In particular

    rho=x^2 y+O(r^5), grad rho=grad(x^2 y)+O(r^4),
    D2 rho=D2(x^2 y)+O(r^3)

near zero, uniformly in direction. These claims only use the first spline span. Across later knot circles, the defining spline is exactly C6, sufficient for all derivatives used here. At infinity all compact factors and their first two scaled spatial derivatives are bounded, so |D^j rho|=O(r^(k-j)), j=0,1,2. The verified data have 0<k<1.

The canonical density strain formula from proof 01 therefore converges absolutely and is

    c[rho]=(1/pi) integral_R2 rho sin(3theta)/r^3 dX
           =(1/pi) integral_0^infinity integral_0^(2pi)
                        rho(r,theta) sin(3theta) r^(-2) dtheta dr.

With v=1-q and b=2/(1-k), u^2=v^(-b)-1. Differentiation gives

    u du=v^(-b-1)dq/(1-k),
    (1+u^2)^((k-3)/2)=v^((3-k)/(1-k)).

The powers cancel exactly. Parity yields the compact full-plane identity

    c[rho]=4L^2/[pi(1-k)] integral_0^1 integral_0^(pi/2)
       cos^2 theta sin theta sin(3theta) exp(S(q,theta)) dtheta dq. (1)

For compact evaluation use

    s=1-(1-q)^b, chi=s/[s+r0^2(1-s)].

This includes the entire exterior prescribed by the X3 formula; no truncation radius or inverse cutoff is used.

## Piecewise polynomial construction, with exact conformity

On each exact knot span, reconstruct the eight nonzero B-spline basis functions by the Cox recurrence beginning with the degree-zero basis equal to one on that span. Perform this recurrence with exact rational polynomials in the span's affine coordinate. Contract their eight polynomial coefficient vectors with the eight original coefficient rows. This gives the exact degree-seven polynomial for each mode on the span. It is a representation of the original conforming B-spline, not a replacement by independently rounded pieces. The evaluation code checks partition of unity and matches this representation against an independently evaluated de Boor recurrence.

For a subinterval contained in the span, use that same polynomial extension for complex estimates. A polynomial extension need not coincide with the spline outside the span. Only its values and derivative bounds on the integration subinterval are used.

## Rigorous Gaussian error bound

For an interval of length ell and n-point Gauss-Legendre rule, suppose f has a holomorphic extension on the union of all complex disks of radius R centered in the interval and is bounded there by M. Then

    |I f-Q_n f| <= ell M C_n (ell/R)^(2n),
    C_n=(n!)^4/[(2n+1)((2n)!)^2].                         (2)

Here is a proof of the constant. Hermite interpolation at the n Gaussian nodes gives a remainder bounded by sup|f^(2n)|/(2n)! times the square of the monic node polynomial. The integral of that square is ell^(2n+1) C_n, as follows by scaling the Legendre polynomial norm and leading coefficient. Cauchy's inequality bounds sup|f^(2n)|/(2n)! by M/R^(2n). Combining these facts proves (2).

For a q-cell [a,b] of half-width h, choose R_q=2h. The complex rectangle

    Re q in [mid-3h,mid+3h], Im q in [-2h,2h]

contains every required disk. On each such rectangle the computation explicitly verifies Re(1-q)>0, Re s>0 and nonvanishing denominator s+r0^2(1-s). These strict conditions select analytic branches agreeing with the real powers in (1). Bound

    log M_q <= sum_m |chi^max(m-1,0)b_m(q)|
                 +B_p |s^(p/2)T(2q-1)|,
    B_p=((p-2)/p)^((p-2)/2) 2/p.

The value B_p is the maximum of t^(p-2)(1-t^2) on 0<=t<=1, proved by differentiating with respect to t^2. The real angular kernel has modulus at most one.

For an angular cell of physical half-width h, choose R_theta=h. Use the complex rectangle with real half-width 2h and imaginary half-width h. Explicitly verify Re cos(theta)>0 for the branch of cos(theta)^(p-2). Let C_m be the maximum absolute original spline coefficient in mode m and C_T the sum of absolute Chebyshev coefficients. On the real q interval, spline convexity and 0<=chi,s<=1 give

    log M_theta <= sum_m C_m |cos(2m theta)|
                      +C_T |cos(theta)^(p-2)sin^2 theta|.

Multiply exp of this bound by an enclosure of |cos^2 theta sin theta sin(3theta)| on the angular rectangle. These are separate one-variable extensions; no unnecessary joint complex extension is asserted.

For the tensor rule, write I_q I_theta-Q_q Q_theta = (I_q-Q_q)I_theta+Q_q(I_theta-Q_theta). All Gaussian weights are positive and their sum equals the corresponding interval length. Therefore an unscaled total error bound is

    E_q <= (pi/2) sum_qcell ell_q M_q C_(nq),
    E_theta <= sum_thetacell ell_theta M_theta C_(nt) 2^(2nt).

The covered q range has length at most one. Arb enclosures of roots, weights, coefficients, powers and exponentials contain the finite-rule rounding error.

## Endpoint strips and final outward enclosure

Let C_sum=sum C_m and M0=exp(C_sum+C_T B_p). Exclude q in [0,eps_q] and [1-eps_q,1]. Their combined unscaled contribution has modulus at most eps_q pi M0. Exclude theta in [pi/2-d,pi/2], where d=(pi/2)eps_theta. Since cos theta<=pi/2-theta there, that strip contributes at most

    (d^3/3) exp(C_sum+C_T d^(p-2)).

Adding the strip bounds safely overcounts their intersection. These endpoint estimates require only real continuity, so fractional powers at the endpoints cause no missing analytic assumption.

Add all four errors to the ball containing the computed tensor sum, then multiply by the positive exact prefactor in (1). Finally compute the held normalization defect 3/k-1-c[rho] with outward arithmetic. A strict interval for this defect need not contain zero, since the raw stored background is an approximation. No residual, source location, modal approximation error, or inverse theorem follows from this scalar certificate.

## Verification plan

Use exact original input hashes, exact rational spline-polynomial construction, explicit branch checks on every cell, positive Gaussian weights with moment checks through degree 2n-1, a separate de Boor evaluation check, and an independent high-precision recomputation or refinement. Record every mesh, order, precision, mathematical remainder and final ball. The mathematical derivation precedes the code. Recompute reported enclosure containment at higher precision before issuing a CONFIRMED verdict.

## Completed verification and origin consequences

Both tensor sums have completed: 24 by 40 nodes on 789 by 49 cells at 192 bits, and 28 by 44 nodes on 821 by 52 cells at 256 bits. The independent de Boor audit checked 593352 mode evaluations and all raw binary64 values against the exact export. A further 512-bit program checked exact contiguous partition coverage, every complex branch box, all error bounds, Gaussian moment identities, and overlap of the two final enclosures. The refined mathematical error in c is less than 2.728174e-18. The saved ball for the finite sum encloses its arithmetic error separately.

With all displayed decimals interpreted as exact rationals, the final outward report intervals are

    15.726087821623500282 < c[X3] < 15.726087821623500289,
    1.0301137738456e-8 < 3/k-1-c[X3] < 1.0301137743913e-8.

This certifies the defect's sign. For the held exponent ell=1/k, and separately for the normalized exponent ell=(1+c[X3])/3, exact interval arithmetic checks

    a=ell-c<0<b=ell+c,
    (2b-1)/(b-a)>1/2, (1-2a)/(b-a)>1/2,
    1+2ell-c<0<1+2ell+c.

The earlier regularity and tail proof, together with the local canonical kernel estimate, makes U[X3] locally C2 with V=diag(a,b)X+O(r^2), DV=diag(a,b)+O(r). To justify this last regularity directly, split the defining velocity integral with a smooth cutoff equal to one near the point. The compact C^(2,alpha) part has a C^(2,alpha) order-zero singular integral, by subtracting its local Taylor differences in the principal value. The remote differentiated kernel is absolutely integrable against the O(r^k) tail for k<1. No derivative of an unverified fitted velocity is used.

Thus proof 05's full quasimode theorem applies to raw X3 for every X_m, m>=2, both to the held-exponent linearization and to the actual normalized derivative, with their respective V. Proof 09's nonclosed-J theorem also applies. Proof 02's negative origin energy persists, with the general matrix diag(1+2ell-c,1+2ell+c). These facts rule out the stated same-norm inverse or energy estimates on domains containing the constructed sequences. They do not rule out other domain and range spaces, nor prove or exclude a stationary profile.
