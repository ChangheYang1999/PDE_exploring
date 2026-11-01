# A convergent branch led by sin(11 theta)

Status: PROVED, admitted in V484 after complete integer-response coverage, exact prefix checks, an exact majorant supersolution and an independent 1024-bit replay.

All numerical response bounds and majorant boxes below use the unit leading profile, epsilon=1. For general nonzero epsilon, sigma_k scales by epsilon^Q and its absolute lower bound by |epsilon|^Q; the stated exterior radius already includes the resulting amplitude scaling.

## Statement to be certified

Set delta=4/9, c=9/5, and f_1(theta)=sin(11 theta). At order n=9k, write H_(9k) for the coefficient of the free stream harmonic sin((4k-2)theta). Let sigma_k be its affine response in the coefficient of sin((4k+1)theta) in f_(9k+9).

If an explicit s>0 satisfies |sigma_k|>=s for every integer k>=1, then there is a unique compatible sequence of pure density and stream coefficients. Their series converge with every appropriately weighted derivative on each sufficiently large closed exterior. A common potential converges on the same strict exterior; it necessarily includes one finite nonzero correction lambda log r at order9, as proved in36 and specialized in228. The solution is nontrivial, its leading density changes sign within the first quadrant, and no whole-plane stationary extension is claimed.

## Proof of the conditional statement

The leading bandwidth is B=12. Before order 9, the density supports lie in the signed frequency set 11S_r+E_(r-1), where S_r consists of integers of the same parity as r with absolute value at most r, and E_j consists of integers of the same parity as j with absolute value at most j. The Poisson inverse shifts a density frequency by one, and the bilinear polar advection adds the resulting signed frequencies. Induction therefore proves this support inclusion, as detailed in topic 197.

The interval implementation uses this proven support set to replace excluded coefficients by exact zero, after checking that their computed enclosures contain zero. It does not infer an identity from a small interval.

At r=9, every element of 11S_9+E_8 has absolute value at least 11-8=3. The coefficient of sin(theta) vanishes. This is exactly the first compatibility condition, so the first stream kernel is admissible.

Assume the stated all-index lower bound. Topic 145 now applies with h=2, Q=9 and B=12. Its affine tuning identity sets H_(9k)=-R_k/sigma_k at every successive block. Its triangular scalar majorant gives geometric coefficient bounds. Its reconstruction theorem gives a common potential, including the necessary order-9 logarithm, with the same geometric base. Absolute convergence, the strict exterior ratio, and the polynomial derivative bounds justify the stationary equation term by term.

The leading density is nonzero, so the resulting solution is nontrivial. Its angular sign changes follow directly from sin(11 theta); sufficiently far out, the leading term controls the sign at any fixed angle away from its zeros. Scaling the leading profile by epsilon!=0 rescales each order-n coefficient by epsilon^n and the sufficient exterior radius by |epsilon|^(9/4).

## Proposed all-index certificate

The low fields F_1 through F_9 and G_1 through G_8 are computed independently in the Cartesian encoding. The compact response formula of topic 149 holds for any finite leading Fourier polynomial, including this single harmonic. Carrier separation holds whenever q=4k-2>=BQ=108, hence for k>=28.

Check every finite response k=1,...,27 by the full two-carrier calculation. For the remaining indices cover 0<=t<=1/110, where t=1/(4k-2), by the exact rational interval method of topic 149. A leaf is accepted only when a directed response enclosure has absolute lower bound greater than s. It may be discarded only when it contains no parameter of an integer k>=28. The finite checks and the complete replayed cover together would prove the hypothesis. A zero-containing finite response or a failed interval cover would leave the hypothesis open. A tentative target may be lowered during construction if a rigorously nonzero integer sample is smaller than expected; every prior accepted leaf must still pass against the final target. No leaf is omitted because it is inconvenient.

If successful, an explicit exterior radius must additionally be certified by the existing prefix majorant using the complete low-order density and harmonic bounds. No numerical growth fit will be used as a substitute.

## Evidence and dependencies

Topics 01 and 197 supply the Cartesian recurrence and support proof; topics 144 and 149 supply the affine and compact responses; topic 145 supplies the conditional convergence and common-potential theorem. Exact higher-order tuning is checked separately in topic 197. The initial probe here records finite values and the limiting response only; by itself it proves no all-index bound.

## Completed certificate, 2026-10-31T17:27:41+00:00

The all-index hypothesis is now established with s=2^-29. The finite part checks k=1 through27. The tail certificate partitions [0,1/110] into25 degree-two Taylor interval leaves and99 singleton leaves; there are no omitted or empty leaves. Exact rational endpoint and integer-range reconstruction proves that every k>=28 is covered. Every nonempty leaf was recomputed at1024 bits and again separated from [-s,s]. The proof of the Taylor enclosure is234 and that of singleton coverage is232.

The independently reconstructed rational prefix agrees in2029 coefficient positions with the interval prefix. Exact density norms bound all nine inputs. The N9 prefix majorant has a verified supersolution at w=2^-213, where w=z^9=r^-4. Consequently, for every real epsilon!=0, the tuned series with leading term epsilon sin(11 theta) converges with all appropriately weighted derivatives on

    r>=R>2^(213/4)|epsilon|^(9/4).

The summed common potential, including its required order9 logarithm, yields a stationary exterior solution. The sufficient exponent is not claimed optimal. The original direct interval attempt and its incomplete partition were retained; only the completed Taylor/singleton certificate is used. Files verification/checks.json and verification/review.json identify the complete cover and exact box by hashes.
