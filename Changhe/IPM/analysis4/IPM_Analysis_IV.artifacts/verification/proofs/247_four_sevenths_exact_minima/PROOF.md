# Exact locations of the three delta4/7 response minima

Status: PROVED. Directed construction, independent precision replay and comparison with a separate rational-function proof are complete.

## Statement

Let b_1<b_2<b_3 be the three real roots of the degree-seven first-compatibility polynomial in239, and let sigma_k(b) be the response associated with the leading profile sin(theta)+b sin(3theta) at delta4/7. The proposed assertion is that the infimum of |sigma_k(b_i)| over positive integer k is attained uniquely at k=4,8,6 for i=1,2,3 respectively.

The roots and all-index nonvanishing are already established in239. This new claim concerns the exact minimizing index, not a new convergence theorem.

## Certificate argument

For each root choose a rational isolating interval containing exactly that root. Directed full-recurrence evaluation at the candidate minimizing index m gives an interval for |sigma_m| with a rational upper endpoint U. For every other k below a threshold K, independently evaluate the full response and require |sigma_k|>U. The thresholds are16,24,16 respectively, all beyond the compact-formula threshold8.

For k>=K the compact identity gives sigma_k=S(1/(4k-2)). Cover [0,1/(4K-2)] by a finite partition with rational endpoints. Each interval has one of three justified statuses: it contains no sample with k>=K; it contains a single such sample whose directed response has modulus greater than U; or its full Taylor enclosure has modulus greater than U. The reciprocal formulas in232 determine the exact sample range. A complete partition proves |sigma_k|>U>=|sigma_m| for every remaining k. Thus the minimum is uniquely at m.

The limit at t=0 is included in the cover, although no finite index maps to zero. Threshold U is fixed throughout and cannot be reduced during this certificate. Reducing it would establish a lower bound but would not prove the minimizing index. A separate higher-precision replay checks the partition, finite comparisons and every accepted response bound.

## Scope

The minimizing value is the exact algebraic number |sigma_m(b_i)|. Printed decimal values are enclosures or approximations to that number. This assertion neither locates the convergence radius nor upgrades any finite numerical tail experiment.

Dependencies: the exact root isolation and compact/full identities239; directed Taylor inclusion234; rational integer coverage232; elementary comparison of real numbers.

## Verification

At 1024 bits, all finite comparisons and every fixed-threshold Taylor interval pass. A fresh 1536-bit replay independently recomputes the finite values, interval bounds and partition. The respective tails use two, one and four Taylor intervals; none requires a singleton exception. The minimizing values are approximately 3.4763891709725342510e-7, 2.1886260118350592726e-6 and 47.281200359817079940. Exact enclosures are in the retained compressed certificates. A separate polar rational-function proof from the theory part gives the same unique minimizing indices. V513 admits this conclusion.

## Consequence for a sharper prefix bound

The positive rational numbers s_1=347/1000000000, s_2=109/50000000 and s_3=1182/25 lie below the three certified minima. Replace only the response lower bound in the already certified order-seven prefix majorants of239 by the appropriate s_i. The initial density bounds remain valid. With h=2, Q=7, B=4, L=147/80 and kappa=48/7, an exact nonnegative box Y satisfying Y>=Y0 and Phi(2^(-q),Y)<=Y proves the majorant converges for |w|<2^(-q). Since w=z^7=r^(-4), the sufficient exterior radius is R>2^(q/4)|epsilon|^(7/4). A failed heuristic box search asserts nothing about an optimal radius. New q values require their own exact replay before admission.

The exact boxes now pass at q=108,117,109 for roots1,2,3. Fresh replay confirms all box inequalities and42 scalar coefficient identities per root. Thus the sufficient exponents are27,117/4,109/4, each with amplitude power7/4. V514 admits these improved bounds; no optimality is asserted.
