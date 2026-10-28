# Stable horizontal and far principal inverses

## A constant-order transport estimate

We use the following elementary finite-coefficient fact. Let s>1, let m be an integer with m>s, and let v be a vector of bounded W^(m,infinity) coefficients on a Euclidean cylinder of fixed dimension2. Then the real energy contribution of v.grad on H^s is bounded by

 |Re <v.grad f,f>_Hs|<=C_s ||v||_Wm ||f||_Hs^2.          (1)

A bounded Wm scalar multiplier has the analogous H^s bound. The inhomogeneous dyadic norm or the Bessel-potential norm may be used with a fixed equivalence constant; a perturbation of size epsilon gives an O(epsilon) energy change in the Bessel norm itself.

Here are details of the finite-regularity point. Reduce the Bessel norm by its Fourier multiplier Lambda^s. The principal transport contribution is integrated by parts and costs ||div v||_infinity. In the commutator, split coefficient and function frequencies. A coefficient frequency below the function frequency gives a factor of that lower frequency by the multiplier difference and costs the bounded Lipschitz norm plus the summable higher coefficient blocks. A coefficient block at scale2^j has L-infinity norm at most C2^(-mj)||v||_Wm. If the input frequency is2^k with k<j-3, the weighted commutator block is bounded by

 C 2^((s-m)j) 2^((1-s)k)||v||_Wm (2^(sk)||Delta_k f||_2).

The j sum converges since m>s, and the k sum converges since s>1. Comparable input and coefficient frequencies have the extra decay2^(-(m-1)j); output frequencies below that scale gain the usual factor2^(s(l-j)), which is summable for s>0. The low inhomogeneous blocks are bounded directly. Schur's row and column sums give(1). This argument uses only coefficient L-infinity block bounds and works without compact support in the unbounded cylinder direction. The scalar estimate follows from the same decomposition without a derivative. Approximation gives the assertion for weak Wm derivatives.

This proof is also the constant-order version of proof 126. It does not assert that v.grad is a bounded H^s-to-H^s operator.

## Horizontal theorem

Let s=41/20, a>0, and c_0 range over a compact set in C such that

 kappa=Re c_0+a/2-sa>=kappa_*>0.

Let b be real and odd in z and e complex and even in z, compactly supported in a fixed z interval and satisfying

 ||b||_W4+||e||_W4<=epsilon.

On R_t times R_z set

 P=-partial_t+(az+b)partial_z-c_0+e.

For sufficiently small epsilon, depending only on the displayed fixed data, P is bijective on the exact maximal H^s domain and

 ||P^(-1)F||_Hs<=2||F||_Hs/kappa_*.                     (2)

It is also bijective on its maximal unweighted L2 domain. If F is in H^s, the two selected inverses agree. The same conclusions hold on either parity subspace in z.

For the frozen operator, Fourier change of variables in the explicit transport semigroup gives

 ||S_tau||_Hs<=exp[-(Re c_0+a/2-sa)tau], tau>=0.

Equivalently its real energy is at most-kappa||u||_Hs^2. The perturbation changes this energy by at most C epsilon||u||_Hs^2 by(1), since4>s. Thus the exact transport group for P contracts at rate at least kappa_*/2 when epsilon is small. It is strongly continuous on H^s: the finite-time flow is a uniformly smooth diffeomorphism after removing the linear dilation, and its scalar integrating factor has the required bounded derivatives. Smooth approximation and the energy inequality justify the bound for W4 coefficients. The negative integral of the group proves(2) and produces a distributional solution.

In L2 the frozen gap Re c_0+a/2 is larger, so the same smallness choice gives a contracting group there. Its generator is the maximal distributional domain by the logarithmic-coordinate and flow-core argument of topics101 and133. An H^s homogeneous solution is an L2 homogeneous solution and hence vanishes. The H^s inverse therefore is two-sided on the maximal H^s domain: any u there has the same distributional image as the constructed inverse, and their difference vanishes by L2 uniqueness. The L2 and H^s integral solutions coincide in distributions. This proves the asserted selection, not only an estimate on smooth test functions.

## Actual horizontal origin end

In the chart t=log x, z=y/x with x>0, write h=x^(3+delta)u and q_i=V_i/X_i. The exact principal equation is

 (V.grad-1-lambda)h/x^(3+delta)
 =q_1 partial_t u+(q_2-q_1)z partial_z u
   +[(3+delta)q_1-1-lambda]u.

At the origin q_1=-A, q_2=D. Divide by -q_1, which is positive sufficiently far left. The frozen coefficients in the horizontal theorem are

 a=Sigma/A,
 c_0=(Sigma+delta A+lambda)/A,
 kappa=(m_x+Re lambda)/A.

Thus every compact subset of Re lambda>-m_x has a positive uniform gap. The actual inner expansion and parity give small W4 coefficient errors on a fixed z strip sufficiently far left, as explained with seven derivatives in proof 133. Cut them off in t and z, preserving parity, to obtain an operator satisfying the theorem. This gives a stable selected horizontal end inverse with a qualitative end location. Its right side must include every cutoff commutator. No prior identification of the full physical low space with unweighted L2 is needed or asserted for the local theorem.

## Far-end theorem and its axis structure

Fix sigma=25/4 and gamma=-1/2. On the full cylinder C=R_t times S^1 let p(theta)=cos(theta)^2 sin(theta), and fix a vertical sector cutoff chi_y whose transition avoids the vertical and horizontal axes. Let X_infty be the closed parity subspace with norm

 ||v||_Hsigma^2+||chi_y v/p||_Hsigma^2,

where the cofactor is even in the normal coordinate at each vertical axis and has zero trace there. Let q_0>0, let lambda range over a compact set K with

 m+Re lambda>=kappa_*>0, m=1-gamma q_0,

and consider coefficients q,theta_dot with

 ||q-q_0||_W7+||theta_dot||_W7
 +||theta_dot p'/p||_(W7 on the vertical sector)<=epsilon.

Assume q>q_0/2, the physical parity, and theta_dot=0 on each axis. The smoothly extended quotient theta_dot p'/p is required as part of this hypothesis. Define

 T=q partial_t+theta_dot partial_theta+gamma q-1.

For epsilon sufficiently small, T-lambda is bijective on its maximal X_infty domain, with an inverse bound uniform for lambda in K. All constants depend on the fixed sector cutoffs and q_0,K. No numerical inverse bound is claimed.

The frozen operator T_0-lambda=q_0 partial_t-m-lambda is a translation with scalar decay. Its group contracts at rate m+Re lambda in both norm components. For the actual operator the cofactor w=v/p satisfies exactly

 (T-lambda)v/p
 =q partial_t w+theta_dot partial_theta w
  +[gamma q-1-lambda+theta_dot p'/p]w.

The coefficient error in each equation has real H^sigma energy at most C epsilon times the corresponding norm square by(1), since7>sigma. Localizing the cofactor adds theta_dot chi_y' w. On that transition p is bounded away from zero, so its norm is at most C epsilon||v||_Hsigma. This proves a total energy bound with gap at least kappa_*/2. Axis tangency preserves the zero trace, and parity is preserved. The flow therefore gives a strongly continuous contracting group on this closed space. Smooth cofactor trace correction supplies a dense core; alternatively it follows by reflecting, smoothing and subtracting the even trace on a smaller sector.

The group integral gives a bounded right inverse. Uniqueness holds in the ambient unweighted bulk L2 space, where the same small coefficient perturbation preserves the positive frozen gap. The same maximal-domain argument as in the horizontal theorem proves that the constructed inverse is two-sided on exactly {v in X_infty:(T-lambda)v in X_infty}. This includes the axis conditions in the space, rather than adding them after inversion.

## Actual far end

For the exact modal trial, q=V.X/r^2 tends to ell and theta_dot tends to zero. Their cylinder derivatives, and those of theta_dot p'/p on the fixed vertical sector, tend to zero through order7 after subtracting the limiting q. The finite exact outer representation has slowest velocity correction of order exp((k-1)t), with k<1; the matching correction and the other powers decay faster. Parity makes the divided angular coefficient smooth. All these facts follow term by term from the finite outer exponential-polynomial representation, so neither an all-orders regularity assumption at a spline knot nor a merely C1 convergence argument is used.

Here m=1+ell/2=3.787681305..., and Re lambda>-m_x gives a positive far gap. Freeze the coefficients to their limits with a fixed t cutoff before a sufficiently large t. The resulting global extension satisfies the far theorem. Localizing an actual far-end solution then gives its selected principal estimate, with the complete cutoff commutator included in the forcing.

## What remains separate

These two end theorems, together with proof 133, control the principal transport in selected auxiliary realizations. They do not by themselves estimate the full nonlocal coupling on the ends, propagate all transition commutators into a compact error, establish low injectivity, or prove nonlinear closure. In particular a small coefficient in front of a first derivative has been absorbed in energy, not treated as a bounded zeroth-order perturbation.
