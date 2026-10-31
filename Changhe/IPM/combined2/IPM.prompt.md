# 48-Hour Coordinated Research Campaign
## Rigorous Stationary IPM Existence and Numerical Residual Optimization

**Duration: 48 hours of actual wall-clock research.**

**Organization: One Research Coordinator, two parallel research teams, and independent targeted auditors.**

**Main objective: Prove a rigorous fixed-parameter stationary IPM existence theorem and optimize the numerical reference until the theorem and numerical residual can be quantitatively closed.**

Before starting this 48-hour research campaign, carefully review Changhe/IPM/combined1, including its existing theoretical proofs, numerical experiments, Candidate 007 reference data, verification reports, and previous research conclusions. Build directly on the established results and avoid repeating work that has already been completed.

---

# PART 0 — CRITICAL INSTRUCTIONS

## 0.1 Do not restart the research from scratch

This task continues an extensive research program with several established analytical results.

A detailed **Existing Proof Reference** is included below.

Its purpose is to prevent unnecessary repetition of completed work.

**You must not spend substantial time re-proving the previously established results.**

In particular, do not restart proofs of:

1. Signed \(L^2\) coercivity and the existing \(L^2\) inverse construction.
2. Preservation of S1 symmetry and origin normalization.
3. The conditional frozen-transport fixed-point theorem.
4. Weak \(L^2\) Schauder–Tychonoff existence once a convex high-regularity invariant set is available.
5. The \(L^2\)–\(C^{1,\alpha}\) interpolation inequalities.
6. The exact frozen-origin Fourier resolvent formula.
7. The previously established asymmetric frozen-origin inverse estimates.
8. The conditional exterior weighted \(C^{1,\alpha}\) lifting.
9. The conditional finite-flow-tube propagation of regularity.

These results are written in the reference sections below, together with the main arguments.

For long technical proofs, use the previous research reports and their cited proof files as the authoritative detailed sources.

A brief consistency check is allowed when importing a result into a new setting. Do not turn this into a new multi-hour proof project.

If an actual error, missing assumption, or incompatibility is discovered, document it and assign one targeted worker to resolve it. Do not silently assume a broken lemma.

Distinguish:

- An established theorem under its stated hypotheses.
- A prior report's technical claim requiring a source check.
- A hypothesis not yet verified for Candidate 007.
- A genuinely open theorem.

Do not upgrade a conditional result to an unconditional one.

## 0.2 What is genuinely new in this campaign?

The main analytical target is the **uniform weighted \(C^{1,\alpha}\) regularity lifting for the full frozen-transport operator**:

\[
\boxed{
\mathcal A_kh=-F,\qquad
\mathcal A_k=\mathcal L+U[k]\cdot\nabla.
}
\]

The \(L^2\) inverse is already available under the established background assumptions.

The difficulty is proving that its unique \(L^2\) output is uniformly in weighted \(C^{1,\alpha}\), with estimates strong enough to construct an invariant high-regularity ball.

This is the primary unresolved analytical problem.

The primary numerical target is to reduce the stationary residual, especially its \(L^2\) norm, using the existing Candidate 007 basis and controlled expansions of that basis.

Theory and numerics must communicate continuously.

---

# PART I — EXACT MATHEMATICAL SETTING

## 1. Stationary IPM

We consider

\[
\boxed{
(c_lX+U[\rho])\cdot\nabla\rho-\rho=0,
}
\]

where

\[
\boxed{
U[f]=(-R_1R_2f,R_1^2f).
}
\]

The IPM velocity is divergence-free:

\[
\nabla\cdot U[f]=0.
\]

The Fourier multiplier is

\[
\boxed{
m(\xi)=
\left(
\frac{\xi_1\xi_2}{|\xi|^2},
-\frac{\xi_1^2}{|\xi|^2}
\right).
}
\]

Let \(\bar\rho\) be the numerical reference and

\[
\bar u=U[\bar\rho].
\]

We impose the fixed-parameter condition

\[
\boxed{c_l=\bar c_l.}
\]

The current numerical reference is Candidate 007, with

\[
\bar c_l\approx1.81031921.
\]

The exact parameter is stored as a rational number in its authoritative coefficient file.

Do not vary \(c_l\) during the initial campaign.

Write

\[
\rho=\bar\rho+h.
\]

The correction satisfies

\[
\boxed{
\mathcal Lh+U[h]\cdot\nabla h=-F,
}
\tag{1.1}
\]

where

\[
\boxed{
\mathcal Lh
=
(\bar c_lX+\bar u)\cdot\nabla h
-h+U[h]\cdot\nabla\bar\rho
}
\tag{1.2}
\]

and

\[
\boxed{
F=(\bar c_lX+\bar u)\cdot\nabla\bar\rho-\bar\rho.
}
\tag{1.3}
\]

The symmetry is

\[
h(-x,y)=h(x,y),\qquad
h(x,-y)=-h(x,y).
\]

Define the origin strain functional

\[
\boxed{
\ell(h)=\partial_yU_2[h](0).
}
\]

The normalized correction satisfies

\[
\boxed{\ell(h)=0.}
\]

The known residual satisfies the compatible condition

\[
F_y(0)=0.
\]

---

# PART II — EXISTING PROOF REFERENCE

**This part is the established analytical reference for the new campaign.**

It is not a list of new research tasks.

The theory agents should use the statements and proof structures here, consult the previous detailed reports where necessary, and concentrate on the gaps identified later.

## Reference R1 — Signed \(L^2\) coercivity

**Status: Existing analytical result, conditional on the background bounds.**

Let

\[
V=\bar c_lX+\bar u.
\]

For sufficiently regular, decaying \(h\),

\[
\langle V\cdot\nabla h,h\rangle
=
-\frac12\int(\nabla\cdot V)h^2
=
-\bar c_l\|h\|_2^2,
\]

because

\[
\nabla\cdot V=2\bar c_l.
\]

Consequently,

\[
\begin{aligned}
-\langle\mathcal Lh,h\rangle
={}&(\bar c_l+1)\|h\|_2^2\\
&-\langle U[h]\cdot\nabla\bar\rho,h\rangle.
\end{aligned}
\]

The previously established signed IPM estimate controls the nonlocal quadratic term by

\[
\langle U[h]\cdot\nabla\bar\rho,h\rangle
\le(\theta+\kappa)\|h\|_2^2.
\]

Here \(\theta\) and \(\kappa\) are the specific background quantities defined and estimated in the earlier signed \(L^2\) analysis.

One formulation uses

\[
\theta=
\sup_X\frac{|\nabla\bar\rho(X)|-\bar\rho_y(X)}2,
\]

with \(\kappa\) controlling the remaining nonlocal coefficient variation through an explicit Riesz-kernel estimate.

The important conclusion is

\[
\boxed{
-\langle\mathcal Lh,h\rangle
\ge
\beta_0\|h\|_2^2,
\qquad
\beta_0=\bar c_l+1-\theta-\kappa>0.
}
\tag{R1.1}
\]

The detailed proof exploits the signed nonlocal structure, not a generic absolute-value Calderón–Zygmund bound.

For Candidate 007, earlier independent numerical reports recorded a signed gap exceeding \(2\), although the final campaign must distinguish historical certification from certificates actually present in the current workspace.

**Do not rederive the signed nonlocal quadratic estimate. Read its existing proof and numerical certificate.**

### Extension to frozen nonlinear transport

For any sufficiently regular \(k\),

\[
\langle U[k]\cdot\nabla h,h\rangle
=
\frac12\int U[k]\cdot\nabla(h^2)=0.
\]

Therefore, defining

\[
\boxed{
\mathcal A_k=\mathcal L+U[k]\cdot\nabla,
}
\]

we have

\[
\boxed{
-\langle\mathcal A_kh,h\rangle
\ge\beta_0\|h\|_2^2.
}
\tag{R1.2}
\]

No smallness of \(k\) is needed in this energy estimate.

The required regularity and domain assumptions are those used in the existing transport-generation theory.

---

## Reference R2 — Existence of the frozen \(L^2\) inverse

**Status: Existing proof under global flow and natural-domain assumptions.**

Let

\[
W_k=V+U[k].
\]

Assume \(W_k\) is globally Lipschitz and has at most linear growth, so that its complete flow exists.

The operator

\[
h\mapsto W_k\cdot\nabla h
\]

has its natural \(L^2\) transport domain

\[
D_k=
\{h\in L^2:W_k\cdot\nabla h\in L^2
\text{ distributionally}\}.
\]

The remaining operator

\[
h\mapsto-h+U[h]\cdot\nabla\bar\rho
\]

is bounded on \(L^2\), provided \(\nabla\bar\rho\in L^\infty\).

Thus \(\mathcal A_k\) generates the appropriate \(L^2\) evolution.

Using (R1.2) and extending the energy inequality from the common smooth core to the natural domain gives

\[
\|e^{t\mathcal A_k}\|_{2\to2}
\le e^{-\beta_0t}.
\]

Consequently,

\[
\boxed{
h_k=\int_0^\infty e^{t\mathcal A_k}F\,dt
}
\tag{R2.1}
\]

is the unique \(L^2\) solution of

\[
\mathcal A_kh_k=-F.
\]

It satisfies

\[
\boxed{
\|h_k\|_2
\le\frac{\|F\|_2}{\beta_0}.
}
\tag{R2.2}
\]

The time variable here is merely a construction tool for the stationary inverse.

The final theorem is stationary.

**Do not re-prove the semigroup construction.**

The only new task is to use this already constructed \(L^2\) solution in the new \(C^{1,\alpha}\) regularity argument.

---

## Reference R3 — Origin normalization is preserved

**Status: Existing proof.**

The background satisfies

\[
\bar c_l+\partial_y\bar u_2(0)=1.
\]

Let

\[
a_0=\bar\rho_y(0)>0,
\qquad
b=2\bar c_l-1.
\]

The background transport linearization is

\[
\boxed{
DV(0)=
\begin{pmatrix}
b&0\\
0&1
\end{pmatrix}.
}
\tag{R3.1}
\]

S1 symmetry implies

\[
U[k](0)=0
\]

and

\[
\boxed{
DU[k](0)=
\begin{pmatrix}
-\ell(k)&0\\
0&\ell(k)
\end{pmatrix}.
}
\tag{R3.2}
\]

For \(k,h\in C^{1,\alpha}\), first-order Taylor expansion gives

\[
\boxed{
\partial_y\bigl(U[k]\cdot\nabla h\bigr)(0)
=
\ell(k)h_y(0).
}
\tag{R3.3}
\]

Similarly,

\[
\boxed{
\partial_y(\mathcal Lh)(0)
=
a_0\ell(h).
}
\tag{R3.4}
\]

Therefore, if

\[
\mathcal A_kh=-F,
\]

then

\[
\boxed{
a_0\ell(h)+\ell(k)h_y(0)=-F_y(0).
}
\tag{R3.5}
\]

If

\[
\ell(k)=0,\qquad F_y(0)=0,
\]

we conclude

\[
\boxed{\ell(h)=0.}
\tag{R3.6}
\]

Thus the frozen map preserves the normalization once the output has the necessary \(C^1\) regularity.

No second derivative of \(k\) or \(h\) is required for this identity.

**This step is complete. Do not re-prove it.**

---

## Reference R4 — \(L^2\)–\(C^{1,\alpha}\) interpolation

**Status: Existing proof with explicit constants.**

Let

\[
H=[\nabla h]_{C^\alpha},
\qquad
0<\alpha<1.
\]

The previous proof uses a first-moment identity on a two-dimensional ball to obtain, for every \(r>0\),

\[
\boxed{
\|\nabla h\|_\infty
\le
A\|h\|_2r^{-2}
+B_\alpha Hr^\alpha,
}
\tag{R4.1}
\]

where one possible set of constants is

\[
A=\frac2{\sqrt\pi},
\qquad
B_\alpha=
\frac{16}{\pi(1+\alpha)(4+\alpha)}.
\]

Optimizing \(r\) gives

\[
\boxed{
\|\nabla h\|_\infty
\le
C_\alpha
\|h\|_2^{\alpha/(2+\alpha)}
[\nabla h]_{C^\alpha}^{2/(2+\alpha)}.
}
\tag{R4.2}
\]

The explicit constant may be taken from the existing report.

Similarly, if

\[
\|k\|_2\le R,\qquad
H_{\sigma,\alpha}(k)\le M,
\]

ordinary Riesz-transform estimates imply

\[
\|U[k]\|_2\le R
\]

and

\[
[\nabla U[k]]_{C^\alpha}
\le C_{\alpha,\sigma}(R+M).
\]

Applying (R4.2) to \(U[k]\),

\[
\boxed{
\|\nabla U[k]\|_\infty
\le
C_{\alpha,\sigma}
R^{\alpha/(2+\alpha)}
(R+M)^{2/(2+\alpha)}.
}
\tag{R4.3}
\]

In particular, with \(M\) fixed,

\[
R\to0
\quad\Longrightarrow\quad
\|\nabla U[k]\|_\infty\to0.
\]

However, small \(R\) with bounded \(M\) does not necessarily imply

\[
[\nabla U[k]]_{C^\alpha}\to0.
\]

This distinction is important for the new research.

### The unresolved implication

The interpolation estimates are established.

What is not established is whether the full stationary \(C^{1,\alpha}\) inverse requires smallness of the entire \(C^{1,\alpha}\) deformation or only smallness of \(\|\nabla U[k]\|_\infty\), together with finite higher Hölder control.

**Do not spend time re-proving interpolation. Investigate the unresolved inverse implication.**

---

## Reference R5 — Conditional nonlinear fixed-point theorem

**Status: Existing mathematical proof; high-regularity invariance remains an assumption.**

Define

\[
R=\frac{\|F\|_2}{\beta_0}
\]

and

\[
\boxed{
\mathcal K_{R,M}
=
\left\{
k:
\begin{array}{l}
k\text{ satisfies S1},\\
\ell(k)=0,\\
\|k\|_2\le R,\\
H_{\sigma,\alpha}(k)\le M
\end{array}
\right\}.
}
\tag{R5.1}
\]

Here

\[
H_{\sigma,\alpha}(k)
=
\|\langle X\rangle^\sigma k\|_{C^{1,\alpha}}.
\]

Define

\[
\boxed{
T(k)=-\mathcal A_k^{-1}F.
}
\tag{R5.2}
\]

Assume that the frozen inverse is well-defined and that

\[
\boxed{
H_{\sigma,\alpha}(T(k))\le M
\qquad\text{for all }k\in\mathcal K_{R,M}.
}
\tag{R5.3}
\]

Then \(T\) maps \(\mathcal K_{R,M}\) into itself.

The \(L^2\) constraint follows from (R2.2).

The normalization follows from (R3.6).

### Proof of weak compactness

The set \(\mathcal K_{R,M}\) is convex and bounded in \(L^2\).

A sequence in the set that converges weakly in \(L^2\) has, by the uniform weighted \(C^{1,\alpha}\) bound, locally convergent subsequences in \(C^{1,\beta}\) for every \(\beta<\alpha\).

The local limits agree with the weak \(L^2\) limit in the distributional sense.

The Hölder bound passes to the limit by lower semicontinuity, while the \(L^2\) bound passes by weak lower semicontinuity.

The origin normalization passes through local convergence of the associated velocities.

Thus \(\mathcal K_{R,M}\) is weakly closed.

Since \(L^2\) is reflexive and the set is bounded, it is weakly compact.

### Proof of weak continuity

Let

\[
k_n\rightharpoonup k
\quad\text{in }L^2,
\]

with \(k_n\in\mathcal K_{R,M}\).

Uniform high-regularity bounds and Riesz estimates give local convergence of the velocities:

\[
U[k_n]\longrightarrow U[k]
\]

in a lower Hölder topology, after subsequence extraction.

Let

\[
h_n=T(k_n).
\]

The uniform \(L^2\) and high-regularity bounds allow extraction of a weak \(L^2\) subsequential limit \(h\).

In the distributional equation,

\[
\mathcal Lh_n+U[k_n]\cdot\nabla h_n=-F,
\]

the nonlinear frozen transport can be written

\[
U[k_n]\cdot\nabla h_n
=
\nabla\cdot(h_nU[k_n]).
\]

The strong local convergence of \(U[k_n]\) and weak \(L^2\) convergence of \(h_n\) allow passage to the limit.

Therefore

\[
\mathcal A_kh=-F.
\]

Uniqueness of the \(L^2\) solution gives

\[
h=T(k).
\]

Thus \(T\) is weakly continuous on the weakly compact convex set.

Schauder–Tychonoff gives a fixed point

\[
\boxed{T(h)=h.}
\]

The fixed point satisfies

\[
\boxed{
\mathcal Lh+U[h]\cdot\nabla h=-F.
}
\]

### Important consequence

**Existence does not require contraction in \(C^{1,\alpha}\), or even contraction in \(L^2\).**

It only requires the invariant high-regularity set and the existing frozen \(L^2\) theory.

This entire conditional fixed-point mechanism is established.

**Do not re-prove it in the new campaign.**

### Optional uniqueness

For two frozen states,

\[
\mathcal A_k(T(k)-T(l))
=
-U[k-l]\cdot\nabla T(l).
\]

Therefore,

\[
\boxed{
\|T(k)-T(l)\|_2
\le
\frac{\|\nabla T(l)\|_\infty}{\beta_0}
\|k-l\|_2.
}
\tag{R5.4}
\]

If the gradient factor is smaller than one, this gives contraction and uniqueness within the set.

But this is not required for the existence theorem.

---

## Reference R6 — Exact frozen-origin inverse

**Status: Existing frozen-model results; do not mistake them for a full variable-coefficient inverse.**

Let

\[
\boxed{
\mathcal L_{\mathrm{fr}}
=
bx\partial_x+y\partial_y-1+a_0R_1^2,
\qquad b=2\bar c_l-1>1.
}
\]

Set

\[
d=b-1.
\]

In Fourier variables, the equation

\[
\mathcal L_{\mathrm{fr}}h=-F
\]

becomes

\[
\left(
b\xi_1\partial_{\xi_1}
+\xi_2\partial_{\xi_2}
+b+2
+a_0\frac{\xi_1^2}{|\xi|^2}
\right)\widehat h
=
\widehat F.
\]

Its unique \(L^2\) solution has the exact representation

\[
\boxed{
\begin{aligned}
\widehat h(\xi)
=
\int_0^\infty
&e^{-(b+2)t}
\left(
\frac{e^{-2dt}\xi_1^2+\xi_2^2}
{|\xi|^2}
\right)^{a_0/(2d)}
\\
&\times
\widehat F(e^{-bt}\xi_1,e^{-t}\xi_2)\,dt.
\end{aligned}
}
\tag{R6.1}
\]

The exact signed energy identity is

\[
\boxed{
-\operatorname{Re}
\langle\mathcal L_{\mathrm{fr}}h,h\rangle
=
\frac{b+3}{2}\|h\|_2^2
+a_0\|R_1h\|_2^2.
}
\tag{R6.2}
\]

Therefore

\[
\boxed{
\|h\|_2\le\frac2{b+3}\|F\|_2.
}
\]

The earlier analysis also showed that the unrestricted same-order inverse

\[
L^2\cap C^{1,\alpha}
\longrightarrow
L^2\cap C^{1,\alpha}
\]

is not bounded for all sources, even with the positive \(a_0\) structure.

The obstruction comes from near-vertical frequency packets under anisotropic stationary frequency transport.

This negative result must not be confused with failure of the inverse for more regular or specially structured sources.

### Asymmetric source regularity

Let

\[
s=1+\alpha,
\qquad
\kappa_{\rm ang}=\frac{\alpha}{b-1}.
\]

For sufficiently strong angular damping,

\[
\boxed{
a_0>b(1+\alpha)-1,
}
\tag{R6.3}
\]

the previous frozen-model result allows stronger source regularity to produce \(C^{1,\alpha}\) output.

In particular, for

\[
\kappa_{\rm ang}<\delta<1,\qquad 1<\nu<2,
\]

a previously established estimate has the form

\[
\boxed{
\|\mathcal L_{\mathrm{fr}}^{-1}F\|_{C^{1,\alpha}}
\le
C\|\langle X\rangle^\nu F\|_{C^{1+\alpha+\delta}}.
}
\tag{R6.4}
\]

A useful starting choice is

\[
\alpha=\frac12,\qquad
\delta=0.4,\qquad
\nu=\frac74.
\]

This gives

\[
\boxed{
\|\mathcal L_{\mathrm{fr}}^{-1}F\|_{C^{1,1/2}}
\le
C\|\langle X\rangle^{7/4}F\|_{C^{1.9}}.
}
\]

This is a frozen-origin result.

It is not yet the full variable-coefficient inverse theorem.

The previous proof used angular frequency localization, horizontal-frequency uncertainty bounds, and the exact resolvent representation.

**Read and reuse that proof. Do not derive the Fourier representation again.**

---

## Reference R7 — The IPM velocity cancels part of the angular loss

**Status: Previously established frozen-model special-source estimate.**

The velocity multiplier is

\[
m(\xi)=
\left(
\frac{\xi_1\xi_2}{|\xi|^2},
-\frac{\xi_1^2}{|\xi|^2}
\right).
\]

Near the vertical frequency axis, put

\[
q=\frac{|\xi_1|}{|\xi|}.
\]

Then

\[
|m_1(\xi)|\lesssim q,\qquad
|m_2(\xi)|\lesssim q^2.
\]

The frozen inverse has an angular loss of order

\[
q^{-\kappa_{\rm ang}},
\qquad
\kappa_{\rm ang}=\frac{\alpha}{b-1}.
\]

Consequently, composition with a velocity component produces

\[
q^{m-\kappa_{\rm ang}}
\]

for \(m=1\) or \(m=2\).

When

\[
\kappa_{\rm ang}<1,
\]

the angular decomposition can be summed.

This yields the previously established estimate

\[
\boxed{
\|\mathcal L_{\mathrm{fr}}^{-1}U_i[f]\|_{C^{1,\alpha}}
\le
C_{a_0,b,\alpha}
\left(
\|f\|_2+\|f\|_{C^{1,\alpha}}
\right),
\quad i=1,2,
}
\tag{R7.1}
\]

provided the corresponding damping condition (R6.3) holds.

The proof uses the exact resolvent, anisotropically rescaled angular multipliers, and an integrable angular factor.

It does not require

\[
f\in\mathcal W_{s,\lambda},
\]

and does not require \(D^2f\).

For a fixed sufficiently smooth coefficient \(a(X)\), the previous analysis also obtained localized estimates for

\[
\mathcal L_{\mathrm{fr}}^{-1}(aU_i[f])
\]

using the identity

\[
aU_i[f]=U_i[af]+[a,U_i]f.
\]

The commutator gains one order locally, while the first term retains the velocity multiplier's angular zero.

This is especially relevant to the good-unknown equation below.

**Do not re-prove the frozen special-source estimate. Extend its mechanism to the actual full operator.**

---

## Reference R8 — Good unknown and existing low-norm perturbation estimate

Let

\[
h_0=-\mathcal L^{-1}F,
\qquad
h_k=-\mathcal A_k^{-1}F.
\]

Set

\[
z_k=h_k-h_0.
\]

The exact difference equation is

\[
\boxed{
\mathcal A_kz_k=-U[k]\cdot\nabla h_0.
}
\tag{R8.1}
\]

This identity is the preferred starting point for small-\(k\) regularity.

If

\[
\nabla h_0\in L^\infty,
\]

the signed \(L^2\) inverse immediately gives

\[
\boxed{
\|z_k\|_2
\le
\frac{\|\nabla h_0\|_\infty}{\beta_0}
\|k\|_2.
}
\tag{R8.2}
\]

This part is complete.

The unresolved problem is to upgrade this bound to a useful \(C^{1,\alpha}\) estimate.

Previous analysis also identified a covariant principal-symbol cancellation near the S1 symmetry axis.

After straightening the weak expansion direction, the special source symbol satisfies a bound of the schematic form

\[
\boxed{
\left|
m(D\Phi^T\xi)\cdot\nabla h_0
\right|
\lesssim
\left|\frac{\xi_1}{|\xi|}\right|^2
+|Y|^{2\alpha}.
}
\tag{R8.3}
\]

Here \(\Phi=(x,Y)\) is the local weak-direction coordinate transformation.

This is a proved algebraic/principal-symbol observation in the previous analysis.

**It is not yet a complete stationary inverse estimate.**

The new theory work must quantify the combined effect of:

- The special-source cancellation.
- The complete frozen transport.
- The conjugated Riesz operator.
- The variable coefficients.
- The unique global \(L^2\) solution condition.

Do not infer the complete estimate from the principal symbol alone.

---

## Reference R9 — Exterior weighted \(C^{1,\alpha}\) lifting

**Status: Existing conditional result under explicit background decay and flow assumptions.**

Assume the background has the expected far-field envelopes.

Let

\[
\gamma=1-\frac1{\bar c_l}>0.
\]

The useful bounds are of the form

\[
\frac{|\bar u(X)|}{|X|}
+
|D\bar u(X)|
+
[D\bar u]_{C^\alpha(B_1(X))}
\lesssim \langle X\rangle^{-\gamma},
\]

and

\[
\|\nabla\bar\rho\|_{C^{1,\alpha}(B_1(X))}
\lesssim\langle X\rangle^{-\gamma}.
\]

These background bounds must eventually be checked for the actual numerical reference.

For the frozen equation,

\[
(W_k\cdot\nabla-1)h
+
\nabla\bar\rho\cdot U[h]
=-F,
\]

the outward flow gives the stationary characteristic representation

\[
\boxed{
h(X)=
\int_0^\infty
e^{-t}
\left(
F+\nabla\bar\rho\cdot U[h]
\right)(\Phi_tX)\,dt,
}
\tag{R9.1}
\]

in the exterior, with the terminal term removed using the global \(L^2\) condition.

Let

\[
w_\sigma=\langle X\rangle^\sigma.
\]

After conjugation by the weight, the transport damping coefficient is

\[
1+\sigma
\frac{W_k(X)\cdot X}{1+|X|^2}.
\]

A sufficient weighted Hölder margin is

\[
\boxed{
\mu_R=q_0-(1+\alpha)L_R>0,
}
\]

where \(q_0\) is the lower bound of the conjugated damping and \(L_R\) controls the exterior flow deformation.

In the pure dilation limit,

\[
\boxed{
\mu_\infty=1+\bar c_l(\sigma-1-\alpha).
}
\tag{R9.2}
\]

Thus choosing

\[
\sigma=\frac74
\]

gives a favorable margin for \(0<\alpha<1\) at the current parameter.

The nonlocal term requires care.

The same-weight Riesz estimate is not generally valid without loss. The established exterior estimate has a logarithmic factor,

\[
\|U[f]\|_{C^{1,\alpha}(B_{1/4}(X))}
\lesssim
\langle X\rangle^{-\sigma}
(1+\log\langle X\rangle)
H_{\sigma,\alpha}(f).
\]

The decay of \(\nabla\bar\rho\) then gives

\[
\boxed{
\|\chi_Rw_\sigma\nabla\bar\rho\cdot U[f]\|_{C^{1,\alpha}}
\le
\eta_RH_{\sigma,\alpha}(f),
}
\]

where

\[
\boxed{
\eta_R\lesssim
R^{-\gamma}(1+\log R)\to0.
}
\tag{R9.3}
\]

For large \(R\), this permits a Neumann-series treatment of the exterior nonlocal coupling.

The previous result consequently gives an estimate of the form

\[
\boxed{
\begin{aligned}
H_{\sigma,\alpha}(h)
\le C_R\bigl(
&\|w_\sigma F\|_{C^{1,\alpha}(|X|>R)}\\
&+\|h\|_{C^{1,\alpha}(B_{2R})}
+\|h\|_2
\bigr).
\end{aligned}
}
\tag{R9.4}
\]

This is a regularity-lifting result for the unique \(L^2\) solution, conditional on the background and flow assumptions.

**Do not rebuild the exterior proof. Verify the hypotheses numerically and use the result.**

---

## Reference R10 — Finite-annulus propagation

**Status: Existing conditional proof.**

Suppose \(h\) is already \(C^{1,\alpha}\) in a neighborhood of the origin and the relevant finite annuli are covered by finite flow tubes.

The previous proof uses flow-adapted cutoffs

\[
\chi_t=\chi_0\circ\Phi_{-t}.
\]

Because

\[
(\partial_t+W_k\cdot\nabla)\chi_t=0,
\]

the localized equation has the exact form

\[
\boxed{
(\partial_t+\mathcal A_k)(\chi_th)
=
-\chi_tF
+
\nabla\bar\rho\cdot[U,\chi_t]h,
}
\tag{R10.1}
\]

with the indicated commutator convention.

There is no uncontrolled principal transport cutoff term.

The nonlocal commutator gains one order locally because its kernel contains the factor

\[
\chi_t(Y)-\chi_t(X).
\]

The previous proof uses nested cutoffs and intermediate Sobolev/Hölder spaces to propagate regularity from the known region through a finite flow tube.

It obtains a bound of the form

\[
\boxed{
\begin{aligned}
\|h\|_{C^{1,\alpha}(K)}
\le C_{\rm tube}\bigl(
&\|h\|_{C^{1,\alpha}(\Omega_0)}\\
&+\|F\|_{C^{1,\alpha}(\text{flow tube})}
+\|h\|_2
\bigr).
\end{aligned}
}
\tag{R10.2}
\]

The constant depends on finite flow time, geometric separation and first-order Hölder bounds on the velocity, not on \(D^2k\).

A convenient sufficient geometric condition is

\[
W_k(X)\cdot X\ge\nu|X|^2
\]

across the required annular region.

Uniform flow-tube coverage is sufficient even if this stronger radial inequality is unavailable.

**Do not repeat the nested-cutoff proof. Use its established conditional conclusion.**

---

## Reference R11 — Local geometry and the remaining obstruction

For a normalized perturbation,

\[
DU[k](0)=0.
\]

Near the origin,

\[
W_k(X)=BX+v(X),
\qquad
B=\operatorname{diag}(b,1),
\]

with

\[
v(0)=Dv(0)=0.
\]

The previous work constructed a local \(C^{1,\alpha}\) weak-direction coordinate

\[
Y(X)=
\lim_{t\to\infty}
e^t\Psi_{t,2}(X),
\]

where \(\Psi_t\) is the backward flow.

It satisfies

\[
W_k\cdot\nabla Y=Y.
\]

In coordinates

\[
\Phi(X)=(x,Y(X)),
\]

the transport field takes the triangular form

\[
\boxed{
Z(z)=
\bigl(z_1[b+\widetilde a(z)],z_2\bigr).
}
\tag{R11.1}
\]

The coordinate construction only requires first-order Hölder control of the velocity.

The previous analysis also obtained ordinary \(C^{1,\alpha}\) estimates for the conjugated Riesz operator under the corresponding small coordinate perturbation.

However, a crucial distinction was discovered:

**The angular Fourier norm of a source need not remain uniformly bounded after the nonlinear coordinate change, even if \(k\) is arbitrarily small in the ordinary weighted \(C^{1,\alpha}\) solution space.**

An explicit counterexample was constructed for that intermediate estimate.

This does not disprove the complete inverse \(\mathcal A_k^{-1}F\).

It proves that one cannot separately estimate the transformed source, transport, and Riesz terms in the old angular Fourier norm and then automatically combine the estimates.

The correct remaining problem is a **joint stationary inverse estimate** retaining the cancellations among these terms.

Do not redo the coordinate-change counterexample.

Do not infer that the full inverse fails.

---

## Reference R12 — What is already closed, and what remains open?

### Existing conditional results

- Signed \(L^2\) coercivity.
- Construction and uniqueness of the frozen \(L^2\) inverse.
- Origin normalization identity.
- \(L^2\)–Hölder interpolation.
- Weak \(L^2\) fixed-point mechanism.
- Exact frozen-origin resolvent.
- Asymmetric frozen-origin source-to-solution estimates.
- Frozen-origin special IPM velocity-source estimates.
- Conditional finite-annulus propagation.
- Conditional weighted exterior regularity lifting.

### Genuinely open tasks

**O1. Full \(k=0\) regularity lifting**

For the unique global \(L^2\) solution,

\[
\mathcal Lh_0=-F,
\]

prove a weighted \(C^{1,\alpha}\) estimate using the stronger regularity of the known source \(F\).

**O2. Uniform small-\(k\) regularity lifting**

For

\[
\mathcal A_kh_k=-F,
\]

prove a bound on \(H_{\sigma,\alpha}(h_k)\) uniform over the prescribed normalized \(k\)-set.

**O3. High-norm invariant-ball closure**

Derive explicit dependence on \(R,M,F\) and prove that a finite \(M\) satisfies

\[
H_{\sigma,\alpha}(T(k))\le M.
\]

**O4. Numerical verification**

Certify the background bounds, strong residual norm, flow geometry and final scalar inequalities for a numerical reference.

**O5. Optional regularity bootstrap**

If the final theorem requires a smooth rather than a \(C^{1,\alpha}\) stationary profile, establish the additional bootstrap.

The new theory team should concentrate on O1–O3.

The numerical team should concentrate on improving the reference and certifying the quantities needed for O4.

---

# PART III — THEORY TEAM: NEW RESEARCH ONLY

## 13. Research target

The main objective is to establish

\[
\boxed{
\mathcal A_k^{-1}:
Y_F\longrightarrow X_{\sigma,\alpha},
}
\]

uniformly for a suitable normalized \(k\)-set, with

\[
X_{\sigma,\alpha}
=
L^2\cap w_\sigma^{-1}C^{1,\alpha}.
\]

The source space \(Y_F\) can be stronger.

Initially consider

\[
Y_F=
L^2\cap w_\sigma^{-1}C^{1+\alpha+\delta}.
\]

Do not require \(h\in Y_F\).

Do not require \(h\) or \(k\) to belong to the earlier angular Fourier space \(\mathcal W\).

### First objective: close O1

Prove that the unique global \(L^2\) solution of

\[
\mathcal Lh_0=-F
\]

belongs to weighted \(C^{1,\alpha}\).

Use the existing frozen-origin estimate and the fixed analytic background.

Strong derivatives of the known background are allowed.

Do not repeat the frozen Fourier analysis.

The challenge is extending the known frozen regularity to the complete variable-coefficient operator.

### Second objective: close O2

For small normalized \(k\), use

\[
\mathcal A_k(h_k-h_0)
=
-U[k]\cdot\nabla h_0.
\]

Exploit the special IPM velocity-source angular cancellation, the good unknown, and the complete stationary transport.

Try to prove

\[
\boxed{
H_{\sigma,\alpha}(h_k-h_0)
\le
\eta(R,M;F)M,
}
\]

with a favorable smallness structure.

Do not require this exact form if a weaker estimate is sufficient for invariance.

### Third objective: close O3

Try to establish

\[
\boxed{
H_{\sigma,\alpha}(T(k))
\le
A_F+\eta(R,M)M,
}
\tag{13.1}
\]

where

\[
\eta(R,M)<1.
\]

The ideal result has

\[
\eta(R,M)\to0
\quad\text{as }R\to0
\]

for fixed finite \(M\).

Then choose

\[
M\ge\frac{A_F}{1-\eta(R,M)}.
\]

This gives the invariant ball and, by Reference R5, existence.

### Main strategic preference

Try to make the theorem require only

\[
\|F\|_2\text{ sufficiently small},
\]

while allowing the stronger source norm to be finite but not necessarily tiny.

If this is impossible, formulate the sharpest quantitative tradeoff.

---

## 14. Optimize all theoretical parameters

Do not fix the initial parameter choices.

Optimize

\[
\alpha,\qquad
\delta,\qquad
\sigma,
\]

together with localization radii, interpolation constants, background bounds and all other free proof parameters.

Initial values are

\[
\alpha=0.5,\qquad
\delta=0.4,\qquad
\sigma=1.75.
\]

They are only a starting point.

Use the restrictions established by the existing frozen and exterior theory.

In particular, account for

\[
\delta>\frac{\alpha}{2\bar c_l-2}
\]

in the ordinary stronger-source frozen estimate.

Optimize the actual closure margin, not merely the size of a single inverse constant.

The theory team must continuously provide the numerical team with:

- The currently permitted \(\|F\|_2\).
- The allowable strong residual norm.
- Required background inequalities.
- Required origin and far-field bounds.
- The most sensitive constants.
- Which candidate changes would meaningfully improve closure.

---

# PART IV — NUMERICAL TEAM

## 15. Candidate 007 reference

Use the exact rational Candidate 007 snapshot:

`C1-N1-007-d2w-j7-e2bal`

Expected reference file:

`Changhe/IPM/combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json`

Confirm its actual path and content hash.

Its potential representation is

\[
\boxed{
\chi=
\sum_{j,m,k}
a_{jmk}
r^{2k}(1+r^2)^{p_j-k}\cos(2m\theta),
}
\]

where

\[
p_j=\frac{3+\gamma-j\delta}{2},
\qquad
\gamma=\frac1{\bar c_l},
\qquad
\delta=1-\gamma.
\]

The density and velocity are

\[
\boxed{
\bar\rho=-\partial_y\Delta\chi,
\qquad
\bar u=(-\chi_{xyy},\chi_{xxy}).
}
\]

Candidate 007 contains 2,982 generators and 1,922 nonzero canonical coefficients.

It has eleven exactly canceled forbidden residual far-field sectors.

The accepted numerical reference uses exact rational coefficients.

Use the exact coefficient strings for every structural verification.

Do not use rounded binary64 coefficients as the authoritative reference.

Current benchmark:

\[
\boxed{
\|F_{\rm007}\|_2\approx0.3766893247.
}
\]

The numerical team should obtain other baseline values from the existing records rather than recomputing every historical certificate.

---

## 16. Numerical workstream N1 — Existing basis

Continue optimization in the existing basis.

Primary objective:

\[
\boxed{\min\|F\|_2^2.}
\]

Investigate objective reweighting, constraint elimination, conditioning, Gauss–Newton/LM strategies, and better exploitation of the existing coefficients.

Keep exact far-field and origin constraints.

Pay particular attention to the intermediate radial region.

Previous experiments indicated that approximately 43% of Candidate 007's squared \(L^2\) residual lies in

\[
4\le r<8.
\]

This is a useful diagnostic, not a reason to ignore the rest of the plane.

Record the effect of optimization on the strong Hölder residual norm.

Do not allow the optimizer to reduce \(L^2\) residual by producing an inadmissible far-field tail.

---

## 17. Numerical workstream N2 — Basis expansion

Continue with the same \(\chi\)-based representation initially.

Allow:

- More angular modes.
- More radial modes.
- More localized scales.
- Joint optimization of old and new coefficients.
- Adaptive basis refinement guided by residual localization.

Previous experiments with added high angular modes reduced \(\|F\|_2\) but did not consistently improve the old composite high-order residual norm.

Under the new theoretical framework, such candidates may be useful.

Explore both existing-mode optimization and new-mode expansion.

Preserve the exact stationary far-field constraints.

Do not replace the basis wholesale unless there is concrete evidence that the current representation has become the main bottleneck.

---

## 18. The new strong residual norm

In addition to \(\|F\|_2\), measure

\[
\boxed{
S_F(\alpha,\delta,\sigma)
=
\|\langle X\rangle^\sigma F\|_{C^{1+\alpha+\delta}}.
}
\]

For the initial parameters,

\[
\boxed{
S_F=
\|\langle X\rangle^{7/4}F\|_{C^{1.9}}.
}
\]

The exact choice of \(\alpha,\delta,\sigma\) will be optimized by the theory team.

The numerical team should implement a flexible evaluator, not hard-code only one norm.

For noninteger Hölder order, do not replace the actual global Hölder seminorm with a grid maximum without accounting for the unobserved scales.

A useful rigorous sufficient estimate may be derived from explicit higher Cartesian derivatives, analytic interval bounds, and far-field decay estimates.

Initially estimate the strong norm numerically for feasibility.

Certify it only for promising candidates and when the theoretical theorem makes its role clear.

---

# PART V — COORDINATOR

## 19. Continuous two-way interaction

The coordinator is responsible for making the two research lines converge.

At least every four hours, collect from both teams:

**Theory:**

- Strongest theorem proved.
- Remaining analytical lemma.
- Current admissible residual threshold.
- Optimized theoretical parameters.
- Background constants required.
- Sensitivity of closure to each norm.

**Numerics:**

- Best \(\|F\|_2\).
- Best strong Hölder residual norm.
- Best Pareto candidates.
- Basis size and objective changes.
- Numerical conditioning and optimization bottlenecks.
- Failed structural constraints.
- Background certification status.

Then actively update priorities.

For example, if theory shows that \(S_F\) only needs to be finite, numerical work should emphasize \(\|F\|_2\).

If theory finds that large \(S_F\) severely reduces the allowable \(L^2\) threshold, numerical work should optimize a suitable combined objective.

If numerics finds a background bound consistently too large, theory should attempt to weaken that requirement or exploit additional sign structure.

Do not let the teams work independently for the full 48 hours without quantitative feedback.

---

## 20. Shared closure ledger

Maintain a live ledger containing:

\[
\boxed{
\bar c_l,\quad
a_0,\quad
\beta_0,\quad
\|F\|_2,\quad
S_F,\quad
\alpha,\delta,\sigma,\quad R,\quad M.
}
\]

Include all other binding background and inverse constants.

For every theorem condition, record:

- Exact inequality.
- Proven analytical threshold.
- Current numerical value or enclosure.
- Certified or noncertified status.
- Remaining margin.
- Sensitivity to theory parameters.
- Which team can improve it.

The final objective is not simply minimizing \(\|F\|_2\).

It is making all inequalities simultaneously pass.

When a legitimate residual threshold is available, monitor

\[
\boxed{
\mathcal G=
\frac{\varepsilon_{\mathrm{theory}}}
{\|F\|_2}.
}
\]

Seek a rigorously certified ratio greater than one, together with closure of all other hypotheses.

Do not compute a definitive closure ratio from a conjectural theorem.

---

# PART VI — 48-HOUR EXECUTION

## Hours 0–4

- Establish workspace and coordinator.
- Register both teams and verification workers.
- Import the existing proof references without re-proving them.
- Confirm Candidate 007 and its numerical certificate history.
- Identify the exact remaining analytical and numerical tasks.

## Hours 4–12

Theory:

- Attack the \(k=0\) full stationary inverse.
- Develop the small-\(k\) perturbative argument.
- Begin parameter and constant optimization.

Numerics:

- Reoptimize the existing basis.
- Run initial basis-expansion experiments.
- Estimate the new \(C^{1+\alpha+\delta}\) residual norm.

## Hours 12–24

Theory:

- Prove the strongest available uniform \(C^{1,\alpha}\) lifting.
- Quantify the role of small \(\|\nabla U[k]\|_\infty\).
- Attempt invariant-ball closure.

Numerics:

- Run the most promising optimizations.
- Improve basis conditioning.
- Track Pareto tradeoffs and background bounds.

Coordinator:

- Produce a substantive mid-campaign report.
- Reallocate effort based on the actual closure gap.

## Hours 24–36

- Refine the strongest proof and its constants.
- Optimize numerical candidates against the current theorem.
- Continue adaptive basis expansion where beneficial.
- Begin independent verification of promising candidates.
- Reevaluate the joint parameter choices.

## Hours 36–44

- Attempt rigorous theory–numerics closure.
- Certify binding quantities.
- Test invariant-ball inequalities.
- Independently check the decisive analytical steps.
- Quantify remaining gaps precisely.

## Hours 44–48

- Stop speculative major redesigns.
- Complete targeted independent audits.
- Save proof notes, candidate coefficients and optimizer checkpoints.
- Recompute the final closure ledger.
- Produce final reports and restart instructions.

Stop at the 48-hour wall-clock limit.

---

# PART VII — REQUIRED OUTPUT

Create the following reports.

### 1. `EXISTING_PROOFS_REFERENCE.md`

Copy the established reference structure from Part II, identify the authoritative original proof files, and record the exact assumptions.

This document is for reuse, **not a request to re-prove the lemmas**.

If inconsistencies are found, append a short targeted audit note.

### 2. `THEORY_NEW_RESULTS.md`

Contain only genuinely new theoretical results obtained during this campaign.

Give:

- New inverse and regularity estimates.
- Explicit constants.
- Optimized parameters.
- Invariant-ball conditions.
- Remaining open lemmas.
- Proofs of new results.
- Dependencies on the established reference lemmas.

Avoid restating the earlier proofs at length.

### 3. `NUMERICAL_OPTIMIZATION.md`

Record:

- Baseline Candidate 007.
- Existing-basis optimization.
- Basis expansion.
- \(L^2\) residual improvements.
- Strong Hölder residual values.
- Background constraints.
- Independent numerical checks.
- Best accepted candidate and Pareto alternatives.

### 4. `JOINT_CLOSURE_LEDGER.md`

List every requirement in the strongest theorem and its numerical status.

This must make it immediately clear whether a complete existence theorem has been certified.

### 5. `COORDINATOR_FINAL_REPORT.md`

Summarize:

- What the theory team actually proved.
- What the numerical team actually improved.
- How the teams communicated.
- How parameters were optimized.
- Whether theorem closure was obtained.
- The smallest remaining gap if not.
- Which work should continue next.

### 6. Restartable workspace

Save all significant proof notes, numerical candidate files, exact constraints, optimization states, reproducibility scripts and checkpoints.

---

# FINAL RESEARCH RULES

**Do not re-prove established results unless a concrete mathematical inconsistency is identified.**

In particular:

- Do not restart signed \(L^2\) theory.
- Do not rederive the frozen-origin Fourier formula.
- Do not redo the weak fixed-point argument.
- Do not spend time proving interpolation inequalities already recorded above.
- Do not reconstruct the exterior lifting proof from scratch.
- Do not demand that \(F,h,k\) belong to the same function space.
- Do not require the unknown correction to have the regularity of the known residual.
- Do not impose the old angular Fourier norm on \(h\) unless a new proof demonstrates that it is necessary.
- Do not require high-norm contraction when invariant-ball Schauder existence suffices.
- Do not claim that the full \(C^{1,\alpha}\) inverse follows from a frozen model estimate.
- Do not regard a numerical residual reduction as rigorous existence.
- Do not vary \(c_l\) during this fixed-parameter campaign.
- Do not change the authoritative Candidate 007 reference.

The main research effort should be directed toward

\[
\boxed{
\begin{gathered}
\text{Uniform stationary }C^{1,\alpha}\text{ lifting}\\
+\text{ high-norm invariant-ball closure}\\
+\text{ improved numerical residual}\\
+\text{ optimized theoretical parameters}.
\end{gathered}
}
\]

The coordinator must continuously compare the theoretical requirements against what the numerical team can actually achieve.

**The ultimate objective is not two separate advances. It is one complete, rigorously certified fixed-parameter stationary IPM existence theorem supported by a numerical reference.**
