# Exact background energy in the alternative Q norm

Status: exact algebra and a favorable dilation form. No quantitative bound for the complete new remainder is asserted.

Set q=21/10, W²=1+4r², b=grad rho*, V=cX+u*,
\[
f=J^qg,\quad G=Wf,\quad S=Sym Du_*,\quad a_W=V\cdot\nabla\log W,
\]
\[
Kmat=\begin{pmatrix}-b_y&b_x/2\\b_x/2&0\end{pmatrix},\quad
M_*=(c+1+a_W)I-q(cI+S)-Kmat.
\]
Define T=WJ^-2W^-1. The Q-norm energy is
\[
\mathfrak Q_Q(G)=\Re\langle WJ^qL_*J^{-q}W^{-1}G,G\rangle,
\quad L_*g=V\cdot\nabla g-g+b\cdot U[g].
\]
Using [Jq,cX·grad]J^-q=qc(1−J^-2), the exact decomposition is
\[
\boxed{\mathfrak Q_Q(G)=-\int(RG)^TM_*(RG)-qc\Re\langle TG,G\rangle
+T_{II}+C_{vs3}+E_W^{sym}+C_{tr,Q}+C_{vs1,Q}.}
\]
All remainder symbols denote their real quadratic forms, with
\[
T_{II}=\sum_j\langle a_WR_jG,R_jG\rangle-\langle a_WG,G\rangle,
\]
\[
C_{vs3}=\langle b\cdot U[G],G\rangle-\int(RG)^TKmat(RG),
\quad E_W^{sym}=\Re\langle b\cdot[W,U]W^{-1}G,G\rangle,
\]
\[
C_{tr,Q}=\Re\langle W[J^q,u_*\cdot\nabla]J^{-q}W^{-1}G,G\rangle
-q\int(RG)^TS(RG),
\]
\[
C_{vs1,Q}=\Re\langle W[J^q,b\cdot]J^{-q}UW^{-1}G,G\rangle.
\]
There is no [Jq,aW] commutator. The weight is multiplied after the high derivative, so aW is created only by direct transport conjugation. The q=0 exact double-commutator form and the S1 far multipole cancellation apply directly to Ew_sym, without Jq conjugating it.

The principal matrix is exactly the same M* as in the original N norm. The matrix occurrence does not by itself certify the new remainder.

## The weighted Bessel resolvent has a nonnegative real form

Let l=logW. For Schwartz tests the inverse of T is
\[
T^{-1}=WJ²W^{-1}
=-\Delta+2\nabla l\cdot\nabla+1+\Delta l-|\nabla l|².
\]
Integration by parts gives
\[
\Re\langle T^{-1}h,h\rangle=\|\nabla h\|₂²+
\int(1-|\nabla l|²)|h|²\ge0,
\]
because
\[
|\nabla l|²=\frac{16r²}{(1+4r²)²}\le1.
\]
Putting h=TG yields Re<TG,G>>=0. T is bounded on L2: its Bessel-resolvent kernel is nonnegative, exponentially decaying, and has a finite first spatial moment; the elementary Peetre bound W(x)/W(y)<=sqrt2 W(x−y) and Young's inequality apply. Thus the real-form inequality extends by density to all L2 tests.

Consequently the full dilation term −qc Re<TG,G> is favorable and can be retained or discarded without assigning a positive remainder price. It is not being identified with −qc||J^-1G||².

## What the initial screens show

`full_remainder_screen.py --norm-order Q --skip-gram` evaluates this exact algebra on a finite Fourier grid. Its negative_sandwich output is qc Sym<Tphi_j,phi_i>. KQ=E_Q+principalM+negative_sandwich is the sum of the five displayed remainders. The old B=||WJqphi|| Gram is not the correct finite price for Q and is deliberately not used in Q screens.

At rank36, alpha1, grid512, radius24, the FLOAT largest eigenvalue of KQ is.86685. At rank136 it is.98903. Full pointwise-M dual finite-core absorption at beta0=.5 gives FLOAT largest eigenvalues.86735 and.99343, respectively. These are not operator certificates. The norm change simplifies the analytic remainder and improves the nonlinear loss, but the numerical core is only moderately improved from the old Kc.

A linear coercivity/remainder certificate in this norm is still required. The source and nonlinear estimates are separate obligations, treated elsewhere.

## Quantitative S1 improvement: T controls a fixed Bessel low-order norm

On the real S1 subspace one has the stronger exact inequality
\[
\boxed{\Re\langle WJ^{-2}W^{-1}G,G\rangle\ge\tfrac13\|J^{-1}G\|₂².}
\]
Here is a proof retaining all operator domains through bounded forms.

For an S1 function h, angular Poincare on each circle gives
\(\|h/r\|₂\le\|\nabla h\|₂\). Also \(|\nabla l|\le1\) and \(|\nabla l|\le1/r\). Thus, writing F=||h||₂ and D=||grad h||₂, the symmetric form
\[
H_0[h]=D²+F²-\|h\nabla l\|₂²
\]
is at least F² and at least D², hence
\[
\tfrac12\|h\|_{H¹}²\le H_0[h]\le\|h\|_{H¹}².
\]
The skew form of M=T^-1 is
\[
B_0(h,v)=\langle\nabla h,v\nabla l\rangle-\langle h\nabla l,\nabla v\rangle,
\]
whose absolute value is at most
\(D_hF_v+F_hD_v\le\|h\|_{H¹}\|v\|_{H¹}\).

Consequently the bounded form operator
\(V=J^{-1}MJ^{-1}=H+B\) on L2S1 has H self-adjoint with I/2<=H<=I, and B skew-adjoint with norm<=1. Lax-Milgram, or coercivity of V and its adjoint, makes V invertible. The exact bounded-operator identities give
\[
\Re(V^{-1})=V^{-*}HV^{-1},\qquad
[\Re(V^{-1})]^{-1}=VH^{-1}V^*=H-BH^{-1}B\le3I.
\]
Thus Re(V^-1)>=I/3. On Schwartz inputs, the Lax-Milgram inverse agrees with the explicit T by uniqueness; both extend boundedly to the required spaces. Since T=J^-1V^-1J^-1, the boxed inequality follows.

The frozen Q-norm background energy therefore retains at least
\(qc/3\|J^{-1}G\|₂²\), about1.26722345 at the fixed exponent. This is a proved low-frequency damping allowance; it does not by itself bound any background commutator remainder.

### Sharpening to one half by retaining radial/angular structure

The coordinator sharpened the preceding bound, independently checked here, to
\[
\boxed{\Re\langle TG,G\rangle\ge\tfrac12\|J^{-1}G\|₂²\quad\text{on S1}.}
\]
Indeed ell is radial. Write Drad and Dang for the radial and angular gradient L2 norms. Angular Poincare and |ell|<=1/r give E²=||ell h||²<=Dang², so
\(H_0[h]>=Drad²+||h||²\).
The skew form uses only radial derivatives and |ell|<=1; therefore
\[
|B_0(f,h)|\le Drad(f)\|h\|+\|f\|Drad(h)
\le\sqrt{H_0[f]H_0[h]}.
\]
Thus A=H^-1/2 B H^-1/2 is a skew-adjoint contraction. Its inverse identity gives
\[
\Re(V^{-1})=H^{-1/2}(I-A²)^{-1}H^{-1/2}\ge\tfrac12 H^{-1}\ge\tfrac12 I.
\]
This proves the sharper boxed inequality, hence a free global damping allowance qc/2, about1.90083517. The separate coordinator note `../Q_DILATION_LOCALIZATION.md` records additional spatial localization estimates; they are not proved by the present note.
