# Negative Sobolev cost and the endpoint sectors of a tail cutoff

This independently audits R2 and R3 of T2 the review of T4-314. The original
cutoff construction is already AUDITED in T4-325. Its second complete
review is frozen in source/. The conclusions below are conditional on
the stated functions and decay bounds, and construct no stationary solution.

## 1. Definitions and negative Sobolev theorem

Use the Fourier convention and unitary normalization of the campaign.
For 0 <= sigma <= 1 define

    ||g||_(dot H^-sigma)^2 = integral |g-hat(xi)|^2 |xi|^(-2sigma) dxi.

Let q < -2, let A be a finite real sum of cos(2m theta), and use the
smooth cutoff zeta=0 on r<=1, zeta=1 on r>=2 from the standalone
proof ../far_out_tail_repair/PROOF.md. Put

    chi_1=-zeta(r) r^(q+3) A(theta), h_1=-partial_y Delta chi_1,
    chi_L(X)=L^(q+3)chi_1(X/L), h_L=L^q h_1(X/L), L>=1.

These definitions apply for every q<-2, including the possible resonant
values where the exterior density could vanish. The canonical velocity
is the one given by the potential proof. Set

    C00=||h_1||2, C10=||r h_1||2, D0=||Delta chi_1||2.

All three constants are finite. Then

    ||h_L||_(dot H^-1)=L^(q+2)||h_1||_(dot H^-1)
                      <=L^(q+2)min(C10,D0),                       (1)
    ||h_L||_(dot H^-sigma)
       <=L^(q+1+sigma)C00^(1-sigma)||h_1||_(dot H^-1)^sigma        (2)

for 0<sigma<=1. Thus these costs tend to zero as L tends to infinity.

Proof. The potential is smooth and vanishes near zero; outside a fixed
disk its Laplacian is O(r^(q+1)) and h_1 is O(r^q). The radial power
integrals for D0 and C10 converge because q+2<0. The Fourier identity
h-hat=-i xi_y (Delta chi)-hat gives ||h_1||_(dot H^-1)<=D0.
S1 symmetry supplies only odd sine modes, all with n>=1. The independently
audited Hardy inequality in ../mode_hardy_mellin/PROOF.md, summed by
angular orthogonality, gives the other bound C10. Its original domain
hypotheses h_1,r h_1 in L2 are satisfied, so no origin distribution
extension is required. Direct substitution in the Fourier transform
gives h_L-hat(xi)=L^(q+2)h_1-hat(L xi). Changing variables yields the
exact factor L^(q+1+sigma) in the norm. Finally apply Holder to
(|h-hat|^2)^(1-sigma)(|h-hat|^2/|xi|^2)^sigma and take square roots.
This proves (1)-(2), with the sigma=1 endpoint interpreted directly.

For a set S in the same affine dot H^-sigma class, the norm triangle
inequality gives dist(R+h_L,S)>=dist(R,S)-||h_L||_(dot H^-sigma).
Consequently an existing exclusion with positive distance margin is
preserved for sufficiently large L. This is a conditional transfer of a
previous certificate; no negative Sobolev distance is computed here.

## 2. Weighted C1 and derivative costs

Let -3<q<-1 and A not identically zero in the preceding construction.
Write h_1=r^q B(theta) for r>=2. The homogeneous density map is triangular
and injective in this range, as checked in the second review: the highest
sine mode has nonzero coefficient, since 0<q+3<2. Thus B is nonzero.
Define

    H_q(g)=max(sup (1+r)^(-q)|g|, sup (1+r)^(1-q)|grad g|),
    J_q(g)=max(sup r^(-q)|g|, sup r^(1-q)|grad g|),

where the homogeneous suprema omit the origin; the functions vanish
there. Both norms are finite for h_L, and

    J_q(h_L)=J_q(h_1),
    ||B||infinity <= H_q(h_L) <= 2^(1-q) J_q(h_1).                 (3)

Proof. Substitute X=LY in each expression. On the support |Y|>=1,
|Y|<=L^-1+|Y|<=2|Y|, which bounds the two inhomogeneous weights.
The exterior density gives the lower bound by taking r to infinity.
The differentiated homogeneous expression proves finiteness. Hence
moving the cutoff outward does not make this weighted C1 cost vanish.

For an integer k>=0 and real beta, the homogeneous or inhomogeneous
weighted L2 norm of D^k h_L is finite if and only if

    q+1+beta-k<0.                                                (4)

When finite, the homogeneous norm is exactly L^(q+1+beta-k) times its
value at L=1, and the inhomogeneous norm tends to zero as well. For the
converse, D^k(r^q B) cannot vanish identically: a function with identically
zero full kth derivative on the connected exterior would be a polynomial
of degree below k there, whereas a nonzero function homogeneous of
negative degree is not such a polynomial. Its nonzero continuous angular
part has positive squared circle integral. The radial integral therefore
diverges when (4) fails, logarithmically at equality. The inhomogeneous
weight is comparable to the homogeneous one at infinity. This proves
both directions. This criterion concerns the density; no nonvanishing
assumption about an unrelated velocity component is needed.

## 3. Agreement of the residual sectors through the endpoint

Set c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
q=4gamma-5 and qstar=gamma-4. Let R be any one of the audited references
007,013,014, with the canonical velocity and convergent differentiated
exterior expansion. Let eta be the audited global potential repair of
T4-295, and let h_L be the cutoff with the same A1_m coefficients.
Assume, as holds for those exact references, |U[R]|=O(r^gamma) and
|grad R|=O(r^(gamma-1)). Then for fixed L the residuals F(R+h_L) and
F(R+eta), with F(Q)=c X.grad Q-Q+U[Q].grad Q, have identical coefficients
at every exponent at or above qstar.

Proof. The global repair's potential is

    -sum_m A1_m r^(q+3)(1+r^-2)^(2gamma-m-5)cos(2m theta).

For r>max(2L,1) the difference between this potential and chi_L starts
at degree q+1 and has a convergent series in r^-2. Three differentiations
give eta-h_L=O(r^(q-2)), U[eta]-U[h_L]=O(r^(q-2)), with each further
derivative decreasing the power by one. Expanding the residual difference,
its linear part is O(r^(q-2)), the two background mixed parts are
O(r^(q+gamma-3)), and the correction-quadratic difference is
O(r^(2q-3)). Each exponent is strictly less than qstar for the exact
campaign gamma. Distinct powers in a convergent finite-branch expansion
have unique coefficients, so the claimed equality follows. The endpoint
itself is included; the word 'above' in some review sentences must be
read as 'at or above' for the list containing (1,2).

In particular the first remaining residual sector is (9,0), with the
same coefficient as for R+eta; the other nonzero sectors at or above
qstar are (5,1) and (1,2). If an additional correction k makes R+h_L+k
stationary and H_(1-9delta)(k)<infinity, the separately audited dipole
forced-tail theorem applies to this new reference. It yields

    k=r^(1-9delta) F_(9,0)/(1-c(1-9delta))+o(r^(1-9delta)).         (5)

This conclusion requires the newly named k and its weighted C1 bound.
It is not a statement about the total correction h_L+k having that
faster decay. The convergent reference expansion supplies the finite
growth constants required by that theorem, without certifying their
numerical sizes. The exact profile norm in (5) was already certified
in T4-317; it is not recomputed here.

## 4. Evidence and limits

The checker records exact inequalities in the campaign exponents and
checks the source hashes and review's data. The analytic proofs above
precede its execution. The peer's numerical constants C00 about215936.94,
C10 about346927.02 and its proposed numerical cutoff radii are FLOAT.
They are neither interval certificates nor necessary cutoff sizes for
all possible constructions. This audit accepts the analytic negative
Sobolev and weighted C1 conclusions, and the exact sector agreement.
It makes no claim of a new candidate, stationary solution or inverse.
