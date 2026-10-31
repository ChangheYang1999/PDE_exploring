# A coefficient derivative of the modal tail gauge

Status: proved finite-dimensional identities under the stated hypotheses. Numerical implementations and their error are separate questions.

## Statement and notation

Let Q be a finite collection of real spherical harmonics Y_q on the unit sphere, orthonormal for surface area measure. The degree and azimuthal order of Y_q are integers l_q >= 1 and 0 <= m_q <= l_q. Include both real cosine and sine members whenever m_q > 0. Use the usual angular derivative for which partial_chi of a cosine member is minus m_q times its sine member, and the derivative of the sine member is m_q times the cosine member. Let c be in (2/5,1/2), omega > 0 and R0 > 0, all fixed. Set alpha=(1-c)/c and kappa=omega/c.

For real coefficients t_q and s_q define tau=sum_q t_q Y_q, sigma=sum_q s_q Y_q and the vector field on the sphere

F = -(Delta_S sigma)n + grad_S((2-alpha)sigma+kappa partial_chi sigma) - n cross grad_S tau.

Here n is the outward unit normal, grad_S is the surface gradient and Delta_S is the surface Laplacian. Then its squared norm is

N = integral_S2 |F|^2 dS = sum_q [wT_q t_q^2 + wS_q s_q^2],

where

wT_q = l_q(l_q+1),
wS_q = l_q^2(l_q+1)^2 + l_q(l_q+1)[(2-alpha)^2 + m_q^2 kappa^2].

Suppose the tail coefficients vary on an affine line,

t_q(x)=t_q+x u_q, s_q(x)=s_q+x v_q.

Define

A=sum_q(wT_q t_q^2+wS_q s_q^2),
B=sum_q(wT_q t_q u_q+wS_q s_q v_q),
C=sum_q(wT_q u_q^2+wS_q v_q^2).

Assume A>0. For every interval about zero on which N(x)>0, the gauge g(x)=100(sqrt(N(x))-1) is smooth and

N(x)=A+2Bx+Cx^2, g'(0)=100 B/sqrt(A).

For h>0 with N(h),N(-h)>0, its exact centered difference is

D2(h)=[g(h)-g(-h)]/(2h)=200 B/[sqrt(N(h))+sqrt(N(-h))].

If N is also positive at +-2h, the four-point difference satisfies

D4(h)=[8(g(h)-g(-h))-(g(2h)-g(-2h))]/(12h)=[4D2(h)-D2(2h)]/3.

These identities avoid subtraction of two nearly equal norm squares or two nearly equal gauge values. They do not turn a finite-precision calculation into a certified enclosure.

## Proof of the modal norm

The radial and tangential parts of F are pointwise orthogonal. Since -Delta_S Y_q=l_q(l_q+1)Y_q, orthonormality gives the radial squared norm sum_q l_q^2(l_q+1)^2 s_q^2. Integration by parts gives integral grad_S Y_q dot grad_S Y_r = l_q(l_q+1) times the Kronecker delta. The rotation derivative preserves each fixed-degree space, is skew-adjoint in its orthonormal real basis, and has squared norm m_q^2 on its cosine/sine pair. Consequently the gradient of (2-alpha)sigma+kappa partial_chi sigma has squared norm sum_q l_q(l_q+1)[(2-alpha)^2+m_q^2 kappa^2]s_q^2. Its mixed term is zero because the integral of a derivative of a periodic squared function is zero, degree by degree.

For any smooth real functions f and h on the sphere, integral grad_S f dot (n cross grad_S h)=0. Indeed the tangent field n cross grad_S h is surface-divergence-free, so integration by parts on the closed sphere makes the integral zero. This also follows from the integral of the exact two-form d(f dh). Thus the gradient part and rotated-gradient part of F have zero integrated cross term. Rotation by n preserves tangent lengths, so the latter has squared norm sum_q l_q(l_q+1)t_q^2. Adding these three orthogonal contributions proves the formula for N.

Expanding the weighted squares on the affine line proves N(x)=A+2Bx+Cx^2. The chain rule gives g'(0)=100 N'(0)/(2sqrt(A))=100 B/sqrt(A). Rationalizing sqrt(N(h))-sqrt(N(-h)), and using N(h)-N(-h)=4Bh, proves D2. Directly collecting the two centered differences proves D4.

## Why a fixed-parameter reduced coefficient column is affine

For the inviscid leading-channel constraints, hold c and omega fixed. Each cosine/sine pair has two free radial coefficient lists and four linear equations for their final two entries. The matrix is invertible throughout the stated domain, as proved in ../tail_coordinates/PROOF.md. The solved entries therefore depend linearly on the free entries. The analogous two-by-two real system applies to m=0. At fixed R0, alpha and l,

t_q=R0^(alpha+l_q) sum_k A_kq,
s_q=R0^(alpha+l_q-1) sum_k C_kq.

Thus every reduced coefficient direction gives the affine line required above. A physical or optimizer parameter column does not satisfy this fixed-parameter premise and requires the additional derivatives of the weights, powers and constraint matrix.

## Implementation and validation scope

The production expression in src/optimization/problem.py is the modal sum above. It is not an evaluation of an angular quadrature. A quadrature of F represents the same mathematical norm only if its normalization and exactness, or a suitable error bound, are separately established.

The theorem describes the real function at the specified inputs. A reference can instead hold already-rounded full coefficients fixed; that is a different stated input convention from solving the reduced constraints in higher precision. Both conventions must be reported when compared. Rounding of parameter maps, powers, linear solves, sums, square roots and the final subtraction can all change a floating-point gauge. Agreement of a centered difference with g'(0) does not itself bound those errors.

The implementation uses max(N,10^-300) before the square root. The identities here apply where this clamp is inactive, namely N>10^-300. A positive A alone does not establish inactivity at all requested stencil points; those values must be checked.

The three residual Jacobians J_f, J_cw and J_c have the same mathematical gauge-row coefficient derivative if they use this same gauge with the fixed weight 100 and the same reduced coordinates. Frozen or differentiated pressure and residual weights in other rows do not affect this statement.

Dependencies: finite spherical-harmonic orthogonality, surface integration by parts, finite-dimensional linear algebra, and the ordinary real chain rule. No formal proof, certified arithmetic error bound, Euler solution, or gate pass is asserted.
