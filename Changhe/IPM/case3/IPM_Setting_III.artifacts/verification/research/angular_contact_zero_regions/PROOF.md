# 168. Angular contact and open zero regions: independent audit

Written 2026-10-21 before the independent symbolic checker. This is a standalone audit of the external push2 argument, not a proof of profile existence or full nonexistence. All constructed fields below are explicitly non-profiles.

## Hypotheses, notation and dependencies

Let ell>1 and let rho be a smooth real function on the plane, even in x and odd in y, with a=rho_y(0) nonzero and sublinear density and gradient growth as in the primary class. The canonical stream function is odd in both coordinates, -Delta psi=rho_x, U=(-psi_y,psi_x)=J grad psi and U=o(r). Assume the exact profile equation W.grad rho=rho for W=ell X+U, except in examples explicitly labeled non-profiles. Put D=-y partial_x+x partial_y, v=D rho, q=rho/(a y), Q=Dq, and beta=U2/y, with smooth quotient extensions.

The already audited origin and flow results give psi_xy(0)=1-ell, DW(0)=diag(2ell-1,1), complete flow Phi_t, bounded backward orbits, div W=2ell, and no periodic orbit or polycycle. The exterior scattering result gives, for p=1/ell and every sufficiently large radius, r^(-p)rho(r,theta)=b_r(theta)Theta(H_r(theta)), where b_r>0 and H_r is a circle diffeomorphism. These are dependencies, not extra sign or topology assumptions. When explicitly invoked below, H-dyn means W has no equilibrium other than0; the audited source-basin result then gives q>0 off y=0.

We also use the following precise standard planar-flow theorems, as dependencies: a nonempty compact planar orbit limit set with no equilibrium is a periodic orbit; with finitely many equilibria, a bounded orbit limit set is an equilibrium, a periodic orbit or a graphic made of connections; a hyperbolic saddle has a one-dimensional unstable manifold. No unconditional finiteness or hyperbolicity of equilibria is asserted.

## 1. Angular equations and the missing sign

For R=JX, define C=[R,U]=D U-JU=(DU1+U2,DU2-U1). Expanding the two derivatives shows [D,U.grad]f=C.grad f for every scalar f. Also C=J grad(D psi). Since rotation commutes with dilation and the Laplacian, but [D,partial_x]=-partial_y,

    W.grad v=v-C.grad rho,
    -Delta(D psi)=partial_x v-partial_y rho.

In physical polar components C=(partial_theta Ur)e_r+(partial_theta Utheta)e_theta. Thus

    W.grad v=(1-partial_theta Utheta/r)v-(partial_theta Ur)rho_r.

Substituting rho=a y q yields W.grad q=Aq, where A=1-ell-beta. Applying D gives

    W.grad Q=AQ-q D beta-C.grad q
            =(A-partial_theta Utheta/r)Q-(partial_theta Ur)q_r-q D beta.

The identity v=a(xq+yQ) is the product rule. Smooth odd division justifies all quotients on y=0. These equations require the exact profile; a non-profile has the corresponding derivatives of its residual as extra terms. They do not sign the two displayed forcing terms.

On the backward basin B0 of the origin, W1=x(2ell-1+O(r^2)). Therefore for some lambda>1 every such orbit has |x(Phi_s X)|<=K exp(lambda s) as s tends to minus infinity. Both v and C.grad rho are smooth and odd in x, hence O(x) near0. Integrating the first angular equation and passing to the backward limit gives the absolutely convergent identity

    v(X)=-integral_-infinity^0 exp(-s)(C.grad rho)(Phi_s X) ds.

It does not supply the sign of v without signing that integral. On a bounded smooth domain G, integration by parts instead gives

    integral_G v C.grad rho=(ell+1)integral_G v^2
                    -1/2 integral_boundaryG v^2 W.n.

The two nonnegative terms on a sufficiently large circle occur with opposite signs. Sublinear density growth does not make the boundary term vanish. No full-plane integration by parts with a discarded boundary is being used.

For the center coefficients rho=a y+b x^2 y+d y^3+O(r^5), psi=(1-ell)xy+P x^3 y+Txy^3+O(r^6), Poisson and transport imply

    P+T=-b/3, 3aP+(4ell-2)b=0, aT+2d=0.

Elimination gives 6d=(a-4ell+2)b. If q=1+alpha x^2+gamma y^2+O(r^4), then 6gamma=(a-4ell+2)alpha and Q=(a-4ell-4)alpha xy/3+O(r^4). These are necessary identities; none prescribes the sign of alpha.

## 2. A canonical non-profile with forcing of both signs

Set ell=2, s=x^2+y^2, F(s)=(1-exp(-s))/s, F(0)=1, phi=yF(s), rho=-Delta phi=4y exp(-s), psi=phi_x=2xyh(s), where

    h(s)=F'(s)=-s^(-2) integral_0^s t exp(-t) dt.

Taylor series remove all singularities at0. Direct differentiation gives Delta(yF)=4y(sF''+2F') and sF''+2F'=-exp(-s), proving the Poisson coupling. Since psi=O(r^-2) and U=O(r^-3), this is the canonical inverse: a harmonic difference has sublinear gradient, harmonic derivative estimates make that gradient constant, and the two odd parities eliminate it. The density is Schwartz and satisfies every required growth bound.

Here a=4, psi_xy(0)=-1, q=exp(-s), Q=0, v=4x exp(-s), and

    U1=-2xh-4xy^2h', U2=2yh+4x^2yh'.

The integral formula gives -1/2<=h<=0. Hence W_r=r(2-2h cos2theta)>=r: the origin is the sole equilibrium and every backward orbit converges to it. Direct substitution into the angular forcing yields

    -q D beta-C.grad q=8xy exp(-s)(h'+2h).

This is negative near0 in the first quadrant since h(0)=-1/2 and h'(0)=1/3. At x=y=1/sqrt2 its value is -4/exp(2). At this same point -C.grad rho=(16x/exp(1))(-1+2/exp(1))<0, whereas near0 it is8x+O(xr^2)>0 for x>0.

This density is not a profile: at (0,1/sqrt2) its gradient vanishes but its value does not. Thus these examples refute signing the forcing using only canonical coupling, parities, growth, origin normalization, positivity and global-source geometry. They do not refute angular monotonicity for exact profiles, since the non-profile angular equations include residual derivatives.

## 3. First contact, including a zero-density contact

Assume an attained first radius r1 where u=v/a has an off-axis zero with x>0, and assume u>0 at all smaller positive radii on the open right half-circles. Reflect in y to choose0<theta1<pi/2. Continuity implies u>=0 on the right half-circle at r1. At X1,

    u=0, u_theta=0, u_theta,theta>=0, u_r<=0.

The last inequality is one-sided, not equality. Because v=0 the density gradient is radial, and the two exact equations give

    W_r rho_r=rho, W_r v_r=-(partial_theta Ur)rho_r.

Oddness gives rho(r1,theta)/a=integral_0^theta u(r1,alpha) d alpha>=0. If rho(X1) is nonzero, then it has the sign of a, and eliminating rho_r gives

    W_r^2 u_r=-(partial_theta Ur)rho/a.

Consequently partial_theta Ur>=0, with strict inequality when u_r<0. Also q>0 and Q=-(x/y)q<0 at this contact. These are compatibility conditions, not a contradiction. Under H-dyn this is the only possible density case.

If rho(X1)=0, the nonnegative integral implies rho=u=0 on the circle arc from theta0=0 to theta1. Inside that arc and for both small positive and negative times, a trajectory stays in the zero set by transport and stays in the first quadrant. It cannot enter r<r1, where rho/a>0. Its radial derivative must therefore be0, so W_r=0 on the whole open arc. Angular differentiation and endpoint continuity give W_r(X1)=partial_theta Ur(X1)=0. At the horizontal endpoint E=(r1,0), parity also gives W2=0; hence E is an equilibrium. This does not make a closed orbit.

This E cannot have a backward basin containing a neighborhood of E, even if degenerate. Reflect the invariant zero circle arc in y. In smooth local coordinates (d,y), d=r^2-r1^2, both coordinate axes are invariant and rho vanishes on both. Twice applying smooth division gives

    rho=y d h, W.grad d=d A1, W.grad y=y A2.

At E the derivative in these coordinates is diagonal and A1(E)+A2(E)=2ell. For any orbit converging backward to E choose1<kappa<2ell; eventually A1+A2>=kappa, so |yd|(Phi_-t X)<=K exp(-kappa t). The smooth h is bounded. Transport implies |rho(X)|<=C exp((1-kappa)t), hence rho(X)=0. A source basin containing a neighborhood would contradict rho/a>0 just inside the circle. If E is hyperbolic its positive trace therefore forces a saddle. The saddle or degenerate alternative remains open.

## 4. Canonical realization of the nonzero-density contact data

Near the closed unit disk prescribe

    rho_b=y exp(3s)(1-4s y^2/3+4y^4/5).

Then v_b=x exp(3s)(1-4x^2y^2). The inequality4x^2y^2<=r^4 proves positivity for x>0,r<1 and first off-axis contact at X1=(1/sqrt2,1/sqrt2). Direct differentiation gives

    rho_b(X1)=8 exp(3)/(15 sqrt2), rho_b,r(X1)=28 exp(3)/(15 sqrt2),
    v_b,r(X1)=-4 exp(3)/sqrt2, v_b,theta(X1)=0.

Both contact equations hold with W_r=2/7 and partial_theta Ur=30/49. These velocity data can be attained without changing rho near the disk. Extend rho_b by a smooth radial cutoff. Its logarithmic Newtonian potential phi_b solves -Delta phi_b=rho_b. Oddness gives zero total mass, so phi_b=O(r^-1) at infinity by expansion of the logarithm, and psi_b=partial_x phi_b gives a decaying canonical velocity.

For n=2,4,6 and a radial cutoff chi equal1 on a larger disk, add phi_n=k_n chi Im(x+iy)^(n+1)/(n+1). Define delta rho_n=-Delta phi_n and delta psi_n=partial_x phi_n. These preserve the parities, canonical coupling and the density near the disk. There delta psi_n=k_n r^n sin(n theta). Since Ur=-psi_theta/r, their changes to (psi_xy(0),W_r(X1),partial_theta Ur(X1)) are

    k2(2,0,4), k4(0,4,0), k6(0,0,-36).

This triangular matrix is invertible: choose k2 to set psi_xy(0)=-1, k4 to set W_r=2/7 and k6 to set the final angular derivative30/49. The field is nonzero with compactly supported density, so the audited nonzero far trace of exact profiles rules out its being a profile. It realizes only the stated pointwise contact data; no global-source or inner-disk profile equation is claimed.

## 5. Open zero regions and flat equilibria

Let Z={rho=0}, Omega=int Z. Transport and completeness make these sets invariant. Each connected component G of Omega is invariant, because an orbit is a continuous path in Omega. The flow Jacobian is exp(2ell t). For a ball E inside G, |G|>=exp(2ell t)|E| for all t>0. Thus each such component has infinite area and is unbounded.

An open zero arc of Theta gives, through the exterior scattering formula, an open zero arc on a sufficiently large circle. There W_r>0. The map (t,theta) -> Phi_t(r e_r(theta)) has nonsingular derivative on the arc, since W is transverse to the circle. It therefore sweeps out an open zero set. Conversely an unbounded component of Omega meets a large circle in an open arc, whose scattering image is an open zero arc of Theta. This proves equivalence between a nonempty open zero region and an open zero arc. Positive measure alone is not being substituted for nonempty interior.

Let Fflat={X:all derivatives of rho vanish at X}; this is closed. A point of Omega and its entire orbit lie in Fflat. Its nonempty compact backward limit set also lies in Fflat. If that set had no equilibrium, the equilibrium-free Poincare-Bendixson theorem would give a periodic orbit, already excluded. It therefore contains a flat equilibrium Xstar. Since rho_y(0)=a!=0, Xstar!=0. This argument does not assert convergence to a point or a finite equilibrium set.

At a flat equilibrium, rho_x=0, so psi_yy=-psi_xx and

    DW=[[ell-psi_xy,psi_xx],[psi_xx,ell+psi_xy]].

Its eigenvalues are ell+-sqrt(psi_xy^2+psi_xx^2). Thus it is a hyperbolic source, a saddle, or has eigenvalues0 and2ell. If it is a hyperbolic source, its symmetric positive definite derivative gives |Phi_-t X-Xstar|<=K exp(-mu t) for every orbit in its backward basin, once near Xstar. Flatness gives |rho(Xstar+z)|<=C_N |z|^N for every integer N. Choose N mu>1; transport then forces rho=0 on that entire basin.

Under the additional hypothesis that all equilibria are hyperbolic, the compact equilibrium set is finite, since otherwise accumulation would contradict isolation. The finite-equilibrium planar classification, absence of periodic orbits and polycycles, and hyperbolicity imply backward convergence to an equilibrium. Sources and saddles are the only possibilities since the trace is positive. A finite union of one-dimensional unstable saddle manifolds cannot cover Omega. Some point of Omega therefore converges backward to a source. It is flat, and its whole backward basin has zero density and lies in Omega. This conditional conclusion does not remove the hyperbolicity assumption.

## 6. Local harmonicity does not exclude a zero-density source

A second explicit non-profile uses potentials with disjoint cutoffs. At ell=2, set phi0=-y(x^2+y^2)/2 near0. Then rho=4y, psi=-xy and W=(3x,y), and the profile equation holds there. Near Xstar=(3,3), set phistar=6xy+3(y^2-x^2). This is harmonic and gives rho=0, psi=6y-6x, U=(-6,-6), W=2(X-Xstar). The profile equation also holds there. Cut off these potentials in disjoint disks and reflect the second one evenly in x and oddly in y, with the four reflected supports disjoint from each other and from0. The resulting global compactly supported phi has the required parity. Set rho=-Delta phi and psi=phi_x: all couplings are canonical and the local formulas are preserved.

The resulting density is nonzero and compactly supported, hence not an exact profile. It proves that a local harmonic zero-density neighborhood of a source is compatible with canonical coupling and with a separate normalized primary origin. It does not construct a whole zero-density basin; trajectories may cross a cutoff where rho is nonzero.

## 7. Scaling and audit verdict

The genuine dilation rho_lambda(X)=lambda rho(X/lambda), psi_lambda=lambda^2 psi(X/lambda), U_lambda=lambda U(X/lambda) gives W_lambda(X)=lambda W(X/lambda), unchanged ell,a and equilibrium eigenvalues, and Theta_lambda=lambda^(1-p)Theta. Thus flatness and zero arcs persist and basins dilate. A profile-dependent far-radius threshold is not invariant under this dilation.

CONFIRMED, subject to the explicit standard-flow dependencies: the exact angular equations, center relations, examples, attained-contact necessary conditions, zero-arc/open-region equivalence, existence of a nonorigin flat equilibrium, and the stated hyperbolic-source consequences. OPEN: global signs of v/(a x) or Q for exact profiles, exclusion of zero arcs or zero basins in the full class, and the principal endpoint. This audit supplies no new global existence or nonexistence conclusion.
