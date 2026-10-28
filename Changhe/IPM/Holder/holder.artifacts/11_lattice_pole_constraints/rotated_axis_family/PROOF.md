# Rotating the far-field witness independently of the local projection

## Statement

Fix 0<a<1. Use the real homogeneous Holder space modulo constants, with seminorm [f]_a=sup_{z!=w}|f(z)-f(w)|/|z-w|^a, and the increment-defined singular integrals of ../../01_setup/PROOF.md. Let x=(1/2,0), y=-x, H={X>0}, k=2^(a-1), and h(X,Y)=k X^a on H. Let Q_delta be counterclockwise Euclidean rotation through delta. Fix b>0, and define the closed polygon Z and signed-distance function g_b as follows.

In H put B(X)=1/2-X for 0<X<=1/2, B(X)=X-1/2 for 1/2<=X<=1/2+b, and B(X)=[X-1/2+(sqrt(3)-1)b]/sqrt(3) thereafter. The set Z is the union of the vertical axis, the graphs Y=+-B(X) in H, and their reflections into X<0. The sign sigma is positive when X>0 and |Y|<B(X), negative when X>0 and |Y|>B(X), and is reversed by X-reflection. Set g_b=k sigma dist(.,Z)^a, with value zero on Z.

Define the homogeneous projection profile

    P_0(u)=1/2[|u|^a+sgn(u_1^2-u_2^2)(|u_1^2-u_2^2|/|u|)^a],
    P_0(0)=0,    P_phi(u)=P_0(Q_(-phi/2)u).

Let K be any proved upper bound for [P_0]_a, and choose lambda>=0 with lambda K<=1. For arbitrary real c, delta and phi define on H

    F(w)=min(g_b(Q_delta w)+c, -1/2+lambda P_phi(w-x)),
    f(w)=max(-h(w),min(h(w),F(w))).

Extend f by central oddness, f(-w)=-f(w), and set f=0 on X=0. Then [f]_a<=1, f(x)=-1/2 and f(y)=1/2. Put

    K_phi(u)=[cos(phi)(u_1^2-u_2^2)+2sin(phi)u_1u_2]/(2pi|u|^4),
    nu_phi(w)=K_phi(w-x)-K_phi(w-y),
    I_phi=PV integral_R2 nu_phi(w)f(w) dw.

The principal value removes equal centered disks at x and y, or subtracts the respective pole value from the own-pole kernel inside each disk. The resulting integral converges at infinity, and

    D_a >= |I_phi|+1/2,

where D_a is the norm of R_1^2=T_xx-I/2 on the stated real homogeneous space. The same lower bound holds when D_a is initially defined using real compact smooth tests.

For a numerical enclosure, fix 0<epsilon<1/2 and write e_delta=|sin(delta/2)|. Suppose

    lambda epsilon^a+k(e_delta+epsilon)^a <= c+1/2,
    lambda epsilon^a <= 1/2.                             (1)

Define

    A(a)=Gamma(1+a/2)/(2sqrt(pi)Gamma(3/2+a/2)),
    M=lambda A(a)epsilon^a/a+cos(phi)epsilon^2/4,
    E=a epsilon/[pi(1-2epsilon)^(1-a)]
        +epsilon^(a+2)/[(a+2)(1-epsilon)^2].              (2)

Each pole disk has regularized integral in [M-E,M+E]. Their combined contribution is therefore in [2M-2E,2M+2E]. For R>1/2 the absolute contribution of |w|>R is at most

    2^a R^(a-1)/[(1-a)(1-1/(4R^2))^2].                 (3)

This is a family of analytic lower-bound witnesses and error formulas. No numerical improvement is asserted without a separate outward-arithmetic enclosure of the middle region, the hypotheses (1), and the profile bound K.

## Admissibility and the operator increment

The signed-distance function g_b has seminorm at most one. Indeed, on a component with fixed sign the distance function is 1-Lipschitz and |s^a-t^a|<=|s-t|^a. Across opposite signs, the segment meets Z. Thus d(p)+d(q)<=|p-q|, and k(d(p)^a+d(q)^a)<=|p-q|^a by concavity. Values on Z follow by continuity. Rotations preserve the seminorm. The profile hypothesis and lambda K<=1 give [lambda P_phi]_a<=1. Minima and maxima preserve this bound, so [F]_{a,H}<=1. Since P_phi(0)=0, F(x)<=-1/2 for every real c; no restriction on c is needed for this admissibility step.

The half-plane gluing proof in ../half_plane/PROOF.md applies. For clarity, |f(X,Y)|<=k X^a and the clamp preserves the seminorm within H. For p in H and q in -H, |f(p)-f(q)|<=k(X_p^a+|X_q|^a)<=(X_p+|X_q|)^a<=|p-q|^a. Reflection gives the bound within -H and continuity gives the bound on X=0. At x, h=1/2 and F<=-1/2, so f(x)=-1/2; central oddness gives f(y)=1/2.

The kernels are even, hence nu_phi is centrally odd. The product nu_phi f is centrally even. The kernel difference is O(|w|^-3), while |f(w)|<=k|w|^a, giving convergence at infinity for a<1. Near each pole, subtracting its value leaves an absolutely integrable product O(r^(a-2)); the subtracted constant integrates to zero on each centered annulus. The operators T_phi-I/2 and T_phi+I/2 both have norm D_a by rotation and sign, as proved in ../half_plane/PROOF.md. Their increments at x,y are I_phi+1/2 and I_phi-1/2. Their larger absolute value is |I_phi|+1/2, proving the lower bound. Compact smooth approximation for this fixed increment follows from ../../01_setup/PROOF.md.

Central reflection is essential here. For nonzero phi or delta, one must not replace it by reflection in X alone or assume evenness in Y. No positive Stieltjes formula is claimed for this family.

## The omitted pole disks

The pole x belongs to Z. Hence dist(Q_delta(x+u),Z)<=|Q_delta x-x|+|u|=e_delta+|u|. Since 0<=P_phi(u)<=|u|^a, (1) implies

    -1/2+lambda P_phi(u)<=g_b(Q_delta(x+u))+c

throughout |u|<=epsilon. The second condition gives -1/2+lambda P_phi(u)<=0<h(x+u). Thus only the lower clamp can change the projection branch. Write

    f(x+u)=-1/2+lambda P_phi(u)+d(u),
    d(u)=[1/2-h(x+u)-lambda P_phi(u)]_+.

Because P_phi>=0, d vanishes for u_1>=0 and satisfies 0<=d(u)<=a(-u_1)/(1-2epsilon)^(1-a) for -epsilon<=u_1<0. This is the mean-value estimate for (1+2u_1)^a/2. Using |K_phi(u)|<=1/(2pi|u|^2) and integral_(cos theta<0)(-cos theta)dtheta=2 gives

    |integral_(|u|<epsilon) K_phi(u)d(u)du|
       <=a epsilon/[pi(1-2epsilon)^(1-a)].

The rotation defining P_phi aligns its angular factor with cos(2theta-phi). Its radial part has zero angular integral, while the remaining part gives (1/(4pi))integral_0^(2pi)|cos(2theta-phi)|^(a+1)dtheta=A(a). Radial integration therefore gives lambda A(a)epsilon^a/a exactly.

The smooth other-pole kernel is K_phi(e_1+u), which is harmonic throughout the disk. Its mean is K_phi(e_1)=cos(phi)/(2pi). Consequently the constant pole value contributes cos(phi)epsilon^2/4. The remaining smooth term is bounded by epsilon^(a+2)/[(a+2)(1-epsilon)^2], since |f(x+u)+1/2|<=|u|^a. These estimates prove (2) for the right disk. Central reflection w->-w interchanges the disks and preserves nu_phi f, including the corresponding pole-value subtraction, so their contributions agree.

## Exterior error and choice of rotations

Identifying w with X+iY gives the exact identity

    nu_phi(w)=Re[e^(i phi)w/(pi(w^2-1/4)^2)].

For r=|w|>R>1/2, its absolute value is at most 1/[pi r^3(1-1/(4R^2))^2]. Multiply by |f(w)|<=k r^a and integrate in polar coordinates. The radial integral is R^(a-1)/(1-a); the angular integral is 2pi. This proves (3).

Away from its limiting rays, the unrotated polygon signs at large radius follow cos(3theta), whereas the leading dipole phase is cos(3theta-phi). The choice delta=-phi/3 therefore aligns these limiting signs before the half-plane clamp. The local projection is rotated through -phi/2. This observation motivates exploration only. It does not prove an optimal phase, an improved integral, or an exact expression for the clamped far profile.

## Dependencies and verification

The setup proof fixes all singular-integral and space conventions. The half-plane gluing argument and the signed-distance lemma are reproduced above. The only numerical input required for admissibility is the separately certified profile seminorm K. All new local and exterior estimates are proved here. This proof was written before any numerical evaluation of the new family. Independent lead cross-read is pending; any numerical results remain observations until the verifier accepts their complete certificate.
