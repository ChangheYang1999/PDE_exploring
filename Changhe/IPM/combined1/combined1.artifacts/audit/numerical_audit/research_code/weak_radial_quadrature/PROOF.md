# Matched radial rules for the exact first-mode weak pairing

## Candidate and target

Use the exact rational candidate C1-N1-007-d2w-j7-e2bal and its independently assembled first-sine residual projection

    F_1(r)=r sum_ell v^(ell delta/2) P_ell(t),
    t=r^2/(1+r^2), v=1-t, delta=1-1/c.

The canonical source and projection hashes identify the function. Every background-frequency interaction contributing to mode1 was retained when assembling the projection. The test phi_k=y t^k v^2 has continuum pairing

    I_k=integral_(R^2) F phi_k dX
       =(pi/2) sum_ell integral_0^1 v^(ell delta/2-1)(1-v)^(k+1) P_ell(1-v)dv.

The full-circle sine square integrates to pi. The formula follows by substituting r dr=d t/(2v^2) and r^2=t/v. The exact power-beta formula in ../localized_weak_probe/BETA_EVALUATION.md evaluates this finite integral without quadrature. Existing confirmed projection and beta identities are the dependencies; each new k value is still marked according to its peer status.

## The finite radial rule being tested

For positive radial nodes r_i and weights w_i approximating ds=dr/r, the analytically integrated angular pairing is

    Q_k=pi sum_i w_i t_i^(k+2) sum_ell v_i^(ell delta/2)P_ell(t_i).

This is exactly the previous integral's log-radius quadrature. The N1 finite radial rule uses20 equal panels between log(0.02) and16 and Gauss-Legendre nodes of the selected order per panel, then retains nodes with0.02<=r_i<=10000. This postfilter can retain a partial last panel. The checker recreates that rule independently using the stated formulas and NumPy's floating nodes. Each recorded binary64 radius and weight is then interpreted as an exact rational input to Arb. It does not certify the floating Gauss construction as an exact Gaussian rule.

The resulting ball Q_k encloses the finite weighted sum for those recorded nodes. The difference Q_k-I_k is therefore an enclosure of its total continuous-pairing error, including quadrature and both omitted radial domains. This calculation evaluates the exact rational candidate at the recorded nodes. It does not use N1's field evaluator or angular summation.

## Independent field evaluation and tail separation

For every polynomial P_ell, compose P_ell(1-v) exactly and evaluate that endpoint polynomial with outward coefficients. The code also evaluates P_ell(t) independently at each node and requires interval overlap. The two compositions are identical polynomials, so this check is an arithmetic consistency check. Summation over branches precedes pairing or error measurement. Require at least100relative accuracy bits in each nonzero radial residual amplitude.

For k in {0,1,2,4,8}, the omitted domains can be separated exactly. Expand the finite polynomial Z_ell(v)=(1-v)^(k+1)P_ell(1-v), set b=ell delta/2-1, and use

    A_(b,Z)(x)=x^(b+1) sum_j z_j x^j/(b+j+1),  A(0)=0.

For the nonzero candidate branches b>-1 is checked; every denominator is positive. The antiderivative identity is proved by termwise differentiation and continuity at0. With x_R=1/(1+R^2), the exterior pairing beyond R is(pi/2)sum_ell A_(b,Z)(x_R). The interior pairing below R is the full pairing minus that expression. Thus the exact middle pairing between1/50 and10000 is separated from both omitted domains. A quadrature error against that middle integral cannot be blamed on either omitted domain.

All rational powers, coefficients and moments are enclosed at2048bits. A manifest retains exact node and weight rationals, source hashes, proofs and helper implementations. Comparisons with N1's printed test log are diagnostic because its mesh fields are FLOAT and the log rounds their values. The new whole-plane values remain OPEN where no independent peer value is available. No optimization step or claim of existence follows from this audit.
