# What the complete first-moment family tests

Date: 2026-10-20. Independent audit of the lead's 23:06Z claims (a)-(d), with a separate derivation of the counterexample's angular integral. Status: CONFIRMED as stated below; 19 independent exact arithmetic checks passed at 2026-10-20T23:14:04Z. This is a conditional result, not an exclusion of the primary profile class.

## 1. Precise assumptions and the residual identity

Let ell>1, D=ell-1, A=2ell-1, and a!=0. Let rho,psi,U be a smooth canonical pair on the whole plane with the required parities, rho_y(0)=a, psi_xy(0)=-D, U=o(r), and the sublinear density and gradient bound with exponent gamma in (0,1). No transport equation is assumed in this paragraph. Set

    W=ell X+U,  H=y-rho/a,  phi=psi+Dxy,
    v=(-phi_y,phi_x),  V=v2,  mu=yH,
    B=X.W/r^2,  beta=X.v/r^2,  G=V/y,
    R=W.grad rho-rho.

The quotient G extends smoothly across y=0. Assume H,V=O(r^n) at zero for an integer n>=3. For smooth fields these value bounds imply the corresponding Taylor derivative bounds. At infinity H,V,W=O(r). Define, for 2<m<(n+3)/2,

    I=int mu r^(-2m),  L=int mu omega_x^2 r^(-2m),
    J=int V y r^(-2m),  omega=X/r.

Every integral below is over R2 and uses Lebesgue area measure. The exact residual formula is

    int mu r^(-2m) Phi_m = (1/a) int R y r^(-2m),                 (1)
    Phi_m=a(2m omega_x^2-1)/(2(m-2)) + A+3+G-2m B.              (2)

The plus sign immediately after the fraction in (2) is essential. The source draft mel1/PROOF.md omits that sign in its first displayed definition of Phi_m; its expanded formula (2.6) has the intended value.

To prove (1), direct substitution and Poisson give

    W.grad H-H-V=-R/a,  Delta V=a H_xx,
    B=1+(A-1)omega_x^2+beta.                                  (3)

The test F=y r^(2-2m)/[4(m-1)(m-2)] satisfies

    Delta F=y r^(-2m),
    F_xx=y r^(-2m)(2m omega_x^2-1)/[2(m-2)].

The independently checked compact-cutoff argument in result81, positive_moment_endpoint/PROOF.md, applies to Delta V=a H_xx without transport. Cutoff errors are O(eps^(n+3-2m)+Rout^(4-2m)), using only value bounds on H,V. It yields J=a(2mL-I)/[2(m-2)]. Testing the first equation of (3) gives

    (1/a)int R y r^(-2m)
        =J+int mu r^(-2m)(A+3+G-2mB).

Here div W=2ell and W2=y+V account for A+3=2ell+2. This proves (1). The product mu G is HV, so its integrability does not require a separate global bound on the quotient G. Its local and far radial majorants are r^(2n+1-2m) and r^(3-2m). The other displayed integrals have majorants r^(n+2-2m) and r^(3-2m). No unproved global bound on DU is needed for this cutoff proof.

## 2. Exact content of the all-m family

Put R1(r)=int_0^(2pi) R(r,theta) sin(theta)dtheta. Then (1) has zero left side for every m in the stated interval if and only if R1(r)=0 for every r>0.

Indeed its right side is a^(-1)int_0^infinity R1(r)r^(2-2m)dr. The hypotheses imply R1=O(r^n) at zero and O(r^gamma) at infinity: the latter follows from U=o(r) and the prescribed first-derivative bound on rho. Thus

    M(z)=int_0^infinity R1(r)r^(z-1)dr

is holomorphic on -n<Re z<-gamma. Differentiation under the integral is justified on every compact substrip by bounding logarithmic factors with slightly neighboring powers. The tested real parameters z=3-2m fill the nonempty open interval (-n,-1). Vanishing there implies vanishing on the strip by the identity theorem.

Fix a real z0 in this strip. The function g(t)=R1(exp t)exp(z0 t) is in L1(R). Its Fourier transform is M(z0-i xi), which is zero. Fourier uniqueness can be obtained directly: convolve g with any centered Gaussian approximate identity. Fourier inversion for the Gaussian and Fubini make each convolution zero; convergence to g in L1 then gives g=0 almost everywhere. Continuity of R1 upgrades this to every positive radius. The converse is immediate.

This identifies exactly an angular projection of the residual. It does not establish independence of that projection from the canonical coupling, nor construct a non-profile with this projection identically zero.

## 3. A cancellation parameter

Expanding (2) gives

    Phi_m=C(m)omega_x^2+d(m)+G-2m beta,
    C(m)=am/(m-2)-2m(A-1),
    d(m)=-a/[2(m-2)]+A+3-2m.

Suppose the all-m family vanishes, in particular for an exact profile, and 0<a<(n-1)(A-1). Then m*=2+a/[2(A-1)] belongs to the convergence interval. Substitution gives C(m*)=0 and d(m*)=-a/(A-1), hence

    int mu r^(-2m*) (G-2m* beta)
        =a/(A-1) int mu r^(-2m*).                            (4)

If mu>=0 and is nonzero, the last integral is positive. Thus (4) is a positive weighted compensation condition. The capped-profile theorem already excludes this parameter range under its additional cap hypothesis. No cap or sign for G-2m beta is inferred here.

## 4. Far-field moment and its transport endpoint

For this paragraph assume also rho,U=O(r^p), 0<p<1. Define

    M_s=int rho y r^(-s),  Mx_s=int rho y omega_x^2 r^(-s),
    E_s=int U2 y r^(-s),  Q_s=int rho U.grad(y r^(-s)).

The first three moments converge for p+3<s<4. Near zero their radial majorant is r^(3-s); at infinity it is r^(p+2-s). Test Delta U2=-rho_xx against y r^(2-s), with compact cutoffs. Since

    Delta(y r^(2-s))=(2-s)(4-s)y r^(-s),
    partial_xx(y r^(2-s))=(2-s)y r^(-s)(1-s omega_x^2),

and the cutoff errors are O(eps^(4-s)+Rout^(p+3-s)), one obtains

    (4-s)E_s=s Mx_s-M_s.                                    (5)

For an exact profile with p=1/ell, testing transport gives

    Q_s=ell(s-p-3)M_s.                                     (6)

The sign follows from int R y r^(-s)=ell(s-p-3)M_s-Q_s. The same cutoff orders justify the transport test.

Assume now the far-field expansion rho=r^p Theta0(theta)+O(r^(2p-1)), uniformly in angle. Then

    lim_(s down p+3) (s-p-3)M_s=int Theta0 sin(theta)dtheta.

The contribution of the remainder is bounded at the endpoint because its radial majorant there is r^(p-2). At s=p+3 the integral Q_s itself is absolutely convergent: its radial bounds are r^(-p) at zero and r^(p-2) at infinity. Neighboring exponents give an integrable common majorant, so dominated convergence in (6) proves

    int rho U.grad(y r^(-p-3))
          =ell int_0^(2pi) Theta0(theta)sin(theta)dtheta.     (7)

The expansion and O(r^p) velocity bound are explicit hypotheses here. When applied to exact primary profiles, they are dependencies on the previously verified exterior analysis. No positivity of rho y/a follows from mu>=0 alone.

## 5. A canonical counterexample to sufficiency of the local endpoint

Let ell=2, p=1/2, eta=1/sqrt(6), and a=12+4sqrt(6). Define

    f(r)=(1+r^2)^(-1/4),  chi(r)=r^2/(1+r^2),
    rho=a y f(r)[1-eta y^2/(1+r^2)],  q=rho/(a y).

This is smooth, has the required parities and nonzero slope a, and obeys the sublinear density and derivative bounds. Since 0<eta<1, one has 0<(1-eta)f<=q<=f<=1. The first nonzero part of H=y-rho/a is

    H3=y[(1/4)x^2+(1/4+eta)y^2].

For arbitrary 0<eta<1 the sine density modes of this formula are

    b1=a r f(1-3eta chi/4),  b3=a eta r f chi/4.

The canonical stream is given by the full Green integrals

    psi2=(1/2)[r^2 int_r^infinity b3(t)t^(-2)dt
                         -r^(-2)int_0^r b1(t)t^2 dt],
    psi4=-(1/2)r^(-4)int_0^r b3(t)t^4 dt,
    psi=psi2 sin(2theta)+psi4 sin(4theta).

These are the angular integration-by-parts formulas derived in the separately checked angular inverse. The integrals converge; their local Taylor series are smooth Cartesian harmonic polynomials times power series in r^2. At infinity psi=O(r^(3/2)) with differentiated bounds, hence U=o(r). The parities and Poisson equation hold, and harmonic uniqueness fixes the gauge.

The center formula gives c=-a/4+a eta/2. The chosen a and eta satisfy a=4/(1-2eta), so c=-1=1-ell. The cubic endpoint relation is 6E=(a-2A)B with A=3, B=1/4, E=1/4+eta. It is equivalent to a=12+24eta, also satisfied by the same chosen constants. Thus the example satisfies the local endpoint and the actual canonical center constraint.

It nevertheless fails the whole moment family. Put

    Theta=a sin(theta)(1-eta sin(theta)^2),
    P=(5eta-2)/14,  Q=-eta/44,
    Phi=a[P sin(2theta)+Q sin(4theta)].

Inserting the leading density terms into the convergent Green integrals gives psi=r^(3/2)Phi+O(r^(-1/2)), with differentiated bounds. Therefore the leading velocity is r^(1/2)(-Phi',3Phi/2) in the polar frame. The dilation residual 2r rho_r-rho tends to zero. The limiting first angular residual divided by a^2 is

    int [(1/2)(-Phi'/a)(Theta/a)+(3Phi/(2a))(Theta'/a)]sin(theta)dtheta.

For an independent polynomial evaluation put u=sin(theta)^2. The integrand becomes

    -[P(1-2u)+2Q(1-8u+8u^2)]u(1-eta u)
       +3u(1-u)[P+2Q(1-2u)](1-3eta u).                       (8)

Using int_0^(2pi) u^k dtheta=2pi*binom(2k,k)/4^k and collecting powers of eta gives

    lim_(r->infinity) R1(r)
       =-pi*a^2*(2951eta^2-3344eta+880)/4928
       =pi*a^2*(3344sqrt(6)-8231)/29568 <0.                  (9)

The exact sign follows from 8231^2-6*3344^2=655345>0. Thus R1 is not identically zero and Section2 implies that at least one interior moment identity fails. This proves strict additional information in the whole family, even among canonical smooth one-sided densities with the exact center normalization. It does not show that a non-profile can satisfy the whole family or establish an upper bound on profile slopes.

## Dependencies and verification scope

Result81 supplies the already checked cutoff inverse moment; its short derivation is repeated in Section1. The Mellin uniqueness argument is fully stated here. The explicit example uses the already checked angular canonical Green formula, with the relevant formulas and endpoint bounds given above. The companion exact checker uses rational polynomial arithmetic in u and eta and an independent angular monomial integral. It supports algebraic constants, not the existence of an unknown profile. Every assertion remains invariant under the true spatial scaling because all tests are homogeneous; a and ell are never fixed by that symmetry.
