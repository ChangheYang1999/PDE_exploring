# A nonlinear energy bound for Q(g)=||WJ^q g||₂

Status: proved analytic estimate at q=21/10. The unweighted principal/core estimate is reproduced and verified in the [fresh operator review](../operator_theory/NONLINEAR_CORE_AND_Q_REVIEW_v01.md), the completed [3210-interval scalar certificate](../operator_theory/nonlinear_core_scalar_result.json), and the [independent coordinator replay](../ROOT_NONLINEAR_CORE_REPLAY.json). It does not depend on a missing inherited audit. The remaining estimates below are explicit Fourier/product arguments; linear background coercivity and stationary existence are separate obligations.

Let W²=1+4|X|², q=21/10, theta=(q-2)/q. Define the scalar Wiener interpolation constants Bp by
\[
B_p=(4q\sin(\pi s))^{-1/2}(1-s)^{-(1-s)/2}s^{-s/2},\quad s=(p+1)/q,
\]
for p=0,1. Set Cs=B1/4, Ca=B0/sqrt2,
\[
S_1=[2\sqrt{\pi(q-1)(q-2)}]^{-1}.
\]
The distinction is that B0 controls a general scalar test's Wiener norm, while Ca controls U[k] using its angular multiplier.

Assume real S1 k has ||k||₂<=R and Q(k)<=M. For a real test g with ||g||₂<=R and G=Q(g)>=M, define
\[
r=R/M,\quad z=q r^{1/q},\quad v=C_a M r^{1-1/q},
\]
\[
L_0=qC_sR^\theta M^{1-\theta}+\frac{53}{100}S_1M,
\quad C_c=q2^{q-2}\left(B_1R^\theta M^{1-\theta}+S_1M\right),
\]
\[
P=2^{q-1}(C_a+B_0)M r^{1-1/q},\qquad
T=q2^{q-2}(C_a+B_1)M r^{1-1/q}.
\]
Then the nonlinear frozen-drift energy satisfies
\[
\boxed{
|\Re\langle WJ^q(U[k]\cdot\nabla g),WJ^qg\rangle|
\le L_Q(R,M)G²,
}
\]
\[
\boxed{L_Q=L_0(1+2z)²+4C_c(1/2+z)z+2(qv+P+T).}
\]
The hypothesis G>=M is deliberate. The [forced-evolution bridge](../operator_theory/Q_FORCED_EVOLUTION_BRIDGE_v02.md) applies this estimate to trajectories on the exterior of the ball before inferring high regularity of the stationary inverse. The bound ||D^q k||₂<=M follows directly from the stipulated coefficient Q ball.

## Proof

Put a=U[k], f=J^qg, Xj=xj f,
\[
Z_j=[x_j,J^q]g=q\partial_jJ^{q-2}g,\qquad
Y_j=J^q(x_jg)=X_j-Z_j.
\]
Write X²=sum||Xj||₂² and Z²=sum||Zj||₂², so G²=||f||₂²+4X² and
\[
X\le G/2,\quad Z\le q\|J^{q-1}g\|₂\le qR^{1/q}G^{1-1/q},\quad
\Big(\sum_{ij}\|\partial_iZ_j\|₂²\Big)^{1/2}\le qG.
\]
All commutator signs follow from the unitary Fourier convention: [xj,Jq]=q partial_j J^(q-2).

The exact identity
\[
x_jJ^q(a\cdot\nabla g)
=a\cdot\nabla X_j-a\cdot\nabla Z_j+[J^q,a\cdot\nabla](x_jg)
-J^q(a_jg)+[x_j,J^q](a\cdot\nabla g)
\]
follows by commuting xj and using xj(a·grad g)=a·grad(xjg)-ajg. The direct transport terms pair to zero with f and Xj because div a=0.

The freshly proved unweighted principal/core bound cited above, whose proof imposes no symmetry on the test, gives
\[
|\Re\langle[J^q,a\cdot\nabla]h,J^qh\rangle|\le L_0\|J^qh\|₂².
\]
Here the coefficient k remains S1; the tests xjg may have other parity. The coefficient bound uses ||Dq k||₂<=||Jq k||₂<=Q(k)<=M.

A separate operator estimate, used only in a lower-order cross term, is
\[
\|[J^q,a\cdot\nabla]h\|₂\le C_c\|J^qh\|₂.
\]
Indeed
\[
|\langle s\rangle^q-\langle r\rangle^q|
\le q2^{q-2}|p|(\langle r\rangle^{q-1}+|p|^{q-1}),\qquad p=s-r.
\]
Young's inequality and Fourier Cauchy-Schwarz give the stated bound from
||Da||A<=B1 R^theta M^(1-theta), ||Dq a||₂<=M and ||grad h||A<=S1||Jq h||₂.

Splitting each commutator pairing against Xj=Yj+Zj gives
\[
\begin{aligned}
|E_Q|\le{}&L_0(\|f\|₂²+4\sum_j\|Y_j\|₂²)
+4C_c\left(\sum_j\|Y_j\|₂²\right)^{1/2}Z\\
&+4X\left[q\|a\|_\infty G+\|J^q(ag)\|₂
+q\|J^{q-1}(a\cdot\nabla g)\|₂\right].
\end{aligned}
\]
Since Y<=X+Z, the first two terms are bounded by L0(G+2Z)²+4Cc(G/2+Z)Z.

For the last two products, the elementary inequality
\(\langle r+p\rangle^s\le2^{s-1}(\langle r\rangle^s+\langle p\rangle^s)\), s>=1, yields
\[
\|J^q(ag)\|₂\le2^{q-1}(\|a\|_A\|J^qg\|₂+\|J^qa\|₂\|g\|_A),
\]
\[
q\|J^{q-1}(a\cdot\nabla g)\|₂
\le q2^{q-2}(\|a\|_A\|J^qg\|₂+\|J^{q-1}a\|₂\|\nabla g\|_A).
\]
Use
\[
\|a\|_A\le C_a R^{1-1/q}M^{1/q},\quad
\|g\|_A\le B_0R^{1-1/q}G^{1/q},
\]
\[
\|J^qa\|₂\le M,\quad
\|J^{q-1}a\|₂\le R^{1/q}M^{1-1/q},\quad
\|\nabla g\|_A\le B_1R^\theta G^{1-\theta}.
\]
Dividing by G and using G>=M gives P and T exactly; note 1/q+theta=1-1/q. Also ||a||infty<=v, Z/G<=z. Substitution proves the boxed LQ bound. The identities first hold for smooth tests; all final terms are continuous in the indicated weighted graph norm and extend by density.

## Numerical comparison

At the inherited safe R=4.549261e-7 and M=.387, the companion Arb program encloses LQ below.293151. The older N-norm/CE loss upper was.3651689966. This comparison supplies no linear coercivity; it is an improvement in a newly proved nonlinear bound under the changed norm.
