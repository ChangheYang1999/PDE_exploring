# Weaker norms and explicit radii

**Status.** The necessity of the report's full norm \(X\) is **REFUTED**. A plain \(C^2\) tail norm is also **REFUTED** as a sufficient replacement. The norm (12), the modulus extension below, and the exclusion radii in this file are **CONFIRMED**. An optimal dual norm, or a uniquely “weakest” norm without specifying an ordered family of spaces, is not established or asserted.

Dependencies are the differential in `01-differential/PROOF.md` and the quantitative remainder in `02-remainder/PROOF.md`. All constants referred to below are defined there.

## 1. What regularity is actually needed

The origin part of (12) controls only the second derivative of the remainder. The missing first and zeroth derivatives follow by integration, so this simplification is equivalent to the corresponding origin part of \(X\), up to explicit factors in (13). One may choose any \(\sigma>b_+\), however close to \(b_+\); choosing \(\sigma=1\) is convenient, not necessary.

The tail condition is strictly weaker than a full \(C^{2,\theta}\) norm. It only compares \(v''(u)\) to its endpoint value. For example, a function whose second derivative near 1 is
\((1-u)^\theta\sin((1-u)^{-p})\), \(p>0\), has the required endpoint bound and can be smooth on the open interval, but need not be \(C^{0,\theta}\) in its second derivative over pairs of points. Integrate twice from 1 and cut off away from 1 to obtain a compatible direction. This proves strict weakening within the admissible class.

A larger family is covered by precisely the same proof. Let \(\omega:(0,\ell]\to(0,\infty)\) be increasing, continuous, tending to zero at zero, and suppose
\[
L_\omega=\sup_{0<s\le\ell}\frac{s}{\omega(s)}<\infty,\qquad
I_\omega=\int_0^\ell \omega(s)s^{b_--2}\,ds<\infty.             \tag{29}
\]
Replace the last term of (12) by
\[
\sup_{r\le u<1}\frac{|v''(u)-v''(1)|}{\omega(1-u)}.
\]
In the proof of the second-order estimate replace every \(\ell^{1-\theta}\) by \(L_\omega\), the averaging gain \(1/(1+\theta)\) by 1, \(I_t\) by \(I_\omega\), and every reference endpoint seminorm by its \(\omega\) version. All other formulas are unchanged. To check this assertion, the only properties of the old modulus used in that proof were the product inequality, \(s\le \ell^{1-\theta}s^\theta\), the estimate of the average of the modulus, and the final tail integral. The replacements give exactly those four statements; monotonicity gives \(\omega(ts)\le\omega(s)\). Thus this is a proved extension, not an appeal to an unspecified continuity theorem.

For example,
\[
\omega(s)=\frac{s^{1-b_-}}{\log(e/s)^2}
\]
satisfies (29), since the last integral becomes
\(\int_0^\ell ds/[s\log(e/s)^2]\). This permits a weaker endpoint modulus than every power \(s^\theta\) with \(\theta>1-b_-\). The exponent 2 on the logarithm can itself be replaced by any number greater than 1. There is therefore no least choice even in this logarithmic subfamily. The absolute-integral condition (29), rather than a particular Hölder exponent, is the endpoint condition of this method. The complex buffer makes \(b_-\) slightly smaller than the real minimum exponent; it can be chosen arbitrarily small subject to positive margins. A real-derivative proof could instead work directly with real endpoint weights and two logarithmic moments, but no separate numerical certificate for that variant is claimed here.

### Why a bare \(C^2\) norm fails

Take a smooth compatible reference and a direction supported near 1 with
\[
v''(1-s)=s^\gamma,\qquad 0<\gamma\le1-\beta.
\]
Integrate twice from the endpoint and multiply \(v\) by a cutoff that is one near 1 and zero on a neighborhood of 0. It is a compatible \(C^2\) direction. Arbitrarily small multiples preserve negativity and the source conditions. For the perturbed trace, the nonsmooth leading term in \(Q(1-s)-Q(1)\), to first order in its amplitude, has coefficient
\[
\left(\frac{1}{2A(\gamma+1)g_*^2}-\frac{e}{2g_*^3}\right)s^\gamma.       \tag{30}
\]
Indeed, the corresponding increment in \(j\) is \(s^\gamma/(\gamma+1)\), the increment in \(a\) is \(O(s^{\gamma+1})\), and the endpoint increment of \(g\) is \(O(s^{\gamma+1})\). The constant change of \(g_*\) only changes smooth reference terms. Formula (30) follows from \(Q=(kg^{-2}-ew''g^{-3})/2\). Choose \(\gamma\) away from the at most one cancellation value. The same coefficient stays nonzero at sufficiently small nonzero amplitudes, by continuity of \(g_*\).

Since \(K\asymp s^{\beta-2}\), the defining integral then contains a nonzero multiple of
\(\int_0 s^{\gamma+\beta-2}\,ds\), which diverges. Thus \(C^2\)-smallness alone does not even make \(\mathcal B\) a finite-valued map on a neighborhood.

At a reference satisfying
\[
e\ne \frac{g_*}{A(2-\beta)},                                \tag{30a}
\]
failure also holds if one restricts to directions smooth through the source. This includes both rational references evaluated here. To see it, choose a nonnegative smooth \(\varphi\), supported in \((1,2)\), and prescribe
\(v_\epsilon''(1-s)=\varphi(s/\epsilon)\) near the source. Integrate twice from 1 and cut \(v_\epsilon\) off at a fixed distance from 1. Its \(C^2\) norm stays bounded; it vanishes near zero and is smooth through 1. The leading local terms in the derivative are
\[
\frac{1}{2Ag_*^2s}\int_0^s v_\epsilon''(1-t)\,dt
 -\frac{e}{2g_*^3}v_\epsilon''(1-s).
\]
Interchanging the first integral with the weight \(s^{\beta-2}\) gives, to leading order, the coefficient
\[
\frac{1}{2Ag_*^2(2-\beta)}-\frac{e}{2g_*^3}
\]
times
\(\epsilon^{\beta-1}\int_1^2\varphi(t)t^{\beta-2}\,dt\), multiplied by the nonzero reference prefactor \(\kappa A^{\beta-2}g_*^{1-\beta}\). The remaining terms have at least one extra factor of \(s\), or arise from the fixed remote cutoff, and are \(o(\epsilon^{\beta-1})\). For example \(\delta a=O(\epsilon)\), \(\delta j=O(\min(1,\epsilon/s))\), and the endpoint-subtracted logarithmic reconstruction is the integral of these bounded quotient variations; these estimates give the claimed lower order after integration. Under (30a) the derivative therefore grows without bound in a bounded \(C^2\) set. The isolated cancellation of this leading coefficient is not claimed to restore a \(C^2\) neighborhood for the nonlinear functional.

### The origin threshold

For compactly supported variations approaching the origin, integrating the leading \(v''\) term in (6) twice gives
\[
\lambda(u)\sim
\frac{e(1-\beta)(6+\beta)(7+\beta)}{6A}\,u^{-8-\beta}.          \tag{31}
\]
The other terms are lower order. Notice the factor \(e\), required by the normalized coordinates.

Let \(\phi\ge0\) be a nonzero smooth function supported in \((1,2)\), and
\(v_t(u)=t^{7+\beta}\phi(u/t)\). Then \(D\mathcal B(v_t)\) tends to a nonzero constant, whereas
\[
\sup u^{-5-\sigma}|v_t''(u)|=O(t^{\beta-\sigma}).
\]
Thus weights with \(\sigma<\beta\) do not bound the derivative. At \(\sigma=\beta\), sums of finitely many disjoint, geometrically separated such bumps have uniformly bounded weighted supremum and unbounded derivative: choose the scales small enough that every response has the same sign and a fixed positive lower bound. Every finite sum is smooth and zero near zero. This proves failure of the critical unmodified supremum weight too. Integrated weights or logarithmic improvements are possible; discarding the singular origin control is not.

## 2. Radius formula

Let \(b_0>0\) be a certified lower bound for \(|\mathcal B(A_0,e_0,w_0)|\), and let \(D_A,D_e\) bound the absolute values of the two reference parameter derivatives (9)–(10). Define
\[
P=D_Ah+D_eh'+\tfrac12K_{AA}h^2+K_{Ae}hh',\qquad
m=b_0/2-P,
\]
\[
D=D_N+K_{Av}h+K_{ev}h'.
\]
If \(m\le0\), these bounds give **no positive radius**. If \(m>0\), one possible radius is
\[
\boxed{\varepsilon(h,h')=
\min\left\{\delta_0,\frac{m}{2(D+R_{vv}\delta_0)}\right\}.}     \tag{32}
\]
It uses only rational operations in the specified constants. The sharper quadratic-root choice is
\[
\min\left\{\delta_0,
\frac{2m}{D+\sqrt{D^2+4R_{vv}m}}\right\},                     \tag{33}
\]
with an open trace ball. Formula (32) has an extra strict margin even for a closed ball.

Proof: (27) and the first differential give
\[
|\mathcal B-\mathcal B_0|\le P+Dt+R_{vv}t^2.
\]
If \(t\le\delta_0\), its last two terms are at most
\((D+R_{vv}\delta_0)t\). Substitution of (32) makes this at most \(m/2\), strictly below \(m\). This proves
\[
|\mathcal B-\mathcal B_0|<|\mathcal B_0|/2.
\]

Using only the single constant \(C_2\) in (28) would instead give the parameter budget
\(D_Ah+D_eh'+C_2(h+h')^2\). For the numerical constants below that budget is too large, and its radius is zero. This is a loss in the isotropic packaging of the estimate, not a counterexample to exclusion. Formula (27), which proves the requested estimate, retains the information needed for (32).

## 3. Proved rational certificates for the two rational references

Take \(r=1/2,\sigma=1,\theta=9/10\) throughout. These put the origin cutoff away from the highly singular small-\(u\) layer while leaving simple analytic reference bounds. They satisfy (15) with \(\tau=1\) for \(A_0=10.150725,h=0.06\), and with \(\tau=1/2\) for \(A_0=4,h\le0.06\).

The file `verification/rational_certificate.py` uses exact `Fraction` arithmetic for every inequality. It writes all constants, both as exact rational numbers and as outward decimal bounds, to `verification/rational_bounds.json`. No sampled supremum or floating-point quadrature is used in these certificates.

Here are convenient outward bounds from that computation:

| Quantity | \(A_0=10.150725,\ e_0=0.0135206\) | \(A_0=4,\ e_0=1/16\) |
|---|---:|---:|
| \(h,h'\) | \(0.06,\ 0.0003\) | \(0.06,\ 0.0003\) |
| allowable \(\delta_0\), lower bound | \(0.1046\) | \(0.04085\) |
| \(M\), upper bound | 2577 | 6962 |
| \(M_e\), upper bound | 95058 | 73293 |
| \(D_N\ge\|D_w\mathcal B\|_{N^*}\) | 12240 | 83924 |
| \(K_{Av}\) | 13532 | 192028 |
| \(K_{ev}\) | 454269 | 897034 |
| \(R_{vv}\), hence a valid \(C_2\) | 235346 | 4171171 |
| \(K_{AA}\) | 0.052053 | 0.468711 |
| \(K_{Ae}\) | 3.187433 | 3.831090 |
| \(D_A\) | 0.109429 | 0.368446 |
| \(D_e\) | 30.632175 | 12.180000 |
| proved \(b_0\), lower bound | 0.321857 | 0.141975 |
| formula (32), lower bound | \(1.9177\,10^{-6}\) | \(8.3260\,10^{-8}\) |
| simple proved radius | \(\boxed{10^{-6}}\) | \(\boxed{10^{-8}}\) |

The lower bounds for (32) use the exact constants in the JSON, not recomputation from the coarser display table. At \(A_0=4,e_0=1/16,h=h'=0\), the same proof gives (32) greater than \(1.5279\,10^{-7}\), so \(\varepsilon=10^{-7}\) is proved. This is a substantial improvement over \(\exp(-10^7)\), but the coordinates and norm are different: these are normalized traces on \([0,1]\), with (12). They should not be described as the radius of the earlier physical-coordinate \(X\)-ball.

### Why the reference bounds used in the code are analytic bounds

Write \(R=r^2=1/4\). For the rational reference,
\[
z_0=\frac{1-u^2}{1+u^2},\quad E_0=-\log(1-u^2),\quad
D_0=-\frac{4u^2}{(1+u^2)^2},\quad
J_0=-\frac{4(3-u^2)}{(1+u^2)^3}.
\]
The absolute power-series sums give
\[
Z,n\le\frac{1+R}{1-R},\quad
D\le\frac{4R}{(1-R)^2},\quad
J\le\frac{4(3+R)}{(1-R)^3},\quad
E_o\le\frac{R}{1-R}.
\]
For the last inequality use \(-\log(1-R)=\sum R^j/j\le R/(1-R)\). The series sums bound (16) since every omitted power is at least \(u^6\).

On \([r,1]\),
\[
a_*=\frac{A_0r(1+r)}{1+r^2},\quad
K_0=\frac2{r(1+r^2)},\quad
H_a\le\frac{2A_0}{(1+r^2)^2},\quad
H_k\le\frac{2(1+3r^2)}{r^2(1+r^2)^2}.
\]
The bounds for \(H\) follow by bounding the derivative and using
\((1-u)^{1-\theta}\le1\). The derivative of \(a_0/A_0\) is
\((1+2u-u^2)/(1+u^2)^2>0\), proving the stated minimum.
Furthermore,
\[
S_w=\frac{4A_0r(3-r^2)}{(1+r^2)^3},\quad
H_w\le\frac{12A_0(1+6r^2+r^4)}{(1+r^2)^4},
\]
\[
S_p=\frac{(1+r^2)^p}{r^{2p}},\quad
H_p\le\frac{2p(1+r^2)^{p-1}}{r^{2p+1}}\quad(p=2,3).
\]
Indeed \(w_0''=4A_0u(3-u^2)/(1+u^2)^3\) decreases for \(u\ge1/2\). For its derivative, the positive upper majorant
\((1+6t+t^2)/(1+t)^4\) decreases for \(t\ge1/4\), since its derivative has numerator \(2-16t-2t^2<0\). The derivatives of \(g_0^{-p}=(1+u^2)^p/u^{2p}\) have maximal magnitude at \(r\).
The weight in (18) is
\[
u^{-b}(1+u)^{b-2}(1+u^2).
\]
It decreases in \(u\in(0,1]\) and increases in \(b\in(0,1)\). The first assertion follows by writing it as
\((1+u^2)/(1+u)^2\) times \((1+1/u)^b\), both decreasing. Therefore the code's rational majorant
\(W_0\le(1+r^2)/(r(1+r))\) is valid. It also replaces \(r^{-4-b_+}\) by \(r^{-5}\), and the positive powers of \(r,\ell\) in \(I_o,I_t\) by 1. Thus all expressions become rational.

For the small parameter constants, put
\[
I_n(\beta)=\mathrm B(n-\beta/2,\beta),\quad
P_5=5/(6A)-5e,\quad P_3=1/(2A)+e.
\]
The exact rational-family identity is
\[
\mathcal B=P_5 I_3+P_3 I_2.                                  \tag{34}
\]
Here is a derivation, including the finite-part step. Direct substitution gives
\[
Q=(1-6Ae)u^{-5}+(1+2Ae)u^{-3},\qquad
m=A(1-u^2)/u.
\]
Integration by parts in (1) gives
\[
\mathcal B=\frac1{3A}\operatorname{FP}\int_0^1
Q'(u)u^{1-\beta}(1-u^2)^{\beta-1}\,du.
\]
There is no constant boundary term at zero, because the singular powers are nonintegral; at 1 use \(Q-Q(1)=O(1-u)\) before taking the boundary limit. Substituting \(t=u^2\) gives beta finite parts
\(\frac12\mathrm B(-2-\beta/2,\beta)\) and
\(\frac12\mathrm B(-1-\beta/2,\beta)\).
The recurrence
\(\mathrm B(x+1,\beta)=x\,\mathrm B(x,\beta)/(x+\beta)\)
follows by integrating a derivative; it also holds for these finite parts by the same cutoff subtraction. Applying it five times and three times, respectively, gives
\[
\mathrm B(-2-\beta/2,\beta)=-\mathrm B(3-\beta/2,\beta),
\qquad
\mathrm B(-1-\beta/2,\beta)=-\mathrm B(2-\beta/2,\beta).
\]
All denominators are nonzero for \(0<\beta<1\). These two identities prove (34). They also explain the convergent positive-power integral used by the numerical code. Finally
\(I_3/I_2=(4-\beta)/(4+\beta)\), so collecting the constant and \(e\) terms yields the formula for \(\mathcal B_0\) below with
\[
S_A=\frac{6A(4A-3)}{8A-1}.
\]

Let \(b_l=2/A_+\), \(b_h=2/A_-\), \(p=n-1-b_h/2\). The code uses the proved bounds
\[
I_n\le b_l^{-1},\quad
|I_n'|\le b_l^{-2}+(p+1)^{-2}+(b_l+1)^{-1},
\]
\[
|I_n''|\le4b_l^{-3}+2(p+1)^{-3}+2(b_l+2)^{-1}.                \tag{35}
\]
To verify them, differentiate the beta integral and put
\(L(t)=\log(1-t)-\frac12\log t\). Bound \(t^p\le1\) for the \(\log(1-t)\) moments. For the \(\log t\) moments split at \(1/2\): on the first half \((1-t)^{b_l-1}\le2\), and on the second \(-\log t\le2(1-t)\). Integrate the elementary moments after extending each half to \([0,1]\). For the second derivative use
\((|\log(1-t)|+\frac12|\log t|)^2\le2|\log(1-t)|^2+\frac12|\log t|^2\).
This proves (35), including its constants. The product rule applied to (34) now gives exactly the \(K_{AA},K_{Ae},D_A,D_e\) formulas in the code.

Finally,
\[
\mathcal B_0=
\frac{16-\beta_0}{3A_0(4+\beta_0)}
\mathrm B(2-\beta_0/2,\beta_0)(1-S_{A_0}e_0).
\]
Here \(1-S_{A_0}e_0>0\), and \(t^{1-\beta_0/2}\ge t\) implies
\[
\mathrm B(2-\beta_0/2,\beta_0)\ge\frac1{\beta_0(1+\beta_0)}.
\]
This gives the rational lower bound \(b_0\). The script verifies the final exclusion inequality by exact rational comparison.

## 4. Numerical conditioning evidence and its limits

`verification/numerical_checks.py` evaluates (34) and the one-dimensional integral obtained by integrating the polynomial subtraction by parts, at 65-digit working precision. These are two formulas implemented in the same code, not two independently authored codes. They agree to more than 55 decimal places:

| Reference | \(\mathcal B_0\), numerical | \(B_A\), numerical | \(B_e\), numerical |
|---|---:|---:|---:|
| \(10.150725,\ 0.0135206\) | 0.325795091172477577 | -0.015121738732642729 | -15.152547371000407 |
| \(4,\ 1/16\) | 0.153095696660659004 | -0.065147161847025660 | -4.153552813750053 |

For \(L=8.6000638\) instead of the exact decimal \(e=0.0135206\), the first value is \(0.325794766045071107\). For \(L=8.6\) it is \(0.325791726307171718\). None of these floating-point evaluations is needed for the rational certificates above.

At the first reference the three polynomial directions \(\phi_j\) from (7) give, numerically,
\[
D\mathcal B(\phi_3)=0.8291351718,\quad
D\mathcal B(\phi_5)=0.4843139593,\quad
D\mathcal B(\phi_7)=0.2149083399.
\]
They are computed by differentiating the original finite-part formula. For these polynomial directions \(\eta_v\) is a polynomial, the remaining integrand is a finite Laurent polynomial times \(u^{1-\beta}(1-u^2)^{\beta-1}\), and each monomial has the finite-part moment
\(\frac12\mathrm B((p+2-\beta)/2,\beta)\).
Exact rational Bernstein bounds give respectively
\(\|\phi_j\|_N\le1111.75,633.5,259.25\).
Thus these tests suggest the numerical lower bound
\[
8.28\,10^{-4}\ \lesssim\ \|D\mathcal B\|_{N^*}
\ \le\ 12240.                                                \tag{36}
\]
The right inequality is proved; the left is numerical evidence. This is deliberately an honest, wide bracket, not a sharp numerical estimate of the dual norm. Determining that norm accurately remains an optimization problem. The exclusion does not require solving it.

The very large responses in §6.3.2(c) are consistent with (36). For the source-cutoff lognormal bump centered at physical \(x=1\), its flat origin jet is zero. Sampling only the origin term of (12) already gives
\[
\|v\|_N\gtrsim8.08\,10^9\quad(\text{width }0.3),\qquad
\|v\|_N\gtrsim4.28\,10^{14}\quad(\text{width }1).
\]
The maximizing sampled points are \(u\approx0.0691\) and \(0.002707\); the remote source cutoff equals one there. The reported responses \(6.37\,10^4\) and \(1.31\,10^9\) divided by these lower bounds are at most about \(7.9\,10^{-6}\) and \(3.1\,10^{-6}\), respectively. A unit relative bump amplitude is therefore very far from a unit \(N\)-perturbation. The large raw responses do not contradict a bounded derivative in \(N\); they demonstrate why an unweighted fit error is inadequate.
