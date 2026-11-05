# Far-field analytic hypotheses and inherited numerical evidence

This note separates new analytic verification from inherited numerical conclusions. It does not describe an archived number as newly replayed.

## Actual coefficients and analytic hypotheses

The exact-input check `verify_structure013.py` binds the actual unchanged Candidate 007 and actual raw correction 013 by their SHA256 values, checks both exact exponents, verifies the original and elementary correction representations agree, and proves the origin normalization. `STRUCTURE013_PROOF.md` derives all-order background decay directly from those finite algebraic formulas.

Consequently the actual far scalar coefficient
\[
a_f=(1-\chi)\frac{4u_*\cdot X-c}{1+4|X|^2}
\]
is smooth, real, even in both coordinates, and belongs to \(S^{-\gamma}\), \(\gamma=1-1/c\in(0,1)\). The notation and erflog cut are exactly those of the inherited chain. The dyadic Fourier proof in `OPERATOR_BRIDGE_v01.md`, Lemma 6, proves that its transform is an ordinary locally integrable function with no point mass at zero and every nonnegative absolute Fourier moment finite.

At the exact inherited window \(R_w=W_w=200\), put
\[
w(r)=1-\operatorname{Sinf}((r-200)/200),\qquad
a_W=wa_f,\qquad a_t=(1-w)a_f.
\]
The usual flat exponential step Sinf is smooth, constant outside [0,1], and takes values in [0,1]. Thus a_W is smooth with compact support, its Fourier transform is Schwartz, and every derivative norm needed at orders 1 through 5 exists. The tail a_t retains the same all-order symbol decay, ordinary Fourier transform, and finite absolute moments. Its entire tail, without an outer truncation, is included in these statements.

The source/window identities used in the inherited route hold classically for these actual functions:

* Ordered derivatives satisfy the exact Leibniz formula, whose tensor-product Frobenius bound gives the stated binomial derivative-energy majorants.
* Derivatives of a radial window satisfy the exact Faà di Bruno set-partition formula, since the window transition stays away from r=0; the inner disk has a constant window.
* A positive continuous radial Schur weight bounded above and below on the finite band satisfies the admissibility hypothesis. The actual AE weight has these properties, and the clipped CS-B weight has them globally.
* Polar reflection reductions apply because the actual source is even in each coordinate. The angular Fourier decomposition is finite by the exact potential representation.
* Fourier kernel identities, integrations by parts, and the relevant Cauchy--Schwarz or Schur inequalities extend from test functions using the absolute moments just established. The continuum finite-band integral is finite, including the Riesz origin, under the inherited Lemma BOX majorants; no sampled value is used to justify this finiteness.

These arguments supply the qualitative smoothness, source calculus, Fourier integrability, matching-window and classical differentiation hypotheses retained as H-FA. They do not evaluate a derivative norm or verify a table's arithmetic.

## What is inherited numerically

Combined2 `theory_agent_2/notes/T2_PART7_v15.md`, section 2.2, and `IPM.report.md`, section A row 7, record the following as certified by the earlier theory and numerical auditors, within their explicitly retained input-containment assumptions:

| Input | Exact upper used in the existing far form |
|---|---|
| Windowed Hessian charge SC | 4194197216881219/9007199254740992 |
| Windowed Schur remainder S_W | 537734762519297/9007199254740992 |
| Entire tail OMF | 513586856047295/4503599627370496 |
| Windowed AE band upper | 5915921936389617/4503599627370496 |

The earlier independent audit entries are AT1366--1367, AT1598, AT1921--1922, AT1928--1929, AT1336--1338, and AT1891; the numerical-auditor adoptions of the Schur/window stage are exchanges v529 and v532. Their exact scalar sum is
\[
A_{far}=\max(SC,A_E)+S_W+OMF
=\frac{13396752347393121}{9007199254740992}.
\]
The continuum 324-subcell cover, including the necessary BOX origin bounds and the exceptional sinhc endpoint, is part of the inherited AE certificate. It is not inferred anew from a plotted or periodic eigenvalue.

The original source/window derivative tables, AE executor, and all original transitive hash-bound records are not published in the combined2 artifact subset. Hence the current campaign can inherit the accepted mathematical conclusions with their stated scopes, but cannot claim that this artifact subset alone replays those far certificates. A new standalone replay would require restoring the omitted inputs or reimplementing and recertifying the calculations. The new exact source check and analytic proof do not replace this distinction.

## Consequence in its exact scope

If these previously certified numerical upper bounds are inherited as the established results specified by the prompt, and the original input-containing arithmetic conclusions are retained, the analytic hypotheses above permit the actual far-form theorem to be applied to Candidate 013 at the same window. The accepted scalar comparison is then
\[
q\left(c-\frac{137}{125}\right)-A_{far}
=\frac{71675071190082633}{5629499534213120000}>0.
\]
Thus the original far scalar form is absorbed under that inherited global strain certificate. The strictly favorable numerical difference does not bound TIS, the velocity-source forms, or any uncharged near/far decomposition error. In a new decomposition that retains \(-qcJ^{-2}\) exactly, A_far can be charged directly to that damping, with the separately retained strain terms paid explicitly. It must not be charged twice.

This is an analytic discharge and assembly of inherited results. It is neither a fresh far numerical certificate nor an invariant-ball or existence theorem.
