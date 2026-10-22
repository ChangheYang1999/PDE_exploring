# A two-term dipole obstruction and shifted radial vorticity exclusion

Date:2026-10-20. Status: CONFIRMED by independent proof and checked actual Opus41 review.
This excludes a shape subclass only. It is not a full NO endpoint.

## 1. Exact setting and dependencies

Let beta>=2 and let (Theta,Omega,V) be a smooth full-plane solution of

    W.grad Omega+Omega=Theta_x, W.grad Theta=(beta-2)Theta,
    W=beta X+V, div V=0, Omega=partial_y V1-partial_x V2,
    V=U-U(0), U=(-Psi_y,Psi_x), -Delta Psi=Omega.

Assume the full prompt's x-reflection parity, Theta(0,y)=0, the nonzero
quadratic center jet a0 x^2, sublinear canonical velocity and polynomial
vorticity/temperature control. No sign condition, global-source condition,
or y-reflection is imposed. Packets33,36,40 give, with nu=1/beta and
m=1-2nu, smooth functions a,b,h on the angle circle such that

    Omega(r,theta)=r^{-nu}a(theta)+r^{-2nu}b(theta)+o(r^{-2nu}),
    Theta(r,theta)=r^m h(theta)+o(r^m),                 (1)

with every fixed angular derivative, and

    |D^j Omega(X)|<=C_j r^{-nu-j}, a not identically0,
    h(pi/2)=h(-pi/2)=0.                               (2)

The functions omega0=r^{-nu}a(theta), theta0=r^m h(theta) and their
canonical homogeneous velocity u0 satisfy

    r^{-2nu}b(theta)=u0.grad omega0-partial_x theta0.  (3)

These are already independently proved far-field consequences of the
full class, not additional decay assumptions. Packet36 supplies smoothness
at every angle; uniform continuity alone would not suffice below. The
canonical homogeneous inverse and its absence of a free affine strain
are proved in35. The parameter range beta<2 was excluded in01.

## 2. Angular theorem

There is no such profile for which

    a(theta)=A cos(theta), b(theta)=B cos(theta)       (4)

with real constants A!=0 and B. The value and sign of a0 are unrestricted.

Proof. The canonical homogeneous inverse of omega0=A r^{-nu}cos(theta)
is

    Psi0=C r^{2-nu}cos(theta),
    C=A/[1-(2-nu)^2]=-A/[(1-nu)(3-nu)] !=0.           (5)

Indeed Delta[r^k cos(theta)]=(k^2-1)r^{k-2}cos(theta), so
-Delta Psi0=omega0. No harmonic homogeneous correction of degree2-nu
exists: 2-nu is strictly between1 and2, whereas the nonzero angular
frequencies of a single-valued harmonic function are integers. The
canonical velocity has polar components

    u0_r=C r^{1-nu}sin(theta),
    u0_theta=(2-nu)C r^{1-nu}cos(theta).              (6)

The sign in(6) is specifically U=(-Psi_y,Psi_x). Direct multiplication
with omega0_r and r^{-1}omega0_theta gives

    u0.grad omega0=-2CA r^{-2nu}sin(theta)cos(theta).

Also partial_x theta0=r^{-2nu}[m cos(theta)h-sin(theta)hprime].
Consequently(3)-(4) require

    m cos(theta)h-sin(theta)hprime
           =-2CA sin(theta)cos(theta)-B cos(theta).  (7)

First suppose beta>2, so0<m<1. On each of the intervals
(-pi/2,0) and(0,pi/2), a particular solution is

    hpart=(CA/nu)sin(theta)-B/m.

The homogeneous equation has the solutions D |sin(theta)|^m, since
hprime/h=m cot(theta). Thus h=hpart+D_-|sin(theta)|^m on the lower
interval and h=hpart+D_+|sin(theta)|^m on the upper interval. Smoothness
of h at0 forces both D_-=D_+=0: a nonzero such term has an unbounded
first derivative because0<m<1. Taking the two endpoint limits and
using(2) gives

    0=CA/nu-B/m, 0=-CA/nu-B/m.

Their difference forces CA=0, contradicting(5) and A!=0.

If beta=2, then m=0 and nu=1/2. Evaluating(7) at theta=0 forces B=0.
For sin(theta)!=0 it then gives hprime=2CA cos(theta). Smoothness across0
makes the integration constant the same on both intervals, so
h=2CA sin(theta)+D on the right semicircle. Its two axis values again
force CA=0. This contradiction proves the angular theorem for all
beta>=2. It uses no behavior across the line y=0 other than the full
profile's given smoothness; it imposes no horizontal symmetry. QED.

## 3. Shifted radial quotient corollary

No full-target profile can have

    Omega(x,y)=x g(x^2+(y-H)^2)                       (8)

for a fixed real shift H and a smooth scalar g on[0,infinity).
No positivity, monotonicity or global-source hypothesis is needed.

Proof. At points (r,H), whose Euclidean radius is comparable to r for
large r, (2) and direct differentiation of(8) give

    |g(r^2)|<=C r^{-1-nu},
    |g(r^2)+2r^2 gprime(r^2)|<=C r^{-1-nu},

hence |gprime(S)|<=C S^{-(3+nu)/2} for large S. For an arbitrary
angle theta put S=r^2-2Hr sin(theta)+H^2. It is comparable to r^2,
and its distance to r^2 is at most C_H r for large r. The mean-value
theorem therefore gives, uniformly in theta,

    Omega(r,theta)=r cos(theta)g(r^2)+O(r^{-1-nu}).    (9)

Since nu<=1/2<1, the error is o(r^{-2nu}). At theta=0, (1) and(9)
give

    r g(r^2)=r^{-nu}a(0)+r^{-2nu}b(0)+o(r^{-2nu}).   (10)

Substitute this into(9) and compare the first term in(1), then subtract
that first term and compare the second. It follows successively that

    a(theta)=a(0)cos(theta), b(theta)=b(0)cos(theta).

Nonvanishing of a implies a(0)!=0. This contradicts Section2. QED.

The fixed shift contributes first at a faster order than the second
vorticity term, which is why shifting the radial center cannot remove
the angular obstruction. The statement is conditional on the exact
shape(8), not on an approximately dipolar core or a fitted radial ansatz.
It strengthens49's shifted radial exclusion from the positive global
source subclass to the full admissible target. General profiles can
have angular corrections b that are not proportional to cos(theta),
and are not excluded here.

## 4. Verification and scope

The inverse, transport sign, particular solution and endpoint conditions
are independently derived above. An exact symbolic check is stored in
verification/algebra.json, generated by the verifier's own script in
code_independent. No numerical solver state is used. Actual model-review
metadata and any corrections are recorded in verification/audit.json.
No formal verification is claimed; formal/README.md records the restriction.

Actual Opus41 returned a written CONFIRMED audit on2026-10-20T17:47:10Z,
model claude-opus-5-5, elapsed61.206223751seconds. Its sign, endpoint
and fixed-shift calculations were checked against the proof. The harmless
radius-comparability clarification was adopted. Its suggestion that the
beta2 argument only needs continuity is understood after the angular PDE
has been established pointwise; the proof retains the given smoothness.
The previous Opus40 request returned no text and is not an endorsement.
