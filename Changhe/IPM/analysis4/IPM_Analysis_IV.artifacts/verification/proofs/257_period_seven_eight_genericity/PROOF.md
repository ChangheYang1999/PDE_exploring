# Generic tuning from an irreducible two-mode specialization

Status: PROVED in V532 after the independent review of18:35Z. The period-seven and period-eight inputs are proved in253 and256.

## Statement

Fix an integer Q>=3, delta=2/Q, c=Q/(Q-2), and an even integer B>=6. Put d=B/2-2 and normalize the leading profile as

    f_1(b,t)=sin(theta)+b sin(3theta)
               +sum_(j odd,5<=j<B) t_j sin(j theta),
    t in R^d.

Use the fixed pure sine recurrence, with density exponents p_n=1-2n/Q, stream exponents P_n=2-2n/Q and zero homogeneous stream coefficients below the first nontrivial resonance2Q. Let O(b,t) be the sin(theta) coefficient of f_(2Q). Assume:

1. O(b,0) has degree2Q and is irreducible over Q, up to a nonzero rational constant.
2. There is a real b_* with O(b_*,0)=0 for which every response sigma_k(b_*,0), k>=2, and the limiting response sigma_infinity(b_*,0) is nonzero.

The response sigma_k is the change in the sin((2k-1)theta) coefficient of f_(Q(k+1)) caused by adding one unit of sin((2k-2)theta) to g_(Qk). It is defined by the Q-step affine response recurrence, whether or not the initial profile satisfies O=0.

Let M be the regular real hypersurface O=0, grad O!=0, and let

    G={x in M: inf_(k>=2)|sigma_k(x)|>0}.

Then G is relatively open and dense in every connected component of M, and M minus G has measure zero in every smooth coordinate chart. Every point of G determines a unique tuned pure density and stream series that converges on a sufficiently large exterior with all weighted derivatives and an associated convergent common-potential expansion. Compact subsets of G have a common sufficient exterior radius. The potential may include the permitted logarithmic terms at Q and2Q.

When B=6, M minus G is countable and relatively closed. Its accumulation points inside M belong to the finite set {O=0,sigma_infinity=0}. The theorem makes no nonexistence or divergence assertion at excluded points, at singular points of O=0, or at profiles with vanishing first sine coefficient.

For a general nonzero first coefficient epsilon, divide all amplitudes by epsilon. The responses acquire the factor epsilon^Q, and each sufficient radius acquires |epsilon|^(Q/2).

## Proof

### Polynomial structure

Every coefficient below the first nontrivial resonance is a homogeneous rational polynomial of its order in the leading amplitudes. Indeed, the recurrence only adds products of coefficients of complementary orders and divides by fixed nonzero rational scalars. At order Q the potential zero stream frequency is absent in the sine class, so it introduces no free coefficient or compatibility condition. Consequently O is a rational polynomial of total degree at most2Q after normalization.

The coefficient of b^(2Q) in O is nonzero by hypothesis1. Total degree implies that this coefficient is constant in t. Divide O by it to obtain a monic polynomial P in b, of degree2Q. Its specialization P(b,0) is irreducible.

P is irreducible in Q[t,b]. Otherwise a proper factorization P=A C has leading b coefficients whose product is1. These coefficients are units of Q[t], hence rational constants. Rescale A,C to be monic. Specializing t=0 preserves both b degrees and would factor P(b,0). Irreducibility of the specialization therefore forces one factor to have b degree0. A monic degree-zero polynomial in b is1, contrary to properness. Gauss's lemma gives irreducibility in Q(t)[b].

The response recurrence contains exactly Q leading amplitudes in each term. Thus every sigma_k is a rational polynomial of total degree at mostQ in(b,t). The compact response formula and its denominator separation for sufficiently large k show local uniform convergence, on finite complex parameter neighborhoods, to sigma_infinity. This limit is also a rational polynomial of total degree at mostQ: the compact expression is rational in the inverse carrier with rational-polynomial parameter coefficients, and its value at inverse carrier0 gives the limit. Hypothesis2 makes every one of these polynomials nonzero.

For h equal to a finite k>=2 or infinity, the b degree of sigma_h is less than2Q. Irreducibility of P in Q(t)[b] therefore implies coprimality. The resultant

    R_h(t)=Res_b(P(b,t),sigma_h(b,t))

is a nonzero rational polynomial. A common real zero of P and sigma_h projects to a zero of R_h. Monicity of P ensures that this implication survives specialization of t, even if the degree of sigma_h drops.

### Nonvanishing on every regular component

Points where partial_b P!=0 are dense in M. If partial_b P vanished on a nonempty relatively open piece, regularity would supply some partial_(t_j)P!=0 near a point of that piece. Write the hypersurface as t_j=phi(b,t_hat). Implicit differentiation gives partial_b phi=0 there. On a smaller coordinate box, phi is independent of b. Fixing t_hat then gives a fixed t for which P(b,t)=0 on an interval of b. This contradicts monicity and positive b degree.

If sigma_h vanished on any nonempty relatively open piece of M, that piece would contain a point with partial_b P!=0. Locally write b=beta(t), where t ranges over an open subset of R^d. Then R_h vanishes on that open subset, contradicting its nonzero polynomial character. In particular sigma_h is not identically zero on any regular connected component. This uses rational irreducibility to produce a resultant, and does not assume irreducibility over R or C.

Each response zero set on M is closed and nowhere dense. It has chart measure zero: a nontrivial real analytic function has a null zero set, as follows by covering its zeros with regular level sets of its derivatives. More explicitly, at each zero choose a first nonzero Taylor derivative; a derivative of one lower order vanishes there with nonzero gradient. A countable chart cover and the countable collection of derivatives yield a countable union of smooth hypersurfaces. Analytic continuation excludes an identically flat point unless the function vanishes on the component, which was ruled out above.

### Uniform positivity and convergence

Local uniform convergence of the responses gives

    inf_k|sigma_k(x)|>0
      iff sigma_infinity(x)!=0 and sigma_k(x)!=0 for every k>=2.

The reverse implication follows by separating the nonzero limit and taking the minimum of the remaining finitely many nonzero terms. Uniformity on a small neighborhood shows that this property is open. Its complement is the countable union of the finite and limiting response zero sets. Baire's theorem gives density on each regular component, and the preceding measure argument gives full measure.

At a point of G, the exact first compatibility and the positive response infimum are precisely the hypotheses of the integer-period tuning and convergence theorem131. They yield unique successive free coefficients and an analytic majorant for the resulting series. Reconstruction132 supplies the common potential and weighted derivative convergence. The permitted exceptional potential orders are Q and2Q. A compact subset of G has a finite cover of neighborhoods with positive response lower bounds and bounded leading norms, so one common majorant radius suffices.

### The three-mode case

When B=6 there is one t coordinate. Each nonzero R_h has finitely many zeros, and each fiber P(b,t)=0 has at most2Q points. Each individual response zero set on P=0 is therefore finite. Their union is countable and, because G is open, relatively closed in M.

Near a point where sigma_infinity!=0, local uniform convergence separates every response beyond one index K. Only the finitely many finite zero sets with k<K remain, so distinct exceptional points cannot accumulate there. The common zeros of P and sigma_infinity form a finite set by the same resultant argument. This proves the asserted accumulation restriction.

## Applications and verification status

At Q=7,253 proves that O(b,0) is irreducible of degree14, has ten simple real roots, and that every root has a uniform positive response bound, including its nonzero limit. Either one of these roots supplies hypothesis2. Hence the theorem applies at delta2/7.

At Q=8,256 proves the degree16 irreducible polynomial, its ten simple real roots, and a uniform positive response bound at every root. Thus both hypotheses hold and the theorem applies at delta1/4. One fully certified root would suffice for hypothesis2; all ten are not logically needed for genericity.

Dependencies: the independent recurrence01, general response and majorant131, common-potential reconstruction132, the component argument135, compact response149, and the exact arithmetic and complete covers253 or256. No finite growth fit is used.
