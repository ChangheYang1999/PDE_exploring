# A direct weighted estimate for the full derivative tensor of velocity

Status: new T4 operator theorem, OPEN independent Opus review. This is
an input to a possible derivative hierarchy, not an inverse or closure.

## Exact statement

Let k be a nonnegative integer, R>0 and w(X)=(1+|X|^2/R^2)^(1/2).
For a real smooth compactly supported centrally odd scalar h on R2,
let U[h]=(-R1R2h,R1^2h) be the canonical IPM velocity, with R_j multiplier
i xi_j/|xi|. Let D^k denote the full ordered derivative tensor, with
all 2^k entries; for k=0 it is the scalar itself. Sum squares over all
velocity and tensor components. Then

    ||w D^k U[h]||2 <= sqrt(1+2/(k+1)) ||w D^k h||2.     (1)

The constants do not depend on R. In particular the Hessian estimate is

    ||w D^2 U[h]||2 <= sqrt(5/3) ||w D^2 h||2.           (2)

No sharpness of these constants is asserted. For k=1 the separately
proposed T4-194 constant at p=1 is slightly better. Assertion(1) uses
central oddness, hence applies to S1. It extends by completion of the
stated test class, with the output identified locally in distributions.

For arbitrary compact smooth h, k>=1, the same proof gives the less
sharp constant sqrt(1+2/k). No k=0 full-space growing-weight bound is
asserted.

## 1. Fourier symbol and the exact moment identity

Use the unitary Fourier transform. Write xi=kappa e(theta), kappa>0,
e=(cos theta,sin theta). The real two-component velocity multiplier is

    sigma(theta)=(cos theta sin theta,-cos(theta)^2).

It includes the local identity contribution to R1^2. Direct differentiation
shows

    |sigma|^2=cos^2 theta,
    |sigma'|^2=1,
    sigma.sigma''=-2cos^2 theta.                      (3)

Let A(xi) be any smooth finite tensor for which the expressions below
are integrable. In polar coordinates, expansion and integration by parts
in theta give

    int |grad_xi(sigma A)|^2 dxi
      =int cos^2 theta [|grad_xi A|^2+2|A|^2/kappa^2] dxi. (4)

Indeed the radial derivative contributes |sigma|^2|partial_kappa A|^2.
The angular derivative contributes |sigma|^2|partial_theta A|^2,
|sigma'|^2|A|^2 and
sigma.sigma' partial_theta|A|^2. Integrating the last term around the
circle combines the last two into -sigma.sigma''|A|^2. Equations(3)
prove(4). This argument works componentwise for complex A by taking
real parts in the cross term.

For h in the test class take A=(i xi)^(tensor k) hhat. Plancherel gives

    |||X| D^k U[h]||2^2
      =int cos^2 theta [|grad_xi A|^2+2|A|^2/kappa^2] dxi,
    |||X| D^k h||2^2=int |grad_xi A|^2 dxi.             (5)

At xi=0, hhat=O(kappa) by oddness, so all expressions in(5) are locally
integrable, including k=0. At infinity hhat is Schwartz. The weak
Fourier derivatives in(5) agree with their ordinary derivatives off zero:
the small-circle boundary contribution vanishes because sigma A=O(kappa)
for k=0 and vanishes to higher order for k>=1. Thus Plancherel is justified,
not merely a formal differentiation of a singular multiplier.

## 2. Tensor compatibility provides the constant

Ignore the constant unit phase i^k and write A=a(kappa,theta) S_k(theta),
where a=kappa^k hhat and S_k=e^(tensor k). Its real tensor identities are

    |S_k|^2=1, S_k.S_k'=0, |S_k'|^2=k.                (6)

For the last identity differentiate one factor at a time. The k resulting
tensors have norm1 and are mutually orthogonal, since e.e'=0. Therefore

    |grad_xi A|^2
      =|partial_kappa a|^2+
         (|partial_theta a|^2+k|a|^2)/kappa^2.         (7)

Central oddness gives a(kappa,theta+pi)=-a(kappa,theta). Its angular
Fourier expansion has only odd integers, hence

    int_0^(2pi) |partial_theta a|^2 dtheta
       >= int_0^(2pi)|a|^2 dtheta.                   (8)

This elementary inequality follows directly from Parseval; smoothness
of hhat justifies the expansion on each circle. Combining(7)-(8),

    int |A|^2/kappa^2 dxi
       <=1/(k+1) int |grad_xi A|^2 dxi.             (9)

Use cos^2 theta<=1 in(5) and then(9):

    |||X| D^k U[h]||2^2
       <=(1+2/(k+1)) |||X| D^k h||2^2.             (10)

The unweighted multiplier bound |sigma|<=1 gives
||D^k U[h]||2<=||D^k h||2. Add this squared estimate to R^-2 times(10),
and use 1+2/(k+1)>=1, proving(1).

Without oddness, drop(8) and keep the k|a|^2 term in(7). For k>=1 this
replaces k+1 by k and proves the stated full-space version. Its local
integrability at xi=0 follows from A=O(kappa^k), since k>=1.

## 3. Completion and scope

The input weighted derivative seminorm defines the completion of the
compact odd test class. The inequality makes the velocity derivatives a
bounded map into the corresponding weighted tensor L2 space. To identify
it with the canonical distribution, the input norm must control local
input distributions up to the usual derivative-seminorm polynomial gauge;
for the present compact-test completion this can be handled without an
implicit normalization as follows.

For k=0 there is weighted L2 convergence of h itself, so the existing
canonical extension applies. For k>=1, D^k h converges locally and in
unweighted L2, and the canonical operator U is bounded on unweighted L2
for each tensor component. Thus D^k U[h_n]=U[D^k h_n] converges to that
unique canonical tensor. This defines the output on the derivative
completion, independently of representatives. No pointwise origin jet
is inferred from this seminorm alone.

The estimate keeps the ordered tensor relation and the full signed
velocity symbol. Treating derivative components as unrelated weighted
functions would lose these identities. It does not control the full
linearized transport operator, its lower derivative couplings, the strain,
a fractional commutator, or the nonlinear correction equation. Those are
separate requirements for any proposed hierarchy using(2).

Dependencies: the displayed Fourier multiplier, Plancherel, angular
integration by parts and elementary Fourier orthogonality. No numerical
input or outside operator theorem is used.
