# A local background identity in the Q norm

Status: exact identity and analytic implication. Actual pointwise coefficient
bounds and the final invariant-ball arithmetic must be supplied separately.
This route eliminates the individually priced TIS, TII, Ew, and Riesz
principal-source commutators from the final join.

Let q=2+delta=21/10 and use an auxiliary weight
\[
W²=1+\omega r²,\quad\omega=a²>0,\qquad
f=J^\delta g,\quad h=J²f=J^qg,\quad G=Wh.
\]
The center is the actual corrected Candidate013, with divergence-free u,
b=grad rho, V=cX+u, S=Sym Du, and
\[
d=c+1+V\cdot\nabla\log W,\quad
K=\begin{pmatrix}-b_y&b_x/2\\b_x/2&0\end{pmatrix},\quad
M=(d-qc)I-qS-K.
\]
Here b_y denotes the y component of b, namely rho_y. Put
\[
C=W²M,\quad D=W²d,\quad v=W²\operatorname{div}(cI+S)
=\tfrac12W²\Delta u.
\]
The only nonlocal lower-order source retained below is b·U f. The full
source commutator and the two fractional transport terms are precisely the
ones in the separately proved source estimate and second-Taylor note.

## Exact background energy before estimating any term

For real S1 Schwartz g, let
\(E=\Re\langle WJ^qL_*g,G\rangle\), with
\(L_*=V\cdot\nabla-1+b\cdot U\).
Remove the exact full source commutator
\(\langle W[J^q,b\cdot]U[g],G\rangle\)
and the exact two fractional transport terms in the second-Taylor note;
call their sum Efrac. Then
\[
\begin{aligned}
E-Efrac={}&-\sum_{k=1}^2\int(\nabla\partial_kf)^TC(\nabla\partial_kf)
-\int(\nabla f)^T(C+DI)\nabla f-\int Df²\\
&+\frac12\int(\nabla f)^T\operatorname{cof}D²(\operatorname{tr}C)\nabla f
+\frac12\int\operatorname{divdiv}(C+DI)f²\\
&+q\int(\nabla f)^T[\tfrac12(\operatorname{div}v)I-
\operatorname{Sym}Dv]\nabla f
+\frac q2\int(\operatorname{div}v)f²\\
&+\int W²h\,b\cdot U f.
\end{aligned}
\tag{1}
\]
The cofactor in this formula is the 2-by-2 matrix cofactor; for a symmetric
matrix it is a linear map and has the same operator norm.

Here are the required exact reductions. Transport integration gives
\(-\int(d-qc)W²h²-qc\int W²fh\).
The second-Taylor main term is
\(-q\operatorname{div}(S\nabla f)\).
The joint IPM velocity convention gives the exact local identity
\[
U\Delta f=(f_{xy},-f_{xx}),\qquad
b\cdot U h=b\cdot U f-K:D²f.
\]
Thus the highest-order integrand is
\(-W²(\Delta f)(M:D²f)\).
The remaining fD²f coefficient is W²(M+dI), the remaining f² coefficient
is -W²d, and the remaining transport cross term is
\(-q\int h\,v\cdot\nabla f\).

For symmetric 2-by-2 M and H, the pointwise Cayley-Hamilton identity is
\[
(\operatorname{tr}H)(M:H)
=\sum_k(H e_k)^TM(H e_k)+(\operatorname{tr}M)\det H.
\]
The null-Lagrangian identity, obtained by two integrations by parts, is
\[
\int A\det D²f=\int A_{xy}f_xf_y-
\tfrac12\int(A_{xx}f_y²+A_{yy}f_x²).
\]
These give the first and fourth terms in(1). Symmetric integration by
parts in f(C+DI):D²f gives the second and fifth terms. Finally
\[
-q\int(f-\Delta f)v\cdot\nabla f
=q\int[\tfrac12(\operatorname{div}v)I-\operatorname{Sym}Dv]
:(\nabla f\otimes\nabla f)
+\tfrac q2\int(\operatorname{div}v)f²,
\]
which is crucial: this cross term is a purely local quadratic lower-order
form. It need not be bounded by a first-order cross-norm estimate.

## Comparison with Q and the exact lower coefficients

The quadratic weight has the exact identity
\[
\boxed{\|Wh\|²=\|WD²f\|²+2\|W\nabla f\|²+\|Wf\|²
-2\omega\|\nabla f\|²-4\omega\|f\|².}
\tag{2}
\]
Indeed ||WDelta f||²-||WD²f||²=2 integral W²detD²f=-2omega||grad f||²,
and integration by parts in -2 integral W²fDelta f gives
2||Wgrad f||²-4omega||f||².

Suppose an actual pointwise certificate proves M>=beta I and d>=dmin>=beta.
Define the explicit local correction coefficients
\[
E_1=\tfrac12\operatorname{cof}D²(\operatorname{tr}C)
+q[\tfrac12(\operatorname{div}v)I-\operatorname{Sym}Dv]
-2\beta\omega I,
\]
\[
E_0=\tfrac12\operatorname{divdiv}(C+DI)
+\tfrac q2\operatorname{div}v-4\beta\omega.
\tag{3}
\]
Then(1)--(2) imply, with N=||G|| and Fw=||Wf||,
\[
E\le-\beta N²-(dmin-\beta)(\|W\nabla f\|²+Fw²)
+K_1\|\nabla f\|²+K_0\|f\|²
+\int W²h\,b\cdot U f+Efrac,
\tag{4}
\]
whenever E1<=K1 I and E0<=K0 pointwise. One may use conservative absolute
norm uppers, but only an upper bound is required.

Every coefficient in(3) is bounded globally for the actual source:
\(W²d=(c+1)+\omega[(2c+1)r²+u\cdot X]\)
and C is a quadratic polynomial plus symbols of growth2-gamma. Its second
derivatives are constants plus decaying symbols. The derivative Dv uses
at most third derivatives of u; the source contribution uses at most third
derivatives of rho. Thus these are finite, explicit pointwise obligations.

There is an especially useful exact scalar simplification. Since
divdiv S=0, divdiv K=0, tr S=0, div v=omega X·Delta u,
\[
\boxed{E_0=\omega\{2(4c+2-qc)-4\beta+
(1-q/2)X\cdot\Delta u+\rho_y+x\rho_{xy}-y\rho_{xx}\}.}
\tag{5}
\]
In particular the scalar correction needs only second profile derivatives,
and the velocity coefficient1-q/2=-1/20 is small. The signs in(5) follow
from div K=(-rho_xy/2,rho_xx/2) and tr K=-rho_y.

A sufficient new certificate for dmin=c+1 is simply ||S||infty,op<c.
Indeed u(0)=0 and
X·u(X)=integral_0^1 X·S(tX)X dt>=-||S||infty r²,
so V·X>=0 and V·grad(logW)>=0. This does not require reproducing the
sharper inherited137/125 number. Direct certification of V·X>=0 is an
alternative.

## The remaining lower source is cheap to split in physical space

For a chosen radius Rb define
\[
Bnear=\sup_{r\le Rb}W|b|,\qquad Bfar=\sup_{r>Rb}|b|.
\]
The split requires no coefficient differentiations. The joint unweighted
velocity norm is at most one, and the separately proved S1 weighted
velocity estimate is ||WU f||<=sqrt3||Wf|| for every quadratic W.
Therefore
\[
\left|\int W²h\,b\cdot Uf\right|
\le Bnear\|f\|N+\sqrt3Bfar Fw N.
\]
For any 0<eta_f<=dmin-beta, the latter term is bounded by
\(\eta_f Fw²+3Bfar²N²/(4\eta_f)\), paid from the explicit negative
weighted-f allowance in(4).

If N=Q(g)>=M and ||g||<=R, let r=R/M. Exact L2 interpolation gives
\[
\|\nabla f\|²/N²\le r^{20/21},\qquad
\|f\|²/N²\le r^{40/21},\qquad\|f\|/N\le r^{20/21}.
\]
Consequently the entire local and lower-source loss in(4) is at most
\[
\boxed{(K1+Bnear)r^{20/21}+K0r^{40/21}
+\frac{3Bfar²}{4\eta_f}.}
\tag{6}
\]
The source commutator and the two fractional transport terms retain their
separately proved small outside-ball rates. The nonlinear frozen-drift
estimate can then be added directly. No TIS, TII, Cvs3, or Ew term should
also be charged in this branch; doing so would double-count the exact
local reductions.

All identities extend from Schwartz tests to the Q graph form by density.
For clarity, Q controls the weighted H² norm of f: use h=J²f and the
bounded smooth Bessel multipliers p², grad p², Hess p²; their coordinate
commutators are bounded by differentiating their smooth Fourier symbols.
Thus Wf,Wgrad f,WD²f are L2 and smooth cutoffs approximate the form. The
bounded coefficients E0,E1 and the stated tame source/fractional estimates
permit passage to the limit. Numerical completion of these coefficient
bounds, actual M/d certificates, and the final ball inequality remains
essential before asserting any stationary theorem.
