# A polynomial bound for the second-order remainder

**Status: CONFIRMED.** The constants below are conservative Cauchy bounds, not a claim to compute the optimal Hessian norm. They give a directly evaluable, reference-dependent result. Keeping the different quadratic terms separate is important when \(h\) is prescribed.

## 1. Space and reference inputs

Fix \(0<r<1\), \(0<\sigma\le2\), \(0<\theta\le1\), and write \(\ell=1-r\). For a compatible direction
\[
v=c_3u^3+c_5u^5+c_7u^7+R_v
\]
define
\[
\boxed{\|v\|_N=\sum_{j=3,5,7}|c_j|
+\sup_{0<u\le r}u^{-5-\sigma}|R_v''(u)|
+\sup_{[r,1]}|v''|
+\sup_{r\le u<1}\frac{|v''(u)-v''(1)|}{(1-u)^\theta}.}          \tag{12}
\]
The functions and their derivatives match at \(r\), and \(v(1)=v'(1)=v'(0)=0\). The associated complex Banach space is obtained by using complex absolute values. All admissible real traces below belong to its affine translate. Smoothness on the open interval may be imposed for comparison with the PDE obstruction.

There are no unbounded integration constants hidden in (12):
\[
|R_v'|\le\frac{\|v\|_N u^{6+\sigma}}{6+\sigma},\qquad
|R_v|\le\frac{\|v\|_N u^{7+\sigma}}{(6+\sigma)(7+\sigma)},       \tag{13}
\]
\[
|v'(u)|\le(1-u)\|v\|_N,\qquad
|v(u)|\le(1-u)^2\|v\|_N/2\quad(u\ge r).                      \tag{14}
\]
These follow by integration from 0 and 1, respectively. In particular (12) is a norm, and the space is complete by taking limits of the coefficients and the controlled second derivatives and integrating (13)–(14).

Let \(w_0\) be a compatible reference at \(A_0>2\), analytic at 0 and \(C^3\) through 1, negative on \((0,1)\). An analytic polynomial perturbation of the rational reference is an allowed example. Reconstruct \(g_0>0\) with \(g_0/u^2\to1\). Define
\[
I=[A_-,A_+]=[A_0-h,A_0+h],\quad E=[e_0-h',e_0+h'],\quad
e_+=|e_0|+h'.
\]
Choose a complex-parameter buffer \(\tau>0\) such that, on putting
\[
A_m=A_--\tau>2,\quad A_M=A_++\tau,\quad
b_-=\frac2{A_M},\quad b_+=\frac2{A_m},
\]
one has
\[
\boxed{\sigma>b_+,\qquad \theta+b_->1.}                       \tag{15}
\]
The notation \(b_\pm\) here includes the complex buffer; it is not just the range of the real exponent. If the distance of complex \(A\) from \(I\) is at most \(\tau\), then
\[
|A|\in[A_m,A_M],\quad |\beta|\le b_+,\quad
b_-\le\Re\beta\le b_+.
\]
For completeness, inversion maps the disk \(|A-a|\le\tau<a\) to a disk with real endpoints \(1/(a+\tau),1/(a-\tau)\); this proves the asserted real-part bounds.

Here is the complete list of reference function norms needed for the bound. For an origin function
\[
F=F_0+F_2u^2+F_4u^4+R_F
\]
put
\[
\|F\|_{\mathcal A}
=|F_0|+|F_2|r^2+|F_4|r^4+
\sup_{0<u\le r}\frac{|R_F(u)|}{(u/r)^{4+\sigma}}.               \tag{16}
\]
Compute
\[
z_0=-w_0/(A_0u),\quad D_0=uz_0',\quad J_0=-w_0''/(A_0u),
\quad E_0(u)=\log\frac{g_0(u)}{u^2z_0(u)},
\]
and the five numbers
\[
Z=\|z_0\|_{\mathcal A},\quad n=\|z_0^{-1}\|_{\mathcal A},\quad
D=\|D_0\|_{\mathcal A},\quad J=\|J_0\|_{\mathcal A},\quad
E_o=\|E_0\|_{\mathcal A}.
\]
Require
\[
\Gamma_0=1-(2+b_+)E_o>0.                                     \tag{17}
\]
For any such reference this can be arranged by reducing \(r\).

For a tail function write
\[
S(F)=\sup_{[r,1]}|F|,\qquad
H(F)=\sup_{r\le u<1}\frac{|F(u)-F(1)|}{(1-u)^\theta}.
\]
Compute
\[
a_0=-w_0/(1-u),\quad k_0=g_0'/g_0,\quad
a_*=\inf_{[r,1]}a_0>0,\quad H_a=H(a_0),
\]
\[
K_0=S(k_0),\quad H_k=H(k_0),\quad
S_w=S(w_0''),\quad H_w=H(w_0''),\quad
g_*=g_0(1),\quad w_{2*}=w_0''(1).
\]
Also compute \(S_p=S(g_0^{-p})\), \(H_p=H(g_0^{-p})\) for \(p=2,3\), and
\[
W_0=\max_{b\in\{b_-,b_+\}}\sup_{r\le u\le1}
(a_0(u)/A_0)^{b-2}g_0(u)^{1-b}.                              \tag{18}
\]
All of these are suprema, an infimum, endpoint values, or a one-dimensional reconstruction integral of explicit reference functions. In particular no unknown neighboring trace appears in this input list.

## 2. An explicit complex neighborhood

Define
\[
Z_1=\frac1{A_0}\max\left(r^2,r^4,r^6,
\frac{r^{6+\sigma}}{(6+\sigma)(7+\sigma)}\right),
\]
\[
D_1=\frac1{A_0}\max\left(2r^2,4r^4,6r^6,
\frac{(8+\sigma)r^{6+\sigma}}{(6+\sigma)(7+\sigma)}\right),
\quad
J_1=\frac1{A_0}\max(6,20r^2,42r^4,r^{4+\sigma}),
\]
\[
E_D=\frac23 n^2Z_1,\qquad
K_D=\frac2{a_*}(1+K_0\ell/2),
\]
\[
H_g=\frac43nZ_1+E_D+\ell K_D,\quad
a_D=\frac{2\ell}{3a_*},\quad
W_D=(2+b_+)a_D+(1+b_+)H_g.
\]
The symbol \(H_g\) is a bound for a logarithmic reconstruction, not \(H(g_0)\). Set
\[
\boxed{d=\min\left(
1,\frac1{4nZ_1},\frac{a_*}{2\ell},
\frac1{12H_g},\frac1{4W_D},
\frac{\Gamma_0}{2(2+b_+)E_D}\right).}                         \tag{19}
\]
All denominators are positive. Let
\[
\rho_+=A_0/A_-,\qquad \boxed{\delta_0=d/(2\rho_+).}             \tag{20}
\]

We will bound the holomorphic function
\[
\mathscr H(A,e,\zeta)
=\mathcal B\left(A,e,\frac A{A_0}(w_0+\zeta)\right)
\]
for \(\|\zeta\|_N<d\), complex \(A\) at distance at most \(\tau\) from \(I\), and real \(e\in E\). This use of complex parameters is only an analytic estimate; the exclusion concerns real traces.

## 3. Reconstruction without a large exponential

The algebra (16) is submultiplicative. Indeed, polynomial products of degree 0, 2, 4 stay in the polynomial part; every higher polynomial degree is at least 6, which is at least \(4+\sigma\), and belongs to the remainder. Estimating the three remaining products proves the assertion. On zero-constant functions the operator \(\mathcal I F=\int_0^uF(t)\,dt/t\) has norm at most \(1/2\).

For \(\bar w=w_0+\zeta\), put \(z=-\bar w/(A_0u)\), \(D_z=uz'\), \(J_z=-\bar w''/(A_0u)\), \(E_z=\mathcal I(z^{-1}-1)\). Equations (13) and (16) give
\[
\|z-z_0\|_{\mathcal A}\le Z_1d,\quad
\|D_z-D_0\|_{\mathcal A}\le D_1d,\quad
\|J_z-J_0\|_{\mathcal A}\le J_1d.
\]
The geometric series and (19) imply
\[
\|z^{-1}\|_{\mathcal A}\le N_z:=\frac n{1-nZ_1d},
\qquad
\|E_z-E_0\|_{\mathcal A}\le E_Dd.
\]
Here the latter follows from
\(\frac12n^2Z_1d/(1-nZ_1d)\le(2/3)n^2Z_1d\).
The exact reconstruction is
\[
g=u^2z\exp(E_z).
\]
At \(r\),
\[
|\log(g/g_0)(r)|\le[(4/3)nZ_1+E_D]d.
\]

On the tail put \(a=-\bar w/(1-u)\), \(j=(A_0-\bar w')/(1-u)\). Direct integration from 1 gives
\[
a(u)=\int_0^1\bar w'(1-t(1-u))\,dt,\quad
j(u)=\int_0^1\bar w''(1-t(1-u))\,dt,\quad k=j/a.
\]
Thus \(a(1)=A_0\), \(j(1)=\bar w''(1)\), and \(k(1)=\bar w''(1)/A_0\). In particular \(g\) extends positively and \(C^1\) to 1 for real traces. If the endpoint modulus is \(\theta\), then
\[
g(u)=g(1)\{1-k(1)(1-u)+O((1-u)^{1+\theta})\}.
\]
The reference analytic case has an ordinary Taylor expansion there.

Equations (14) give \(|a-a_0|\le \ell d/2\), hence
\[
|k-k_0|\le K_Dd,\qquad
\boxed{|\eta(u)|:=|\log(g/g_0)(u)|\le H_gd\le1/12.}           \tag{21}
\]
In addition,
\[
|\eta(u)-\eta(1)|\le K_Dd(1-u).
\]
For complex \(\zeta\), use the logarithm obtained by continuation from \(\zeta=0\); the displayed estimates preclude zeros and give a single branch.

This is the precise replacement for the earlier Gronwall estimate. The earlier proof bounded \(k\) in a whole-tail Hölder norm and used
\(G=g_r^+\exp(HK)\), \(g_{\min}=g_r^-\exp(-\ell K)\).
Repeated inversion of the resulting very small lower bound produced the quoted constants. Here \(g_0\) is retained exactly, and only \(\eta=\int(k-k_0)\), including its origin value, is bounded. Every exponential used below has exponent at most \(1/4\), and is replaced by \(1/(1-t)\le4/3\). There is no exponential of a large reference bound.

## 4. A fully specified bound for \(\mathscr H\)

The following scalar formulas complete the certificate; they can be evaluated without differentiating the nonlinear functional numerically.

Set
\[
\Gamma=1-(2+b_+)(E_o+E_Dd)>0,
\quad
T=\frac{N_z^4}{2\Gamma}
\{1+Z+Z_1d+D+D_1d+e_+A_M(J+J_1d)\},
\]
\[
T_e=\frac{N_z^4 A_M(J+J_1d)}{2\Gamma},\qquad
V=N_z/\Gamma,
\]
\[
F=r^{-4-b_+}\max\{b_-^{-1},(\sigma-b_+)^{-1}\},
\quad I_o=\frac{r^{1-b_+}}{1-b_+},\quad
I_t=\frac{\ell^{\theta+b_--1}}{\theta+b_--1},\quad
c_+=\frac{1+b_+}{3A_m}.
\]
To define the tail numbers, put
\[
a_m=a_*-\ell d/2,\quad
N_a=a_m^{-1},\quad
H_{a^{-1}}=(H_a+\ell^{1-\theta}d/2)a_m^{-2},
\]
\[
K_H=\left[\frac1{1+\theta}+\frac{K_0\ell^{1-\theta}}2+
\frac{H_k\ell}2\right]N_a+(1+K_0\ell/2)H_{a^{-1}},
\]
\[
\widehat S_p=\frac43S_p,\qquad
\widehat H_p=\frac43\{H_p+pS_p\ell^{1-\theta}dK_D\}
\quad(p=2,3).
\]
Finally set
\[
Q_*^+=\frac23(|w_{2*}|+d)
\left(\frac1{A_0g_*^2}+\frac{e_+A_M}{A_0g_*^3}\right),
\quad
Q_{e*}^+=\frac{2A_M(|w_{2*}|+d)}{3A_0g_*^3},
\]
\[
Q_H=\frac12\left\{(K_0+dK_D)\widehat H_2+
(H_k+dK_H)\widehat S_2+
\frac{e_+A_M}{A_0}
[(S_w+d)\widehat H_3+(H_w+d)\widehat S_3]\right\},              \tag{22}
\]
\[
Q_{eH}=\frac{A_M}{2A_0}
[(S_w+d)\widehat H_3+(H_w+d)\widehat S_3].
\]
Hatted symbols concern powers of \(g^{-1}\). In the code the corresponding names are `w2S,w2H` and `g2S,g2H`.

The two final complex bounds are
\[
\boxed{
M=c_+\{FT+Q_*^+ I_o V+(4/3)W_0 Q_H I_t\},\qquad
M_e=c_+\{FT_e+Q_{e*}^+ I_o V+(4/3)W_0 Q_{eH}I_t\}.}          \tag{23}
\]
They bound respectively \(|\mathscr H|\) and \(|\partial_e\mathscr H|\) throughout the specified complex neighborhood.

### Verification of (23)

The exact origin/tail decomposition is
\[
\mathscr H=c(A)\left\{\mathfrak F_\beta(T_z)-Q(1)
\int_0^r u^{-\beta}V_z\,du+
\int_r^1(Q-Q(1))(1-u)^{\beta-2}
(a/A_0)^{\beta-2}g^{1-\beta}\,du\right\},                    \tag{24}
\]
where
\[
T_z=\frac{z^{-4}}2
\{e^{-(\beta+1)E_z}(1+z+D_z)+eA e^{-(\beta+2)E_z}J_z\},
\quad V_z=z^{-1}e^{(1-\beta)E_z},
\]
\[
\mathfrak F_\beta(T_z)=
\sum_{j=0,2,4}\frac{(T_z)_jr^{j-4-\beta}}{j-4-\beta}
+\int_0^r u^{-5-\beta}
[T_z-(T_z)_0-(T_z)_2u^2-(T_z)_4u^4]\,du.
\]
Substitution of \(g=u^2ze^{E_z}\) proves (24). The operators in the first two terms have bounds \(F,I_o\); this follows by integrating each of the three monomials and the weighted remainder. Since \(|\beta+j|\|E_z\|_{\mathcal A}<1\), the exponential series is bounded by the corresponding geometric series, giving \(T,V,T_e\) above.

For the tail, the product inequality
\(H(FG)\le S(F)H(G)+S(G)H(F)\)
and (21) give \(\widehat S_p,\widehat H_p\). Applying it to
\[
k-k_0=\frac{(j-j_0)-k_0(a-a_0)}a
\]
gives \(K_H\); the average defining \(j\) contributes \(1/(1+\theta)\). Applying it to \(Q=(kg^{-2}-e(A/A_0)\bar w''g^{-3})/2\) gives (22). Endpoint substitution gives \(Q_*^+\).

The relative logarithm of \(a\) is bounded by \(a_Dd\). Therefore the ratio of the tail weight to
\((a_0/A_0)^{\Re\beta-2}g_0^{1-\Re\beta}\)
has modulus at most \(\exp(W_Dd)\le4/3\).
Now \(|Q-Q(1)|\le Q_H(1-u)^\theta\); integration gives the tail term in (23). Keeping only the terms linear in \(e\) gives \(M_e\).

These same bounds give locally uniform convergence of the subtracted integrals in complex \(A,\zeta\), and hence holomorphy. One can verify holomorphy without an abstract theorem by expanding each inverse and exponential in its uniformly convergent power series, integrating term by term using the displayed integrable majorants, and passing to limits.

## 5. Second-order constants

Two small, purely parametric constants should be evaluated from the reference, without the large complex bound (23). Set
\[
B_0(A,e)=\mathscr H(A,e,0),\qquad
K_{AA}=\sup_{A\in I,e\in E}|\partial_A^2B_0(A,e)|,\quad
K_{Ae}=\sup_{A\in I}|\partial_A\partial_eB_0(A,e)|.
                                                                    \tag{25}
\]
These are explicit reference quantities: \(B_0\) is (24) with the fixed functions \(z_0,E_0,g_0,a_0\). Differentiate that displayed expression twice. For a completely mechanical prescription, if
\[
J(A,e,\beta)=\operatorname{FP}\int(Q-Q(1))n^{\beta-2}g_0^{-1},
\quad n=-w_0/(A_0g_0),
\]
then \(J_{AA}=0\) at fixed \(\beta,e\), \(J_A=-e\,\operatorname{FP}\int
[w_0''g_0^{-3}-w_{2*}g_*^{-3}]n^{\beta-2}g_0^{-1}/(2A_0)\);
\(J_\beta,J_{\beta\beta}\) insert \(\log n,(\log n)^2\), and likewise for mixed derivatives. With \(\beta'=-2/A^2,\beta''=4/A^3\),
\[
B_{0,AA}=c''J+2c'(J_A+\beta'J_\beta)
+c\{2\beta'J_{A\beta}+\beta''J_\beta+(\beta')^2J_{\beta\beta}\},
\]
\[
B_{0,Ae}=c'J_e+c(J_{Ae}+\beta'J_{\beta e}),\qquad
c''=(12-2A)/(3A^4).
\]
Every FP here is differentiated using the three explicit subtraction fractions in (24). Condition (15) permits the logarithmic factors by domination. Since the dependence on \(e\) is affine, extrema in \(e\) in (25) need only its two endpoints.

Define
\[
\boxed{
D_N=M/d,\quad
K_{Av}=\rho_+\frac M d\left(\frac1\tau+\frac1{A_-}\right),\quad
K_{ev}=\rho_+\frac{M_e}d,\quad
R_{vv}=4\rho_+^2 M/d^2.}                                    \tag{26}
\]
Then, with \(a=|A-A_0|\), \(b=|e-e_0|\), \(t=\|w-(A/A_0)w_0\|_N\le\delta_0\),
\[
\boxed{
|\mathcal B-\mathcal B_0-B_A(A-A_0)-B_e(e-e_0)-D_w\mathcal B(v)|
\le \tfrac12K_{AA}a^2+K_{Ae}ab+K_{Av}at+K_{ev}bt+R_{vv}t^2.} \tag{27}
\]
In particular the exact inequality asked for in question (2) holds with
\[
\boxed{C_2=\max\{\tfrac12K_{AA},\tfrac12K_{Ae},
\tfrac12K_{Av},\tfrac12K_{ev},R_{vv}\}.}                       \tag{28}
\]
Apart from the displayed scalar cutoff powers, all constants are algebraic or rational expressions in the listed reference quantities and the chosen positive margins. Powers and logarithms of reference functions occur inside the explicit reference integrals/norms. There is no Gronwall exponential in any constant.

If “polynomial” is interpreted literally as excluding noninteger powers of the scalar cutoffs, use the following rational majorants throughout: replace \(r^{-4-b_+}\) by \(r^{-5}\); replace the positive powers \(r^{1-b_+}\), \(\ell^{\theta+b_--1}\), and \(\ell^{1-\theta}\) by 1; replace \(r^{6+\sigma}\) by \(r^6\) and \(r^{4+\sigma}\) by \(r^4\) in \(Z_1,D_1,J_1\). Recompute \(d\) and the subsequent constants using those majorants. The proof is unchanged. The resulting constants use rational operations, maxima and minima in the reference inputs and the scalar parameters, equivalently polynomial bounds in those inputs and the inverses of the stated positive margins. Noninteger powers in the reference norm \(W_0\) remain inside a permitted explicit reference supremum. The rational numerical certificates below use the exact integer choice \(\sigma=1\).

### Proof of (27)

For fixed \(A,e\), Cauchy's formula on a complex direction disk of radius \(d/2\) about any \(\|\zeta\|\le d/2\) gives
\[
|D_\zeta^2\mathscr H(\xi,\xi)|\le8M\|\xi\|_N^2/d^2.
\]
The factor 8 is \(2!/(1/2)^2\). At \(\zeta=0\), Cauchy's formula gives
\[
\|D_\zeta\mathscr H\|\le M/d,\quad
\|\partial_A D_\zeta\mathscr H\|\le M/(\tau d),\quad
\|\partial_eD_\zeta\mathscr H\|\le M_e/d.
\]
The mixed estimate uses separate disks in \(A\) and in the chosen direction; their product is contained in the specified neighborhood.

The physical direction in the question is represented by \(\zeta=(A_0/A)v\). Hence
\[
D_v\mathcal B(A,e,0)=(A_0/A)D_\zeta\mathscr H(A,e,0).
\]
Differentiating this factor explains the additional \(1/A_-\) in \(K_{Av}\). Taylor-expand first in \(v\) at the current \(A,e\), then integrate the change of its linear coefficient from \((A_0,e_0)\), and finally expand \(B_0(A,e)\). These three remainders are respectively \(R_{vv}t^2\), \(K_{Av}at+K_{ev}bt\), and \(\frac12K_{AA}a^2+K_{Ae}ab\). There is no \(b^2\) term because \(B_0\) is affine in \(e\). Their sum proves (27), and comparison with \((a+b+t)^2\) proves (28).
