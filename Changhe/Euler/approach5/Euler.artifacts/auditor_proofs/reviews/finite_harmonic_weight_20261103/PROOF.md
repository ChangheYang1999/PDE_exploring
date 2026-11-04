# Flat continuation with a finite harmonic scalar jet

Status: independently proved at the precise local gradient-equation scope below. All nine sections of LIT219 were read and reconstructed. Read after the exact harmonic-weight review.

## 1. Exact theorem

Let A be a symmetric smooth uniformly positive definite matrix on a planar disk B_R, with A(0)=I. Let S and psi be real smooth functions there. Suppose the first nonzero Taylor term of S is a nonzero homogeneous harmonic polynomial H_l of integer degree l>=1. Fix0<eta<1. Assume, pointwise on the whole disk,

    S div(A grad psi)-eta(A grad S).grad psi=0.             (1.1)

If psi is flat at0, including its value, then psi vanishes on a neighborhood of0. If grad psi is flat, then psi is constant on a neighborhood of0. Constants and the neighborhood can depend on A,S,l,eta. No integrability of the bare weight |S|^(-eta) at0 is assumed, and l eta>=2 is allowed.

The proof retains the full scalar S and matrix A. It needs neither analyticity of S nor an elliptic equation for S. It does require the exact equation(1.1); a first-order drift is not included.

## 2. An explicit nodal-compatible coordinate change

Write H_l(r e(theta))=r^l h(theta), where e(theta)=(cos theta,sin theta). Harmonicity makes h a nonzero sinusoid of frequency l. It has2l simple zeros theta_j. Taylor's integral remainder gives

    r^(-l)S(r e(theta))=h(theta)+r E(r,theta)

with E smooth in (r,theta) down to r=0. The implicit function theorem at the simple zeros gives exactly2l nodal arcs in a small punctured disk; compactness of the complement of their angular neighborhoods excludes any others. Parametrize each arc by outward arclength r as gamma_j(r). Set e_j=e(theta_j), n_j^0=J e_j, n_j(r)=J gamma_j'(r), and q_j(r)=A(gamma_j(r))n_j(r). Then gamma_j=r e_j+O(r^2), gamma_j'=e_j+O(r), q_j=n_j^0+O(r), with differentiated smooth radial remainders.

Choose smooth angular cutoffs chi_j with disjoint supports and equal1 near theta_j. On their supports use the local angular difference theta-theta_j and define

    Phi(r e(theta))=r e(theta)+sum_j chi_j(theta)
      [gamma_j(r)-r e_j+r(theta-theta_j)(q_j(r)-n_j^0)].    (2.1)

The correction is r^2 times a smooth function of (r,theta). Consequently Phi-id=O(r^2), D Phi-I=O(r), and D2 Phi is bounded off0. Extending D Phi continuously by I makes Phi C1,1: integrate the bounded second derivative along segments, splitting at0 if necessary. For a sufficiently small disk ||D Phi-I||<1/2; integration along segments makes Phi injective with a Lipschitz inverse, and the inverse-function theorem off0 plus the derivative at0 makes it a C1,1 diffeomorphism onto its image. It is smooth off0. Its higher derivatives grow at most as fixed negative powers of r.

On the jth ray, exactly

    Phi_r=gamma_j'(r), Phi_theta=r A(gamma_j(r))n_j(r).

Thus the ray maps to the true nodal arc. Since r^(-l)S(Phi(r e(theta)))=h(theta)+r E1(r,theta) and E1 vanishes at every theta_j, division at the simple zeros of h gives

    S(Phi(x))=H_l(x)g(x),
    g=1+O(r)>0, |grad g|<=C.                            (2.2)

Indeed E1/h extends smoothly in (r,theta) across each ray. This also proves that g is Lipschitz at0 and smooth off0. These estimates include derivatives close to the nodal rays; they are not estimates only away from them.

## 3. The transformed equation and separate conormal data

Set u=psi composed with Phi, w=|H_l|^(-eta), and

    M=g^(-eta) det(D Phi)(D Phi)^(-1)
                        A(Phi)(D Phi)^(-T).

Then M is symmetric uniformly elliptic and Lipschitz, is smooth off0, and obeys M(0)=I, |M-I|<=Cr, |DM|<=C. Off the nodal rays, the change of variables in div(|S|^(-eta)A grad psi)=0 gives

    div(w M grad u)=0.                                  (3.1)

Let nu=x/r and tau=Jnu. On each nodal ray,

    tau.M nu=0.                                        (3.2)

To verify this exactly, the old-coordinate gradient of the new angle is normal to gamma_j', hence proportional to n_j. The old-coordinate gradient of the new radius annihilates Phi_theta=r A n_j. Their A-inner product is therefore zero. The positive scalar factors in M preserve that equality. It would generally fail for an arbitrary straightening of the arcs.

At each positive-radius nodal point, grad S is nonzero. Equation(1.1) there gives (A grad psi).grad S=0. Transforming it gives zero conormal flux M grad u across that ray. Since the transformed data are smooth at every such point, its normal component is O(distance to the ray). Multiplication by w thus gives a flux tending separately to zero on each side like distance^(1-eta). There is no reliance on cancellation between adjacent sectors.

Flatness of psi and bounded D Phi imply |u|+|grad u|<=C_N r^N for every integer N, after changing the constants. These estimates ensure that all central integrals below converge, even if the bare weight does not.

## 4. Controlling the angular singularity

Define

    mu=nu.M nu, T=M nu-mu nu, Z=Mx/mu.

Then mu=1+O(r), grad mu is bounded, T is tangent to the circle and O(r), and Z=x+rT/mu. In particular Z.nu=r, Z-x=O(r^2), DZ=I+O(r). At every nodal ray T=0 by(3.2). The Lipschitz bound on M implies |partial_theta T|<=Cr. If d(theta) is distance to the nearest nodal angle, then

    |T|<=Cr d(theta), |h'/h|<=C/d(theta).

Since grad log w=-(l eta/r)nu-(eta/r)(h'/h)tau, these imply

    |T.grad log w|<=C,
    |(Z-x).grad log w|<=Cr.

It follows that

    div(wZ)=(2-l eta+O(r))w,
    |div_circle(wT)|<=Cw.                              (4.1)

The first relation uses the exact homogeneity of w and DZ=I+O(r). The second uses the arclength derivative r^(-1)partial_theta together with the preceding estimates. Both hold with constants uniform up to the removed rays.

## 5. Energy and mass identities with all limiting boundaries

For small r>0 define

    D(r)=integral_(B_r) w grad u.M grad u,
    H(r)=integral_(partial B_r) w mu u^2,
    B(r)=integral_(partial B_r) w (nu.M grad u)^2/mu.

The angular integrals are finite because eta<1. The radial integrals converge by flatness. Integrate(3.1) times u in each sector after removing the center and narrowing the angular sector slightly. At fixed inner radius, all ray terms tend to zero by the separate conormal estimate in Section3. Then let the inner radius tend to zero: its boundary term is bounded by C_N r^(1-l eta+2N), which tends to zero for large N. Thus

    D=integral_(partial B_r) w u nu.M grad u.              (5.1)

The same sequential limits apply below, so constants need only be uniform on each positive-radius annulus for the ray limit. Flatness controls the subsequent central limit.

Differentiating H at positive radius gives

    H'=(1-l eta)H/r+2 integral w mu u u_r+integral w mu_r u^2.

Equation(5.1) and tangential integration by parts give

    D=integral w mu u u_r-(1/2)integral div_circle(wT)u^2.

Its endpoint term wT u^2 tends to zero because T vanishes linearly at each ray and eta<1. By(4.1), bounded mu_r and ellipticity,

    H'=(1-l eta)H/r+2D+E_H, |E_H|<=CH.                 (5.2)

Every displayed circle integral is over the full circle, equivalently the sum over its sectors.

## 6. The exact Rellich calculation

Let e=grad u.M grad u. On each open sector form

    Q=w e Z-2w(Z.grad u)M grad u.

Differentiation and(3.1) give

    div Q=div(wZ)e+w(Z.grad M)_ij u_i u_j
                        -2w M_ij u_j(partial_i Z_k)u_k.

The terms containing D2u cancel by symmetry of M. Since Z=O(r), DM is bounded, DZ=I+O(r), and(4.1) holds, ellipticity yields

    div Q=(-l eta+O(r))w e.                            (6.1)

The radial field Z is tangent to each nodal ray by(3.2). Thus the normal component of the first term of Q is O(distance^(1-eta)) on any compact annulus. The second has the same vanishing by the conormal condition. Both separate ray fluxes vanish. At the center, |Q| is bounded by Cr w|grad u|^2, so its circle flux tends to zero by flatness. All volume terms are integrable for the same reason.

On the outer circle, Z.nu=r and Z.grad u=r(nu.M grad u)/mu. Hence integration of(6.1) gives

    rD'-2rB=-l eta D+E_R, |E_R|<=CrD,
    D'=-(l eta/r)D+2B+E_D, |E_D|<=CD.                 (6.2)

This verifies the coefficient -l eta and its sign, not only a dimensional estimate.

## 7. Frequency and contradiction to flatness

If H(r)=0 at a small radius, positivity of w and mu and continuity imply u=0 on that circle. Equation(5.1) then gives D(r)=0. Ellipticity and continuity of grad u off0 imply grad u=0 throughout the punctured disk, hence u is constant and flatness makes it zero. This proves the theorem in this case.

Otherwise H is positive at every sufficiently small radius. Set N=rD/H>=0. Cauchy-Schwarz in(5.1) gives D^2<=HB. Differentiate using(5.2),(6.2); all homogeneous terms cancel exactly and

    N'=2r(B/H-D^2/H^2)+E_N, |E_N|<=CN.

Thus N'>=-CN and exp(Cr)N(r) is nondecreasing. Fix r0; for0<r<=r0,

    N(r)<=exp(Cr0)N(r0)=N0<infinity.

Equation(5.2) implies H'/H<=(1-l eta+2N0)/r+C. Integrating from r to r0 yields H(r)>=c0 r^(1-l eta+2N0) with c0>0. Flatness, however, gives H(r)<=C_N r^(1-l eta+2N) for every integer N. Taking N>N0 and letting r decrease to zero is a contradiction. Therefore a zero-mass radius must occur, proving local vanishing. Subtracting psi(0) proves the gradient version.

## 8. Scope, dependencies and limits

This proof handles all smooth higher-order terms of S and a smooth symmetric variable matrix with the stated frozen harmonic jet. The coordinate construction, conormal conditions, angular bounds, central limits and frequency identities have all been checked directly. No external unique-continuation theorem or numerical calculation is used.

An additional first-order drift or a non-gradient field is outside this theorem. In particular, the existence of a formal harmonic leading term of an actual Euler scalar does not supply(1.1). An actual-tail reduction must establish the exact potential equation and coefficient class. The unrestricted Euler conclusion remains open. The complete LIT219 source and proof hashes are retained in verification; no formal-source claim is made.
