# Quotient coordinates, physical constraints and invariant damping

Status: sections1 and2 independently confirm the analytic claims in N4-175 and N4-178 under the previously confirmed ranks; the concrete reduction is separately checked by code. Section3 is a proposed coordinate-invariant replacement for Euclidean damping, OPEN independent Opus review. No optimization gain is asserted.

## 1. Exact coordinate reduction

Let B:R^n->V be the linear potential map of the exact007 generators, n=2982, with independently confirmed rank r=1922. Select a set P of r original indices. For every j outside P suppose there is an exact polynomial identity

    B e_j+sum_(i in P) a_ji B e_i=0.

Define E:R^r->R^n by insertion into the selected positions, and R:R^n->R^r by

    (R x)_i=x_i-sum_(j outside P) a_ji x_j.

Then RE=I and BER=B. All original columns lie in the selected span, which must have dimension r because rank B=r. Thus BE is bijective onto V, ker R=ker B, and every physical potential has a unique reduced vector. All identities hold over R because their rational coefficients are exact.

The concrete verifier expands every original and selected shape by the exact shifted-Legendre binomial formula, checks all1060 unit-nonpivot identities, verifies the selected shapes and transformed coefficients, and reconstructs the entire canonical polynomial map. It uses the already independently confirmed rank rather than repeating the elimination that chose the pivots. The exact reduced coefficients preserve the original potential. Rounded convenience coefficients carry no such guarantee.

## 2. Physical constraints preserve the entire redundant kernel

Let C:V->R^q be differentiable at the reference potential, with rank DC=q=426. Its rows comprise the420 independent tail conditions, one strain condition and five Taylor residual conditions. Let J:V->Y be any derivative of physical residual or observation rows. Every v in ker B is annihilated by DC B and J B, because B(x+tv)=Bx for all real t.

The restricted map B:ker(DC B)->ker DC is onto: for w in ker DC choose x with Bx=w. Its kernel remains ker B. Therefore

    dim ker(DC B)=(1922-426)+(2982-1922)=1496+1060=2556.

In particular none of the1060 zero potentials is absorbed by the426 physical constraints. If Z is an injective coordinate map onto ker(DC B), then J B Z has a kernel of dimension at least1060. Its square normal matrix has the same kernel; the list of only min(rows,columns) singular values of a rectangular matrix need not display all these zeros. Invertible column rescaling does not change rank. Floating thresholds on rounded normal matrices cannot replace these exact dimensions.

Euclidean damping is not invariant under adding redundant coordinates. At x=0 for the objective (x-1)^2/2, a single coordinate and damping lambda>0 give x_new=1/(1+lambda). Writing x=a+b gives the same physical objective, with both columns of unit norm. Damping the two-coordinate normal matrix by lambda I gives a_new=b_new=1/(2+lambda), hence x_new=2/(2+lambda). The physical steps differ by lambda/((1+lambda)(2+lambda))>0. At lambda=1 they are1/2 and2/3. This confirms the N4-178 counterexample; it does not identify the cause of any failed optimizer step.

## 3. A coordinate-invariant physical damping functional

Let W=ker DC be a finite-dimensional admissible potential tangent. Let K:R^d->W be any onto linear parameterization, possibly redundant. Give W a positive-definite inner product with norm ||.||_G, and give the observation space Y an inner product. For f in Y, J:W->Y linear and lambda>0, minimize

    Q(w)=||f+Jw||_Y^2+lambda ||w||_G^2,  w in W.       (1)

There is a unique physical minimizer w*. Its pullback objective Q(Kz) has precisely the minimizer set {z:Kz=w*}; any two coefficient minimizers differ by ker K. Thus any onto parameterization produces the same physical step. Its normal equation is

    (K*J*J K+lambda K*G K)z=-K*J*f.                  (2)

Here coordinates and adjoints refer to fixed Euclidean bases, and G is the positive-definite matrix of the physical inner product. Both sides annihilate redundant directions. Equation(2) is consistent, and its coefficient solutions are exactly one affine coset of ker K. Solve it on the quotient, or in any exact independent basis, rather than declaring its redundant matrix invertible.

Proof: on W the quadratic form J*J+lambda G is positive definite since its value on nonzero w is ||Jw||_Y^2+lambda||w||_G^2>0. Completing the square gives the unique w*. Surjectivity of K identifies the minima of the pullback; differentiating gives(2). Conversely the vanishing derivative at any z is equivalent to a vanishing derivative in every W direction because K is onto. That is the unique minimizer condition. This proves all assertions and invariance under every change of onto parameterization.

For the campaign an L2 density metric is permissible only on a tangent W whose density is actually in L2. The unrestricted1922-dimensional potential space contains growing density tails and has no finite full L2 Gram. The fixed-tail tangent has dimension1502 before strain and1496 after all426 independent constraints. On it the density L2 form is positive definite by the audited potential-to-density injectivity. A point-sampling form would require a separate injectivity proof before it could be called a positive-definite physical metric. This theorem asserts no quantitative conditioning, convergence, nonlinear feasibility or PDE inverse estimate.

## Dependencies and verification

Inputs: the exact candidate rank and kernel T4-195, density injectivity T4-199/R1-024, and constraint rank T4-209. Source files and maps are frozen with hashes. Polynomial verification is exact over Q. Section3 is finite-dimensional linear algebra and needs no numerical experiment; a concrete large Gram construction is neither claimed nor required. The derivative constraints define a tangent only at the reference; the exact007 Taylor constraints are not all zero, so this text does not assert a zero-constraint manifold through007.
