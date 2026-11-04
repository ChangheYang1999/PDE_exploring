# Local outgoing obstruction at a vortical stagnation point

## Exact statement

Let `U in C^2` and `P in C^1` solve the rotating Euler profile equation in a neighborhood of `p`, with `div U=0`. Let `B=(cI-omega J)y+U`, `Omega=curl U`, and suppose `B(p)=0`, `Omega(p)!=0`. Assume there are `kappa in R` and `epsilon>0` such that

\[
 B(y)\cdot(y-p)\ge\kappa|y-p|^2\qquad(|y-p|<\epsilon).
\]

Then `c>=1/2+kappa`, for every finite `omega`. No decay, pressure normalization, or global-flow assumption is used. In the target range `0<c<1/2`, a local outgoing bound with `kappa>=0` is therefore impossible at a vortical stagnation point.

Moreover, even without that outgoing assumption, the matrix `DB(p)` has eigenvalue `1+c`. If `c<1/2`, it has at least one eigenvalue with negative real part.

## Proof

Let `S=(DU+DU^T)/2`. The local vorticity equation is

\[
 \Omega+B\cdot\nabla\Omega-DU\,\Omega+\omega J\Omega=0.
\]

At `p`, take its inner product with `Omega(p)`. Antisymmetry of `J` and of `DU-S` yields

\[
 \Omega(p)\cdot S(p)\Omega(p)=|\Omega(p)|^2.
\]

Thus the largest eigenvalue of the real symmetric matrix `S(p)` is at least one. Differentiating the outgoing inequality along each line through `p` gives

\[
 cI+S(p)=\operatorname{sym}DB(p)\ge\kappa I.
\]

Since `tr S(p)=0`, the two smaller eigenvalues are at least `kappa-c`, and therefore the largest is at most `2(c-kappa)`. It follows that `1<=2(c-kappa)`.

For the last statement, the vector vorticity equation at `p` reads

\[
 (DU(p)-\omega J)\Omega(p)=\Omega(p),
\]

hence `DB(p) Omega(p)=(1+c) Omega(p)`. The other two eigenvalues, counted with algebraic multiplicity, have sum `3c-(1+c)=2c-1`. If this real sum is negative, at least one has negative real part, whether the pair is real or complex conjugate.

## Scope

The local outgoing property is an additional H6 hypothesis. The statement does not prove that a general decaying profile has that property. It also does not assert `S Omega=Omega` in the rotating case: only the scalar equality used above is automatic. The negative-real-part conclusion controls a point-limit basin; it does not classify nonpoint backward limits.

This reconstructs and extends the scalar argument in Constantin, Ignatova and Vicol, Theorem 3.8. No numerical or formal verification is used.
