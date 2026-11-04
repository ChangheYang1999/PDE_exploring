# A canonical-pressure countertest to a reduced twist estimate

Status: A649 CONFIRMED at the exact hypotheses below, after complete source and independent proof postreads.

## 1. Exact field and scope

Let r=|x|, rho=(x1^2+x2^2)^(1/2), z=x3/r, w=1-z^2, Jx=(-x2,x1,0), and D=R3 minus{0}. Set p=5/4, c=4/9, lambda=1/4, mu=3/4, eta=1/10, t=omega/c and

    V=rho^2 r^(-p-3)Jx,
    P2=r^(-2p)u(z),
    u=-2(975z^6-3465z^4+7845z^2-1259)/8775,
    S=P2-|V|^2/2=r^(-2p)h(z),
    h=(4875z^6-12465z^4-5055z^2-3739)/17550.            (1)

For every real omega, V is smooth on D, divergence free, has V.curl V=0, and has the required twisted homogeneity. P2 is its global canonical Newtonian stress pressure. S is strictly negative and |S|^eta is locally A2 on D. When omega!=0, k=(cx-omega Jx).V vanishes exactly on the axis, where curl V=0.

Nevertheless the actual-tail scalar transport and vortical rank identities fail. In particular this example only refutes a twist bound based on the reduced hypotheses explicitly retained here. It does not refute the stronger estimate with every actual-tail identity imposed.

## 2. Velocity, curl and flux

The only cylindrical velocity component is V_phi=rho^3 r^(-p-3). It is axisymmetric, so div V=0. Its curl is poloidal, giving zero helicity. The scalar multiplier rho^2 r^(-p-3) and its gradient vanish on the punctured axis, so curl V vanishes there as well. Ordinary degree -p and covariant axisymmetry imply twisted homogeneity for any omega.

The exact spherical curl is

    W_r=4r^(-p-1)z w,
    W_theta=(p-1)r^(-p-1)w^(3/2), W_phi=0.             (2)

In the twisted angular variables chi=phi+t log r, the one-form coefficients are

    R=H=0, F=w^2, K=-t w^2,
    k=c r^(1-p)K.

In particular k=0 implies W=0 for t!=0. With the signed quantities of A641,

    D0=-lambda mu integral sgn(K)R=0,
    T=-lambda mu t integral sgn(K)F
      =lambda mu integral |K|=(2pi/5)|t|.              (3)

Here integral_S2 F=2pi integral_-1^1(1-z^2)^2 dz=32pi/15, and sgn K=-sgn t almost everywhere. This is exact saturation of the nodal flux inequality. For t=0 the nodal premise fails off the axis, as expected; no claim uses that case to meet it.

## 3. The pressure, including its normalization

Pure swirl acceleration is -(V_phi^2/rho)e_rho. Differentiating its cylindrical divergence gives

    tr((DV)^2)=r^(-2p-2)[-6w^2+2(p+3)w^3].             (4)

Also Delta(r^-2p u)=r^(-2p-2)[(wu')'+2p(2p-1)u]. Thus the pressure equation is

    (wu')'+(15/4)u=6w^2-(17/2)w^3.

The right side has coefficients (-5/2,27/2,-39/2,17/2) in powers (1,z^2,z^4,z^6). The operator on z^(2j) gives

    2j(2j-1)z^(2j-2)+(15/4-2j(2j+1))z^(2j).

Inserting the four coefficients (2518,-15690,6930,-1950)/8775 gives precisely that same four-term list. This is an exact hand coefficient verification.

The stress is O(r^-5/2) and is integrable near0. For each x!=0 the pressure kernel is smooth near y=0, giving absolute convergence there. At infinity its second Newtonian derivative is O(|y|^-3), so the radial majorant is r^-7/2 dr. Around y=x the smooth stress admits the ordinary principal-value subtraction and the local delta term. Hence its canonical Newtonian stress pressure exists and is smooth off0. Scaling the homogeneous distributional kernel shows that this pressure has ordinary degree -5/2. It solves the same Poisson equation as (1).

Their difference is therefore a smooth harmonic scalar on D of degree -5/2. Its spherical function f would solve Delta_S2 f+(15/4)f=0. The spherical eigenvalues l(l+1), l a nonnegative integer, never equal15/4. All spherical coefficients vanish, so the difference is zero. This verifies canonical pressure without adding an arbitrary local harmonic function. No behavior at the singular origin is asserted.

## 4. Strict negativity and the two nonzero defects

Subtracting the kinetic energy r^-2p w^3/2 gives exactly h in (1). For v=z^2 in [0,1], use v^3<=v^2 to get

    4875v^3-12465v^2-5055v-3739
       <=-7590v^2-5055v-3739<=-3739.

Thus h is uniformly negative on the sphere. On a compact subset of D both |S|^eta and its reciprocal are bounded. This proves local A2 directly.

By (2),

    W.grad S=r^(-3p-2)G(z),
    G=-8p z w h-(p-1)w^2 h'
      =-z w Q(z)/7020,
    Q=16575z^6-41949z^4-24195z^2-15967.                 (5)

The rank coefficient is

    [h K'-eta K h']/t=z w Q(z)/17550.                  (6)

To check both expressions independently, write h=N/17550. Then 10N+wN'/(4z)=(5/2)Q and 4N+wN'/(10z)=Q as polynomial identities, so no division at z0 is needed in the final formulas. These give (5),(6), and their ratio G=-2p times (6) is consistent.

Again v^3<=v^2 shows Q<0 for |z|<=1. Thus G>0 on 0<z<1, and the coefficient in (6) is negative there. Consequently scalar transport fails for every omega and vortical rank fails for every omega!=0. At omega0 k=0 makes that rank condition vacuous, but transport still fails. The two exact failures explain why actual-tail scalar-symmetry theorems do not apply.

## 5. The estimate that fails and the full-profile defect

An estimate

    |T|<=C(p)|t|(D0+integral |K|)                      (7)

uniform over nonzero t for this reduced class would, by (3), require C(5/4)>=3/(16|t|). This is impossible for a finite constant independent of t. If the second summand on the right is lambda mu integral|K|, the necessary bound is instead C(5/4)>=1/|t|. Thus both versions fail with only the reduced hypotheses in Section1. Retaining the identities whose nonzero defects appear in Section4 could change that conclusion; it has not been decided.

The full similarity-linear part vanishes because V is twisted homogeneous. The remaining acceleration plus pressure gradient has azimuthal curl

    (curl(DV V+grad P2))_phi
       =(2p+6)x3 rho^5 r^(-2p-8).                     (8)

Indeed the radial cylindrical acceleration is -rho^5 r^(-2p-6); its x3 derivative is (8). It is nonzero away from the axis and equatorial plane, regardless of pressure. Therefore V is not a full profile even locally on those regions. It is also singular at0. Its energy integral at infinity grows as R^(3-2p)=R^(1/2). No smooth decaying whole-space counterexample is provided.

## 6. Dependencies and verification

The complete LIT164 proof was read. The velocity and flux test were previously checked as A637; the pressure coefficients, normalization, strict sign and both scalar defects have been independently reconstructed above. No new computation is needed or claimed. The existing configured-model CO37 input is the source of the proposed twist question, and the stronger question with all equations remains open. A canonical pressure alone does not supply the missing scalar identities.
