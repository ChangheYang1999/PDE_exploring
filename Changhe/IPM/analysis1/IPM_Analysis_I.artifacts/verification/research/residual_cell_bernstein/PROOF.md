# Real-interval refinement of the three-cell derivative bounds

## Statement and dependencies

Use the exact modal trial and the three closed cells in residual_cell_cauchy/PROOF.md, with its mandatory addendum, resolutions, adjudication and accepted verdict. In each cell let t=t_c+h z, h>0, |z|<=1. All522 residual modes have validated coefficient boxes through degree64 and the explicit derivative-tail bound T_ij of that result, for i+j<=5. The boxes enclose the same exact Taylor coefficients of the entire local continuations. Canonical center inputs remain inherited; no new integration or radial coverage is claimed.

Intersect the two validated overlapping boxes for a_Nq, and write the exact rational intersection as [m_Nq-r_Nq,m_Nq+r_Nq], with r_Nq>=0. Put P_N(z)=sum_{q=0}^{64}m_Nq z^q. For i<=5, define

    E_Ni=sum_{q=i}^{64}(q)_i r_Nq.

On |z|<=1 the derivative of the uncertain degree64 polynomial differs from P_N^(i)(z) by at most E_Ni. This follows term by term from |z|^(q-i)<=1 and does not use correlation assumptions. The previously proved analytic tail is separate.

Partition [-1,1] into eight equal closed subintervals [a_s,b_s], s=0,...,7, with a_s=-1+s/4, b_s=a_s+1/4. The number eight is fixed before the real-interval computations. Set d=64-i. Express the exact polynomial P_N^(i)(a_s+(b_s-a_s)u) in the Bernstein basis of degree d on 0<=u<=1, with coefficients beta_Nisk. Define

    M_Nis=max_{0<=k<=d}|beta_Nisk|+E_Ni.

Then for each cell and i+j<=5,

    sup_cell sum_N (2N+1)^j |D_t^i epsilon_N(t)|
    <= h^(-i) max_s sum_N (2N+1)^j M_Nis + T_ij.

This is the intended new bound. A minimum with a previously proved upper bound is allowed, but both constituent bounds and their actual values must be retained. No smaller bound is assumed in advance. Saved producer caps remain a diagnostic comparison, not inputs. If this new bound is below a saved cap it validates that cap only for the designated cell and derivative, conditional on the explicitly inherited canonical certificate. A new upper bound above a saved cap does not refute it.

## Bernstein coefficient formula and range proof

For a polynomial Q(u)=sum_{q=0}^d c_q u^q, the degree-d Bernstein coefficients are

    beta_k=sum_{q=0}^k c_q binom(k,q)/binom(d,q).

Indeed u^q=sum_{k=q}^d [binom(k,q)/binom(d,q)] binom(d,k)u^k(1-u)^(d-k). Cancel the binomial factors and factor u^q; the remaining sum is (u+(1-u))^(d-q)=1. Therefore Q=sum_k beta_k B_k^d, where B_k^d(u)=binom(d,k)u^k(1-u)^(d-k). These weights are nonnegative and sum to1, so |Q(u)|<=max_k |beta_k|. This remains true if the actual degree is less than d, with zero missing power coefficients.

For Q(z)=sum c_q z^q, substitution z=a+w u gives exact power coefficients

    c'_p=w^p sum_{q=p}^d c_q binom(q,p)a^(q-p).

Applying the preceding formula computes each local Bernstein vector using only exact rational arithmetic. Polynomial composition with a rational linear polynomial is an equivalent finite operation.

## Independent subdivision construction

A second algorithm starts with the global Bernstein vector on [-1,1] and subdivides it three times at midpoints. If beta_0,...,beta_d is a vector on one interval, the vectors on its left and right halves are

    L_k=2^(-k) sum_{q=0}^k binom(k,q) beta_q,
    R_k=2^(-(d-k)) sum_{q=0}^{d-k} binom(d-k,q) beta_{k+q}.

Substituting these formulas in the Bernstein expansion and applying the binomial theorem gives Q(v/2) and Q((1+v)/2), respectively. Equivalently, form successive rows by averaging adjacent entries. The successive leftmost entries give L in increasing order; the successive rightmost entries, reversed, give R. Repeating on each half yields the same eight ordered local Bernstein vectors as direct affine composition.

The first algorithm will use exact fmpq polynomial composition and the exact coefficient formula. The second will use Arb balls and repeated midpoint averaging. They share the proved Bernstein identity but not the local affine-composition algorithm. Both read the original retained Taylor enclosures, reconstruct their exact intersections, differentiate the midpoint polynomials and account separately for E_Ni. Every saved modal/subinterval maximum and coefficient-radius contribution must be compared or independently rechecked. Do not infer correctness solely from sampled polynomial values.

## Full range conclusion

For each real z choose a subinterval containing it. The Bernstein convex-hull bound and coefficient uncertainty yield |D_z^i polynomial_N(z)|<=M_Nis. Multiply by the nonnegative angular weight and sum over N. Maximizing over the eight intervals gives the finite part in the statement. Multiplying by h^(-i) converts z derivatives to t derivatives. The inherited Cauchy estimate bounds the summed, angularly weighted derivatives of all omitted terms on the whole cell by T_ij, so adding it proves the result, including shared subinterval endpoints.

This theorem concerns only the same three cells. It does not supply a complete radial cover, a physical maximum location, a global forcing norm, an inverse estimate, nonlinear closure or an IPM endpoint. Exact arithmetic, source pins, coefficient coverage and independent comparison must pass before any output is accepted.
