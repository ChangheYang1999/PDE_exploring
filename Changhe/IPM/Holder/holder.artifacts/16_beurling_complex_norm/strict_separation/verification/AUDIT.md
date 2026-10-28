# Independent audit, 2026-10-28T07:44Z

The analytic endpoint arguments were rechecked: a2<=1/pi follows from
positive-integral log-convexity and its two endpoint values; a3<=1/4
for a>=3/4 follows from the fourth-power inequality81sqrt3<2pi^4.
Qn<=n^a follows from min(1,v)<=v^a. The small and large endpoint margins
are strictly positive under the elementary bounds pi>3 and sqrt3<2.

For the central interval the first checker uses the difference of two
positive binomial series. The independent checker instead combines their
integrands first, obtaining the positive rational series

    a3(a)=(3/pi) sum_(k>=0) c_k 4^(-k-1)
                 *2(a+5+2k)/[(a+2+2k)(a+4+2k)],
    c_k=binom(2k,k)/4^k.

It is the expansion of(3s-4s^3)(2s)^a/sqrt(1-s^2) after integration
on[0,1/2]. Since c_k<=1 and the integrated bracket is at most
3/(a+2+2k), the tail afterNterms is at most

    3*4^(-N)/[pi(a+2+2N)].

The second checker uses100terms at256bits, while the first uses80terms
at192bits. It also evaluates the real upper bound as
(2a2)^(1-a)[2a3+(1-a)b]^a/[a(1-a)], an independent rearrangement of the
optimized-radius expression. Both methods prove all42 selected gaps
positive. The independently recomputed minimum scaled central margin
exceeds0.003639. Exact rational endpoints are checked for once-only
coverage, source hashes agree, and no sampled point replaces a full
interval. The universal strict-separation theorem is CONFIRMED.
