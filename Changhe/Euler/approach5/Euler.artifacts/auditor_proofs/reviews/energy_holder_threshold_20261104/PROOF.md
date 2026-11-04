# Local Holder growth, velocity norms and the weak endpoint

Status: independently reconstructed and compared with the existing theory agent. Exact designated verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md). The main theorem and sharpness examples are kinematic. They do not settle the unrestricted rotating Euler problem.

## 1. Exact hypotheses and conclusions

Let V:R3->R3 be continuous and suppose

    E(R)=integral_(B_R)|V|^2=L R^beta+O(R^(beta-1)),
    L>0, 0<beta<1.

For 0<alpha<=1 suppose that, outside a fixed ball,

    [V]_(alpha;B2(y))<=K(1+|y|)^kappa,
    0<=kappa<alpha(1-beta)/3.

The seminorm is the supremum of |V(x)-V(z)|/|x-z|^alpha over distinct
points of the indicated ball. Define

    sigma=[alpha(1-beta)-3kappa]/(2alpha+3)>0,
    p_star=2+beta/sigma>2.

Then |V(y)|<=C(1+|y|)^(-sigma), V is bounded, and V belongs to Lp for
every p>p_star. In fact V belongs to weak L^(p_star), meaning
sup_(lambda>0) lambda^(p_star)|{|V|>lambda}|<infinity. This endpoint
conclusion is proved separately in Section3; the source makes no claim
about it. Neither divergence freedom nor an a priori bound on V enters.

There are smooth divergence-free uniformly decaying fields with this
energy law at every fixed center, satisfying the local seminorm bound,
but in no strong Lp for p<=p_star and in no weak Lp for p<p_star. Thus
the strong threshold is exact within these hypotheses, and the weak
endpoint does hold. At kappa=alpha(1-beta)/3 a logarithmically improved
seminorm growth bound still permits failure of every finite strong and
weak Lp norm. Each constructed field has a smooth Poisson pressure but
fails full rotating Euler for every real c and omega.

## 2. Local amplitude bound without assuming bounded velocity

Subtract the actual energy values at R+1 and R-1. The difference of the
leading terms and both remainder values are O(R^(beta-1)). Hence

    integral_(R-1<|x|<R+1)|V|^2<=C_E R^(beta-1),          (1)

which tends to zero. No asymptotic derivative is taken.

Fix |y|=R large and delta=|V(y)|. Choose H_R=C_H R^kappa>=1 bounding
the seminorm on B2(y). If delta>=2H_R, all of B1(y) has |V|>=delta/2,
so its energy is at least (pi/3)delta^2>=4pi/3, contradicting(1).
Thus delta<2H_R for all sufficiently large R.

For delta>0 put rho=(delta/(2H_R))^(1/alpha)<1. On B_rho(y), the
seminorm bound gives |V|>=delta/2. The ball lies in the shell of(1),
up to boundaries of measure zero. Its volume yields

    (pi/3)delta^2(delta/(2H_R))^(3/alpha)
        <=C_E R^(beta-1).

Solving for delta gives delta<=C R^(-sigma). The case delta=0 is
immediate. Continuity on the remaining compact ball now proves global
boundedness and the stated global decay estimate. At alpha=1 an
exterior bound |DV|<=C(1+|y|)^kappa supplies this local Lipschitz
hypothesis, because a line segment in B2(y) remains there and its points
have comparable large radius.

## 3. Strong norms and a universal weak endpoint

For p>2, the unit shell n<=|y|<n+1 has

    integral |V|^p<=C n^(-sigma(p-2)) n^(beta-1).

The shell energy bound follows from(1) with a slightly shifted center
radius. The series converges if beta-1-sigma(p-2)<-1, exactly p>p_star.
The compact part is finite by continuity. A ratio limit for E alone
would not supply the small shell energy used here.

For the endpoint choose global constants C0,C1 such that
|V(y)|<=C0(1+|y|)^(-sigma) and E(R)<=C1(1+R)^beta for all R>=0.
For 0<lambda<C0, the superlevel set lies in a ball of radius at most
R_lambda=(C0/lambda)^(1/sigma). Chebyshev's inequality on this finite
ball gives

    |{|V|>lambda}|<=lambda^(-2)E(R_lambda)
       <=C lambda^(-2-beta/sigma)=C lambda^(-p_star).

For lambda>=C0 the set is empty after increasing C0 if necessary.
This proves weak L^(p_star). It does not prove strong membership at the
endpoint. The construction below makes the distinction exact.

## 4. Smooth baseline, bumps and exact compensation

Write J(x1,x2,z)=(-x2,x1,0), K0=8pi/3, s=(beta-5)/2 and
b=sqrt(beta L/K0). Choose a smooth scalar chi0 between0 and1, zero on
r<=1 and one on r>=2. Add a suitable multiple t0 of a nonzero smooth
bump zeta supported in(1/4,1/2), and set

    f0(r)=b chi0(r)r^s+t0 zeta(r),  V0=f0(r)Jy.

The energy density in the radial integral is K0 r^4 f0(r)^2. The cut
tail contributes at most L(2^beta-1) inside B2, strictly less than
L2^beta. The two scalar supports are disjoint, so choose the unique
positive t0 making the missing energy exact. Consequently

    E0(R)=L R^beta for R>=2,
    T0(r)=E0'(r)=beta L r^(beta-1) for r>=2.

Take psi(t)=exp(-1/(1-t)) for t<1, extended by zero for t>=1. Then

    W=curl[psi(|x|^2)Jx]
      =(-2x1 x3 psi',-2x2 x3 psi',2psi+2(x1^2+x2^2)psi')

is smooth, compactly supported, divergence-free and satisfies W.Jx=0.
It is nonzero at0. Let K2=integral|W|^2>0, and fix a ball D0 inside B1
with |W|>=m0>0 on D0.

Choose a nonnegative smooth chi supported in(0,1), integral chi=1,
and 0<eta<=beta L/(4sup chi). Put Rn=10n for n>=n0. In the subcritical
case take

    an=Rn^(-sigma), en=eta Rn^(beta-1),
    epsilon_n=(en/(K2 an^2))^(1/3).

Since 2sigma<1-beta, epsilon_n tends to zero. Choose n0 large enough
that epsilon_n<1/4. Let

    Wn(y)=an W((y-Rn e3)/epsilon_n),
    g(r)=sum_n en chi(r-Rn-2)/T0(r),
    f(r)=f0(r)sqrt(1-g(r)),
    V(y)=f(|y|)Jy+sum_n Wn(y).                          (2)

Only r>2 occurs in g. Its disjoint supports and the lower bound
T0(r)>=beta L Rn^(beta-1)/2 there give 0<=g<=1/2. The fields and all
cutoffs are smooth; their sums are locally finite. The toroidal part
is divergence-free. Axial translation preserves Wn.Jy=0, and distinct
bumps are disjoint, so every velocity cross term vanishes pointwise.
Each bump adds exactly en energy; the later interval(Rn+2,Rn+3)
removes exactly en. At centered radius R the resulting correction is
between0 and en during the n-th modified interval and zero afterward.
This proves E(R)=LR^beta+O(R^(beta-1)). The toroidal part is bounded by
the decaying baseline, while an tends to zero, so V decays uniformly.

## 5. Fixed centers and local seminorms

For the baseline density F0=|V0|^2, evenness makes the first derivative
of integral_(B_R(a))F0 in a vanish at a=0. Its second derivative is a
sphere integral of a first derivative of F0. Along every fixed center
segment, the large sphere lies in the homogeneous tail, where
|grad F0|<=C r^(beta-4). The second derivative is therefore
O_a(R^(beta-2)), and Taylor's formula gives

    integral_(B_R(a))F0=LR^beta+O_a(R^(beta-2)).

Each signed density correction in(2) has total mass zero, absolute mass
at most2en, and support in Rn-1/4<|y|<Rn+3. It contributes nothing if
B_R(a) contains all of that support or none. Otherwise
|Rn-R|<=|a|+4. Since the Rn are linearly spaced, only O_a(1) indices
contribute. Their masses give O_a(R^(beta-1)). This proves the same
precise energy law at every fixed center, without claiming uniformity
in the center.

Global Holder scaling gives [Wn]_alpha<=C an epsilon_n^(-alpha).
A ball B2(y) meets at most one bump. On the compensation intervals,
g and g' are bounded uniformly; outside them they vanish. Differentiating
f(r)Jy therefore gives an exterior bound O(r^((beta-3)/2)), which tends to zero. This order
can be attained on the compensation intervals; off them the baseline
derivative has the faster order O(r^((beta-5)/2)). On B2(y), a derivative bound implies
an alpha seminorm bound via |x-z|<=4^(1-alpha)|x-z|^alpha. Thus the
toroidal part is harmless. For the bump,

    an epsilon_n^(-alpha)
      =C Rn^[-sigma-alpha(beta-1+2sigma)/3]
      =C Rn^kappa.

Here Rn is comparable to |y| whenever B2(y) meets that bump. This
establishes the stated local seminorm assumption for the whole field.

## 6. Sharp norms and the critical growth boundary

On the disjoint sets Rn e3+epsilon_n D0, orthogonality gives
|V|>=m0 an. Hence, for every p>0,

    integral |V|^p>=C_p sum_n epsilon_n^3 an^p
       =C_p' sum_n Rn^(beta-1-sigma(p-2)).

This diverges for p<=p_star, including equality. Taking
lambda_N=(m0/2)(10N)^(-sigma), the sets with n0<=n<=N all lie in the
superlevel set. Their total volume is bounded below by
C N^(beta+2sigma), because beta+2sigma>0. Therefore

    lambda_N^p |{|V|>lambda_N}|
       >=C_p N^(beta-sigma(p-2)),

which diverges for p<p_star. Section3 proves that this same example
is in weak L^(p_star). Thus no missing endpoint counterclaim is needed.

At the critical boundary replace the scales by

    ell_n=log(Rn+e), an=ell_n^(-1),
    en=eta Rn^(beta-1)/ell_n,
    epsilon_n=(en/(K2 an^2))^(1/3).

The construction and fixed-center proof are unchanged and give the
smaller error O_a(R^(beta-1)/log R). The bump seminorm becomes

    C Rn^[alpha(1-beta)/3] ell_n^(-1-alpha/3),

as claimed. The decaying toroidal bound is smaller than this bound
at large radius. The strong lower series is now
sum Rn^(beta-1)ell_n^(1-p), divergent for every finite p>0. For
lambda_N=m0/[2log(10N+e)] and N/2<=n<=N, the total bump volume is at
least C N^beta log N. Thus
lambda_N^p|{|V|>lambda_N}|>=C_p N^beta(log N)^(1-p), also divergent.
At alpha=1 the gradient bound is O(r^((1-beta)/3)(log r)^(-4/3)).
It is unbounded: at a fixed point where DW is nonzero, the rescaled
bump gradient tends to infinity, while the toroidal gradient tends to
zero. The seminorm growth is nevertheless little-o of the critical
power, and uniform velocity decay holds.

## 7. Poisson pressure and full-equation failure

For either construction the smooth density admits the pressure

    P0(y)=-|V(y)|^2/3+(1/(4pi))PV integral
       [(3z_i z_j-|z|^2 delta_ij)/|z|^5]
       V_i(y-z)V_j(y-z) dz.

Summation over i,j is understood. Near0 subtract the density value at
y; the kernel has zero angular mean, and the remaining singularity
is O(|z|^(-2)), locally integrable. On far dyadic annuli the absolute
bound is C R^(-3)E_y(2R)=O(R^(beta-3)), summable. A smooth partition
of the density into a compact part around an observation compact set
and a part separated from it proves local smoothness: derivatives of
the latter fall on the kernel and improve its distant decay. No bound
on derivatives of V at infinity is required.

First truncate the density smoothly at large radius. The Hessian of
1/(4pi|z|) equals the displayed principal-value kernel minus
(delta_ij/3)delta0. The truncated pressures therefore solve
-Delta P_R=partial_i partial_j(chi_R V_iV_j). They converge locally
uniformly by the same tail estimate, and the right sides converge in
distributions. Thus -Delta P0=partial_i partial_j(V_iV_j)=tr((DV)^2).

On each complete untouched shell Rn+4<r<Rn+8, V=b r^s Jy. Rotation
terms cancel, and full momentum would require

    (1+cs)b r^s Jy-b^2r^(2s)(y1,y2,0)+grad P=0.

A circle integral of the angular component forces1+cs=0. If it holds,
the required gradient is b^2r^(2s)(y1,y2,0). Its first component has
nonzero z derivative at points with y1z!=0, while its third component
is zero. This cannot be a gradient, even of a C1 pressure, since that
smooth prescribed gradient would make the pressure locally C2.
Every real c and omega is excluded, independently of any harmonic
addition to P0. The fields are not Euler profile counterexamples.

## 8. Euler scope and verification boundary

For bounded C1/C1 full profiles with weak dilation limit0 and
2/5<c<1/2, the previously confirmed A3053 energy theorem supplies
(1) with beta=5-2/c unless the field is zero. The displayed Holder
condition is then an additional sufficient premise for the finite
norms, including the weak endpoint. This is not a nonexistence theorem.
No optimal full-Euler threshold or automatic Holder-growth premise is
proved. At alpha=1 and kappa=0 the strong threshold reduces to
(2+3beta)/(1-beta), extending the earlier A3091 statement by removing
an unnecessary a priori boundedness assumption.

All seven source sections atc801bbad, all32manual checks and the formal
scope note were read. No mathematical computation or formal build was
used. The complete existing A133 comparison, all four sections and
remarks Y1-Y4, was read and independently checked. It challenged the
global constant, finite-ball Chebyshev step, small-level radius and
large-level empty set; all are justified in Sections2-3. Its numerical
diagnostics and claimed executions are not certified. Existing
configured model file collaboration is used; actual provider execution
is independently unattested.


## 9. Lorentz sharpness and exact decay order

Write mu(lambda)=measure{|V|>lambda}. Boundedness together with weak
L^(p_star) also yields every strong p>p_star directly: if M bounds |V|,
Tonelli's layer-cake formula gives

    integral |V|^p=p integral_0^M lambda^(p-1)mu(lambda)dlambda
        <=C p M^(p-p_star)/(p-p_star)<infinity.

This is an alternative to the unit-shell series, not an endpoint upgrade.
For the subcritical control, Section6 gives
mu(lambda_N)>=C N^(beta+2sigma), with lambda_N=C0 N^(-sigma).
If lambda_(N+1)<=lambda<=lambda_N, monotonicity of mu gives

    lambda^(p_star)mu(lambda)
       >=C (N+1)^(-sigma p_star)N^(beta+2sigma)>=c0>0,

since sigma p_star=beta+2sigma. The positive c0 is independent of N.
Thus the distribution characterization of a Lorentz L^(p_star,q)
quasinorm, for every finite q>0, contains the divergent integral

    integral_0^[lambda_(n0)]
      [lambda^(p_star)mu(lambda)]^(q/p_star) dlambda/lambda.

The example belongs to weak L^(p_star)=L^(p_star,infinity), but to none
of these finite-q Lorentz spaces. This proves sharpness in the Lorentz
scale at the stated exponent. At the bump center the swirl vanishes,
other bumps vanish, and W(0)=(2/e)e3. Hence

    V(Rn e3)=(2/e)Rn^(-sigma)e3.

No larger uniform decay exponent follows from the stated kinematic
hypotheses. In contrast, a homogeneous tail of magnitude r^(-sigma0)
with nonzero angular part, where sigma0=(3-beta)/2, has energy order
R^beta and norm threshold 3/sigma0=6/(3-beta). Since
sigma<= (1-beta)/5 < sigma0, this threshold is strictly below p_star.
No homogeneous behavior is assumed for general fields in the theorem.

## 10. Stronger full-profile consequence under C2 regularity

The earlier confirmed full-profile theorems give more when their
additional hypotheses hold. Suppose U is C2, P is C1, the full rotating
profile equation holds with 2/5<c<1/2 and any finite real omega, U is
bounded, U(R .) tends to0 in distributions, and

    |DU(y)|=o(|y|^(1/2)) uniformly at infinity.

A498 gives DU tending uniformly to0. Therefore DU is globally bounded.
If U is not already zero, A3053 gives the precise energy law with
beta=5-2/c. Section2 at alpha=1,kappa=0 now implies uniform U decay.
A476-A477/A492, whose explicit hypotheses were reread, then give
|DU(y)|<=C(1+|y|)^(-1/c). For each unit theta, integrate along its ray
using U(r theta) tending to0. Since 1/c>1,

    |U(r theta)|<=integral_r^infinity |DU(s theta)|ds
       <=C' r^(-(1-c)/c).

The constants are uniform in theta, not asserted uniform in omega or
the profile. Superlevel sets are therefore contained in balls of
radius O(lambda^(-c/(1-c))). This gives weak L^(p0), where
p0=3c/(1-c), and boundedness plus layer cake gives every strong p>p0.
In particular p0=6/(3-beta)<p_star for all the subcritical Holder
parameters of this proof. When alpha=1 the assumed local Lipschitz
bound implies |DU|=O(r^kappa) with kappa<(1-beta)/3<1/3, so the extra
little-o half-power condition holds automatically for C2 profiles.
The critical logarithmically improved Lipschitz control also lies in
that half-power class. Consequently the sharp kinematic examples in
this proof cannot establish an optimal full-Euler norm threshold.

This chain makes no assertion for bare C1 profiles, for an alpha<1
seminorm without derivative control, or for arbitrary bounded Hb
profiles. The unrestricted finite-norm question remains open. A498's
separate big-O half-power alternative requires velocity decay; this
argument has used its bounded-velocity little-o alternative and has
not silently replaced that premise by big-O.
