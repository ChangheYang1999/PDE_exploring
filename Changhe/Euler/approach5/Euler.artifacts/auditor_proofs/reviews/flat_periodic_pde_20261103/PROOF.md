# Symmetry and finite-order obstructions at a flat periodic carrier

Status: independent reconstruction and complete final postread finished; confirmed at A559-A560 scope. General C2 germs remain open. A local construction is excluded by a closed vortex only when the no-closed-vortex condition is included.

## 1. Exact setting

Let 0<c<1/2, a=1-2c, kappa=1+c, d=3c, omega any finite real number, Jx=(-x2,x1,0) and A=cI-omega J. On a tubular neighborhood N of a periodic B-orbit Gamma, suppose U is C2, P is C1, B=Ay+U, div U=0, U.W=0 for W=curl U, and the rotating profile equation holds. Write

    H=P+|U|^2/2+(Ay).U, g=U.B.

Assume Gamma is in the closure of {W!=0}, has period T, and on Gamma

    W=DW=0, U!=0, g=0, H=h0,
    dH=-a Uflat, dg=rho Uflat,
    Phi_t^*dH=exp(rho t)dH.

Its Floquet multipliers are 1, exp(rho T), exp((d-rho)T). Work in either range rho>=2-c or rho<=-2a. They are hyperbolic saddle ranges with positive simple transverse multipliers. In the first range the rho cylinder is unstable and W vanishes there; in the second it is stable and W is tangent there. These cylinder facts are the confirmed A474/A462 inputs, or explicit local hypotheses.

The exact identities used near Gamma are

    grad H=-aU+B cross W, BH=-ag, WH=0,
    [B,W]=-kappa W, div B=d, div W=0.

For global C2 profiles with uniform U=o(|y|), A014 prohibits nonconstant closed W-orbits. For a purely local germ impose that prohibition separately. The following conclusions hold:

1. An axisymmetric germ cannot satisfy this prohibition. A germ with nonzero-pitch screw symmetry cannot have the specified carrier and multipliers, even without the prohibition.
2. If U is C^(n+2) and W has a first nonzero transverse Taylor term of degree n>=2 along Gamma, there is a nonconstant closed W-orbit in every sufficiently small tube. Thus a real-analytic germ satisfying all the carrier and no-closed-vortex conditions is impossible.
3. A C-infinity germ satisfying these conditions has W flat to every order along Gamma and W=0 on both local invariant cylinders. This gives no vanishing neighborhood.

The statements do not assume decay beyond the global hypothesis needed to invoke A014. They do not construct or exclude a general C2 nonsymmetric germ.

## 2. The local scalar normal form is a reduction only

On a simply connected vortical box with dH!=0, g!=0 and dH wedge dg=0, set x=H-h0 and g=G(x). Put beta=Uflat+dx/a. The triple product gives grad x cross beta_sharp=gW, hence dx wedge beta=G d beta. Choose f!=0 with f'/f=1/G. Then d(beta/f)=0 and

    U=f(x)grad psi-grad x/a,
    B psi=0, W=f'(x)grad x cross grad psi.

Since Bx=-aG!=0, W=0 here is equivalent to grad psi=0. The remaining equations are precisely

    (Ay+f grad psi-grad x/a).grad psi=0,
    (Ay+f grad psi-grad x/a).grad x=-aG(x),
    f Delta psi+f' grad x.grad psi-Delta x/a=0.        (1)

Conversely sufficiently regular solutions of (1), f'=f/G and the displayed U, with P=h0+x-|U|^2/2-(Ay).U, satisfy div U=0, helicity zero and B cross W=af grad psi. This is grad H=-aU+B cross W and therefore the full profile equation. This converse is understood at regularity yielding U in C2 and P in C1.

If G(x)=-(rho/a)x+o(x), integration gives f=|x|^(-a/rho+o(1)). If the error is O(x^2), f=C_+/- |x|^(-a/rho)(1+O(|x|)). Divergence of f is compatible with vanishing grad psi. Neither a global function G on disconnected level fibers nor an equation in an open irrotational gap follows. This repeats the confirmed A482 scope.

## 3. Axisymmetry creates closed vortex circles

Assume [Jy,U]=0 in N. Then [Jy,B]=0. Along Gamma, Jy is a periodic variational solution. Simplicity of the multiplier 1 makes it a constant multiple of B. If this multiple vanished, the entire nonconstant periodic orbit would lie on a line, which is impossible by uniqueness for a one-dimensional autonomous flow. Otherwise Gamma is a rotation circle r=R>0,z=Z. Choose a smaller rotation-invariant tube.

The profile equation makes grad P rotation-equivariant. The difference P(R_theta y)-P(y) is spatially constant, additive in theta and periodic, so it is zero. H and g are likewise axisymmetric. On Gamma, B is nonzero and azimuthal, and g=0 gives U_theta=0. Consequently B_theta=-omega R. At omega=0 this already contradicts periodicity; otherwise its minimal period is 2pi/|omega|.

Set ell=r U_theta. The azimuthal equation is

    B_r partial_r U_theta+B_z partial_z U_theta
                         +(1-c+U_r/r)U_theta=0.

The rotation terms cancel exactly. Using B_r=cr+U_r gives B ell=-a ell. Also W_r=-ell_z/r and W_z=ell_r/r. Since WH=0 and grad H!=0 on a small meridional box, ell=L(H-h0), with L in C2. Choose connected meridional level arcs so this is one function on the smaller tube. The two transport laws give L'(x)g=L(x).

A C2 transversal q(s) with H(q(s))-h0=s gives k(s)=g(q(s))=-(rho/a)s+O(s^2). W=0 on Gamma gives L(0)=L'(0)=0. On either punctured side k(s)L'(s)=L(s); if the solution is nonzero there, linear ODE uniqueness and integration of 1/k give

    L(s)=C |s|^(-a/rho) exp(O(s)), C!=0.

For positive rho this is unbounded at zero. For rho<=-2a its exponent is in (0,1/2], contrary to L=o(s). Hence ell=0 on the entire smaller tube. W is then azimuthal and every nonzero W-point lies on a whole rotation circle with constant nonzero angular speed. Such points exist by the carrier closure hypothesis. These closed vortex circles contradict the specified prohibition. Without that prohibition the local conclusion is the existence of circles, not local PDE nonexistence.

## 4. Nonzero-pitch screw symmetry forces an impossible multiplier

Let Z=e3 and K=Jy+bZ with b!=0, and assume [K,U]=0 locally. Curl has the same symmetry. For the local screw motion S_s y=R_s y+bsZ,

    B(S_s y)=R_s B(y)+cbsZ, W(S_s y)=R_s W(y).

Pushing the C1 bracket equation forward and subtracting gives partial_z W=0, with no second derivative of W. Combining this with screw symmetry gives ordinary axial symmetry of W. Away from the axis its physical cylindrical components depend locally only on r. All derivatives of rW_r vanish by div W=0. The connected tube with the axis removed is path connected, since polygonal paths can be perturbed off a codimension-two line. A nonconstant closed orbit has an off-axis point, where W=0; hence W_r=0 everywhere in this connected region.

Put D0=W_z-b W_theta/r. Screw symmetry gives partial_theta U_j=-b partial_z U_j in cylindrical components. The radial curl relation, the z derivative of U.W=0 and the radial bracket equation respectively give

    partial_z U_theta=-(b/r)partial_z U_z,
    D0 partial_z U_z=0,
    D0 partial_z U_r=0.

Thus partial_z U=0 where D0!=0. There is no open vortical subset with D0=0: there W=wK and

    [B,W]=(Bw)K-cbwZ=-kappa wK,

and independence of K,Z forces w=0, a contradiction. Consequently {D0!=0} is dense in the vortical set off the axis. Continuity extends partial_z U=0 to its closure, including all of Gamma. Along Gamma, DB Z=cZ, so exp(ct)Z is a variational solution. It forces multiplier exp(cT). In the upper range rho>c and d-rho<0; in the lower range rho<0 and d-rho>=2-c>c. Neither list contains c or allows c=0, so the multiplier is impossible. No vortex-period argument is used here.

## 5. A first transverse Taylor term produces a closed vortex

Assume U in C^(n+2), n>=2, and its first nonzero transverse W term has degree n. The profile equation gives P,H in C^(n+2) locally. The hyperbolic invariant cylinder C through the rho direction has the same required differentiability, and W is tangent to it by the stated input. Since the restriction of dH to this cylinder is nonzero, choose periodic coordinates (theta,x,y), theta modulo T, with x=H-h0 and C={y=0}.

Here is the required first-order normalization. The two positive real Floquet multipliers give periodic real transverse Floquet vectors. The rho vector has nonzero pairing with dH, constant along Gamma by the displayed covector transport; rescale it to pairing 1. The other vector pairs to zero. The resulting tubular coordinates have

    B=partial_theta+rho x partial_x+sigma y partial_y+O((|x|+|y|)^2),
    sigma=d-rho.

Replacing the transverse coordinate by H-h0 and straightening C only changes coordinates to second order. The identity d(BH)=rho dH on Gamma preserves the displayed first-order form. Both line bundles are orientable because their multipliers are positive.

Write Euclidean volume as j dtheta dx dy. On Gamma its density j0 is constant: div B=d says j0'/j0+rho+sigma=d. Since WH=0, W=w partial_theta+v partial_y, and cylinder tangency says v(theta,x,0)=0. The degree n-1 divergence equation gives partial_y v_n=0, so v_n=0. The degree n tangential bracket equation then reads

    (partial_theta+rho x partial_x+sigma y partial_y)w_n=-kappa w_n.

Every monomial coefficient satisfies a scalar real constant-coefficient ODE in theta. Periodicity makes each surviving coefficient constant and requires m rho+l sigma=-kappa, m+l=n. Since rho!=sigma, at most one pair survives. Thus w_n=C0 x^m y^l with C0!=0.

Define the single-valued periodic function

    F(theta,x,y)=integral_0^y j(theta,x,s)w(theta,x,s) ds.

Exact divergence and v(theta,x,0)=0 give F_y=jw, F_theta=-jv, and WF=0. Uniform Taylor expansion yields

    F=j0 C0 x^m y^(l+1)/(l+1)+O((|x|+|y|)^(n+2)).

Fix x=epsilon>0. For epsilon/2<y<3epsilon/2, F_y has a fixed nonzero sign for sufficiently small epsilon, uniformly in theta. The level F=j0 C0 epsilon^(n+1)/(l+1) has opposite endpoint inequalities, so the implicit function theorem gives a unique periodic graph y=epsilon+O(epsilon^2). There w=C0 epsilon^n+O(epsilon^(n+1))!=0. The graph is a closed curve tangent to W and its period is the finite integral of dtheta/w over one circuit, with orientation chosen by the sign. This proves the claim at the stated finite regularity.

For analytic U, absence of every transverse coefficient makes all tangential derivatives of those coefficients zero as well. Smooth-coordinate chain rules then make every ambient derivative of W zero at a carrier point. Analyticity would imply W=0 nearby, contradicting the carrier closure. Thus analyticity forces a finite first term and the preceding contradiction applies. Smoothness alone gives infinite-order flatness, not analytic continuation.

## 6. Infinite-order flatness kills both invariant cylinders

Suppose U is smooth and no closed vortex is allowed. Section 5 makes |W(q)|<=C_N dist(q,Gamma)^N in a fixed tube for every positive integer N. Let L bound ||DB|| on a slightly larger compact tube. Along any orbit segment in it, the conorm of DPhi_t is at least exp(-L|t|). Cauchy therefore gives the safe lower bound

    |W(Phi_(+/-t)q)|>=exp(-(kappa+L)t)|W(q)|, t>=0.  (2)

On the local stable cylinder, dist(Phi_tq,Gamma)<=C exp(-alpha_s t) for some alpha_s>0. Choose N alpha_s>kappa+L. Compare (2) with the flatness bound C_N C^N exp(-N alpha_s t) and send t to infinity to obtain W(q)=0. On the unstable cylinder do exactly the same in backward time, with its positive backward decay rate alpha_u. Both cylinders are irrotational.

This repairs a direction omission in coordinator addition(5). For negative rho, its cited sigma cylinder is the unstable cylinder, already known to be irrotational. The forward stable-rho estimate above is needed to establish the second cylinder. For positive rho the sigma cylinder is stable. One fixed sufficiently large N suffices in each comparison; no uniform constant in N is needed.

## 7. Reduced countertest and remaining scope

On an abstract half cylinder r>0, take

    B0=partial_theta+rho r partial_r,
    W0=r^(-kappa/rho)F(theta-log(r)/rho) partial_theta,
    -kappa<rho<0,

with a smooth periodic F having zeros. The phase is B0-invariant, so [B0,W0]=-kappa W0. Since -kappa/rho>1, extension by zero through r=0 is C1 with W0=DW0=0 there. Every r-loop has zeros. This tests only the intrinsic bracket and loop-zero condition; it is not a divergence-free Euler realization in ambient space.

Vanishing on the two cylinders does not control points that enter and leave the tube. There is no construction, unique continuation statement or general C2 exclusion. Kelvin transport and the volume law hold for local Euler solutions while their trajectories stay in the domain; they do not by themselves prohibit a saddle. No claim identifies which global extension condition would necessarily fail for a hypothetical local germ.

## 8. Verification and model comparison

The complete actual external referee (a second model), its standalone proof, question and configured-model coordinator check CO29 were read. The arguments and all component cancellations above were reconstructed manually; no computation was needed. The inner the external referee (a second model) explicitly reports that its attempted model call failed to obtain credentials, so it is not counted as a successful review. The existing outer configured-model coordinator supplied the actual check, and the lower-cylinder repair was posted for continued exchange.
