# Axis symmetry and the missing half-plane constant

## Statement and scope

Fix 0<alpha<1, x=(1/2,0), y=-x and H={X>0}. All functions are real,
with [f]_alpha=sup_{z!=w}|f(z)-f(w)|/|z-w|^alpha, considered modulo
constants. Let K_phi and nu_phi have the conventions of the setup proof,
and let all pole integrals use centered circular principal values. Put

    h(X,Y)=2^(alpha-1) X^alpha,   X>0.

The fixed-axis functional for R_1^2 is

    A(f)=PV integral nu_0 f - (f(x)-f(y))/2.

Its norm is exactly

    sup_F |2 PV integral_H nu_0 F - F(x)|,                    (1)

where [F]_{alpha,H}<=1, |F|<=h, and F(X,-Y)=F(X,Y). No pole value is
prescribed in this supremum. Prescribing F(x)=-1/2 gives an admissible
lower-bound family, not a consequence of symmetry. Whether that extra
constraint preserves this norm is left OPEN here.

The half-plane kernel mass is

    PV integral_H nu_phi = -cos(phi)/2.                     (2)

Consequently, if J0=integral_H nu_phi(z)(F(z)-F(x)) dA(z), then

    Jf=PV integral_H nu_phi F=J0-cos(phi) F(x)/2.             (3)

The integral defining J0 is absolutely convergent at the pole and at
infinity. In the axis direction, for F(x)=-1/2,

    Jf=J0+1/4,    A(f)=2J0+1.

For the full operator norm D_alpha, the favorable choice between the
rotated operators T_phi-I/2 and T_phi+I/2 yields the valid lower bound
2|Jf|+1/2 for this pole-normalized family. Replacing Jf by J0 in that
bound is not a valid functional identity.

## Proof of the symmetry reduction

Let c(X,Y)=(X,-Y) and n(X,Y)=(-X,-Y). Both are Euclidean isometries.
The kernel K_0 is invariant under both maps. Since c fixes x,y while n
swaps them, A(f composed with c)=A(f) and A(f composed with n)=-A(f).
Apply the commuting averages (I+C)/2 and (I-N)/2 to f. They preserve A,
do not increase its seminorm, and produce a function even under c and
odd under n. The resulting function is odd under cn(X,Y)=(-X,Y).
Comparison with that reflected point gives

    2|f(X,Y)|<= (2X)^alpha,  X>0.

Its restriction F therefore belongs to the class in (1).

Conversely, for any F in that class, extend by f(-z)=-F(z) for z in H
and f=0 on X=0. The half-plane lemma proves [f]_alpha<=1: on opposite
sides the difference is bounded by

    2^(alpha-1)(X^alpha+X'^alpha)<=(X+X')^alpha<=|z-w|^alpha.

On each side use the seminorm of F. Evenness in Y supplies the required
axis symmetries. Central oddness of nu_0 and f gives its full integral
as twice the half-plane integral; the identity term is -F(x). This
proves (1). It does not force |F(x)| to equal its allowed maximum 1/2.

## Proof of the half-plane mass

Write K_xx=-partial_X V_X/(2pi), where

    V_X(X,Y)=(X-c)/((X-c)^2+Y^2)

for a pole (c,0). Integrate on H intersected with a large disk centered
at the origin, removing a small centered disk if c>0. On the line X=0
the flux of (V_X,0) is c/(c^2+Y^2), whose integral tends to pi sign(c).
On the outer semicircle its flux tends to pi/2. If c>0, the inner
boundary flux is -integral_0^{2pi}cos(theta)^2 dtheta=-pi. Thus

    PV integral_H K_xx(z-(c,0)) = -sign(c)/4.

Only differences of these improper integrals are used; their difference
has an absolutely integrable tail. Taking c=1/2 and c=-1/2 proves (2)
for phi=0. The K_xy terms are odd in Y, so their half-plane integral is
zero with these cutoffs. Linear combination proves (2) for every phi.
Subtracting the constant F(x) now proves (3). Since F is Holder, the
pole remainder is O(r^(alpha-2)); the increment kernel is O(r^-3) and
F-F(x)=O(1+r^alpha), proving the claimed absolute convergence.

## Exact counterexample to omitting the constant

Take

    f(X,Y)=-2^(alpha-1) sign(X)|X|^alpha.

On one side, |s^alpha-t^alpha|<=|s-t|^alpha. On opposite sides,
2^(alpha-1)(s^alpha+t^alpha)<=(s+t)^alpha. Equality holds for equal
opposite abscissae, so [f]_alpha=1. It has f(x)=-1/2 and f(y)=1/2.

For a function of X alone, R_1^2 f=-f and T_xx f=-f/2, modulo constants.
For completeness, the distributional identity K_xx-I/2 has multiplier
-xi_1^2/|xi|^2, equal to -1 on xi_2=0 away from the origin. Equivalently,
solve -u''=f in one dimension, so partial_XX u=-f. The homogeneous
increment definition agrees with this action by the setup theorem.
Hence A(f)=1 and PV integral nu_0 f=1/2. The half-plane values are
Jf=1/4 and J0=0 by (3). The expression 2|J0|+1/2 is 1/2, whereas the
actual increment is 1. This refutes the proposed subtraction identity,
without asserting that a universal inequality using that smaller
expression would fail for this example.

## Dependencies

Kernel normalization, the homogeneous extension and compact smooth
approximation from 01_setup/PROOF.md; the half-plane extension lemma in
11_lattice_pole_constraints/half_plane/PROOF.md. No floating-point data
or unproved saturation principle is used.
