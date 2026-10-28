# The uncancelled rank-one vector is outside the target

## Claim under audit

Theory author note41, dated2026-10-28 12:40Z, proposes applying the reverse triangle inequality to

 A_0 d=L_fix d+c[d]M_0,
 ||A_0d||Y_H/|c[d]| >= ||M_0||Y_H-||L_fix d||Y_H/|c[d]|,

and estimating the high target norm of M_0 separately. That inequality is not a meaningful inequality of finite target norms in the stated spaces. For every compactly supported smooth bulk direction d with c[d]!=0, both M_0 and L_fix d are outside Y_H and outside either low target of proof 173. Their sum has the required cubic cancellation. This refutes the proposed split diagnostic, not the scalar-radius necessary condition of proof 181.

## Exact spaces, family and statement

Use the exact normalized modal trial rho_0=x^2y+O(r^5), the canonical velocity with U[f]=c[f](-x,y)+O(r^3) near0 for a smooth density f supported away from0, and the exact moving-tail family of topics167 and174. Let

 zeta=partial_ell rho_ell at ell_0,
 n'_0=3-c[zeta]>=3,
 H_0=chi_0 X.grad rho_0/3,
 M_0=H_0+m_0=partial_ell F_ell(rho_ell)|ell_0/n'_0.

Here chi_0=1 near0 and has compact support; zeta vanishes near0, has sublinear growth at infinity and has a canonical finite strain. The finite vector m_0 belongs to Y_H by proof 167. For the high target, write E gamma=x^2y gamma(log r), Gamma_H=a_H H^(25/4)(R), with a_H(t) comparable to exp(9t/5) as t tends to minus infinity. The high remainder has zero vertical cofactor trace. For either low target, the scalar norm is L2(g_w dt) with g_w=exp(-t/2) for t<0, and the remainder weight has angular exponent a_w>5/2. These are exactly the spaces of proof 173.

Then

 M_0=x^2y+O(r^5),
 L_fix d=-c[d]x^2y+O(r^5) near0                           (1)

for every parity-compatible smooth d supported in a compact annulus. If c[d]!=0, neither term belongs to either target. On the actual high realization the correct finite decomposition is

 L_ren d=L_fix d+c[d]H_0,
 A_0d=L_ren d+c[d]m_0.                                   (2)

For such d, both terms in(2) belong to Y_H. Hence the valid reverse triangle inequality is

 ||A_0d||Y_H/|c[d]| >= ||m_0||Y_H-||L_ren d||Y_H/|c[d]|.   (3)

No conclusion about the relative sizes of these finite quantities is made here.

## Proof of the expansions

Since rho_ell agrees with rho_0 near0 and the canonical strain is linear, differentiation of the exact residual at fixed ell gives

 partial_ell F_ell(rho_ell)|ell_0=X.grad rho_0+L_fix zeta.

The separated tail zeta vanishes near0. Thus L_fix zeta=U[zeta].grad rho_0 there. The density parity and the canonical strain expansion yield

 c[zeta](-x,y).grad(x^2y)=-c[zeta]x^2y.

The O(r^3) velocity remainder times the O(r^2) leading gradient, and the linear velocity times the O(r^4) gradient remainder, are O(r^5). Also X.grad rho_0=3x^2y+O(r^5). Therefore the differentiated residual has cubic coefficient3-c[zeta]=n'_0. Dividing by n'_0 gives the first expansion in(1). The same kernel argument applies to compact annular d. Its local derivative and value vanish near0, so L_fix d=U[d].grad rho_0=-c[d]x^2y+O(r^5), proving the second.

The factorization along the vertical axis is legitimate: all functions in this calculation are finite angular polynomials for zeta, or have smooth separated kernels for a smooth compact d. The parity supplies x^2y, and the corresponding vertical cofactor has limit1 for M_0 and -c[d] for L_fix d.

## Why the terms do not belong to the target

The scalar coordinate of a target element is its unique vertical cofactor trace. The trace of M_0 tends to1 at minus infinity. Dividing by a_H therefore has magnitude comparable to exp(-9t/5), which is not L2 there. Thus M_0 is not in E Gamma_H plus the zero-trace high remainder. A nonzero limiting scalar trace also fails the low scalar norm because integral_(-infinity)^0 exp(-t/2)dt diverges. It cannot be hidden in the low remainder: x^2y times a nonzero radial coefficient has angular density |cos theta|^(4-2a_w) near the vertical axis, whose integral diverges when a_w>5/2. The scalar/remainder decomposition is unique.

The same arguments with limiting coefficient-c[d] prove nonmembership of L_fix d when c[d]!=0. In particular, writing infinity minus infinity is not an application of the reverse triangle inequality. A fifth derivative point value of the weighted axis trace of M_0 is finite at a fixed nonzero point but cannot turn the full infinite norm into a finite quantity.

Finally H_0 has the same unit cubic coefficient as M_0. Proof 167 proves m_0=M_0-H_0 belongs to Y_H, with both tails and every spline join included. The closed renormalized coupling theorem and compact support of d put L_ren d in Y_H. This proves(2)-(3).

A concrete nonzero-strain direction exists in this class: take d=x^2y beta(log r), where beta is nonnegative, smooth, nonzero and compactly supported in a finite t interval. The canonical strain formula gives c[d]=(1/4)integral exp(2t)beta(t)dt>0. Such a d is in the full high domain. Hence the invalid split is not merely an empty exceptional case.

## Consequences and scope

Proof 181 already requires the actual combined image A_0d in its necessary condition eta_H|c[d]|<=N_4||A_0d||Y_H. That theorem is unaffected. A candidate diagnostic must evaluate the combined image, or the finite renormalized split(2), with its exact norm. The theory author's expectation that the norm of M_0 is of the order of eta_H is false in these spaces: the former is infinite and the latter is finite by proof 177. This issue concerns target membership, not numerical precision or the size of a pointwise estimate.

Dependencies: topics35 and167 for the canonical kernel and exact moving tail, proof 173 for the unique scalar coordinates and weights, proof 181 for the unchanged necessary test.
