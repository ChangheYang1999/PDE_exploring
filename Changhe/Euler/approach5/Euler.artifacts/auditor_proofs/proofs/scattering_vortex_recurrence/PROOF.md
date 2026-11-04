# Scattering vortex flow, recurrence, and basin energy

## Hypotheses and exact inputs

Let U in C2(R3;R3), P in C1(R3) solve the divergence-free rotating Euler profile equation with A=cI-omega J, B=Ay+U, 1/3<c<1/2, and finite real omega. Assume U bounded, U(R .)->0 in distributions, and

    integral_1^infinity sup_(|y|>=r)|DU(y)| dr/r < infinity.

Write Omega=curl U, k=(1-c)/c>1. The confirmed scattering theorems A209-A210 supply a compact null set K of forward-bounded B orbits and a continuous proper map S with S^-1(0)=K and |S(y)-y|<=||U||infinity/c. Off K, S is a measure-preserving C1 diffeomorphism onto R3 minus0, and

    S(Phi_s y)=exp(sA)S(y),
    Omega_tilde(Sy)=DS(y)Omega(y),
    Omega_tilde(exp(sA)z)=exp(-s)exp(-omega sJ)Omega_tilde(z).

Set G=Omega_tilde restricted to S2, G_r(w)=w.G(w), and

    Y(w)=G(w)-G_r(w)w+(omega/c)G_r(w)Jw.

The same theorem gives |Omega(y)|<=C(1+|y|)^(-1/c). Its velocity part gives V=curl^-1 Omega_tilde, continuous away from0, div V=0, curl V=Omega_tilde, and

    V(exp(sA)z)=exp(-(1-c)s)exp(-omega sJ)V(z),
    U(y)-V(y)=o(|y|^-k)

uniformly at infinity. Put F=V restricted to S2. This velocity input uses Omega=curl U; it is not available for an arbitrary independent transported field.

## Skew product and quantitative bound

Define rho=log|S(y)| and w=pi(Sy), where pi(z)=exp(-A log|z|/c)z. In these coordinates dy=exp(3rho) d rho dA(w). Reparametrize the vortex field to

    X(y)=|S(y)|^(1+1/c) Omega(y)

on R3 minus K. It is C1 there and preserves the measure |S|^(-1-1/c)dy. Direct differentiation of rho and pi gives the coordinate vector field (G_r(w),Y(w)), independent of rho and bounded on the cylinder. Though Y is only known continuous, its flow is unique by conjugacy with the C1 field X. Bounded cylinder speed and compactness of S2 make the flow complete: finite-time trajectories stay in a compact cylinder, whose inverse image under S is compact in R3 minus K.

It therefore has the form

    (rho,w) -> (rho+h_t(w),Y_t w),
    h_t(w)=integral_0^t G_r(Y_s w) ds.

It preserves exp(-(k-1)rho) d rho dA. Apply this invariance to (0,1) times a Borel set E in S2. After cancelling the positive integral of exp(-(k-1)rho) on (0,1), one obtains

    |E|=integral_(Y_t E) exp(-(k-1)h_t(Y_(-t)w')) dA(w').

Taking E={h_t>=M} yields

    |{w:h_t(w)>=M}|<=4pi exp(-(k-1)M)

for every real t and M>=0. In a scattering shell r1<|S|<r2, the corresponding volume bound is this fraction times (4pi/3)(r2^3-r1^3).

Each component of a vortex line outside K is one complete X orbit, with vortex time tau satisfying d tau/dt=|S|^(1+1/c)>0. Its vortex-time interval may be finite at an endpoint where it meets K. The statement concerns the complete reparametrized component, not necessarily all vortex times on the original line.

## Non-escape and recurrence

For fixed M>0, the sets {h_t>=M for all t>=n} increase with n and have measure at most4pi exp(-(k-1)M). Thus the set {h_t->+infinity as t->+infinity} is null, and so is the analogous negative-time set. Their cylinder lifts and inverse images under S are null. If one wants to transfer this conclusion across possible visits to K, apply Fubini to all vortex-time translates of the bad set. For almost every starting point, no open component of the line outside K is bad. Infinitely many visits to compact K give bounded returns; otherwise the eventual component has bounded-radius returns. The X time cannot end at a finite value while vortex time tends to infinity, since then its compact X orbit segment would bound d tau/dt. This proves non-escape at both ends.

There is a shorter stronger argument under the available vorticity bound. More generally, suppose Omega is C1, divergence-free and |Omega(y)|<=C(1+|y|)^(-p), p>2. Put

    b(y)=(1+|y|^2)^((p+1)/2), Z=b Omega.

Then |Z(y)|<=C'(1+|y|), so its flow is complete. It preserves the finite measure b^-1dy, because div(b^-1 Z)=0. Poincare recurrence for its time-one map and inverse, applied to a countable basis of balls, gives recurrence to the initial point in both time directions for almost every point. The measures b^-1dy and dy have the same null sets. Vortex time is the integral of b along this flow and b>=1, so the recurrent times also tend to positive and negative infinity in vortex time. Thus almost every vortex line returns arbitrarily close to its starting point at both ends. In the present setting p=1/c>2.

This does not preclude unbounded excursions. More general recurrence for the actual sublinear Euler setting was already established in A048-A049; this proof supplies the stated independent decay criterion.

## Basin cones

Suppose Lambda is a regular vortical basic backward attractor with open basin D. Use the confirmed basin description: D is invariant under B and the complete Omega flow, is the union of the vortex lines through Lambda, and B cross Omega is nowhere zero in D. Then D minus K maps under S to a nonempty open twisted cone

    {z!=0:pi(z) in Sigma_D},

where Sigma_D is an open Y_t-invariant subset of S2. This follows from the B-equivariance, the vortex-flow conjugacy and the fact that pi is an open submersion. Distinct disjoint basins give disjoint Sigma_D.

The identity DS B=AS and the invertibility of DS show that B and Omega are independent precisely when Az and Omega_tilde(z) are. Since w.Aw=c and Y=G-(G_r/c)Aw, this is equivalent to Y(w)!=0. Hence Y has no zero in Sigma_D.

Every y in D minus K reaches Lambda, and therefore K, at some finite positive or negative vortex time. At the first such contact, continuity gives S->0 and rho->-infinity. The bounded rho speed for X forces the corresponding X time to tend to positive or negative infinity. Therefore for each w in Sigma_D, h_t(w)->-infinity at at least one time end. A periodic Y orbit in Sigma_D cannot have zero total rho gain: otherwise h_t would be bounded at both ends. The set Sigma_D has positive area because it is nonempty and open.

## Basin energy for 2/5<c<1/2

Now assume c>2/5 as well and put alpha=3-2k>0. For any open B-invariant D, not necessarily a hyperbolic basin, let Sigma_D be its scattering angular set. Then

    lim_(R->infinity) R^-alpha integral_(D intersect B_R)|U|^2
      =alpha^-1 integral_(Sigma_D)|F|^2 dA.

To prove this, change variables z=S(y) off null K. The domains |S^-1z|<R are sandwiched between |z|<R-C and |z|<R+C. Uniform tail convergence and the bounded displacement of S give

    U(S^-1z)=V(z)+o(|z|^-k).

The latter displacement estimate follows by rescaling to a fixed annulus and using uniform continuity of V there. Hence the squared-energy error is o(|z|^-2k) at infinity, with bounded contribution on compact z sets. Its integral is o(R^alpha). Twisted polar coordinates give exactly

    integral_(cone intersect B_R)|V|^2
      =(R^alpha/alpha) integral_(Sigma_D)|F|^2.

The fixed-width outer shell contributes O(R^(2-2k))=o(R^alpha), proving the limit without a regularity assumption on the boundary of D.

For a regular vortical basin this constant is strictly positive. If its integral were zero, continuity of F and openness of Sigma_D would make F vanish throughout Sigma_D. Homogeneity would give V=0 on the open cone, hence curl V=Omega_tilde=0 there. Then G and Y would vanish on Sigma_D, contrary to the established nonvanishing. Distinct basin cones are disjoint, so their constants sum to at most alpha^-1||F||_2^2.

The energy formula uses the curl-coupled velocity-tail theorem. It does not use the scalar energy identity, but that alone does not make it a theorem for arbitrary independent bracket models.

## Tail example

For omega=0, choose Y=sin(theta)e_theta and G_r=2cos(theta)/(k-1). Then div_S2 Y=2cos(theta)=(k-1)G_r. The cylinder equations give tan(theta/2)=exp(t-t0) and r=C sech(t-t0)^(2/(k-1)). Every off-axis tail line approaches the singular origin at both X-time ends, in finite original vortex time since d tau/dt=r^(k+2) is integrable. This verifies RemarkV.1's example and its singular-tail qualification.

## Verdict

TheoremV(a)-(d), RemarkV.1, and V.5-V.6 are confirmed with their exact stated hypotheses and the curl-coupling qualification for V.6. No velocity-decay-only proof of the scattering hypothesis or arbitrary-omega nonexistence is supplied.
