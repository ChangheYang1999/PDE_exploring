# Axisymmetric pressure and zero swirl

## 1. Statement, notation and scope

Fix 0<c<1/2 and a finite real omega. Let J(x_1,x_2,z)=(-x_2,x_1,0). Suppose U is a C^2 vector field on R^3 and P is a C^1 real function satisfying

    (1-c)U+(B.grad)U+omega JU+grad P=0,
    div U=0,   B=(cI-omega J)y+U.

Assume uniform sublinearity: for every epsilon>0 there is R_epsilon such that |U(y)|<=epsilon|y| for |y|>=R_epsilon. If the actual pressure P is invariant under all rotations about the z-axis, then

    U=b e_z,   P=-(1-c)b z+p_0

for real constants b,p_0. In particular a uniformly decaying profile in this class is zero. No symmetry of the velocity is assumed. The same conclusion follows if instead the angular momentum Gamma=(Jy).U vanishes identically. Under these profile and growth hypotheses, pressure axisymmetry and Gamma=0 are equivalent.

This is an independent reconstruction of LIT359 at source 0c5a871e. It uses the full momentum equation, not just its pressure Poisson equation. The proof does not assume a global bound on DU, an energy estimate, a pressure normalization, or point convergence of general carrier trajectories. Pressure symmetry remains an additional hypothesis, so the unrestricted rotating conjecture is not settled.

## 2. The carrier and torque

Uniform sublinearity and local boundedness give |U(y)|<=C_epsilon+epsilon|y|. Hence B has at most linear growth and is locally Lipschitz. On any finite time interval the usual integral inequality bounds |Y(t)| for a solution Y'=B(Y), in both time directions. Local existence then extends to all real times. Write Phi_t for this complete flow.

For sufficiently large R, skew symmetry of J gives

    y.B(y)=c|y|^2+y.U(y)>=(c/2)|y|^2   (|y|>=R).

The reverse-time vector field points strictly into every sphere of radius at least R. A first crossing would have an outward radial derivative, contradicting this inequality. Therefore

    |Phi_t(y)|<=max(R,|y|),   t<=0.

Each backward semiorbit is contained in a compact ball. This alone does not give its point limit.

Differentiate Gamma=(Jy).U. The identities

    B.grad Gamma=(JB).U+(Jy).(B.grad U),
    (JB).U=c Gamma-omega(J^2y).U,
    (Jy).JU=-(J^2y).U

give

    B.grad Gamma+(1-2c)Gamma=-(Jy).grad P.

Thus pressure axisymmetry implies Gamma(Phi_t y)=exp(-(1-2c)t)Gamma(y). The left side stays bounded as t tends to minus infinity. Since 1-2c>0, Gamma(y)=0. Conversely Gamma=0 in this identity gives (Jy).grad P=0; integration along every circle gives pressure invariance. In the remainder assume Gamma=0.

## 3. Axis regularity from the full vorticity equation

Write y=(x,z), x in R^2. Off the axis the horizontal component U_h is parallel to x. Continuity then gives U_h(0,z)=0, since a fixed nonzero vector cannot be parallel to every radial direction. If L=D_x U_h(0,z), differentiability gives Lx parallel to x for every x. The two coordinate directions make L diagonal, and their sum makes its diagonal entries equal. Hence

    D_x U_h(0,z)=a(z)I_2,   partial_z U_h(0,z)=0.

Set v(z)=U_z(0,z), g(z)=D_x U_z(0,z), and beta(z)=cz+v(z). Divergence gives

    2a+v'=0,   beta'=c-2a.

The axis is invariant for B, with scalar equation z'=beta(z). Its vorticity is

    w(z)=Omega_h(0,z)=(g_2,-g_1),   Omega_z(0,z)=0.

The momentum equation expresses grad P as a C^1 vector field, so P is C^2 and its curl vanishes classically. Taking curl yields

    Omega+B.grad Omega-(Omega.grad)U+omega JOmega=0.

On the axis the horizontal stretching is a w, while the vertical stretching is g.w=0. Therefore

    beta w'+(1-a)w+omega J_2w=0.                         (A)

Consider an axis point with beta not zero. Its orbit remains in one connected component of {beta!=0}, by uniqueness. It is strictly monotone and backward bounded, so it tends to a finite z_* as t tends to minus infinity. Necessarily beta(z_*)=0: otherwise its speed has a fixed nonzero lower bound near the proposed limit. If beta is positive on the component, the orbit approaches its left endpoint and beta(z)/(z-z_*)>0; if beta is negative, it approaches its right endpoint and both numerator and denominator are negative. In either case differentiability implies beta'(z_*)>=0. Consequently

    a(z_*)<=c/2<1.

For all sufficiently negative t, 1-a(z(t))>=delta>0. Taking the Euclidean squared norm in (A), the skew term cancels and gives

    d|w(z(t))|^2/dt=-2(1-a(z(t)))|w(z(t))|^2.

Any nonzero value at a finite time would force exponential growth backward on that tail. This contradicts continuity of w on the compact orbit closure. Thus w=0 at every nonstationary axis point.

At an equilibrium, (A) is the algebraic equation

    ((1-a)I_2+omega J_2)w=0,

whose determinant is (1-a)^2+omega^2. If the determinant is zero, then omega=0 and a=1. In that exceptional case beta'=c-2 is nonzero, so the equilibrium is isolated, with nonstationary points arbitrarily close. Their w values are zero, and continuity gives w=0 at the equilibrium. All other equilibria have invertible matrices. This includes nonisolated equilibrium sets. We conclude

    D_x U_z(0,z)=0   for every z.                         (B)

Only one-dimensional axis orbits were proved to converge. No convergence statement for the full three-dimensional carrier flow was used.

## 4. The damped meridional quotient

For r=|x|>0 write U=f(r,theta,z)e_r+g_0(r,theta,z)e_z. Here g_0 is a scalar component, distinct from the axis gradient g above. Define

    D=(cr+f)partial_r+(cz+g_0)partial_z-omega partial_theta.

The frame derivative of -omega partial_theta U cancels omega JU. Because the azimuthal velocity is zero, there is no azimuthal centrifugal term. The radial and vertical momentum equations and divergence are

    Df+(1-c)f+P_r=0,
    Dg_0+(1-c)g_0+P_z=0,
    f_r+f/r+(g_0)_z=0.

Let q=f_z-(g_0)_r and xi=q/r. Apply partial_z to the first momentum equation and subtract partial_r of the second. The commutator terms are

    f_z f_r+(c+(g_0)_z)f_z
      -(c+f_r)(g_0)_r-(g_0)_r(g_0)_z
    =(c+f_r+(g_0)_z)q.

Thus

    Dq+(1+f_r+(g_0)_z)q=0,
    Dq+(1-f/r)q=0.

Since Dr=cr+f, division gives exactly

    Dxi=-(1+c)xi.                                       (C)

All theta dependence remains present. The angular coefficient -omega is constant, so it causes no additional commutator term.

On any fixed compact cylinder, local C^2 bounds and the axis equalities give

    |f_z|<=Cr,   |(g_0)_r|<=Cr.

Indeed partial_z U_h vanishes on the axis and has bounded horizontal derivative there; D_x U_z vanishes on the axis by (B) and has bounded horizontal derivative. Both estimates are uniform in theta and z on the cylinder. Therefore xi is bounded uniformly up to the axis, although a continuous extension of xi itself is not asserted or needed.

An off-axis trajectory cannot meet the axis in finite time, by invariance of the axis and uniqueness of the complete flow. Equivalently, on any finite compact trajectory segment, r'=(c+f/r)r has bounded coefficient, since U_h vanishes on the axis and DU is locally bounded. Along an arbitrary backward off-axis orbit, the compact bound for xi and (C) imply

    xi(Phi_t y)=exp(-(1+c)t)xi(y),   t<=0.

The factor diverges backward, since 1+c>0. Hence xi=0 and q=0 off the axis.

## 5. Auxiliary harmonic slices

Fix an angle theta_0. Copy f(r,theta_0,z) and g_0(r,theta_0,z) to an auxiliary axisymmetric field

    V(r,phi,z)=f(r,theta_0,z)e_r(phi)+g_0(r,theta_0,z)e_z,
    V(0,z)=v(z)e_z.

This construction does not claim that U was axisymmetric. It permits a separate harmonic argument for each meridional slice.

The local axis limits, uniform for z in compact intervals, are

    f/r -> a,   f_r -> a,   f_z -> 0,
    (g_0)_r -> 0,   g_0 -> v,   (g_0)_z -> v'.

For example D_x U_h=aI gives the first two, and (B) gives the fourth. The horizontal derivative of V_h is

    (f/r)I_2+(f_r-f/r)e_r tensor e_r,

which tends to aI_2. The other derivative limits are precisely the remaining displayed limits. The first-order expansions also give differentiability on the axis. Therefore V is globally C^1, without any unproved C^2 parity expansion at r=0.

Off the axis, the already proved divergence and q=0 identities give div V=0 and curl V=0. Since V is C^1, these identities hold on the axis by continuity, hence on all R^3 in distributions. There is no possible line-supported curl or divergence defect. Consequently each component of V is distributionally harmonic and therefore smooth and harmonic.

The auxiliary field has the same norm as the original field at the point (r,theta_0,z), so uniform sublinearity is inherited. For an entire harmonic scalar h with this growth, the interior gradient bound is

    |grad h(y_0)|<=C R^-1 sup_(B_R(y_0))|h|.

Given epsilon>0, split this supremum into a fixed compact set, where h is bounded, and its complement, where |h(y)|<=epsilon|y|. Letting R tend to infinity gives |grad h(y_0)|<=C epsilon; then let epsilon tend to zero. Thus V is constant. Its horizontal part vanishes on the axis, so V=b(theta_0)e_z. All slices share the same axis function v(z); constancy of each slice forces that function to be one constant b, independent of theta_0. Hence U=b e_z globally. Substitution gives the pressure stated in Section 1.

## 6. Necessary distinction and verification limits

The smooth divergence-free field U=(0,0,x_1) has Gamma=0 but q/r=-cos(theta)/r, so smoothness and zero swirl alone do not supply the quotient bound. Its pressure-free profile residual is (x_1+omega x_2)e_z, whose curl is (omega,-1,0). Thus it is not a full profile for any omega; it also fails uniform sublinearity. The axis use of the full vorticity equation is necessary in this proof.

All source proof sections and the 33 stated author checks were read. They agree with the reconstruction. These author checks are not an independent verification log. No mathematical computation is needed or has been performed for this audit. Standard inputs are ODE uniqueness and continuation under linear growth, the elementary first crossing argument, distributional harmonic regularity and the harmonic interior gradient estimate. There is no external dynamical theorem hidden in the proof.

The exact additional hypothesis remains pressure axisymmetry, or equivalently Gamma=0 under the stated assumptions. Nothing here proves that hypothesis from decay. The angular mean of an arbitrary pressure is axisymmetric, but the corresponding averaged velocity solves an equation with Reynolds-stress forcing. It does not satisfy the unforced profile equation assumed here, so averaging does not allow this theorem to be applied to every profile. An existing configured model comparison of the full source and this reconstruction is requested before a new designated verdict. Actual provider execution remains independently unattested.


## 7. Existing C comparison and final audit

The complete eight-item C comparison dated 2026-11-04T06:45:33Z was read. Its first five items independently recover the torque cancellation, axis slope sign, exceptional stationary matrix, damped quotient, C1 auxiliary field, and shear countertest. They agree with Sections 2-6. The sixth item translates the pressure hypothesis into the vanishing of every nonzero angular pressure mode. This translation is valid under the stated regularity. Its assertion about a nonzero profile is read in the decaying class: the constant axial solution is a nonzero sublinear profile with symmetric pressure. The following report pointer explicitly uses that qualification.

The two optional analytical precisions are valid. At nonstationary orbit points the ratio beta(z)/(z-z_*) is strictly positive, while its limiting derivative is merely nonnegative. For the C1 extension, let G be the continuous matrix field supplied by the off-axis derivative formulas and their axis limits. Approximate a line segment from p to p+h by parallel segments missing the axis. The fundamental theorem of calculus and uniform convergence give V(p+h)-V(p)=integral_0^1 G(p+th)h dt. Continuity of G proves differentiability on the axis with derivative G(p), including segments lying in the axis. Alternatively the local first-order expansions in Section 5 give the same result. No extra parity or C2 regularity of the auxiliary field is used.

The comparison's diagnostic paragraph reports two symbolic scripts and two stopped preliminary runs. These scripts and logs were not read or rerun in this audit. Their counts, failure histories and generic-versus-sample classifications are therefore not certified here and are not proof premises. The eight analytical comparison items were read in full; the separate statement about the report's unchanged D4-D6 block is not a fresh audit of that block.

Conclusion: the exact theorem in Section 1 is confirmed, for every finite omega. The pressure or zero-swirl condition remains essential to the theorem as proved. It is not obtained by angular averaging, and this result does not settle the unrestricted rotating problem. The independently established nonrotating case is unchanged. The comparison uses an existing agent configured as model; actual provider execution is independently unattested. No new client or agent was used.

## 8. Source status revision

The source revision 57757d62fa504996bf622ab0e004cf0253850f233b504196bc81cd4c88d47039 was compared byte for byte with the originally reviewed 0c5a871e27af520f40247b8d49d2f50aa81168380aed52c861ab26d152cdf486. The entire one-hunk difference changes only the status paragraph. It cites A3029-A3031, retains pressure symmetry as an additional hypothesis, and explicitly permits nonzero axial constants under sublinearity while imposing zero under decay. All eight mathematical source sections are unchanged. The full difference was read and agrees with the designated verdicts. The C comparison's analytical qualification in Section 7 remains in force; no diagnostic code or execution history is certified by this status check.
