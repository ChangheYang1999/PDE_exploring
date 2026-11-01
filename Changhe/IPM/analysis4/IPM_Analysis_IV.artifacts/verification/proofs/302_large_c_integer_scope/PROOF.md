# The large-c uniform-radius family requires an integer index

Status: the extension to real indices is REFUTED. The proved integer-index corollary is unchanged.

## Exact statement and notation

The claim that the pure far-field series for `f_1(theta)=sin(theta)` converges on `r>=128` for every `c=2N+sqrt(5)` with real `N>=16` is false. Its valid established version assumes `N` is an integer, as in topic76 and Section7.5 of the mathematical report.

## Complete counterexample

Set

\[
N=(37-\sqrt5)/2,\qquad c=37,\qquad \delta=1-1/c=36/37.
\]

Since `sqrt(5)<5`, one has `N>16`. The number `N` is irrational, since otherwise `sqrt(5)=37-2N` would be rational. Thus this parameter belongs to the claimed real-index family but not the proved integer-index family.

The denominator37 is prime: no prime at most its square root, namely2,3 or5, divides it. The numerator36 is even and satisfies `4<=36<37`. Topic31 therefore applies with `p=37` and `a=36`. The first stream resonance is at order37, in stream mode34. If `kappa` denotes the coefficient of density mode33 in `f_37`, the theorem gives

\[
\kappa\equiv(-1)^{(36-4)/2}=1\pmod {37}.
\]

In particular `kappa` is nonzero. The pure Poisson equation at this order is incompatible, so the pure series does not exist to all orders and cannot converge to an exact solution on `r>=128` or on any other exterior. This proves the counterexample.

## Source discrepancy and repair

The frozen report of22:18:28 states the real-index-looking claim in Section0 item1, line525. The corresponding frozen theory has the same text at line497. Their full Section7.5 corollary correctly says every integer `N>=16`; the summary table also includes `N in Z`. Insert `N in Z` into Section0 item1 and rebuild the report. No change to the proof or radius is needed.

## Dependencies and scope

The first-resonance obstruction is the already admitted all-prime theorem of topic31, with exact recurrence and compatibility from topic01. This is a document-scope counterexample, not a new arithmetic recomputation of order37. It makes no assertion about the logarithmic series at `delta=36/37`.
