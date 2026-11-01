# A certified enclosure of a two-sided real-line polynomial norm

Status: PROVED enclosure lemma, independently confirmed by the theory part at 2026-10-31T07:00Z; finite interval audit V155. A sampled maximizing point is not asserted to be the location of the global maximum.

## Statement

Let H(t,theta)=sum_(q=0)^K t^q H_q(theta) be a finite real trigonometric polynomial, and let ||.|| be the angular Fourier Wiener norm. Fix eta>0 and define

    N_eta(H)=sup_(t in R) exp(-eta|t|)||H(t)||,
    u_q=||H_q||, U(x)=sum_(q=0)^K u_q x^q.

Choose any partition 0=x_0<x_1<...<x_J=K/eta, and any finite sample set S of real points. If K=0, take N_eta(H)=u_0. If K>0, then

    max_(t in S) exp(-eta|t|)||H(t)|| <= N_eta(H)
      <= max_(1<=j<=J) exp(-eta x_(j-1)) U(x_j).     (1)

Thus interval lower bounds at sample points, together with interval upper bounds for the finite right side, give an enclosure of the global supremum on the entire real line. No root search and no sampling assumption about the location of the maximum are required.

## Proof

The lower bound follows from the definition of a supremum. The triangle inequality gives ||H(t)||<=U(|t|). On a partition interval [x_(j-1),x_j], the nonnegative-coefficient polynomial U is nondecreasing and exp(-eta x) is nonincreasing. Their product is at most exp(-eta x_(j-1))U(x_j).

For x>=K/eta, every monomial exp(-eta x)x^q, 0<=q<=K, is nonincreasing, because its derivative has sign q-eta x<=0. Therefore exp(-eta x)U(x) is nonincreasing on that tail. Its value at K/eta is bounded by the last partition bound. This proves(1) for all x>=0 and hence for all real t. For K=0 the statement is immediate.

With step size at most h, the upper bound differs from the supremum of exp(-eta x)U(x) by at most the multiplicative factor exp(eta h), since each interval estimate equals exp(eta(x_j-x_(j-1))) times the value at x_j. The gap between this positive-coefficient envelope and the actual H can be much larger because of cancellation.

## Application and scope

The audit uses the frozen canonical sin(theta), delta2/3 coefficient balls through order290. For each retained order and eta=1/3, it independently evaluates the positive and negative sampled maxima selected by the theory part's quarter-step grid on[-640,640]. Those points supply lower bounds only. It separately constructs the global upper bound in(1) with partition step at most1/4. Every stored midpoint and radius is decoded exactly before outward-rounded arithmetic.

The theory part's source evaluator explicitly describes a grid estimate. The report phrase that the global supremum is attained near a particular negative point is stronger than this method establishes. Also, the source stores the upper endpoint of each evaluation as a floating logarithm; that number is not itself a certified lower bound on the true global supremum. The present interval evaluations restore a rigorous lower bound, while(1) supplies a rigorous global upper bound.

No exact global maximizing point, asymptotic norm growth, or convergence conclusion follows from this finite calculation. The lemma is independent of the IPM recurrence and applies to any finite trigonometric polynomial with polynomial log coefficients.

## Finite enclosure result

The completed audit at2026-10-31T06:47:51Z checks both fields at150,180,200,210,240,260,270,290. Its sixteen enclosures are retained in verification/20261031T064751Z/checks.json, with the frozen grid input and executable source. At290 the density log10 supremum belongs to[-171.454138171955,-170.661702963069] and the stream log10 supremum to[-174.496487643806,-173.700189332168]. These displayed endpoints are rounded outwards. The exact interval outputs give narrower bounds. The actual audit runtime is9.9454779997468 seconds.
