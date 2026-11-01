# A unique formal parameter curve through each tuned c = 3 profile

Status: PROVED formal parameter curve, after the independent11:52Z analytic review recorded in V306. No analytic convergence of the parameter series is asserted.

## Statement

Let delta0 = 2/3. Let b0 be either exact real root of the sextic obstruction in119, and let (f_n^*,g_n^*) be its unique tuned pure density and stream coefficients. Their existence and positive response infimum are proved in119. Put t = delta-delta0.

There is a unique formal power series

    b(t) = b0 + sum_(j >= 1) beta_j t^j

with real coefficients such that every coefficient of the nonresonant pure recursion, evaluated at delta = delta0+t and leading profile sin(theta)+b(t) sin(3 theta), belongs to R[[t]], and its value at t=0 equals the tuned coefficient. The recursion is first computed over the Laurent-series field R((t)); regularity means that each angular Fourier coefficient has no negative power of t.

The coefficients beta_j are determined successively. Let O_b be the derivative of the first density obstruction O6 with respect to b at b0, and let sigma_k be the tuned response from the free stream mode at n=3k to the next density obstruction. For k >= 2 define

    C_k = O_b (product_(ell=2)^(k-1) sigma_ell)
                    / (product_(r=2)^k (6r)).

Empty products equal1. Each C_k is nonzero. After beta_1,...,beta_(k-2) have been fixed, the constant value of the resonant stream coefficient H_(3k) is an affine function of beta_(k-1), with slope C_k. Matching H_(3k)^* determines beta_(k-1) uniquely.

At k=2 this gives beta_1 = 12(H6^*-H6_lim)/O_b, agreeing with152. The theorem neither provides an analytic curve in delta nor changes the exterior convergence radius proved at the single rational exponent.

## Local resonant division

At n=3k, write q=2k-2 and P_n=2-n delta. The resonant stream coefficient is

    [(P_n-q) a_(q-1) + (P_n+q) a_(q+1)]
                       / [2(q^2-P_n^2)].

Here P_n = -q-nt. The denominator has derivative -4nq at t=0. The coefficient multiplying a_(q-1) in the numerator has value -2q. Hence a change in the density obstruction a_(q-1) contributes

    a_(q-1)/(2nt)

to leading order at the resonance. All other factors in this local formula are regular after its numerator's constant term vanishes. A compatible numerator is therefore divisible by t, and inversion lowers the order of a perturbation by exactly one when its leading obstruction is nonzero.

Every nonresonant denominator at delta0 is a unit of R[[t]]. The apparent stream zero mode at n=3 is absent by symmetry. The first positive resonant denominator is at n=6; subsequent ones are at n=9,12,..., each simple in t.

## Perturbation propagation lemma

Suppose two leading shape series first differ by eta t^j, j >= 1. Assume the lower jets have already made the recursion regular through the resonances preceding n=3k, and that their constant coefficients agree with the tuned pair. For 2 <= k <= j+1, the leading difference of the resonant stream coefficients at order3k is

    C_k eta t^(j-k+1).

All earlier fields vary to at least this order, with one further power before each corresponding resonant division.

For k=2, the density obstruction at order6 differs by O_b eta t^j plus higher powers, because every earlier inverse is regular and its leading data differ by eta t^j. The local division formula gives (O_b/12) eta t^(j-1), establishing C_2.

Assume the assertion at k. Its leading perturbation is a change in the free resonant harmonic at order3k. Propagate it to the next density obstruction by the linearized finite recurrence. At t=0 this coefficient is exactly sigma_k times that change. Earlier direct perturbations carry at least one additional power of t, so they cannot contribute to this leading term. A product of two varying factors is also of higher order: when the perturbation order is positive this is immediate; for the final zero-order case the next step is not needed, since k <= j+1. Equivalently, the finite response is affine in the free harmonic through the next compatibility because two factors depending on it cannot meet before order6k+1 > 3k+3. The next local division multiplies the leading coefficient by1/(6(k+1)) and lowers its t order by one. This gives C_(k+1) = sigma_k C_k/(6(k+1)).

This argument uses only lower constant coefficients and the exact finite response. It does not require a uniform bound on the derivatives in t.

## Construction and uniqueness

First fix b(0)=b0. The order6 density obstruction vanishes, so the stream coefficient g_6 is regular for every choice of higher shape coefficients. Its constant harmonic is H6_lim+(O_b/12) beta_1. The first obstruction polynomial is squarefree at b0, hence O_b != 0. Choose beta_1 to match H6^*.

Proceed inductively. Suppose beta_1 through beta_(k-2) are fixed so that the constant coefficients through the preceding resonant stream order3k-3 agree with the tuned pair. All intervening nonresonant coefficients are regular. Their constants are generated by the same recurrence as the tuned pair, so the density obstruction at order3k vanishes. The next resonant inverse is therefore regular. Its constant harmonic depends only on beta_1,...,beta_(k-1). The propagation lemma shows that its dependence on the last coefficient is affine with nonzero slope C_k. Choose that coefficient to match H_(3k)^*.

Higher shape coefficients cannot change any constant already fixed: the lemma gives a positive power of t at each earlier resonance. This determines all beta_j consistently. For any fixed spatial order n, only finitely many resonant divisions occur below it. A sufficiently long shape jet makes every coefficient at that order regular and gives its tuned constant. Passing to the compatible inverse limit of the finite jets constructs b(t) in R[[t]]. Each rational recurrence coefficient depends continuously on a sufficiently long jet after its finite possible losses, so the infinite formal series has the asserted regularity.

Conversely, suppose a formal shape makes every coefficient regular. At t=0 its constant density and stream coefficients form a compatible pure formal solution with leading shape b0. The uniqueness theorem119 forces the tuned pair. At every induction step the nonzero slope C_k then forces beta_(k-1) to equal the constructed value. Thus the parameter series is unique.

## Scope and unresolved analytic question

The construction proves compatibility of every finite parameter jet. It does not bound beta_j as j grows. A divergent b(t) is consistent with all conclusions here. Even convergence of b(t) would require a separate estimate for the spatial series uniformly in a parameter neighborhood, where nearby rational exponents have their own resonances. No open interval of convergent exact exponents is claimed.

Dependencies:119 for tuned existence, uniqueness and nonzero sigma_k;151 for the first removable limit;152 for the first slope. The local division and induction are written out here for independent review. No numerical finite approach is used as proof of the formal all-order assertion.

## Independent second-jet check

A separate Cartesian Taylor algebra computes the recursion for b(t)=b0+beta1*t+beta2*t^2. At a resonance it verifies that the numerator's constant interval contains zero, removes that coefficient using the proved compatibility, and divides the remaining series by the nonzero linear factor. The two tests beta2=0 and beta2=1 reproduce the slope C3=sigma2*O_b/(12*18).

At the smaller and larger roots, respectively, the resulting beta2 values are approximately308.68293237503641942475 and-445.70126957033191843148. These are Taylor coefficients; the second derivative is twice beta2. With these coefficients all288 constant density/stream comparisons through density12 and stream11 match the independently tuned prefix. The next density obstruction vanishes as a certified interval. Leaving beta2=0 gives nonzero simple-pole residues at order12 of approximately4.1956895658684284815e-14 and-5.4017022068907497480e-9. This illustrates the need for successive shape derivatives without proving convergence of their formal series.

The certificate is verification/second_jet_checks.json. The all-order proof was independently confirmed in V306; this finite calculation is V301.
