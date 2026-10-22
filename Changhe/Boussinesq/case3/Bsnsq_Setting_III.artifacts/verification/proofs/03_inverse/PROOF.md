# Canonical relative velocity and the absolute center drift

Status: proved within the stated decay class; the choice of a canonical absolute velocity for broader tails remains an explicit part of the problem. Independently audited on 2026-10-20.

## Statement and conventions

Write J(z1,z2)=(z2,-z1). The profile convention is U=(-Psi_y,Psi_x), -Delta Psi=Omega. Thus curl U=partial_x U2-partial_y U1=-Omega. The corresponding velocity kernel is

    K(Z)=JZ/(2 pi |Z|^2).

Suppose Omega is locally C^alpha for some 0<alpha<1 and satisfies |Omega(Y)| <= C(1+|Y|)^(-delta), delta>0. Define

    V(X)=integral_R2 [K(X-Y)-K(-Y)] Omega(Y) dY.

Then the integral is absolutely convergent at every X, V(0)=0, div V=0, curl V=-Omega, and V=o(|X|). For any C^1 sublinear velocity U with the same divergence and curl, V=U-U(0). If Omega is odd in x, V1 is odd in x and V2 is even in x.

There is also an absolutely convergent relative stream function

    Psi_rel(X)=-(1/(2 pi)) integral_R2
       [log|X-Y|-log|Y|+X.Y/|Y|^2] Omega(Y) dY.

It satisfies Psi_rel(0)=0, grad Psi_rel(0)=0, -Delta Psi_rel=Omega, and V=(-Psi_rel_y,Psi_rel_x).

## Proof of convergence, sign and growth

The fundamental solution of -Delta in two dimensions is -(1/(2 pi))log|Z|. Apply (-partial_y,partial_x) to obtain K as displayed. Near Y=X and Y=0 the velocity singularities have order 1/r and are locally integrable in two dimensions against bounded Omega. For |Y|>2|X|+1, the mean-value estimate for K gives

    |K(X-Y)-K(-Y)| <= C_1 |X| |Y|^(-2).

The far integral is bounded by C_2 |X| integral r^(-1-delta) dr and converges. The logarithmic subtraction has a remainder O(|X|^2/|Y|^2) at infinity; its logarithmic singularities and its 1/|Y| subtraction near zero are locally integrable. This proves absolute convergence of both displayed integrals.

Differentiation of the stream integral once gives V. In distributions the subtractions are harmonic or affine in X, so -Delta Psi_rel=Omega. Local elliptic regularity for locally Holder continuous Omega gives the stated classical divergence/curl identities. It also justifies local C^1 regularity of V and evaluation at zero. Parity follows by changing Y1 to -Y1 in the integrals.

For completeness, put R=|X|>=2. In the outer region |Y|>2R, the kernel-difference estimate gives O(R^(1-delta)). In |Y|<=2R the subtraction term is bounded by C integral_0^(2R)(1+r)^(-delta) dr. For the remaining centered kernel, first use |X-Y|>=R/2 in |Y|<=R/2. The resulting bound is C R^(-1) integral_0^(R/2) r(1+r)^(-delta) dr. In R/2<|Y|<=2R, use |Omega(Y)|<=C R^(-delta) and integral_|Z|<=3R |Z|^(-1) dZ=O(R). Combining these regions gives

    |V(X)| <= C' [1+R^(1-delta)]     if 0<delta<1,
    |V(X)| <= C' [1+log R]          if delta=1,
    |V(X)| <= C'                    if delta>1.

Each bound is sublinear.

## Proof of uniqueness of relative velocity

If U and U' are C^1, divergence-free, have equal curl, and are sublinear on the whole plane, their difference D has distributionally harmonic components because both its divergence and curl vanish. Harmonic regularity makes D smooth. At a fixed X0, the interior harmonic estimate gives

    |grad D(X0)| <= C/R sup_{B_R(X0)} |D|.

Sublinearity implies the right side tends to zero as R tends to infinity. Hence D is constant. Apply this to U and V, then use V(0)=0. Under the required x parity, the remaining constant has only a vertical component.

This is uniqueness of the relative velocity. It is not a proof that the unregularized Biot-Savart value U(0) converges.

## Center moments and the gauge issue

The strain moment is gauge independent. The displayed v0 moment is the center component of the ordinary Biot-Savart representative, when that convention is selected and the scalar integral converges absolutely:

    v0_2=(1/(2 pi)) integral_R2 y1 Omega(Y)/|Y|^2 dY,
    c=(1/pi) integral_R2 y1 y2 Omega(Y)/|Y|^4 dY.

For an arbitrary sublinear div-curl velocity, convergence of the scalar integral does not fix U_2(0): an added vertical constant preserves those equations. The equality v0_2=U_2(0) in the display requires selecting that ordinary inverse representative. The c integral converges at infinity under the power decay above. At zero odd smooth Omega is O(|Y|), which also gives absolute local convergence. For v0, the sufficient absolute condition is integral |Omega(Y)|/(1+|Y|) dY<infinity. In polar variables, if a1(r) is the cos(phi) coefficient of Omega and b2(r) its sin(2phi) coefficient, circular truncations give

    v0_2(R)=(1/2) integral_0^R a1(r) dr,
    c(R)=(1/2) integral_0^R b2(r)/r dr.

A tail a1(r)=A r^(-delta)+o(r^(-delta)), A!=0, causes power divergence of v0_2(R) when 0<delta<1, and logarithmic divergence when delta=1. Vanishing of the leading a1 coefficient alone is not sufficient for convergence. A remainder r^(-delta)/log r still diverges when delta<=1. Angular cancellation over circular shells also does not imply absolute integrability.

For this slow-tail class, V determines the stationary transport field W=beta X+V. A reconstructed physical solution still requires a stated rule selecting a constant v0 and U=V+v0. One may use a fixed finite-part convention only after defining every subtraction, its reference scale, and remainder hypotheses. The rule must not introduce a fitted independent drift. If the ordinary full-plane inverse converges and is the selected convention, its value must be reproduced, even when nonzero.

Changing a constant velocity together with the center curve translates the physical scalar and vorticity fields. It is not valid to leave those physical fields at the same spatial points and merely add a time-dependent velocity. This distinction is needed when using the observer-frame freedom.

## Why power-decaying Omega is an additional assumption

Sublinear U alone does not force uniform decay of its curl. For example, let

    Psi(x,y)=x exp(-x^2) sin(y^3)/(1+y^2),
    U=(-Psi_y,Psi_x),    Omega=-Delta Psi.

These fields are smooth with the required x parity. U is bounded on the plane: the leading y derivative of sin(y^3)/(1+y^2) is bounded. Therefore U=o(|X|). The leading second y derivative contains a nonzero multiple of y^2 sin(y^3), so Omega does not decay and is polynomially bounded. For fixed nonzero x it is unbounded along suitable sequences of y.

This example is not asserted to satisfy either transport equation. It refutes only the implication from the velocity growth hypothesis to power decay of vorticity. A full NO cannot identify the power-decay subclass with the entire prompt class without a further argument using the equations.

## Independent quadrature and verification

`../../code_independent/cartesian_inverse.py` implements V using physical-space quadrature. In a fixed square it integrates two sets of Cartesian Duffy triangles centered separately at X and at zero. Outside the square it uses its four sides and the radial compactification r=R q^(-1/delta), 0<q<1, extending to infinity. The actual source function is evaluated at every exterior point; no modal Green formula or prescribed exterior harmonic field is inserted.

The stable exterior integrand computes r^2[K(X-r e)-K(-r e)] as

    [JX-Je(2 X.e-|X|^2/r)/|e|^2] / [2 pi |e-X/r|^2].

This avoids subtracting two almost equal kernels at large r. The integration parameter delta changes the map only. It does not change Omega.

`../../verification/cartesian_inverse_manufactured.json` contains real run times, all six evaluation points, and absolute errors for three square sizes and three quadrature orders. Both manufactured fields have independently differentiated exact velocities. The slow field has Omega=O(r^(-1/3)) and U=O(r^(2/3)); it validates an infinite exterior integral. These tests are floating-point convergence evidence, not interval certification, and do not validate any B2 profile candidate.

The distinct scalar and radial integrability conditions, and a cutoff-shape counterexample, are proved explicitly in research/11_adversarial_examples/PROOF.md.
