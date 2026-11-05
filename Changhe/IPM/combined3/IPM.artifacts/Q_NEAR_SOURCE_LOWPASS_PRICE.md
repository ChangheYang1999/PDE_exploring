# A coefficient-aware Gaussian price for the near Q source

Status: proved operator estimate, independently checked for the parity-sensitive R1 step. Actual coefficient envelopes are produced separately. This controls the low/low block only; its near high/cross block is not certified here.

Let q=21/10, W=sqrt(1+4r²), G=WJqg, and P=exp(Delta/(2mu²)). Suppose g is real S1 (even in x, odd in y). Let b_N be a centrally even near-source coefficient, and let a be a nonnegative bounded radial envelope satisfying

|b_N(x)|<=a(r), sup a<=a0, sup r*a<=a1.

No derivatives of a are required. For m=2,3 and j=0,1,2 set
\[
A_m=\sup_\xi \langle\xi\rangle^m P(\xi),\quad
D_m=\sup_\xi|\nabla_\xi(\langle\xi\rangle^mP(\xi))|,\quad
B_j=\sup_\xi|\xi|^jP(\xi),
\]
\[
L_m=(A_m+2D_m)a_0+2A_m a_1.
\]
The coefficient-aware version of the interior adjoint proof gives
\[
\|aPWJ^qg\|_2\le C_b\|g\|_2,\qquad
C_b=N_2^{9/10}N_3^{1/10},
\]
where
\[
N_2=L_2+(4B_1+8B_0)a_0,\quad
N_3=L_3+(\sqrt8 A_2+24B_1+4B_2+40B_0)a_0.
\tag{1}
\]
Indeed the adjoint is Jq W P a. For v of norm one, exact coordinate commutation gives
||WJm P av||<=Lm, using ||av||<=a0 and ||xav||<=a1. The integer product bounds on W and spectral interpolation are exactly those in finite_rank/QNORM_INTERIOR_LOWPASS_PRICE.md. This avoids replacing a1 with the weaker product of support radius and a0.

## The one Riesz component required by the IPM matrix

For h odd in x and odd in y, its Fourier angular modes have nonzero even indices, so
\[
\|\widehat h/r\|_2\le\tfrac12\|\nabla\widehat h\|_2.
\]
Angular integration by parts gives the exact identity
\[
\|\nabla(\cos\theta\,\widehat h)\|_2²
=\int\cos²\theta|\nabla\widehat h|²+
\int\frac{\cos²\theta}{r²}|\widehat h|²
\le\frac54\|\nabla\widehat h\|_2².
\]
Thus ||WR1h||<=sqrt(5)/2 ||Wh|| on this parity subspace. Radial a, Jm, and P preserve it.

The output of aR1PWJq on S1 has exactly the odd-x/odd-y parity. Its adjoint therefore only requires the preceding weighted R1 bound on that output subspace. Repeating the integer product proof gives
\[
\|aR_1PWJ^qg\|_2\le C_R\|g\|_2,\qquad
C_R=\widetilde N_2^{9/10}\widetilde N_3^{1/10},
\tag{2}
\]
where \(\widetilde N_m\) is (1) with Lm replaced by sqrt(5)/2 Lm. All the other terms remain unchanged: they use only the unweighted norm of R1. This does not assert a negative-weight bound for a general single Riesz transform.

## The near source low block

Let
\[
K_N=\begin{pmatrix}-(b_N)_y&(b_N)_x/2\\(b_N)_x/2&0\end{pmatrix},
\quad
S_N(G)=\operatorname{Re}\langle b_N\cdot WUW^{-1}G,G\rangle
-\int(RG)^TK_N(RG).
\]
The velocity term on PG is bounded by sqrt(3)Cb||g||||PG||, using the symmetry-restricted weighted velocity norm. For the matrix term write X=R1PG, Y=R2PG. Pointwise,
\[
|-(b_N)_y X²+(b_N)_xXY|
\le |b_N||X|\sqrt{X²+Y²}.
\]
The vector Riesz isometry and (2) therefore give
\[
|S_N(PG)|\le(\sqrt3 C_b+C_R)\|g\|_2\|PG\|_2.
\]
For mu<=1, ||PG||<=||J^-1G|| exactly. Hence for every delta>0,
\[
\boxed{|S_N(PG)|\le
\delta\|J^{-1}G\|_2²+
\frac{(\sqrt3 C_b+C_R)²}{4\delta}\|g\|_2².}
\tag{3}
\]
The missing K22 entry is crucial: a general matrix would require pricing the parity component R2PG that can have angular mode zero. The proof does not make that invalid substitution.

The far high-pass source lemma and its certificate can be added to (3) only after the near high/cross source block, the transport terms, and every damping allocation have also been bounded.
