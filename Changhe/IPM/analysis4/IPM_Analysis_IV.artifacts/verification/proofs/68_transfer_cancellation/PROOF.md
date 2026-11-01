# Cancellation of a resonant transfer at rational parameters

Status: CONFIRMED after independent theory-part review dated2026-10-31T05:25Z and verifier recheck. The finite checks described below are recorded separately. No full rational logarithmic convergence theorem is claimed.

## 1. Definitions and dependencies

Use the canonical polynomial-logarithmic recurrence of topic67. Let Q>=3 be an integer, delta=2/Q, c=Q/(Q-2), and let f_1 be a nonzero finite real S1 sine polynomial. Write t=log r. The stream integration constant at every resonance is zero. Set m_k=2k-2. For k sufficiently large, insert an external stream coefficient sin(m_k theta) at order Qk, and propagate the part linear in that coefficient through Q further orders using only the fixed low-order coefficients F_j,G_j, 1<=j<=Q. All those low-order coefficients are constant in t.

Let H_Q be the resulting density at order Q(k+1). Its sine coefficient K(k) at frequency m_k+1 drives the next resonant stream coefficient. Define R(k)=-K(k)/(2k). In a log column of degree k-1-d the corresponding transfer is kR(k)/(k-d). Let Lambda=lim_{k to infinity} kR(k), as established by the finite rational offset map in topic67.

For each fixed d>=0, the deficit-d columns mean

    [t^(k-1-d)] F_(Qk+r), 1<=r<=Q,
    [t^(k-1-d)] G_(Qk+r), 0<=r<Q,

at k>=d+1. The same degree is used throughout a block. Topic67 proves the triangular structure: the only current-deficit scalar propagated between blocks is the resonant coefficient at G_(Qk); every inhomogeneous term uses strictly lower deficits. Its convergence assertion was independently reviewed and confirmed; the frequency argument here does not require its quantitative growth estimate.

## 2. Two-mode limiting cancellation at delta=2/3

For f_1=alpha sin(theta)+beta sin(3theta),

    Lambda = (314 alpha^3 -2925 alpha^2 beta
              +6735 alpha beta^2 +75 beta^3)/259200.       (1)

Each low-order density F_j is homogeneous of degree j in the leading coefficients, as is G_j. A linearized cycle with Q leading leaves is homogeneous of degree Q. Consequently Lambda for Q=3 is a homogeneous cubic. The exact low-order polar recurrence, followed by the limiting offset operations of topic67, gives at alpha=1 the numerator 314-2925 beta+6735 beta^2+75 beta^3. This is a finite identity of rational polynomials, not a fit to approximate values. The source in verification gives an independent formal-polynomial calculation; exact Cartesian low-order calculations provide additional evaluations of the identity.

Let P(b)=75b^3+6735b^2-2925b+314. Its signs alternate at the endpoints of the three pairwise disjoint rational intervals

    (-90233/1000,-90232/1000),
    (19598/100000,19599/100000),
    (23674/100000,23675/100000).                           (2)

The intermediate value theorem gives a real root in each interval. A cubic has at most three distinct roots, so these are exactly its three roots and all are simple. In particular there are two positive algebraic ratios beta/alpha for which Lambda vanishes.

By the confirmed fixed-deficit theorem in topic67, at either positive ratio every fixed-deficit factorial column has zero exponential rate in k. This is a statement about one deficit at a time. Constants and onset orders need not be uniform in d, so (1) gives no convergence conclusion for the full sum over log degrees.

## 3. An exact frequency-gap cancellation

Suppose now that Q is odd and that there is an odd integer M>Q such that every nonzero leading frequency is an odd multiple of M. Let L be the largest leading frequency. Then

    R(k)=0 whenever 4k>Q(L+1)+2.                         (3)

This is exact vanishing of the rational transfer, not only Lambda=0.

To prove it, use signed complex Fourier support. Angular differentiation leaves a frequency unchanged, and a product adds frequencies. A Poisson inversion maps a density frequency ell into stream frequencies ell-1 and ell+1; logarithmic differentiation and integration preserve the angular frequency. This support inclusion remains valid at resonance. Cancellations can remove frequencies but cannot add one outside this inclusion.

A density F_j is a sum of binary recursion trees with j leading density leaves and j-1 Poisson inversions. A stream G_j has one additional inversion. A linearized density tree with one external stream leaf and Q leading density leaves has Q nonlinear vertices. Exactly one of the Q left-stream occurrences is the supplied external stream leaf, so precisely Q-1 new Poisson inversions occur. This count can alternatively be proved by induction in the recurrence defining H_r and J_r.

Therefore any signed angular frequency in H_Q has the form

    epsilon m_k + sum_(a=1)^Q epsilon_a ell_a
                  + sum_(b=1)^(Q-1) eta_b,             (4)

where every sign is +1 or -1 and every ell_a is a leading frequency. We ask whether (4) can equal the positive target m_k+1.

If epsilon=+1, the middle sum is M times an odd integer: Q is odd and every ell_a/M is odd, independently of the signs. Its absolute value is at least M. The last sum has absolute value at most Q-1. Hence their sum has absolute value at least M-(Q-1)>1 and cannot equal1.

If epsilon=-1, their sum would have to equal2m_k+1=4k-3. Its absolute value is at most QL+Q-1. The inequality in (3) gives 4k-3>QL+Q-1, so this case is impossible as well. Thus the target coefficient K(k) is zero, proving (3). All factors in the cycle are defined once k>=2; the intermediate orders are nonresonant and the final canonical integration is always defined.

## 4. Consequence for fixed-deficit columns

Under the hypotheses of Section3, every fixed-deficit column is identically zero at all sufficiently large block indices k. Its extracted series is therefore a polynomial.

Here is the induction, with the quantifiers made explicit. At deficit0 there are no strictly lower deficits. Apart from finitely many initial blocks, the entire deficit0 block is the linear propagation of its resonant scalar. By (3), that scalar is zero after a fixed finite block. Hence all deficit0 block columns have finite support in k.

Suppose that all columns at deficits0,...,d-1 have finite support in k. There are finitely many such deficits and finitely many positions in a block. Their union of supports is therefore finite. A known linear term at deficit d uses one of these columns and a low-order coefficient; a known quadratic term uses two lower-deficit columns whose orders add to the output order. Such terms vanish once the output order exceeds the largest possible sum of their finite supports. Logarithmic derivatives couple only to smaller deficits, and the relevant triangular inverses use only finitely many such columns at a fixed d. Consequently the inhomogeneous forcing in the deficit-d scalar recurrence vanishes for all sufficiently large k. Equation (3) then makes the scalar zero one block later, and all remaining columns in that block vanish as well. This proves the induction.

This consequence uses the exact triangular decomposition in topic67, not an inference from finite computed coefficients. It does not assert a cutoff uniform in d and does not prove that the full logarithmic series converges.

## 5. Verification and scope

The completed exact check computes (1) in a formal rational polynomial ring using the polar sine recurrence, independently of the Cartesian code. Additional evaluations compare the separate Cartesian low-order engine. The signs in (2) are checked as rational numbers. Finite cycles check (3) for pure and mixed high-harmonic profiles, including finite-order reflection exceptions below the threshold.

These results identify special leading profiles for the rational logarithmic problem and distinguish a vanishing limiting transfer from an eventually zero transfer. A profile with Lambda=0 need not satisfy (3). Neither property controls all deficits simultaneously. The full exterior convergence problem at these rational parameters remains OPEN.

The formal cubic identity, nine independent Cartesian evaluations, three exact root brackets, and60 exact cycles across seven profiles at Q3,5,7 all pass. Of these cycles,28 lie at or beyond the proved vanishing threshold and are exactly zero. Actual computation time1.853058760985732 seconds. See verification/checks.json and the retained source snapshots.

## Verification closure, 2026-10-31T05:29:25Z

The independent theory-part review is retained in sources/lead_review_20261031T0525Z.md. Its index and sign checks agree with the argument above and the independent exact computations. The stated theorem is CONFIRMED. No convergence of the complete rational logarithmic series is inferred.
