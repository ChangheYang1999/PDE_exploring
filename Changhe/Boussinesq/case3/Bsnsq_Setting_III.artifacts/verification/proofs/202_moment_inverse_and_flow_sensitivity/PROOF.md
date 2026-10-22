# Exact strain moments and finite-cutoff characteristic sensitivities

## Statement, notation and hypotheses

Use the B2 conventions -Delta Psi=Omega, V=(-Psi_y,Psi_x), with V(0)=0 in the relative gauge, and X=(r sin phi,-r cos phi). Let Omega=sum_(n=1)^N H_n(r) sin(n phi), smooth at the center and with positive power decay at infinity. Assume enough radial derivatives for the expressions below. There is no freely added linear strain. Write the canonical modal stream as Psi=sum r f_n(log r) sin(n phi), and c=Psi_xy(0). All integrations extend over the whole plane. This result is an inverse and prescribed-velocity transport calculation; it gives no fixed point or B2 existence theorem.

For the second sine mode, M_2=integral_0^infinity H_2(s) ds/s exists and equals -2c. Put

 A_n(r)=integral_0^1 z^(n+1) H_n(rz) dz,
 C_1(r)=integral_0^1 H_1(rz) dz,
 I_2(r)=integral_0^1 H_2(rz) dz/z.

Then the relative modal inverse satisfies

 f_1=(r/2)(A_1-C_1),  Psi_1'=-(r/2)(A_1+C_1),
 f_2=(r/4)(A_2+M_2-I_2),  Psi_2'=(r/2)(-A_2+M_2-I_2).

For n>=3 use O_n(r)=integral_0^1 q^(n-3)H_n(r/q)dq and

 f_n=r(A_n+O_n)/(2n),  Psi_n'=r(-A_n+O_n)/2.

The exact second-mode moment can replace a cancellation-prone exterior integral. The formula is exact for the specified source, including a nonzero numerical projection remainder in its actual center moment. It does not license replacing a source moment by a desired target value.

## Proof of the inverse formulas and moment

The radial equation -Psi_n''-Psi_n'/r+n^2 Psi_n/r^2=H_n has homogeneous solutions r^n,r^-n. Variation of constants, regularity at0 and exclusion of a growing homogeneous strain for n>=2 give

 Psi_n=(1/(2n))[r^-n integral_0^r s^(n+1)H_n(s)ds+r^n integral_r^infinity s^(1-n)H_n(s)ds].

The displayed A_n,O_n formulas follow by s=rz and s=r/q. Differentiation cancels the two boundary-source terms and gives the formula for Psi_n'. For n=1 subtract the center linear stream, replacing the exterior integral by -integral_0^r H_1(s)ds. This gives the stated f_1 and derivative. For n=2 the exterior factor is integral_r^infinity H_2(s)ds/s=M_2-I_2. Since H_2(r)=O(r^2) at0, A_2,I_2=O(r^2). Thus Psi_2=(M_2/4)r^2 sin(2phi)+O(r^4). As r^2 sin(2phi)=-2xy, c=-M_2/2. Other angular modes make no contribution to Psi_xy(0). This also proves the sign of the moment.

For an r2 divided spline G=D sum S_k(t)rho_k(r)cos(kphi), Omega=xG, the angular product gives H_2=rD rho_odd(S_1-S_3)/2. With t=1-(1+(r/L)^2)^(-1/(2b)) and D=(1-t)^(b+1), D rho_odd dr=bL dt. Hence M_2=(bL/2)integral_0^1(S_1-S_3)dt=-2c. For partition-of-unity-normalized B-splines whose support lies in [0,1], including clamped and repeated knots, the integrals are (knot_(j+d+1)-knot_j)/(d+1). For binary-rational b and L, binary-rational coefficients, and regenerated binary-rational knots, this moment is an exact rational number. The actual native origin masks are needed for smoothness; arbitrary unmasked angular coefficients need not define a smooth source. Canonical here means no added homogeneous solutions, not decay of the stream, whose second mode may grow like r^(2-1/b). Mixed sources are treated linearly in their separate native maps. No large numeral table or generated formal file is needed.

## A C2 velocity interpolant and its directional second derivative

Let s=log r and f=Psi_n/r. The modal Poisson equation gives

 f_ss=(n^2-1)f-2f_s-rH_n,
 f_sss=(n^2-1)f_s-2f_ss-rH_n-r^2 H_n'.

A piecewise degree-seven Hermite interpolant matching f,f_s,f_ss,f_sss at each radial node is C3 in s; its stream is C3 on any positive annulus and its velocity is C2 there. The formulas use actual source derivatives. They do not imply exact Poisson inversion between nodes. Distinct node grids and direct inverse values must still be compared.

Here and below dots mean summation over n. Let e_r=X/r, e_t=J e_r, J=[[0,-1],[1,0]], Q=[e_r,e_t], S=sin(nphi), C=cos(nphi). The Hessian of Psi in this moving orthonormal frame is B with

 B_rr=dot(f_s+f_ss,S)/r,
 B_rt=dot(n f_s,C)/r,
 B_tt=dot((1-n^2)f+f_s,S)/r.

Consequently DW=beta I+J Q B Q^T. At a physical direction Z put ds=e_r.Z/r and dphi=e_t.Z/r. Differentiation of Q gives dQ=dphi QJ, so

 D(DW)[Z]=J Q [B_s ds+(B_phi+JB-BJ)dphi] Q^T.

The components needed are

 (B_rr)_s=dot(f_sss-f_s,S)/r,
 (B_rt)_s=dot(n(f_ss-f_s),C)/r,
 (B_tt)_s=dot((n^2-1)f-n^2 f_s+f_ss,S)/r,

 (B_rr)_phi=dot(n(f_s+f_ss),C)/r,
 (B_rt)_phi=-dot(n^2 f_s,S)/r,
 (B_tt)_phi=dot(n((1-n^2)f+f_s),C)/r.

These follow by differentiating the displayed B, including derivative of1/r. They supply a directional Hessian of W without subtracting nearly equal velocity Jacobians. They will be independently checked against Cartesian differentiation on a polynomial stream and on the interpolant.

## Moving hit time and parameter sensitivity

Fix beta>2, a0, delta>0 and a final point Y. Let W_h=W_0+h Z_0 be a C2 family on a compact annulus. Let x(t,h) solve backward flow x_t=-W_h(x), x(0,h)=Y, with a unique transverse first hit |x(T(h),h)|=delta and positive flux W_h.n. Let p=partial_h x at fixed t. At h=0,

 p_t=-DW_0(x)p-Z_0(x), p(0)=0,
 T_h=n.p(T)/(n.W_0(x(T))),
 x_seed,h=p(T)-W_0(x_seed)T_h.

These follow by differentiating the ODE and the circle equation. In particular n.x_seed,h=0. The temperature with boundary a0 x_seed,x^2 satisfies

 Theta_h=exp((beta-2)T)[(beta-2)T_h a0 x_seed,x^2+2a0 x_seed,x x_seed,h,x].

The corrected full gradient seed is g_seed=v+n N/F, where v=(2a0 x_seed,x,0), N=(beta-2)a0 x_seed,x^2-W_0.v and F=n.W_0. Its derivative follows by the product and quotient rules using n_h=x_seed,h/delta, v_h=(2a0 x_seed,h,x,0), W_seed,h=DW_0 x_seed,h+Z_0. The vorticity seed is4a0 x_seed,x/beta and its derivative4a0 x_seed,h,x/beta. These boundary values are imposed finite-cutoff data, not exact finite-radius center Taylor series.

For the forward gradient-vorticity vector v=(g_x,g_y,omega), let A(X) have upper-left block (beta-2)I-DW_0(X)^T, lower row(1,0,-1), and zero upper-right block. Use fixed tau in[0,1] and xbar(tau,h)=x(T(h)(1-tau),h). Its derivative is

 xbar_h=p(T(1-tau))-W_0(xbar)(1-tau)T_h.

The forward system is v_tau=T A(xbar)v. Therefore its sensitivity w=v_h satisfies

 w_tau=T_h A v+T A w+T A_h,total v,

where A_h,total has upper-left block -[D(DW_0)[xbar_h]+DZ_0]^T and all other entries0. Start at the differentiated corrected boundary data. Ordinary ODE parameter dependence under the C2 and transverse-hit hypotheses proves that w(1) is the exact derivative of this finite-cutoff interpolated-flow map. The source parameter enters both the projected self field and the fixed native source as in P200. This theorem does not assert a uniform delta-to-zero limit or a continuum derivative.

## Planned verification and dependencies

P200 gives the finite-cutoff scalar construction and projected source convention. This proof independently rederives the inverse moment, moving hit and response equations. Manufacture smooth streams and known transported fields to check signs and compatibility. Recompute native directions using the moment identity and record complete quadrature failure reasons. Compare C2 interpolants, parameter sensitivity equations, parameter differences, cutoff radii and node grids. Raw quadrature error estimates are not validated error bounds. No full B2 endpoint is implied.

## Interpretation of the numerical comparisons

At the same fixed beta, cutoff, source projection and node interpolant, the differentiated ODE and centered parameter differences evaluate the same scalar map derivative. Their agreement tests the implemented sensitivity equations; it is not a bound on derivatives of the continuum characteristic map. Comparing two cutoff radii changes the imposed finite-radius boundary data and integration time, so this is a different approximation error. Comparing node grids changes the prescribed velocity itself. These errors must be reported separately component by component.

For the forced source, denote Omega_total=Omega_projected_self+lambda Omega_native. The independent inverse constructs W=beta X+V[Omega_total]. Its transported vorticity Omega_transport is a different scalar, obtained from the prescribed finite-cutoff transport problem. The unforced B2 equations would require Omega_transport=Omega_total as well as the remaining compatibility and normalization conditions. Thus a sampled difference between these quantities is a useful closure diagnostic. It does not by itself certify a global residual or rigorously exclude an exact profile near the sampled field. No numerical value in this comparison is an existence theorem or a validated error enclosure.

## Linearity control for the numerical derivative experiment

Fix the same radial nodes. The map from the source and inverse node data (f,f_s,H,H') to (f,f_s,f_ss,f_sss) is linear, by the displayed modal Poisson identities. At each interval, Hermite interpolation is the unique polynomial satisfying its eight linear endpoint constraints. The interpolation operator is therefore linear. Differentiation and evaluation of the stream to obtain W-beta X and DW-beta I are also linear. Consequently the interpolant constructed from base+h times direction node arrays is identical in exact arithmetic to the affine field W_0+h Z_0, with Jacobian DW_0+h DZ_0. An implementation evaluating this affine combination directly is a legitimate way to study the same prescribed family while avoiding a repeated polynomial construction. Floating-point constructions can differ, and subtracting reconstructed scalar outputs at parameter separation h can amplify those differences by 1/h. This observation suggests a diagnostic, not a proved explanation of the observed errors; the two constructions and tolerance effects must actually be compared.

## Parameter stencil and regularity scope

The implemented parameter comparison is D_h F=[F(-2h)-8F(-h)+8F(h)-F(2h)]/(12h), applied componentwise at a fixed base point. For a C1 scalar F, write each difference from F(0) as an integral of F'. The coefficients cancel the constant and reproduce the linear term, and therefore

 |D_h F-F'(0)| <= (5/3) sup_{|t|<=2|h|}|F'(t)-F'(0)|.

Thus this stencil converges for a C1 map, without a rate supplied by C1 alone. If F is C5 on a neighborhood, Taylor's formula gives D_h F=F'(0)-F^(5)(0)h^4/30+o(h^4). The finite-cutoff C2 velocity theorem above gives C1 parameter response, not the needed uniform C5 property across interpolation knots. The numerical report therefore identifies the actual four-point centered stencil without claiming a validated order of truncation or an O(h) error bound.

The exact affinity assertion concerns real arithmetic on the stored base and direction node arrays. Each array was originally produced by its own adaptive quadrature. They are then held fixed for every h, interpolation comparison and ODE tolerance within the diagnostic process. No new adaptive quadrature is invoked at shifted h. It is not asserted that separate, adaptively selected quadrature calls on base+h times direction would themselves constitute a linear numerical operation. A fixed linear operation can be recomputed without breaking exact affinity. The stream is C3 and its velocity C2 on the interpolation annulus; higher spatial derivatives at knot surfaces need not exist two-sidedly. These qualifications leave the finite-cutoff derivative theorem unchanged.
