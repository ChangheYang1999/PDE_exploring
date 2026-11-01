# The size of an inverse-order correction to a period-three decrement

Status: exact countercalculation. The numerical statement that a decrement drift of about0.002 per period near n=365 is explained by a factor1-c/n with c about0.4 is false under either standard interpretation below. This does not rule out an inverse-order asymptotic with a different coefficient or additional terms.

## Per-period multiplier interpretation

Assume a positive magnitude multiplier is a_n=A(1-c/n), with A>0, c=2/5, and n>=360. Its base-ten logarithmic decrement is D_n=log10(a_n). Then exactly

    D_(n+3)-D_n = log10(1+3c/((n+3)(n-c))).

Since log(1+x)<=x for x>=0 and log(10)>2, this is bounded above by

    3c/[2(n+3)(n-c)] <= 3c/[2*363*(360-c)] < 0.000005.

This is over400 times smaller than0.002. The inequality log(10)>2 can be justified without decimal arithmetic: the exponential series gives e<3, hence e^2<9<10.

## Polynomial prefactor interpretation

Suppose instead that the coefficient norm has the form M_n=A^n n^(-c), with the same c=2/5, and define its three-order decrement by D_n=log10(M_n/M_(n-3)). Then

    D_(n+3)-D_n = c log10(n^2/(n^2-9))
                      <= 9c/[2(n^2-9)] < 0.000014

for n>=360. This is over142 times smaller than0.002. The conventional positive prefactor n^c would produce a negative drift instead. A per-order ratio A(1-c/n) has the same leading polynomial-prefactor scale, so it also does not justify the stated coefficient0.4 at these orders.

## Scope

These calculations audit the units and magnitude of the proposed interpretation. They do not fit the actual IPM sequence or prove its limiting behavior. A large fitted coefficient, another correction form, and a later change of regime remain possible. The finite conditional decrement data should be reported directly unless an asymptotic model is independently supported.
