# Response bounds restricted to the unknown tail

Status: PROVED comparison theorem. The independent theory-part review is retained in sources/lead_review_20261031T1642Z.md. The first and fourth root certificates at K=30 are admitted in V470; further roots require their own completed checks.

## Statement

Fix one of the four exact delta=3/5 profiles from200. Let N=10K be a positive multiple of10 with K>=7. Suppose its density coefficients throughN and tuned stream harmonics throughN-10 have the certified bounds used in220. Let s_K>0 satisfy

    |sigma_k|>s_K for every integer k>=K.

Then the finite-prefix majorant of172 and220 remains valid with s replaced by s_K. In particular, every exact box certificate at w=2^(-q) gives the same smooth exterior solution theorem on r>=R>2^(q/6), with amplitude scaling |epsilon|^(5/3). No bound on sigma_k for k<K enters this comparison once the stated finite coefficients have been certified.

## Proof of the comparison change

The finite-prefix majorant treats f_1 through f_N and H_10 through H_(N-10) as known polynomials. Its first unknown harmonic is H_N. For a harmonic at n=10k with k>=K, the affine block identity reads

    H_(10k)=-R_k/sigma_k.

The proof of172 bounds the absolute numerator R_k using the known prefix, previously bounded unknown coefficients and nonnegative quadratic convolution terms. Its only use of the response lower bound is the division by |sigma_k| at this step. The present hypothesis gives the required bound 1/|sigma_k|<1/s_K at every such unknown harmonic. Lower harmonics have already entered through their certified e_a and require no further division. All remaining comparisons and the nonnegative polynomial map are unchanged. Induction over successive blocks therefore proves the majorant with s_K. The exact box, monotone convergence, potential reconstruction and derivative conclusions follow from172,202 and220.

This argument does not remove the need to prove the prefix. Every earlier compatibility equation, harmonic choice and enclosure remains a hypothesis verified by208 and209.

## Certificate for the tail response

Use the compact response from204. For k>=K>=7 set t=1/(6k-2). Its exact response is a continuous rational expression of t and the fixed algebraic root, evaluated by directed arithmetic wherever its intermediate denominators do not contain zero. The complete integer tail lies in

    0<=t<=1/(6K-2).

A candidate s_K is chosen from finite samples and the limiting response, but only the complete interval cover proves it. Bisect this interval rationally. Accept a leaf when its directed response enclosure has |midpoint|-radius>s_K. Discard a leaf only when the exact integer interval

    max(K,ceil((1/b+2)/6))<=k<=floor((1/a+2)/6)

is empty, with no upper bound at a=0. Retain the binary addresses and exact enclosures. Reconstruct each leaf and check every accepted inequality and integer exclusion independently; check that the leaves partition the initial interval. The accepted leaves cover every required integer, proving the tail bound. A failed cover proves no bound and is not used.

## Numerical certificate and scope

The first intended specialization is K=30, N=300. The stored coefficient norm bounds come from220 and are checked against its input hash. New boxes are recomputed with s_30; no empirical growth estimate is used. A separate rational replay reconstructs the polynomial map and its exact box image. These are sufficient exterior radii, not optimal radii and not whole-plane extension results.

## Alternative validated leaf enclosures

For roots2 and3 the replacement cover may use the complete integer partition of232. A nonempty leaf with a single admissible integer k is certified by evaluating the compact response at exactly1/(6k-2); an interval leaf uses the degree-two Taylor enclosure of234. The exact partition and integer-range argument above are unchanged. In the stored schema both leaf kinds have status `accepted`, with method `singleton` or `taylor` identifying the evaluation rule. Every singleton also records k and its equal lower and upper integer bounds. The independent higher-precision replay applies the recorded rule and proves the lower bound anew.

The first root2 natural-interval search hit its30000-node limit at s=2^-40. Its next attempt was stopped on2026-10-31T17:21:36Z. The old source and log are preserved. A search limit or a stopped attempt establishes no response bound. The replacement retains the same exact response and finite-prefix inputs.
