# Exact profile equations on an arbitrary prescribed disk

Written 2026-10-21T04:59:48.846655+00:00 before code. Status: CONFIRMED after independent exact, Cartesian and inverse controls 2026-10-21T05:03:32.829297+00:00; actual Opus167/168 returned no written audit. The construction was proposed in the lead lane's astra/bigdisk/PROOF.md, read in full. Its code has not been executed or imported. This packet also proves a new exterior exclusion. It does not decide existence of a full B2 profile.

## Statement

For every beta>2, a0>0 and radius R>0 there exist smooth full-plane fields Psi, Omega=-Delta Psi, Theta such that Psi and Omega are odd in x, Theta is even, Theta=0 on x=0, Omega>0 for x>0, Theta>0 off the axis, and the following hold. With U=(-Psi_y,Psi_x), V=U-U(0) and W=beta X+V, V is the canonical full-plane relative inverse, U=o(r), DU=O(r^(-1/beta)), and Omega has a smooth nonzero uniform leading tail r^(-1/beta) A(theta). Every backward W orbit tends to0. The temperature equation holds globally and Theta has a polynomial growth bound. Both profile PDEs hold exactly on B_R, with Theta=a0 x^2 and the required center strain and vorticity coefficient. The chosen fields do not solve both PDEs on the full plane.

The last assertion is stronger than the scope statement in the proposed construction. Every member, with its finite chosen anisotropy, agrees with a particular analytic relative velocity and vorticity outside a compact set. No C2 temperature can solve both PDEs on any nonempty open region for that prescribed analytic pair. This exclusion does not apply to arbitrary other exterior fields or to limits that lose exact exterior agreement.

## 1. Anisotropic base and exact normalization

Put

    q=4a0/beta, c=1+beta/2, lambda=(beta-2)/2,
    mu=1+3beta/2, p=(beta-1)/(2beta), d=6c/q,
    kappa=9c^2/(beta q^2).

Choose a finite L with L^2>=kappa and define

    eta=kappa/L^2, h=3c/(q eta), S0=(1+beta)L^2,
    S=L^2+x^2+eta(y-h)^2=S0+x^2-dy+eta y^2,
    B=q S0^(1-p)/(6p), Psi_L=-B x S^p,
    ell=Psi_L,x(0)=-q S0/(6p).

Here 0<eta<=1, eta h=d/2 and eta h^2=beta L^2. S>=L^2>0 everywhere. Cartesian differentiation gives

    Omega_L=2Bp x S^(p-2) [(3+eta)L^2+(1+2p+eta)x^2
                       +eta(3+(2p-1)eta)(y-h)^2].       (1)

All bracket coefficients are positive because 2p-1=-1/beta and eta<=1. Thus Omega_L/x>0. The center derivatives are

    Psi_L,xy(0)=c, Psi_L,xxx(0)=-q,
    Psi_L,xyy(0)=-2Bp eta S0^(p-2)[L^2+(2p-1)eta h^2]=0.

Parity excludes the other cubic terms, so the cubic Taylor polynomial is ell x+P0, where P0=cxy-qx^3/6. The center vorticity derivative is q. No vertical velocity is forced to zero in the ungauged representative: it is ell. It is subtracted in W exactly.

Let b_L(y)=W_L,2(0,y). Directly,

    W_L,1/x=beta+2Bp eta(y-h)S^(p-1),
    b_L'=beta-2Bp eta(y-h)[L^2+eta(y-h)^2]^(p-1).

For t>=0 the function t(L^2+t^2)^(p-1) attains its maximum at t=sqrt(beta)L: its derivative has sign L^2+(2p-1)t^2. Adding x^2 only decreases the relevant absolute value because p-1<0. The maximum with prefactor 2Bp sqrt(eta) is c. Consequently

    W_L,1/x>=lambda, b_L'>=lambda.                    (2)

These two lower bounds are uniform in L. No uniform bound on every other field norm or tail constant as L increases is asserted.

## 2. Convergence to the cubic in a quantitative C3 norm

For a fixed M>0 let ||f|| be the sum over i+j<=3 of the sup norm of partial_x^i partial_y^j f on B_M divided by i!j!. Leibniz's rule makes this norm submultiplicative. Set H=M+1, C0=2+d, T=x^2-dy+eta y^2, z=T/S0. Since eta<=1,

    ||x||<=H, ||T||<=C0 H^2, ||z||<=C0 H^2/[(1+beta)L^2].

When the last quantity is <=1/2, the convergent binomial series for (1+u z)^(p-1), 0<=u<=1, converges also in this norm. Its coefficient magnitudes are at most1 because 0<1-p<1. Put J=int_0^1 (1+u z)^(p-1)du. Then ||J-1||<=2||z||. The fundamental theorem of calculus gives the exact identity

    Psi_L-ell x=-(q/6)x T J.

Therefore E_L=Psi_L-ell x-P0 equals -(q/6)x[eta y^2+T(J-1)], and

    ||E_L||<=D_M/L^2,
    D_M=(q/6)[kappa H^3+2C0^2 H^5/(1+beta)].          (3)

This is a bound on all derivatives through order3, not just a pointwise expansion. It requires L^2>=2C0 H^2/(1+beta). In particular the very large linear stream term ell x causes no error in the relative field after subtraction. No spatial scaling changes a0 here.

## 3. Compact replacement and positivity

Let chi be any smooth radial function equal1 on B1, zero outside B2, and between0 and1. Let Cchi be its global norm defined as above. Such a function exists by the elementary smooth bump construction, and Cchi is finite. Choose

    Delta=mu-2lambda=3+beta/2, k=q/(2Delta),
    D=1+2R+kR^2, M=2D.

Select L so that

    L^2 > max(kappa, 2C0(M+1)^2/(1+beta),
              16(1+Cchi)D_M/q, 2Cchi D_M/lambda).     (4)

All right-hand quantities are fixed before choosing L. Define delta=-chi(X/D)E_L and Psi=Psi_L+delta. Since D>=1, scaled-cutoff derivatives have norm at most Cchi. The stream is ell x+P0 on B_D and Psi_L outside B_(2D). Its center derivative and hence center velocity remain unchanged, since E_L has zero Taylor jet through degree3.

On B_M the difference F=Psi-ell x-P0 is odd in x and obeys ||F||<q/16. Delta F is also odd; the horizontal segment from (0,y) to (x,y) stays in B_M. The mean value theorem gives

    |Delta F/x|<=||F_xxx||_infty+||F_xyy||_infty<=8||F||.

The loose factor8 follows from 3!+1!2! with the specified norm. Thus Omega/x=q-Delta F/x>q/2 there. Outside B_M positivity follows from (1). There is no missing annulus sign assumption.

Similarly ||delta||<=Cchi D_M/L^2<lambda/2. Oddness gives |delta_y/x|<=||delta_xy||<lambda/2. The changes to W1/x and b' are -delta_y/x and delta_xy(0,y). Hence the final field has

    W1/x>=lambda/2, b'>=lambda/2.                   (5)

All quotients extend smoothly to x=0 by parity.

## 4. Full-plane inverse, basin and temperature

For fixed positive eta, let H_eta=cos^2(theta)+eta sin^2(theta)>=eta. Expanding (1) at infinity gives uniformly in angle

    Omega_L=r^(-1/beta)[A(theta)+O(r^-1)],
    A=2Bp cos(theta) H_eta^(p-2)[(1+2p+eta)cos^2(theta)
                              +eta(3+(2p-1)eta)sin^2(theta)].

A is smooth, positive in the open right semicircle and nonzero. Differentiation gives U_L=O(r^(1-1/beta)), DU_L=O(r^(-1/beta)). The compact stream correction preserves these estimates. The constants may depend strongly on L and eta. The subtracted full-plane Biot-Savart integral converges for this vorticity decay; its difference from V is an entire harmonic vector field of sublinear growth, hence a constant by the growing-ball gradient estimate. Both relative fields vanish at0, so the constant is0. This establishes the canonical relative inverse, without a wall, an added strain, or an independent fitted drift.

DU is bounded globally. With gamma=lambda/2, (5) implies for backward time t>=0

    |x(-t)|<=|x0|e^(-gamma t),
    D^+|y(-t)|<=-gamma|y(-t)|+C|x0|e^(-gamma t).

Here |W2(x,y)-b(y)|<=C|x| follows from bounded Psi_xx, and b(0)=0. Integrating gives |y(-t)|<=e^(-gamma t)(|y0|+C|x0|t). The globally Lipschitz flow is complete and all its backward orbits tend to0.

On a small ball B_rho inside B_D, with rho<lambda/q, W is the polynomial

    W_P=(lambda x,mu y-qx^2/2).

Its radial component is positive on each punctured small ball, so B_rho is backward invariant. Put xi=x there. For general X choose a sufficiently large t with phi_-t(X) in B_rho and set xi(X)=e^(lambda t)(phi_-t(X))_1. This is independent of the entry time because W_P,1=lambda x within that ball. A fixed sufficiently large t works for a neighborhood of any given X, proving smoothness without an infinite differentiated integral. Reflection and flow uniqueness imply xi odd in x and zero exactly on the axis. Its flow relation gives W.grad xi=lambda xi.

Thus Theta=a0xi^2 is smooth, strictly positive off-axis and solves the temperature equation globally. At large r, sublinearity gives d(log r)/dt<=-beta/2 in backward time until entry into a fixed ball. Entry occurs within (2/beta)log(r/R0), so |Theta|<=C(1+r)^[2(beta-2)/beta]. This loose polynomial bound suffices for the declared class. It is not a finite-temperature-norm or bounded-data blow-up assertion.

## 5. Exactness on B_R

The polynomial backward trajectory from X0 is

    x(t)=e^(-lambda t)x0,
    y(t)=e^(-mu t)y0+k x0^2(e^(-2lambda t)-e^(-mu t)).

Direct differentiation gives x'=-lambda x, y'=-mu y+q x^2/2. For X0 in B_R and all t>=0,

    |(x(t),y(t))|<=|x0|+|y0|+k x0^2<2R+kR^2<D.

Therefore this entire curve is the actual backward orbit, by uniqueness. The definition of xi gives xi(X0)=x0. On B_R one has Theta=a0x^2, Omega=qx and W=W_P. The temperature residual is [2lambda-(beta-2)]a0x^2=0, and the vorticity residual is [(lambda+1)q-2a0]x=0. This proves all construction claims.

Any bounded prescribed set is contained in a disk. Negative a0 may be obtained by the exact B2 transformation Psi_tilde(x,y)=-Psi(x,-y), Omega_tilde(x,y)=-Omega(x,-y), Theta_tilde(x,y)=-Theta(x,-y); the new relative transport is (W1(x,-y),-W2(x,-y)). This changes the sign of a0 and Omega on the right half-plane, while preserving the disk and all other equations. The positive-vorticity statement itself is for a0>0.

## 6. These finite-L fields still fail on their exterior

The local elimination identity of packet124 is restated to specify exactly what is used. For any smooth prescribed W,Omega and k0=beta-2 put

    F=W.grad Omega+Omega, J=W2_x,
    D0=(k0-W1_x)F-W.grad F, Z=W1 F J+W2 D0,
    E=J Z_y-Z J_y-k0 D0 J.

If a C2 temperature satisfies both equations then differentiating its transport equation in x gives J Theta_y=D0, and multiplying the original equation by J gives k0 J Theta=Z. Differentiating in y and eliminating Theta_y gives E=0, without division. For Psi_L all functions in E are analytic on the connected plane because S>0.

Write q_L(y)=Omega_L,x(0,y), b=W_L,2(0,y), C(y)=Psi_L,xxx(0,y). From the cubic center data, b(0)=b''(0)=0, b'(0)=mu, C(0)=-q and q_L(0)=q. The general parity calculation in packet124, which uses only these data, gives

    [x^2 y]E=q(2beta+4)mu(2beta+1)q_L'(0).           (6)

It follows also by setting H=bq_L'+(2beta+1-b')q_L and G=bH'-(2b'-3beta-2)H, then noting [x^2]E=-C(bG)'+bG C'+k0CG. At0, G=0 and G'=mu(2beta+1)q_L'(0).

Differentiate (1) on the axis. Its bracket at0 is 3S0, its y derivative is -d(3-eta/beta), and S_y(0)=-d. Using 2Bp S0^(p-1)=q/3 gives

    q_L'(0)=q d[3(1-p)+eta/beta]/(3S0)
            =c[3(beta+1)+2eta]/[beta(beta+1)L^2]>0.

Every factor in (6) is positive. E cannot vanish identically and hence cannot vanish on any nonempty open set by analytic continuation. No C2 temperature solves both equations for this prescribed analytic pair on an open set. The compact correction has zero gradient at0, so outside B_(2D) its relative velocity and vorticity agree exactly with the base. A hypothetical global B2 solution would contradict this open-set exclusion. The constructed fields are therefore nonprofiles. The argument does not exclude a limit with L tending to infinity: the nonzero coefficient tends to0 and the tail class is not uniformly controlled in that limit.

## Dependencies and limits

The proof uses only Cartesian differentiation, a smooth cutoff, an elementary complete-flow argument, the canonical-inverse uniqueness for the stated slow tail, and the real analytic identity theorem. The mean-value, C3 norm and polynomial trajectory bounds have all been spelled out. Packet124 supplies a previously audited algebraic identity; it is rederived above. No lead or NUM code is a dependency. The proposed exterior three-mode route is not needed.

A further combination with packet123, giving all residual jets zero on the entire axis while retaining the prescribed disk, is plausible because the new reference is polynomial near the central axis interval and has the same positive algebraic axis tails. That combined claim is not part of the present theorem until its uniform strip estimates and preservation of the polynomial backward trajectories are checked separately. No full YES or NO follows from this packet.
