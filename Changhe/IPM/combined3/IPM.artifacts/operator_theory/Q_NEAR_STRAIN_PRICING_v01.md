# Whole-plane near-strain pricing in the Q norm

Status: proved analytic inequalities with an executed Arb scalar certificate
`Q_near_strain_pricing_a2_v01.json`. The background input ||S||infty,op<=137/125
is inherited. This does not certify the other Q-norm remainders or existence.

Let q=21/10, W²=1+4r², G=WJ^qg, N=||G||2, R0=||g||2,
p=J^-1, m=|D|J^-1, n=1-m. Let psi_lambda=exp(-(|xi|/lambda)^4),
nu=1/40, a=chi(r/2)S and P=||pG||2. All vector Riesz multipliers are
jointly measured in their Euclidean output norm. The erflog chi is exactly
the inherited cut.

For mu=10 the actual constants proved here give
\[
\boxed{|T_{IS}(a;G)|+
|q\langle a pRG,pRG\rangle|
\le\frac{3716827}{50000000}N²+\frac9{10}P²
+\frac{68592382803}{20}R_0².}
\tag{1}
\]
The split is TIS p-charge 4/5 and sandwich p-charge 1/10. The companion
program also certifies mu=12,16,20; mu=12 gives rate45972359/864000000 and
weak price684461921409/80. No low-band constant from the old N norm is
used. In particular the Q/N order of W and Jq is fully accounted for.

## Actual coefficient moments

Write A0=||op(a)||2, A1=||W op(a)||2, A2=||r² op(a)||2. The exact erflog
moment, with ell=log(8)/(2sqrt(pi)), is
\[
I_b=\int_0^\infty r^{b-1}\chi(r)^2dr
=\frac{8^{b/2}}b e^{b²\ell²/4}
\operatorname{erfc}\left(\frac{b\ell}{2\sqrt2}\right).
\]
Using s=137/125 and spatial scale alpha=2 gives the upper bounds
\[
A0\le s(2\pi\alpha²I_2)^{1/2},\quad
A1\le s[2\pi(\alpha²I_2+4\alpha^4I_4)]^{1/2},\quad
A2\le s(2\pi\alpha^6I_6)^{1/2}.
\tag{2}
\]
Their certified displays are 9.74524,86.39021,267.48874. All uses of these
displays in the program use containing Arb values rather than rounded
decimal inputs.

## A smooth input cutoff resolves the very-low Riesz kernel

Let K=F^-1(R psi_nu). The direct Bessel proof of the low-kernel note,
specialized to exponent zero, gives
\[
|K(z)|\le\frac{3\nu²}{10\pi},\quad
|K(z)|\le\frac4{\pi|z|²},\quad
\|K\|2²=\frac1{2\pi}\int_0^\infty r e^{-2(r/\nu)^4}dr.
\tag{3}
\]
The exponent-zero variation is the unperturbed integral
1+8exp(-5/4)<7/2<4, so no positive-exponent estimate is needed here.

Choose L=8000000 and b_L(y)=exp(-|y|²/L²). Split
a R psi_nu G=a K b_L G+a K(1-b_L)G. The second operator is
Hilbert--Schmidt on G, with
\[
\boxed{\eta²\le\frac{8A2²\|K\|2²}{L^4}
+\frac{128A0²}{\pi L²}.}
\tag{4}
\]
Indeed, for z=x-y,
1-b_L(y)<=min(1,2|x|²/L²)+min(1,2|z|²/L²). Square this, use
the inequality (u+v)²<=2u²+2v², and integrate. The first term is
8A2²||K||2²/L4. For the second, the tail bound in (3) gives exactly
\[
\int|K(z)|²\min(1,2|z|²/L²)^2dz\le64/(\pi L²).
\]
This is an operator estimate on G, hence contributes eta N without
requiring a small unweighted norm of Wg.

The first operator has adjoint kernel J_y^q[b_L(y)W(y)K(x-y)]. It is
therefore priced from g in L2 by the Hilbert--Schmidt norm of that kernel.
For L>=10^6,
\[
\|D(Wb_L)\|infty\le4,\quad
\|D²(Wb_L)\|infty\le7,\quad
\|D³(Wb_L)\|infty\le61.
\tag{5}
\]
All derivative tensors use the ordered Frobenius norm. For clarity,
||DW||<=2, ||D²W||F<=4sqrt2<6, ||D³W||F<60. For exp(-|y|²/L²), its
derivative constants c1,c2,c3 are below1,5,12, and those derivatives
multiplied by |y|/L have constants below3/4,3,11. These follow by maximizing
s^j exp(-s²); the program verifies the resulting exact exp/rational
comparisons. Leibniz gives (5), bounded by respectively
2+1/L+3/2, 6+10/L+5/L², and60+18/L+52/L²+12/L³.

Let E_j=||D^jK||2² and V_j=||z D^jK||2². For j>=1,
\[
E_j=\frac1{2\pi}\int_0^\infty r^{2j+1}e^{-2(r/\nu)^4}dr,
\]
\[
V_j=\frac1{2\pi}\int_0^\infty e^{-2(r/\nu)^4}
[(j²+j+1)r^{2j-1}-8j r^{2j+3}/\nu^4+16r^{2j+7}/\nu^8]dr.
\tag{6}
\]
The angular tensor (unit xi)^(tensor(j+1)) has derivative norm² j+1,
which proves (6) directly by Plancherel. Every integral is a closed Gamma
value. Symmetry makes the weighted kernel cross term linear in x·z vanish.
Thus ||a W D^jK||HS<=sqrt(A1² E_j+4A0² V_j).

For j=0 use the smooth cutoff itself. Splitting relative displacement at
|z|=L and using W²b_L²<=2L² for the tail gives
\[
T_0²\le A1² E_0+A0²\left[\frac9{50\pi}
+\frac{128}\pi\log(L\nu)+\frac{32}\pi\right].
\tag{7}
\]
On the inner region drop b_L, use W(x-z)²=W(x)²-8x·z+4|z|²,
and integrate (3); on the outer region integrate |K|²<=16/(pi²r4).
For j=1,2,3, Leibniz and (5) give
\[
T_j\le\sqrt{A1²E_j+4A0²V_j}
+A0\sum_{l=1}^j\binom jl M_l\sqrt{E_{j-l}},\quad(M1,M2,M3)=(4,7,61).
\]
Consequently H2=(T0²+2T1²+T2²)^1/2 and
H3=(T0²+3T1²+3T2²+T3²)^1/2 bound the adjoint H² and H³
Hilbert--Schmidt norms. Fourier Holder interpolation gives its H^q norm
at most H2^.9 H3^.1. The executed values prove
\[
\boxed{\|aR\psi_\nu G\|2\le220R0+\eta N,
\qquad\eta<7.776\cdot10^{-6}<11\cdot10^{-6}.}
\tag{8}
\]

## The pR/nR low corrections and the entire mid band

For any kernel H whose weighted H²/H³ quantities are finite define
B_j=||J^j H||2, U2=||a W J²H||HS,
Ug=||a W grad J²H||HS. Direct product differentiation gives
\[
P2=U2+A0(4B1+8B0),
\]
\[
Pg=Ug+A0(6B2+16B1+32B0),\quad P3=(P2²+Pg²)^{1/2}.
\tag{9}
\]
Here Hess(W) has operator norm<=4, Delta(W)<=8, and
|grad Delta(W)|<=32. Thus P2^.9 P3^.1 prices a H WJ^q from g in L2.

For the low corrections use
nR=R-mR, |m(r)|<=r, |m'(r)|<=1;
pR=R-(1-p)R, 0<=1-p<=r²/2, |(1-p)'|<=r.
If |b|<=C r^d, |b'|<=D r^(d-1), the symbol J^j b psi_nu satisfies
\[
|\partial_r(J^jb\psi_\nu)|²
\le3j²C²r^{2d+2}J^{2j-4}\psi_\nu²
+3D²r^{2d-2}J^{2j}\psi_\nu²
+48C²r^{2d+6}J^{2j}\psi_\nu²/\nu^8.
\tag{10}
\]
Add the angular term C²r^(2d-2)J^(2j)psi². For grad J²H the angular
tensor has rank two, and replace (d,D) by(d+1,D+C). Equations(9)--(10)
give Q low correction prices below .005335 for p and .403318 for n.
Together with the unrounded R price219.556475, both full low prices are
still below220 with the same eta in (8).

For the mid band H=R(psi_mu-psi_nu), optionally multiplied by p or n,
the weighted Fourier kernel norm is finite with no input cutoff. For
J²H the scalar radial bounds (beta,d) are (2,2),(1,1),(0,2) for R,pR,nR;
for grad J²H they are (3,3),(2,2),(1,3), with angular rank two. These
follow from n=1/[J(J+r)], J²n=J/(J+r),
|(J²n)'|=1/[J(J+r)²]. The program integrates the simple inequalities
amplitude<=J^beta and derivative<=d J^(beta-1), including the two quartic
cut derivatives. The radial tail powers integrate to Gamma values.
At beta=0 the angular r^-1 integral over r>=1 is bounded by the finite
r^0 integral; no Gamma(0) expression is used.

Applying (9) and H²/H³ interpolation gives, including the low band,
\[
\begin{array}{c|rrr}
\mu&A_n&A_p&A_R\\\hline
10&800&2127&19063\\
12&921&2920&32876\\
16&1168&4949&78535\\
20&1421&7582&155209
\end{array}
\]
For each row and B=nR,pR,R respectively,
\(\|a B\psi_\mu G\|2\le A_B R0+11\cdot10^{-6}N\).
All rounded integers are strict containing uppers checked by Arb.

## Final TIS and sandwich assembly

The remaining algebra is independent of the norm used to represent G.
Use G_high=(1-psi_mu)G and G_low=psi_mu G. The exact polarized form is
\[
TIS(a;G)=q[\langle anRG,nRG\rangle
+\langle apRG,pRG\rangle-2\Re\langle aRG,nRG\rangle].
\]
The high/high part is bounded by
q s(2/mu²+1/(4mu4))N². The remaining polarized terms, using the three
prices just proved and Young's inequality, have bound
\[
(8q\eta+e_Y)N²+D P²+
\left[q²(A_n+A_p+A_R)²/D+q²A_n²/e_Y\right]R0².
\tag{11}
\]
This is the same explicit expansion as in the earlier near-strain note;
its operator inputs have now been reproved in Q. For the near p sandwich,
the high/high part costs q s/mu² N², and its remaining terms give
\[
2q\eta N²+D_sP²+q²A_p²/D_s\,R0².
\tag{12}
\]
Set eY=1/200, D=4/5, Ds=1/10, eta=11/10^6. Substitution of mu10 in
(11)--(12) gives exactly (1). The certificate stores every separate rate
and price, allowing a reviewer to allocate them without hidden rounding.
