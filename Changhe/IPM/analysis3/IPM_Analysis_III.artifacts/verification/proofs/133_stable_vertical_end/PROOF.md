# Stability of the selected vertical inverse under small coefficient errors

## Statement and exact spaces

Put sigma=25/4 and q=sigma-2=17/4. Let a>0, let K be a compact set of complex numbers c_0 satisfying

 kappa_2=3a/2-Re c_0>=kappa_*>0,

and fix Z>=1. On R_t times R_z consider

 P=partial_t+B(t,z)partial_z+C(t,z),
 B=-az+b(t,z), C=c_0+c(t,z).

The real coefficient b is odd in z and c is complex and even in z. Both vanish for |z|>=Z and have seven bounded weak derivatives in(t,z). Suppose

 ||b||_(W^(7,infinity))+||c||_(W^(7,infinity))<=epsilon.

There are epsilon_*>0 and C_*<infinity, depending only on a,kappa_*,K,Z, such that, if epsilon<=epsilon_*, the following holds. Give P its maximal distributional domain in

 H_y=L2(R^2,|z|^(-9/2)dt dz).

Then P is bijective in H_y. If F is even in z, belongs to H^sigma(R^2), and has trace F(t,0)=0, its selected low solution u=P^(-1)F satisfies, for every finite Z_1,

 u is even, u(t,0)=partial_z u(t,0)=0,
 ||u||_(H^sigma(R times(-Z_1,Z_1)))<=C_(Z_1)||F||_H^sigma.   (1)

Here every Sobolev norm is the ordinary isotropic Bessel-potential norm, except for the explicitly named intermediate space

 E_q=L2(R_t;H^q(R_z)).

No tangential Fourier cutoff or bounded-frequency hypothesis occurs. Constants in(1) are uniform in c_0 in K and in the displayed coefficient ball. No numerical epsilon_* or C_(Z_1) is asserted. This is a theorem about the selected H_y realization. The differently weighted physical low space is not silently identified with H_y.

## The low realization

Since b(t,0)=0, |b(t,z)/z|<=||partial_z b||_infinity. The vector field(1,B) is globally Lipschitz and complete, preserves both half-planes z>0 and z<0, and is tangent to z=0. Its flow and the scalar integrating factor exp(integral C) define a strongly continuous transport group in H_y.

For smooth functions away from z=0 the exact integration by parts is

 Re <Pu,u>_H_y
 = integral [Re C-(partial_z B)/2+(9/4)B/z]|u|^2 |z|^(-9/2).

Its bracket is at most Re c_0-7a/4+C epsilon. Hence the positive-time group contracts at rate at least

 kappa_y=7a/4-Re c_0-C epsilon
         >=kappa_*+a/4-C epsilon>0.                     (2)

For completeness the group generator is the maximal distributional domain, not an additional boundary realization. On each half-plane put z=+/-exp(v) and include the weight Jacobian in the unitary change of unknown. The resulting transport field is(1,B(t,+/-exp(v))/(+/-exp(v))). It and its first derivatives are bounded, and its divergence and transformed potential are bounded. Smooth compactly supported functions form a generator core there: expanding cutoffs have commutators tending strongly to zero, and convolution has a uniformly bounded first-order commutator tending to zero on smooth functions and then on L2 by density. Alternatively the explicit globally Lipschitz flow gives the same identity by testing along its inverse flow. Thus an L2 function whose distributional transport image is L2 belongs to the generator domain. Logarithmic cutoffs in |z| have bounded commutator B/z times their derivative and tend strongly to the identity. They glue the two half-planes distributionally without adding a trace at z=0.

The convergent integral of the positive-time group, with a minus sign, is the two-sided inverse. Its norm is at most1/kappa_y. This also proves uniqueness needed below. The argument applies to the stated W7-infinity coefficients, which have a C6,1 representative, by the same flow or by smooth approximation with uniformly bounded first derivatives.

The assumed F belongs to H_y. Indeed evenness gives its first normal trace zero. Write

 F(t,z)=integral_0^z(z-v)F_zz(t,v)dv.

The H^1_z embedding gives ||F_zz||_(L2_t L-infinity_z)<=C||F||_H^3. Thus its weighted square near zero is bounded by C||F||_H^3 squared times integral_0^1 z^(-1/2)dz. For |z|>=1 the weight is at most1. This proves low membership with a norm bound.

## A stable equation for two normal derivatives

Set w=u_zz. Formally differentiating twice gives

 Qw=F_zz-(B_zz+2C_z)u_z-C_zz u,
 Q=partial_t+B partial_z+C+2B_z.                        (3)

We shall solve(3) first and reconstruct u, so this differentiation does not assume the high regularity being proved.

The frozen operator Q_0=partial_t-az partial_z+c_0-2a generates a contraction on E_q at rate kappa_2=3a/2-Re c_0. One may either change Fourier variables in z or note that the dilation shrinks every nonnegative z Sobolev weight. The t translation is unitary on E_q. To control the perturbation in energy, put Lambda_z^q=(1-partial_z^2)^(q/2). Then

 Re <b partial_z w,w>_E_q
 = Re <b partial_z Lambda_z^q w,Lambda_z^q w>_L2
   +Re <[Lambda_z^q,b]partial_z w,Lambda_z^q w>_L2.

The first term is bounded above by ||b_z||_infinity ||w||_E_q squared/2. The commutator obeys

 ||[Lambda_z^q,b]partial_z w||_L2
 <=C_Z ||b||_(L-infinity_t W_z^(6,infinity)) ||w||_E_q.  (4)

Here is an explicit finite-regularity justification. At each t, the Fourier kernel is bhat_t(eta-zeta) times (<eta>^q-<zeta>^q) i zeta. The elementary inequality

 |(<eta>^q-<zeta>^q)zeta|/<zeta>^q
 <=C_q |eta-zeta|<eta-zeta>^(q-1)

follows by the mean value formula when |eta-zeta|<=|zeta|/2 and by the triangle inequality otherwise. Compact z support and six bounded derivatives give

 |bhat_t(k)|<=C_Z epsilon min(1,|k|^(-6)).

The product with |k|<k>^(q-1) is integrable, because q-6=-7/4<-1. Young's inequality proves(4) uniformly in t. The same Fourier convolution, without the commutator difference, proves multiplication by c+2b_z is bounded on E_q with norm C_Z epsilon. Seven derivatives of b provide the six derivatives of this last coefficient.

Consequently

 Re <Qw,w>_E_q<=-(kappa_*-C_Z epsilon)||w||_E_q^2.       (5)

This is an energy estimate for a first-order perturbation. It is not an assertion that b partial_z is bounded on E_q.

The transport group for Q exists and is strongly continuous on E_q. On each finite time interval its z flow has six uniformly bounded derivatives after the linear dilation is separated; its scalar multiplier has six bounded derivatives. The one-dimensional chain rule and difference quotients give the corresponding composition bound on H^q_z, uniformly in the starting t. Smooth coefficient approximation, the flow formula and Fatou's lemma transfer(5) to the stated finite regularity. Thus, for epsilon small, the negative integral of this group defines an inverse

 ||Q^(-1)||_(E_q to E_q)<=2/kappa_*.                     (6)

It solves the equation distributionally. Uniqueness may be checked already in unweighted L2, where the same transport group has the same or better gap and its generator is the maximal domain by the preceding flow argument. An E_q solution is an L2 solution, so this determines its realization exactly.

## Reconstruction and the bounded lower-order correction

For w in E_q define

 (I^2 w)(t,z)=integral_0^z(z-v)w(t,v)dv.

On a fixed bounded z interval I^2 maps H^q_z boundedly to H^(q+2)_z, with zero value and first derivative. This follows by differentiation and the fractional difference quotient for the highest derivative. Moreover

 ||I^2 w||_H_y<=C||w||_E_q.                             (7)

For |z|<=1 use q>1/2 to bound w in L-infinity_z and integrate z^4|z|^(-9/2). For |z|>=1 Cauchy-Schwarz gives |I^2w(t,z)|^2<=|z|^3 ||w(t,.)||_L2^2/3, and integral_1^infinity z^(-3/2)dz is finite. These calculations prove(7), including the large-z part.

Define the operator

 K w=(B_zz+2C_z)partial_z I^2w+C_zz I^2w.

The displayed coefficients vanish for |z|>=Z. They have five bounded z derivatives and norm at most C epsilon. Smooth localization to a larger fixed strip, the bounded integration maps just proved and the ordinary H^q_z product estimate give

 ||K w||_E_q<=C_Z epsilon ||w||_E_q.                    (8)

To check the product estimate at the precise finite regularity, a compactly supported W5-infinity coefficient has H5 norm bounded by its W5-infinity norm. In one dimension H^q is an algebra for q>1/2; since5>q, multiplication by that coefficient is bounded on H^q with the required small norm. The factors I^2w and its first derivative have at least H^q regularity on the strip.

Choose epsilon still smaller so that ||Q^(-1)K||<=1/2. Equation

 w=Q^(-1)(F_zz-Kw)                                     (9)

then has a unique solution in E_q, with ||w||_E_q<=C||F||_H^sigma. All its operators preserve evenness, so w is even. Let u=I^2w. It belongs to H_y by(7). Equation(3), now justified in distributions, gives

 partial_z^2(Pu-F)=0.

A distribution with zero second z derivative is alpha(t)+beta(t)z. Its value and first z trace vanish: u and u_z have zero traces by construction, F and F_z have zero traces, and B(t,0)=0. This remains legitimate for the t derivative by testing against a smooth t function first; the z traces of the resulting H^(q+2)_z functions commute with distributional differentiation in t. Therefore alpha=beta=0 and Pu=F. It follows that u belongs to the maximal low domain and equals its unique selected inverse. In particular

 ||u||_(L2_t H_z^sigma(-Z_1,Z_1))<=C_(Z_1)||F||_H^sigma. (10)

This step proves regularity of the selected solution without assuming that its differentiated equation already has an E_q solution.

## Recovery of full isotropic regularity

The coefficient of partial_t in P is exactly1. On a bounded z strip extend B to a bounded W7-infinity coefficient without changing it on a slightly smaller strip. For a function v supported there and 1<=r<=sigma, Fourier weights and the elementary split between small and large normal frequency give

 ||v||_H^r<=C_r(||Pv||_H^(r-1)
              +||v||_(L2_t H_z^r)+||v||_H^(r-1)).      (11)

Indeed ||v||_H^r is bounded by a constant times ||v_t||_H^(r-1)+||v||_(L2_t H_z^r). Replace v_t by Pv-Bv_z-Cv. Multiplication by the bounded W7-infinity coefficients is bounded in H^(r-1). For every eta>0,

 ||v_z||_H^(r-1)<=eta||v||_H^r+C_(r,eta)||v||_(L2_t H_z^r).

Absorb the first term after multiplication by the fixed coefficient norm. This proves(11) for smooth v.

Estimate(11) also proves regularity when v is initially only H^(r-1). Use the smoothing multiplier J_e=(1+e^2|xi|^2)^(-N), N>sigma+2. Its commutator with B partial_z is uniformly bounded on H^(r-1), and the commutator with C is bounded there as well. One can verify the finite-regularity assertion by dyadic decomposition: when the coefficient frequency is below the function frequency, the multiplier difference contributes the ratio of those frequencies and cancels the derivative on v; summing the low coefficient frequencies costs its Lipschitz norm. When the coefficient frequency is comparable or larger, its W7-infinity block has norm at most C2^(-7j), while the derivative and the H^p weight, p=r-1<=21/4, cost at most2^((p+1)j). The remaining sum is bounded by sum_j 2^(-(6-p)j), which converges since p<=21/4<6. The comparable-frequency outputs below that scale are bounded by the same sum, or by the geometric Sobolev row weights when p>0. This gives the uniform bound in every p in[0,21/4]; at p=0 the coefficient decay itself makes the row sum finite. This is also the constant-order case of the finite-coefficient dyadic estimate in proof 126. No unproved absolute Fourier moment in two dimensions is imposed on a nondecaying t-dependent coefficient.

Thus P J_e v is uniformly bounded in H^(r-1) by Pv and v. Apply(11) to J_e v, whose pure normal norm is no larger than that of v, and let e tend to zero using Fatou. Nested z cutoffs now give local isotropic H^1,H^2,...,H^6, followed by H^(25/4). Their commutators are B chi' u and have the previous isotropic order. At every stage the pure normal norm is supplied by(10); F has all the needed orders. This proves(1).

## Application to the actual origin-end principal operator

Use the actual normalized modal field V and the exact chart t=log y, z=x/y on y>0. Put q_1=V_1/x and q_2=V_2/y, with their smooth parity extensions at x=0. Write h=x^2 y^(1+delta)u, delta=9/5. Direct differentiation gives

 (V.grad-1-lambda)h/(x^2 y^(1+delta))
 =q_2 partial_t u+(q_1-q_2)z partial_z u
   +[2q_1+(1+delta)q_2-1-lambda]u.

At the exact origin q_1=-A and q_2=D, with D=2A+1. Dividing by q_2 gives the limiting coefficients

 a=Sigma/D, c_0=delta-lambda/D.

For lambda in any compact subset of Re lambda>-m_x, proof 131's exact arithmetic gives

 3a/2-Re c_0=(3Sigma/2-delta D+Re lambda)/D
             >=Sigma/(4D)>0.

The actual inner expansion has ||q_1+A||_W7+||q_2-D||_W7 tending to zero uniformly on every fixed bounded z strip as t tends to minus infinity. To check the regularity and convergence, use the finite exact exponential-polynomial velocity representation of topics68 and69. Its sole exponent-zero term is the certified linear strain; all remaining terms have positive radial exponent. The leading cubic density is the exact polynomial x^2y, so no exponent-zero logarithm occurs. Finite t differentiation, angular differentiation and smooth division by the parity factors preserve convergence of every fixed derivative order. In fact the first positive exponent is2; polynomial logarithmic factors at later exponents still tend to zero with all seven cylinder derivatives. The finite angular degree makes this a uniform statement on the closed strip. This is a property of the exact modal trial, not a conclusion from a C1 approximation alone.

Hence q_2>D/2 sufficiently far left. Divide by q_2, cut off the coefficient differences smoothly in t and z, and extend them by zero outside a larger strip and a left end. The cutoffs may preserve evenness and have fixed derivative bounds. Taking the end sufficiently far left makes the extended coefficients satisfy any required epsilon bound. The theorem therefore applies to this extended actual principal operator. For a localized cofactor solution, its right side includes every cutoff commutator, namely the cutoff derivative along the normalized vector field. On the support where the extension agrees with the actual field, this yields the stated uniform local estimate.

This application supplies a stable selected vertical principal estimate with seven coefficient derivatives and a qualitative sufficiently small end. It does not yet control the angular or radial transition commutators, prove a compact-error estimate for the full coupling, identify the physical low realization with the unweighted H_y realization, or complete H3. Those are separate assertions.
