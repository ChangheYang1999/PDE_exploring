# Audit of the polynomial remainder bound

**Verdict: CONFIRMED for the norm in equation (12) of the original remainder estimate (`raw_bounds/02-remainder/PROOF.md`).** The complex extension, reconstruction, main-integral bound (23), and Taylor estimate (27) have no failed division or endpoint integrability step under their stated margins.

**Qualification:** equation (12) in that file uses a monomial remainder. The report uses a different polynomial remainder. Applying the original constants unchanged to that other norm is **UNCLEAR**, because the required estimate is not supplied. Section 7 below repairs the proof in the report's convention and retains the advertised simple radii. We do not claim a counterexample to the old numerical upper bounds themselves.

## Statement and notation

The reference \(w_0\) is compatible at \(A_0>2\), negative on \((0,1)\), analytic and odd at 0, and \(C^3\) through 1. Let \(g_0/u^2\to1\) be its reconstruction. Fix
\[
0<r<1,\quad \ell=1-r,\quad 0<\sigma\le2,\quad 0<\theta\le1.
\]
In this section, until explicitly changed, the norm is
\[
N_{\rm mon}(v)=\sum|c_j|+
\sup_{0<u\le r}u^{-5-\sigma}|R_{\rm mon}''|
+\sup_{[r,1]}|v''|
+\sup_{r\le u<1}\frac{|v''(u)-v''(1)|}{(1-u)^\theta},
\]
where \(R_{\rm mon}=v-\sum_{j=3,5,7}c_ju^j\), \(v(1)=v'(1)=v'(0)=0\), and the origin expansion fixes \(R_{\rm mon}(0)=R_{\rm mon}'(0)=0\). Derivatives match at \(r\). Taking the completion allows the weighted \(C^2\) origin regularity; imposing smoothness on the open interval selects a subspace, and is not needed to claim that this smooth subspace itself is complete.

If \(N_{\rm mon}(v)\le t\), direct integration gives
\[
|R_{\rm mon}'|\le\frac{t u^{6+\sigma}}{6+\sigma},\quad
|R_{\rm mon}|\le\frac{t u^{7+\sigma}}{(6+\sigma)(7+\sigma)},\quad
|v'|\le ts,\quad |v|\le ts^2/2\ (s=1-u,\ u\ge r). \tag{R1}
\]
Thus the norm contains every integration constant used later.

The functional \(B\) and its finite-part convention are defined in the preceding proof. All unadorned capital constants below have exactly the definitions in the original `raw_bounds/02-remainder/PROOF.md`, equations (15) through (26). We restate the essential formulas while checking them, so the argument does not depend on an unproved continuity assertion.

## 1. Complex parameters and positive margins

Set \(I=[A_0-h,A_0+h]=[A_-,A_+]\). Choose \(\tau>0\) with
\[
A_m=A_--\tau>2,\quad A_M=A_++\tau,\quad
b_-=2/A_M,\quad b_+=2/A_m,
\]
\[
\sigma>b_+,\qquad \theta+b_->1. \tag{R2}
\]
For a complex \(A\) within distance \(\tau\) of \(I\), choose a real \(a\in I\) with \(|A-a|\le\tau\). The reciprocal disk has real endpoints \(1/(a+\tau)\) and \(1/(a-\tau)\). Hence
\[
A_m\le|A|\le A_M,\quad |\beta|\le b_+,\quad
b_-\le\Re\beta\le b_+.
\]
In particular \(b_+<1\). Merely using the real parameter interval's extrema of \(2/A\) would not justify the complex Cauchy estimates. The original proof correctly includes the buffer.

The function used for Cauchy estimates is
\[
\mathscr H(A,e,\zeta)=B\left(A,e,\frac A{A_0}(w_0+\zeta)\right).
\]
Its reconstruction \(g\) depends only on \(w_0+\zeta\), not on \(A\). The proof bounds complex \(A,\zeta\) and real \(e\in E=[e_0-h',e_0+h']\). This is enough. Dependence on \(e\) is affine and entire, and the derivative in \(e\) is bounded directly by \(M_e\). No unproved bound over a complex disk in \(e\) is needed.

## 2. Origin algebra and every perturbation constant

For
\[
F=F_0+F_2u^2+F_4u^4+R_F
\]
use
\[
\|F\|_{\mathcal A}=|F_0|+|F_2|r^2+|F_4|r^4+
\sup_{0<u\le r}|R_F(u)|(r/u)^{4+\sigma}.
\]
This norm dominates \(\sup|F|\). It is submultiplicative: retain polynomial products of degrees at most four; assign every other polynomial product to the remainder. Its degree is at least six, and
\((u/r)^j\le(u/r)^{4+\sigma}\) for \(j\ge6\), because \(\sigma\le2\). Products involving remainders satisfy the same bound since \(u/r\le1\). Every product of summands has therefore been counted once and is bounded by its contribution to \(\|F\|_{\mathcal A}\|G\|_{\mathcal A}\).

On the subspace with zero constant term,
\[
\mathcal IF=\int_0^uF(t)\,dt/t,\qquad \|\mathcal IF\|_{\mathcal A}\le\frac12\|F\|_{\mathcal A}.
\]
The coefficients are divided by 2 or 4, and the remainder by \(4+\sigma\ge4\). These observations justify both the inverse and exponential series in this algebra.

Put
\[
z_0=-w_0/(A_0u),\quad D_0=uz_0',\quad J_0=-w_0''/(A_0u),
\quad E_0=\log(g_0/(u^2z_0)).
\]
Let \(Z,n,D,J,E_o\) denote respectively their five norms, with \(n=\|z_0^{-1}\|_{\mathcal A}\). Since \(z_0(0)=1\),
\[
E_0=\mathcal I(z_0^{-1}-1).
\]
Assume \(\Gamma_0=1-(2+b_+)E_o>0\). Analyticity at zero implies \(E_o\to0\) as \(r\to0\), so this is a legitimate additional choice of cutoff.

For \(\bar w=w_0+\zeta\), write \(z=-\bar w/(A_0u)\), \(D_z=uz'\), \(J_z=-\bar w''/(A_0u)\). Equations (R1) give the following constants, each by dividing the corresponding monomial or remainder by \(A_0u\):
\[
Z_1=A_0^{-1}\max\left(r^2,r^4,r^6,
\frac{r^{6+\sigma}}{(6+\sigma)(7+\sigma)}\right),
\]
\[
D_1=A_0^{-1}\max\left(2r^2,4r^4,6r^6,
\frac{(8+\sigma)r^{6+\sigma}}{(6+\sigma)(7+\sigma)}\right),
\]
\[
J_1=A_0^{-1}\max(6,20r^2,42r^4,r^{4+\sigma}). \tag{R3}
\]
For example \(uz'-uz_0'=-(\zeta'-\zeta/u)/A_0\); using the sum of the two remainder bounds produces exactly \(8+\sigma\) in \(D_1\). Thus no derivative of the weighted remainder beyond its second derivative is being assumed.

If \(\|\zeta\|<d\) and \(nZ_1d\le1/4\), the algebra inverse gives
\[
\|z^{-1}\|\le N_z=\frac n{1-nZ_1d}.
\]
With \(E_z=\mathcal I(z^{-1}-1)\),
\[
\|E_z-E_0\|\le\frac{n^2Z_1d}{2(1-nZ_1d)}
\le E_Dd,\qquad E_D=\frac23n^2Z_1. \tag{R4}
\]
The exact identity
\[
g=u^2z\exp E_z
\]
follows by differentiating its logarithm:
\[
2/u+z'/z+(z^{-1}-1)/u=(\bar w'-A_0)/\bar w.
\]
It has the correct origin normalization. Since
\(\|(z-z_0)z_0^{-1}\|\le1/4\), the logarithm series gives, uniformly on \((0,r]\),
\[
|\log(g/g_0)|\le\left(\frac43nZ_1+E_D\right)d. \tag{R5}
\]
The factor \(4/3\) comes from \(\sum_{k\ge1}q^k/k\le q/(1-q)\), not from an exponential in a reference norm.

## 3. Tail reconstruction, signs, and sources

Define
\[
a_0=-w_0/s,\quad a_*=\inf_{[r,1]}a_0>0,\quad
k_0=g_0'/g_0,\quad K_0=\sup|k_0|.
\]
For \(\bar w\), let \(a=-\bar w/s\), \(j=(A_0-\bar w')/s\), \(k=j/a\). The endpoint averaging formulas proved in the preceding file give
\[
|\delta a|\le sd/2,\quad |\delta j|\le d,\quad
|a|\ge a_*-\ell d/2.
\]
The condition \(d\le a_*/(2\ell)\) makes this lower bound at least \(3a_*/4\). Since
\[
k-k_0=\frac{\delta j-k_0\delta a}{a},
\]
we get the conservative bound
\[
|k-k_0|\le K_Dd,\qquad K_D=\frac2{a_*}(1+K_0\ell/2). \tag{R6}
\]
Integrating (R6) from \(r\) and using (R5) proves
\[
|\eta|:=|\log(g/g_0)|\le H_gd,\quad
H_g=\frac43nZ_1+E_D+\ell K_D,
\]
\[
|\eta(u)-\eta(1)|\le K_Dds. \tag{R7}
\]
Also
\[
|\log(a/a_0)|\le a_Dd,\qquad a_D=\frac{2\ell}{3a_*}.
\]
This again uses a relative perturbation of size at most \(1/4\).

For real traces these estimates preserve \(z>0\) on \((0,r]\) and \(a>0\) on \([r,1]\). Therefore \(\bar w<0\) on \((0,1)\). Multiplication by positive real \(A/A_0\) preserves that sign. The affine constraints give exactly the zero and slope at 1, and the sign excludes earlier positive zeros. The reconstruction is positive and has a finite positive endpoint value. In fact
\[
g(1-s)=g(1)\{1-k(1)s+O(s^{1+\theta})\}.
\]
For complex traces these arguments assert absence of zeros, not positivity; the relative logarithm is its convergent branch from the reference. This is precisely what holomorphy requires.

The original cutoff
\[
d=\min\left(1,\frac1{4nZ_1},\frac{a_*}{2\ell},
\frac1{12H_g},\frac1{4W_D},
\frac{\Gamma_0}{2(2+b_+)E_D}\right),
\quad
W_D=(2+b_+)a_D+(1+b_+)H_g \tag{R8}
\]
enforces every preceding condition. It also gives
\[
H_gd\le1/12,\quad W_Dd\le1/4,\quad
\Gamma:=1-(2+b_+)(E_o+E_Dd)\ge\Gamma_0/2>0.
\]
All divisions are by specified positive quantities. Setting
\(\rho_+=A_0/A_-\) and \(\delta_0=d/(2\rho_+)\) ensures that \(v=w-(A/A_0)w_0\), \(\|v\|\le\delta_0\), corresponds to \(\zeta=(A_0/A)v\) with \(\|\zeta\|\le d/2\).

## 4. Main-integral bound (23)

The exact decomposition is
\[
\mathscr H=c(A)\left\{
\mathfrak F_\beta(T_z)-Q(1)\int_0^r u^{-\beta}V_z\,du
+\int_r^1(Q-Q(1))s^{\beta-2}(a/A_0)^{\beta-2}g^{1-\beta}\,du
\right\}, \tag{R9}
\]
where \(c(A)=(\beta-1)/(3A)\), \(\mathfrak F_\beta\) is the explicitly subtracted operator in (D6), and
\[
T_z=\frac{z^{-4}}2\left[
e^{-(\beta+1)E_z}(1+z+D_z)
+eA e^{-(\beta+2)E_z}J_z\right],
\quad V_z=z^{-1}e^{(1-\beta)E_z}.
\]
Substitution of \(g=u^2ze^{E_z}\) proves every power and sign here. In particular the plus sign before \(eAJ_z\) agrees with the minus sign in \(-ew''\), since \(J_z=-\bar w''/(A_0u)\).

The algebra series gives
\[
\|T_z\|\le T=\frac{N_z^4}{2\Gamma}
[1+Z+Z_1d+D+D_1d+e_+A_M(J+J_1d)],
\]
\[
\|\partial_eT_z\|\le T_e=\frac{N_z^4 A_M(J+J_1d)}{2\Gamma},
\quad \|V_z\|\le V=N_z/\Gamma,
\]
with \(e_+=|e_0|+h'\). Indeed each exponential is bounded by its geometric series, using \(|\beta+j|\le2+b_+\) and the margin \(\Gamma>0\).

The bounds for the two origin operators are
\[
F=r^{-4-b_+}\max\{b_-^{-1},(\sigma-b_+)^{-1}\},\qquad
I_o=\frac{r^{1-b_+}}{1-b_+}.
\]
For \(F\), integrate each of the three subtracted monomials: its denominator has modulus at least \(b_-\). The remainder contributes
\(r^{-4-\Re\beta}/(\sigma-\Re\beta)\) times its norm. Their sum is bounded by the maximum, because the algebra norm is the sum of the four corresponding components. Thus no missing factor four occurs.

Here is a check of all tail seminorm constants. Write
\[
S(F)=\sup_{[r,1]}|F|,\quad
H(F)=\sup_{r\le u<1}\frac{|F(u)-F(1)|}{s^\theta}.
\]
Let \(H_a=H(a_0)\), \(H_k=H(k_0)\), \(S_w=S(w_0'')\), \(H_w=H(w_0'')\), and \(S_p=S(g_0^{-p})\), \(H_p=H(g_0^{-p})\), for \(p=2,3\).

* With \(a_m=a_*-\ell d/2\), \(N_a=a_m^{-1}\), one has
  \[
  H(a^{-1})\le H_{a^{-1}}=(H_a+\ell^{1-\theta}d/2)a_m^{-2}.
  \]
  The two denominators in the difference of reciprocals are both at least \(a_m\); this also holds at 1 since \(a(1)=A_0\).
* The averaged second derivative gives \(H(\delta j)\le d/(1+\theta)\); (R1) gives \(H(\delta a)\le\ell^{1-\theta}d/2\), \(S(\delta a)\le\ell d/2\). Applying
  \(H(FG)\le S(F)H(G)+S(G)H(F)\) to the quotient in (R6) proves
  \[
  H(k-k_0)\le dK_H,
  \]
  \[
  K_H=\left[\frac1{1+\theta}+\frac{K_0\ell^{1-\theta}}2+
  \frac{H_k\ell}2\right]N_a+(1+K_0\ell/2)H_{a^{-1}}.
  \]
* From \(g^{-p}=g_0^{-p}e^{-p\eta}\), \(pH_gd\le1/4\) and (R7),
  \[
  S(g^{-p})\le\widehat S_p=\frac43S_p,\quad
  H(g^{-p})\le\widehat H_p=\frac43[H_p+pS_p\ell^{1-\theta}dK_D].
  \]
  For complex \(\eta\), integrate the exponential derivative along the straight segment between \(\eta(u)\) and \(\eta(1)\); that segment stays within the same modulus bound. There is no hidden real-positivity argument here.
* Apply the product inequality to
  \(Q=(kg^{-2}-e(A/A_0)\bar w''g^{-3})/2\). It gives exactly
  \[
  Q_H=\frac12[(K_0+dK_D)\widehat H_2+
  (H_k+dK_H)\widehat S_2+
  (e_+A_M/A_0)((S_w+d)\widehat H_3+(H_w+d)\widehat S_3)],
  \]
  \[
  Q_{eH}=\frac{A_M}{2A_0}
  [(S_w+d)\widehat H_3+(H_w+d)\widehat S_3].
  \]
* At 1, \(k(1)=\bar w''(1)/A_0\). Writing \(g_*=g_0(1)\), \(w_{2*}=w_0''(1)\), this gives
  \[
  |Q(1)|\le Q_*^+=\frac23(|w_{2*}|+d)
  [1/(A_0g_*^2)+e_+A_M/(A_0g_*^3)],
  \]
  \[
  |\partial_eQ(1)|\le Q_{e*}^+
  =\frac{2A_M(|w_{2*}|+d)}{3A_0g_*^3}.
  \]

Finally set
\[
W_0=\max_{b\in\{b_-,b_+\}}\sup_{[r,1]}
(a_0/A_0)^{b-2}g_0^{1-b}.
\]
For intermediate real \(b\), the logarithm of the expression is affine in \(b\), so its value is bounded by the maximum at the endpoints. For complex \(\beta\), the ratio of the perturbed weight to its reference modulus is bounded by
\[
\exp\{|\beta-2|\,|\log(a/a_0)|+|1-\beta|\,|\eta|\}
\le e^{W_Dd}\le4/3.
\]
Using \(|Q-Q(1)|\le Q_Hs^\theta\), its integral is bounded with
\[
I_t=\ell^{\theta+b_--1}/(\theta+b_--1),\qquad
c_+=(1+b_+)/(3A_m).
\]
Collecting the preceding bounds proves the original (23), without a missing supremum:
\[
|\mathscr H|\le M=c_+[FT+Q_*^+I_oV+(4/3)W_0Q_HI_t],
\]
\[
|\partial_e\mathscr H|\le M_e
=c_+[FT_e+Q_{e*}^+I_oV+(4/3)W_0Q_{eH}I_t]. \tag{R10}
\]
All reference suprema are finite under the stated reference regularity and sign assumptions. All neighboring-trace bounds have been deduced from them.

## 5. Holomorphy and second derivatives

Inverses and logarithms are represented by uniformly convergent series in the origin algebra and tail supremum spaces. The explicitly subtracted integrals have uniform integrable majorants
\[
u^{\sigma-b_+-1}\quad\text{and}\quad s^{\theta+b_--2}.
\]
On slightly smaller parameter neighborhoods their derivatives can also be dominated with any fixed finite number of logarithmic factors. These facts prove holomorphy in complex \(A,\zeta\), for example by termwise integration of the locally uniformly convergent series. Smoothness in \(u\) beyond that controlled by the norm is not needed for this conclusion.

Let \(B_0(A,e)=\mathscr H(A,e,0)\), and let \(K_{AA},K_{Ae}\) be the real suprema in the original (25). They are finite reference quantities. To check the stated prescription, \(B_0=cJ\) at fixed reference shape, with \(J_{AA}=0\) when \(\beta,e\) are held fixed. The chain rule gives
\[
B_{0,AA}=c''J+2c'(J_A+\beta'J_\beta)
+c[2\beta'J_{A\beta}+\beta''J_\beta+(\beta')^2J_{\beta\beta}],
\]
\[
B_{0,Ae}=c'J_e+c(J_{Ae}+\beta'J_{\beta e}),
\]
where \(c''=(12-2A)/(3A^4)\), \(\beta''=4/A^3\). These are exactly the stated formulas. Finite-part subtraction derivatives and logarithmic moments are covered above.

Cauchy's formula on direction disks inside \(\|\zeta\|<d\) gives
\[
\|D_\zeta\mathscr H(0)\|\le M/d,\quad
\|\partial_AD_\zeta\mathscr H(0)\|\le M/(\tau d),\quad
\|\partial_eD_\zeta\mathscr H(0)\|\le M_e/d.
\]
The product of the \(A\) disk and the direction disk is contained in the declared neighborhood. At \(\|\zeta\|\le d/2\), the second directional derivative is bounded by \(8M\|\xi\|^2/d^2\). If a disk touches the boundary, use smaller radii and pass to the limit; the uniform bounds are unchanged.

Since the physical direction coordinate is \(\zeta=(A_0/A)v\), its linear coefficient is \((A_0/A)D_\zeta\mathscr H(0)\). The derivative of \(A_0/A\) contributes precisely the extra \(1/A_-\) in
\[
D_N=M/d,\quad
K_{Av}=\rho_+\frac Md(1/\tau+1/A_-),\quad
K_{ev}=\rho_+M_e/d,\quad R_{vv}=4\rho_+^2M/d^2.
\]
Taylor expansion first in \(v\) at the current parameters, then of its linear coefficient, and finally of \(B_0(A,e)\), proves
\[
|B-B_0(A_0,e_0)-B_A\Delta A-B_e\Delta e-D_wB(v)|
\le \tfrac12K_{AA}a^2+K_{Ae}ab+K_{Av}at+K_{ev}bt+R_{vv}t^2,
\]
where \(a=|\Delta A|\), \(b=|\Delta e|\), \(t=\|v\|\le\delta_0\). This is (27). There is no \(b^2\) term because of affine dependence on \(e\). Comparing coefficients with \((a+b+t)^2\) proves (28), including the factors \(1/2\) on mixed coefficients.

## 6. What “polynomial constants” means

The bounds use rational operations, minima, maxima, scalar powers, and explicit reference norms and integrals. Scalar powers can be replaced by the rational majorants given in the original proof. In that sense the bounds are polynomial in the inputs and inverses of the positive margins. These margins include \(A_m-2\), \(a_*\), \(\Gamma_0\), the complex buffer \(\tau\), the origin and source integrability gaps, and the cutoff quantities, not just the two Hölder gaps.

The proof avoids exponentiating a large *bound* for \(\int|k|\). It retains the reference \(g_0\) as an input and exponentiates only uniformly small relative perturbations. It does not assert that the actual reference values of \(g_0\) cannot contain an exponential of a reconstruction integral. For a polynomial fit, the displayed formula \(g_0=u^2H e^T/[A_0(1+u^2)]\) explicitly contains such an exponential. The report's stronger literal wording should be corrected.

## 7. Repair for the norm used in the report

If the norm instead uses \(R_\phi=v-\sum c_j\phi_j\), the integration estimates apply to \(R_\phi\), but (R3) must account for the \(u^9,u^{11}\) pieces of each \(\phi_j\). Put \(a_j=(11-j)/2\), \(b_j=(9-j)/2\). Valid replacement constants are
\[
Z_1^\phi=A_0^{-1}\max\left(
\left\{r^{j-1}+a_jr^8+b_jr^{10}:j=3,5,7\right\},
\frac{r^{6+\sigma}}{(6+\sigma)(7+\sigma)}\right),
\]
\[
D_1^\phi=A_0^{-1}\max\left(
\left\{(j-1)r^{j-1}+8a_jr^8+10b_jr^{10}:j=3,5,7\right\},
\frac{(8+\sigma)r^{6+\sigma}}{(6+\sigma)(7+\sigma)}\right),
\]
\[
J_1^\phi=A_0^{-1}\max\left(
\left\{j(j-1)r^{j-3}+72a_jr^6+110b_jr^8:j=3,5,7\right\},
r^{4+\sigma}\right). \tag{R11}
\]
These follow term by term from the algebra norm; cancellation is not needed. Every later argument in this proof is unchanged after replacing those three constants and recomputing their dependents.

For \(r=1/2,\sigma=1\), their maxima are attained at \(j=3\), giving
\[
A_0Z_1^\phi=275/1024,\quad
A_0D_1^\phi=335/512,\quad
A_0J_1^\phi=1509/128.
\]
The accompanying exact-rational calculation makes precisely this repair to the audited scalar certificate. Outward bounds are:

| Quantity | Computed parameters, stated widths | \(A_0=4\), stated widths | \(A_0=4\), fixed parameters |
|---|---:|---:|---:|
| lower bound for \(\delta_0\) | 0.10269550 | 0.04009823 | 0.04070887 |
| upper bound for \(M\) | 2587 | 7051 | 6503 |
| upper bound for \(M_e\) | 95521 | 74297 | 68419 |
| upper bound for \(D_N\) | 12519 | 86597 | 79863 |
| upper bound for \(K_{Av}\) | 13841 | 198144 | 179692 |
| upper bound for \(K_{ev}\) | 465069 | 926433 | 840343 |
| upper bound for \(R_{vv}\), also \(C_2\) | 245246 | 4384989 | 3923610 |
| lower bound for radius (32) | \(1.8749\,10^{-6}\) | \(8.0690\,10^{-8}\) | \(1.4814\,10^{-7}\) |
| valid simple radius | \(10^{-6}\) | \(10^{-8}\) | \(10^{-7}\) |

“Stated widths” means \(h=0.06,h'=0.0003\), with \(\theta=0.9\), \(\tau=1\) at the computed reference and \(\tau=0.5\) at \(A_0=4\). Pure parameter constants and the lower bound for \(|B_0|\) are unchanged by this repair.

## Scope

This validates an explicit local functional estimate in either clearly specified norm. It neither estimates the distance of the stored numerical trace in these norms nor proves the PDE endpoint input. The repaired numbers are conservative bounds, not estimates of the actual Hessian or optimal dual norm.
