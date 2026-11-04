# Explicit synthesis of a quartic with a feasible Laplacian

Status: independent reconstruction and existing coordinator comparison complete. Exact verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md).

## 1. Statement and notation

Let C be any real symmetric three-by-three matrix. If C=lambda I, the quartic F=lambda|x|^4/20 has Delta F=x^T Cx and is nonnegative for lambda>=0. For nonscalar C with eigenvalues c_i, let mu, Z_+, Z_- be the unique real-root data

    mu>-min c_i,  Z_+Z_-=49,
    Z_+=sum sqrt(c_i+mu),  Z_-=sum (c_i+mu)^(-1/2).

Define by symmetric spectral calculus

    B=(C+mu I)^(-1/2)/Z_-,
    nu=1/Z_-^2>0,  m=49nu-mu,  A=B^-1-7I.

Then the explicit homogeneous quartic

    F_C(x)=(nu/8)(x^T A x)^2+(m/20)|x|^4               (1)

satisfies Delta F_C=x^T Cx. If m>=0 it is nonnegative. If m>0 it is at least (m/20)|x|^4 and positive away from0. At m=0 it is one square with positive coefficient. The direct sufficiency uses no Hilbert theorem or separation theorem.

With A2790, existence of any nonnegative homogeneous quartic preimage is equivalent to m>=0 in the nonscalar case and lambda>=0 in the scalar case. The first proof of necessity retains the explicit dependencies of A2790. The independent elementary cone proof in the team records supplies the same necessity without Hilbert or separation. No full Euler equation is assumed or inferred.

## 2. Root and spectral identities

For completeness, the root exists uniquely because p(mu)=Z_+Z_- decreases continuously from infinity to9. Differentiation gives 2p'=Z_-^2-Z_+ sum(c_i+mu)^(-3/2)<0, by Cauchy-Schwarz with equality only for constant c. Repeated eigenvalues cause no problem. The formula for B is independent of all eigenbasis choices because equal c_i give equal eigenvalues b_i of B.

The root equation yields

    tr B=1,  tr B^-1=49,
    C+mu I=nu B^-2,
    C=mI+nu(B^-2-49I),  tr A=49-21=28.                 (2)

To verify the relation to the dual minimum, take any beta_i>0 with sum beta_i=1 and sum1/beta_i<=49. Cauchy-Schwarz gives sum(c_i+mu)beta_i>=Z_+^2/49=49nu. Equality holds at the eigenvalues of B. Thus m is the eigenvalue minimum. Orthogonal-orbit variation forces a minimizing matrix to commute with C, as in the preceding independent scalar audit, so this is also the matrix minimum. This proves the needed minimum formula without a Lagrange-multiplier assumption.

## 3. Direct differentiation and signs

For symmetric A, put q=x^T Ax. The identities grad q=2Ax and Delta q=2tr A give

    Delta(q^2)=x^T(8A^2+4tr(A)A)x.

Using tr A=28 and A=B^-1-7I,

    8A^2+112A
      =8[(B^-1-7I)^2+14(B^-1-7I)]
      =8(B^-2-49I).                                   (3)

In three dimensions, differentiating (sum x_i^2)^2 gives Delta|x|^4=20|x|^2. Therefore (1), (2) and (3) imply

    Delta F_C=x^T[nu(B^-2-49I)+mI]x=x^T Cx.

For m>=0 both summands in (1) are nonnegative. The claimed strict radial lower bound for m>0 is immediate, and at m=0 only the square remains. For a nonscalar C at m=0, A cannot vanish: otherwise tr B^-1 would be21 rather than49. In the scalar case the stated formula follows directly from the radial differentiation. If lambda<0, no nonnegative quartic preimage exists, since integration over the sphere gives mean F=tr C/60=lambda/20<0.

## 4. Pressure certificate and exactness boundary

For any real homogeneous quadratic solenoidal Q and any real gamma, define C_gamma by

    x^T C_gamma x=-tr((DQ)^2)-gamma Delta|Q|^2.

When its scalar or nonscalar sign condition holds, let

    R=gamma|Q|^2+F_(C_gamma).

Then -Delta R=tr((DQ)^2) and R>=gamma|Q|^2 pointwise. The statement includes all directions x, not only tested points. The real root in the definition is specified exactly by its unique equation and interval. For algebraic input coefficients it may be represented algebraically; arbitrary real input need not produce algebraic coefficients over the rationals. A decimal approximation without an error enclosure does not establish the required sign of m.

All four submitted sections and all eighteen final source-check entries were read; the latter were not rerun. The source records a final elapsed check time of1.658162seconds. No numerical search establishes the formula or any global optimization. A nonzero Q grows quadratically and need not solve the full stationary or similarity momentum equation. This certificate supplies neither a decaying counterexample nor the pressure premise missing in the global Euler conjecture.

## 5. Existing model comparison and verification scope

The complete coordinator comparison dated02:43Z was read, including all four items and W1-W4, together with all twenty entries of its existing check log. The generic differentiation, spectral identities and scalar case agree with Sections1-3. Its twelve rotated numerical cases and sampled sign checks are supplementary observations, not proof steps. No code was rerun. The earlier Theory Agent C 02:35Z hand comparison was also read; its numerical log was not inspected.

W1 is already addressed by the basis-free spectral formula in Section1. W2 is resolved by the separately reconstructed elementary cone proof, which reproduces both directions rather than citing this pending source. For W3, in the eigenbasis of B let a_i=1/b_i-7 and let M have diagonal12b_i and off-diagonal2(b_i+b_j). Directly,

    (Ma)_i=8-56b_i+2b_i(49-21)+2(3-7)=0.

Consequently ell_B((x^T A x)^2)=0. Also ell_B(|x|^4)=20tr B=20, so ell_B(F_C)=m. The positive atomic representation therefore excludes nonnegativity if m<0. Equivalently, sum a_i=28 and sum b_i a_i=-4 show that A has both signs; at a nonzero point of its null cone, F_C=(m/20)|x|^4. This establishes the sign claim without sampled directions.

The coordinator is configured as model and the C agent as model. This agent cannot independently attest their actual provider runtime. The exact source and comparison hashes are retained in verification.

## 6. Source confirmation revision

The revised LIT333 source replaces its pending Hilbert-dependent necessity with the independently confirmed elementary necessity A2805. The added matrix-function formula, Ma=0 identity, atomic argument and indefinite null-cone sign test agree with Sections1-5 above. They preserve the exact feasibility statement and the distinction from a full Euler profile. All changed lines were read; no displayed construction is altered.

The exact revised-source hash and the complete delta are retained in the team records and in the team records. No new mathematical computation was run.
