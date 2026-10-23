# Proposed 860-generator potential space: specification and embedding

**Status, 2026-10-23: mathematical specification, not an implemented basis or an enlarged restart.** The preserved production model has 186 generators and 181 feasible variables. The Linux sequence is baseline qualification and accepted278 reproduction, then direct development of this exact extension; see [the research plan](NEXT_RESEARCH_PLAN_860.md). No long 181D continuation is an intervening milestone.

## Definition, order and rank boundary

Set \(R=1+r^2\), \(t=r^2/R\), \(H_m=\operatorname{Re}(x+iy)^{2m}\),
\(\gamma=1/c_l\), \(\lambda=1-\gamma\), and \(p_j=(3+\gamma-j\lambda)/2\). The proposed **unscaled** generators are
\[
\boxed{\chi_{mkj}=r^{2k}R^{p_j-k}\cos(2m\theta)
      =H_mR^{p_j-m}t^{k-m}},
\qquad j=0,1,2,3,\quad m=0,\ldots,9,\quad k=m,\ldots,25.
\]
There are exactly \(4\sum_{m=0}^9(26-m)=860\) generators. No Legendre or Jacobi polynomial occurs in this new definition: its compactified radial factors are monomials. The specification's unique zero-based ordering is **j, then m, then k**, with
\[
I(j,m,k)=215j+26m-\frac{m(m-1)}2+(k-m).
\]
A future versioned manifest must enumerate these triples explicitly, record formula/normalization/derivative versions and bind the chosen \(c_l\). This order is proposed, not a manifest already consumed by production.

At the current \(c_l=1.8089923602744993\), the four \(p_j\) differ by noninteger amounts. For fixed m, division by the common positive radial envelope leaves finite polynomials multiplied by distinct noninteger powers of \(1-t\); their different endpoint powers, together with polynomial independence within each branch, establish exact independence. Angular cosines separate m. This is an algebraic rank statement, **not numerical conditioning**. At \(c_l=3\), \(p_0-p_3=1\) and cross-branch identities occur; rank must be rechecked at exceptional parameters, rather than assuming independence globally.

Potential-function independence and physical-field rank are also different. At \(c_l=2\), p3=1 and the j3 functions R, r² and x²−y² (triples m0/k0, m0/k1, m1/k1) each give \(\psi=\rho=0\); at \(c_l=3\), p2=1 produces analogous kernels in addition to the cross-j identities. This is not a complete classification. Stop for a rank/kernel audit near exceptional parameters.

860 is a generator count, not a certified feasible-variable count. The free \(c_l\), analytic center elimination, five Taylor equations, actual zero-field kernels, gauge treatment and numerical rank must be audited in the enlarged chart. Do not append these 860 generators to the old 186: that introduces exact dependencies.

## Exact Cartesian origin behavior and free parameters

Because \(k\ge m\),
\[
r^{2k}\cos(2m\theta)=(x^2+y^2)^{k-m}H_m
\]
is a polynomial, and \(R^{p_j-k}\) is smooth for every finite real exponent. Potential degree begins at \(2k\); \(f=-\partial_y\Delta\chi/y\) and \(\psi_x/y=\chi_{xxy}/y\) have smooth parity extensions. If \(k\ge\max(m,5)\), these two fields start at degree at least six, so such changes preserve the center and the quadratic/quartic data entering the five Taylor equations term by term. Lower-k additions require the full feasible chart. All 860 coefficients are not automatically feasible.

Retain \(\psi=\chi_{xy}\), \(\rho=-\partial_y\Delta\chi=yf\), the established analytic center relation and all five equations in [MATHEMATICS.md](MATHEMATICS.md). Both \(c_l\) and physical \(a_0=\rho_y(0)\ne0\) stay free. \(a_{\rm ref}=23.95065822465609\) is fixed only in the unchanged primary loss \(J_{\rm abs}\).

The genuine spatial dilation is
\[
\chi_L(X)=L^4\chi(X/L),\quad
\rho_L=L\rho(X/L),\quad\psi_L=L^2\psi(X/L),\quad f_L=f(X/L).
\]
It leaves \(c_l\) and \(a_0\) unchanged. Any proposed gauge handling must be checked against this physical transformation, not coefficient normalization or fixing either parameter. Exact dilation need not remain in this fixed finite radial space; do not claim an exact coefficient map by refitting. The preserved 181D solver removes no scaling direction.

## Source-confirmed old generators and exact coordinate map

The sources are [absolute_fields.py](../research/absolute_fields.py) lines26–39, [spectral_basis.py](../research/base/spectral_basis.py) lines58–84,112–135, [campaign_tools.py](../research/base/campaign_tools.py) lines14–22, and the saved [Global mode manifest](../research/inputs/global.json) from line233. Accepted278's own serialized modes are authoritative for that candidate; the input manifest is the same generator list, not its current coefficients.

Let \(b_{m,s}\) be the old core coefficient, with offsets
\(\sigma_s=(0,1,2,\lambda/2,\lambda,3\lambda/2)\). The old generator is
\(H_mR^{p_0-m-\sigma_s}\), \(m=0,\ldots,3\). Its order is \((m,s)\), m0..3/s0..4, followed by \((m,5)\), m0..3. Let \(g_{mn}\) follow the exact 162 saved Global modes: m0..8/n0..17 lexicographically, omit (3,0), then append (9,0). Begin with every new \(a_{mkj}=0\), then **add** these contributions:

1. For s=0,1,2,
   \[
   H_mR^{p_0-m-s}
     =\sum_{h=0}^{s}(-1)^h\binom sh\,\chi_{m,m+h,0},
   \qquad a_{m,m+h,0}\mathrel{+}=b_{m,s}(-1)^h\binom sh .
   \]
   This is \(R^{p_0}t^m(1-t)^s\cos(2m\theta)\), a finite identity.
2. For s=3,4,5, set j=s−2:
   \[
   H_mR^{p_0-m-j\lambda/2}=\chi_{m,m,j},
   \qquad a_{m,m,j}\mathrel{+}=b_{m,s}.
   \]
3. A Global mode is
   \[
   G_{mn}=R^{p_0}t^{v_m}N_nP_n(2t-1)\cos(2m\theta),\qquad v_m=\max(m,5),
   \]
   with ordinary Legendre \(P_n(1)=1\), mathematically \(N_n=\sqrt{2n+1}\), and
   \[
   P_n(2t-1)=\sum_{h=0}^n(-1)^{n-h}\binom nh\binom{n+h}h t^h.
   \]
   Therefore
   \[
   a_{m,v_m+h,0}\mathrel{+}
     =g_{mn}N_n(-1)^{n-h}\binom nh\binom{n+h}h .
   \]
   The largest required k is \(8+17=25\); (9,0) uses k=9.

Production evaluates \(N_n\) via its log-Gamma expression: for n>0,
\[
N_n=\exp[-\tfrac12\{\lgamma(n+1)+\lgamma(n+1)-\log(2n+1)
                     -\lgamma(n+1)-\lgamma(n+1)\}],
\]
and N0 uses the n=0 expression in the source. Mode defaults are alpha=beta=0, normalize=true, scale=1. The mathematical factor is exactly \(\sqrt{2n+1}\); the floating-point operation sequence need not give identical last bits. Use the source-evaluated normalization for binary reconstruction checks and record rounding errors separately from the analytic identity.

This proves exact nesting of all 186 old functions; it is neither least-squares projection nor approximate dilation. The known removed Global (3,0) was exactly the old m3 combination (1,−2,1) at integer offsets0,1,2. Do not reintroduce it as an additional coordinate. Large alternating monomial coefficients can cause serious cancellation: an exact map on paper is not evidence of a numerically stable evaluator. Compensated/high-precision construction or an equivalent stable internal evaluation is allowed only with independently verified equivalence and explicit versioning.

### Complete c_l dependence of the embedding

\[
\gamma'=-c_l^{-2},\quad\lambda'=c_l^{-2},\quad
p_j'=-\frac{j+1}{2c_l^2},\quad
\partial_{c_l}\chi_{mkj}=p_j'\log R\,\chi_{mkj}.
\]
The displayed old-to-new **linear coefficient matrix B is analytically independent of \(c_l\)**: the integer expansions, Legendre coefficients and Nn are constant, while the fractional dependence is in the matched basis functions. Thus for any differentiable old coefficient path \(u(c_l)\),
\[
a=Bu,\quad a'=Bu',\quad
\frac d{dc_l}\sum a\chi=\sum(a'\chi+a\,p_j'\log R\,\chi).
\]
At accepted278, u contains the **analytically eliminated** c0, not merely its rounded display; u′ includes that center chain and, when differentiating feasible variables, the C5 chart. Fixed raw coefficients and a feasible chart path are different derivative tests. Compare both old/new physical derivatives including explicit \(c_l\) drift in \(R_f\), not only potential values. A future cl-dependent reconditioning or moment chart adds its own coordinate-map derivative.

## Every inverse-even moment and its physical meaning

For r>1, the binomial expansion is convergent termwise:
\[
\chi=\sum_{j=0}^3\sum_{q\ge0}r^{s_{jq}}C_{jq}(\theta),\quad
s_{jq}=3+\gamma-j\lambda-2q,\quad
C_{jq}=\sum_{m=0}^9 C_{mjq}\cos(2m\theta),
\]
\[
\boxed{C_{mjq}=\sum_{k=m}^{25}a_{mkj}\binom{p_j-k}{q}},\quad
C_{mj0}=\sum_k a_{mkj},\quad C_{mj1}=p_j\sum_k a_{mkj}-\sum_kka_{mkj}.
\]
For N=26−m coefficients in one (m,j) block, the first N moment rows are an invertible polynomial/Vandermonde map. Fixing L≤N independent moments leaves N−L radial shape directions; origin-invisible blocks have N=26−max(m,5). This exact rank says nothing about numerical conditioning. In the first campaign these moments are **diagnostics**, not new constraints.

For any homogeneous potential \(r^sC(\theta)\), let \(D=(s^2+\partial_\theta^2)C\). Then
\[
\rho=r^{s-3}F,\quad f=r^{s-4}Q,\quad\psi=r^{s-2}\Phi,
\]
\[
\boxed{F=-[(s-2)\sin\theta D+\cos\theta D'],\quad
Q=-[(s-2)D+\cot\theta D'],}
\]
\[
\boxed{\Phi=\tfrac12\sin(2\theta)[s(s-2)C-C'']
                 +(s-1)\cos(2\theta)C'.}
\]
The apparent cotangent is evaluated by its smooth finite-Fourier limit. Density F and quotient Q are different functions. Substituting \(s=s_{jq}\) gives every physical coefficient, with \(\alpha_{jq}=s_{jq}-3=\gamma-j\lambda-2q\). Moment derivatives must use
\[
\frac d{dc_l}C_{mjq}
=\sum_k a'_{mkj}\binom{p_j-k}{q}
+p_j'\sum_k a_{mkj}\,\partial_z\binom zq\big|_{z=p_j-k},
\]
where the derivative of the finite falling-factorial polynomial is valid also at roots; avoid dividing by z−h there. Differentiate s in both boxed physical maps as well.

## Formal compatibility, angular nonclosure and diagnostic policy

The [portable derivation extract](reference/FAR_FIELD_DERIVATION_EXTRACT.md) gives the Poisson equation, first three transport recurrences, scale-invariant coefficient diagnostics and branch qualifications. They are formal necessary relations under differentiated asymptotic/remainder assumptions, not an existence or universal expansion theorem.

For q=0, \(F_0\) from m≤9 reaches odd density harmonic19 and \(\Phi_0\) even sine harmonic20. Their first nonlinear density forcing generically reaches odd harmonic39:
\[
\mathcal E_1=-(c_l-1)F_1+(\gamma+1)\Phi_0F_0'-\gamma\Phi_0'F_0.
\]
The new F1 still reaches only19. The entire \(\mathcal E_1\) therefore cannot generally vanish at this uniform cutoff. A small projected low-mode defect leaves unresolved high modes. At accepted278 a nonzero coefficient yields original \(R_\rho\propto r^{2\gamma-1}=r^{0.105587864228\ldots}\), despite decaying quotient residual and finite loss. The current reported angular L2 coefficient is about0.440353421495; inspect [farfield.json](../verification/farfield.json) for its exact scope.

**Do not hard-enforce \(\mathcal E_1,\mathcal E_2,\mathcal E_3=0\), add a far-field penalty, or change \(J_{\rm abs}\) in the first enlarged campaign.** Measure full unprojected Fourier coefficients, density/quotient axis limits, absolute norms, dilation-invariant ratios and unresolved norm beyond the represented cutoff. The 0.145222% unresolved E1 norm fraction came from **accepted165**, not accepted278; it predicts neither this endpoint nor a future optimized profile. Later cutoffs \(M_j=(9,19,29,39)\) are a possible escalation, requiring radial k bounds at least29/39 for regular higher modes; they are not this first860 task.

The radial basis also generates the second lattice \(\alpha_{jq}=\gamma-j\lambda-2q\). Without exponent collisions or added multipole forcing its formal residual is
\[
\mathcal E_{jq}=-[j(c_l-1)+2c_lq]F_{jq}
+\sum_{\substack{a+b=j-1\\u+v=q}}
[(\alpha_{au}+1)\Phi_{au}F_{bv}'-\alpha_{bv}\Phi_{au}'F_{bv}].
\]
For example, the unforced j0/q1 equation requires F01=0 for an exact formal solution at the current exponent. This lies below the first three fractional orders. It does **not** license setting every radial moment to zero: higher interactions, branch collisions and canonical multipoles must be checked in order. Resonant Poisson powers can force logarithms. No all-orders pure fractional expansion is assumed.

## Receiving implementation and acceptance contract

1. Qualify the native Linux source/provider/BLAS and reproduce accepted278 before numerical edits. Preserve the full saved181D restart closure.
2. Implement a versioned860 module and explicit triple manifest outside the preserved production closure. Construct the analytic B map without fitting. Audit exact dependencies and conditioning, especially exceptional cl and monomial cancellation.
3. Independently compare every old/new generator identity and physical derivative; Cartesian origin/axis behavior; cl changes; all potential moments; canonical Green inverse; strict large-radius/high-precision tests. Verify the profile and cl/physical-a0 invariants, C5, fresh whole-axis loss and independent sampled maxima at embedded accepted278. State tolerances before examining differences. No enlarged optimizer state exists until a new chart/map/epoch is qualified.
4. Build the enlarged feasible chart including low-k contributions, analytic center elimination and all five Taylor equations. Preserve physical free parameters and genuine dilation semantics. Audit rank and full Jacobian in cl, tail, core and weak directions with independent finite differences.
5. Only after those gates pass, run guarded pilots and the substantive new campaign under the same absolute loss, independently integrate every physical trial and checkpoint all outcomes. Track origin/transition/large-radius errors and E1/E2/E3 without interpreting lower loss as stationarity, uniform decay, convergence or an exact PDE solution.

Source provenance and the accepted64/165 versus278 scope boundary are recorded in [farfield_derivation_provenance.json](../metadata/farfield_derivation_provenance.json). No numerical basis, coefficient, source or checkpoint was changed to write this specification.

