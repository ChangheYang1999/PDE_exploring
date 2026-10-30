# The weighted gradient budget forced by an endpoint profile

Status: new T4 result, OPEN independent Opus review. This proof is written
before its specialization checker. It strengthens the necessary weighted
budget, and bounds the reach of the existing endpoint closure test. It
does not bound the actual distance to a solution from above.

## 1. A tail profile inherits the weighted gradient bound

Let q<0 and let h be a real C1 function on R2 with

    H_q(h)=max(sup_X (1+|X|)^(-q)|h(X)|,
                 sup_X (1+|X|)^(1-q)|grad h(X)|)<=H<infinity.

Suppose b is a real C1 function on the circle and

    sup_theta |r^(-q)h(r,theta)-b(theta)| -> 0 as r -> infinity.

Then

    H >= max_theta max(|b(theta)|,
                         sqrt(q^2 b(theta)^2+b'(theta)^2)).       (1)

No asymptotic expansion for grad h is assumed or obtained.

Proof. The amplitude part follows by taking r to infinity in the
weighted amplitude bound. For the gradient part put
h_R(X)=R^(-q)h(RX). On every compact subset of R2 minus the origin,
h_R converges uniformly to f(X)=|X|^q b(arg X), and

    |grad h_R(X)|<=H (|X|+1/R)^(q-1).

Fix X0 != 0 and 0<epsilon<|X0|. Integrating this gradient bound on a
line segment in the ball B(X0,epsilon), and using q-1<0, gives

    |h_R(X)-h_R(Y)|<=H (|X0|-epsilon+1/R)^(q-1)|X-Y|.

Pass to the uniform limit. As f is C1, differentiation at X0 and
then epsilon down to zero give |grad f(X0)|<=H |X0|^(q-1).
At unit radius the polar components of grad f are (q b,b').
This proves (1), without differentiating a remainder that is only
known to be small in the uniform norm.

## 2. Eliminate the unknown first moment by an angular projection

Let c>1, gamma=1/c, delta=1-gamma and q=gamma-4. Retain every
hypothesis of the moment-resolved endpoint theorem in
../moment_resolved_tail/PROOF.md, Section 2. In addition assume that
A and P are C1 periodic functions, where

    P(theta)=gamma cos(2theta)Theta(theta)+sin(2theta)Theta'(theta).

This extra regularity holds for the finite trigonometric polynomials
used below. For a stationary correction in that theorem,

    b(theta)=[A(theta)+(m/pi)P(theta)]/(4c),
    m=integral_R2 y h(x,y) dx dy.

The theorem provides precisely the uniform tail convergence required
in Section 1. Define angular quadratic norms using the full circle:

    ||v||_0^2=integral_0^(2pi) v(theta)^2 dtheta,
    ||v||_q^2=integral_0^(2pi) [q^2 v(theta)^2+v'(theta)^2] dtheta,
    B0=min_t ||A+tP||_0/(4c),
    B1=min_t ||A+tP||_q/(4c).

Assume P != 0. Both minima are ordinary orthogonal projections, in
their indicated Hilbert norms; their minimizing t need not coincide.
Integrating the squared pointwise bound (1) gives

    H_q(h)>=B1/sqrt(2pi).                                      (2)

It also gives the more precise lower bound with ||A+(m/pi)P||_q in
place of its minimum. For S1 odd sine polynomials
A=sum a_n sin(n theta), P=sum p_n sin(n theta), set w_n=q^2+n^2.
Orthogonality gives the exact finite formulas

    (4c B0)^2=pi [sum a_n^2-(sum a_n p_n)^2/sum p_n^2],
    (4c B1)^2=pi [sum w_n a_n^2
                    -(sum w_n a_n p_n)^2/sum w_n p_n^2].        (3)

Missing coefficients are zero. The minimizing moment for the second
norm is -pi sum(w_n a_n p_n)/sum(w_n p_n^2). All frequencies here are
positive odd integers, so B1>=sqrt(q^2+1) B0. This comparison follows
before taking minima, and is not an assumption about their minimizers.

## 3. Consequence for the existing closure inequality

Assume B0>0. Let E>0 be the valid velocity remainder constant in that
same theorem and let G>0 satisfy its reference-gradient bound. Put
D_delta=1-c(q-delta)>0. The existing closure inequality (CI) of
../endpoint_closure_inequality/PROOF.md has integrand

    r^(2q+1) [B0-sqrt(2pi) ehat(r;H)]_+^2,

where all five terms of ehat are nonnegative and one term is
H E G r^(-delta)/D_delta. By (2), this positive part vanishes for

    r <= r_grad=[E G B1/(D_delta B0)]^(1/delta).

For r>r_grad it is at most B0. Hence, for every admissible H and
starting radius R1, the square root of the right side of (CI) is at most

    cap_grad = B0 r_grad^(q+1)/sqrt(-2q-2).                    (4)

Compared with the earlier amplitude-only cap, the improvement factor
is (B1/B0)^((q+1)/delta), which is less than one. If only a positive
lower bound G>=g0 is known, replacing G by g0 in (4) still gives an
upper bound, since q+1<0. An effective velocity constant for a test
that could reach a specified beta>0 would therefore have to satisfy

    E <= Ecrit(beta)
      = D_delta B0/(g0 B1)
          * [B0/(beta sqrt(-2q-2))]^(delta/(-q-1)).              (5)

This is a necessary condition for the reach of this particular test,
not a sufficient condition for exclusion, coercivity or existence.
Other error terms and a finite R0 can only reduce its reach.
The absence of an upper H_q budget is unchanged: the right side of
(CI) can tend to zero as the allowed H tends to infinity.

## 4. Exact campaign inputs and verification scope

Use c=4076476460239181/2251799813685248 and the exact angular coefficient
maps for 007, 013 and 014 in data/. Their hashes are bound in the input
manifest. These are the endpoint data for the independently audited
three-cutoff references, with all original growth and remainder
hypotheses retained. No statement here asserts that the original,
unrepaired references satisfy the endpoint hypotheses.

The checker must reconstruct both projections independently from the
coefficient maps, compare B0 with the accepted amplitude projection,
and check B1^2>=(q^2+1)B0^2 exactly. It evaluates (2), (4) and (5) in
Arb, with g0=Theta'(0)>0 and the proved E from the moment-resolved
theorem. Hypothetical E=1 rows are diagnostics, not verified velocity
constants. The beta values used in (5) are labeled exactly in JSON;
rounded ceilings are only the stated reference values, not claims
that every scalar framework has that exact admissible radius.

Dependencies: the uniform endpoint theorem T4-335, accepted through
T4-350; its three-cutoff application T4-338 and T4-339, accepted through
T4-365; the explicit (CI) and its nonnegative error terms T4-351.
This result supplies no missing derivative estimates for a PDE inverse.
