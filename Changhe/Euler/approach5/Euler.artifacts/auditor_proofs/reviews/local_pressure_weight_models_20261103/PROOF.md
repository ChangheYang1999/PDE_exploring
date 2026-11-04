# Two exact local countertests: pressure sign and a degenerate weight

Status: independent proof and scope audit of LIT203 and LIT204. The displayed models are confirmed at their stated local or reduced scope. Neither is a decaying rotating similarity profile or an actual scattering tail.

## 1. Polynomial stationary Euler fields with nonnegative pressure

Let n>=1 be an integer, r^2=x^2+y^2 and J(x,y,z)=(-y,x,0). Define on R3

    v=r^(2n) Jx,
    pi=r^(4n+2)/(4n+2),
    s=pi-|v|^2/2=-n|v|^2/(2n+1).                 (1)

All powers in (1) are polynomials in x and y. Then

    div v=0, (v.grad)v+grad pi=0,
    -Delta pi=tr((Dv)^2), v.curl v=0.             (2)

Every point on the z-axis has

    v=Dv=curl v=pi=grad pi=D2pi=0,

and belongs to the support of curl v. Nevertheless pi>=0 everywhere. For every real epsilon<1/4, every off-axis point satisfies s<-epsilon|v|^2.

To prove this, Jx.grad annihilates r, div Jx=0 and D(Jx)Jx=J^2x=-(x,y,0). Therefore div v=0 and (v.grad)v=-r^(4n)(x,y,0). Direct differentiation gives grad pi=r^(4n)(x,y,0). Taking the divergence of this stationary equation and expanding div((v.grad)v) gives tr((Dv)^2), proving the pressure identity. Independently,

    curl v=(0,0,(2n+2)r^(2n)),

which is perpendicular to v and nonzero exactly off the axis. The transverse polynomial orders of v and pi are 2n+1>=3 and 4n+2>=6. They give all the asserted jets. Finally |v|^2=r^(4n+2) and n/(2n+1)>=1/3>1/4 prove the deficit and sign claims.

The normalization pi=0 on the axis is fixed; no additive pressure shift is used. This disproves the local inference from a negative Bernoulli deficit and the pressure Poisson equation to negative pressure, even with a supported flat zero and zero helicity. It does not decide the stronger statement for an actual negative-homogeneous tail.

## 2. No pressure makes this a rotating similarity profile

For any c>0 and finite real omega, consider the rotating similarity expression

    (1-c)v+Dv((cI-omega J)x+v)+omega Jv+grad pi.

The polynomial has ordinary degree 2n+1, so Dv x=(2n+1)v. Equivariance v(exp(tJ)x)=exp(tJ)v(x) gives Dv(Jx)=Jv. The stationary nonlinear terms cancel, as do the rotation terms. The residual is exactly

    (1+2nc)v.                                    (3)

If a different C1 pressure P canceled it on an open set meeting the off-axis region, then grad(P-pi)=-(1+2nc)v. The distributional curl of a gradient is zero, contradicting the explicit nonzero curl v and 1+2nc>0. Thus this velocity cannot solve the target equation with any pressure. It grows like r^(2n+1), also violating the decay condition. The construction is solely an exact test of a local inference.

## 3. A smooth planar model at a regular scalar interface

Let c>0, a>0, b>a, eta=a/b in (0,1), and q=1/eta. Work on the oriented (t,s) plane with R(t,s)=(-s,t). Define

    h=s, psi=t^3-3t s^2/(1-eta),
    F=grad psi, Y=(c/a)RF, rho=(div F)/a.          (4)

Then, globally on the plane,

    F=-(a/c)RY, div Y=0, div F=a rho,
    F.grad h=b rho h.                            (5)

Indeed the components and divergence are

    F=(3t^2-3s^2/(1-eta), -6ts/(1-eta)),
    div F=-6eta t/(1-eta),
    rho=-6eta t/[a(1-eta)].                       (6)

The first identity follows from R^2=-I. Rotating a gradient gives a divergence-free field. Since q eta=1, b rho s=q s div F=-6ts/(1-eta)=F.grad h. The scalar h has nonzero gradient everywhere, while rho(0)=0 and partial_t rho!=0.

## 4. The full weighted weak equation has no interface charge

The polynomial psi satisfies on the whole plane, in distributions,

    div(|s|^(-eta) grad psi)=0.                   (7)

For s!=0 this is Delta psi-eta psi_s/s=0, verified using (6). On a compact set, psi and grad psi are bounded and the weight is integrable because eta<1; hence both have finite weighted L2 norm. Smooth cutoff polynomials belong to the corresponding local weighted Sobolev space directly.

For a compactly supported smooth test function, integrate by parts over s>delta and s<-delta. The interface normal flux is controlled by

    |s|^(-eta)psi_s=-6t sign(s)|s|^(1-eta)/(1-eta).

It tends uniformly to zero on bounded t intervals. All interior integrals converge by weighted integrability, so the interface boundary term disappears as delta tends to zero. This proves (7) across the line, with no delta measure there. It is stronger than solving the equation separately on the two half-planes.

## 5. An isolated finite-order flat zero with negative index

The second component in (6) vanishes only when t=0 or s=0. In either case the first component vanishes only at the origin. Thus F has exactly one zero, and its homogeneous quadratic components give DF(0)=0. The same holds for Y.

Use the positive coordinate scaling z=s/sqrt(1-eta). Up to a positive constant and a positive diagonal scaling of vector components, F becomes

    (t^2-z^2,-2tz).

The coordinate scaling preserves orientation. A positive diagonal output matrix is homotopic to the identity through invertible matrices and cannot introduce a zero on a surrounding loop. Thus neither operation changes the index. The resulting complex vector is (t-iz)^2, with winding number -2 on a positively oriented circle. A fixed rotation and positive multiplication preserve this number, so both F and Y have index -2.

This is a finite-order flat gradient zero on the regular scalar level h=0. It is consistent with strong unique continuation, which excludes certain infinite-order vanishings of the scalar solution, not a cubic polynomial with a quadratic gradient zero. The example supplies no positive-index zero.

## 6. A weak solution that fails the needed vector regularity

The function psi_o=s|s|^eta also solves (7) weakly. Its classical first derivative is continuous, and

    grad psi_o=(0,(1+eta)|s|^eta),
    |s|^(-eta)grad psi_o=(0,1+eta)

almost everywhere. The latter has zero distributional divergence. The weighted square gradient is proportional to |s|^eta, locally integrable; the weighted square function is proportional to |s|^(2+eta), likewise integrable.

The vector grad psi_o vanishes along the whole interface. Its difference quotient in the s direction has magnitude proportional to |s|^(eta-1), which is unbounded. It is not C1 there. The actual open-zero tail argument has a C^(1,alpha) projected vector field through F=-(a/c)RY. Therefore this weak example is excluded by that regularity premise. Weak solvability alone cannot replace the stronger vector regularity in an isolation argument.

## 7. Exact limitations and dependencies

The second construction verifies only a flat Euclidean conservation pair and its weighted potential equation. It omits the sphere metric, negative radial and twisted homogeneity, the full relation W=curl V, the three-dimensional pressure equation, and realization by a global original profile. It cannot prove the existence of a corresponding full Euler tail germ. Conversely it refutes any claim that the reduced weighted equation alone forbids a finite-order flat zero at a regular interface.

Both constructions are elementary and were checked by direct differentiation, distributional integration and a winding-number argument. No numerical computation, literature theorem, formal build, characteristic-flow completeness assumption or pressure normalization at infinity is used. The cited Sire-Terracini-Tortone context in the source is not a dependency of these proofs and is not independently re-audited here.

The pressure-sign issue arose in the existing configured-model coordinator comparison CO49; the exact countertest is an independent response. A focused follow-up acknowledging the correction remains pending. The LIT203-LIT204 sources are from the existing the external referee (a second model) agent. No substitute model invocation is claimed.

## 8. Sources and verification

- LIT203: in the team records, all five sections read; exact snapshot in the team records.
- LIT204: in the team records, all six sections read; exact snapshot in the team records.
- Earlier pressure-sign audit A1081-A1082: in the team records, Section9.

Source hashes and a full post-read record are retained separately.
