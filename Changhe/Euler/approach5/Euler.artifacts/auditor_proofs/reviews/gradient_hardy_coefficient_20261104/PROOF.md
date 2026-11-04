# Independent reconstruction of the critical gradient coefficient

Independent argument and complete coordinator comparison for LIT378, source SHA256 10135e9458e76ed3742d2f716021d49cfd79eb95a0eb35543f3b6d0ea740a80f. Designated verdicts are recorded separately in the auditor's ledger (AUDIT_LEDGER.md). The result concerns a kinematic class and a conditional consequence for Euler profiles.

## 1. Exact statement and evidence scope

Let U belong to C1(R3;R3), with div U=0. Let 0<beta<1 and L>0. Assume

    E(R)=integral_(B_R(0)) |U|^2
        =L R^beta+O(R^(beta-1)) as R tends to infinity.

Set t=(beta-3)/2, k=t+2=(beta+1)/2 and

    H=t^2+2-4beta/(2+k^2)=t^2(k^2+4)/(k^2+2)>0.
    G_a(R)=integral_(1<|x-a|<R) |x-a|^(2-beta)|DU(x)|_F^2 dx.

Here |DU|_F is the full Cartesian Frobenius norm. For every fixed a there is C_a<infinity such that

    G_a(R)>=beta H L log R-C_a,  R>=2.                 (1)

If only E(R)/(LR^beta) tends to 1, then the conclusion is

    liminf G_a(R)/log R >= beta H L.                  (2)

The coefficient is attained, as a logarithmic limit, by a smooth uniformly decaying divergence-free U with E(R)=LR^beta for R>=2. The same field satisfies, for each fixed a,

    E_a(R)=LR^beta+O_a(R^(beta-2)),
    G_a(R)=beta H L log R+O_a(1),                     (3)

and admits a smooth P0 with -Delta P0=tr((DU)^2). No C1 pressure makes this example a full rotating Euler profile for any real c or omega.

All seven source sections, all 47 manual checks and the support note were read. The actual Hamamoto PDF is retained with SHA256 0d9d0b7d1bbe9341880168c9109d18c5abe69ab874f9409046a6b1cc8d48a476. This audit read its extracted pages 1-3 and the start of page 4; rendered pages 2 and 3 were independently inspected. No full-manuscript reading or certification of its other dimensions and weights is claimed here. The local proof below does not import its theorem as a black box. Source acquisition records and snapshots are in the team records.

## 2. Relation to the finite-norm Hardy theorem

Hamamoto's Theorem 1.1 in arXiv:2305.12177v1 concerns smooth solenoidal fields in the finite norm

    integral (|Du|^2+|u|^2/|x|^2)|x|^(2gamma) dx.

Its formulas (1.2)-(1.4), read on the actual pages, give at N=3 and gamma=1-beta/2

    C_(3,gamma)=t^2+min(2,2-4beta/(2+k^2))=H.

The second branch is smaller because beta>0. The source's equality statement in this finite-norm class allows only zero. The fields in the present statement have divergent integral r^(-beta)|U|^2, so that equality statement is not contradicted by (3). Ordinary radial multiplication of U need not preserve divergence freedom. The proof therefore localizes the modal identity itself, and never applies the finite-norm theorem to a nonadmissible field. No novelty of the Hardy constant is asserted.

## 3. Complete vector spherical harmonics and their energies

Write r=|x|, z=log r, n=x/r, U(rn)=r^t v(z,n). Direct differentiation and 2t+3=beta yield

    integral r^(-beta)|U|^2 dx = integral |v|^2 dz dS,
    integral r^(2-beta)|DU|^2 dx
      =integral (|v_z+t v|^2+|nabla_S v|^2) dz dS,      (4)
    (partial_z+k)v_r+div_S v_T=0.                     (5)

The angular derivative in (4) differentiates the Cartesian vector, including the moving basis. By the divergence theorem, integral_(S2) v_r=0 at each radius. This excludes the degree-zero radial flux mode. Hodge decomposition on S2 and scalar spherical harmonics give modes

    v=f(z)Y n+g(z)nabla_S Y+h(z)J_S nabla_S Y,
    integral Y^2=1, -Delta_S Y=Lambda Y,
    Lambda=ell(ell+1), ell>=1,  J_S X=n cross X.

There is no harmonic tangential one-form on S2. Equation (5) is exactly

    g=(f'+kf)/Lambda.                                (6)

For a poloidal mode the squared velocity norm and angular derivative norm are

    K=f^2+Lambda g^2,
    A=(Lambda+2)f^2-4Lambda fg+Lambda^2g^2.             (7)

Indeed the ambient angular derivative has normal part (f-g)nabla_S Y and tangential part fY I+g Hess_S Y. Use integral|nabla_S Y|^2=Lambda, integral Y Delta_S Y=-Lambda, and the integrated Bochner formula integral|Hess_S Y|^2=Lambda(Lambda-1). A toroidal mode has norms Lambda h^2 and Lambda^2h^2: its normal derivative contributes Lambda h^2 and its intrinsic derivative contributes Lambda(Lambda-1)h^2.

All angular cross terms vanish between distinct orthonormal scalar harmonics. Poloidal-toroidal orthogonality also holds for the derivative norm, not merely the velocity norm. The only possible terms are multiples of integral grad Y.J_S grad Z and integral Hess Y:J_S Hess Z. The first is zero by integration by parts and div_S(J_S grad Z)=0. Since J_S is parallel and Ric on S2 is the identity, integrating the second once reduces it to -integral grad Y.J_S grad(Delta_S Z+Z), which is also zero. The trace pairing with Y I is zero pointwise because a symmetric Hessian contracted with J_S has zero trace. This proves the required full modal decomposition of (4).

## 4. Local modal identity and all boundary errors

Let eta>=0 be C2 with compact support in z. Substituting (6), the gradient density of a poloidal mode is

    D=(f'+tf)^2
      +(f''+(k+t)f'+tkf)^2/Lambda
      +(Lambda+2)f^2-4f(f'+kf)+(f'+kf)^2.

Expanding each square and integrating on the finite support of eta gives

    integral eta(D-HK)
      =integral eta[f''^2/Lambda+B_Lambda f'^2+D_Lambda f^2]
       -(k+t)/Lambda integral eta' f'^2
       -[2t+((k+t)tk-Hk)/Lambda] integral eta' f^2
       +tk/Lambda integral eta'' f^2,                 (8)

where

    B_Lambda=2+(k^2+t^2-H)/Lambda,
    D_Lambda=(t^2-H)(1+k^2/Lambda)+Lambda+t^2-2.

For an explicit sign check, the f''f' cross term gives -(k+t)eta' f'^2/Lambda. The 2tk f''f/Lambda term gives -2tk eta f'^2/Lambda+tk eta'' f^2/Lambda. The total original ff' coefficient is 4t+2((k+t)tk-Hk)/Lambda, giving exactly the negative eta' f^2 term in (8). There are no discarded endpoint terms.

Define

    R_Lambda(0)=t^2+Lambda-2beta Lambda/(Lambda+k^2).

Then D_Lambda=(1+k^2/Lambda)(R_Lambda(0)-H), R_2(0)=H, and

    d R_Lambda(0)/d Lambda
      =1-2beta k^2/(Lambda+k^2)^2
      >=1-beta/(2Lambda)>0.

Here k^2/(Lambda+k^2)^2<=1/(4Lambda). Therefore D_Lambda>=0 for all allowed degrees. Since H<=t^2+2,

    B_Lambda>=2-2/Lambda>=1.

The three error integrals in (8) are bounded in absolute value by

    C_beta integral (|eta'|+|eta''|)K,                (9)

uniformly in Lambda. The needed derivative estimate uses (6):

    f'^2/Lambda <=2Lambda g^2+(2k^2/Lambda)f^2
                  <=C_beta K.

Every remaining scalar coefficient is bounded uniformly for Lambda>=2. Thus no pointwise or boundary bound on DU was assumed in controlling the errors.

The toroidal identity is

    integral eta(D_tor-H Lambda h^2)
      =Lambda integral eta[h'^2+(t^2+Lambda-H)h^2]
       -t Lambda integral eta' h^2.

Its bulk terms are nonnegative, since t^2+Lambda-H>=0. Summing the two parts gives

    integral eta (|v_z+t v|^2+|nabla_S v|^2)
      >=H integral eta |v|^2
       -C_beta integral (|eta'|+|eta''|)|v|^2.         (10)

C1 U suffices: f,g,h are C1 on compact z intervals, and (6) makes f C2 there. Prove (8) for finite angular sums. Parseval and the decomposition just proved give convergence in local angular H1 and in L2 of the z derivative. Both sides of (10) pass to the limit on a compact annulus; the error bound is independent of the truncation. No global norm or extra regularity of U is used.

## 5. Energy asymptotics imply the logarithmic bound

Choose eta_R supported in (0,log(2R)), equal to one on [log 2,log R], between zero and one, and with uniformly bounded first two derivatives on the two transition strips. R>=4 suffices. The inner error in (10) is finite. The outer error is at most

    C R^(-beta) E(2R)=O(1).

Thus (4) and (10) give

    G_0(2R)>=H integral_(2<r<R) r^(-beta)|U|^2 dx-C.  (11)

Finite-interval integration by parts, not differentiation of the asymptotic remainder, gives

    integral_(2<r<R) r^(-beta)|U|^2 dx
      =R^(-beta)E(R)-2^(-beta)E(2)
       +beta integral_2^R r^(-beta-1)E(r)dr
      =beta L log R+O(1).                            (12)

The error integrand is O(r^-2). Under just the ratio limit it is o(1/r), whose integral is o(log R); also E(2R)=O(R^beta). Replace R with R/2 in (11). This proves (1) and (2) at the origin, with bounded small radii absorbed in C_0.

For any fixed a, ball inclusions E(R-|a|)<=E_a(R)<=E(R+|a|) imply the same O_a(R^(beta-1)) energy asymptotic, or the same ratio limit. Apply the entire kinematic argument to U(a+.). This is not a translation invariance assertion about the Euler equation.

## 6. Smooth exact-energy attainment

Take Y=sqrt(3/(4pi))cos theta, Lambda=2, K0=1+k^2/2 and b=sqrt(beta L/K0). For a smooth radial f let

    V_f=f(r)Y n+(rf'(r)+2f(r))/2 grad_S Y.             (13)

Its divergence is zero by direct substitution in the spherical divergence formula. A constant f gives the constant vector f sqrt(3/(4pi)) e3. The tail f=br^t has shell energy b^2K0 r^(beta-1).

Let chi_epsilon be a fixed smooth rescaled transition from zero on r<=2-epsilon to one on r>=2, with 0<epsilon<1, and put

    f_epsilon=b[(1-chi_epsilon)2^t+chi_epsilon r^t].

This is constant near the origin, so (13) is globally smooth. The term chi_epsilon'(r)(r^t-2^t) is uniformly bounded on the transition interval. Consequently V_f is uniformly bounded on B2 as epsilon tends to zero. Away from that shrinking interval V_f is the constant b2^t sqrt(3/(4pi))e3. Dominated convergence gives

    integral_(B2)|V_f|^2 --> b^2 2^beta.

The target L2^beta=b^2(K0/beta)2^beta is strictly larger, since K0>1>beta. Fix sufficiently small epsilon, so the deficit D0 is positive. Let eta0 be smooth radial, one near zero and zero for r>=1/2. Put W=eta0(r)Jy, where J generates rotations about e3, and I0=integral|W|^2>0. W is divergence-free and pointwise orthogonal to the poloidal V_f. Then

    U=V_f+a0 W,  a0=sqrt(D0/I0)>0                    (14)

has exact energy L2^beta inside B2. The tail shell energy integrates to E(R)=LR^beta for every R>=2. Since t<0 the field decays uniformly. The constant logarithmic poloidal mode with Lambda=2 has f=b, g=kb/2 and quotient D/K=H. Therefore

    integral_(S2)|DU(rn)|^2 dS=beta H L r^(beta-5),

and G_0(R)=beta H L log R+O(1).

The poloidal vector in (13) is even under x to -x; W is odd, and their cross term is zero. Thus rho=|U|^2 is even. For F_R(s)=integral_(B_R(sa))rho, F_R'(0)=0 and

    F_R''(s)=integral_(boundary B_R(sa))
                     (a.grad rho)(a.n) dS
             =O_a(R^(beta-2))

for large R, uniformly in s in [0,1]. Here only the homogeneous tail meets the boundary and grad rho=O(R^(beta-4)). Taylor's formula proves the first assertion in (3). On large |x|,

    abs(|DU(a+x)|^2-|DU(x)|^2)<=C_a |x|^(beta-6).

After multiplying by the critical weight and integrating the angular measure, this has radial bound C_a r^-2. The finite inner pieces are harmless. The second assertion in (3) follows at every fixed center for this same field.

## 7. Poisson pressure, arbitrary rotation, and the remaining open step

Let N(x)=1/(4pi|x|), so -Delta N=delta_0. Define P0=sum_(i,j)(partial_i partial_j N)*(U_iU_j), including the distributional local term -(1/3)|U|^2 and the principal value part. Locally the smooth tensor can be cut off and the Hessian singularity handled by its angular cancellation. At infinity a dyadic annulus contributes at most C R^-3 E_y(2R)=O(R^(beta-3)), a summable sequence. Derivatives of the separated tail kernel decay still faster, so compact localization proves P0 is smooth. Truncate the tensor and pass to distributions to obtain

    -Delta P0=partial_i partial_j(U_iU_j)=tr((DU)^2).

This q is the signed trace of the square, not the squared Frobenius norm.

Near zero (14) is U=d e3+My, where d=b2^t sqrt(3/(4pi)), M=a0J and a0>0. For every real c and omega its momentum without pressure is exactly

    (1-c)U+(((cI-omega J)y+U).grad)U+omega JU
       =(1-c)d e3+(M+M^2)y.

The commutators vanish since M=a0J and J e3=0. The curl is 2a0e3, while any C1 pressure gradient has zero distributional curl. Thus no pressure and no harmonic adjustment of P0 can turn this control into a full Euler profile.

Here the full profile system is

    (1-c)U+(((cI-omega J)y+U).grad)U+omega JU+grad P=0,
    div U=0, J(y1,y2,y3)=(-y2,y1,0),

and Hb means U(R.) tends to zero in distributions as R tends to infinity. For a nonzero bounded C1 full profile with C1 pressure and Hb, at 2/5<c<1/2, the independently confirmed energy theorem A3053 gives the premise with beta=5-2/c. The present lower bound is then necessary for every finite omega and fixed center, with weight 2-beta=2/c-3. Decaying C2 target profiles satisfy the previously confirmed Hb implication. Finite critical gradient integral, or a logarithmic liminf strictly smaller than beta H L, would exclude such a profile. Neither additional premise is established by velocity decay or by this proof. Even the separately conditional natural derivative rate O(r^(-1/c)) gives the critical radial upper majorant r^-1, not finite integral. Optimality in the full Euler class, automatic improved derivative control, and the main arbitrary-rotation conjecture remain open.


## 8. Coordinator comparison and quantitative derivative necessity

The complete coordinator comparison, retained as
in the team records, was written from the source
before the coordinator read this reconstruction. Its eleven checks agree
with Sections 1-7. The coordinator read only rendered pages 2 and 3 of the
Hamamoto paper and did not recheck the Poisson argument in detail; those
limits are retained. The local Poisson construction is independently
justified in Section 7. No symbolic script, parameter grid or sphere
quadrature in that comparison is used as a mathematical proof here.

For its W1, put m=2-beta, D=beta^2+2beta+9. The improvement over the
source-based coefficient k_beta=beta m(1-beta) follows analytically from

    H-m(1-beta)=3(3-beta)(beta+1)/4-16beta/D.

For 0<beta<1, (3-beta)(beta+1)=3+2beta-beta^2>=3 and
D-12beta=(1-beta)(9-beta)>=0. Thus

    H-m(1-beta)>=9/4-4/3=11/12>0,
    beta H>k_beta.

The inequality is merely a convenient strict bound, not a claim about
the best gap. As beta tends to zero, H tends to 17/4 and m(1-beta)
tends to 2, so beta H/k_beta tends to 17/8. This comparison involves
no grid or numerical extrapolation.

For W2, first work in the kinematic class of Section 1, even with only
the energy ratio limit. If for all sufficiently large |y| one has

    |DU(y)|_F<=D0 |y|^(-(5-beta)/2),

then, in spherical coordinates and with the sphere's area equal to 4pi,

    G_0(R)<=C+4pi D0^2 log R.

The exponent is exactly -1 after inserting the weight r^(2-beta),
the squared derivative bound r^(-(5-beta)), and the radial Jacobian r^2.
Combining this upper bound with (2) gives

    4pi D0^2>=beta H L.                               (15)

More generally, define the extended nonnegative number

    D_infinity=limsup_(|y| to infinity)
                       |y|^((5-beta)/2)|DU(y)|_F.

If it is infinite, the inequality below is automatic. If it is finite,
for every D0>D_infinity the displayed pointwise upper bound holds
outside a sufficiently large ball. Apply (15) and let D0 decrease to
D_infinity. Therefore every field in this kinematic class satisfies

    D_infinity>=sqrt(beta H L/(4pi))>0.               (16)

For the full profiles of Section 7, beta=5-2/c, so (16) becomes

    limsup_(|y| to infinity)|y|^(1/c)|DU(y)|_F
                      >=sqrt((5-2/c)H_(5-2/c)L/(4pi))>0.  (17)

This is uniform in the sense of validity for every finite omega, with
no restriction to axisymmetric or small-amplitude profiles. The number
L belongs to the particular profile. In particular, the additional
condition DU=o(r^(-1/c)) forces U=0 in the bounded Hb class for
2/5<c<1/2. No finite derivative upper bound is assumed in (17) itself.
It is a limsup statement over all distant points, not a pointwise lower
bound in every direction or on every sphere.

The earlier A3102 theorem has separate hypotheses: U is C2, P is C1,
U is a bounded full profile with Hb, and DU=o(r^(1/2)). It supplies
|DU|<=C(1+r)^(-1/c). For a nonzero such profile, (17) makes its natural
weighted derivative limsup finite and strictly positive. This does not
remove A3102's additional growth hypothesis or prove that arbitrary
velocity decay controls derivatives.

W3 asks that the modal limit and fixed inner transition be explicit.
They already are: the degree blocks are orthogonal for the angular
energy and dense in local H1, while the divergence constraint makes f
C2 from C1 modal coefficients. The inner transition of eta_R can be one
fixed function of z on (0,log 2), with the outer transition its translate
on (log R,log(2R)). Thus its error is independent of R. These facts
justify the passage to all modes, rather than only a finite truncation.
