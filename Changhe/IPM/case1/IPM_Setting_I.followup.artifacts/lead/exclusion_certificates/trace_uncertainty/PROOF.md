# Trace distances and what samples can establish

**Question (3): CONFIRMED** for the comparisons and the conditional analytic estimate below. **REFUTED** is the implication that agreement with samples away from the origin, by itself, places a compatible trace in the exclusion ball. **UNCLEAR** is whether an exact IPM profile near the numerical trial satisfies any quantitative hypothesis that would place it there.

The distances and obstruction differences in the first table are numerical, without a certified error bound. The jet lower bounds, the norm conversion, the analytic estimate, and the interval evaluations of that estimate are proved.

## Definitions and alignment

Use \(A_0=10.150725\), \(e_0=8.6000638^{-2}\), \(r=1/2\), \(\sigma=1\), and \(\theta=9/10\). For a compatible difference \(v\), let \(c_3,c_5,c_7\) be its coefficients at zero. Define

$$
N_{\rm raw}(v)=\sum|c_j|
+\sup_{0<u\le1/2}u^{-6}|(v-c_3u^3-c_5u^5-c_7u^7)''|
+\sup_{[1/2,1]}|v''|
+\sup_{1/2\le u<1}\frac{|v''(u)-v''(1)|}{(1-u)^{9/10}}.
\tag{1}
$$

This is the norm of the earlier referee answer's remainder estimate ([../raw_bounds/02-remainder/PROOF.md](../raw_bounds/02-remainder/PROOF.md)), equation (12). If the remainder means subtraction of the compatible directions

$$
\phi_j=u^j+\frac{j-11}{2}u^9+\frac{9-j}{2}u^{11},
$$

replace the remainder in (1) by \(v-\sum c_j\phi_j\) and call the result \(N_\phi\). The distinction matters numerically; neither remainder convention is silently substituted for the other.

The lead JSON files use \(A_i=10.150725214760579\), slightly different from \(A_0\). Comparing their original traces in (1) is not defined as a comparison of compatible directions at the same \(A\). We therefore compare

$$
w_i^{\rm aligned}=(A_0/A_i)w_i^{\rm original}
=-A_0u(1-u^2)/(1+u^2)+u^3(1-u^2)^2(A_0/A_i)q_i(u^2).
\tag{2}
$$

Every obstruction below uses the common \(A_0,e_0\). The fitted trace already has this normalization. The original exact decimal strings and the numerical evaluator are copied under `verification/`. All three differences in (2) are odd polynomials and are compatible.

## Numerical comparison, with a separate exact conclusion

| First trace minus second | \(N_{\rm raw}\), numerical | \(N_\phi\), numerical | \(\Delta B\), numerical |
|---|---:|---:|---:|
| K12 minus K18 | 60.21334564 | 46.48554886 | -0.03216808067 |
| K12 minus fitted | 66.65219990 | 53.11771495 | -0.01659106177 |
| K18 minus fitted | 15.43032830 | 14.86439258 | +0.01557701891 |

The aligned obstruction values are, numerically,

$$
B_{\rm K12}=0.2674821674646158,\quad
B_{\rm K18}=0.2996502481374085,\quad
B_{\rm fitted}=0.2840732292314196.
$$

[verification/compare.py](verification/compare.py) evaluates polynomial derivatives using the exact coefficient strings, brackets stationary points on a 16385-point grid, refines the brackets, and evaluates all resulting extrema and endpoints. In particular it treats the near-source Hölder supremum separately; the maximizers in these three comparisons lie near \(u=0.999\). A grid does not certify that all stationary points were found. The obstruction evaluator uses 40-digit arithmetic and order 80 without a proved truncation error. Accordingly these results are numerical, not interval certificates, and printed digits do not assert that many digits of accuracy.

There is nevertheless an exact separation statement. In both norms the coefficient sum alone is a lower bound. Its exact values are

$$
\begin{array}{ll}
\mathrm{K12-K18}:&
\displaystyle\frac{151672617763777950633257011056171}
{303006722828674000000000000000000}>0.50,\\[4pt]
\mathrm{K12-fitted}:&
\displaystyle\frac{270308357916325440273656710126953}
{507536260738028950000000000000000}>0.53,\\[4pt]
\mathrm{K18-fitted}:&
\displaystyle\frac{666090278816278280225661751886267}
{20301450429521158000000000000000000}>0.032.
\end{array}
\tag{3}
$$

These follow by polynomial coefficient subtraction in (2) and rational arithmetic; `analytic_bounds.py` checks the stored fractions against the exact coefficient differences. Thus the references lie outside each other's tiny exclusion balls even without certifying a single supremum in the numerical table. Their simultaneous agreement with the stored trial is a premise of the question; this computation does not certify that agreement or the accuracy of the trial as a PDE solution.

## Relation between the two norm conventions

For \(j=3,5,7\), respectively,

$$
u^{-6}(\phi_j-u^j)''=
-288u+330u^3,\quad -216u+220u^3,\quad -144u+110u^3.
$$

These are negative on \(0<u\le1/2\). Their absolute values increase there, since their derivatives are respectively \(288-990u^2\), \(216-660u^2\), and \(144-330u^2\), all positive on that interval. Their maxima are \(411/4,161/2,233/4\). The triangle inequality now gives, in both directions,

$$
N_{\rm raw}(v)\le\frac{415}{4}N_\phi(v),\qquad
N_\phi(v)\le\frac{415}{4}N_{\rm raw}(v).
\tag{4}
$$

Only the origin remainder changes; its change is at most
\((411/4)\sum|c_j|\). Adding the unchanged terms proves (4).

Consequently the certified radii in the compatible-remainder convention are exactly

$$
\varepsilon_\phi=\frac4{415}(4.5\,10^{-6})
\quad\hbox{or}\quad
\varepsilon_\phi=\frac4{415}(5\,10^{-6}),
\tag{5}
$$

for varying or fixed parameters. They are approximately \(4.33735\,10^{-8}\) and \(4.81928\,10^{-8}\). Formula (5), not its decimal approximation, defines the radius. For a full inventory in this convention, multiply \(D_N,K_{Av},K_{ev}\) by \(415/4\), multiply \(R_{vv}\) by \((415/4)^2\), and divide \(\delta_0\) by \(415/4\); all other inputs remain unchanged. These operations preserve every inequality in the preceding proof.

## Why samples alone cannot bound either norm

Fix a nonzero nonnegative smooth function \(\chi\) with compact support in \((1,2)\). For \(0<d<0.01\), put

$$
v_d(u)=-d^3\chi(u/d)\quad(u\ge0)
$$

and extend it oddly. It vanishes near zero and near the source, so all its origin coefficients and compatibility defects vanish. Moreover \(w_0+v_d<0\) on \((0,1)\) and it agrees exactly with \(w_0\) on the entire interval \([0.02,1]\). But

$$
\sup_{0<u\le1/2}u^{-6}|v_d''(u)|
=d^{-5}\sup_{1<s<2}s^{-6}|\chi''(s)|\longrightarrow\infty.
\tag{6}
$$

The constant on the right is positive: a nonzero compactly supported function cannot have zero second derivative. Even uniform convergence of \(v_d\) to zero in value therefore gives no bound in either norm.

Qualitative analyticity is also insufficient for finitely many samples. Given positive sample locations \(u_i<1\), the entire compatible perturbation

$$
v_C(u)=-C u^3(1-u^2)^2\prod_i(u^2-u_i^2)^2,\qquad C>0,
\tag{7}
$$

vanishes at every sample, is nonpositive on \([0,1]\), and has
\(|c_3|=C\prod_i u_i^4\to\infty\). This remains true if the source endpoint is sampled. These are counterexamples among compatible traces, not constructions of exact IPM profiles. The PDE might impose additional quantitative restrictions, but none are supplied by sampled agreement.

## An explicit sufficient analytic hypothesis

Here is one completely quantitative way to close the missing implication. Let
\(a=0.02\), \(b=0.985\), \(c=(a+b)/2\), and \(h=(b-a)/2\). Let \(E_\rho\), \(\rho>1\), be the open Bernstein ellipse with foci \(a,b\), parametrized on its boundary by

$$
z=c+\tfrac h2(\rho e^{it}+\rho^{-1}e^{-it}).
$$

Assume that the **aligned error**
\(v=\widetilde w-(A/A_0)w_0\) is holomorphic on \(E_\rho\), continuous on its closure, real on the real interval, and satisfies

$$
|v|\le M\ \hbox{on }\overline E_\rho,\qquad
|v|\le\delta\ \hbox{on }[a,b],\qquad 0<\delta\le M.
\tag{8}
$$

Assume also compatibility and oddness near zero, as required for (1).
This is a hypothesis directly on the exact trace relative to a known reference. Alternatively a bound \(|\widetilde w|\le M_{\rm trace}\) on the same ellipse implies (8) with \(M=M_{\rm trace}+(|A|/A_0)M_0\), provided \(w_0\) is holomorphic there and \(M_0\) bounds it. For the ellipse \(E_4\) used below, one entirely explicit choice is

$$
M_0=
\frac{A_0R_z(1+R_z^2)}{(1-Y)^2}
+R_z^3(1+R_z^2)^2\sum_k|q_k|R_z^{2k},
\quad R_z=1.5278125,\quad Y=0.9046875.
$$

Indeed \(|z|\le R_z\), \(|\Im z|\le Y<1\) throughout \(E_4\), so the poles \(\pm i\) are outside it and \(|1+z^2|\ge(1-Y)^2\). These exact rational constants follow from the ellipse's semiaxes. This direct bound can be very large; a bound on the error itself can be much sharper.

For \(d>0\) define

$$
S_d=\max(a+b,2-a-b)+2d,\quad
v_d=S_d/(b-a),\quad
\rho_d=v_d+\sqrt{v_d^2-1}.
$$

If \(\rho_d<\rho\), put

$$
\lambda=1-\frac{\log\rho_d}{\log\rho}>0,\qquad
C(d)=d^{-3}+d^{-5}+d^{-7}+36d^{-9}
+2d^{-2}+6(1/2)^{1/10}d^{-3}.
$$

Then

$$
\boxed{N_{\rm raw}(v)\le C(d)M^{1-\lambda}\delta^\lambda.}
\tag{9}
$$

In particular a sufficient hypothesis for the varying-parameter raw ball is

$$
\delta\le
M\left(\frac{4.5\,10^{-6}}{C(d)M}\right)^{1/\lambda}.
\tag{10}
$$

The fixed-parameter version replaces \(4.5\,10^{-6}\) by \(5\,10^{-6}\). Formula (9) can directly establish the raw-ball alternative regardless of the remainder convention used elsewhere. If a bound specifically in \(N_\phi\) is wanted, (4) gives \(N_\phi\le(415/4)\) times the right side of (9).

**Proof of (9).** On the slit ellipse \(E_\rho\setminus[a,b]\), let
\(\Phi(z)=\xi+\sqrt{\xi^2-1}\), \(\xi=(z-c)/h\), with the branch for which \(|\Phi|>1\). Its modulus tends to 1 on the slit and equals \(\rho\) on the outer boundary. The subharmonic maximum principle applied to \(\log|v|\) and the harmonic comparison function

$$
\log\delta+\frac{\log|\Phi(z)|}{\log\rho}\log(M/\delta)
$$

gives the two-constants bound. Zeros cause no difficulty: remove small disks around them and pass to the limit, or use the usual subharmonic extension with value \(-\infty\).

For any point within distance \(d\) of \([0,1]\), its sum of distances to \(a,b\) is at most \(S_d\). Indeed this sum on \([0,1]\) is bounded by \(\max(a+b,2-a-b)\), and moving a distance \(d\) increases it by at most \(2d\). The level curves of \(|\Phi|\) have focal-distance sum \((b-a)(|\Phi|+|\Phi|^{-1})/2\). Therefore \(|\Phi|\le\rho_d\) throughout this tube. It follows that \(|v|\le\eta=M^{1-\lambda}\delta^\lambda\) there.

Cauchy's formula on disks of radius approaching \(d\) about real points gives
\(|v^{(k)}|\le k!\eta/d^k\). Thus
\(\sum|c_j|\le\eta(d^{-3}+d^{-5}+d^{-7})\).
Oddness and \(v'(0)=0\) show that the degree-6 Taylor polynomial of \(v''\) is exactly \(6c_3u+20c_5u^3+42c_7u^5\). Taylor's integral remainder and the ninth derivative bound give

$$
|R_v''(u)|\le\frac{9!}{7!}\eta d^{-9}u^7
=72\eta d^{-9}u^7.
$$

Multiplication by \(u^{-6}\) and maximization for \(u\le1/2\) gives \(36\eta d^{-9}\). Finally the tail supremum is at most \(2\eta d^{-2}\), and the mean value theorem bounds its anchored seminorm by \(6\eta d^{-3}(1/2)^{1/10}\). Adding proves (9).

## Sizes under explicit illustrative assumptions

For the illustrative choices \(\rho=4\), \(M=10\), and a **uniform** error \(\delta=10^{-7}\) on \([a,b]\), interval arithmetic gives the following upper bounds for the right side of (9):

| \(d\) | \(\lambda\), approximately | proved upper bound from (9) |
|---|---:|---:|
| 0.05 | 0.615989 | \(2.177\,10^9\) |
| 0.10 | 0.501248 | \(3.520\,10^7\) |
| 0.20 | 0.334958 | \(1.472\,10^6\) |
| 0.30 | 0.209391 | \(387554\) |
| 0.40 | 0.106456 | \(194408\) |

For example \(d=0.05\) makes the threshold on the right of (10) lie between \(1.4492\,10^{-31}\) and \(1.4493\,10^{-31}\). Hence the explicit hypothesis \(\delta\le1.4492\,10^{-31}\), with this \(M,\rho,d\), suffices for the raw ball. These computations are enclosed by [verification/analytic_bound_certificate.json](verification/analytic_bound_certificate.json), using exact input fractions and `mpmath.iv`.

These are deliberately conservative sufficient estimates, not lower bounds on the actual uncertainty or optimal continuation rates. A very large upper bound cannot prove that a trace is far away. Even \(M=10\) is an optimistic hypothetical bound on the complex error; no such bound for an exact profile is known here. Nothing establishes that a putative exact profile is analytic in this ellipse. The example shows quantitatively that this particular continuation argument, under the stated trial-scale accuracy, does not supply the tiny required radius.

To pass from discrete samples to the uniform error in (8), a further step is essential. Suppose endpoints \(a,b\) are sampled, the maximum gap is \(\Delta\), and \(|v(u_i)|\le\delta_s\). If disks of radius \(d_b\) about \([a,b]\) lie in \(E_\rho\), Cauchy's formula and piecewise linear interpolation give

$$
\sup_{[a,b]}|v|\le\delta_s+\frac{M\Delta^2}{4d_b^2}.
\tag{11}
$$

For completeness, on a gap of length \(\Delta_i\), the interpolation error is bounded by
\(\sup|v''|\Delta_i^2/8\); this follows from the integral remainder for linear interpolation, whose kernel has one sign and integral at most \(\Delta_i^2/8\). Since \(\sup|v''|\le2M/d_b^2\), (11) follows. Complex-valued functions obey the same integral-kernel bound.

For \(\rho=4\), disks with \(d_b=1/2\) are contained in the ellipse: their focal-distance sum is at most \(b-a+1\), strictly less than \((b-a)(4+1/4)/2\). With \(M=10\), \(\Delta\le1/700\), and \(\delta_s=3\,10^{-7}\), (11) is exactly \(10147/490000000<2.071\,10^{-5}\). This is an illustrative mesh, not a claim about the stored sampling grid. Both the exact-profile error at each sample and the reference's sample fit error would have to be proved before their sum could serve as \(\delta_s\). No such exact-profile error bounds are provided.

## Dependencies and scope

The distance calculation uses only the three exact input polynomials and the stated normalization. The conditional estimate uses the subharmonic maximum principle, Cauchy's formula, and Taylor's theorem, with all steps and constants given above. The exclusion radii themselves are proved in [../radius_budget/PROOF.md](../radius_budget/PROOF.md). Neither (6) nor (7) is asserted to solve IPM. Which additional restrictions the full coupled equation imposes on these trace uncertainties remains open.
