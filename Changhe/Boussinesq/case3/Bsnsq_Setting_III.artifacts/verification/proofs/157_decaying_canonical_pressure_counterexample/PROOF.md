# A decaying canonical-pressure counterexample to the closed apex equation

Status: CONFIRMED by independent calculation and exact/physical-space controls. The informal proof preceded the controls. Actual Opus5.5 returned no written review in245 or246. This concerns the axis reduction audited in153, not a B2 profile.

## 1. Exact statement and dependencies

Use coordinates x,y, and J(a,b)=(-b,a). Fix a,b,mu,lambda>0 and let

    S(x,z)=xz exp(-a x^2-b z^2),
    Psi_0(x,y)=sqrt(mu) S(x,y/sqrt(mu))
              =xy exp(-a x^2-b y^2/mu).

The initial physical velocity U_0=J grad Psi_0 is smooth and rapidly decaying, and is equivariant under each coordinate reflection. Its canonical anisotropic Euler pressure satisfies

    (partial_xx+mu partial_yy)p_0=2 det Hess Psi_0,         (1)

with the inverse obtained by the linear change z=y/sqrt(mu) from the ordinary whole-plane logarithmic inverse. Its additive constant is fixed by decay at infinity. No harmonic quadratic pressure is added.

Write alpha=sqrt(a),gamma=sqrt(b),t=(alpha-gamma)/(alpha+gamma). Define

    Q_iso=t[2-5 alpha gamma/(alpha+gamma)^2].              (2)

Then the isotropic canonical pressure associated with S has at0

    ptilde_xx=-1-Q_iso/2,
    ptilde_zz=-1+Q_iso/2.                                (3)

Consequently

    (p_0)_yy-(p_0)_xx
       =(-1+Q_iso/2)/mu+1+Q_iso/2.                      (4)

In particular a=4,b=1 gives Q_iso=8/27 and

    (p_0)_xx=-31/27, (p_0)_yy=-23/(27mu).                 (5)

The smooth full-plane Euler solution from these data, after the stated time and coordinate changes, gives a smooth solution of the m=1 system(2.10) of153 with u=0 and v(0)=g(0)=1 at the initial time. At that time

    lambda v_t(0)=-4/27.                                (6)

For mu=3,lambda=2, which are the source's parameters(2.22) at m=1,q=1, the asserted closed apex formula instead gives v_t(0)=1/4, whereas(6) gives -2/27. The omitted pressure anisotropy is70/81. Thus the missing term persists for rapidly decaying initial velocity and the canonical decaying pressure, without a freely added harmonic pressure.

The pressure calculation below is elementary and self-contained. Turning the compatible initial jet into an actual time-dependent solution uses the classical smooth full-plane two-dimensional Euler existence and uniqueness theorem. The source used for that dependency is Theorem1.3 of arXiv2401.06476v1, together with its equations(1.1)-(1.3). For our initial vorticity, all H^s norms and the low-frequency homogeneous H^-1 norm are finite. Only local smooth existence, uniqueness and its canonical velocity are needed, not any blow-up assertion or later microlocal estimate. This standard PDE existence theorem is a named external dependency, not reproved here.

## 2. The canonical pressure and its exact Hessian

First take mu=1. Set X=(x,z),r=|X|,c=cos(theta),d=sin(theta), and

    A(theta)=a c^2+b d^2.

Differentiation of the displayed S gives

    det Hess S = exp(-2a x^2-2b z^2)
      [-1+4a x^2+4b z^2-4a^2 x^4-4b^2 z^4
                +20ab x^2 z^2-8a^2b x^4 z^2-8ab^2 x^2 z^4].    (7)

The Euler pressure equation follows by taking the divergence of U_t+U.gradU=-grad p. For U=J grad S, tr((DU)^2)=-2 det Hess S, so Delta p=2 det Hess S. Its right side is Schwartz. Its integral is zero, as can be checked by integrating the divergence

    det Hess S=partial_x(S_x S_zz)-partial_z(S_x S_xz).

The two first moments vanish by evenness. Therefore the whole-plane potential

    ptilde(X)=(1/(2pi)) int log|X-Y| [2 det Hess S(Y)]dY   (8)

converges, is smooth, solves the pressure equation and tends to0 at infinity. The zero-mass and zero-first-moment conditions remove the logarithmic and dipole terms. These facts fix the stated pressure gauge. A globally harmonic correction decaying at infinity is zero by the harmonic Liouville theorem.

The difference of its two second derivatives has no local delta contribution from the logarithmic Hessian, since that term is proportional to the identity matrix. Its circular principal value is

    Q_iso=(2/pi) PV int [(x^2-z^2)/r^4] det Hess S dx dz.  (9)

This principal value exists. Near0, det Hess S=-1+O(r^2); the constant's angular integral against cos(2theta) vanishes. At infinity the source is rapidly decaying. Subtracting exp(-2r^2) in the radial integral of the constant term is therefore legitimate after angular integration.

For completeness, radial integration of(7) gives, modulo a theta-independent constant,

    int_0^infinity [det Hess S](r,theta) dr/r
       = (1/2)log A + 1/2
                    +(5/2)ab c^2 d^2/A^2.              (10)

Here the regularized constant term is (1/2)log A, using

    int_0^infinity [exp(-2A r^2)-exp(-2r^2)]dr/r
                                  =-(1/2)log A.

The quadratic term contributes1. The quartic terms contribute -1/2+(7/2)ab c^2d^2/A^2 and the sixth-order term contributes -ab c^2d^2/A^2. Thus their sum gives(10). Each nonconstant radial integral is absolutely convergent.

It follows that

    Q_iso=(1/pi)int_0^(2pi) cos(2theta)log A dtheta
        +(5ab/pi)int_0^(2pi) cos(2theta)c^2d^2/A^2 dtheta. (11)

There are two elementary angular integrals. Factoring

    A=((alpha+gamma)^2/4)|1+t exp(2i theta)|^2,

with |t|<1 and taking the uniformly convergent logarithmic Fourier series yields

    int cos(2theta)log A dtheta=2pi t.                  (12)

The substitution tan(theta)=q on a quadrant, followed by partial fractions, gives

    I(a,b)=int_0^(2pi) c^2 d^2/A dtheta
                                  =pi/(alpha+gamma)^2. (13)

The formula also holds when a=b by continuity. Differentiate(13) under the integral, which is allowed since a,b>0. Then

    int cos(2theta)c^2d^2/A^2
       =-partial_a I+partial_b I
       =pi(gamma-alpha)/[alpha gamma(alpha+gamma)^3].   (14)

Substitute(12),(14) in(11) to obtain(2). Finally Delta ptilde(0)=2 det Hess S(0)=-2, so the sum of the Hessian diagonal entries is-2. Their difference is(2), proving(3).

## 3. Anisotropic coordinates and an actual smooth solution

Let u_iso(tau,x,z),ptilde(tau,x,z) be the ordinary two-dimensional Euler solution whose stream at time0 is S. Its initial vorticity Delta S is Schwartz, has zero integral, and gives a Schwartz initial velocity J grad S. In particular it is in H^s for every s and in homogeneous H^-1. The stated standard theorem gives a smooth solution on a nonzero time interval. Uniqueness preserves both velocity reflections. The pressure is determined by the canonical Poisson inverse.

Set L=diag(1,sqrt(mu)), tau=t/lambda, X=L(x,z), and

    U(t,X)=L u_iso(t/lambda,L^-1 X),
    p(t,X)=ptilde(t/lambda,L^-1 X).

The chain rule gives

    div U=0,
    lambda U_t+U.gradU=-diag(1,mu)grad p.               (15)

Its stream is Psi(t,x,y)=sqrt(mu) S_t(x,y/sqrt(mu)), where S_t is the isotropic stream at time t/lambda. The reflection symmetries make the stream odd separately in x,y after fixing its constant. By the smooth Hadamard division formula,

    psi=Psi/(xy), v=Psi_y/x, g=Psi_x/y

extend smoothly and evenly across both axes. They obey

    v=psi+y psi_y, g=psi+x psi_x,
    y g_y-x v_x+g-v=0,
    U=(-x v,y g).                                      (16)

Writing D=lambda partial_t-xv partial_x+yg partial_y, the two components of(15) are exactly

    Dv=v^2+p_x/x, Dg=-g^2-mu p_y/y.                   (17)

With the source's scalar u identically0, its remaining equation Du=(1/2)uv is also satisfied. Thus(16)-(17) provide an actual local smooth solution of all six m=1 equations, with pressure quotients defined by smooth even extension. These steps do not assert that the m=2 system is two-dimensional Euler.

At time0, (1) follows either from divergence of(15) or the coordinate transformation. The determinant of the stream Hessian is unchanged under this transformation: Psi_xx=sqrt(mu)S_xx, Psi_yy=S_zz/sqrt(mu), Psi_xy=S_xz. The canonical inverse in the scaled coordinates yields p_xx=ptilde_xx and p_yy=ptilde_zz/mu, proving(4)-(5).

At the origin the transport velocity is0 and v=g=1. The first equation(17) gives lambda v_t=1+p_xx=-Q_iso/2. This proves(6) for a=4,b=1. The second equation gives the same value lambda g_t=-1-mu p_yy=-Q_iso/2, consistent with g=v at the origin.

## 4. Source comparison and precise scope

The source's closed apex identity at m=1,u=0 is

    lambda(mu+1)v_t=(mu-1)v^2.                         (18)

The correct identity from the full equations is

    lambda(mu+1)v_t=(mu-1)v^2-mu(p_yy-p_xx).             (19)

At a=4,b=1, (5) gives p_yy-p_xx=(31mu-23)/(27mu). The right side of(19) is -4(mu+1)/27, exactly matching(6). For mu=3,lambda=2, (18) instead predicts v_t=1/4. The source's formula mu=m^2(2q+m)/(2q-m^2),lambda=m^2(q+1)/q gives precisely these parameters at m=q=1. The denominator is positive. Thus even this permitted parameter choice does not save the asserted closure.

The example resolves the potential objection that153's explicit polynomial pressure was an unphysical free harmonic choice. Here the initial velocity is rapidly decaying and the canonical decaying pressure is uniquely specified. The pressure anisotropy is a nonlocal functional of that velocity. Reflection does not force it to vanish. The construction still does not supply a B2 profile: its scalar u is zero and it is a time-dependent Euler subclass, with both reflections. It proves nothing about the target B2 existence or nonexistence question.

## 5. Verification plan

The proof above precedes controls. Independently check the determinant, the pressure source, each radial coefficient, the angular identities and the source parameter comparison using exact algebra. Numerically check the full-plane pressure Hessian through the verifier's physical Cartesian Duffy inverse of the explicit Schwartz source, using centered velocity differences and multiple domains, rather than reusing the angular pressure calculation. Retain actual UTC times, failures, code and input hashes. The numerical control is evidence for the derivation, not its proof.

Written UTC 2026-10-21T10:53:14.842841+00:00.

Finalized UTC 2026-10-21T11:05:08.233000+00:00. The first numerical tolerance failed and was retained; refinement passed. See verification/SUMMARY.md for exact scope and evidence.
