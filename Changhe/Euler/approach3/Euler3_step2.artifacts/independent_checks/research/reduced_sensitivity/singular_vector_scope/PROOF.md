# Parameter content of a finite set of singular vectors

Status: proved finite-dimensional bounds and counterexamples. The application to the campaign's stored floating-point factors is conditional. No new factorization or numerical vector check is performed here.

## Statement, hypotheses and notation

Fix integers n,q,m >= 1 with m <= n+q. Decompose Euclidean R^(n+q) into n coefficient coordinates and q parameter coordinates. Let P:R^(n+q) -> R^q be the projection onto the last q coordinates. Let V be a real (n+q)-by-m matrix with columns v_j. Assume

||V^T V-I_m||_2 <= delta < 1,

and ||P v_j||_2^2 <= epsilon_j for j=1,...,m, with epsilon_j >= 0. Then every w in range(V) satisfies

||P w||_2^2 <= [sum_j epsilon_j/(1-delta)] ||w||_2^2.       (1)

Thus, if m=20, delta=0 and every epsilon_j <= 8e-13, the squared parameter content of any unit vector in this particular span is at most 1.6e-11. These constants are a conditional arithmetic illustration, not verified campaign measurements.

If, in addition, a real matrix A has exact orthonormal right singular vectors v_j with singular values at most tau, then every w in their span satisfies ||A w||_2 <= tau ||w||_2. Neither assertion bounds vectors outside the chosen span. In particular, a bound on the 20 smallest right singular vectors does not characterize all directions below a larger singular-value threshold.

## Proof

Write w=V a. The Gram-matrix bound gives

||w||_2^2 = a^T V^T V a >= (1-delta)||a||_2^2.

For each row of P V, Cauchy-Schwarz bounds its product with a by the row's Euclidean norm times ||a||_2. Summing these squared bounds yields

||P V a||_2^2 <= ||P V||_F^2 ||a||_2^2
              = [sum_j ||P v_j||_2^2] ||a||_2^2.

Combining the two inequalities proves (1). For exact right singular vectors, A^T A v_j=sigma_j^2 v_j. Therefore

||A V a||_2^2 = a^T V^T A^T A V a
                = sum_j sigma_j^2 a_j^2
                <= tau^2 ||a||_2^2,

while ||V a||_2^2=||a||_2^2. This proof applies to rectangular A and includes zero singular values without requiring a left singular vector for every selected zero direction.

## Why the conclusion concerns only the chosen span

Take n=20, q=2 and 0<t<1/2. In the coefficient/parameter coordinate order let

A=diag(t,...,t,2t,1),

with 20 copies of t. Its 20 smallest singular vectors span exactly the coefficient coordinates and have zero parameter content. Nevertheless the first parameter coordinate is a unit vector with residual norm 2t. At any threshold greater than or equal to 2t this is another small-singular-value direction, entirely in the parameter coordinates. Thus examining 20 vectors cannot exclude other weak parameter directions without locating the remainder of the spectrum relative to the declared threshold.

An exact positive smallest singular value of a known matrix would exclude an exact kernel. A tiny positive output of a floating-point SVD is not such a certificate without a suitable matrix and factorization error bound. This distinction is separate from the finite-span bound (1).

## Coordinate scaling matters

The campaign uses a column-scaled Jacobian A=J D^(-1), where D is positive diagonal. A vector w in the scaled coordinates represents the physical displacement D^(-1)w. Its parameter fraction need not equal that of w. For example, in one coefficient and one parameter coordinate take 0<e<1, w=(sqrt(1-e),sqrt(e)) and D^(-1)=diag(1,1/sqrt(e)). The scaled unit vector has parameter squared norm e. The physical displacement is (sqrt(1-e),1), whose parameter fraction of its squared norm is 1/(2-e). This tends to 1/2 as e tends to zero. Extra coordinates can be zero, so the example also applies to the two-parameter setting.

Consequently a report must identify the scaled coordinates when describing the measured parameter content. It must not identify small scaled parameter content with the same numerical fraction in physical c_l and omega coordinates.

## Dependencies and scope

Dependencies are Euclidean Cauchy-Schwarz, the spectral bound for a symmetric Gram matrix, and the definition of an exact singular-vector decomposition. Read this after ../PROOF.md and ../spectral_gap/PROOF.md. No nonlinear stationarity, uniqueness, parameter identification, exact rank of a floating-point factor, or Euler solution follows. The formal subfolder records the absence of a formal build; the verification subfolder states the numerical application status.
