Prepared 2026-10-22T09:13:41.369383+00:00 before controls.

# Audit of the complete 4.56 entry

This audit concerns literal text_v3 and its seven surrounding replacements on FINAL_REPORT SHA256 1b4403d4. Dependencies are P321 (all-order formal hierarchy), P326 (common disk), and the actual notation and finite statement 4.55 checked in P319/P323. It does not establish a B2 endpoint.

## Exact statement under review
For beta=2, u=y_*-y, real Ck nonzero, B=u+k u^2-(Ck/260)u^13 and H=-k^7/231, fix t'/t=(8+2B')/B, Y'/Y=(5+B')/B with normalized leading coefficients 1, and G'=t/(BY), G(0)=0. Put a_1=Ct/2, q_0=Y(H-CG), v_0=B and v_2=-(q_0+B'')/2. The claim is uniqueness of a compatible sequence of smooth coefficient germs satisfying every thermal, vorticity and curl relation, with every coefficient analytic on |u|<R_*, where R_*=min(1,1/(4|k|),(65/|Ck|)^(1/12)). The statement concerns a formal x series, not an actual two-dimensional solution.

## Argument and mapping to the report
With derivatives in u, W_1=(4+B')x+sum v_{2j}' x^(2j+1)/(2j+1) and W_2=B+sum v_{2j}x^(2j). Hence div W=4 and Omega=d_y W_1-d_x W_2 gives q_j=-v_{2j}''/(2j+1)-(2j+2)v_{2j+2}. Direct coefficient extraction gives

B a_l'-(8l+2l B')a_l = sum_(j=1..l-1) [2(l-j)v_{2j}'a_(l-j)/(2j+1)-v_{2j}a_(l-j)'],
B q_j'-[8j+5+(2j+1)B']q_j = -2(j+1)a_(j+1)+sum_(i=1..j)[(2(j-i)+1)v_{2i}'q_(j-i)/(2i+1)-v_{2i}q_(j-i)'].

These use the negatives of the report's right-side convention. Empty sums verify T_1 and V_0 from the fixed factors; the definition of v_2 verifies initial curl. Homogeneous factors are t^l and t^jY, with orders 10l and 10j+6.

For Bf'-hf=g analytic at0 and homogeneous z=u^m times a nonvanishing analytic unit, g/(Bz) has pole order at most m+1. Integrating its finite principal part proves that zero residue gives an analytic solution f=zP and one arbitrary multiple of z. A nonzero residue produces r z log|u|; its m-th derivative has a nonzero logarithmic divergence, whereas the nonlogarithmic particular part is analytic. Thus there is no one-sided C^m solution, and a two-sided smooth solution must be analytic. The two one-sided homogeneous constants must agree by continuity of the m-th derivative. This proves smooth-to-analytic uniqueness, not merely analytic uniqueness.

At step n>=2, delta a_n=E t^n, delta q_(n-1)=-2n E t^(n-1)YG+F t^(n-1)Y and delta v_{2n}=-delta q_(n-1)/(2n). Only the distinct terms j=1 and j=n vary in each next forcing. There are no products of varied factors. Before thermal compatibility, remove its recorded residue divided by u and choose zero Laurent constant in its primitive. This defines an affine trial coefficient. The next vorticity residue depends only on its terms through u^(10n+6), while the omitted thermal logarithm starts at u^(10n+10); its normalized vorticity contribution is O(u^3 log|u|). Adding t^(n+1) changes this integrand by a multiple of G', with zero residue. Thus the affine convention is coherent.

P321 proves the general-a,H coefficients
r_E=208n a+(12/5)(n/3+1/(2n+1))Ck, r_F=0,
s_F=(208n-26)a+((n+1)(8n-9)/(10n))Ck,
s_E=-3n k^8/385-3(n+1)(6n-5)Hk/[5(2n+1)].
The pole-order-at-most-12 estimate belongs to coefficient variations only. It does not bound the fixed forcing. Unit corrections of relative order12 cannot affect those variation residues; differentiated curvature terms B'' and B''' must be retained. Substitution gives [[12Ck/(5(2n+1)),0],[-k^8(2n+5)/(385(2n+1)),-9Ck/(10n)]] and determinant -54C^2k^2/[25n(2n+1)] nonzero. Both constants are fixed uniquely. Base compatibility is P303/P306, independently rederived in A173, and agrees with n=2 in 4.55. Induction fixes every coefficient permanently after finitely many steps. Comparing the first differing pair proves uniqueness among smooth hierarchies.

On the claimed disk, |B/u-1|<1/2. The regular logarithmic derivatives are (-6k-4Ck u^11/65)/(B/u) and (-4k-7Ck u^11/260)/(B/u). Their primitives exponentiate to nonzero units on that entire disk, and G'=u^3 times an analytic unit. Each zero-residue scalar forcing has only a pole at0. Its meromorphic primitive is single valued: the finite principal part integrates without a logarithm and the holomorphic remainder has a primitive on the disk. Multiplication by z removes the pole. Products and derivatives preserve holomorphy on the same open disk. Induction gives the common interval without a limiting process in the coefficient index. Reality follows from real data and conjugation. This is precisely P326's continuation argument.

All surrounding replacements must retain the prescribed-family and local-formal limitations. The sign restriction Ak<0 is conditional on extra sign hypotheses of 4.54, not imposed on this general local family. A173, A174 and the lead computations supply finite checks, not the proofs. A174 accepts the all-order hierarchy as input. Both referee Bedrock attempts failed before inference and are not Opus endorsements; actual Opus reviews of P321/P326 are separately recorded.

## Literal integration verification
Independently parse eight Z sections, insert Z1 before section5, apply each unique old/new pair once, append the unique table row, and reconstruct the timeline. Compare every token with the frozen preview; also compare all prior table rows and timeline entries. Parse matrices as data, never execute lead code. Recompute their entries and base residues with exact rational arithmetic. Verify source hashes and preserve failures. Equality of the entire text confines changes to declared edits.

## Scope
No convergence in x, uniform coefficient bound, attachment to the material center, canonical whole-plane inverse or B2 profile follows. General B2 remains OPEN. No JavaScript/TypeScript, no servers/listeners, no RLScience cluster, no Lean/Lake builds; write only in verification.

## Exact prime certificates for the reported modular controls
If N-1 has a complete factorization into already certified primes and a^ (N-1)=1 modulo N, while a^((N-1)/q) is not1 modulo N for every prime divisor q of N-1, the multiplicative order of a is exactly N-1. It divides the order of the group of units modulo N. That group has at most N-1 elements, and for composite N has fewer, so N is prime. A recursive certificate bottoms out at2. Candidate factorizations and witnesses can be generated by any method; the consumer must independently multiply all factors and verify each modular power. This supplies exact arithmetic justification for the two finite fields in the lead log.
