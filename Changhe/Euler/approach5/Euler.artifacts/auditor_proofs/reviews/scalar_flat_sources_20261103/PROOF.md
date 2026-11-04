# Scalar-flat weighted sources and a pressure obstruction for polar swirls

Status: independently proved at the exact planar-countertest and nonrotating local-cone scopes below. All six sections of LIT221 and all seven sections of LIT222 were read. Read after the finite-scalar first-order theorem. Neither example is an original Euler profile.

## 1. A planar smooth flat countertest

For any q>1 set eta=1/q, t=x^2+y^2, E(t)=exp(-1/t) for t>0, and define

    F=E(t)(x,y), S=t^q exp(-q/t).

Extend both by0 at the origin. Every Cartesian derivative is a finite sum of polynomial factors times a real power of t and exp(-lambda/t), lambda>0. Such terms tend to0 faster than every power. Difference quotients inductively prove smoothness and flatness at0, including noninteger q. Off0,

    div F=2E(1+1/t), curl F=0,
    grad S=2q S(1/t+1/t^2)(x,y).

Therefore S div F-eta F.grad S=0 everywhere, including0. F is nonzero elsewhere and has the positive radial index+1. This satisfies the exact first-order planar system with K=I and b=0, except for the finite scalar jet premise. It refutes deleting that premise with no replacement assumption.

## 2. The exact weighted point source and stream period

The divided vector is |S|^(-eta)F=(x,y)/t. It has norm1/r and is locally integrable in two dimensions. Its classical divergence vanishes off0, but its outward flux across every centered circle is2pi. For a compactly supported smooth test function phi, punctured-disk integration gives

    -integral ((x,y)/t).grad phi
       =lim_(epsilon to0) integral_0^(2pi) phi(epsilon e(theta))dtheta
       =2pi phi(0).

Thus its distributional divergence is2pi delta0, with positive sign. This is a genuine source, not merely a divergent integral.

Its weighted energy |S|^(-eta)|F|^2=E(t) is finite on bounded disks. Nevertheless R|S|^(-eta)F=(-y,x)/t has period2pi around a positively oriented circle and has no single-valued stream potential on the punctured disk. On a slit disk the potential is the angle and is not flat. Flat F and finite energy alone therefore justify neither center removability nor a flat potential after division by a flat scalar.

## 3. A three-dimensional lift fails the pressure equation

Extend t,E independently of z and set v=E(t)(-y,x,0), pi=S+tE^2/2. This smooth field is divergence free and has v.curl v=0, and pi-|v|^2/2=S. Its axis is a supported flat zero set. For any g(t), Delta g=4(tg''+g'). Direct differentiation gives

    tr((Dv)^2)=-2E^2(1+2/t),
    Delta(tE^2/2)=2E^2+4E^2/t+8E^2/t^2,
    Delta S=(4qS/t^3)[q t^2+(2q-1)t+q].

Consequently the pressure residual is

    Delta pi+tr((Dv)^2)
       =8E^2/t^2+(4qS/t^3)[q t^2+(2q-1)t+q]>0

for every t>0. A pressure constant cannot fix it. A changed pressure would change the assigned scalar, so would not be the same test. No homogeneity or actual-profile realization is claimed.

## 4. Exact local polar-swirl nonexistence statement

Fix0<c<1/2, p=(1-c)/c>1, d=p-1, a=cd, q=2p/d>2 and omega=0. On a full polar cone containing the north ray, suppose

    V(r,theta,phi)=r^(-p) f(theta)e_phi

is smooth, is flat at x0=(0,0,1), and f(theta)!=0 for every0<theta<theta0. Then there is no smooth pressure P2 of ordinary homogeneous degree -2p on a smaller such cone satisfying, with W=curl V and S=P2-|V|^2/2,

    W.grad S=0, -Delta P2=tr((DV)^2).

The scalar is allowed to depend on azimuth. There is no spatial-origin regularity premise, but all north-axis points in the cone are included. Nonvanishing on the punctured cap is a hypothesis.

The exact curl is

    W=r^(-p-1)[(f'+cot(theta)f)e_r+d f e_theta].

Thus div V=0, V.W=0, X.V=0 and X cross W=aV for X=cx. Write S=r^(-2p)h(theta,phi). Its transport equation is

    d f h_theta=2p(f'+cot(theta)f)h.

Because f never vanishes in the punctured cap, all solutions are

    h=C(phi)|sin(theta)f(theta)|^q.

Fixing one interior angle shows C is smooth, periodic and bounded. No sign or azimuthal invariance of C is assumed.

## 5. Uniform scalar smallness contradicts local pressure

The exact ratio is

    |S|/|V|^2<=||C||_infinity sin(theta)^q |f(theta)|^(q-2).

It tends uniformly to0 at the axis because f tends to0 and q>2. The radial factors cancel. On a small ordinary ball centered at x0, S>=-|V|^2/4, with zero values on the axis by continuity. Flatness of V and this ratio show S and P2 vanish to arbitrary orders in value at x0; smoothness identifies their Taylor jets as zero.

Translate the ball center to0, put v=V, pi=P2 in translated coordinates, and let sphere averages at radius R define E=average|v|^2, A0=average(v.n)^2, Y=average(pi-pi(0))+A0. The exact pressure divergence and div v=0 give

    Y'=(E-3A0)/R.

For clarity, integrating Delta pi=-partial_i partial_j(v_i v_j) over the ball gives (average pi)'=-average[n_i partial_j(v_i v_j)]. Differentiating n_i and integrating the tangential divergence yields the latter average=A0'+(3A0-E)/R. This proves the displayed identity with no remote boundary.

Since pi(0)=0 and S>=-|v|^2/4, Y>=E/4+A0>=0 and Y'<=4Y/R. Hence R^(-4)Y is nonincreasing. Flatness gives limit0 at0, so Y=E=0 at all small radii. Thus v=0 on the ball, contradicting nonzero f at every small positive angle. This proves the stated local nonexistence theorem. It is the precise flat case of A1200 with its pressure argument included.

## 6. The spherical weighted source survives all the geometric identities

Take t=sin(theta)^2, f(theta)=sin(theta)exp(-1/t), and h0=(t exp(-1/t))^q. Then

    V(x)=|x|^(-p-1)exp(-1/t)Jx,
    t=(x1^2+x2^2)/|x|^2,
    S=r^(-2p)h0.

The exponential extension is smooth on the full polar cone and flat on its north ray. It is nonzero off the axis. The homogeneity, curl, divergence, helicity, X cross W=aV and scalar transport above all hold. The rank relation is automatic because k=0. With P2=S+|V|^2/2, pressure is the missing equation. Section5 excludes every smooth homogeneous pressure completion satisfying transport, including azimuthally varying alternatives, since it lists all possible C(phi).

On the unit sphere the projected angular field is F=d f e_theta. Since eta=1/q,

    |h0|^(-eta)F=d e_theta/sin(theta).

Its classical surface divergence is zero off the north pole, and its flux through each small geodesic circle is2pi d. Test-function integration thus gives div_S(|h0|^(-eta)F)=2pi d delta_north. It is locally integrable. The energy density is |h0|^(-eta)|F|^2=d^2|f|/sin(theta), integrable against sin(theta)dtheta dphi. This proves that actual spherical geometry and curl do not alone remove the source. The pressure equation supplies the separate obstruction.

## 7. Exact scope and dependencies

The planar example refutes an unrestricted scalar-flat extension of the first-order theorem; it does not refute a theorem separately assuming zero weighted source and a flat stream potential. The polar result is restricted to omega=0, a purely azimuthal velocity, and an amplitude nonzero on the punctured cap. Additional zero circles, general angular velocities, arbitrary finite rotation and simultaneous scalar/velocity flatness in a full local tail remain open here. No actual Euler profile is constructed or excluded outside these hypotheses.

All derivatives, center fluxes and pressure signs were checked directly. No numerical computation, external theorem, formal build or new model client is used. A focused comparison through the existing configured model agents remains requested. Model provider runtime remains unattested.
