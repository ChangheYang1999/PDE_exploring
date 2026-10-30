# A pure L2 necessary distance from the d2 background

## 1. Exact setting

Let Rj have Fourier multiplier i xi_j/|xi| on R2, U[h]=(-R1 R2 h,R1^2 h), and let rho be a smooth real background. Set V=cX+U[rho] and F=V.grad rho-rho, for fixed real c. Assume div U[rho]=0, U[rho]=O(r^gamma), grad rho=O(r^(gamma-1)) at infinity for some gamma<1, and F in L2. Lebesgue measure is used throughout.

A correction means any real h in L2 satisfying

    F+div(Vh)-(2c+1)h+U[h].grad rho+div(h U[h])=0             (1)

in distributions. Every classical correction, and every H^(2+s) correction with s>0, satisfies (1). Conversely no extra regularity of a distributional correction is being asserted. Products in (1) are well-defined locally: U is an L2 vector contraction, background coefficients are smooth, and h U[h] belongs to L1.

Put phi=y/(1+r^2)^2, u=(1+r^2)^(-1), t=1-u, and

    I=|integral F phi|,
    A=||phi [(3c+1)-4c t]||2,
    B=||u^2 U[rho]||2,
    C=||r u^2 grad rho||2.

For either D=A+5B+C or the sharper D=A+3B+C, every correction obeys

    I <= D m+m^2,  m=||h||2.                                (2)

When I>0, this implies

    m >= 2I/(D+sqrt(D^2+4I)).                                (3)

The D=5B version independently audits N4's source theorem. The D=3B improvement is an additional T4 claim pending an independent review. No inverse estimate, symmetry, strain condition, gradient bound or high Sobolev radius is needed.

## 2. Weak estimate and cutoff removal

The multiplier vector of U has squared length xi_1^2/|xi|^2<=1, giving ||U[h]||2<=m. Test (1) against compact smooth real psi and integrate the two divergences:

    <F,psi>=<h,V.grad psi+(2c+1)psi>
            -<U[h],psi grad rho>+<h U[h],grad psi>.

Thus

    |<F,psi>|<=m[||V.grad psi+(2c+1)psi||2
                  +||psi grad rho||2]+m^2||grad psi||infinity.       (4)

To use phi, take radial cutoffs chi_R, equal to one on r<=R and zero on r>=2R, with |grad chi_R|<=C0/R. The decay phi=O(r^-3), grad phi=O(r^-4), V=O(r), and grad rho=O(r^(gamma-1)) proves that phi, V.grad phi and phi grad rho lie in L2. The new term phi V.grad chi_R tends to zero in L2, since it is bounded by a constant times |phi| on its annular support. F in L2 gives convergence of the left side. Moreover grad(chi_R phi) tends uniformly to grad phi; both discarded gradient and cutoff contribution are O(R^-4). Since h U[h] is L1, the nonlinear integral converges. This proves (4) with psi=phi, directly from the distributional formulation.

## 3. Gradient and linear denominator

The vector map G(X)=u^2 X has symmetric derivative

    DG=u^2 I-4u^3 X tensor X.

Its tangential eigenvalue is u^2 and its radial eigenvalue is u^2(1-4t). As phi is the second component of G, |grad phi|<=||DG||operator. For 0<=t<=1/4 both absolute eigenvalues are <=1. For 1/4<=t<=1, the other absolute eigenvalue is (1-t)^2(4t-1), whose maximum is 1/4, attained at t=1/2. Hence ||grad phi||infinity<=1, with equality at the origin.

The direct formula grad phi=u^2 e_y-4yu^3 X gives the audited conservative estimate |grad phi|<=5u^2. Alternatively |1-4t|<=3 gives the sharper pointwise estimate |grad phi|<=3u^2. The latter constant cannot be lowered uniformly in this relative bound, since along the y-axis the ratio tends to 3 as r tends to infinity.

Also |phi|<=r u^2 and

    cX.grad phi+(2c+1)phi=phi[(3c+1)-4ct].

The triangle inequality therefore bounds the linear bracket of (4) by either stated D. This proves (2). The polynomial m^2+Dm increases strictly for m>=0 unless D=m=0, and solving the quadratic gives (3). The stable expression in (3) avoids subtracting nearly equal positive values in interval evaluation.

## 4. d2 numerical evidence and scope

The source file T4_weak_integrals.json is the T4-044 independent reconstruction of the d2 weak integrals, using exact rational polar fields and the background weak identity. Those integrals have already been checked against N4's independent full-plane computation. This audit does not reuse N4's pure-L2 postprocessor.

The code evaluates both positive roots in Arb512 from the already enclosed integrals and checks the exact rational test radius 27/10000. The records include input, proof and code SHA256 hashes, precision, time and strict comparison flags. Positivity of I-Dm-m^2 excludes the entire closed L2 ball of that radius for distributional corrections at the fixed c. This excludes all smaller high-regularity balls whose L2 projections lie there. It is a local distance bound from this specific background, not nonexistence of every stationary profile.

Dependencies: Plancherel, Cauchy-Schwarz, L1-Linfinity duality, elementary cutoff convergence and the independently confirmed weak integrals. No formal proof-assistant artifact is supplied or run.
