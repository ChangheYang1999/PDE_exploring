# An analytic local Euler circle with swirl and no closed vortex orbit in its tube

Status: independent reconstruction of LIT93, checked against the focused configured-model challenge. Final verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md). The local analytic existence assertion is distinct from any global extension. The construction has nonzero helicity.

## 1. Exact theorem and purpose

Fix 0<c<1/2, omega!=0, R>0 and nonzero real constants K,C. Put kappa=1+c, d=3c, a=1-2c and sigma=d/kappa, so 0<sigma<1. There is a real analytic axisymmetric velocity U and single-valued analytic pressure P on a full tube about the circle r=R,z=0, solving incompressibility and every component of the rotating Euler profile equation.

The circle is a carrier orbit of least period2pi/|omega| and backward exponents (kappa,0,-d-kappa). On it W=0, DW has rank1 and image R B, and D(B cross W)=0. The zero set of W in the tube is exactly r=R. Off that cylinder its radial component has the strict sign of K. Thus the tube contains no nonconstant closed vortex orbit.

This refutes an inference from that local nonflat spectrum alone to nearby closed vortex circles. It does not refute such an inference with additional global zero-helicity hypotheses. Here helicity is nonzero, and neither a global extension nor decay is established.

## 2. Convergent regular-singular existence, with its proof

The following elementary analytic lemma is used. If F(x,Y) is holomorphic near (0,Y0), F(0,Y0)=0, and no eigenvalue of A=D_YF(0,Y0) is a positive integer, then xY'=F(x,Y), Y(0)=Y0 has a unique holomorphic germ. Real data give a real germ.

Translate Y0 to zero and write F=AY+R. On zero-constant power series let LZ=xZ'-AZ. Its coefficientwise inverse is

    (L^(-1)V)_m=(mI-A)^(-1)V_m, m>=1.

All matrices are invertible and their norms are uniformly bounded by M, since their norms are O(1/m) for large m. Equip zero-constant series with the complete norm sum_m |Z_m|rho^m, choosing a finite-dimensional norm compatible with an absolute coefficient majorant. The power-series product is bounded in this norm. Holomorphic composition is defined by its absolutely convergent coefficient series on a small ball.

Since R(0,0)=0 and D_YR(0,0)=0, a fixed convergent coefficient majorant gives constants C0,C1 for all sufficiently small rho such that

    ||R(x,0)||<=C0 rho,
    ||R(x,Z)-R(x,V)||
       <=C1(rho+||Z||+||V||)||Z-V||.

Choose C0,C1 positive, enlarging them if necessary, and a polydisk radius delta where these estimates hold for rho,||Z||,||V||<=delta/2. On the closed ball ||Z||<=2MC0 rho the map L^(-1)R has Lipschitz constant at most MC1(1+4MC0)rho. Choose

    rho<=min(delta/[2max(1,2MC0)],
             1/[2MC1(1+4MC0)]).

Its Lipschitz constant is at most1/2, and its value at zero has norm at most MC0 rho, so it maps the ball into itself. Its fixed point converges on |x|<rho and solves the equation coefficientwise and therefore pointwise on the open disk. Recursion with mI-A determines every coefficient, so any other analytic germ is identical. Complex conjugation gives the real assertion. This argument proves convergence, not just formal solvability.

The actual Rong arXiv1307.3823v1 pages1-2 were read. Proposition2.1 on page2 states this same nonresonant result and refers its proof to another work. That book was not obtained or used. The proof above is independent and no positive-integer resonant case is invoked.

## 3. Analytic radial functions

Solve for psi,l,b,Z,J as functions of real x near0:

    x psi'=x l,
    x l'=x^5 b l,
    x b'=-5b-lZ/(2kappa),
    x Z'=(sigma-2+x^5b)Z-K^2 kappa l^2/(2psi^2),
    x J'=-(sigma+3+2x^5b-xl/(2psi))J-(C/kappa)sqrt(psi).

The square root is the analytic branch positive at psi=R^2. Prescribe

    psi0=R^2, l0=2R,
    Z0=2K^2 kappa/[R^2(sigma-2)],
    b0=-RZ0/(5kappa), J0=-CR/[kappa(sigma+3)].

Each right side vanishes at the prescribed initial point. In the variable order psi,l,Z,b,J the Jacobian at x=0 is lower triangular with diagonal0,0,sigma-2,-5,-sigma-3. The analytic lemma applies. Its constants and a positive admissible radius can be chosen uniformly on compact sets of the parameters c,R,K,C with 0<c<1/2 and R>0. The radial system is independent of omega. No uniform radius as R tends to zero or the parameters become unbounded is asserted. Shrink the interval until psi,l>0. Then r=sqrt(psi) satisfies r_x=l/(2r), r(0)=R,r_x(0)=1, so it has an analytic inverse x(r).

Define

    w=x^5b, A=-kappa xl/(2r),
    D=2c+kappa(1+w), beta=c+D,
    v=-K kappa x^2l/2, j=xJ,
    h(0)=0, h_x=xJl/(2r), G=beta h-Aj.

In radial coordinates h_r=j. Direct differentiation gives

    A partial_r=-kappa x partial_x,
    A_r+A/r=-kappa(1+w), D=2c-A_r-A/r,
    D_r=-r x^4Z.

For the last equation w_x=5x^4b+x^5b_x=-l x^4Z/(2kappa), then use r_x=l/(2r). Let q1=x^4Z and q0=Cx. The radial system gives

    A(q1)_r+(beta+kappa)q1=2v^2/r^4,
    A(q0)_r=-kappa q0,
    A v_r+(beta+a)v=0,
    A j_r+(A_r-beta)j=r Cx,
    D_r h-G_r=r q0.                                      (1)

To check the first formula, its left side is kappa x^4[(sigma-2+w)Z-xZ'], hence K^2 kappa^2x^4l^2/(2psi^2). The third follows from v=K r A x and the first two identities for A. For the fourth,

    -(A_r-beta)/kappa=sigma+2+2w-xl/(2psi),

and substitution j=xJ gives precisely the J equation. The last follows by differentiating G=beta h-Aj. Any intermediate division by x was only off x=0; both sides of all displayed identities are analytic and extend to x=0.

## 4. Actual velocity, curl and full momentum

Write zeta=z+h(r), F=A-cr and set

    U_r=F, U_theta=v zeta/r, U_z=Dz+G.

These are single-valued analytic Cartesian fields on the full tube away from the axis. Their divergence is F_r+F/r+D=0. Direct cylindrical curl gives

    W_r=-v/r,
    W_theta=r(q1 zeta+q0),
    W_z=(v_r zeta+v h_r)/r.

In particular these are derivatives of the actual velocity, not independent transported variables. Let M=r U_theta=v zeta and q=W_theta/r. Because G=beta h-Ah_r, the carrier acts on axisymmetric scalars by Bzeta=beta zeta and Bx=-kappa x. Equations(1) imply

    BM=-aM, Bq=-kappa q+r^(-4)partial_z(M^2).               (2)

The last term is the nonzero swirl forcing and cannot be dropped.

Cartesian axisymmetry gives (Jy).grad U=JU, including differentiation of the cylindrical basis, so the rotation terms cancel for any omega. Set X=cy+U and N=(1-c)U+(X.grad)U. Cylindrical acceleration gives

    rN_theta=BM+aM=0.

Also curl N=W+(X.grad)W-(W.grad)U. Its theta component is

    W_theta+A(W_theta)_r+B_z(W_theta)_z-F W_theta/r
       +W_r(U_theta/r-(U_theta)_r)-W_z(U_theta)_z.

The first line equals r(Bq+kappa q); using W_r=-M_z/r and W_z=M_r/r, the second equals -2MM_z/r^3. Thus (2) makes this component zero. All other curl components vanish because N is axisymmetric with N_theta=0.

The meridional tube is a simply connected rectangle in (r,z), even though the full three-dimensional tube is not simply connected. The single possible period of the closed form -N.dy is -2pi r N_theta. Curl-free axisymmetry alone would allow N_theta to be a nonzero constant divided by r. Here BM+aM=0 makes N_theta exactly zero, removing that period. The explicit formula

    P(r,z)=-integral_R^r N_r(s,0)ds-integral_0^z N_z(r,t)dt

has P_z=-N_z and P_r=-N_r, using partial_r N_z=partial_z N_r. It is analytic and single valued on the full tube. This verifies every momentum component, not just curl N=0 in a multiply connected domain.

## 5. Circle, derivative cocycle and vortex geometry

At x=0, A=v=h=G=j=0, D=2c+kappa and beta=d+kappa. Moreover A_r=-kappa and D_r=G_r=v_r=0. The carrier circle therefore has theta'=-omega and transverse linear equations delta r'=-kappa delta r, delta z'=(d+kappa)delta z; linear angular displacement has rate0. The periodic cylindrical frame and its inverse remain bounded, giving backward exponents (kappa,0,-d-kappa). The normalized time measure is whole-flow ergodic with time-one entropy0; no time-one ergodicity is needed.

At a point of the circle,

    DW(e_r)=CR e_theta, DW(e_theta)=DW(e_z)=0.

Hence rank DW=1 and image DW=R B, and B cross DW=0 gives D(B cross W)=0. These are full Cartesian first-jet statements because W itself vanishes there. Also g=U.B=0 and grad g=c kappa R e_r=-kappa U on the circle, so the negative covector orientation is realized.

On the whole cylinder x=0 all three components of W vanish for every z. At x!=0,

    W_r=K kappa x^2l/(2r)

has the strict sign of K. A nonconstant vortex orbit cannot meet a zero of the smooth vortex field by uniqueness. Away from the zero cylinder its radial coordinate is strictly monotone as long as it stays in the tube, so it cannot be a closed orbit inside that tube. This concerns frozen vorticity, not the different carrier field.

## 6. Helicity and second-jet comparison

On z=0 the leading terms are

    U_r=-cR+O(x), W_r=K kappa x^2+O(x^3),
    U_theta=O(x^4), W_theta=CRx+O(x^2),
    U_z=O(x^2), W_z=O(x^3).

Consequently U.W=-cR K kappa x^2+O(x^3), nonzero near the circle. This supplies a concrete failure of the global zero-helicity hypothesis and does not state a sign on an essential basin.

The radial equations give l=2R+O(x^5), psi=R^2+2Rx+O(x^6). With delta=r-R,

    A=-kappa(r^2-R^2)/(2r)+O(delta^6),
    D=2c+kappa+O(delta^5),
    G=-C(r^2-R^2)^2/(8R)+O(delta^7).

The last follows by integrating G_r=D_rh-rCx. The added swirl U_theta has transverse total degree at least3. Therefore the velocity second jet agrees along the circle with the A440 k1 family after its coefficient is changed to C/(2R). Nevertheless their frozen-vortex geometry differs. A velocity second jet alone does not encode the existence of a nearby closed vortex circle. By A442, this shared second jet fails the global helicity-free rank identity with transverse mismatch 3(2c+kappa)^2>0. Thus even that second jet cannot occur on such a circle in a global helicity-free uniformly sublinear profile; no local or global sign-changing profile is excluded by this observation.

## 7. Verification and limits

The complete analytic and algebraic argument preceded the reproduction. The submitted checker was read in full; its thirteen rational identities and deleted-swirl negative control test local coordinate algebra only. The reproduction ran from 2026-11-03T03:29:09.766786Z to 03:29:11.216321Z on one permitted CPU worker. All thirteen rational identities and the deleted-swirl negative control passed; actual times, script hash and output are in the team records and in the team records. The proof of convergence, positivity of r,l, global single-valued pressure on the tube and the monotone-radius argument are the hand arguments above.

No continuation to the axis or infinity, decay, uniformly sublinear growth or global completeness away from the circle is claimed. The local construction does not evade a global helicity-free rank filter, since its helicity already fails that premise. The main conjecture and the unrestricted componentwise growth question remain open.
