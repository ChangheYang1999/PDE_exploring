# Pairing the balanced part of a local residual measure

## Statement

Let 0<a<1 and [f]_a=sup_(z!=w)|f(z)-f(w)|/|z-w|^a for real functions
on R^2. Fix x=(1/2,0), y=-x and 0<s<=1/2. Let sigma be a finite real
signed measure supported in the closed disk B(x,s). Let M(z)=-z and
mu=sigma-M_#sigma. Write V=|sigma|(R^2) and q=sigma(R^2). Then

    |integral f dmu|
       <= [f]_a [(V-|q|)(2s)^a+|q|(1+2s)^a].          (1)

Consequently, if V<=Vhat and |q|<=Qhat, the valid explicit upper cost is

    Vhat(2s)^a + min(Vhat,Qhat)[(1+2s)^a-(2s)^a].      (2)

This never exceeds Vhat(1+2s)^a. It is strictly smaller if the upper
bound for |q| is strictly smaller than Vhat.

In the local annulus certificate for T_phi=cos(phi)T_xx+sin(phi)T_xy,
with kernel K_phi(z)=Re(exp(i phi)/z^2)/(2 pi), use the right density

    w(r,theta)=[cos(2theta-phi)
                 -r^2 Re(exp(i phi)/(1+r exp(i theta))^2)]/(2 pi)

against dtheta dr/r. On a radial bin [r0,r1] with 0<r0<r1<=1/2,
suppose extracted signed cell masses have total signed mass E. Then
the unextracted right residual has exactly

    q=-cos(phi)(r1^2-r0^2)/2-E.                       (3)

Take s=r1 in (2). The original certified upper residual variation is
still usable as Vhat. Every extracted transport cost, omitted-disk
estimate, middle/exterior term and phase interpolation is unchanged.
The statement applies to the homogeneous seminorm and to the original
circular principal values, with operators defined modulo constants.
For R_1^2=T_xx-I/2 it applies directly when the full identity atoms were
included in the extracted transport, as in the global-atom construction.
It asserts no numerical operator improvement before recombination.

## Proof of the residual estimate

Write the Jordan decomposition sigma=sigma^+-sigma^-, with masses P,N.
Set h=min(P,N). Extract mass h from each Jordan part and couple the
extracted positive and negative pieces arbitrarily within B(x,s).
The cost for |z-z'|^a is at most h(2s)^a. The reflected negative measure
has the same balanced mass h and admits the same estimate in B(y,s).
Their combined cost is 2h(2s)^a=(V-|q|)(2s)^a.

The remaining right measure has one sign and mass |q|. Its negative
reflection is the remaining left measure. Pair every right point z
with -z. Since |2z|<=1+2s, this cost is at most |q|(1+2s)^a.
Applying the Holder inequality to these three couplings proves (1).
When P or N vanishes the balanced coupling is empty; when q=0 the
cross-disk coupling is empty, so both edge cases are covered.

Rewrite (1)'s cost as

    V(2s)^a+|q|[(1+2s)^a-(2s)^a].

Both coefficients are nonnegative and |q|<=V. Hence V<=Vhat and
|q|<=min(Vhat,Qhat) prove (2), including the comparison with the old
reflection cost. No assumption about a density or pointwise signs of
the residual is needed.

## Exact residual mass for the singular-integral certificate

The own-pole angular density has mean zero. The function
z -> (1+z)^(-2) is holomorphic on the open unit disk. Its mean on
|z|=r<1 is its value at zero, namely one. Taking the real part after
multiplication by exp(i phi) gives

    integral_0^(2pi) w(r,theta) dtheta=-r^2 cos(phi).

Integrating against dr/r on [r0,r1] gives
-cos(phi)(r1^2-r0^2)/2. Subtracting the signed extracted mass E proves
(3). The left residual is the negative central reflection because
both the original measure and the extraction were paired that way.
Thus the abstract theorem applies without changing the finite spatial
partition or introducing an additional identity contribution.

If some identity mass remains in the residual, add its signed right
atom mass to q and retain its variation in Vhat. Thus an unextracted
right identity atom of mass -m changes q to q-m, with m>=0.
The support remains in the same closed disk because the pole belongs
to it. This variant follows directly from the abstract theorem; its
actual mass must be specified and checked before computational use.

## Dependencies and verification

The finite extracted-mass and support hypotheses are exactly those in
../PROOF.md and ../radial_atoms/PROOF.md. Their full operator completion
supplies the singular limits, exterior convergence and phase estimates.
The new ingredient is the explicitly constructed residual transport
above. A certificate may evaluate (3) in outward arithmetic, add its
absolute upper endpoint as Qhat, and use (2) with its existing upper
variation Vhat. Floating LP optimization and sign tests alone do not
certify any of these masses. Independent cross-read is pending.
