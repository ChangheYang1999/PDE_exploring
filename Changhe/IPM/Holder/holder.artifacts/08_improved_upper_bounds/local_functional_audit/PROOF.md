# The two-pole local angular bound is phase dependent in sharpness

## Statement and conventions

Fix 0<alpha<1. Let x=(1,0), y=(0,0), R=1/2, and let [f]_alpha be the real Euclidean homogeneous Holder seminorm. Put

    K_phi(h)=cos(2 arg h-phi)/(2 pi |h|^2),
    L_phi(f)=pv integral_(B(x,R)) K_phi(z-x) f(z) dz
             -pv integral_(B(y,R)) K_phi(z-y) f(z) dz,
    a2(alpha)=2^(1+alpha/2)/(pi(alpha+2)),
    U(alpha)=2 a2(alpha) R^alpha/alpha.

Both principal values use circular holes and are defined by subtracting the value at the corresponding pole. This is the own-kernel local functional only; it omits the opposite-pole cross kernels and any identity atoms. Its norm is on all real f with [f]_alpha<=1, modulo constants.

Then

    ||L_0|| < U(alpha),       ||L_(pi/2)|| = U(alpha).          (1)

Thus the statement that the two disks' individual angular extremizers are jointly attainable at every phase is false. The same number U remains a valid upper bound at every phase, and is the exact maximum over phases. No certified operator endpoint is invalidated.

## Universal bound and attainment of the local norm

For a pole p define

    A_p(r)=(1/(2pi)) integral_0^(2pi) cos(2theta) f(p+r omega(theta)) dtheta.

The accepted exact angular reflection lemma gives |A_p(r)|<=a2 r^alpha. Integrating dr/r gives |L_0(f)|<=U; rotation of the angular lemma gives the same bound at every phase.

Normalize f(0)=0. The Holder unit ball is compact in local uniform convergence by Arzela-Ascoli on successive disks. For each positive inner cutoff epsilon, L_phi with both disks cut off is a continuous functional of f on this ball. The omitted inner portions have norm at most 2a2 epsilon^alpha/alpha, uniformly in f and phi. Thus L_phi is a uniform limit of continuous functionals and attains its absolute norm on this compact ball. Changing f to -f, a maximizer may be chosen with L_phi(f)>=0.

## Strictness at the axis phase

Suppose L_0(f)=U. The nonnegative deficits a2 r^alpha-A_x(r) and a2 r^alpha+A_y(r) have zero dr/r integral. They are continuous for r>0, so both vanish for every 0<r<R.

In the angular reflection proof, each positive half-lobe is paired with the adjacent negative half-lobe across the intervening zero ray. The Holder inequality on every pair has a nonnegative deficit. Its integral with strictly positive cosine weight in the half-lobe is zero. Continuity therefore forces equality for every pair, including the endpoint pair by taking a limit.

At the pole x, take the reflection across angle 3pi/4, whose endpoint pair is p=x-r e1 and a=x+r e2. At the pole y, use the reflection across pi/4 for the negative angular functional, whose endpoint pair is b=y+r e2 and q=y+r e1. The forced equalities are

    f(p)-f(a)=(sqrt(2)r)^alpha,
    f(b)-f(q)=(sqrt(2)r)^alpha.

But |p-q|=1-2r and |a-b|=1. Consequently

    1 >= f(b)-f(a)
      =2(sqrt(2)r)^alpha + f(q)-f(p)
      >=2(sqrt(2)r)^alpha-(1-2r)^alpha.

As r increases to1/2, the last quantity tends to2^(1-alpha/2)>1. This is a contradiction. Since the local norm is attained, its upper bound is strictly smaller than U, proving the first part of (1). This proof establishes a strict gap but does not quantify it.

## Exactness at the diagonal phase

Let Z be the union of the horizontal axis and the two vertical lines through x and y. On the complement define

    sigma(z)=sign(z2) sign(z1(z1-1)),
    f(z)=2^(alpha-1) sigma(z) dist(z,Z)^alpha,

and set f=0 on Z. The sign is constant on each connected component of the complement. If two signs differ, their joining segment crosses Z. The signed-distance Holder lemma therefore gives [f]_alpha<=1.

In B(x,1/2), the nearest vertical line is z1=1, and sigma has the sign of (z1-1)z2. Thus f restricts to the exact angular extremizer for sin(2theta) about x. In B(y,1/2), the nearest vertical line is z1=0, and sigma is minus the sign of z1 z2. Thus f restricts to the exact negative angular extremizer about y. The two local contributions both attain a2 R^alpha/alpha, proving L_(pi/2)(f)=U and the second part of (1).

## Implication for the numerical calibration

The floating program locD_lp.py compares a fixed-phase local C value with U. At phi=pi/2 this is comparison with a known exact value. At phi=0 the gap U minus the program value contains both a genuine transport gap and discretization effects. It cannot all be described as a discretization deficit. Transferring the phi=pi/2 deficit to other phases or to the local D functional remains a heuristic calibration, not an established error estimate.

The report's observation about possible savings can remain explicitly numerical after this distinction is made. The currently accepted global C and D bounds use U only as an upper bound and are unaffected.

Dependencies: the angular reflection and signed-distance lemmas, local uniform compactness, and the displayed elementary inequalities. No numerical integration, external theorem or global exact norm is used.
