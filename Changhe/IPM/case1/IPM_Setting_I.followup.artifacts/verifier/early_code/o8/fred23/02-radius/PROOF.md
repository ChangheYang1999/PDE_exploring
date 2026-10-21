# The inventory and certified exclusion radii

**Question (2): CONFIRMED.** In the norm of fred22/02-remainder, equation (12), the following closed-ball radii are proved:

$$
\varepsilon=4.5\,10^{-6}\quad(h=0.06,\ h'=0.0003),\qquad
\varepsilon=5\,10^{-6}\quad(h=h'=0).
\tag{1}
$$

These are sufficient radii, not optimal radii or estimates of the actual dual norm.

## Statement and remainder convention

Take \(r=1/2\), \(\sigma=1\), \(\theta=9/10\),
\(v=w-(A/A_0)w_0\), with \(v'(0)=v(1)=v'(1)=0\). Let \(c_3,c_5,c_7\) be its Taylor coefficients and put

$$
R_v=v-c_3u^3-c_5u^5-c_7u^7,\qquad
\|v\|_N=\sum|c_j|+\sup_{0<u\le1/2}u^{-6}|R_v''|
+\sup_{[1/2,1]}|v''|
+\sup_{1/2\le u<1}\frac{|v''(u)-v''(1)|}{(1-u)^{9/10}}.
\tag{2}
$$

This is the actual convention in the earlier equation (12). Subtracting \(\sum c_j\phi_j\) instead gives a different norm, dealt with explicitly at the end.

**Functional theorem.** If \(w\) is compatible, smooth on \((0,1)\), has the origin expansion and endpoint modulus in (2), and satisfies either parameter/radius alternative (1), then

$$
\mathcal B(A,e,w)>7/50=0.14.
\tag{3}
$$

The PDE consequence is separate.

## The estimate being applied

The dependency is the reference-relative theorem in fred22/02-remainder, copied in full to [verification/reference_estimate.md](verification/reference_estimate.md); its source digest is recorded. It gives, for \(a=|A-A_0|\), \(b=|e-e_0|\), \(t=\|v\|_N\le\delta_0\),

$$
|\mathcal B-B_0-B_A\Delta A-B_e\Delta e-D_w\mathcal B(v)|
\le\tfrac12K_{AA}a^2+K_{Ae}ab+K_{Av}at+K_{ev}bt+R_{vv}t^2,
\tag{4}
$$

with \(\|D_w\mathcal B\|\le D_N\). Here \(B_A\) is the fixed-shape derivative.

For clarity, its mechanism is a bound \(|\mathscr H|\le M\),
\(|\partial_e\mathscr H|\le M_e\) for
\(\mathscr H(A,e,\zeta)=\mathcal B(A,e,(A/A_0)(w_0+\zeta))\)
on a complex trace ball of radius \(d\) and an \(A\)-buffer \(\tau\). The reconstruction satisfies
\(|\log(g/g_0)|\le H_gd\le1/12\). The integrable endpoint majorants are \(u^{\sigma-\Re\beta-1}\) and \((1-u)^{\theta+\Re\beta-2}\). Consequently Cauchy's formula gives

$$
D_N=M/d,\quad K_{Av}=\rho_+(M/d)(1/\tau+1/A_-),\quad
K_{ev}=\rho_+M_e/d,\quad R_{vv}=4\rho_+^2M/d^2,
\tag{5}
$$

where \(\rho_+=A_0/A_-\), \(\delta_0=d/(2\rho_+)\).
The full explicit arithmetic formulas for \(d,M,M_e\) are equations (19)–(23) of the copied proof and are implemented locally in `radius.py`. The proof estimates reconstruction relative to \(g_0\); it does not exponentiate a large reference bound.

## All reference inputs

Choose \(\tau=1\). Set \(A_m=A_0-h-1\), \(A_M=A_0+h+1\),
\(b_-=2/A_M\), \(b_+=2/A_m\). Exact comparisons prove
\(e_0-h'>0\), \(A_m>2\), \(\sigma>b_+\), and \(\theta+b_->1\) for both alternatives.

The origin algebra is

$$
\|F\|_{\mathcal A}=|F_0|+|F_2|r^2+|F_4|r^4+
\sup_{0<u\le r}\frac{|F-F_0-F_2u^2-F_4u^4|}{(u/r)^5}.
$$

On the tail write \(S(F)=\sup|F|\), \(H(F)=\sup|F(u)-F(1)|/(1-u)^\theta\).
The complete inventory is below. Every entry is a **proved rational bound**; bounds are upper unless labeled otherwise.

| Input | Bound |
|---|---:|
| \(H_{\min}\), \(\inf[-w_0/(u(1-u))]\), lower | \(A_0\) |
| \(H_{\max}\) | \(11\) |
| \(Z=\|z_0\|_{\mathcal A}\), \(n=\|z_0^{-1}\|_{\mathcal A}\) | \(1.84,\ 1.89\) |
| \(D=\|uz_0'\|_{\mathcal A}\) | \(2.43\) |
| \(J=\|-w_0''/(A_0u)\|_{\mathcal A}\) | \(47.11\) |
| \(E_o=\|-\log(1-u^2)+T(u^2)\|_{\mathcal A}\) | \(0.246\) |
| \(a_*=\inf[-w_0/(1-u)]\), lower | \(6.090435\) |
| \(H(a_0)\) | \(13.24\) |
| \(S(k_0)\), \(H(k_0)\), \(k_0=g_0'/g_0\) | \(3.18,\ 9.78\) |
| \(S(w_0'')\), \(H(w_0'')\) | \(31.53,\ 123.51\) |
| \(g_*\), lower; \(\inf_{[r,1]}g_0\), lower | \(2/5;\ 4/25\) |
| \(S(g_0^{-2})\), \(H(g_0^{-2})\) | \(39.0625,\ 248.4375\) |
| \(S(g_0^{-3})\), \(H(g_0^{-3})\) | \(244.140625,\ 2329.1015625\) |
| \(W_0=\max_{b=b_\pm}\sup(a_0/A_0)^{b-2}g_0^{1-b}\) | \(25/9\) |
| \(w_0''(1)\), exact | \(0.7768297940321664\) |
| \(D_A,D_e,K_{AA},K_{Ae}\) | \(0.007,\ 7.1,\ 0.007,\ 1.85\) |
| \(b_0\), lower bound for \(B_0\) | \(7/25\) |

The exact formula \(k_0(1)=w_0''(1)/A_0\) and the enclosure of
\(Q_0(1)=w_0''(1)/(2A_0g_*^2)-e_0w_0''(1)/(2g_*^3)\)
are also supplied by the preceding certificate (`Q1_components` stores the two components). No endpoint datum is imported from a numerical reconstruction.

### Origin bounds, including remainders

For \(R=r^2\), \(\|F(u^2)\|_{\mathcal A}\le\sum|F_k|R^k\) for an absolutely convergent series in \(t=u^2\): every omitted power has \(2k\ge6>5\).
Write \(z=z_R+z_p\), where \(z_R=(1-t)/(1+t)\),
\(z_p=-t(1-t)^2q/A_0\), and \(Q_R=\sum|q_k|R^k\). Then

$$
Z\le\frac{1+R}{1-R}+\frac{R(1+R)^2Q_R}{A_0},\qquad
n\le\frac{1+R}{1-R}
\left(1-\frac{R(1+R^2)Q_R}{A_0}\right)^{-1}.
$$

The inverse bound is the convergent geometric series for \(A_0/H\).
For \(D\), use \(4R/(1-R)^2+\sum2k|(z_p)_k|R^k\).
For \(J\), use \(4(3+R)/(1-R)^3\) plus the coefficient sum of
\(-p''(u)/(A_0u)\), \(p=u^3(1-u^2)^2q(u^2)\).

For \(E\), series division gives the first 40 coefficients of \(1/z\) exactly; the \(t^k\) coefficient of \(E\) is \([t^k](1/z)/(2k)\) for \(k\ge1\).
At \(S=1/3\), the absolute coefficient sum of \(E\) is bounded by

$$
\frac{S}{1-S}+
\frac{S(1+S)^2Q_S}{2A_0[1-S(1+S^2)Q_S/A_0]}.
$$

The denominator is positive. Multiplying by \((R/S)^{40}\) bounds the omitted tail at \(R=1/4\). This gives the rational upper bound \(E_o\le0.246\), and hence \(\Gamma_0=1-(2+b_+)E_o>0\). Thus every origin norm includes a bound on its whole remainder.

### Tail bounds

Since \(H\ge A_0\), \(a_0=u(1+u)H(u^2)/(1+u^2)\) is bounded below by
\(A_0r(1+r)/(1+r^2)\). The rational factor is increasing because its derivative has positive numerator \(1+2u-u^2\).

The code encloses \(a_0'\), \(k_0\), \(k_0'\), \(w_0''\), and \(w_0'''\) by interval jets of their rational formulas on each of 128 complete subintervals of \([r,1]\). It uses

$$
k_0=2/u+2u\left(H'(u^2)/H(u^2)-1/(1+u^2)+T'(u^2)\right).
$$

All divisions avoid zero; every interval bound is rounded upward to a rational hundredth. The mean value theorem gives \(H(F)\le\sup|F'|\).

The first certificate gives \(e^{T(1)}>4/5\), and \(q<0\) gives
\(T(1)\le T(t)\le0\). Therefore
\(g_0(u)\ge(4/5)u^2/(1+u^2)\), whereas
\(g_0(u)\le H_{\max}/(2A_0)<1\).
It follows that \(g_{\min}\ge4/25\),
\(S_p\le g_{\min}^{-p}\), and \(H_p\le pK_0S_p\).
Since \(a_0/A_0\ge3/5\), \(g_0\le1\), \(0<b_\pm<1\), also \(W_0\le25/9\).
The obstruction and four parameter derivative bounds come from the first proof. This completes the requested inventory.

## Exact radius calculation

[verification/radius.py](verification/radius.py) evaluates the explicit remainder theorem using `Fraction`, replacing cutoff powers by the rational majorants allowed in that theorem. [verification/radius_certificate.json](verification/radius_certificate.json) records **all intermediate and final constants as exact fractions**. Useful outward bounds are:

| Constant | varying parameters | fixed parameters |
|---|---:|---:|
| \(d\), lower | \(0.2005\) | \(0.2005\) |
| \(\delta_0\), lower | \(0.0997\) | \(0.1002\) |
| \(M\), upper | \(5616\) | \(5429\) |
| \(M_e\), upper | \(232055\) | \(226640\) |
| \(D_N\), upper | \(27993\) | \(27063\) |
| \(K_{Av}\), upper | \(30950\) | \(29729\) |
| \(K_{ev}\), upper | \(1163734\) | \(1129860\) |
| \(R_{vv}\), upper | \(564862\) | \(539662\) |
| valid \(C_2\), upper | \(581867\) | \(564930\) |

Here \(C_2=\max(K_{AA}/2,K_{Ae}/2,K_{Av}/2,K_{ev}/2,R_{vv})\); in these cases it need not equal \(R_{vv}\).

Equation (4) gives

$$
|\mathcal B-B_0|\le P+(D_N+K_{Av}h+K_{ev}h')t+R_{vv}t^2,\quad
P=D_Ah+D_eh'+K_{AA}h^2/2+K_{Ae}hh'.
$$

For the varying parameters \(P=0.0025959\). At \(t=4.5\,10^{-6}\), the displayed upper constants give

$$
0.0025959+30199.1202(0.0000045)+564862(0.0000045)^2
=0.1385033793555<0.14.
$$

For fixed parameters, \(t=5\,10^{-6}\) gives

$$
27063(0.000005)+539662(0.000005)^2
=0.13532849155<0.14.
$$

Both \(t\)'s are below the proved \(\delta_0\). Since \(B_0>0.28\), (3) follows. These are strict rational inequalities on closed balls. Using the quadratic budget directly improves on the conservative radius formula (32) in fred22 without changing its theorem.

## Alternative compatible-remainder norm

If \(R_v\) instead means \(v-\sum c_j\phi_j\), call the resulting norm \(N_\phi\). The next proof establishes
\(\|v\|_N\le(415/4)\|v\|_{N_\phi}\).
Thus exact certified radii in that convention are

$$
\varepsilon_\phi=\frac4{415}(4.5\,10^{-6}),\qquad
\varepsilon_\phi=\frac4{415}(5\,10^{-6}),
$$

approximately \(4.33735\,10^{-8}\), \(4.81928\,10^{-8}\).
The exact expressions define the balls; no radius is silently transferred between remainder conventions.
