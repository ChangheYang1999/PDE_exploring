# Actual coupled source solutions of any odd initial order on a cone

Date: 2026-10-20. Status: complete informal argument written before the checks. Independent coefficient checks and actual lead Opus review are pending. This is a theorem on a left cone, with no claim about a full source neighborhood or the global admissible class.

## Statement

Let A>1, g>0, and let m>=3 be odd. Set

    q=(m-1)/A, p=m-q=1+(m-1)(1-1/A)>1,
    b=g/[2(A-1)]>0.

Choose a nonzero real C, and 0<kappa<1/sqrt(1+b). There exist R>0 and real fields v,V=(V_1,V_2) on

    Omega={s=-r<0, |y|<kappa r, 0<r<R}

satisfying

    (A s partial_s+y partial_y-1)v+g V_2+V.grad v=0,
    div V=0, partial_s V_2-partial_y V_1=-v_s.              (1)

The density v and V_2 are odd in y, while V_1 is even. All fields are real analytic in Omega and vanish with their first derivatives at the vertex. Put f=g y+v and W=(A s,y)+V. Then W.grad f=f, div W=A+1 and curl W=-f_s, with source jet DW(0)=diag(A,1) and f_y(0)=g.

For G_j(-r)=partial_y^j v(-r,0)/j!, the following identities hold exactly at every open axis point:

    V(-r,0)=0, G_j(-r)=0 for odd j<m,
    G_m(-r)=C r^(-q),
    G_(m+2)(-r)=-b q(q+1)C r^(-q-2)/[(m+1)(m+2)].        (2)

In particular r^q G_m=C is nonzero. If C>0, the next naturally scaled coefficient r^((m+1)/A)G_(m+2) tends to negative infinity.

Let p=k+alpha with k an integer and 0<alpha<1, if p is not an integer. On every smaller closed cone and sufficiently small closed radial interval the fields are C^(k,alpha) up to the vertex. The density is not C^(k,beta) there for any beta>alpha with beta<=1. If p is an integer, the fields are C^(p-1,1) up to the vertex and the density is not C^p. Regularity here means the continuous extension of derivatives from the cone, with the indicated Holder bounds. No equation or regularity outside this cone is asserted.

Explicit sufficient convergence constants are

    B=kappa^2/(1-kappa^2),
    a_bar=|C| kappa^m/[1-max(1,b) kappa^2],
    K=(2m+1)kappa/[(A-1)(1-kappa^2)(1-bB)].

Any R with 4 K a_bar R^(p-1)<1 suffices. These are conservative bounds, not sharp radii.

## 1. The analytic linear germ

For a radial power r^h and z=y/r, write a prospective linear triple as r^h(phi(z),alpha(z),beta(z)). The frozen transport, divergence and curl equations with density forcing r^h H(z) are equivalent to

    (Ah-1)phi+(1-A)z phi'+g beta=H,
    beta'=h alpha-z alpha',
    -h beta+z beta'-alpha'=h phi-z phi'.                   (3)

The signs follow from partial_s[r^h phi(y/r)]=-r^(h-1)(h phi-z phi'). Expand phi,beta,H in odd powers and alpha in even powers, and fix alpha_0=beta_1=0. For each odd j,

    c_j(h)phi_j+g beta_j=H_j,
    c_j(h)=Ah-1-(A-1)j,
    beta_(j+2)=-(h-j)(h-j-1)(beta_j+phi_j)/[(j+1)(j+2)],
    alpha_(j+1)=(j-h)(beta_j+phi_j)/(j+1).                (4)

These equations are derived directly by coefficient comparison in (3); conversely they give all coefficients of (3).

Take h=p and H=0. The unique odd resonance is j=m. Set all lower coefficients to zero and set phi_m=C. The recurrence then gives

    phi_0(z)=C sum_(l>=0) (-1)^l (b)_l(q)_(2l)m!
                          z^(m+2l)/[l!(m+2l)!].          (5)

The notation (a)_l is the rising factorial, including (a)_0=1. To check the formula, at j=m+2l with l>=1 transport gives phi_j=(b/l)beta_j. Substitution into the second equation of (4) gives the ratio of consecutive coefficients in (5). The absolute ratio tends to one, so the radius of convergence is one. Formula (5) and the recurrence define the velocity germ analytically in |z|<1. They also give

    alpha_(m+1)=q C/(m+1),
    beta_(m+2)=-q(q+1)C/[(m+1)(m+2)].                    (6)

The first two nonzero density coefficients are those in (2). This step is local: it uses neither a Fourier inverse nor data on the other side of s=0. In particular no canonical full-plane interpretation of this chosen linear germ is required for the theorem.

## 2. Uniform inversion above each resonance

For n>=0 set

    p_n=1+(n+1)(p-1),
    J_n=m+n(m-1), M_n=m+n(m+1).

Then c_j(p_n)=(A-1)(J_n-j). For n>=1, the resonant index J_n lies strictly below M_n, with gap M_n-J_n=2n. If H starts at angular order M_n, set every density coefficient below M_n, including the free coefficient at J_n, to zero. The compatibility equation at J_n is 0=0. Recurrence (4) then uniquely constructs a formal triple with

    phi=O(z^M_n), alpha=O(z^(M_n+1)), beta=O(z^(M_n+2)).   (7)

The estimates below prove convergence of this formal inverse. Use the absolute coefficient norms

    ||u||=sum_j |u_j| kappa^j,
    ||H||_-1=sum_(odd j>=1) |H_j| kappa^j/j.

For every j>=M_n, 0<p_n<j. Consequently both |j-p_n|/(j+1) and (j-p_n)(j+1-p_n)/[(j+1)(j+2)] are less than one. From the last two recurrences in (4), first for finite coefficient sums and then by monotone convergence,

    ||beta|| <= kappa^2(||beta||+||phi||),
    ||alpha|| <= kappa(||beta||+||phi||).

It follows that

    ||beta|| <= B ||phi||,
    ||alpha|| <= kappa/(1-kappa^2) ||phi||.               (8)

To justify the limiting step without assuming convergence, apply these inequalities to the coefficients through a common finite index. All recurrences use only earlier coefficients; including the last generated beta coefficient can only enlarge the right side. The following transport bound then bounds every finite density sum uniformly.

For n>=1 and j>=M_n,

    1/(j-J_n)<=1/(2n)<=1/2,
    j/(j-J_n)<=M_n/(2n)<=(2m+1)/2.

The first equation in (4) gives

    ||phi|| <= (2m+1)/[2(A-1)] ||H||_-1+b||beta||
             <= L ||H||_-1,
    L=(2m+1)/[2(A-1)(1-bB)].                             (9)

The denominator is positive by the choice of kappa. Thus all finite sums are uniformly bounded and (7) converges absolutely at kappa. Differentiation on smaller disks gives (3). The bounds (8) apply to the n=0 germ too because p<m and its coefficients start at m.

For the initial density, the successive terms in its absolute norm have ratio

    kappa^2 (l+b)/(l+1)
       * (q+2l)(q+2l+1)/[(m+2l+1)(m+2l+2)]
       <=kappa^2 max(1,b)<1.

This proves a_0=||phi_0||<=a_bar. Notice q<m-1<m, as A>1. All denominators in these bounds are strictly positive.

## 3. The nonlinear construction and convergence

Inductively let (phi_n,alpha_n,beta_n) solve (3) with h=p_n and forcing

    H_n=sum_(i+j=n-1)
          [alpha_i(p_j phi_j-z phi_j')-beta_i phi_j']     (10)

for n>=1; n=0 is the germ (5). The radial degree of each product in (10) is p_i+p_j-1=p_n. The lowest possible angular degree in either product is M_i+M_j+1=M_n. Induction therefore proves (7) at every n. It is a lower bound on the order, not an assertion that the first allowed coefficient is always nonzero. In particular, every resonance remains unforced and is consistently set to zero.

Write a_n=||phi_n||. A density monomial in phi_j has index l>=M_j>p_j. In the alpha product of (10) its output index t is at least l, so |p_j-l|/t<=1. In the beta product the output index is the beta index plus l-1, again at least l, so l/t<=1. Taking absolute coefficient convolutions and using (8) gives

    ||H_n||_-1 <= [kappa/(1-kappa^2)+B/kappa]
                          sum_(i+j=n-1) a_i a_j
                =2kappa/(1-kappa^2) sum_(i+j=n-1) a_i a_j.

This deals with the radial derivative p_j at the same time as the angular derivative; no unbounded factor in j is discarded. Combining this estimate with (9) yields

    a_n<=K sum_(i+j=n-1) a_i a_j,
    a_n<=Catalan_n K^n a_0^(n+1)<=4^n K^n a_0^(n+1).     (11)

Now define

    v=sum_(n>=0) r^p_n phi_n(y/r),
    V=sum_(n>=0) r^p_n (alpha_n(y/r),beta_n(y/r)).          (12)

Since p_n=p+n(p-1), (11) proves absolute normal convergence in Omega whenever 4 K a_bar R^(p-1)<1. On smaller angular disks all angular derivatives converge by the coefficient norm and a geometric margin. On compact subintervals of 0<r<R, every radial derivative costs at most a polynomial in n times a fixed negative power of r, which is also absorbed by the geometric margin. Hence (12) is real analytic, may be differentiated termwise, and its products may be formed by absolutely convergent series. Equations (3) and (10) prove (1) exactly.

The angular orders for n>=1 are at least M_1=2m+1>m+2. Thus every nonlinear correction has zero axis density derivatives through order m+2 and vanishes on the axis as a velocity. Convergence near each axis point proves the exact identities (2), not merely asymptotic versions.

As an algebraic check, (6) gives the coefficient of z^(2m+1) in H_1 as

    q(m-2q)C^2/[(m+1)(m+2)].

Since c_(2m+1)(p_1)=-2(A-1), the first allowed correction coefficient is

    (phi_1)_(2m+1)=-q(m-2q)C^2/[2(A-1)(m+1)(m+2)].       (13)

It vanishes when q=m/2. The proof does not require its nonvanishing, and still applies in that case.

## 4. Regularity and its exact scope

Fix a smaller closed cone |y|<=kappa' r with kappa'<kappa and R'<R. Differentiating the uniformly convergent series, for every integer h>=0 there is a constant C_h with

    |D^h(v,V)|<=C_h r^(p-h), 0<r<=R'.                    (14)

All derivatives of integer order less than p therefore extend by zero to the vertex. If p=k+alpha is noninteger, (14) at orders k and k+1 proves the alpha-Holder bound for D^k. For points separated by at least half the smaller radius, each radius is bounded by a constant times their separation and the size bound suffices. Otherwise the line segment lies in the convex cone at comparable radius; integration of the next derivative gives |X-Y| r^(alpha-1)<=constant |X-Y|^alpha. If p is an integer, the bounded derivative of order p similarly proves the Lipschitz bound for D^(p-1). Lower derivatives have the asserted continuous extensions. This proves the positive regularity statements for v and V. The linear pieces in f and W preserve that regularity and give the stated source jet.

To see the asserted failure of stronger density regularity, choose a fixed nonzero z inside the smaller cone with phi_0(z)!=0, possible because its leading coefficient C is nonzero. Along this ray,

    r^(-p)v(-r,rz) -> phi_0(z).

For noninteger p, all derivatives through order k vanish at the vertex. A C^(k,beta) extension on the cone with beta>alpha would give the Taylor remainder bound v=O(r^(k+beta)), a contradiction. This Taylor bound follows along the segment from the vertex and only requires the regularity on the closed cone. For integer p, a C^p extension would instead give a homogeneous polynomial of degree p as the limit r^(-p)v(-r,rz). Its restriction is a polynomial in z of degree at most p. But phi_0 is analytic and starts with the nonzero power z^m, where m>p, so it cannot be that polynomial. Thus the density is not C^p up to the cone vertex.

For m=5 and 4/3<A<2, p=5-4/A lies strictly between two and three. The construction has C^(2,3-4/A) regularity and nonzero fifth scaled trace, with every lower odd density trace zero. At A=2 it has C^(2,1) but not C^3 regularity. For A>2 it is smoother according to p, while the fifth scaled trace stays nonzero. These statements concern a cone and do not assert sharpness for a theorem whose hypotheses hold on a full neighborhood of the source. For A<=4/3 the m=5 construction is not C^(2,alpha) and therefore supplies no counterexample in that class.

## Dependencies and limitations

This proof uses only coefficient comparison, absolutely convergent power series, a uniform inverse estimate, the Catalan recurrence and elementary Holder estimates. Its recurrence agrees with the independently derived one in ../source-formal/PROOF.md. It generalizes sections2-3 of ../third-source-cone/PROOF.md and does not use that file's Fourier distribution construction.

The cone does not contain any point (0,y) with y!=0. The construction supplies neither extension across that line nor data near it, and does not impose the canonical full-plane inverse on V. It does not match the normalized center of an IPM profile, the coefficient relation fixing c_l, or a sublinear far field. It proves no existence or nonexistence endpoint for TASK.md, and does not contradict source results with stronger growth or full-neighborhood hypotheses.
