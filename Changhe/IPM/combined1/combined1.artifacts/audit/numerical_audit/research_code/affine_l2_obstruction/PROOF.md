# An annular necessary condition for an L2 correction

## Statement and status

Let rho be a smooth reference on R2, let u=U[rho] be its smooth divergence-free velocity, and fix a real c. Assume that, for some gamma<1 and all sufficiently large r=|X|,

|u(X)|<=C r^gamma, |grad rho(X)|<=C r^(gamma-1).

Set F_c=(cX+u).grad rho-rho. Suppose its leading exterior residual is

F_c(r,theta)=r^q E(theta)+o(r^q),

uniformly in theta, with a nonzero smooth real E and q>=-1. Then there is no h in L2(R2) with bounded weak gradient such that U[h] is the L2 Fourier-multiplier velocity and rho+h solves the stationary equation at c in distributions. In particular, there is no such h in H^(2+s) for any s>0, regardless of its finite norm.

This is the L2 analogue of the Hdot^-1 affine-class obstruction in Analysis II, section6. It does not assume an Hdot^-1 component. The exponent threshold is -1 here, whereas the earlier Hdot^-1 theorem reaches -2. The proof below is complete but is N4-ORIGIN pending an independent theory-lane review.

## Weak identity

The vector multiplier U has modulus at most one, so U[h] belongs to L2 and ||U[h]||2<=||h||2. Products in

0=F_c+(cX+u).grad h-h+U[h].grad rho+U[h].grad h

are locally integrable under the stated hypotheses. For a real smooth compactly supported test phi, integration by parts gives

<F_c,phi>=<h,(cX+u).grad phi+(2c+1)phi>
           -<U[h],phi grad rho>-<U[h].grad h,phi>.          (1)

Only div u=0 and div(cX)=2c are used here. The terms on the right can be restricted to the support of phi. This restriction, rather than a global L2 bound alone, handles the endpoint q=-1.

## Annular dilation and vanishing of the right side

Choose a smooth nonnegative radial eta supported in 1<r<2, not identically zero, and put psi(r,theta)=eta(r)E(theta). It is smooth and compactly supported away from the origin. Define

phi_R(X)=R^(-1)psi(X/R), A_R={X:R<|X|<2R}.

The norms ||phi_R||2 and ||cX.grad phi_R+(2c+1)phi_R||2 are independent of R. Also ||grad phi_R||2=R^(-1)||grad psi||2. Consequently

||u.grad phi_R||2<=C1 R^(gamma-1),
||phi_R grad rho||2<=C2 R^(gamma-1).

Write d=||grad h||infinity. Cauchy-Schwarz applied to (1), retaining the supports, yields

|<F_c,phi_R>| <= ||h||L2(A_R) [C0+C1 R^(gamma-1)]
                 +||U[h]||L2(A_R) [C2 R^(gamma-1)+d||psi||2].          (2)

Both annular L2 norms tend to zero as R tends to infinity, because h and U[h] belong to L2. The bracketed factors remain bounded since gamma<1. Thus the left side of (2) must tend to zero.

## The nonzero leading moment

Changing variables X=RY and using the uniform asymptotic expansion gives

<F_c,phi_R>=R^(q+1) [A+o(1)],
A=integral_(1<|Y|<2) |Y|^q E(arg Y) psi(Y) dY
 =(integral_1^2 r^(q+1)eta(r)dr)(integral_0^(2pi)E(theta)^2 dtheta)>0.

If q>-1 the pairing tends to positive infinity. If q=-1 it tends to the positive number A. Both conclusions contradict (2), proving the theorem.

## Exponent rigidity without a negative norm

Assume additionally that the reference has differentiated leading expansion

rho(r,theta)=r^gamma Theta(theta)+o(r^gamma),
X.grad rho=gamma r^gamma Theta(theta)+o(r^gamma),

with -1<gamma<1, gamma nonzero, and Theta nonzero. Suppose that at its reference exponent c0 the residual satisfies F_c0=o(r^gamma). At any c different from c0,

F_c=F_c0+(c-c0)X.grad rho
   =(c-c0)gamma r^gamma Theta+o(r^gamma).

The theorem applies with q=gamma>-1. Therefore any stationary solution in rho+L2 with bounded correction gradient must retain c=c0. No norm smallness is needed. This also explains why changing c cannot repair a forbidden leading sector while remaining in the same unweighted L2 affine class.

## Applications and limitations

The finite canonical potentials in this campaign satisfy the smoothness, divergence, differentiated asymptotic and sublinear-growth assumptions. Their reference exponent has gamma=1/c0 in (0,1), and their residual begins below order r^gamma. Hence exponent rigidity applies to every independently verified canonical candidate.

For state131, N4-002 independently confirms a nonzero leading residual sector q=2gamma-1=0.1047775... with full-circle angular norm0.18207889107112578.... The theorem excludes every finite H^(2+s) correction to this unrepaired reference at c0, and the rigidity corollary excludes every other c as well. This is an affine-class statement. It does not exclude a stationary profile obtained by a non-L2 tail repair.

For d2 and the repaired candidates with leading residual exponent below-1, this theorem gives no fixed-exponent nonexistence result. Their finite weak-probe bounds in ../weak_probe are separate quantitative tests and may exclude specified small balls only. Weighted spaces and spaces with explicit exterior coefficients are not covered.

Dependencies are the Fourier multiplier contraction on L2, the weak identity, elementary dilation and L2-tail convergence, the already verified canonical expansions, and the exact state131 sector record. No quadrature or formal build is involved.
