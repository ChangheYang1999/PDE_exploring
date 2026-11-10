# X3 current profile audit

Audit date: 2026-11-06, America/Los_Angeles. This audit inspected fixed existing profiles; it performed no profile search, continuation, or coefficient optimization. Original arrays and certificates were not modified.

## Result

**Both the raw X3 profile and its exactly joined, strain-repaired modal reference have a strictly positive cofactor at every finite point:**

\[
\bar\rho=x^2y\bar a,\qquad \bar a>0.
\]

For raw X3 this follows directly from its defining exponential representation. For the repaired modal reference, a new continuous-domain positivity check passed, with explicit rounding allowances and analytic bounds for both infinite ends; details appear below. Neither profile has a positive constant lower bound for \(\bar a\) on the plane: \(\bar a\to0\) at infinity.

The natural weight is promising for the **transport energy coefficient**, experimentally close to \(5.57536\). It does not yet give a full Darcy inverse estimate. Moreover, for the repaired modal reference,

\[
\boxed{\|F_{\bar\rho}\|_{L^2(1/\bar\rho^2)}=\infty.}
\]

This last conclusion follows from its previously certified nonzero far residual, not from extrapolating a sampled residual. Small pointwise relative error and a finite weighted residual norm are different requirements.

## 1. Located objects and provenance

Paths below are relative to `/mnt/d/Changhe_D/PDE_exploring/Changhe/IPM/`.

| Object | File / definition | Status |
|---|---|---|
| Accepted raw X3 | `case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz` | Historical numerical candidate; retains its strain defect |
| Raw reconstruction | `analysis1/IPM_Analysis_I.artifacts/numerics/src/x3.py`; independent original generator: `case1/IPM_Setting_I.artifacts/d_evaluator/code/gen_shape.py` | Evaluates the actual original arrays |
| Stored modal trial | `analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz` | Rounded stored join fields alone are not the exact repaired reference |
| Exact modal reference | Same independent modal coefficients, with exact order-six endpoint matching and the exact-real scalar repair in Analysis III proof `04_modal_scalar/PROOF.md` | Preferred existing background for the audited S2 theory |
| Exact input export | `analysis1/IPM_Analysis_I.artifacts/verification/data_exact/modal_v2.json.xz` | Hexadecimal dyadic input export; dependent joins and repair still follow their defining equations |
| Modal evaluators | `analysis1/IPM_Analysis_I.artifacts/numerics/src/modal_fit.py`, `trial_green.py` | Factor evaluation and closed-form canonical Green inverse |

Input SHA-256 values, checked in this audit:

```text
raw:   d58bb8834b0a5859ef8d8bfd61091fe4cf1852114378d33afbbc5b5662bb53a2
modal: a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874
```

Raw MD5 also matches the historical identifier `15f8095f7e79dbfa0c50d75e5fe8997a`. The case1 follow-up and Analysis III conventions explicitly identify X3 as the accepted state; later collocation files are diagnostics, not newer accepted candidates. No Candidate 007 or 013 arrays were used. Filename searches also inspected the separate `case1`, `case4`, `case5`, `analysis1`, `IPM_writing`, and fractional-coefficient-audit directories under `/mnt/d/Changhe_D/`; no replacement X3 object was identified there.

## 2. Actual representation and numerical domain

Both objects use the exact input constants

\[
k=\frac{1615536043799051}{9007199254740992},\qquad
\bar c_l=1/k=5.575362610641546\ldots,\qquad
L=\frac{8614738245908811}{1125899906842624}.
\]

The stored binary64 `c_l` is the rounded reciprocal; exact statements use \(1/k\). Likewise, the raw file's stored `c` is the intended target strain, **not** its actual canonical strain.

**Raw X3.** With \(u=r/L\),

\[
\begin{aligned}
q&=1-(1+u^2)^{-(1-k)/2},&s&=u^2/(1+u^2),\\
\chi&=u^2/(u^2+0.02^2),&p&=6+2k/(2-k),\\
H&=\tfrac{k-3}{2}\log(1+u^2)
 +\sum_{m=0}^{200}\chi^{\max(m-1,0)}b_m(q)\cos(2m\theta)
 +s^{p/2}T(2q-1)|\cos\theta|^{p-2}\sin^2\theta,\\
\bar a&=e^H.
\end{aligned}
\]

Each \(b_m\) is a clamped degree-seven spline with 375 stored coefficients and its first basis coefficient fixed to zero. \(T\) has six Chebyshev coefficients. The array has 75,382 entries including \(k\). The compact coordinate covers infinity at \(q=1\). `R_shape=1000` records a historical numerical scale; it is **not** the boundary of this formula. No optional exterior-closure replacement was used.

**Exact modal reference.** Its cofactor is \(\sum_{m=0}^{259}a_m(\log r)\cos(2m\theta)\). There are 1,565 degree-seven spline controls per mode, 1,558 nondegenerate spans, seven inner powers, ten outer powers, and degree-six exponential join corrections. The mathematical joins are the exponentials of the endpoint knots:

\[
r_-=0.007651424601381518\ldots,\qquad
r_+=3412.966858161562\ldots.
\]

The outer factor exponents are \(k-3-j(1-k)-2l\), for the ten stored pairs \((j,l)\). Infinity is an explicit analytic branch, not a finite boundary condition.

The canonical conventions are \(-\Delta\bar\psi=\partial_x\bar\rho\), \(U=(-\bar\psi_y,\bar\psi_x)\), with no added harmonic strain. Existing density/source Fourier Green formulas evaluate \(\bar\psi\) and its derivatives. This audit reused `ModalInverse` for dense diagnostics and `TrialGreen` for targeted closed-form modal checks.

Both factorizations and the even-x/odd-y density symmetry hold exactly. The cofactor is even in both variables. Consequently the density's only zero sets are the two coordinate axes.

## 3. Cofactor sign, extrema, axes, and infinity

### Numerical scan

Binary64 evaluation used 9,400 radii: zero, a logarithmic grid from \(10^{-8}\) to \(10^{12}\), mapped raw spline knots, modal knots and span midpoints, and the source radius. Each radius used 2,049 angles on the closed first quadrant. Symmetry covers the other quadrants. The modal diagnostic copy had its joins recomputed by exact rational arithmetic before conversion to binary64, and included the scalar repair.

| Quantity | Raw X3 | Repaired modal diagnostic copy |
|---|---:|---:|
| Smallest sampled \(\bar a\) | \(2.91132367243\times10^{-32}\) | \(2.91132367248\times10^{-32}\) |
| Location of sampled minimum | \(r=10^{12},\ \theta=0.31063110955\) | Same |
| Largest sampled \(\bar a\) | \(1\), at the origin | \(1\), at the origin |
| Nonpositive samples | 0 | 0 |
| Sampled range of \(\bar a/(1+(r/L)^2)^{(k-3)/2}\) | \([0.6592433,29.70300]\) | Same to displayed precision |

These extrema are experimental; the maximum has not been certified to be exactly one globally. The minimum location corresponds approximately to \((x,y)=(9.52141\times10^{11},3.05660\times10^{11})\). The **global infimum is zero**, approached at infinity, and is not attained at a finite point.

### Continuous-domain positivity validation

Raw positivity requires no grid certificate: every term defining \(H\) is finite at finite radius, its origin limit is zero, and \(e^H>0\).

For the **exact repaired modal object**, this audit obtained the following conservative bounds. Here \(\tau=\log(r/r_+)\) in the outer rows.

| Region | Validated lower bound |
|---|---|
| \(0\le r\le r_-\) | \(\bar a>1-10^{-6}\) |
| \(r_-\le r\le r_+\) | \(\bar a>1.8\times10^{-8}\) |
| \(0\le\tau\le2\) | \(e^{(3-k)\tau}\bar a>1.64\times10^{-8}\) |
| \(\tau\ge2\) | \(e^{(3-k)\tau}\bar a>7.1\times10^{-9}\) |

These are deliberately loose bounds covering continuous regions, including both axes and both infinite ends. They do not assert a constant positive lower bound on the entire plane.

The validation used 384-bit Arb scalar bounds, exact rational endpoint jets, and an explicit error allowance for binary64 matrix products. It is a new check in this audit, not an independently replayed historical certificate. Its reproducible sufficient inequalities are:

* **Inner end:** bound \(|\bar a-1|\) by the sum of absolute inner power coefficients plus \(\sum_{m,j}|E_{i,mj}|\sup_{v\ge0}v^je^{-b_iv}\). This gives an upper bound \(7.698076434\times10^{-7}\).
* **Spline region:** write \(\bar a=\sum_i B_i(t)P_i(\theta)\), where \(P_i=\sum_m S_{mi}\cos(2m\theta)\). For every one of the 1,565 control polynomials, check
  \[
  \min_j P_i(\theta_j)-2^{-38}\sum_m|S_{mi}|
       -\frac1{2500}\sum_m2m|S_{mi}|>1.8\times10^{-8}.
  \]
  The actual smallest lower endpoint was \(1.8042618238\times10^{-8}\). B-spline nonnegativity and partition of unity extend this to every radius in the spline region.
* **Outer end:** after extracting \(e^{(k-3)\tau}\), use the ten angular polynomials with radial factors \(e^{\beta_q\tau}\), where \(\beta_q=-j_q(1-k)-2l_q\). On \([0,2]\), use 65 nodes \(\tau=j/32\), and subtract the radial Lipschitz allowance \(\sum_{q>0}|\beta_q|\|A_q\|_1/64\), the angular allowance above, and rounding error. The resulting lower endpoint was \(1.6475363332\times10^{-8}\). Beyond two, subtract \(\sum_{q>0}e^{2\beta_q}\|A_q\|_1\) from the leading angular lower bound; this gives \(7.1778714909\times10^{-9}\). The rescaled exact outer join correction is bounded by \(2.647889484\times10^{-16}\) and was subtracted in both checks.

All angular checks use \(\theta_j=j\pi/4096\), \(0\le j\le2048\). The nearest-node distance is less than \(1/2500\). Arb-generated cosine values were individually checked within absolute error \(2^{-50}\) of the binary64 table; coefficient and exponential conversions were checked to relative error \(2^{-50}\). The allowance \(2^{-38}\) times coefficient l1 mass dominates both matrix-product roundoff and those conversions, using the standard binary64 round-to-nearest dot-product error bound with unit roundoff \(2^{-53}\). Thus this validation has explicit arithmetic assumptions; it is not a claim that a finite grid alone proves positivity. A second implementation has not independently replayed it.

### Axis values and far field

The axes were evaluated directly from \(e^H\) or the cosine sum, never by dividing small density values. Representative values are:

| \(r\) | Raw \(\bar a(r,0)\) | Raw \(\bar a(0,r)\) | Modal \(\bar a(0,r)\) |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 0.9886352401 | 0.9883013473 | 0.9883013473 |
| 8.600063805 | 0.4022316012 | 0.5402661886 | 0.5402661887 |
| 100 | \(4.935422594\times10^{-4}\) | \(9.220500862\times10^{-3}\) | \(9.220500862\times10^{-3}\) |
| \(10^6\) | \(2.562157100\times10^{-15}\) | \(1.100174639\times10^{-13}\) | \(1.100174639\times10^{-13}\) |

Both have \(\bar a\sim r^{k-3}C(\theta)\), uniformly in angle, with a positive angular coefficient. Sampling the exact leading formulas gives \(C\in[205.00484,9236.73887]\), minimum near \(\theta=0.3106311\), maximum on the vertical axis. These numerical extrema are not interval extrema. The modal tail positivity is covered by the validation above; raw tail positivity follows from its exponential formula. The cofactor vanishes, rather than becoming singular, at infinity.

## 4. Origin normalization, compatibility, and regularity

Both objects have \(\bar a(0,0)=1\) exactly.

The historical raw strain enclosure, inspected with its proof and audit records, is

\[
15.726087821623500282<c[\mathrm{X3}]<15.726087821623500289,
\]
\[
1.0301137738456\times10^{-8}<3/k-1-c[\mathrm{X3}]
 <1.0301137743913\times10^{-8}.
\]

Thus its strain defect **remains**. The exact modal definition instead enforces \(3\bar c_l-c[\bar\rho]=1\) identically. Replaying the existing scalar program at 384 bits reproduced

\[
c_0=15.72608783192467862256381469718\ldots,\qquad
z=-1.19860523645373489046033416489\ldots\times10^{-20}.
\]

The repair changes the leading outer coefficient and recomputes its join correction. It does not add harmonic velocity. The exact real \(z\), defined by the strain integral, must not be replaced by its printed midpoint in an exact definition.

For raw X3, direct differentiation of the original first spline span gives, with 384-bit scalar evaluation,

\[
\bar a=1-0.01145025688899930007\,x^2
         -0.01183915975911603703\,y^2+O(r^4).
\]

For reproduction, if \(b'_0,b'_1\) denote the q-derivatives at zero, the coefficients are \([(k-3)+(1-k)(b'_0\pm b'_1)]/(2L^2)\). Its fractional term has \(p=6.19703025709\ldots\); global smoothness must not be inferred from this local quadratic expansion.

The modal factor has the form \(1+r^2B(\theta)+\cdots\) and is **not Cartesian \(C^2\)** at the origin. Its directional quadratic coefficients on the horizontal and vertical axes are approximately \(-0.01145010329\) and \(-0.01183901693\); these are not a two-variable Taylor polynomial. Analysis III proof `33_modal_origin_regularity` proves that its density is \(C^{4,1}\), not \(C^5\), at the origin. Across positive joining circles it is \(C^6\).

## 5. Vertical trace and similarity-velocity zeros

\(\bar\rho(0,y)=0\) holds exactly throughout the represented vertical axis for both objects. The positive axis cofactors above equal the analytic limit \(\bar\rho_{xx}(0,y)/(2y)\).

For the repaired modal reference, the existing whole-axis certificate gives

\[
\frac{\bar c_l y+\bar\psi_x(0,y)}{y}\ge5.5752>0\qquad(y>0).
\]

Its limits are \(4\bar c_l-1=21.301450442566\ldots\) at zero and \(\bar c_l\) at infinity. Closed-form diagnostic values at \(y=1,10,100,10^6\) were approximately \(21.20151,16.06534,7.55910,5.576427\). No vertical-axis drift zero occurs. Raw dense diagnostics gave the same signs and displayed values; the modal certificate is not automatically a raw-profile certificate.

The existing **modal** global zero-set certificate identifies only \(0\) and \((\pm p,0)\), with

\[
\frac{4841405518533377}{2^{49}}<p<\frac{4841405518533711}{2^{49}},
\qquad p\simeq8.600063805157.
\]

There \(\bar a(p,0)\simeq0.4022316013>0\). The transverse similarity rate is in \((0.99999997745,0.99999997750)\), so the axis limit of \(F/\bar\rho\) is approximately \(-2.2528\times10^{-8}\), not singular. The raw numerical positive-axis root was approximately \(8.60006380065\); a global zero-set proof was not replayed for raw X3.

## 6. Residual factor, relative error, and the weight

Put \(v_1=\bar c_l+U_1/x\), \(v_2=\bar c_l+U_2/y\), with spectral limits on the axes. Then exactly

\[
F=x^2y f,\qquad
f=v_1(2\bar a+x\bar a_x)+v_2(\bar a+y\bar a_y)-\bar a.
\]

There are no terms of degree below three. Raw X3 has \(f(0)=3/k-1-c[\mathrm{X3}]\ne0\), hence a nonzero cubic residual. For the repaired modal reference, \(f(0)=0\) and \(f=O(r^2)\), so \(F=O(r^5)\). The order two is genuinely present: the \(r^2\cos(520\theta)\) coefficient of \(f\) is \((3/k-1)258e^{-2t_-}D_{259,1}\), enclosed around \(4.4367025514\times10^{-11}\). This is an angular expansion, not a claim of Cartesian \(C^2\) regularity for \(f\).

Since \(\bar a>0\), the relative residual \(f/\bar a=F/\bar\rho\) extends across the axes and the similarity sources. Its far behavior is \(O(r^{k-1})\); it is globally bounded for these fixed explicit profiles. A numerical sharp global bound was not certified.

Dense velocity diagnostics used 24,577 log-uniform radii on \([10^{-6}L,10^8L]\), 1,025 closed-quadrant angles, six-point radial Green integration, and a four-power outer tail fit. Axis quotients used the identity \(\sin(2n\theta)=2\sin\theta\cos\theta\,U_{n-1}(\cos2\theta)\), avoiding division near either axis. A targeted closed-form modal Green calculation used 236 radii, including 121 near the source, and 2,049 angles.

| Experimental diagnostic | Raw | Repaired modal copy |
|---|---:|---:|
| Dense sampled range of \(F/\bar\rho\) | \([-1.3511,1.5655]\times10^{-6}\) | \([-1.3534,1.5603]\times10^{-6}\) |
| Dense sampled \(\bar c_l-f/\bar a\) | Approximately \([5.5753610,5.5753640]\) | Same |
| Largest sampled \(|F|\) | \(1.89535\times10^{-4}\) | \(1.89535\times10^{-4}\) |
| Location of that absolute maximum | \(r\simeq40062.35,\theta\simeq0.642738\) | Same |
| Maximum \(|F|/(|V_1\rho_x|+|V_2\rho_y|+|\rho|)\) | \(7.08\times10^{-7}\) | \(7.06\times10^{-7}\) |

The closed-form modal check found relative extrema about \(-1.340\times10^{-6}\) and \(1.5603\times10^{-6}\), consistent with this scale. No blowup was observed near axes or sources; the largest positive relative peak was near \((6.9722,0.06417)\). An inner-join feature around \(r=0.007\) reached roughly \(8\times10^{-8}\) on the vertical-axis limit. The far relative error also stays small and tends to zero.

**Numerical failure retained:** an initial 6,145-radius / 513-angle Green grid produced spurious relative peaks around \(2.1\times10^{-5}\) near the source. Its residual maxima were rejected. Even the fine grid's computed central strain differs from the certified value by about \(2.7\times10^{-10}\); it cannot establish exact origin cancellation. Exact normalization and origin orders above use the defining equations and scalar certificate instead.

**Weighted residual limitation.** Analysis III proof `117_far_residual_leading_term` and its passing 512-bit coefficient check establish a nonzero modal leading residual

\[
F=r^{2k-1}E(\theta)+o(r^{2k-1}),\qquad E\not\equiv0.
\]

Consequently \(F/\bar\rho\sim r^{k-1}E/\Theta\) on an interior angular interval where its leading coefficient is nonzero. Therefore

\[
\int |F|^2/\bar\rho^2\,dX
\quad\text{contains a divergent tail proportional to}\quad
\int^\infty r^{2k-1}\,dr.
\]

The divergence holds despite boundedness and decay of the pointwise quotient. This conclusion is for the exact repaired modal reference. A separate raw leading-residual nonvanishing certificate was not produced here.

## 7. Darcy coefficient diagnostics

Let \(C_x=2+x\bar a_x/\bar a\), \(C_y=1+y\bar a_y/\bar a\). The 9,400-by-2,049 scan gave, for both profiles to displayed precision,

\[
-0.833579\lesssim C_x\le2,\qquad
-1.820640\lesssim C_y\le1.
\]

The smallest sampled \(C_x\) was on the horizontal axis near \(x=30.1163\). The smallest sampled \(C_y\) approached its vertical-axis far limit. No large absolute coefficients were observed. These numerical ranges are not certified supremum bounds.

At the origin \((C_x,C_y)\to(2,1)\). On the vertical axis \(C_x=2\); on the horizontal axis \(C_y=1\). At infinity their sum tends to \(k\); the horizontal limits are \((k-1,1)\), and the vertical limits are \((2,k-2)\). The explicit angular tail formulas give finite limits on every ray. These coefficients can change sign without making \(\bar a\) change sign.

## 8. Existing certification and what was replayed

The following are **historical certificates inspected here**, not rerun in full. Paths are under `analysis3/IPM_Analysis_III.artifacts/verification/proofs/` unless stated otherwise.

| Evidence | Scope |
|---|---|
| `10_raw_x3_strain/PROOF.md`, `evidence/bounds_audit.json` | Raw strain and nonzero defect; includes original-data, quadrature-remainder and coverage checks |
| `04_modal_scalar/PROOF.md`, `evidence/recomputed.json` | Exact modal joins/strain definition and scalar repair; **the scalar computation was replayed here** at 384 bits |
| `15_modal_source/evidence/audit.json` | Modal source bracket and transverse rate below one |
| `68_independent_global_coefficients/evidence/audit.json` | Continuous whole-axis drift lower bound; recorded global lower endpoint \(5.5752039576\ldots\) |
| `79_actual_global_zero_set/PROOF.md` | Complete modal similarity-velocity zero set and flow geometry |
| `154_residual_final_audit/evidence/final_certificate.json` | \(6049.11<\|F\|_Y<8601.42\), in its specified axis-jet strong norm |
| `177_high_residual_majorant/PROOF.md` and Analysis III report §6 | In the explicitly fixed high target norm, historical bounds \(3.8666592266\times10^{10}<\eta_*<6.321\times10^{129}\); not the natural-weight norm |
| `117_far_residual_leading_term/evidence/check.json`, `audit.json` | Nonzero modal far residual and its exact exponent |

For the strong norm above, \(Y=EG\oplus L^2_P(|x|^{-17/2}\max(1,r)^{29/4}\,dX)\), \(E\gamma=x^2y\gamma(\log r)\), and the scalar squared-norm weight is \(e^{-t/2}\) for \(t<0\), \(e^{27t/4}\) for \(t\ge0\). Its large residual norm is compatible with a small pointwise residual.

New floating diagnostics used NumPy 1.26.4 and SciPy 1.14.1. New scalar and positivity bounds used python-flint 0.9.0 at 384 bits. The positivity calculation covers all 260 modal modes and both analytic tails, with the exact-real repair enclosed by the replayed ball. It relies on Arb and the explicitly stated standard binary64 error model, and has not received a second-implementation audit.

Temporary scripts and outputs were kept outside the repository in `/tmp/x3_profile_audit/`. The positivity script SHA-256 was `1e4b46ec5857885d8c753415219d2c6b2398071e7cb588f420e638e4aee1d54d`; the scalar replay used the original `04_modal_scalar/code/recompute.py` with only input/output destinations redirected. The sufficient inequalities and conservative positivity bounds are retained in this report so its conclusions do not depend on retaining temporary files.

## 9. Assessment and minimum remaining work

The proposed factorization and positivity are supported for the existing reference. The weight is defined almost everywhere off the two axes and behaves near them like \(x^{-4}y^{-2}\bar a^{-2}\). Along a fixed ray off the axes, it behaves as \(r^{-2k}/\Theta(\theta)^2\), despite the cofactor tending to zero. Its axis singularity requires an operator domain: for \(h=x^2yb\), the local weighted square is \(|b/\bar a|^2\). The observed bounded logarithmic derivatives and positive transport coefficient support further linear analysis.

The minimum additional work is:

1. Independently replay the new modal positivity inequalities, preferably with fully interval matrix products, and preserve a standalone certificate if these bounds enter a paper. Raw strict positivity already follows from its formula.
2. Certify a coarse continuous bound such as \(|f/\bar a|<\bar c_l/2\): combine origin cancellation, interval bounds on finite radial/angular cells, and explicit relative tail bounds. Resolve cells near source points and spline joins; pointwise density residual bounds alone are insufficient.
3. Specify the weighted operator domain, axis traces, and integration-by-parts boundary behavior, then bound the full nonlocal Darcy coupling in that realization. Positivity of the transport coefficient alone proves no full inverse estimate.
4. If the same weight is intended for an a posteriori residual norm, address the **already established divergent modal residual tail**. A formulation retaining explicit tail coordinates or a suitable additional radial weight would require its own analysis. Improving a finite grid cannot remove this asymptotic obstruction.

No stationary existence claim, nonlinear closure, or full weighted linear invertibility claim is made by this audit.
