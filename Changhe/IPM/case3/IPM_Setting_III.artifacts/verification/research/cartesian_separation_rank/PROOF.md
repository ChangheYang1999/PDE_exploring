# Infinite Cartesian separation rank forced by the far field

Verifier result 108. Written 2026-10-21 before supporting code.

## Statement and scope

No exact profile in the primary class of PROMPT.md has finite Cartesian separation rank on the upper half-plane, even if such a representation is required only outside a fixed disk. Precisely, there cannot exist a finite N, functions F_j:R->R and G_j:(0,infinity)->R, and R0<infinity such that

    rho(x,y)=sum_(j=1)^N F_j(x)G_j(y)
       whenever y>0 and x^2+y^2>R0^2.                    (1)

No regularity is assumed for the individual factors. The conclusion is a restricted nonexistence result. It excludes finite sums of separated Cartesian shapes, but not arbitrary densities, nor approximations whose separation ranks increase. It does not give the principal NO endpoint.

More generally, the nonzero homogeneous far field of such a profile has infinite Cartesian separation rank on y>0. The proof below needs only its Holder regularity with an exponent alpha larger than its homogeneity degree p. It does not use the all-order far-field continuation theorem or analyticity.

## 1. Profile inputs already established

For an exact primary profile, set p=1/ell in (0,1). The canonical inverse, density and gradient growth assumptions, and exact transport give a limit

    R^(-p)rho(RX) -> h(X)=|X|^p Theta(arg X),             (2)

uniformly on compact annuli as R tends to infinity. This limit is homogeneous of degree p, has the density parities, satisfies

    |h(X)| <= C |X|^p,

and belongs to C^alpha locally on the punctured plane for every alpha<1. The y-axis coefficient is nonzero:

    h(0,y)=K y^p for y>0, K!=0.                          (3)

These inputs, including the canonical inverse and the absence of a sign or global source-basin assumption, are proved in ../far_field/PROOF.md, ../far_field_holder/PROOF.md and ../scaling/PROOF.md. The nonzero angular version also appears in ../nonzero_far_field/PROOF.md. Their role is explicit: (2), the Holder exponent gap p<alpha<1, and (3) are the only profile properties needed below. A nonprofile passing one or two projected equations need not have this far field.

For fixed y>0, x -> h(x,y) is C^alpha near x=0, and has global growth at most C_y(1+|x|)^p. At a horizontal-axis point (x0,0) with x0!=0, h is C^alpha in a neighborhood. Both facts follow from the punctured-plane Holder statement. We fix one exponent alpha in (p,1).

## 2. An elementary finite-dimensional dilation lemma

Let V be a finite-dimensional vector space of real functions on R, preserved by every positive dilation

    T_s f(x)=f(sx),  s>0.

Assume every f in V satisfies a bound |f(x)|<=C_f(1+|x|)^p for all x, and is Holder of exponent alpha at zero, where alpha>p>0. Then every f in V is constant.

Proof. Consider the finite-dimensional dilation-invariant space

    W={f-f(0): f in V}.

If W is nonzero, choose a basis g_1,...,g_d. There are d evaluation points x_1,...,x_d such that the matrix g_j(x_i) is invertible. Indeed evaluation functionals span the dual of W: a vector annihilated by every evaluation is the zero function. Selecting a basis from that spanning family gives the required points. The norm

    ||g||_*=max_i |g(x_i)|

is therefore a genuine norm on W, and the coefficients of g in the chosen basis are bounded by C||g||_*.

Each g_j vanishes at zero. Its local Holder bound and global growth bound, combined with the coefficient estimate, give constants C and delta>0 independent of g such that

    |g(x)| <= C ||g||_* |x|^alpha             (|x|<=delta),
    |g(x)| <= C ||g||_* (1+|x|)^p            (all x).       (4)

For all sufficiently small s>0 the first estimate at sx_i yields

    ||T_s||_(W->W) <= C1 s^alpha.

The second estimate at x_i/s yields

    ||T_(1/s)||_(W->W) <= C2 s^(-p).

But T_s T_(1/s) is the identity on the nonzero normed space W. Hence

    1 <= C1 C2 s^(alpha-p),

which is impossible as s decreases to zero. Thus W=0, proving the lemma. No differentiability of the dilation group, classification of Euler eigenfunctions, or power-series argument is used.

The strict exponent gap is necessary. The space spanned by |x|^p is invariant under positive dilation and has growth and origin Holder exponent p. It is a nonconstant finite-dimensional example when alpha=p.

## 3. Finite rank contradicts the limiting field

Suppose h has rank at most N on y>0. Then

    V=span{h(.,y):y>0}

has dimension at most N. Conversely this finite-dimensional span itself is a finite-rank representation, by evaluating coefficients in any basis.

Homogeneity gives

    h(sx,y)=s^p h(x,y/s).

Thus V is preserved by every positive dilation in x, with inverse dilation also preserving it. Every element of V is Holder of exponent alpha near x=0 and has growth O((1+|x|)^p), by Section1 and finite linear combinations. The lemma makes every element constant in x. Evaluating at x=0 and using (3) forces

    h(x,y)=K y^p,  y>0.                                  (5)

Fix x0!=0. Continuity gives h(x0,0)=0 from (5). Its C^alpha regularity there would imply |K|y^p<=C y^alpha for sufficiently small positive y. Since alpha>p and K!=0, this is impossible. Therefore h has infinite separation rank.

This argument also shows where its regularity hypothesis matters: K sign(y)|y|^p has rank one on y>0 and satisfies the same homogeneity and growth, but it has only Holder exponent p across y=0. It is excluded by the established far-field regularity, not by growth alone.

## 4. Passage from an exterior representation to the far field

Assume (1). For arbitrary evaluation points x_1,...,x_(N+1) in R and y_1,...,y_(N+1)>0, the matrix

    [R^(-p)rho(R x_i,R y_j)]_(i,j)

has rank at most N for all sufficiently large R, because all its arguments then lie outside the fixed disk and (1) applies to every entry. Its determinant is zero. Taking the entrywise limit from (2) gives

    det[h(x_i,y_j)]_(i,j)=0                              (6)

for every such set of points.

These determinant identities force dim span{h(.,y):y>0}<=N. Otherwise choose N+1 independent functions from the span, and then evaluation points separating them as in Section2. Expansion of the resulting nonzero evaluation determinant by linearity would produce a nonzero determinant made of N+1 actual sections h(.,y_j), contradicting (6). Equivalently one can first choose N+1 independent sections directly, since the sections span the space. This contradicts Section3 and proves the theorem.

Only entrywise convergence on each finite point set is needed to pass the rank bound. The known uniform annular convergence supplies it. No convergence or boundedness of the separated factors themselves is needed.

## 5. A finite-data consequence and manufactured verification

For every N, infinite rank supplies N+1 horizontal points and N+1 positive vertical points with a nonzero evaluation determinant. On that fixed grid a field of rank at most N cannot approximate h arbitrarily well. If n=N+1, the entries of the true matrix have magnitude at most B, and the entrywise error eta is at most1, the determinant telescoping identity gives

    |det H-det G| <= n n! (B+1)^(n-1) eta.                (7)

Indeed each permutation contributes a product of n entries; replace its factors one at a time, bounding the other factors by B+1. There are n! permutations. For rank(G)<=N, det G=0, giving the strictly positive error lower bound

    eta >= min(1, |det H|/[n n! (B+1)^(n-1)]).            (8)

This is a bound for an identified finite grid, not a universal quantitative rank bound for unknown profiles.

The supporting manufactured field is

    h_test(x,y)=y (x^2+y^2)^(-1/3), X!=0.

It has p=1/3, the required parities and smoothness on the punctured plane, K=1, and |h_test|<=|X|^(1/3). It is not asserted to satisfy either IPM equation. On grids x_i=0,...,n-1 and y_j=1,...,n, its entries can be enclosed exactly using rational lower and upper bounds for positive cube roots. The test will compute nonzero determinant intervals and (8) for n1 through6. These finite checks support the data and determinant algebra only. The all-N theorem is proved by Sections2-4, not by extrapolating them.

## Dependencies, review and status

The external rep7 review suggested a separation-rank exclusion using smooth far-field data and an Euler-generator argument. This independent proof replaces that step by the elementary Holder exponent-gap lemma, drops the all-order far-field dependency, and includes exterior representations. Frozen source provenance and exact supporting tests belong in verification/. Actual Opus5.5 lead review remains to be recorded separately. The result is a proved restricted exclusion, subject to the already checked far-field inputs, and does not exclude general profiles.
