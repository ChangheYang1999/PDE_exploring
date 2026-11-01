# A distance-weighted Poisson norm obstruction

Status: PROVED for the two general-input counterexamples, after the independent theory-part review at2026-10-31T06:46Z and closure V152. No failure on the generated nonlinear sequence is asserted.

## Statement and notation

Fix delta=2/3. At order n let P_n=2-2n/3. For either a density or stream sine polynomial H(t,theta)=sum h_(q,m)t^q sin(m theta), define the proposed common-center norm

\[
 \|H\|_{n,C}=\sum_{q,m}q!\left(\frac{C}{1+d_{n,m}}\right)^q|h_{q,m}|,
 \qquad d_{n,m}=|m-|P_n||,\quad C>0.
\]

The canonical polynomial Poisson inverse is not uniformly bounded in this norm, even when the inputs have odd density frequencies, the usual linear angular support bound, and log degree at most floor((n-1)/3)-1.

For C=1 there is a sequence with inverse norm ratio at least (3/4)2^k. For every fixed C>0 there is another sequence with ratio at least (3/4)(8/5)^k. Both sequences have k tending to infinity linearly with n. Consequently, adding an arbitrary fixed multiplier C to this particular common-center distance weight does not provide a uniform Poisson estimate on all inputs.

## Proof of the C=1 bound

Choose an integer r>=2, n=3r+2, k=r-1, and m=2r. Then
P_n=2/3-2r, P_n+m=2/3, and P_n+(m-1)=-1/3. Take

\[
 F_n=t^k\sin((m-1)\theta).
\]

The density distance is 1/3 and its norm is k!(3/4)^k. The factored Poisson formula gives the stream frequency m coefficient

\[
 b_m=-\frac12(2/3+D)^{-1}t^k,
 \qquad D=\partial_t.
\]

There are no resonances because P_n is nonintegral. Expanding the finite inverse, its constant coefficient has magnitude
k!/[2(2/3)^(k+1)]. A constant log coefficient has norm weight1, so

\[
 \frac{\|G_n\|_{n,1}}{\|F_n\|_{n,1}}
 \ge \frac34\,2^k.
\]

The other stream frequency contributes a nonnegative amount to the norm and cannot cancel this coefficient. The chosen density frequency is below2n, and k=floor((n-1)/3)-1, as required.

## Proof for every C>0

Choose r>=3, n=3r+1, k=r-1, and m=2r-2. Then
P_n=4/3-2r and P_n+m=-2/3. Set F_n=t^k sin((m-1)theta) again. Now the density distance is5/3 and the output stream distance is2/3. The top log coefficient of

\[
 b_m=-\frac12(-2/3+D)^{-1}t^k
\]

is exactly3/4. Comparing only this top coefficient gives

\[
 \frac{\|G_n\|_{n,C}}{\|F_n\|_{n,C}}
 \ge \frac34
 \left(\frac{C/(1+2/3)}{C/(1+5/3)}\right)^k
 =\frac34(8/5)^k.
\]

The fixed multiplier C cancels. The same support and degree checks apply. This proves the uniform-bound obstruction.

## Dependencies and scope

The only analytic input is the factored polynomial Poisson identity
b_m=-(P_n+m+D)^(-1)a_(m-1)/2+(m-P_n-D)^(-1)a_(m+1)/2, with the second expression interpreted consistently with the factorization; only its first channel is used here. Both examples are nonresonant and have unique polynomial inverses. The sign and factor in the used channel follow directly from the differential Poisson equation.

The norm here uses exactly the same center |P_n| for density and stream, as in the proposed diagnostic. A different density center, a norm of factored components, or restrictions imposed by the nonlinear recurrence are different questions. These examples do not show divergence of the actual stationary series and do not rule out a useful distance-sensitive norm with additional structure.
