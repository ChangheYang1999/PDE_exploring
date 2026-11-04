# An explicit gap below the quarter-pressure coefficient

Status: independent reconstruction and full existing coordinator comparison complete. The designated verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md). No numerical bound is used as a proof.

## 1. Statement and conventions

Let gamma0=2499/10000. On an open ball B_R centered at zero in R3, let V be C3 and P be C4, with

    div V=0, -Delta P=tr((DV)^2),
    V(0)=DV(0)=P(0)=0, P>=gamma0|V|^2.

The pressure equation may be distributional. Then V=P=0 on the entire ball. All these are kinematic Poisson assumptions. Their applicability to an arbitrary rotating Euler profile is not asserted.

The key polynomial assertion is that no nonzero homogeneous quadratic divergence-free Q and homogeneous quartic R satisfy the same Poisson relation with R>=gamma0|Q|^2 everywhere. Brackets denote normalized sphere integrals and ||.||2 their L2 norm; derivative matrix norms are Frobenius norms. The polynomial assertion, combined with compact attainment in the separately reconstructed LIT318 theorem, gives Gamma2<gamma0. It is an upper bound, not an optimality statement.

## 2. Explicit sphere estimates

The restrictions of scalar quadratics to S2 are the orthogonal harmonic degrees 0 and 2, with total dimension 6. The quartic restrictions are degrees 0, 2 and 4, with total dimension 15. These decompositions follow by subtracting radial multiples of lower-degree polynomials: Delta(r^2 h_l)=(4l+6)h_l for harmonic h_l, and Delta r^4=20r^2. The Laplacian is therefore onto the lower-degree space in these degrees; the kernel dimensions are 1,5,9. The polar Laplacian gives sphere eigenvalues -l(l+1), and integration by parts proves orthogonality.

For any rotation-invariant space of dimension d with orthonormal basis phi_i, its reproducing kernel K(n,m)=sum phi_i(n)phi_i(m) has K(n,n)=d. Indeed rotations make this diagonal constant, and its integral is d. Cauchy-Schwarz gives |K(n,m)|<=d and

    ||p||infinity<=sqrt(d)||p||2.

For nonnegative p the reproduction formula gives ||p||infinity<=d<p>, and therefore ||p||2<=sqrt(d)<p>. For a homogeneous quartic D, its Laplacian on the three orthogonal sphere components has factors 20,14,0. Consequently

    ||Delta D||2<=20||D||2.                            (2)

For a quadratic vector polynomial A, componentwise application gives ||A||infinity<=sqrt(6)||A||2. Write A_i=x^T M_i x with M_i symmetric. Sphere fourth moments yield

    ||A||2^2=sum_i[(tr M_i)^2+2|M_i|^2]/15.

Since DA_i=2M_i x and Delta A_i=2 tr M_i, on S2

    |DA|<=sqrt(30)||A||2, |Delta A|<=sqrt(90)||A||2.    (3)

## 3. A controlled polarization of the pressure residual

Define

    Rcal(A)=tr((DA)^2)+Delta|A|^2/4,
    Bcal(A,C)=tr(DA DC)+(DA:DC)/2
                        +(A.Delta C+C.Delta A)/4.

The second expression is symmetric and bilinear, with Bcal(A,A)=Rcal(A). The product identity for the Laplacian gives the displayed formulas. The pointwise bounds in Section 2 imply

    ||Bcal(A,C)||2
      <=(45+3sqrt(15))||A||2||C||2
      <57||A||2||C||2.                               (4)

Here the three contributions are respectively 30, 15 and 3sqrt(15). The estimate first holds pointwise and then in the normalized L2 norm. It needs no divergence assumption.

## 4. Orthogonal tangential decomposition

For divergence-free homogeneous quadratic Q, put H=x.Q and write H=H3+r^2 ell, with H3 harmonic cubic and ell=Delta H/10 linear. Define

    N=grad H/3+r^2 grad Delta H/6-x Delta H/6,
    T=Q-N.

Euler's identity gives x.N=H. Since Delta H is linear, direct divergence gives div N=Delta H/3+2Delta H/6-4Delta H/6=0. Thus x.T=0 and div T=0.

Writing ell=a.x, the two parts of N are N3=grad H3/3 and N1=2r^2 a-x(a.x). On the sphere the radial and tangential derivatives of H3 have squared means 9||H3||2^2 and 12||H3||2^2, so

    ||N3||2^2=(7/3)||H3||2^2,
    ||N1||2^2=9||ell||2^2.

Their scalar product is zero: each component of grad H3 is harmonic quadratic and has zero sphere mean, while <H3 ell>=0. Therefore, with v=<H^2>,

    ||N||2^2<=9v.                                    (5)

Also <T.N>=0. Tangency and divergence freedom give zero sphere divergence for T, so integration by parts annihilates <T.grad H>. The x Delta H term is pointwise orthogonal. Finally <T>=0: integrate div(x_j T)=T_j over the unit ball; its boundary flux is zero by tangency, and homogeneity makes its volume integral a nonzero fixed multiple of its sphere mean. This annihilates the remaining constant vector grad Delta H. Hence

    ||T||2^2=||Q||2^2-||N||2^2.                       (6)

## 5. Exact tangential residual norm

Differentiating x.T=0 and using homogeneity gives x cross curl T=-3T. Thus T=x cross Mx for a real matrix M. Divergence freedom implies curl(Mx)=0, so M is symmetric. An oriented orthonormal eigenbasis gives

    T=(a yz,b xz,d xy), a+b+d=0.

Set s=a^2+b^2+d^2. Direct differentiation and sphere moments give

    ||T||2^2=s/15,
    Rcal(T)=k1 x^2+k2 y^2+k3 z^2,
    k_i=(3a_i^2-s)/2, (a_1,a_2,a_3)=(a,b,d).

The relation a+b+d=0 implies sum a_i^4=s^2/2, so sum k_i=0 and sum k_i^2=3s^2/8. For this trace-free quadratic, its squared sphere norm is 2 sum k_i^2/15=s^2/20. Therefore

    ||Rcal(T)||2=(3sqrt(5)/2)||T||2^2.                (7)

No compactness lower bound or approximate coefficient is used.

## 6. Contradiction at the explicit coefficient

Suppose a nonzero polynomial pair exists and normalize <|Q|^2>=1 by scaling Q and R together. Let epsilon=1/4-gamma0=1/10000, E=|Q|^2, v=<(Q.n)^2> and D=R-gamma0 E>=0.

For the polynomial stress Q tensor Q+R I, double divergence is zero and its flux through a centered sphere has no center source. Tangential integration by parts gives r A'=e-3v(r), where A=v(r)+<R(rn)>. Homogeneity then gives

    <R>=(1-7v)/4,
    0<=<D>=epsilon-7v/4<=epsilon,
    v<=4epsilon/7.                                  (8)

Since D is nonnegative quartic, ||D||2<=sqrt(15)epsilon. Since ||Q||infinity^2<=6 and <E>=1, ||E||2<=sqrt(6). The Poisson relation yields Rcal(Q)=Delta(epsilon E-D), and (2) gives

    ||Rcal(Q)||2<140epsilon.                         (9)

Equations (5)-(6) imply ||N||2<=6sqrt(epsilon/7)<(5/2)sqrt(epsilon), ||T||2^2>=1-36epsilon/7 and ||Q+T||2<=2. Since Q-T=N, polarization gives

    ||Rcal(T)||2
      <=||Rcal(Q)||2+||Bcal(N,Q+T)||2
      <140epsilon+285sqrt(epsilon).

But (7) gives ||Rcal(T)||2>=3(1-36epsilon/7). At epsilon=1/10000, these would imply

    3-108/70000 < 358/125.

The reverse strict inequality holds: their difference is 2353/17500>0. This is the contradiction. All larger pressure coefficients also imply the excluded gamma0 inequality. Compact attainment of Gamma2 therefore makes its upper bound strict.

## 7. From Taylor jets to vanishing on the whole ball

For the stated V,P, the pressure is nonnegative and zero at the center. Its linear term vanishes. Its quadratic term is nonnegative and harmonic because DV(0)=0 and the Poisson equation. Its positive semidefinite Hessian has zero trace, so this term vanishes. The cubic term is then nonnegative and odd, hence zero as well. The C3/C4 expansions give

    V=Q+O(r^3), P=R4+o(r^4),
    div Q=0, -Delta R4=tr((DQ)^2), R4>=gamma0|Q|^2.

Section 6 implies Q=0. Thus V=O(r^3), and e,v=O(r^6). For the actual stress V tensor V+P I the same full-ball flux identity holds. Since P(0)=0,

    A(r)=integral_0^r[e(s)-3v(s)]ds/s=O(r^6).

On every radius A=v+pbar>=gamma0 e>=0 and A'<=A/(gamma0 r). Therefore r^(-1/gamma0)A is nonnegative and nonincreasing. Its center limit is zero because 1/gamma0<6. It vanishes at every radius, so e=0 and V=0 throughout the ball. Finally P>=0 and its sphere means vanish, forcing P=0 by continuity. This uses the lower bound on the whole ball, not a continuation theorem from a germ.

## 8. Scope and verification boundary

The quadratic exclusion and whole-ball theorem are independent of any numerical search. The explicit coefficient is conservative. They do not decide Gamma2<=1/6, produce a profile, or derive the pressure bound at an actual Euler tail. The strict bound on the attained Gamma2 additionally uses the fully reconstructed compactness argument of LIT318. No mathematical computation, formal build, new client or agent was used. The completed existing configured model comparison is recorded in Section 9; actual provider runtime remains independently unattested.

## 9. Completed coordinator comparison

All seven items of in the team records and the entire shared in the team records were read. They agree with Sections 1-8. In particular the sphere estimates are proved for every admissible polynomial, not inferred from the sampled matrices in the log; the tangential residual identity and the rational contradiction are exact. Compact attainment, already confirmed in A2699, is the reason the upper bound on Gamma2 is strict. The Taylor argument uses C3 velocity, C4 pressure, the center normalization and the pointwise inequality on the entire ball. It supplies no such inequality for an arbitrary profile.

The existing coordinator is configured as model; its actual provider runtime remains independently unattested. The shared symbolic and sampling log is corroboration and was not rerun. No computation or new client was used in this audit. No disagreement remained after comparing every item.
