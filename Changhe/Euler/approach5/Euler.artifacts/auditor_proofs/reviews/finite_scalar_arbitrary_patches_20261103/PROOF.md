# Finite scalar order across arbitrary irrotational patches

Status: independent proof of LIT223 at the exact local scope below. Its harmonic extension and its one-sector boundary argument are checked separately. No scalar-flat continuation theorem is asserted.

## 1. Exact local theorem

Fix 2/5<c<1/2, omega in R, Jx=(-x2,x1,0), A=cI-omega J, X=Ax, a=1-2c, b=2(1-c), p=(1-c)/c, q=b/a and eta=1/q. Let x0!=0. On a short flow tube about x0, assume smooth real V,P2 with

    div V=0, W=curl V, S=P2-|V|2/2, k=X.V,
    V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    P2(exp(tA)x)=exp(-bt)P2(x),
    -Delta P2=tr((DV)^2), W.grad S=0,
    grad k cross grad S=0 wherever W!=0.

Homogeneity is imposed whenever both points and the relevant short flow segment are in the tube. Suppose all derivatives of V vanish at x0, S(x0)=0, and S has a first nonzero Taylor term of finite order. Then V=0 near x0. In particular such a point cannot belong to supp W.

These are local differential and homogeneity hypotheses, not consequences of mere decay for a general C2 profile. The actual HF/natural tails under discussion satisfy them when they are smooth on the stated neighborhood. No density or boundary regularity of the vorticity patches is assumed.

## 2. Scalar sectors and a strict Laplacian sign

Choose a transverse spherical chart z centered on the flow ray of x0. A fixed positive coordinate dilation first puts its base point on S2; composing V and P2 with that dilation preserves all local identities, so no flow outside the original tube is required. The coordinates (t,z) map to exp(tA)w(z); transversality follows from w.Aw=c>0. On a smaller compact flow interval, homogeneity and smooth flatness imply, for every N and every fixed derivative order,

    |D^j V|+|D^j W|+|D^j k|<=C_(N,j)|z|^N,
    |Delta S|<=C_N|z|^N.

The last assertion follows from the pressure equation and Delta S=-tr((DV)^2)-|DV|2-V.Delta V. Also S(t,z)=exp(-bt)h(z). The first term H_l of h, of integer degree l>=1, is harmonic for the frozen transverse scalar principal matrix. To see this explicitly, in twisted polar coordinates r partial_r acts on S as -2p+(omega/c)(Jw).grad_S. Thus the principal tensor is D0=I+(omega/c)^2(Jw) tensor (Jw). All other terms have lower differential order and do not enter the first nonzero Taylor equation. A fixed linear chart makes H_l an ordinary nonzero harmonic polynomial.

Write H_l=r^l(A_l cos(l theta)+B_l sin(l theta)), with A_l^2+B_l^2>0. Its angular roots are simple and its gradient has magnitude l sqrt(A_l^2+B_l^2)r^(l-1). Taylor expansion gives exactly2l smooth nodal arcs and finitely many connected open scalar sectors in a small punctured disk. It also gives, uniformly in the flow interval,

    |S|<=C|z|^l, |grad S|>=c1|z|^(l-1).

Put g=|S|^eta on any sector tube D. Since 0<eta<1,

    Q=Delta g/g
      =eta [S Delta S-(1-eta)|grad S|2]/S2<0

throughout D after one common shrink. Indeed the first numerator term is O(|z|^(N+l)) for arbitrary N and the negative term is bounded below in magnitude by a positive multiple of |z|^(2l-2). This comparison does not divide by a lower bound for S, so it remains valid arbitrarily close to a nodal side.

## 3. Rank identity and harmonic zero extension

Vector differentiation and homogeneity give

    grad k=X cross W-aV, X.grad k=-ak, X.grad S=-bS.

Contracting grad k cross grad S=0 with X gives k grad S=q S grad k on {W!=0}. Therefore f=k/g has grad f=0 on that open set. Every positive-order derivative of f vanishes on its closure.

Let O=int_D{W=0}. Its complement is the closure in D of {W!=0}. On that complement the product rule gives Delta k=Qk. On O,

    Delta k=X.Delta V-2omega W3=0,

because div V=0 and Delta V=-curl W. The displayed formula follows by differentiating X.V twice; the skew part contributes -2omega W3. By continuity Delta k=0 also on the relative boundary of O. Since Q<0 there and S!=0, k=0 on that boundary. The same is true of every derivative: f=0 there and every positive-order derivative of f already vanishes there; multiply by the smooth nonzero g.

Define K=k on O and K=0 on D minus O. This is a C2 harmonic function on D. For detail, at a boundary point all derivatives of k through order2 vanish. Taylor's formula for k and its first derivatives shows that the piecewise candidate is twice differentiable there with zero derivatives. The interior second derivatives approach zero by their continuity, so the piecewise second derivatives are continuous. Its Laplacian is zero on both open sides and then at their boundary. No regularity of that boundary or count of its components is required.

If D contains vorticity, K vanishes on a nonempty open subset of the connected three-dimensional domain D. A classical harmonic function is analytic on each interior ball, as follows from the convergent Poisson-kernel expansion. Overlapping balls along paths propagate its zero Taylor series. Hence K=0 on D, so k=0 on O. It follows that grad f=0 everywhere in D. If O is nonempty, f=0 there makes its global constant zero. If O is empty, flat k on any fixed interior ray and g comparable to r^(l eta) force the same constant to be zero.

Thus every scalar sector is either entirely irrotational or has k=0 on its whole tube. The second type need not have vorticity near the vertex. The final finite-sector assembly will handle that fact explicitly.

## 4. The first-order system on one k-zero sector

Set tau=omega/c, zeta=Jw, v=w.V, Y=V-vw, rho=w.W/c, R_w h=w cross h and F=W-rho Aw. On a k-zero sector the exact angular identities are

    v=tau zeta.Y, F=-(a/c)R_wY,
    div_S F=a rho, F.grad_S h=b rho h,
    div_S(D0Y)+(2-p)tau zeta.Y=0,
    D0=I+tau2 zeta tensor zeta.

These follow by inserting the homogeneous radial derivatives into div V=div W=0 and W.grad S=0 and by taking w cross in X cross W=aV. In particular the coefficient (p-1)c equals a. Let K=adj D0 and b1=-(2-p)tau R_w zeta. The identity D0R_w=R_w adj D0 gives

    h div_S F-eta F.grad_S h=0, curl_S(KF)=b1.F.

In a chart with metric G and area density sqrt(g), let Fhat=sqrt(g)F_components and Khat=G K/sqrt(g). The system becomes

    h div Fhat-eta Fhat.grad h=0,
    curl(Khat Fhat)=bhat.Fhat.

Its coefficients are smooth, Khat is symmetric positive definite, and adj Khat=sqrt(g)D0G^(-1), the same density principal matrix as the scalar equation. Its frozen form therefore annihilates D2H_l. Fhat is smooth through the sides and flat at the vertex as a field, although this system has only been established inside the chosen sector.

## 5. A stream on one sector, with zero Dirichlet traces

The sector is simply connected and div(|h|^(-eta)Fhat)=0 there. Thus there is a single-valued u with

    grad u=R |h|^(-eta)Fhat,
    Fhat=-|h|^eta R grad u,

where R(x,y)=(-y,x). At a regular side the undivided first equation extends by continuity and gives Fhat.grad h=0. Smoothness makes its normal component O(d), with d the distance to that side on a compact punctured annulus. Therefore u has normal derivative O(d^(-eta)) and side-tangential derivative O(d^(1-eta)). Since eta<1, u has a continuous constant trace on each side.

In nodal coordinates, the oscillation of u on a radius-r arc is at most

    C_N r^(N+1-l eta) integral_sector |H_l(1,theta)|^(-eta) dtheta.

The angular integral is finite. Radial integration on a fixed interior direction gives a finite limit at the vertex and an arbitrary power error. The arc estimate makes both side constants equal to that limit. Subtract it. Then u has zero Dirichlet trace on both sides and is uniformly flat in value at the vertex. Moreover

    u=O(d^(1-eta)), grad u=O(d^(-eta)),
    side-tangential derivative u=O(d^(1-eta)).

The energy |h|^eta|grad u|2=|h|^(-eta)|Fhat|2 is integrable at the sides and vertex. The second first-order equation gives, with A1=adj Khat and beta=R bhat,

    div(|h|^eta A1 grad u)+|h|^eta beta.grad u=0.

This uses KR=R adj K and curl(RG)=div G, and fixes the drift sign. No zero Neumann flux of u, no whole-disk period and no equation in adjacent sectors have been imposed.

## 6. Nodal coordinates and each separate boundary term

Normalize A1(0)=I. The explicit A-normal coordinate map proved in A1244 is available on the two smooth sides. If gamma_j is outward arclength on a side, e_j its initial tangent, n_j=R gamma_j', and chi_j are disjoint angular cutoffs equal to1 near the side directions, it is

    Phi(r e(theta))=r e(theta)+sum_j chi_j(theta)
      [gamma_j(r)-r e_j
       +r(theta-theta_j)(A1(gamma_j(r))n_j(r)-R e_j)].

Taylor expansion gives Phi-id=O(r2), D Phi-I=O(r), bounded second derivatives and h composed Phi=H_l g0 with g0=1+O(r)>0 and bounded gradient. On each ray Phi_r=gamma_j' and Phi_theta=r A1 n_j. Thus the transformed equation is

    div(w M grad u)+w beta1.grad u=0, w=|H_l|^eta,
    M=g0^eta det(D Phi)(D Phi)^(-1)A1(Phi)(D Phi)^(-T),

with bounded beta1, symmetric elliptic Lipschitz M=I+O(r), and the exact condition tau.Mnu=0 on both rays. Here nu=x/r and tau=Rnu. This orthogonality follows because the new angular gradient is proportional to n_j and the new radial gradient annihilates A1 n_j.

Write D=integral w grad u.M grad u, J=integral w u beta1.grad u and I=D-J over the sector ball. Angular Dirichlet Poincare follows by integrating u_theta from a side and applying Cauchy-Schwarz with the integrable reciprocal angular weight. Radial integration then gives integral w u2<=Cr2D and |J|<=CrD. For small r, D/2<=I<=3D/2. Integration by parts gives

    I=integral_arc w u nu.M grad u.

Each separate side term vanishes: u=O(d^(1-eta)) and its weighted conormal derivative is bounded. The inner-circle term vanishes by flatness.

For the Rellich calculation put mu=nu.Mnu, T=Mnu-mu nu and Z=Mx/mu. Then T=O(r times angular distance to a side), Z=x+O(r2), DZ=I+O(r), Z.nu=r. The weighted logarithmic poles are multiplied by these vanishing factors, giving div(wZ)=(2+l eta+O(r))w and |div_arc(wT)|<=Cw. The first Rellich side flux is w(grad u.Mgrad u)Z.n_side=O(d^(1-eta)); the second is w(Z.grad u)(Mgrad u).n_side=O(d^(1-eta)). For the latter, the radial derivative of u is side-tangential and O(d^(1-eta)); the normal part of Z is O(d). Every side flux therefore vanishes separately. No cancellation across a neighboring sector is needed. The drift gives at most CrD in the volume identity. Flatness removes all vertex terms.

## 7. Frequency with drift

On the sector arc define

    H=integral w mu u2, B=integral w(nu.Mgrad u)^2/mu.

The preceding derivative and Rellich computations give, for almost every r,

    H'=(1+l eta)H/r+2I+O(H),
    D'=l eta D/r+2B+O(D), |J'|<=C sqrt(H D').

The last estimate is surface Cauchy-Schwarz; D' is the nonnegative surface energy. If H vanishes at a small radius, the energy boundary identity gives I=D=0 inside, hence Fhat=0 there. Otherwise define N=rI/H and Q0=B/H-I2/H2>=0. Differentiating, with the drift retained, gives

    N'=2rQ0+l eta J/H-rJ'/H+O(N).

Since |J|/H<=CN and D'/H<=CN/r2+2B/H,

    r|J'|/H<=C sqrt(N)+Cr sqrt(Q0)+CN.

Absorb Cr sqrt(Q0) into rQ0+Cr and use sqrt(N)<=N+1. It follows that N'>=-C(N+1). Thus N is bounded as r decreases to0. The equation for H' gives a finite polynomial lower bound H(r)>=C0 r^L. Uniform flatness of u gives an upper bound with every power, a contradiction. Therefore Fhat vanishes on a smaller sector. Since F=-(a/c)R_wY and v=tau zeta.Y, V also vanishes there.

## 8. Finite-sector assembly

There are exactly2l scalar sectors. In each sector of the k-zero type the preceding argument supplies a positive smaller radius with V=W=0. In each entirely irrotational sector W already vanishes. Take the minimum of these finitely many radii and one common shorter flow interval. Then W vanishes off the nodal arcs throughout a full smaller tube, and it vanishes on the arcs and central ray by continuity.

Every component of V is now harmonic on an actual full neighborhood of x0. Its Taylor series there converges, and all its derivatives are zero. Hence V=0 near x0. A harmonic function merely on a corner sector would not justify this last step; the finite-sector assembly is indispensable.

## 9. Consequence for actual profiles and limits

For the global consequence assume 2/5<c<1/2, arbitrary real omega, U in C2(R3), P in C1(R3), div U=0 and (1-c)U+DU(Ax+U)+omega JU+grad P=0. Assume U.curl U=0 and, for one finite C, |U(x)|<=C(1+|x|)^(-p) and |DU(x)|<=C(1+|x|)^(-p-1), p=(1-c)/c. Let V,P2 be the actual tails, W=curl V, S=P2-|V|2/2 and T0={w in S2: V(w)=DV(w)=P2(w)=S(w)=0} intersect supp W. Assume V is smooth near every point of T0; the pressure equation then also makes P2 smooth there. Combining A1151-A1152 with the present local theorem, if U is nonzero, at least one point of T0 has V of infinite order. At every such supported point the present theorem forces S of infinite order too. Thus a nonzero profile in that class requires a supported common infinitely flat V/S point. There is no longer a finite-S alternative with accumulating irrotational patches.

This statement does not exclude each individual finite-order T0 point, does not derive tail smoothness from C2, and does not prove continuation at a common scalar-flat point. The examples A1265-A1267 explain why the finite scalar jet cannot simply be deleted from a general first-order theorem. The unrestricted arbitrary-helicity bare-decay conjecture remains OPEN.

## 10. Verification and dependencies

All ten source sections were read in full. The new harmonic zero extension was reconstructed in Sections2-3, and the one-sector frequency with each separate side flux in Sections5-7. The nodal map is the independently proved A1244 construction; the local angular identities and drift match were also independently checked in A1262 and are restated here. No new external unique-continuation theorem, computation or formal build is used. The source and its actual capture time and hash are in the team records.
