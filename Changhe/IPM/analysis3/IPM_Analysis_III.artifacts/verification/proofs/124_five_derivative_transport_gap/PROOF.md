# Five bounded coefficient derivatives do not imply H2 at order25/4

## Claim under audit

Theory author note27 and work/H2_var.md assert a large-positive-parameter H^(25/4) transport inverse from cylinder coefficient bounds through order5, a smooth nondecreasing order function, axis tangency and a selected low inverse. Those hypotheses do not suffice. The counterexample below satisfies that package and has a smooth forcing whose selected low solution is not in the proposed high space for every sufficiently large positive parameter.

This refutes the stated five-derivative sufficient hypothesis, not H2 for the actual modal IPM field. The latter has stronger finite regularity and requires a repaired argument.

## A locally rough C5 coefficient

On the circle put

 B(theta)=epsilon sum_(n>=1) 2^(-11n/2) cos(2^n theta),    (1)

with 0<epsilon<=1/10. Its derivatives through order5 converge uniformly, since the fifth differentiated series is absolutely dominated by epsilon sum 2^(-n/2). Thus B is C5, is invariant under both coordinate reflections, and has norm in L-infinity less than1/10.

It is not locally H^(23/4) on any nonempty open interval. Here is a localization proof, so global nonmembership alone is not being used. Choose a nonzero smooth cutoff chi supported in that interval with nonzero integral. The Fourier coefficient of chi B at frequency2^n is

 (epsilon/2)2^(-11n/2) chihat(0)+o(2^(-11n/2)).           (2)

For m<n, the separation |2^n-2^m| is at least2^(n-1), so the rapid decay of chihat bounds their sum by O(2^(-Nn)) for arbitrary N. For m>n the separation is at least2^(m-1), and the sum is again O(2^(-Nn)) after choosing N large. The negative-frequency terms have the same bound. Equation(2) follows. The H^(23/4) square sum contains terms comparable to

 2^{(23/2)n} 2^{-11n}=2^{n/2},

and therefore diverges. The same reasoning shows failure of H^(25/4).

## Cylinder field and low realization

Let a and b=exp(3t)a be the weights of proof 123. In particular b(t)=exp(gamma t), gamma=-1/2, for t>=1. Choose a smooth radial cutoff chi_0(t), equal to1 on[3,8], zero outside[2,9], with bounded derivatives. Define

 q(t,theta)=1+chi_0(t)B(theta), vartheta=0,
 V=q(t,theta) r partial_r.

The physical field is tangent to both axes. In the notation of H2_var,

 q_1=q_2=q(3+a'/a).

Every listed coefficient has bounded derivatives through order5. Choose s identically25/4. It is smooth, satisfies the prescribed range and fixed vertical-sector condition, and V.grad s=0. On angular patches separated from both axes the proposed norm is the ordinary H^(25/4) norm of v=h/b, up to smooth bounded factors.

The negative low energy coefficient for T=V.grad-1 on the same R weight is

 1+q+q_t/2+(q/2) partial_t log w.

It is bounded below. Consequently T-lambda has the same future-flow selected low inverse as in the prior transport theorem whenever lambda is sufficiently large. This conclusion also follows directly from the characteristic ODE because q is bounded above and below by positive constants and has bounded first derivatives. No loss of the low inverse causes the example.

## A smooth forcing with a rough high solution

Choose a nonnegative nonzero g in C_c^infinity((6,7)) and a smooth parity-P angular function psi supported away from both axes, equal to1 on some nonempty open interval I in the first quadrant. Take the physical forcing f=b(t)g(t)psi(theta). It is smooth and compactly supported in a regular annulus, hence belongs to R and to the high space.

The equation for v=h/b is

 q partial_t v+[q b'/b-1-lambda]v=g(t)psi(theta).          (3)

At t=4, the entire relevant characteristic segment lies in[3,8], where q=1+B(theta) is independent of t and b'/b=gamma. The selected solution is exactly

 v(4,theta)=psi(theta) H_lambda(1+B(theta)),
 H_lambda(Q)=-Q^(-1) integral_6^7
       exp(-[(lambda+1)/Q-gamma](s-4)) g(s) ds.           (4)

For lambda sufficiently large, for example any lambda>10 after also exceeding the finite low growth bound, H_lambda is real analytic with nonzero derivative on Q in[9/10,11/10]. Indeed the derivative of the positive integrand Q^(-1)exp(-[(lambda+1)/Q-gamma](s-4)) has its own value times

 -1/Q+(lambda+1)(s-4)/Q^2>0.

Thus H_lambda' is strictly negative, and its inverse is analytic on the corresponding compact range.

If the selected solution belonged to H^(25/4) on a neighborhood of {4}xI, the ordinary trace theorem would imply v(4,.) in H^(23/4)(I). Composition with the smooth inverse of H_lambda, using a slightly smaller interval and a smooth extension of the inverse, would imply B in H^(23/4) locally. This contradicts (2). Therefore the selected low solution is not in the claimed high space. The forcing is fixed and smooth; the obstruction occurs for every sufficiently large lambda.

## The failed regularizer estimate

There is also a direct local obstruction to step2 of H2_var. For a C5 coefficient q not in H^(25/4), the expression [Lambda^(25/4),q]w need not be in L2 when w is a fixed smooth function equal to1 near the rough part of q. Its leading term there is Lambda^(25/4)q. With J_delta=<delta D>^(-8), the commutator [Lambda^(25/4)J_delta,q]w therefore cannot have a uniform bound by ||Lambda^(25/4)J_delta w||_2+||w||_2 as delta tends to zero. Otherwise weak compactness would put the limiting commutator in L2. A five-derivative symbolic remainder bound cannot justify that step.

## What remains valid in the draft

The principal commutator symbol

 s xi^T D V xi/<xi>^2
 -8 delta^2 xi^T D V xi/<delta xi>^2
 -(V.grad s)log<xi>

has the stated sign. Left quantization followed on the right by a Fourier multiplier gives the exact product of symbols. The nonnegative logarithmic term has the favorable sign; with suitable coefficient regularity its sharp-Garding lower error is bounded. The radial cutoff has uniformly bounded logarithmic derivative. These facts do not repair the missing coefficient hypothesis by themselves.

For the actual finite-mode C6-joined background, the cylinder field and divided velocity coefficients are C6 with bounded piecewise seventh derivatives, hence locally W^(7,infinity), and their localized H^q regularity reaches q<15/2. This follows from the verified finite-angle Green representation, including the local density term, not from an additional smoothing property of the Riesz transforms. It places the actual coefficients above the counterexample threshold. A complete uniform regularizer or flow-composition proof using that stronger regularity remains a separate task.
