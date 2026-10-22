# Affine kernels and the first constant-induced tail in the stream trial space

Written 2026-10-21T03:08:36.680307+00:00, before implementation. Status: own complete algebraic proof; model follow-up and implementation checks pending. This is a restricted representation statement, not a B2 endpoint.

## Statement and notation

Use packet114's finite smooth stream and temperature basis with R=(1+x²+y²)^(1/2), s=1/beta, t=R^-s, u=2t-1, z=y/R, both shifts d=0,1, and i=0,...,ni-1, j=0,...,nj-1. The raw stream is p=x R^(1-s-d) T_i(u) T_j(z); the represented stream subtracts x p_x(0). Temperature basis elements are x² R^(-1-2s-d) T_i(u) T_j(z). Coefficients are C_ijd,D_ijd. V is the canonical relative velocity, as proved in114.

(A) At an integer beta=m>=3 the raw two-shift kernel has dimension nj max(0,ni-m) for either field. The gauged stream kernel has dimension nj max(0,ni-m)+1 when ni>=m, and zero when ni<m. The extra direction represents an affine raw stream p=x, which is killed by the determined gauge subtraction. Temperature has no such extra direction. These exact functional kernels persist after imposing the center chart. At noninteger beta>2 both field bases, including the gauged stream, are functionally independent. None of this is a statement about the finite collocation Jacobian, which may have further rank losses.

(B) Let 2<beta<3. Put

    P_d(z)=sum_ij (-1)^i C_ijd T_j(z),
    Q_d(z)=sum_ij (-1)^i D_ijd T_j(z),
    C_inf=-sum_ijd C_ijd T_j(0).

The constant term in the relative velocity after its growing homogeneous terms is (0,C_inf). The shift1 leading fields have the degrees and angular factors

    psi_frac=x r^-s P_1(y/r),
    Omega_frac=-Delta psi_frac,
    Theta_frac=x² r^(-2-2s) Q_1(y/r).

If the defining PDE residuals vanish identically then necessarily

    P_1=(C_inf/beta) [(1-s) z P_0+(1-z²) P_0'],
    Q_1=(C_inf/beta) [(-1-2s) z Q_0+(1-z²) Q_0'].             (1)

In particular equations(1) do not force C_inf=0 in this two-shift representation. The shift1 family explicitly supplies the first noninteger-power terms induced by a nonzero constant in the inverse. Applying packet99's missing-power exclusion to this representation would violate its expansion hypotheses. This does not show that any full profile has C_inf nonzero. Equations(1) are necessary conditions only.

## Proof of (A)

The variables (t,z) range over an open two-dimensional set: 0<t<1 and |z|<sqrt(1-t^(2 beta)). Divide a raw dependence by the nonzero common prefactors on x>0. Since u=2t-1, the two radial blocks are P(t,z)+t^beta Q(t,z), with polynomial degree at most ni-1 in t and nj-1 in z. At beta=m, coefficient comparison in z shows P=-t^m Q, and Q has t-degree at most ni-1-m. This gives nj max(0,ni-m) independent coefficients. For noninteger beta, a nonzero relation would make t^beta a rational function of t after fixing any generic z. Its order at t=0 is an integer, a contradiction. Thus the raw noninteger basis is independent.

The kernel added by gauge subtraction is the preimage of the one-dimensional raw affine space spanned by x. The equation for this preimage is P+t^beta Q=t^(beta-1), with no z dependence on the right. When beta=m, t^(m-1) is represented exactly iff ni>=m; t^m Q cannot provide its missing degree when ni<m. When beta is noninteger, the exponents in P are nonnegative integers and those in t^beta Q are beta plus nonnegative integers, so none equals beta-1; their finite linear independence follows, for example, by successively comparing the least exponent as t tends to0. Thus no raw affine direction exists at noninteger beta. Quotienting out the one-dimensional affine image adds exactly one kernel when ni>=m and none otherwise. The raw kernel and affine kernel have zero strain and zero vorticity center derivative, so their directions satisfy the homogeneous center constraints and remain in the fixed-pivot chart.

## Proof of (B)

Expanding R and y/R in even powers r^-2 and each Chebyshev polynomial in powers t gives a convergent differentiable expansion for r>1. The d=0 stream terms have degrees 2-(k+1)s-2n and the d=1 terms have degrees 1-(k+1)s-2n. Their gradients are velocity terms with one lower degree. For noninteger beta in(2,3), no raw velocity degree is zero: (k+1)s+2n=1 would require beta=k+1, and all d=1 degrees are negative. The gauge is therefore the sole constant contribution, C_inf as displayed.

Write psi_0=x r^(1-s) P_0(y/r), Omega_0=-Delta psi_0 and Theta_0=x² r^(-1-2s) Q_0(y/r). In the vorticity residual, the coefficient of the distinct degree -1-s is

    C_inf partial_y Omega_0 - beta Omega_frac.             (2)

Indeed linear transport acts on Omega_frac of degree -1-s by the factor 1+beta(-1-s)=-beta. Products between two unshifted terms have degrees -k s, which cannot equal -1-s at a noninteger beta. Products containing a shifted velocity or shifted vorticity, and the shifted temperature derivative, first have the strictly smaller degree -1-2s. Even radial corrections first lower degree by2. The analogous distinct coefficient of degree -2s in the temperature residual is

    C_inf partial_y Theta_0 - beta Theta_frac.              (3)

The same exponent separation proves this, since products of unshifted fields have degrees 1-k s and the first shifted nonlinear products have degree -3s. A vanishing total residual makes each coefficient vanish by uniqueness of a finite ordered asymptotic expansion.

Equation(2) says Delta(C_inf partial_y psi_0-beta psi_frac)=0 off0. The difference is homogeneous of degree 1-s in(1/2,2/3). A smooth periodic angular function H solves H''+(1-s)²H=0 only if it is zero, since 1-s is not an integer. Hence psi_frac=(C_inf/beta) partial_y psi_0. Direct differentiation at fixed x gives

    partial_y psi_0=x r^-s [(1-s) z P_0+(1-z²) P_0'],
    partial_y Theta_0=x² r^(-2-2s) [(-1-2s) z Q_0+(1-z²) Q_0'].

Together with(3), these are(1). To check that these relations alone permit C_inf nonzero, take beta=5/2, P0=Q0=1, C_inf=1, P1=(6/25)z and Q1=-(18/25)z. With ni>=2,nj>=2 realize this by C_(1,0,0)=-1, C_(0,1,1)=6/25, D_(0,0,0)=1, D_(0,1,1)=-18/25, all other coefficients zero. The displayed leading polynomials and C_inf are exactly as prescribed. This example need not satisfy the center strain or either PDE. This proof uses only exact residual coefficient matching; no numerical fit or assumption of small residual enters.

## Dependencies and scope

Packet114 supplies the representation, parity and canonical relative inverse. Packet99 supplies context for the tempting but invalid missing-power application; the present proof is direct. The constraints allow sign-changing coefficients and do not impose a physical fixed-center condition. Exact finite angular support already prevents an exact admissible profile (packets83-84); no positive residual floor, no behavior of infinite-dimensional limits and no exponent determination is asserted here.
