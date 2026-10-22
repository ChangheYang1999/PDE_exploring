# Logarithmic centre quasimodes in the weighted factor supremum norm

This proof is written before its algebra checks. Status OPEN pending independent review. It concerns a failure of an inverse estimate, not existence or exclusion near X3.

## Exact statement and hypotheses

Fix L>0, 0<k<1, ell in R, and W(r)=(1+r^2/L^2)^((k-3)/2). Let a background rho=x^2 y a have the density parities, canonical full-plane velocity U, and a(0)=1. Assume:

1. a is continuous everywhere and C1 off the origin, with finite constants A0=sup |a|/W and A1=sup r|grad a|/W.
2. U has the velocity parities, U is C1 locally, U(0)=0, and, for some alpha>0 and H<infinity, ||DU(X)-diag(-c,c)||<=H r^alpha for r<=1, where c=3ell-1. Increasing H permits replacing the unit disk by any fixed sufficiently small disk and rescaling the construction below.
3. The canonical inverse exists for the background. For the smooth compact corrections used below it is the Green inverse of -Delta psi=partial_x h, with U[h]=(-psi_y,psi_x).

Write Sigma(h)=psi[h]_xy(0), G=X.grad rho, and

 Lh=(ell X+U).grad h-h+U[h].grad rho+(Sigma(h)/3)G.

Here Lh denotes the operator, whereas the positive constant L in W is the length scale. Set p=x^2 y and

 ||h||F=sup_(xy!=0) |h(X)|/(|p(X)|W(r)).

On corrections with continuous factor this agrees with the supremum of that factor on the whole plane. Define the Banach space B by h=p W b, where b is real, continuous, tends to zero at infinity, is even in both coordinates, and b(0)=0. Its norm is ||h||F=||b||infinity. Multiplication by p W is injective on continuous b because its nonzero set is dense. No canonical velocity or bounded operator L is asserted on all of B.

There are smooth compactly supported corrections z_j in B, vanishing on a neighborhood of the origin, with the prescribed density parity and Sigma(z_j)=0, such that

 ||z_j||F=1,  ||Lz_j||F -> 0,  z_j -> 0 weakly in B.

Every Lz_j belongs to B. Thus no finite constant K gives ||h||F<=K||Lh||F on a test class containing this sequence. No estimate ||h||F<=C||Lh||F+||Th||Z holds there with T:B->Z bounded, linear and compact, and Z a Banach space. No closed linear Fredholm realization of L in B can have a domain containing all z_j. All these statements are conditional on the stated background hypotheses. They do not cover Holder or derivative norms of the factor, a stronger domain norm, a weaker target, or a different normalization selection which excludes the sequence.

The exactly joined canonical modal trial satisfies the hypotheses, as justified below. The result is not an exclusion of an exact profile and gives no decisive endpoint.

## Two explicit Green modes for radial cubic cutoffs

Let chi be smooth, supported in an annulus contained in 0<r<=delta<=1, with |chi|<=1, and set h=p chi(r). Since p=r^3(sin theta+sin 3theta)/4, direct Cartesian differentiation gives only two forcing modes:

 partial_x h=f_1(r)sin 2theta+f_2(r)sin 4theta,
 f_1=r^2 chi+(r^3/4)chi_r,  f_2=(r^3/8)chi_r.

Put I5(r)=integral_0^r s^5 chi(s)ds, I7(r)=integral_0^r s^7 chi(s)ds, and J1(r)=integral_r^infinity s chi(s)ds. Substitution in the canonical Green formula and integration by parts give

 psi_2(r)=(r^2 J1-r^-2 I5)/8,
 psi_4(r)=-r^-4 I7/8.                              (1)

These are the coefficients of sin 2theta and sin 4theta, respectively. Every boundary term at zero and infinity vanishes because chi has annular compact support. These modes are regular at zero and decay outside the support except for the regular interior harmonic mode. In particular there is no added arbitrary affine strain, and

 Sigma(h)=(1/4)integral_0^infinity s chi(s)ds.        (2)

For 0<=chi<=1 this lies in [0,delta^2/8].

Let D=r partial_r and B1=||D chi||infinity. The three primitive bounds, valid for all r>0, are

 |J1|<=delta^2/2,
 r^-4 |I5|<=delta^2/6,
 r^-6 |I7|<=delta^2/8,
 r^2 |chi|<=delta^2,  r^2 |D chi|<=delta^2 B1.

For example use |I5|<=min(r,delta)^6/6 and split r<=delta and r>=delta. Differentiating the exact formulas (1), with D I5=r^6 chi, D I7=r^8 chi and D J1=-r^2 chi, therefore gives the following bounds divided by delta^2:

| Mode m | |psi_m|/r^2 | |D psi_m|/r^2 | |D^2 psi_m|/r^2 |
| --- | --- | --- | --- |
| 2 | 1/12 | 5/12 | 4/3+B1/4 |
| 4 | 1/64 | 3/16 | 1/4+B1/8 |

Each entry is multiplied by delta^2. In an orthonormal polar frame the Hessian of psi_m(r)sin(mtheta) has entries

 (D^2 psi_m-D psi_m)sin(mtheta)/r^2,
 m(D psi_m-psi_m)cos(mtheta)/r^2,
 (D psi_m-m^2 psi_m)sin(mtheta)/r^2.

The operator norm is bounded by the sum of the two diagonal absolute values and twice the off-diagonal absolute value. Summing over m=2,4 yields

 ||DU[h]||infinity <= (7+3 B1/8)delta^2.            (3)

This uses explicit finite modes, not boundedness of a singular integral on arbitrary factor-supremum data. Formula (3) also holds on the axes and at zero by continuity. Velocity parity and the fundamental theorem of calculus imply

 |U[h]_1/x|<=||DU[h]||infinity,
 |U[h]_2/y|<=||DU[h]||infinity,
 |U[h](X)|<=r||DU[h]||infinity.                    (4)

Axis quotients mean their continuous extensions.

## Slowly varying annuli

Choose beta in C_c^infinity((0,1)) with 0<=beta<=1 and max beta=1. Write B=||beta'||infinity. For integers n>=1 set

 chi_n(r)=beta((-log r-n)/n),  h_n=p chi_n,
 delta_n=exp(-n).

Extend chi_n by zero at r=0. It is smooth, vanishes near zero and outside the annulus exp(-2n)<r<exp(-n), and ||D chi_n||infinity<=B/n. Each h_n is globally smooth, including on both axes. Since W tends to1 at zero,

 ||h_n||F -> 1.                                   (5)

Indeed the factor is chi_n/W on its support, its supremum is at least1, and at most1/W(delta_n), which tends to1.

Let V0=diag(ell-c,ell+c)X and R=U-diag(-c,c)X. Normalization gives V0.grad p=(3ell-c)p=p. Therefore

 (V0.grad-1)(p chi_n)=p(D chi_n)(V0.X/r^2).

With Mv=max(|ell-c|,|ell+c|), its factor norm is at most Mv B/[n W(1)]. The C1 center bound and parity imply |R1/x|,|R2/y|<=H delta_n^alpha on the support; also |R|/r<=H delta_n^alpha. Consequently

 ||R.grad h_n||F <= H delta_n^alpha(3+B/n)/W(1).    (6)

All constants are independent of n. This calculation does not divide an arbitrary vector bound by x or y: the component quotient bounds follow by integrating the appropriate derivative from the symmetry axis.

Put CA=3A0+A1. The exact identity

 U[h].grad rho/p=(2U[h]_1/x+U[h]_2/y)a+U[h].grad a

and (4) give ||U[h].grad rho||F<=CA||DU[h]||infinity. Also ||G||F<=CA. Equations (2)-(6) prove the explicit estimate

 ||Lh_n||F <= Mv B/[n W(1)]
   +H exp(-alpha n)(3+B/n)/W(1)
   +CA exp(-2n)(7+3B/(8n)+1/24).                   (7)

Thus the image tends to zero. The smallness of the nonlocal term comes from this particular shrinking smooth sequence, not from any global operator bound in ||.||F.

## Exact strain cancellation and weak convergence

Choose a fixed nonzero nonnegative smooth radial zeta supported in 1<r<2, and put q=p zeta. Its strain s0=(1/4)integral r zeta(r)dr is strictly positive by (2). Both q and Lq have finite factor norm. Define

 a_n=Sigma(h_n)/s0,  w_n=h_n-a_n q.

Then 0<=a_n<=exp(-2n)/(8s0), Sigma(w_n)=0, and w_n vanishes near zero and is compactly supported. Linearity and (5)-(7) show

 ||w_n||F -> 1,  ||Lw_n||F -> 0.

The latter claim uses only the fixed finite number ||Lq||F. This finiteness follows from (1)-(4), with the fixed support radius 2 in place of delta, the background factor bounds, and compact support for the transport part. The rank-one part of Lq need not have factor tending to zero at infinity. No membership Lq in B, or center limit for its factor under these hypotheses, is asserted. For w_n the rank-one term is exactly absent. Thus it is Lw_n, rather than necessarily Lq, which is asserted to lie in B.

For w_n the transport part is compactly supported. Outside the compact support its stream function is a fixed linear combination of r^-2 sin(2theta) and r^-4 sin(4theta), by (1). Cartesian differentiation, or the explicit formulas sin(2theta)=2xy/r^2 and sin(4theta)=4xy(x^2-y^2)/r^4, gives U[w_n]=O(r^-3) and the continuous axis quotients U[w_n]_1/x,U[w_n]_2/y=O(r^-4), uniformly in angle. The background factor-gradient bound therefore gives (U[w_n].grad rho)/(p W)=O(r^-4). Thus Lw_n has factor tending to zero at infinity. Its factor extends continuously across the axes because each radial-cutoff velocity is smooth with the required parity and a is C1 away from zero. Near zero, each w_n is zero and Sigma(w_n)=0. The explicit formulas show that its stream function there is zero, so Lw_n is also zero on a sufficiently small disk. These facts establish Lw_n in B.

Pass to n_j=3^j. The small annuli supporting h_(n_j) are pairwise disjoint. For every finite set of signs epsilon_j in {-1,1},

 ||sum_j epsilon_j h_(n_j)||F <= 1/W(1).

If lambda is any continuous real linear functional on B, choose epsilon_j to be the sign of lambda(h_(n_j)). This gives sum_j |lambda(h_(n_j))|<=||lambda||/W(1), for every finite initial sum. Hence lambda(h_(n_j)) tends to zero. Since a_(n_j)q tends to zero in norm, w_(n_j) tends to zero weakly. Normalize z_j=w_(n_j)/||w_(n_j)||F for all sufficiently large j. This proves the stated sequence. Center coefficient and far asymptotic coefficients vanish for every input, not just in the limit.

## Compact remainder and closed Fredholm consequences

A bounded linear compact operator T:B->Z maps this bounded weak-null sequence to a norm-null sequence. To prove this directly, every subsequence of Tz_j has a norm-convergent further subsequence by compactness; its weak limit must be zero because bounded linear maps preserve weak convergence. Thus the only possible norm-cluster limit is zero. The proposed compact-remainder estimate contradicts ||z_j||F=1.

Suppose a closed linear realization A:D(A) subset B->B agreeing with L on the z_j is Fredholm. Its graph domain is Banach, its kernel is finite dimensional, and its range is closed. The induced bijection from D(A)/ker A onto ran A has bounded inverse by the Banach open mapping theorem. In particular dist_B(z_j,ker A)<=C||Az_j||F tends to zero. Choose k_j in ker A at distances tending to zero. The k_j are bounded, so a subsequence converges in the finite-dimensional kernel to k. Then z_j converges in norm to k on this subsequence, while its weak limit is zero. Thus k=0, contradicting unit norm. No such Fredholm realization exists. This argument does not assume that L is bounded or defined on all of B, or that the realization is densely defined.

## Application and scope

The exactly joined, canonically normalized modal_v2 trial has ell=1/k and c=3/k-1 exactly. Its continuous factor is C1 off the origin. Near zero it is 1 plus finitely many r^(2l) trigonometric modes and higher positive-power logarithmic terms, so |a|+r|grad a| is bounded. At infinity it is a finite sum whose leading order is r^(k-3), with lower powers and exponentially decaying logarithmic join terms in log r; hence |a|+r|grad a|=O(W). On the compact annulus the exact joins and finite formula give finite bounds. Its canonical velocity is C1,alpha near zero for some alpha>0, by the previously accepted canonical regularity theorem, and symmetry and exact strain give its required linear part. These are qualitative consequences of the accepted exact trial definitions; no new numerical constant for A0,A1,H is asserted or needed. If its Hölder estimate is stated on a smaller disk, rescale the annuli by that fixed disk radius; (5)-(7) acquire fixed constants and all conclusions persist.

The factor supremum already fails to control arbitrary interior velocities, by factor_velocity/PROOF.md. The present result is different: even on an explicit smooth strain-zero test sequence with small canonical velocities, a same-factor-norm inverse estimate and a containing closed Fredholm realization fail. A two-norm iteration with a stronger low norm or a different image norm is not excluded. Neither P2 nor Pinfinity existence or nonexistence near X3 is decided. The inputs themselves are smooth, compact and have exact zero center coefficient, so merely imposing smooth center factors does not remove this norm obstruction.

## Dependencies and verification obligations

The canonical full-plane Green convention and exact modal background come from canonical_inverse, modal_repair, trial_regularities and canonical_residual_composition, with their actual accepted verdicts and mandatory addenda. The new identities are (1)-(7), the zero-strain correction and the elementary disjoint-support weak convergence argument. A complete actual Claude Opus5.5 proof review and independent later adjudication are required. Two exact methods will check the radial differentiation/Poisson identities, the cubic affine cancellation, and the rational coefficients in (3) and (7). These finite checks are not a proof of compactness or a substitute for the argument above. No numerical enclosure is proposed.
