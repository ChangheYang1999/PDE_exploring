# Decay is essential in the condensed rotation-rate row

## 1. Claim and counterexample

Appendix A of the assembled c8963e47 report states "Rotation rate unique for a nonzero profile; trivial linear kernel at U = 0" with only H0 in its hypothesis column. H0 denotes U in C2 and P in C1 satisfying the global profile system, without the separately named decay H1. This enlarged claim is false.

Fix any 0<c<1/2 and set U=e3, P=-(1-c)x3. Then div U=0, DU=0, JU=0 and grad P=-(1-c)e3. Consequently

    (1-c)U+(cx-omega Jx+U).grad U+omega JU+grad P=0

for every real omega, with the very same nonzero U and pressure. The same constant vector and pressure also solve the linearized equation. Both functions are smooth. U does not tend to zero, so this counterexample concerns only the omitted hypothesis. It does not contradict the main report's correctly stated decaying theorem or the conjecture.

## 2. Correct rotation-rate theorem and proof

Let 0<c<1/2, U in C2(R3), div U=0 and U(x)->0 at infinity. Suppose U solves the full profile equations at distinct rates omega1,omega2 with C1 pressures P1,P2. Put L U=(Jx.grad)U-JU and q=(P1-P2)/(omega1-omega2). Subtraction gives grad q=L U and div L U=0. Thus q and grad q are harmonic, with their regularity understood distributionally first.

At a fixed x0, the mean-value formula and integration by parts give

    |grad q(x0)| <= (3|Jx0|/R) sup_(boundary B_R(x0)) |U|
                               +avg_(B_R(x0)) |U|.

Indeed Jx.n=Jx0.n on the sphere centered at x0. Boundedness makes the first term vanish as R tends to infinity, and decay makes the ball average vanish. Hence L U=0. Integrating the infinitesimal rotation action shows that U is axisymmetric in the vector sense. Both rotation terms cancel, so U solves the ordinary nonrotating equation. The independently confirmed nonrotating C1 sublinear theorem gives that U is constant; decay then gives U=0. No derivative decay or pressure normalization was assumed.

## 3. Correct linear theorem and proof

Let c>0, omega real, V in C2(R3), div V=0 and V(x)->0, with p in C1 solving

    (1-c)V+(cx-omega Jx).grad V+omega JV+grad p=0.

For W=curl V, taking curl gives W+(cx-omega Jx).grad W+omega JW=0. Along x(s)=exp(cs)R_(-omega s)x0,

    W(x(s))=exp(-s)R_(-omega s)W(x0).

As s tends to minus infinity, x(s) tends to zero where W is bounded. Therefore W(x0)=0. Div V=0 now makes each component of V harmonic; boundedness and decay imply V=0. This is a trivial kernel in the decaying class, not a normed inverse or spectral gap.

## 4. Exact repair and verification scope

Add H1 to the Appendix A hypothesis column and write "trivial decaying linear kernel". The rotation-rate range is 0<c<1/2; the separate linear statement holds for all c>0. Section 4 of the report already states decay and is unchanged. The old A046 proof was read completely and is pinned alongside the offending row. No computation is needed for the constant example or these short arguments.

This correction is necessary for the hypothesis column to mean the actual hypotheses used. It does not add a new hypothesis to the target problem, which already assumes decay. The main arbitrary-rotation nonexistence question remains OPEN.
