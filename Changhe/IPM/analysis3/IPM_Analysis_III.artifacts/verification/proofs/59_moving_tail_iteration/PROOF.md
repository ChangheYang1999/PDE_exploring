# A moving-tail iteration with a fixed forcing

## Setting and claims

Let rho0 be the exact normalized modal profile, ell0=1/k, and p=x^2 y.
Use X0=E B direct-sum R, Y=E G direct-sum R and the Hilbert space H=H_high
of proof 57. Their norms, cutoffs and parameters are fixed. In particular
H embeds continuously into X0, J is a classical continuous cubic
coefficient on H, c is bounded on X0, and the low/high product bound of
proof 57 holds. The positive-axis hypothesis used to define B is assumed.
No positive global energy margin or inverse is assumed in the mapping
claims below.

Fix a smooth radial chi_infinity with 0<=chi_infinity<=1 that vanishes
for r<=1 and equals1 for all sufficiently large r. The fixed leading angular factor is Theta.
For ell>1 put

    q=1/ell,
    rho_ell=rho0+chi_infinity(r)(r^q-r^k)Theta(theta),
    F_ell(rho)=(ell X+U[rho]).grad rho-rho,
    n(ell)=3ell-1-c[rho_ell].

Fix a compact interval I in (1,infinity), with ell0 in its interior and
max(k,1/ell)<5/16 for all ell in I. Let

    H0=chi0(r) X.grad rho0/3,
    B(ell)=F_ell(rho_ell)-n(ell)H0,
    f0=B(ell0)=F_ell0(rho0),

where chi0 is smooth, compactly supported, and equal1 near0. Proof 39 proves
B is a smooth Y-valued family. The scalar result of proof 35 gives
n(ell0)=0 and n'(ell)>=3. The symbol B here denotes this residual family,
not the scalar axis space in E B.

Define the smooth Y-valued family m by the removable quotient

    m(ell)=(B(ell)-B(ell0))/n(ell), ell!=ell0,
    m(ell0)=B'(ell0)/n'(ell0),
    M(ell)=H0+m(ell).                                      (1)

M itself is in span{H0} direct-sum Y, not in Y. Its cubic coefficient is1.
For h in a sufficiently small H ball let ell(h) be the unique solution of

    n(ell(h))=c[h].                                        (2)

It lies in I provided ||c||_(X0*)||h||_X0 is less than
3 dist(ell0, boundary I). Define, for g in H,

    A_h g=(ell(h) X+U[rho_ell(h)]+U[h]).grad g-g
                         +U[g].grad rho_ell(h)+c[g]M(ell(h)). (3)

Then the following statements hold.

1. A_h is a bounded linear map H->Y. It depends smoothly on h in the H
   topology. On every H ball whose scalar values remain in I there is a
   finite constant C such that

       ||(A_h1-A_h0)g||_Y
            <= C ||h1-h0||_X0 ||g||_H.                    (4)

   The constant can be chosen uniformly on the entire scalar interval I;
   it uses the fixed low/high product constant and fixed family bounds.

2. The exact identity

       F_ell(h)(rho_ell(h)+h)=f0+A_h h                     (5)

   holds in Y. Thus (3) gives a fixed-forcing quasilinear formulation of
   the moving-tail problem. All origin jets and exponent variations are
   included. No finite truncation of the powers of log r is used.

3. The general free-J augmented map

       (ell,h) -> (F_ell(rho_ell+h)
                    -(1+J(h))(n(ell)-c[h])H0,
                    n(ell)-c[h])                         (6)

   is smooth from I times H into Y times R. This closes the general
   high-correction membership question for this specified H.

4. The conditional two-norm iteration stated below applies to (3), with
   low space X0 and high space H. Its uniform inverse hypotheses, a
   suitable high forcing norm and numerical smallness inequalities are
   not proved here. Therefore this result is not an existence proof.

## Smooth scalar and residual quotients

Write d=ell-ell0. The quotient in (1) can be defined for every ell in I by

    m(ell)= [integral_0^1 B'(ell0+t d)dt]
             /[integral_0^1 n'(ell0+t d)dt].               (7)

The denominator is at least3. Differentiation under the integral proves
smoothness in Y and uniform bounds for every fixed derivative order on I.
Equation (1) and B(ell0)=f0 now give the exact function identity

    F_ell(rho_ell)=f0+n(ell)M(ell).                        (8)

All derivatives of the tail family are legitimate. Indeed, choose
q_star strictly between max_{ell in I}(k,1/ell) and5/16. Any fixed number
of ell derivatives introduces finitely many logarithmic powers, bounded
by a constant times r^(q_star-max(q,k)) at infinity. Near0 every tail
variation is zero. Canonical Green kernels and their differentiated
moments converge because q_star<1. The finite angular expansion has no
resonance in this parameter interval. These estimates also justify the
smooth Y-valued B family from proof 39 without an informal exchange of
limits at infinity.

Since n'>=3, its inverse on I is Lipschitz with constant1/3. In particular

    |ell(h1)-ell(h0)|<=||c||_(X0*)||h1-h0||_X0/3.           (9)

The smooth scalar inverse theorem makes ell(h) smooth in both X0 and H
on its open domain. No solution of the PDE is used in this step.

## Two auxiliary operator families

Put z_ell=rho_ell-rho0. We need the following uniformly smooth families:

    g -> W[z_ell].grad g          from H to Y,
    g -> U[g].grad z_ell          from X0 to Y.             (10)

Both vanish at ell0, and their operator differences are bounded by a
constant times |ell1-ell0| in the displayed norms.

For the second family use the global coupling proof of topics46-48 with
background z_ell. It has zero density on a fixed neighborhood of0,
finite smooth angular factors on annuli, and far exponent at most q_star.
The leading cubic coefficient is zero. The proofs are linear in the
background and therefore apply to its ell derivatives. The cutoff
normalized coupling maps X0 to Y by those estimates. Removing its cutoff
strain changes it by the fixed rank-one function
-(c[g]/3)chi0 X.grad z_ell, which is supported away from0 on a compact
annulus and belongs to Y after its exact axis subtraction. This proves
both the boundedness and the smooth operator-norm dependence of the
second family. It does not assert that the uncut strain of a growing
background is in Y.

For the first family write W[z_ell]=U[z_ell]+c[z_ell]X/3.
The density z_ell vanishes near0, so its canonical velocity there is
analytic with expansion

    W[z_ell]=c[z_ell](-2x/3,4y/3)+O(r^3).                 (11)

The linear vector field in (11) annihilates p exactly. All its fixed
annular angular derivatives and the divided components are uniformly
bounded after division by r; at infinity the added linear strain
controls the O(r) bound since U[z_ell]=O(r^q_star). The same statements
hold for ell derivatives, with constants uniform on I.

Acting on the factored component g=p[j chi+a u] of H, equation (11)
leaves O(r^(3+delta))+O(r^5) near0. At infinity it is O(r^gamma).
Subtract the exact vertical-axis cofactor. Evenness gives a further
cos^2 factor in the remainder. The squared radial logarithmic powers
are 2delta-1/2>0 at0 and 2gamma+3/4<0 at infinity. These are precisely the
integrals checked in proof 57. On the compact H^s component of H, the
vector field and weight are bounded and the product is an L2 function
supported away from the vertical axis. Thus it lies directly in R.
This proves the first family of (10), including its operator-norm
smoothness. The proof applies to each ell derivative, so the mean value
formula gives the difference bound.

We will also use the smooth family

    T_ell g=(ell X+U[rho_ell]).grad g-g-J(g)n(ell)H0

from H to Y. Its near-origin leading coefficient before subtraction is
J(g)n(ell), because rho_ell=p+O(r^5); after subtraction the same
O(r^(3+delta))+O(r^5) estimate applies. At infinity its size is
O(r^gamma). The axis subtraction and compact H^s component are handled
as above. Consequently this is indeed a bounded smooth family, rather
than an application of a transport operator to an unspecified domain.

## Boundedness of A_h and its low/high difference

At h=0, ell=ell0 and

    A_0 g=(V0.grad-1)g+U[g].grad rho0+c[g]H0+c[g]m(ell0).

The first term is in Y by H->Z. The next two terms are the bounded
cutoff-renormalized coupling, with the harmless compact correction if
H0 uses a different cutoff convention. The final term is bounded rank
one into Y. Hence A_0:H->Y is bounded.

For two corrections h1,h0 put d=h1-h0, ell_i=ell(hi), and
z=rho_ell1-rho_ell0. From (2) we have the exact relation

    c[d]+c[z]=3(ell1-ell0).                               (12)

Subtracting (3) at the two corrections and using (12) gives

    (A_h1-A_h0)g
       = W[d].grad g+W[z].grad g
                          +U[g].grad z+c[g](m(ell1)-m(ell0)). (13)

Each term is in Y. The first is controlled by the low/high theorem of
proof 57. The two middle terms use (10), and the last uses (7) and
continuity of c. Apply (9) and H->X0 to obtain (4). Taking h0=0 proves
boundedness of every A_h. Smoothness in the high topology follows from
the bilinear product, the smooth operator families and scalar inverse.

The identity (12) is essential. Estimating the independent linear drift
and central strain separately would leave a forbidden cubic term in Y.
Similarly, U[g].grad rho_ell and c[g]H0 are not individually Y-valued at0;
they must stay grouped in the renormalized coupling.

Expanding F_ell(rho_ell+h) algebraically gives

    F_ell(rho_ell)+(ell X+U[rho_ell]+U[h]).grad h-h
                                                    +U[h].grad rho_ell.

Insert (8) and n(ell(h))=c[h]. The result is exactly (5). In particular
it is Y-valued by the already proved map A_h:H->Y.

## General free-J augmented membership

For independent ell,h, expand the first component of (6) as

    B(ell)
      + [(ell X+U[rho_ell]).grad h-h-J(h)n(ell)H0]
      + [U[h].grad rho_ell+c[h]H0]
      + [U[h].grad h+J(h)c[h]H0].                          (14)

The first term is smooth Y-valued. The second is the T_ell family proved
above. The third is the normalized coupling, treated exactly as for
A_0 plus the second family in (10). For the last bracket write

    W[h].grad h+c[h](J(h)H0-X.grad h/3).

The low/high bound treats its first part. The second factor has its
cubic term removed, has the extra cos^2 in its axis-subtracted remainder,
and decays like r^gamma at infinity. The same integrals as in proof 57
therefore put it in Y with norm bounded linearly by ||h||_H. Hence the
last bracket is bounded quadratic into Y. This proves (6), including
smoothness and the exact necessity of its (1+J) factor.

At the base point define beta=n'(ell0) and

    eta= d/dell F_ell(rho_ell)|ell0
        = X.grad rho0+L_fix(rho_dot),
    rho_dot=-k^2 chi_infinity r^k log(r)Theta.

Then beta=3-c[rho_dot]=3+k^2 c[KP]>=3 and
M(ell0)=eta/beta. The derivative of the eliminated map is

    D_h F_ell(h)(rho_ell(h)+h)|0
       = L_fix h+(c[h]/beta) eta
       = L_ren h+c[h]m(ell0),                             (15)

where L_ren=L_fix+c[.]H0. The right side is Y-valued. Equation (15)
recovers the exact Schur complement of the verified bordered system;
it does not imply that this operator is invertible.

## Conditional iteration theorem

Let Y_H be a Banach space continuously embedded in Y and containing f0.
Write eta0=||f0||_YH. Choose r>0 so that the closed H ball of radius r has
all scalar parameters in I. Suppose for every v in this ball there is a
linear solution operator R_v on Y_H, taking values in H, with

    A_v R_v f=f,
    ||R_v f||_H<=K_H ||f||_YH,
    ||g||_X0<=K_L ||A_v g||_Y for every g in H.             (16)

Only the first equation on the specified forcing class is required;
no unexplained common maximal low domain is being assumed. A stronger
compatible inverse on Y with a bound into X0 would suffice for (16).
Assume

    K_H eta0<=r,  q0=K_L C K_H eta0<1.                    (17)

Then h0=0, h_(j+1)=-R_hj f0 is well defined, stays in the H ball of radius
K_H eta0, and converges in X0 to h in that ball, with f0+A_h h=0.
It is unique in the closed r ball if K_L C r<1.

Proof. Subtract consecutive equations to get, for j>=1,

    A_hj(h_(j+1)-h_j)=(A_h(j-1)-A_hj)h_j.

Apply (16), (4) and ||h_j||_H<=K_H eta0. The successive X0 differences
contract by q0, proving strong convergence in X0. Reflexivity of H gives
a weakly convergent subsequence in H; its image in X0 must be the same
limit, so the limit belongs to H with the stated norm. Equation (4)
shows A_hj-A_h tends to zero in operator norm H->Y. Therefore
A_h h_(j+1) tends strongly to -f0 in Y. Bounded linearity of A_h also
gives weak convergence to A_h h along a weakly convergent subsequence
of h_(j+1), whose X0 limit is the same h. This proves the equation. For two solutions h,g in the r ball,

    A_h(h-g)=(A_g-A_h)g.

The last inequality of (16) and (4) yield
||h-g||_X0<=K_L C r ||h-g||_X0, proving uniqueness under the stated strict
bound. This proves the conditional theorem.

There is no requirement that H be invariant under a single fixed-domain
transport operator on X0. The needed compatibility is precisely (16),
on H for the estimates and on the fixed forcing class for the solutions.
The actual IPM family has not been shown to satisfy (16).

## Restoring the unit cubic coefficient

If the conditional construction succeeds and |J(h)|<1, then
rho=rho_ell(h)+h has positive cubic coefficient a0=1+J(h). Set

    lambda=sqrt(a0), rho_norm(X)=lambda rho(X/lambda).

Homogeneity of the canonical velocity gives
U[rho_norm](X)=lambda U[rho](X/lambda), and hence
F_ell(rho_norm)(X)=lambda F_ell(rho)(X/lambda)=0.
The cubic coefficient becomes a0/lambda^2=1, while c and ell are
unchanged. The leading tail amplitude changes by lambda^(1-q), as it
must under this scaling. Thus this final normalization does not assert
that the corrected profile remains in an affine space with the old
fixed tail amplitude. A sufficient checked smallness condition would be
||J||_(H*) K_H eta0<1.

## Status and dependencies

Mapping, smoothness, exact moving-tail algebra, the low/high difference
bound and the abstract implication (16)-(17) are proved here. Their
constants are finite qualitative constants. This result supplies no
actual uniform inverse, no certified residual norm in Y_H, and no
numerical smallness test. Those are the remaining requirements for the
existence construction, together with the baseline positive-axis
hypothesis used by B.

Dependencies: exact scalar normalization and its monotonicity (proof 35),
parameter residual membership (proof 39), the bounded renormalized
coupling (topics46-48), the actual modal endpoint bounds (topics50,52),
and the refined high-space theorem (proof 57). The argument explicitly
checks the domain and image of every new operator used here.
