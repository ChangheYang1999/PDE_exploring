# Independent audit of T2's improved scalar energy rate

## Statement and scope

This is an independent audit of T2-R1 and FW-T-TB-rebal-v1 in the frozen source `source/T2_routes_v01.md`, Section 2. It is conditional on the background inequalities of Analysis II, P7.5 and P8.4. It does not certify those inequalities for a new profile and does not supply a small residual.

All functions are real, even in x and odd in y. Use the canonical velocity

\[
U[h]=(-R_1R_2h,R_1^2h),\qquad R_j=\partial_j(-\Delta)^{-1/2},
\]

and the homogeneous negative norm \(H=\dot H^{-1}(\mathbb R^2)\), defined by completion of the smooth compact parity core. Put

\[
\omega=(1+4|X|^2)^{2/5},\quad b_0=20/21,
\]
\[
E_0(h)^2=\|h\|_2^2+b_0\|h\|_H^2,\qquad
E_2(h)^2=\|\omega D^2h\|_2^2+2^{14}\|Dh\|_2^2+2^{18}E_0(h)^2.
\]

Every tensor sums over all ordered Cartesian derivatives. Let \(Lh=(cX+U[\bar\rho])\cdot Dh-h+U[h]\cdot D\bar\rho\). Assume the exact P7.5 inequalities

\[
-\langle Lh,h\rangle_{E_0}\ge \frac{11}{4}E_0(h)^2,
\]
\[
-\langle D Lh,Dh\rangle\ge\frac9{10}a^2-6ab,
\]
\[
-\langle D^2Lh,\omega^2D^2h\rangle
\ge\frac12P^2-\frac{347}{5}aP-10bP-40a^2,
\tag{1}
\]

where \(P=\|\omega D^2h\|_2\), \(a=\|Dh\|_2\), and \(b=\|h\|_2\). Assume the compatible generator realizations and the coefficient bounds of P8.4, namely

\[
(C,U_1,U_2,U_3,R_1,R_2,R_3,R_4)\le(2,6,24,160,22,32,80,2048),
\]

with precisely the component-sum conventions in the frozen P8.4 source under `../graded_closure_audit/source/`. Also assume the baseline structural conditions B0, B0n and B4 when asserting normalized nonlinear existence and positive slope.

Then

\[
-\operatorname{Re}\langle Lh,h\rangle_{E_2}\ge \frac{297}{1000}E_2(h)^2.
\tag{2}
\]

For \(N_s(h)=E_2(J^sh)\), \(J=(1-\Delta)^{1/2}\), and \(0<s\le1/1024\), the maximal distributional realization of \(A_k=L+U[k]\cdot D\) generates a semigroup satisfying

\[
\|e^{tA_k}\|_{N_s\to N_s}
\le\exp\left[-t\left(\frac{297}{1000}-4800s-
\frac{5N_s(k)}{\sqrt s}\right)\right].
\tag{3}
\]

In particular, set

\[
s=2^{-16},\qquad r=3\,2^{-15},\qquad \eta=3/327680.
\tag{4}
\]

If the actual normalized reference residual \(F\) belongs to \(N_s\) and \(N_s(F)\le\eta\), then exactly one correction in \(\{N_s(h)\le r,\ c[h]=0\}\) solves \(F(\bar\rho+h;c)=0\). Here \(c[h]=\partial_yU_2[h](0)\). The exponent remains fixed; a nonzero prescribed leading tail is preserved whenever the baseline tail hypothesis holds.

## Proof of the improved rate

Write \(e=E_0(h)\). Adding (1) with the E2 weights gives

\[
-\langle Lh,h\rangle_{E_2}
\ge\frac12P^2-\frac{347}{5}aP-10bP-40a^2
+2^{14}\left(\frac9{10}a^2-6ab+44e^2\right).
\]

Since \(0\le b\le e\) and the coefficients of b are nonpositive, replacing b by e lowers this expression. After subtracting \(\mu(P^2+2^{14}a^2+2^{18}e^2)\), the result is the quadratic form with matrix

\[
G(\mu)=\begin{pmatrix}
1/2-\mu&-347/10&-5\\
-347/10&2^{14}(9/10-\mu)-40&-3\,2^{14}\\
-5&-3\,2^{14}&44\,2^{14}-2^{18}\mu
\end{pmatrix}.
\]

At \(\mu=297/1000\), its leading principal minors are exactly

\[
\frac{203}{1000},\qquad
\frac{49583691}{62500},\qquad
\frac{4716457761416}{1953125}.
\]

They are positive. Sylvester's criterion proves (2). No numerical eigenvalue is used.

## Generator and nonlinear steps

P8.4 bounds the background fractional commutator by \(4800sN_s(h)^2\) and the rough transport energy by \(5N_s(k)N_s(h)^2/\sqrt s\). Those bounds do not use the value 1/10 of the base rate. Subtracting them from (2) proves the smooth-core estimate (3).

The P8.1 construction is unchanged: approximate k in Ns by compact smooth parity functions, construct their transport-plus-bounded-coupling semigroups, use uniform energy bounds and L2 convergence to obtain the limiting semigroup, and identify its generator with the maximal distributional domain. The new rate is uniform for the approximants. The negative semigroup integral gives both inverse identities when the rate is positive. Equivalent background domains and the existing low realization are retained.

For (4), the rate throughout the ball is exactly bounded below by

\[
\beta=\frac{297}{1000}-4800\,2^{-16}-5(3\,2^{-15})2^8
=\frac{13641}{128000}>\frac1{10}.
\]

Thus the high inverse has norm below 10 and \(10\eta=r\). Define \(T(k)=-A_k^{-1}F\). Exact B0n gives \(F_y(0)=0\). The origin identity

\[
(A_kh)_y(0)=c[k]h_y(0)+a_0c[h]
\]

therefore makes the ball with c[k]=0 invariant. The difference equation is

\[
A_k(T(k)-T(l))=-U[k-l]\cdot DT(l).
\]

The consistent low inverse has norm at most \((19/5-d)^{-1}\), where

\[
d=\frac{r}{2\sqrt{\pi s(1+s)}}<0.00662.
\]

The stream-function divergence identity gives the contraction ratio at most

\[
\frac{d}{19/5-d}<0.0018<1.
\]

The baseline simultaneous-domain argument places this difference in the low generator domain. Weak compactness of the high ball and continuity of its injection into H make that ball complete in the low metric, including the closed strain constraint. The contraction theorem proves existence and uniqueness. For any solution in the same ball the inverse identity makes it a fixed point, so the uniqueness statement covers every distributional solution in that ball.

The B0/B0n/B4 consequence \(a_0>7/10\) and \(|h_y(0)|\le d\) give positive corrected slope. Neither the old numerical inequality d<1/400 nor the old value s=2^-18 is required here. If the optional local moment is desired, take \(\delta=s/2=2^{-17}\), \(p=2^{19}\), and \(\kappa=p+4\). Then p delta=4 and both baseline moment-window inequalities still hold. The actual embedding constants must use this new s.

## Verification evidence and limitations

`code/check_rationals.py` independently constructs G with exact fractions and checks every leading principal minor. It also checks beta and the threshold exactly and encloses d and the contraction ratio with Arb256. Output is in `verification/rationals.json`.

This gives a sufficient threshold 72/5 times the old numerical threshold, but in the different norm N_(2^-16), not in N_(2^-18). For any candidate, membership, all background conditions and the new residual upper bound must still be certified. No candidate is certified here. The existing ordinary-derivative comparison remains valid at the new s.
