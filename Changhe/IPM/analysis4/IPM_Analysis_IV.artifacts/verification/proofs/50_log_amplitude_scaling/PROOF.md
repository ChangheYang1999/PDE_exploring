# Amplitude and length scaling of logarithmic coefficients

Status: algebraic identities and explicit counterexample checked exactly. The all-order conclusions follow directly from uniqueness of the polynomial recurrence in topic10. No logarithmic convergence theorem is asserted.

## Statement

Fix c>1, delta=1-1/c, and a finite real odd-sine leading profile f_1. Let F_n(t,theta), G_n(t,theta) be the polynomial-log coefficients with every free resonant stream constant B_(n,j)(0) set to zero. Then, for every real epsilon,

\[
 F_n[\varepsilon f_1](t,\theta)=\varepsilon^n F_n[f_1](t,\theta),\qquad
 G_n[\varepsilon f_1](t,\theta)=\varepsilon^n G_n[f_1](t,\theta).
 \tag{1}
\]

A physical dilation with lambda>0 acts differently:

\[
 \rho_\lambda(X)=\lambda^{-1}\rho(\lambda X),\quad
 \psi_\lambda(X)=\lambda^{-2}\psi(\lambda X),\quad
 \chi_\lambda(X)=\lambda^{-4}\chi(\lambda X).
 \tag{2}
\]

Its coefficient transformation is

\[
 (F_n,G_n,C_n)(t)\longmapsto
 \lambda^{-n\delta}(F_n,G_n,C_n)(t+\log\lambda).
 \tag{3}
\]

In particular, its resonant free stream constant becomes

\[
 H_{n,j}^{\lambda}=\lambda^{-n\delta}B_{n,j}(\log\lambda).
 \tag{4}
\]

The canonical zero-constant family is therefore generally not preserved by physical dilation. For a pure series, the translation in (3) is absent, and amplitude scaling is exactly physical dilation with epsilon=lambda^(-delta). For logarithmic series, (1) still holds, but one cannot infer an exact physical exterior-radius scaling while keeping the same canonical constants.

## Proof of homogeneity

The leading coefficient scales linearly. Suppose (1) holds below order n. Every stationary forcing term is a product of one coefficient of order i and one of order n-i, with linear radial or angular derivatives. It scales by epsilon^n. The unique polynomial inverse of lambda_n-c partial_t is linear, so F_n scales by epsilon^n. The polynomial Poisson inverse is linear as well. At resonance its only polynomial kernel is the constant resonant harmonic, and the condition B_(n,j)(0)=0 is homogeneous. Thus G_n also scales by epsilon^n. Induction proves (1). The same argument works with prescribed constants H_(n,j) if those constants are themselves replaced by epsilon^n H_(n,j).

## Proof of the dilation law

Three derivatives of lambda^(-4) chi(lambda X) give lambda^(-1) times the original density or velocity evaluated at lambda X. Hence the potential identities are preserved. Moreover grad rho_lambda(X)=grad rho(lambda X), so

\[
 (cX+u_\lambda(X))\cdot\nabla\rho_\lambda(X)-\rho_\lambda(X)
 =\lambda^{-1}\left[(c\lambda X+u(\lambda X))\cdot\nabla\rho(\lambda X)-\rho(\lambda X)\right].
\]

This proves invariance of the full stationary equation. Substituting the powers p_n=1-n delta, P_n=2-n delta, q_n=4-n delta into (2) gives (3), and evaluation at t=0 gives (4).

More generally, the formal coefficient equations are invariant under the two-parameter transformation

\[
 (F_n,G_n)(t)\longmapsto\varepsilon^n(F_n,G_n)(t+s),
\]

because partial_t commutes with translation and every product has total order n. Physical dilation is the one-parameter subgroup epsilon=exp(-delta s). A translated sequence solves the recursion with its transformed resonant constants; it need not solve the zero-constant normalization.

## Explicit first-resonance example

At delta=2/3, c=3 and f_1=sin(theta), the first stream resonance occurs at n=6 and frequency 2. Its canonical coefficient is

\[
 B_{6,1}(t)=b_2t,\qquad
 b_2=-\frac{177047}{1204224000000}\ne0.
\]

Thus H^lambda_(6,1)=lambda^(-4)b_2 log(lambda), which is nonzero for lambda!=1. The canonical solution with leading profile lambda^(-2/3)sin(theta) instead has H_(6,1)=0. The density sequences first differ at order 7: their difference is the scaled translation of a nonzero linear-log coefficient. Topic44 gives that coefficient exactly, and the finite audit here recomputes it without using the top-degree formula.

## Consequence for radius statements

Introduce independent formal variables z and t and write

\[
 \mathcal F(z,t)=\sum_{n\ge1}z^{n-1}F_n(t).
\]

At fixed t, (1) says \(\mathcal F_\varepsilon(z,t)=\varepsilon\mathcal F(\varepsilon z,t)\), so the z-radius is divided by |epsilon| whenever that radius is defined. This is a statement with t fixed. The physical generalized series is evaluated on t=log(r), z=r^(-delta); a change of radius moves both variables. Accordingly the exact rule R_physical->|epsilon|^(1/delta)R_physical applies to the pure series, or to the full logarithmic family with its constants transformed by (4). It has not been established for canonical logarithmic amplitude scaling alone.

The theory part already states the dependence of the canonical normalization on the unit of length in Section14.1. Its earlier amplitude paragraph is correct in the pure-series setting. The numerical report's general opening radius statement should explicitly name that setting, or say that t is held fixed.

## Verification and dependencies

The exact audit constructs the logarithmic recurrence by Cartesian Laurent-polynomial differentiation, checks homogeneity for two rational amplitudes, and verifies both stationary and Poisson identities after two rational t-translations. It also records the nonzero transformed resonant constant and order-seven density difference. All formulas depend only on topic10's polynomial recurrence and the original potential equation; topic44 is used as a second reference for b_2. Reproduce with ../../code/log_amplitude_audit.py. Exact results and source hashes are in verification/checks.json.
