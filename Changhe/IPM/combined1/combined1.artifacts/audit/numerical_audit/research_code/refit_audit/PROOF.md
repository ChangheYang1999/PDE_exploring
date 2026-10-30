# Independent conversion and audit of exact generator refits

## Statement and input contract

Let c>1 be exact rational. Put delta=1-1/c, p_j=(3+1/c-j delta)/2, r^2=x^2+y^2, R=1+r^2, t=r^2/R and H_m=Re(x+iy)^(2m). The input JSON defines the finite smooth potential

chi = sum a H_m R^(p_j-m) T(t).

Here each a is an exact rational, and each generator specification is either [mono,h], meaning T=t^h, or [leg,w,n], meaning T=t^w P_n(2t-1). The Legendre normalization, if any, is already included in a. These semantics are stated in each source JSON and in the archived n12_exact.py header. No floating projection is performed by this audit.

## Conversion identity and proof

Expand T(t)=sum_l b_l t^l using the three-term Legendre recurrence. Since H_m=r^(2m) cos(2m theta),

H_m R^(p_j-m) t^l = r^(2(m+l)) R^(p_j-m-l) cos(2m theta).

Consequently a generator contributes exactly a b_l to canonical coefficient (j,m,m+l). Summing coincident triples gives the same potential at every point, including its smooth value at the origin. The recurrence uses rational arithmetic, so this is an algebraic identity without approximation.

## Center, tail and point checks

The canonical center formula and derivative identities in ../baseline/PROOF.md apply without a restriction on the number of branches. The rational strain is checked against 1-c. Expanding R^(p_j-k)=r^(2p_j-2k)(1+r^-2)^(p_j-k) gives the potential sector of radial descendant q by the exact binomial coefficient binom(p_j-k,q). Cartesian differentiation and multiplication give the residual sector E[h,q] at exponent 1/c-h delta-2q, as proved in ../sector_audit/PROOF.md. All sectors of exponent at least -2 are tested individually. For this exact c they are (h,q)=(0,0),...,(5,0),(0,1),(1,1). Descendants q>=2 have exponent below -2.

The leading branch and c are compared with the canonical state131 input, rather than with rounded displays. The first surviving sector is obtained by sorting all computed exponents and requiring a nonzero exact coefficient. In particular one must not omit q=1 descendants when determining that first sector.

The point evaluator and exact radial Fourier representation in ../radial_fourier/PROOF.md apply unchanged. Arb enclosures at rational points can certify a violated necessary pointwise condition. They do not establish positivity on an unsampled region. A full-plane norm requires the separate integration argument, not this conversion.

## Dependencies and scope

Dependencies are the exact input contract, the three-term Legendre recurrence, the chain and product rules, and the preceding independently derived canonical identities. A confirmed admissibility claim concerns the stated far-field cancellations and smooth finite potential only. It does not assert residual smallness, all background conditions, or existence of a solution.
