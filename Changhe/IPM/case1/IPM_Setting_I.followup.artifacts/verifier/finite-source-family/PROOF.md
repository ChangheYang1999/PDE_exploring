# Arbitrarily many independent source data for actual coupled cone solutions

Date: 2026-10-20. Status: complete informal proof written before coefficient checks. This is a local cone family. It gives no family of the global profiles in TASK.md.

## Statement

Fix A>1, g>0 and finitely many distinct odd integers 3<=m_1<...<m_d. Set

    h=1-1/A>0, b=g/[2(A-1)],
    q_i=(m_i-1)/A, p_i=1+(m_i-1)h,
    0<kappa<1/sqrt(1+b).

For any real amplitudes C_1,...,C_d there is R>0 and a real analytic solution on 0<r=-s<R, |y|<kappa r of

    (As partial_s+y partial_y-1)v+gV_2+V.grad v=0,
    div V=0, partial_s V_2-partial_y V_1=-v_s.          (1)

The functions v,V_2 are odd in y, V_1 is even, and V(-r,0)=0. All fields and their first derivatives vanish at the vertex. Hence f=gy+v, W=(As,y)+V solve the local coupled source equations with source jet diag(A,1). The amplitudes parameterize distinct solutions. On a common sufficiently small cone they depend analytically on the amplitudes in each bounded set.

If not all amplitudes are zero, let i be the smallest index with C_i nonzero and put p=p_i. The pair has the same exact density regularity at the vertex as in ../higher-source-cone/PROOF.md: C^(floor(p),p-floor(p)) for noninteger p, and C^(p-1,1) but not C^p for integer p. The stronger regularity failures concern density; the positive bounds apply to both fields. If all amplitudes vanish the pair is zero.

For the set {3,5,7}, abbreviate lambda=2/A and let G_j=partial_y^j v(-r,0)/j!. There are exact identities

    G_3=C_3 r^(-lambda),
    G_5=-b lambda(lambda+1)C_3 r^(-lambda-2)/20
                                      +C_5 r^(-2lambda),
    G_7=b(b+1)(lambda)_4 C_3 r^(-lambda-4)/1680
          +[-b(2lambda)(2lambda+1)C_5/42
             -lambda(3-2lambda)C_3^2/(40(A-1))]
                                           r^(-2lambda-2)
          +C_7 r^(-3lambda).                            (2)

Here (x)_4=x(x+1)(x+2)(x+3). Thus C_3,C_5,C_7 are independently prescribed renormalized axis data at the source, with the forced lower-order contributions displayed. These are not the center coefficients B_3,B_5,B_7. The theorem does not match any center, impose a canonical inverse, or continue across the line s=0 away from its vertex.

## Coefficient construction

For a nonzero multiindex a=(a_1,...,a_d) of nonnegative integers put

    N=|a|, p_a=1+sum_i a_i(p_i-1),
    J_a=1+sum_i a_i(m_i-1),
    M_a=J_a+2(N-1)=sum_i a_i(m_i+1)-1.

All J_a,M_a are odd. Seek a triple r^(p_a)(phi_a(z),alpha_a(z),beta_a(z)) with z=y/r and the stated parities. For a prescribed density forcing r^(p_a)H_a(z), coefficient comparison in (1) and the div-curl equations gives, at odd angular index j,

    c_j phi_(a,j)+g beta_(a,j)=H_(a,j),
    c_j=(A-1)(J_a-j),
    beta_(a,j+2)=-(p_a-j)(p_a-j-1)
                         (beta_(a,j)+phi_(a,j))/[(j+1)(j+2)],
    alpha_(a,j+1)=(j-p_a)(beta_(a,j)+phi_(a,j))/(j+1).    (3)

Set alpha_(a,0)=beta_(a,1)=0. These recurrences follow from

    (A p_a-1)phi+(1-A)z phi'+g beta=H,
    beta'=p_a alpha-z alpha',
    -p_a beta+z beta'-alpha'=p_a phi-z phi',

using partial_s(r^p phi(z))=-r^(p-1)(p phi-z phi'). Conversely (3) imposes every coefficient of these three equations.

For a=e_i take H=0 and choose its one resonant coefficient phi_(e_i,m_i)=C_i, with all lower coefficients zero. The resulting analytic germ is

    phi_(e_i)=C_i sum_(l>=0) (-1)^l(b)_l(q_i)_(2l)m_i!
                                      z^(m_i+2l)/[l!(m_i+2l)!].       (4)

The velocity follows from (3). Its orders are m_i+1 and m_i+2. The ratio formula in (4) verifies the recurrence directly and proves radius at least one.

For N>=2 set

    H_a=sum_(u+v=a, |u|,|v|>=1)
           [alpha_u(p_v phi_v-z phi_v')-beta_u phi_v'].              (5)

At every lower order the radial identity p_u+p_v-1=p_a holds. The first possible angular degree is

    M_u+M_v+1=M_a.

Since the resonance is J_a=M_a-2(N-1), it is unforced. Choose its free coefficient to be zero, together with all other density coefficients below M_a. Recurrence (3) constructs a unique triple with

    phi_a=O(z^M_a), alpha_a=O(z^(M_a+1)), beta_a=O(z^(M_a+2)).        (6)

Radial degrees can coincide for different multiindices, for example p_(2e_1)=p_(e_2) when (m_1,m_2)=(3,5). They are allowed to coincide. The independent coefficients in (5) are bookkeeping by amplitudes, and their sums still solve the same linear equation. No distinctness of radial degrees is used.

## Uniform inverse and convergence

Use ||u||=sum_j |u_j|kappa^j and ||H||_-1=sum_(odd j>=1)|H_j|kappa^j/j. Because 0<p_a<J_a<=M_a for all a, the last two recurrences in (3) give, first for finite partial sums,

    ||beta_a||<=B||phi_a||,
    ||alpha_a||<=kappa/(1-kappa^2)||phi_a||,
    B=kappa^2/(1-kappa^2).

Indeed the absolute ratios in (3) are less than one before the factors kappa^2 and kappa are restored. Let m_max=m_d. For N>=2 and j>=M_a,

    j/(j-J_a)<=M_a/[2(N-1)]<=(2m_max+1)/2,
    g/|c_j|<=b.

The first bound follows from M_a<=N(m_max+1)-1, whose indicated ratio is largest at N=2. Thus

    ||phi_a||<=L||H_a||_-1,
    L=(2m_max+1)/[2(A-1)(1-bB)].                       (7)

The denominator is positive by the cone aperture condition. These inequalities bound every finite coefficient sum, so monotone convergence justifies both the infinite norm and the analytic solution of the recurrence. No convergence assumption is built into (7).

In each product of (5), its output degree is at least the degree l of the differentiated density coefficient. Since l>=M_v>p_v, the factors |p_v-l|/output_degree and l/output_degree are at most one. Hence

    ||H_a||_-1<=2kappa/(1-kappa^2)
                         sum_(u+v=a)||phi_u||||phi_v||.

Put a_N=sum_(|a|=N)||phi_a||, and

    K=(2m_max+1)kappa/[(A-1)(1-kappa^2)(1-bB)],
    a_bar=sum_i |C_i|kappa^(m_i)/[1-max(1,b)kappa^2].

The germ ratios imply a_1<=a_bar. Summing the preceding estimate over all multiindices of length N gives

    a_N<=K sum_(j=1)^(N-1)a_j a_(N-j),
    a_N<=Catalan_(N-1)K^(N-1)a_1^N.                  (8)

Every ordered pair of multiindices occurs once in this sum. No missing combinatorial multiplicity remains.

Let delta=min_i(p_i-1)>0. For 0<r<=1, p_a>=1+Ndelta, so (8) proves absolute normal convergence of

    (v,V)=sum_(a nonzero) r^(p_a)(phi_a,alpha_a,beta_a)(y/r)          (9)

on any cone with R<=1 and 4K a_bar R^delta<1. If a_bar=0 the series is zero. On smaller angular disks, arbitrary angular derivatives are controlled by the geometric coefficient margin. Radial derivatives cost a polynomial in p_a=O(N) times a power of r, and the geometric margin in (8) absorbs that polynomial on each positive radial compact interval. For complex r,z with Re r>0, |r|<R and |z|<kappa, define r^p_a=exp(p_a log r) by the holomorphic logarithm. Each p_a is real, so |r^p_a|=|r|^p_a. Bound (8) proves locally uniform convergence on this complex domain as well. The sum is holomorphic, and its composition with r=-s,z=y/r is real analytic at every real cone point. Thus (9) may be differentiated and multiplied termwise. Equations (3),(5) then prove (1) exactly.

Each coefficient triple is a homogeneous polynomial of degree a_i in each amplitude C_i. This follows from (4), the bilinear forcing and the linear inverse (7). Applying the same absolute norm estimates to complex amplitudes in a bounded polydisk proves normal convergence there on a common smaller cone. Consequently the real solution depends real analytically on the amplitudes. This is a local parameter claim; it refers to none of the function spaces for the global profile problem.

## Independence, traces and regularity

At the first index m_i where two amplitude vectors differ, all contributions to the angular coefficient of degree m_i that use smaller seeds agree. Terms that use a larger seed have higher angular degree. Terms that involve m_i and any other seed have degree at least m_i+4>m_i by (6). Thus the difference of the corresponding axis coefficients is exactly

    (C_i-C_i')r^(-q_i).

It is nonzero, proving that the solutions are distinct and all d parameters are independent. This argument avoids any claim that the raw unrenormalized G_(m_i) is determined solely by C_i.

For {3,5,7}, the angular orders show that only the three linear germs and the quadratic (3,3) interaction can affect G_7. The linear germ coefficients in (4) give all linear terms in (2). For two cubic germs, the coefficient of z^7 in (5) is lambda(3-2lambda)C_3^2/20. The inverse coefficient is c_7=-2(A-1), so the density correction is -lambda(3-2lambda)C_3^2/[40(A-1)]. Its radial exponent after seven y derivatives is -2lambda-2. This proves (2), including possible cancellation when lambda=3/2. Since 0<lambda<2, the three displayed radial exponents in G_7 are distinct. The identities explicitly recover C_3,C_5,C_7 after subtracting lower forced terms.

For regularity, remove any zero-amplitude seeds and let p be the smallest remaining p_i. The leading term in (9) is its nonzero germ r^p phi_(e_i)(y/r); all other terms have a strictly higher radial degree. On every smaller closed cone, termwise differentiation with the norm bounds gives

    |D^h(v,V)|<=C_h r^(p-h)

for every fixed integer h. The standard two-point estimate, using the next derivative along a segment at comparable depths and the amplitude bound for separated points, proves the stated Holder or Lipschitz regularity. All derivatives of order strictly below p extend by zero at the vertex. If p is noninteger, a stronger Holder density bound would contradict the nonzero limit r^(-p)v(-r,rz)=phi_(e_i)(z) on a suitable fixed ray. If p is integer, C^p would make that limit a homogeneous polynomial of degree p restricted to the ray. The germ begins with z^(m_i), where m_i>p, so it cannot be that polynomial. This proves the regularity assertions, including the source jets and their precise limitations.

## Dependencies and scope

The construction generalizes the single-seed theorem in ../higher-source-cone/PROOF.md; the recurrence and estimates are given again here with all multiindex factors. It uses only local equations. The choice of zero axis velocity is part of the construction. Adding an arbitrary harmonic velocity need not preserve transport and is not an extra coupled freedom.

A family of solutions of the full-plane admissible problem would also have to extend around the entire source, obey the canonical velocity prescription, reach a normalized smooth center with the required c_l identity, and have the prescribed global growth. None of those matching conditions is imposed here. Thus even arbitrarily many local source parameters do not settle the global family question or either endpoint. The theorem shows precisely that transport and div-curl coupling restricted to a left cone do not remove these finite local parameters.
