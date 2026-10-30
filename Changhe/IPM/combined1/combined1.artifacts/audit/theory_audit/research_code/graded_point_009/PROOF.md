# Independent uniform graded point audit

## Exact statement

Fix c=4076476460239181/2251799813685248 and the exact candidate C1-N1-009-d2w-j7-x3balk. Let h be a fixed-c stationary correction and set g=J^s h for s>0. Suppose

    ||omega D²g||2<=r2, ||Dg||2<=r1, ||g||2<=r0, omega>=1,
    n²=r2²+2r1²+r0²,
    1/2-4708s-(217/50+(1049/5)s)n/sqrt(s)>0.

Then the necessary point inequality below is violated at X=(1/10,73/100). Therefore this candidate admits no exact correction in any original graded or gradedL2 box with that top margin. This does not cover a changed top margin or scaling parameter.

## Point estimate and elimination of all radii

The Fourier identity (1+|xi|²)²=1+2|xi|²+sum_ij xi_i²xi_j² implies ||h||H^(2+s)<=n. The audited point estimate, obtained by subtracting the stationary equations, is

    |F(X)|<=C1(s)n|V(X)|+C0(s)n(1+|D rho(X)|)+C0(s)C1(s)n²,
    C0(s)=[4pi(1+s)]^-1/2, C1(s)=[8pi s(1+s)]^-1/2.

The velocity Fourier multiplier has Euclidean magnitude at most1, which gives the same C0 bound for U[h]. The H^(2+s) embedding gives continuous first derivatives, so evaluating the equation at X is justified. The exact point fields were independently computed in the present exact-generator point reproduction.

Dropping the nonnegative (1049/5)s term in the top margin gives

    n/sqrt(s)<25/217,
    n<(50/217)(sqrt(s)/2-4708 s^(3/2)).

The latter cubic in sqrt(s) has maximum50/(651 sqrt(28248)). Put

    b0=50/(651 sqrt(28248) sqrt(4pi)), b1=25/(217 sqrt(8pi)).

Since 1+s>1, C0n<b0 and C1n<b1. Consequently every such correction must satisfy

    |F(X)|<=b1|V(X)|+b0(1+|D rho(X)|)+b0b1.

The checker reconstructs V and D rho from independently stored Cartesian components, rather than using the peer's stored norms, evaluates this bound outward and compares all peer values. The positive gap excludes every radius and every s covered by the displayed top margin.

## Finite scalar and graded boxes

For each separately specified finite box, use its exact s and n or an upper bound for ||h||H^(2+s), and evaluate the original point inequality directly. The sharp and sharpw energy norms dominate H^(2+s), since their component weights exceed1 and2 as needed. This gives independent tests of the two sharper scalar balls and three finite graded instances.

All inputs, their hashes, exact radii and outward intervals are retained with the results. The comparison uses a necessary condition only and claims no inverse or existence theorem. Dependencies are the audited point estimate in residual_witness/PROOF.md, graded_budget_audit/PROOF.md, and the present exact-generator point reproduction's exact candidate point data.
