# A fixed irrotational spiral sector for a nonzero comparable profile

## 1. Exact conditional theorem

Let 2/5<c<1/2, omega be any real number, Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J and p=(1-c)/c. Suppose U in C2(R3;R3), P in C1(R3) satisfy

    LU+DU(Ax+U)+grad P=0, div U=0, U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1).

Let V and P2 be their actual velocity and normalized pressure tails, Pinf the pressure limit, D=R3 minus {0}, W=curl V, k=(Ax).V, E=|V|^2 and S=P2-E/2. Assume constants 0<r_-<=r_+<infinity satisfy

    r_-|S|<=E<=r_+|S| on the unit sphere.              (1)

If U is nonzero, there exist a nonempty relatively open spherical disk O, R>0 and v0>0 for which

    G={y: |y|>R, exp[(omega/c)log|y| J]y/|y| in O}

satisfies curl U=0 and |U(y)|>=v0|y|^(-p) throughout G. In particular U is a nonzero vector field with smooth harmonic components there and G has a fixed angular aperture on every sufficiently large sphere. This is a necessary-geometry theorem, not an exclusion of G.

A sufficient original-variable replacement for (1) is, for all sufficiently large |y|,

    r_-|P(y)-Pinf-|U(y)|^2/2|<=|U(y)|^2
      <=r_+|P(y)-Pinf-|U(y)|^2/2|.                  (2)

Under the theorem's assumptions, the additional condition that {curl U!=0} is dense relative to {U!=0} in some exterior implies U=0. This condition permits the zero field and open zero regions.

## 2. The exact dependencies and a nonempty rank-defect set

The confirmed natural-tail package A533/A538/A539 gives locally C1 convergence of the actual scaled fields below, V in C^(1,alpha) and P2 in C^(2,alpha) for every alpha<1. It supplies div V=0, twisted homogeneity, and Delta P2=-tr((DV)^2). Global helicity freedom gives W.grad S=0 and the actual tail rank relation

    grad k cross grad S=0 on {W!=0}.               (3)

For the original fields define H=P+|U|^2/2+(Ax).U and R0=P-|U|^2/2. The confirmed global C2 helicity-free identity A413 gives

    grad H cross grad R0=0 wherever curl U!=0.     (4)

Its global hypotheses are satisfied here. This identity is not asserted for arbitrary kinematic fields. The entire A413 argument and the natural-pressure/faithful-tail argument were reread during A1873-A1879 immediately before this audit.

A516/A570 says that V=0 implies U=0 under exactly the bounds in Section1. Its mechanism is grad P=O(r^(-2p-1)), the linear spiral integral giving U=O(r^(-2p-1)) when its limiting tail vanishes, and then vanishing drift, cubic and pressure fluxes in the radial energy identity. The coefficient 1-5c/2 is nonzero. Thus U nonzero implies V nonzero.

Write F_t=exp(tA) and a=1-2c. The homogeneities are k(F_t x)=exp(-at)k(x) and S(F_t x)=exp(-2(1-c)t)S(x). Since |V|^2 has the same scaling as S, (1) extends to every point of D. Choose alpha with 2/c-4<alpha<1, which is possible throughout the target interval. The confirmed natural-regularity full-rank comparison theorem A1866-A1871 then says that if (3) held on all {S!=0}, V would be zero.

Consequently, for nonzero U the set

    Sigma={x in D: S(x)!=0 and grad k cross grad S(x)!=0}

is nonempty and open. By (1), V!=0 throughout Sigma; by (3), W=0 there. The cross-product transformation is

    (grad k cross grad S)(F_t x)
      =exp(-(3-2c)t)exp(-omega tJ)(grad k cross grad S)(x).

Both factors are invertible, so Sigma is F_t-invariant and meets the unit sphere. On Sigma the linear Lamb identity grad k=Ax cross W-aV gives V=-grad k/a. Thus Delta k=0 there and V is smooth harmonic. Moreover P2+|V|^2/2 is harmonic there: DV is symmetric, Delta V=0, Delta P2=-|DV|^2, and Delta(|V|^2/2)=|DV|^2. None of this proves continuation across its boundary.

Choose a spherical disk O with compact closure inside Sigma intersect S2. Shrink it until |V|>=2v0>0 and |grad k cross grad S|>=d0>0 on its closure.

## 3. Passage to exact original irrotationality

Put b=2(1-c) and define

    u_t(x)=exp((1-c)t)exp(omega tJ)U(F_t x),
    p_t(x)=exp(bt)(P(F_t x)-Pinf),
    h_t(x)=exp(at)(H(F_t x)-Pinf),
    r_t(x)=exp(bt)(R0(F_t x)-Pinf).

The identities, with no asymptotic error, are

    h_t=(Ax).u_t+exp(-t)(p_t+|u_t|^2/2),
    r_t=p_t-|u_t|^2/2.

Natural-tail convergence therefore gives h_t->k, r_t->S and u_t->V in C1 on a compact neighborhood of the chosen closed disk. This uses convergence of the actual scaled fields, not an independently chosen homogeneous solution.

For every sufficiently large t and all x in the closed disk,

    |u_t(x)|>=v0,    grad h_t(x) cross grad r_t(x)!=0.

The chain rule gives grad h_t=exp(at)F_t^T grad H(F_t x), and the corresponding formula with b and R0. Applying the same invertible matrix to two vectors preserves their linear dependence. Thus grad H cross grad R0 is nonzero at F_t x. The contrapositive of (4) gives curl U(F_t x)=0. This step proves exact zeros in the original field. Convergence to a zero tail curl alone would not suffice.

For x on the unit sphere, |F_t x|=exp(ct), and orthogonality gives

    |U(F_t x)|=exp(-(1-c)t)|u_t(x)|
               >=v0 |F_t x|^(-p).

The map (t,x)->F_t x is a smooth bijection from (t0,infinity) times O onto G, with smooth inverse

    t=log|y|/c,
    x=exp[(omega/c)log|y| J]y/|y|.

Choosing R=exp(ct0) proves the stated open sector and lower bound. Since div U=curl U=0 there, Delta U=0 distributionally; local harmonic regularity gives smooth harmonic components. No assumption about the completeness of the nonlinear characteristic flow is needed in this passage.

## 4. Original comparison and the weaker density corollary

For a fixed x in D, F_t x eventually lies in the exterior where (2) holds. Multiply that inequality by exp(bt). The two resulting quantities are |u_t(x)|^2 and |p_t(x)-|u_t(x)|^2/2|. Their limits are E and |S|, proving (1) with the same constants. The subtraction of Pinf is essential and has not been replaced by a free pressure normalization.

Let E_ext denote any exterior region. Failure of density of {curl U!=0} relative to its open subset {U!=0} means there is a point of {U!=0} with a neighborhood in E_ext disjoint from {curl U!=0}. Shrinking inside {U!=0} gives a nonempty open irrotational region with nonzero velocity. Conversely any such region contradicts relative density. Thus relative density is equivalent to U vanishing on every open irrotational subset of that exterior.

If U were nonzero under the theorem's hypotheses, Section3 would produce an open irrotational sector with nonzero velocity extending beyond every radius. This contradicts the additional relative-density assumption in any exterior. Hence U=0. No density on the whole exterior, no density of tail vorticity, and no A2 weight premise has been inserted.

## 5. Audit verdict and limits

LIT271 is confirmed at the exact global profile, helicity-free, natural-bound and comparison scope of Section1. The full-rank comparison theorem replaces the earlier A2 premise only in the step forcing Sigma to be nonempty. The direct rank-to-sector passage was already established in A604 and is reconstructed in Section3 with a fixed angular disk and an explicit nonzero lower bound.

The theorem does not exclude this sector, extend rank across arbitrary irrotational holes, or derive helicity freedom, comparison or the natural derivative bound from bare decay. It applies to every finite omega; it does not assert uniform constants as |omega| tends to infinity. No computation, new model client, new agent, formal build or remote execution was used. Existing configured model comparison continues through working files, with actual provider runtime independently unattested.
