# What a table sensitivity screen can establish

Status: exact algebraic results about a proposed numerical screen. They neither establish a pressure error nor invalidate a measured Euler residual.

## Statement and hypotheses

Let N and M be positive integers, let O be an open subset of R^N, and let F:O -> R^M be continuously differentiable. A table is represented by t in O. For a perturbation v with the segment from t to t+v contained in O,

    F(t+v)-F(t) = integral_0^1 DF(t+s v) v ds.

Consequently, a screen that replaces the final output by F(t)+w tests that chosen output perturbation w. It does not in general test perturbing the input table by v, even if both w and v use the same relative scale.

More specifically, fix u>0 and epsilon>0, set t=1+epsilon, and take F(t)=t-1 on R. Perturbing the input relatively by u changes the output by u(1+epsilon). Perturbing the final output relatively by u changes it by u epsilon. The ratio is (1+epsilon)/epsilon and has no finite upper bound independent of epsilon.

Second, let k<N and fix k tested directions v_1,...,v_k in R^N. There is a nonzero linear functional A:R^N -> R such that A(v_i)=0 for every i, yet A(v)>0 for some other v. Thus zero responses in finitely many directions do not give a uniform bound on every possible perturbation, without further assumptions on the derivative or tested directions.

Third, let H:O -> R^M and W:O -> R^(M by M) be continuously differentiable and define R(t)=W(t)H(t). Its derivative is

    DR(t)[v] = DW(t)[v] H(t) + W(t) DH(t)[v].

A screen that freezes W at its base value tests a different perturbation response unless DW(t)[v] H(t)=0 or a separate bound controls that term. Equality of the base residual values alone does not establish equality of their perturbation responses.

## Proof

For each component of F apply the one-dimensional fundamental theorem of calculus to s -> F(t+s v). Its derivative is DF(t+s v)v by the chain rule. This proves the first identity. In the scalar example,

    F((1+u)t)-F(t) = (1+u)t-t = u(1+epsilon),
    (1+u)F(t)-F(t) = u(t-1) = u epsilon.

The ratio is 1+1/epsilon, which tends to infinity as epsilon tends to zero through positive values. These calculations are exact and do not assume a floating-point error model.

For the second statement, the span of the k tested vectors has dimension at most k<N. Choose a nonzero a orthogonal to that span and define A(v)=a dot v. Then A(v_i)=0 and A(a)=||a||^2>0. This is an existence counterexample to a deterministic inference from those responses. It does not state the probability that a fixed numerical map escapes a random screen.

Finally, differentiate the finite sums R_i=sum_j W_ij H_j and apply the scalar product rule to each term. This gives the displayed formula. Freezing W deletes its first term, proving the stated condition for first-order agreement.

## Dependencies, interpretation and scope

Dependencies are the finite-dimensional chain rule, fundamental theorem of calculus and elementary linear algebra. No imported numerical table is used in this proof. No formalization or interval certificate is claimed.

For the current campaign, perturbing a returned gauge residual cannot stand in for perturbing the parameter-dependent leading-tail amplitudes before subtracting the normalization constant. Perturbing returned closure rows likewise differs from perturbing their carried patterns, target and target norm. These classes may be examined separately, but their names and coverage must remain exact. A table screen against the complete residual must also recompute its parameter-dependent weights if those weights depend on the perturbed quantities.

A four-draw screen is empirical evidence for the tested table, directions, arithmetic and point. It is not a worst-case rounding bound. A class which was never called, a missing group, or a perturbation which rounded to zero requires an explicit scope decision; none should be silently converted into a successful active-class test.

## Directional spacing at a binary64 binade boundary

Assume binary64 arithmetic with rounding to nearest and ties to even. At t=1, the next larger representable number is 1+2^-52 and the next smaller one is 1-2^-53. The exact real midpoint 1+2^-53 rounds to 1, since 1 has the even low significand bit. Thus an exact value which rounds to 1 can have rounding error 2^-53. A move from 1 to its smaller neighbor has exactly that size, not twice that size. This refutes the uniform statement that a randomly signed one-neighbor move is always at least twice the largest rounding error of an entry. Away from the change in spacing the usual half-spacing bound gives the factor two. The one-neighbor screen can still be used as an explicitly registered empirical test; this example concerns its stated rationale.
