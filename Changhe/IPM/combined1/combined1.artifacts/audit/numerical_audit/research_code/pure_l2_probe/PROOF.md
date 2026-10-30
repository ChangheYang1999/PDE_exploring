# A necessary L2 correction size without a gradient cap

## Exact statement

Work on R2 with Lebesgue measure and the campaign Fourier normalization. Let
U[h]=(-R1 R2 h,R1^2 h), where Rj has symbol i xi_j/|xi|. Fix a real c and a smooth real background rho. Put V=cX+U[rho] and F=V.grad rho-rho. Assume div U[rho]=0, U[rho]=O(r^gamma), grad rho=O(r^(gamma-1)) as r tends to infinity, for some gamma<1, and F in L2.

Let h be any real L2 function satisfying the stationary correction equation in its distributional divergence form

F+div(Vh)-(2c+1)h+U[h].grad rho+div(h U[h])=0.             (1)

The products are locally integrable: the background coefficients are smooth, U[h] is L2, and h U[h] is L1. This notion includes every classical or H^(2+s) stationary correction at the same c. No gradient bound, parity, strain condition, or high Sobolev bound is assumed.

Define phi=y/(1+r^2)^2, u=(1+r^2)^(-1), t=1-u, and

I=|integral F phi|,
A=||phi[(3c+1)-4c t]||2,
B=||u^2 U[rho]||2,
C=||r u^2 grad rho||2,
D=A+5B+C.

Every such h, with m=||h||2, satisfies

I <= D m+m^2.                                         (2)

Consequently, when I>0,

m >= 2I/(D+sqrt(D^2+4I)).                             (3)

For the exact primary-chart d2 background, the separately computed full-plane intervals in ../weak_probe/verification/d2_1024.json permit a numerical evaluation of (3). In particular, if I>D(27/10000)+(27/10000)^2, no solution of (1) lies in the closed L2 ball of radius 27/10000. The numerical assertion is conditional on those interval computations and their independent audit. This is a distance bound from one background at its fixed c, not nonexistence of all stationary profiles.

## Weak identity

For a real compactly supported smooth test function psi, (1) gives

<F,psi>=<h,V.grad psi+(2c+1)psi>-<U[h],psi grad rho>+<h U[h],grad psi>.

The vector multiplier of U has squared modulus xi1^2/|xi|^2<=1. Plancherel yields ||U[h]||2<=m. Cauchy-Schwarz, followed by Holder for the last term, therefore gives

|<F,psi>| <= m[||V.grad psi+(2c+1)psi||2+||psi grad rho||2]+m^2||grad psi||infinity.     (4)

This estimate differs from the earlier gradient-cap probe by integrating the nonlinear transport term by parts before estimating it.

## Removing the compact cutoff

Choose smooth radial chi_R, equal to one for r<=R and zero for r>=2R, with |grad chi_R|<=C0/R. Apply the exact weak identity to psi_R=chi_R phi. We have phi=O(r^-3), grad phi=O(r^-4), V=O(1+r), and grad rho=O(r^(gamma-1)). Thus phi, V.grad phi, and phi grad rho are in L2. The extra term phi V.grad chi_R is bounded on its annular support by a fixed multiple of |phi|, so tends to zero in L2. The F term converges by F in L2. Finally, grad(chi_R phi) converges uniformly to grad phi, because the discarded gradient and the new cutoff term are both O(R^-4). Since h U[h] is L1, the nonlinear integral converges. Formula (4) therefore holds for phi.

## Exact gradient bound and the conservative linear denominator

The function phi is the second component of G(X)=u^2 X. The symmetric derivative DG has tangential eigenvalue u^2 and radial eigenvalue u^2(1-4t). For 0<=t<=1/4, both eigenvalue moduli are at most one. For 1/4<=t<=1, the other modulus is (1-t)^2(4t-1), whose derivative is 6(1-t)(1-2t); its maximum is 1/4 at t=1/2. Hence ||DG||operator<=1 everywhere, and equality occurs at X=0. In particular ||grad phi||infinity=1.

Also grad phi=e_y u^2-4yX u^3, so |grad phi|<=5u^2 and |phi|<=r u^2. Direct differentiation gives

cX.grad phi+(2c+1)phi=phi[(3c+1)-4c t].

The triangle inequality yields

||V.grad phi+(2c+1)phi||2<=A+5B,
||phi grad rho||2<=C.

Insert these and ||grad phi||infinity=1 in (4), proving (2). The map m to m^2+Dm is increasing for m>=0, and solving its positive quadratic root proves (3).

## Numerical verification and dependencies

The input pairing and A,B,C are exact angular reductions and outward Arb finite-power integrals from ../weak_probe/PROOF.md. The present postprocessor reads their immutable hashed output and evaluates the positive root at 512-bit precision. It also checks the rational radius directly, avoiding reliance on a rounded root. Code is in code/, interval records in verification/. All new numerical conclusions remain N4-ORIGIN until independent reproduction. There is no formal Lean artifact or numerical quadrature.
