# Exterior radius bounds from the completed delta3/5 prefixes

Status: PROVED by the previously admitted finite-prefix theorem and the complete input, exact-box and separate replay checks, admitted inV462.

## Exact setting and inputs

Let delta=3/5, c=5/2, and f_1=sin(theta)+b sin(3theta), where b is one of the four exact real roots isolated in200. The uniquely tuned pure-power branch is the one in200 and208. Fix a multiple N of10, with N<=300. Assume the completed producer coefficients through N enclose this branch as proved in208, with artifact hypotheses verified there and independent Cartesian equation checks through300 in209. The provisional stream kernel at300 is never used.

Let s>0 be the all-index lower bound |sigma_k|>s from204 for the same root. Choose exact positive rational bounds d_j>=j||f_j||_1 for1<=j<=N and e_a>=10a|H_(10a)| for1<=a<N/10, obtained by outward rounding of the directed sums of the saved coefficient intervals. Retain the dyadic sum enclosures and the rounded rational bounds so that their inequalities can be checked again without a full high-order checkpoint.

## Majorant theorem and radius conclusion

Use the finite-prefix residue majorant of172, with h=3,Q=10,B=4 and

    L=75/29,
    kappa_N=16(N+1)/(3N).

Here L bounds the weighted particular stream inverse; the density and stream bandwidths are4j-1 and4j. The twenty nonnegative coordinates comprise nine next-block density responses, the unknown next harmonic series, and ten future density residue series. Their variable is w=z^10=r^(-6). The known polynomials consist precisely of the above d_j and e_a; no measured tail growth is inserted.

Let Phi(w,Y) be this polynomial map. Its value at zero is c+JY, with J strictly lower triangular and nonnegative. Thus T=(I-J)^(-1)=I+J+...+J^19 is nonnegative and Y0=Tc. Define

    G(w,Y)=Y0+T[Phi(w,Y)-Phi(0,Y)].

If a retained integer q>0 and a positive rational vector B0 satisfy the exact coordinate inequalities G(2^(-q),B0)<=B0, then iteration of G from zero has nonnegative coefficients and is bounded by B0 at this positive argument. Monotone convergence gives a finite majorant there. The comparison induction of172 bounds the exact tuned coefficients by its coefficients, using |sigma_k|>s when the harmonic is chosen. Therefore the infinite density and stream series converge absolutely and uniformly, after their prescribed radial weights, on every closed exterior

    r>=R>2^(q/6).

The common potential is the pure potential from202. Its inverse multipliers grow at most polynomially, and the finite angular bandwidth permits termwise differentiation of any fixed order after a strict radius margin. The potential, velocity, density and all appropriately weighted derivatives consequently converge uniformly there and solve the stationary exterior equation. For leading amplitude epsilon, replace R by R|epsilon|^(5/3).

This is the same proved theorem as205 with a longer certified prefix. Increasing N changes the known polynomial and kappa_N, not the underlying exact branch or its tuning rule. It need not improve a sufficient bound in every case.

## Verification and limitations

The calculation checks the all-index response receipt, producer artifact receipt, completed independent equation receipt, source hash and root index before using a checkpoint. It independently sums each density norm and extracts only already tuned harmonic entries. Every rounded bound is checked against its retained dyadic enclosure. The first three residue coefficients are compared with a separately indexed scalar recurrence. Candidate boxes may be proposed using ordinary floating arithmetic, but only exact rational inequalities admit a box. A second script reconstructs every admitted map from the saved rational inputs and recomputes its box image.

Failure of a proposed box proves no divergence or sharp lower radius. The conclusion is an exterior solution theorem; it does not give a global stationary extension. The canonical logarithmic branch for unit sine at2/3 is unrelated to these tuned3/5 branches.

## Completed finite-prefix certificates

All four roots pass the coefficient bounds and the exact boxes for N=60,100,150,200,300. The respective dyadic exponents q are138 at every N for root1;140 at N60 and139 at N>=100 for root2;134 at every N for root3;130 at every N for root4. Thus roots1 and2 improve the earlier sufficient radius exponents to23 and139/6. Roots3 and4 retain67/3 and65/3. The common sufficient exponent is139/6. All bounds carry the amplitude factor |epsilon|^(5/3), and none is an optimality claim.
