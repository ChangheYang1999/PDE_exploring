# Symmetric conjugation is a Hilbert-Schmidt remainder on a regular patch

## Statement

Let M be a bounded self-adjoint convolution singular integral on L2(R2), represented by the strong L2 limit of its radially truncated kernel operators plus a constant multiple of the identity. Assume its off-diagonal kernel is a real even function K(X-Y) satisfying

 |K(Z)|<=C_K |Z|^(-2), Z!=0.

A constant multiple of the identity may be included in M. Let b be real, bounded and globally Lipschitz, supported on a measurable compact set E of area A. Write ||b||_infinity<=B and Lip(b)<=L_b. Let f=exp(q), where q is a bounded real Lipschitz function, and set Q=sup q-inf q and Lip(q)<=L_q. Multiplication by f and f^(-1) is then bounded. Define

 D=sym(M_f M_b M M_(f^-1))-sym(M_b M),
 sym(T)=(T+T*)/2.

Then D is the Hilbert-Schmidt integral operator with kernel

 H(X,Y)=K(X-Y)/2 [b(X)(exp(q(X)-q(Y))-1)
                         +b(Y)(exp(q(Y)-q(X))-1)].        (1)

In particular, with

 C0=(C_K exp(Q)/2)(L_b L_q+B L_q^2),
 Cfar=C_K B(exp(Q)-1),

one has for every R>0

 ||D||_HS^2 <=2 pi A(C0^2 R^2+Cfar^2/R^2).                (2)

The same formula applies componentwise to the actual regular-patch coupling b_j U_j. Both IPM velocity components are self-adjoint with the convention of proof 01, and C_K=1/(2pi) is a valid scalar kernel bound. The point-mass part of U2 cancels from D. Sum the two resulting Hilbert-Schmidt bounds for the vector coupling.

This is a regular-patch theorem. It requires a bounded positive Lipschitz extension f of the conjugating factor. It does not permit the singular global angular weight itself in place of f, and it does not include axis jets or nonlocal interactions outside the patch.

## Proof of the kernel and cancellation

First truncate the singular kernel away from the diagonal and apply the multiplication operators. Taking the adjoint reverses f and f^(-1) and changes b(X) to b(Y), since M is self-adjoint. Subtract the similarly symmetrized unweighted coupling. This gives (1). The diagonal multiplication part cancels exactly because all multipliers commute.

Put d=q(X)-q(Y). The bracket in (1) is exactly

 (b(X)-b(Y)) sinh(d)+(b(X)+b(Y))(cosh(d)-1).               (3)

Since |d|<=Q and |d|<=L_q|X-Y|,

 |sinh d|<=exp(Q)|d|,
 |cosh d-1|<=exp(Q)d^2/2.

Together with |b(X)-b(Y)|<=L_b|X-Y| and |b(X)+b(Y)|<=2B, these prove |H(X,Y)|<=C0. Alternatively, bound each exponential difference by exp(Q)-1 to get |H(X,Y)|<=Cfar |X-Y|^(-2). The kernel vanishes unless X or Y lies in E. Therefore, splitting at |X-Y|=R and counting this union by its two parts,

 integral |H|^2 <=2 A[pi R^2 C0^2
             +Cfar^2 integral_(|Z|>=R)|Z|^(-4)dZ],

and the last integral is pi/R^2. This proves (2). Near-diagonal truncation errors converge to zero in Hilbert-Schmidt norm, so the limiting kernel equals the bounded-operator difference D. One may justify the truncated singular-integral identity on smooth compact functions, then pass by the assumed strong convergence of the truncated operators and the Hilbert-Schmidt convergence. The actual IPM Riesz products have this standard principal-value representation; merely specifying an arbitrary bounded operator off the diagonal would not, without a further argument, justify that passage. No first-order singular remainder survives in the real energy.

If C0 and Cfar are both positive, optimize at R^2=Cfar/C0 to obtain

 ||D||_HS^2 <=4 pi A C0 Cfar.                             (4)

If L_q=0 or B=0, the operator is zero and that case is immediate.

## Explicit finite-rank error route

Let 0<epsilon<R. The omitted near-diagonal part has Hilbert-Schmidt norm at most sqrt(2 pi A) C0 epsilon. The part with |X-Y|>R has norm at most sqrt(2 pi A) Cfar/R. Between these cutoffs, the kernel lies on a bounded set because at least one point lies in E and the other is within distance R. A smooth cutoff may be used at the two radii; its actual derivative bounds belong in the next step.

If b,q and K have the required first derivatives there, the cutoff kernel is H1 on a bounded product rectangle. Its projection onto tensor products of cellwise constants has error bounded by the explicit Poincare formula in proof 92. This gives a finite-rank approximation with an error expressed only through C0,Cfar, the chosen radii, cell widths and actual derivative integrals. The derivative integral of the uncut kernel is not assumed finite at the diagonal. The near-diagonal deletion avoids that endpoint issue.

The theorem proves a constructive Hilbert-Schmidt remainder for symmetric conjugation. It neither evaluates the actual constants nor proves that the resulting rank is affordable. Combined with proof 94 it identifies two distinct second-order cancellations available to the real-energy certificate.

## Independent checks

The accompanying symbolic script verifies the exponential and symmetric-operator kernel identities. The proof uses exact algebra and elementary two-dimensional radial integrals; there is no numerical quadrature or external compactness theorem. Dependencies: proof 01 for the actual IPM kernel convention, proof 92 for the finite-rank projection estimate.
