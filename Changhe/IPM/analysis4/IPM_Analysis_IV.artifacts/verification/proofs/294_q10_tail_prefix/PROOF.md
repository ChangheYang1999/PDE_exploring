# A period-ten prefix with a bound only on the remaining responses

Status: PROVED in V597, admitted 2026-10-31T21:56:52+00:00, within the exact scope below.

## Statement

Let delta=1/5, c_l=5/4 and p_n=1-n/5. Let b be the fifth increasing real root of the degree20 compatibility polynomial of281, and set f_1=sin(theta)+b sin(3theta). Use the density and stream recurrence01, with each positive-frequency stream resonance at n=10k resolved by the unique free harmonic H_(10k) enforcing the next compatibility condition. Existence and uniqueness of this tuned sequence follow from281,282 and285.

For an integer M>=10, put N=10M. Suppose a directed Cartesian prefix through f_N and the particular part of g_N agrees with the independently expressed polar recurrence, including its two provisional continuations at each earlier resonance. This prefix excludes H_N, the first harmonic to be fixed in the tail. Choose rational bounds d_n>n||f_n||_1 for1<=n<=N and e_k>10k|H_(10k)| for2<=k<M, with e_1=0.

Suppose a positive rational s bounds |sigma_k(b)| from below for every integer k>=M. Set L=75/29 and kappa_N=(208/5)(N+1)/N. Form the residue map G from175 using this prefix and s. If a nonnegative rational vector v satisfies v>=Y0 and G(2^-q,v)<=v, then the tuned series and all its fixed weighted spatial derivatives converge absolutely and uniformly on each closed exterior r>=R>2^(q/2). For nonzero amplitude epsilon the sufficient threshold is multiplied by |epsilon|^5. The common potential includes its mandatory finite order10 logarithm. No sharp-radius or whole-plane extension claim is made.

## Proof

Only responses at k>=M are inverted when extending this fixed prefix. The harmonic H_N introduced at N=10M is fixed by the compatibility equation at order N+10=10(M+1). Writing that equation R_N+sigma_M H_N=0, its solution is unique and bounded by |R_N|/s. Repetition constructs all later coefficients. The earlier responses are already accounted for in the certified finite prefix; their smaller values need not enter this tail bound.

The ordinary Poisson estimate is L=3Q^2/[4(3Q-1)]=75/29 at Q=10. The advection estimate of175 is kappa_N=B[2-delta+max(delta,1-delta)](1-delta)/delta*(N+1)/N. With B=4 and delta=1/5 this is (208/5)(N+1)/N. The scalar induction of175 therefore dominates all newly constructed density and harmonic coefficients. Its nonnegative residue map has a strictly triangular affine part at zero. The finite inverse of this affine part gives G. Iteration from zero is monotone and bounded by v at w=2^-q. Hence all residue generating functions converge there. Finite Fourier bandwidth absorbs every fixed derivative on a strict exterior, and reconstruction132 gives the common potential with at most its two permitted finite logarithms. Absolute convergence justifies every differentiation and product in the stationary equation. Degree-n amplitude homogeneity gives the factor |epsilon|^5. This is the comparison argument of262 specialized to Q=10.

## Certifying the remaining response bound

For M<=k<21, evaluate the exact response polynomials of282 on the entire rational isolating interval I for b, and check |sigma_k|>s by a fixed-sign enclosure. For k>=21, use the normalized exact rational response sigma_k=N(k,b)/D(k) of282. Choose the limiting sign e. If every coefficient of D(21+x) is positive and every coefficient polynomial of eN(21+x,b)-sD(21+x) is positive throughout I, then |sigma_k|>s for all real k>=21, and therefore all the remaining integers. Separate exact rational interval arithmetic replays every coefficient and finite response inequality. Sampling proposes s only and proves no infinite claim.

## Verification and dependencies

Retain the independent polar prefix, exact low-order comparisons, every rational upper bound and all sources. Reassemble the residue map from the saved bounds, compare with the directly indexed scalar sums for two periods and verify every box inequality using exact fractions. The optional floating box search only proposes a box; an already verified exact baseline is retained if that search fails. Dependencies are01,131,132,175,226,262,281,282,285. Inputs are read only. Any failed check leaves the proposed improvement OPEN, while all earlier admitted radii remain valid.

## Completed verification

At the fifth period-ten root, the remaining-response lower bounds are s=1/2097152 for k>=10, s=1/1048576 for k>=12. Each tail certificate has110 strictly positive shifted numerator coefficients and110 strictly positive denominator coefficients; the two finite ranges contribute20 inequalities. The exact boxes give q=175 at N100 and q=174 at N120. The best sufficient exterior is R>2^(87)|epsilon|^5, compared with2^(177/2) from the full-range bound. All800 exact low-prefix comparisons,240 independently recomputed norms,11 harmonic/response comparisons and120 independently indexed scalar identities pass. Actual runtimes: Cartesian prefix273.068419s, polar replay354.054256s, bound construction7.162106s, exact replay2.889317s.

The stated sufficient bounds are PROVED. No optimal radius, coefficient-growth law or whole-plane extension follows.
