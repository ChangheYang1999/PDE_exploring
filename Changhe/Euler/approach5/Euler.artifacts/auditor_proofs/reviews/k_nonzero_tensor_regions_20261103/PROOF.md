# Positive stress on a fixed nonzero-k component

## 1. Statement and exact hypotheses

Fix 2/5 < c < 1/2 and omega real, and let x0 != 0 lie in an open subset G of R^3. Set A=cI-omega J, X=Ax, L=(1-c)I+omega J, a=1-2c, b=2-2c and q=b/a > 6. Suppose V,P are smooth on G, W=curl V, E=|V|^2, k=X.V, S=P-E/2, and

    div V=0, V.W=0, DV X=-LV, -Delta P=tr((DV)^2),
    grad k=X cross W-aV, X.grad S=-bS, W.grad S=0,
    k grad S=qS grad k on supp W.

Put M=V tensor V+P I and Q=P+E/2=S+E. For a component C of {W != 0, k != 0}, the last identity gives S=D_C|k|^q, with one finite constant D_C. This local theorem does not assume or establish existence of an actual global profile. The only imported rigidity input is the already confirmed C1 tensor lemma A1610, whose proof is recalled in Section 5.

The submitted conclusions about a fixed component, regular k zeros, irrotational pieces and necessary complement regions are confirmed below. A common flat point means that both V and S vanish to infinite value order there; smoothness then also gives flatness of k,E,P and M.

## 2. Both signs of the component constant

Suppose x0 is in closure C and V(x0)=0. On C, k != 0 forces E > 0, and

    |S| <= |D_C| |X|^q E^(q/2).

Because X is bounded locally and E tends to zero, for every 0 < epsilon < 1/2 a sufficiently small ball has |S| <= epsilon E on C. The eigenvalues of M are P on V-perp and P+E along V, with P=E/2+S. Hence

    (1/2-epsilon)E I <= M <= (3/2+epsilon)E I,

and its eigenvalue ratio is at most (3+2epsilon)/(1-2epsilon). Thus M is positive definite and -M is negative definite at every point of C near x0 for either sign of D_C. The ratio tends uniformly to 3 as x approaches x0 within C. No positivity on the complement of C follows.

At a point of supp W with k=0 and grad k != 0, the scalar rank relation directly gives S=0. Consequently P=E/2 there. This includes support points that are not in the open vortical set.

## 3. Irrotational decomposition and exact sphere mean

On an open set O where W=0, V=-grad k/a, Delta k=0 and DV is symmetric. Since Delta V=0,

    Delta(E/2)=|DV|_F^2, Delta P=-|DV|_F^2,
    Delta Q=0, Delta S=-2|DV|_F^2.

Also X.grad E=-bE, because V.JV=0, so X.grad Q=-bQ. The stress decomposition is

    M=(V tensor V-E I/2)+Q I,
    div(V tensor V-E I/2)=0.

For completeness, every smooth symmetric M with div div M=0 on a ball B_r(z) satisfies

    integral_B tr M = r integral_boundary n.Mn.             (1)

Indeed integrate div(M(x-z)); the extra volume term integral (x-z).div M is zero after integrating against the scalar (r^2-|x-z|^2)/2, which vanishes on the boundary and has gradient -(x-z). Its remaining volume term contains div div M=0. Here the Poisson and divergence equations give div div M=0 exactly.

On a closed ball contained in O, tr M=3Q-E/2, and harmonicity gives integral_B Q=(4pi r^3/3)Q(z). Dividing (1) by 4pi r^3 yields

    average_boundary n.Mn = Q(z) - integral_B E/(8pi r^3).   (2)

Thus the harmonic term Q is a real additional term. It is not set to zero by the local tail Poisson equation. No stationary momentum equation for the tail is presumed.

## 4. The complement regions forced by flatness

Suppose now x0 is a common flat point in closure C. For 0 < delta < 1/2 define Z_delta={P < delta E}. Then x0 belongs to closure Z_delta. To prove this, suppose P>=delta E on a ball about x0. Its stress M is positive semidefinite with eigenvalue ratio at most 1+1/delta, including points where E=0 and M=P I. It is flat, C1 and double-divergence free. Section 5 forces M=0 on that ball. Since P>=0, this gives E=0, contradicting the nonzero velocity points of C arbitrarily close to x0.

For every Dbar > 0 choose a smaller ball so

    Dbar sup_ball |X|^q E^(q/2-1) <= 1/2-delta

pointwise there. A point y in Z_delta in this ball must be one of the following:

- y is outside supp W, hence in int{W=0}; there Q<(1/2+delta)E.
- y is in supp W with k=grad k=0. A regular k-zero is impossible by Section 2.
- y is in supp W with k != 0 and D(y)=S(y)|k(y)|^(-q)<-Dbar.

For the last case E>0 and the strict pressure inequality gives

    |D(y)| > (1/2-delta)|X(y)|^(-q) E(y)^(1-q/2).          (3)

This contradicts |D(y)|<=Dbar under the chosen radius, and proves the assertion. Since E is flat, the right side grows faster than every inverse power of |y-x0| along such points. More precisely, for any N choose an integer L with L(q/2-1)>N and use E<=C_L |y-x0|^L in (3). This shows |D(y)||y-x0|^N tends to infinity. The claim concerns the ratio on support points; no finite number of component constants is assumed.

## 5. Recalled tensor rigidity and the gauge remark

For a positive semidefinite C1 symmetric tensor T with a uniform finite eigenvalue ratio, put A(r)=average_sphere n.Tn and B(r)=average_sphere(tr T-n.Tn). The equation div div T=0 and boundedness of div T at the center make its radial flux zero. Polar divergence then gives

    A'=[B-2A]/r <= K A/r

for a finite constant K>=0 fixed by the eigenvalue ratio. Therefore r^(-K)A is nonincreasing and A(r)>=(r/r1)^K A(r1) for r<r1. Infinite value flatness rules out A(r1)>0. Positivity and the eigenvalue comparison then force T=0 on the ball. This proof handles arbitrary zero sets and does not divide by A.

For f in C4, the tensor G_f=D2f-(Delta f)I has div div G_f=0. If F(r) is the spherical average of f, its normal mean is alpha=-2F'/r and its trace mean is r alpha'+3alpha. Thus adding G_f preserves the form of (1), though it generally changes its values. A flat gauge that itself satisfies the positive-semidefinite uniform-ratio hypotheses must be zero by the same lemma. If M+G_f meets those hypotheses and is flat, the conclusion is M=-G_f; this is not by itself a contradiction or a way to force V=0.

## 6. Scope and source comparison

All four source sections were read and the entire proof above was checked after writing. C55(a)-(d) are CONFIRMED with the exact local hypotheses. The sphere coefficient is 1/(8pi r^3); the signs of M and -M and both signs of D_C have been checked. No characteristic or far-field boundary term occurs in this local theorem, and no pressure gauge is changed.

The statement identifies necessary complement regions and gives no exclusion at a common flat point. A bound on the negative component constants, control of the irrotational harmonic Q, or a way to cross the critical set is still needed for such an exclusion. The full bare-decay problem is OPEN. No numerical computation or formal build was used. The existing Theory Agent C agent is configured model; provider runtime is not independently attested.
