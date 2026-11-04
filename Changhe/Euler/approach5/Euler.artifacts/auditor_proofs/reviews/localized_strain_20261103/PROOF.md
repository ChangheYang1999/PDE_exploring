# Local vorticity misalignment and a conditional derivative-decay criterion

Status: CONFIRMED A902-A907 at the scopes below. The positive-part equivalence is REFUTED A908; the unconditional stretching bound and wider natural-rate clause remain OPEN A909.

## 1. Local statement with explicit constants

Let U be C2 and divergence free near the closed ball B(z,2rho), rho>0. Write W=curl U and S=sym DU. Choose a unit xi with W(z) cross xi=0; this includes xi=W(z)/|W(z)| when W(z)!=0. Define

    D_rho=(3/(4pi)) integral_{|x|<2rho}|W(z+x) cross xi| |x|^(-3) dx,
    m_ann=sup_{rho<=|y-z|<=2rho}|U(y)|,
    Lambda_delta=sup_{0<|x|<delta}|W(z+x) cross xi|/|x|,
    w_rho=sup_{B(z,2rho)}|W|, K=5 log 2.

Then D_rho is finite and

    |xi.S(z)xi|<=D_rho+K m_ann/rho.                         (1)

For 0<delta<=2rho,

    D_rho<=3 Lambda_delta delta+3 w_rho log(2rho/delta).    (2)

If W has Holder seminorm H of order alpha in (0,1] on the ball, the first term can be replaced by 3H delta^alpha/alpha. In particular D_rho<=6rho Lambda_(2rho). If Lambda=Lambda_(2rho0), m0=sup_B(z,2rho0)|U|, then

    |xi.S(z)xi|<=max(2 sqrt(6K Lambda m0),2K m0/rho0).     (3)

No profile equation is used in (1)-(3).

## 2. Decomposition and the constant

Choose a smooth radial cutoff chi equal to one on B(z,rho), supported in B(z,2rho), with 0<=chi<=1. Extend F=chi U by zero. Put f=grad chi.U, G1=chi W and G2=grad chi cross U. The compact div-curl identity, with Gamma(x)=1/(4pi|x|), is

    F=curl(Gamma*(G1+G2))-grad(Gamma*f).

The distributional second derivative of Gamma is its principal-value kernel (3 xhat_j xhat_l-delta_jl)/(4pi|x|^3), together with -delta_jl delta_0/3. The delta contribution to D curl(Gamma*G) is antisymmetric, as is the identity part of the principal kernel. Contracting the symmetric part with xi twice leaves

    T_chi=(3/(4pi)) integral (xhat.xi)
             det(xi,xhat,chi(z+x)W(z+x)) |x|^(-3) dx.

Since W(z) cross xi=0 and W is C1, this integral is absolutely convergent. It satisfies |T_chi|<=D_rho. The contribution of G2 has absolute value at most 3 log 2 ||grad chi||_infinity m_ann. The Hessian of Gamma applied to f contributes at most 2 log 2 times the same product, since |3(xhat.xi)^2-1|<=2. Thus

    xi.S(z)xi=T_chi+R_chi,
    |R_chi|<=5 log 2 ||grad chi||_infinity m_ann.          (4)

A sequence of smooth cutoffs with gradient norm at most (1+eta)/rho, eta tending to zero, proves (1). Radial integration on the inner ball and outer annulus proves (2). Minimizing 6 Lambda rho+K m0/rho over 0<rho<=rho0 proves (3), including Lambda=0 by using rho0. If m0=0 the field is zero and the claim is immediate.

The exact identity uses the signed integral T_chi. The nonnegative D_rho is a majorant, not an equal expression for stretching.

## 3. Decaying profiles and the averaged sufficient condition

Suppose now U belongs to C2(R3), is divergence free, tends uniformly to zero, and satisfies the profile vorticity equation

    DW B=(DU-I-omega J)W,
    B=(cI-omega J)y+U,

with 0<c<1 and any real omega. Equivalently a C1 pressure exists by the checked curl criterion A852. Let M=sup|U|, m(r)=sup_{|y|>=r}|U(y)|, and choose R1>=2M/c, R1>0. The B flow is complete, and a far point z reaches S_R1 in backward time s(z), with

    |cs(z)-log(|z|/R1)|<=log 2.

On nonzero-vorticity orbits xi=W/|W| is defined throughout. For fixed rho and |y|>=4rho, (1) gives

    |xi.Sxi(y)|<=D_rho(y)+K m(|y|/2)/rho.                 (5)

The error tends to zero. The same conclusion holds for a positive measurable radius rho(r) with rho(r)<=r/4 and m(r/2)/rho(r) tending to zero, provided the displayed orbit integrals are measurable; a continuous choice suffices.

Fix alpha in (0,1) and assume [W]_(C^alpha(B(y,3)))<=C(1+|y|)^N for finite C,N. Suppose there are epsilon>0 and Rstar such that for every |z|>=Rstar with W(z)!=0,

    average_{backward segment to S_R1} D_rho<=1+c/2-epsilon.   (6)

Then DU tends uniformly to zero. In the campaign range 2/5<c<1/2, and more generally in the checked range c>1/3, the natural bounds follow:

    |U|=O((1+|y|)^(-(1-c)/c)),
    |DU|+|W|=O((1+|y|)^(-1/c)).                          (7)

For 0<c<=1/3 the cited argument confirms DU tending to zero and the O(r^-1) gradient bound, but does not establish (7).

To prove this, parametrize the segment by y(t)=Phi_t y0, y0 in S_R1. Radial growth gives |y(t)|>=R1 exp(ct/2). The remainder in (5) therefore has a Cesaro average tending to zero, uniformly over y0. Initial portions in a fixed compact region have uniformly bounded duration and contribute o(1) to the average. The exact scalar transport is

    d/dt log|W(y(t))|=xi.Sxi-1.

Thus (6) gives, for sufficiently large endpoints,

    |W(z)|<=C exp((c/2-epsilon/2)s(z))
           <=C'|z|^(1/2-epsilon/(2c)).                  (8)

The two-sided O(1) time error handles either sign of this exponent. Zero-vorticity endpoints satisfy the bound automatically. Let w(y)=sup_B(y,3)|W| and H(y) be the stated Holder seminorm. Polynomial H and (8) imply

    w(1+log^+(H/w))=O(|y|^(1/2)).

For very small w use w log^+(H/w)<=w log^+H+w log^+(1/w); otherwise the logarithm is O(log r). The checked local logarithmic div-curl estimate A686 then gives DU=O(sqrt(r)), A498 gives DU tending to zero, and A476-A477 give (7) for c>1/3. Full dependencies and their range check are in the team records, Sections 6-7.

## 4. Necessary misalignment for square-root vorticity growth

Under the profile and decay assumptions of Section 3, suppose |z_n| tends to infinity and |W(z_n)|>=delta0 |z_n|^(1/2), delta0>0. The initial vorticity on S_R1 is bounded. The scalar transport identity and the time estimate give

    average_segment xi.Sxi>=1+c/2-o(1).

Subtracting the vanishing Cesaro remainder in (5) proves

    average_segment D_rho>=1+c/2-o(1),
    integral_segment (D_rho-1)^+ >=(c/2-o(1))s(z_n).      (9)

The second statement is a consequence of the first, not an equivalent condition in general. For example a nonnegative function equal to 3 on a fraction c/4 of an interval and zero elsewhere has average (D-1)^+=c/2 but average D=3c/4<1+c/2 for 0<c<1. This refutes the source's word "Equivalently" as an algebraic converse; both necessary inequalities (9) remain proved.

When W does not vanish in the ball, Lambda_(2rho)<=w_rho Lip(xi), because W(z+x) cross xi(z)=|W(z+x)|xi(z+x) cross xi(z). Thus (2) also provides a necessary averaged cost in magnitude times directional variation. No upper bound for that cost has been derived from decay alone.

## 5. Exact transport algebra and shell times

For any orientation-preserving invertible matrix F,

    (Fv) cross (Fw)=det(F)F^(-T)(v cross w).

Apply this with F=D Phi_t, det F=exp(3ct), B(Phi_t)=FB and W(Phi_t)=exp(-(1+c)t)FW. The covector C=B cross W obeys C(Phi_t)=exp(-at)F^(-T)C, a=1-2c. Thus this covector law adds no independent information to these three transport facts. A cocycle F=diag(exp(ct),exp((1+c+d)t),exp((c-1-d)t)) with B0=e1,W0=e2 permits arbitrary net stretching d t; it is a matrix countertest, not a profile.

If W(p)=k B(p) at an exterior point, then W(Phi_t p)=k exp(-(1+c)t)B(Phi_t p). Radial growth comparable to exp(ct) and |B|=O(|y|) give |W|=O(|y|^(-1/c)) on that orbit. Transverse vorticity at the initial point is the only additional transported component.

On a shell R<|y|<2R with R>=2M/c, radial speed lies between cr-m(R) and cr+m(R). Its crossing time is between

    c^-1 log((2cR+m)/(cR+m)) and
    c^-1 log((2cR-m)/(cR-m)),

hence (log 2)/c+O(m/R). The time threshold (c/2)t corresponds to (1/2)log R+O(1). Weighted shell averages alone give Markov bounds on fractions of the shell, not uniform pointwise control.

## 6. Exact nondecaying profile with externally supplied strain

For omega=0 put ell=1+2c and

    U=(0,ell y,-ell z+x^3),
    P=-ell(1+ell)y^2/2-ell(ell-1)z^2/2.

Direct substitution gives div U=0 and the full profile equation: the x^3 coefficient in its third component is 1-c-ell+3c=0, and the linear terms are canceled by grad P. Here W=(0,-3x^2,0), -Delta P=2ell^2=tr(DU^2). Along gamma(x)=(x,0,x^3/(1+4c)), x>0, one has x'=cx, xi=-e2, xi.Sxi=ell and net stretching 2ct. All nearby nonzero vorticity is parallel, so D_rho=0. The missing decay premise is essential; backward trapping, outward foliation and vortex recurrence also fail. This field supplies no counterexample to a decaying-profile theorem.

## 7. Three kinematic tests and their precise limits

First choose geometrically separated shell balls and smooth cutoffs chi_n with inner regions of fixed fractional volume. Set U=sum curl((0,0,(a_n/k_n)chi_n cos(k_n x1))), with a_n tending to zero and frequencies k_n arbitrarily large. The supports are disjoint, U is smooth and divergence free, and its nth amplitude is O(a_n). In the inner region W=(0,0,a_n k_n cos(k_n x1)). A fixed volume fraction has absolute cosine at least 1/2. The radial-time weight is comparable to R_n^-3 by boundedness of U. Choosing k_n makes normalized logarithmic vorticity averages arbitrarily large while U tends to zero. The profile transport equation is absent.

Second let V0=curl(eta x1x2 e3), where eta is one on the unit ball and supported in the ball of radius two. Put z_n=10^n e1, a_n=exp(-n^2), rho_n=n a_n, and U=sum a_n V0((y-z_n)/rho_n). This is a smooth decaying divergence-free field with DU tending to zero. At z_n the strain is diag(1,-1,0)/n, while W vanishes in B(z_n,rho_n) and m(|z_n|/2)=||V0||_infinity a_n. For every fixed K, a radius K m is eventually inside this irrotational ball. A localized vorticity operator at that radius is zero, whereas the strain is not O(m)+O(1/|z_n|). The inner harmonic gradient is a local profile with a suitable pressure, but the patched whole field is not an asserted profile.

Third, for x>=3 take delta(x)=exp(-x^2) and a transverse cutoff equal to one for y^2+z^2<=delta^2, supported where y^2+z^2<4delta^2. Apply curl to this cutoff times ((1+c)yz,-xz^2/2,0), with an additional smooth x cutoff near x=2. This is smooth and divergence free; its magnitude is at most C(1+x)^2 delta(x), so it decays. In the inner tube,

    U=(xz,(1+c)y,-(1+c)z-z^2/2), W=(0,x,0).

On the positive axis U=0, B=cx e1, xi.Sxi=1+c and net stretching ct. Direct differentiation gives the off-axis defect

    [B,W]+(1+c)W=(0,xz,0).

It vanishes on the entire distinguished orbit but not in a neighborhood. Thus checking profile transport only on that orbit misses the coupling to nearby points. This is a kinematic countertest, not a solution of the profile equation.

## 8. Audit and remaining step

The entire 298-line C48 submission and the full analytic source proof for its transport and example section were read. All displayed constants, powers, local residuals and cutoff estimates above were rederived; no numerical check was used as proof. This standalone proof was read after writing. The theoretical question is whether localizing strain isolates a sufficient average that closes the derivative premise. Equations (1)-(8) answer that conditional question. The missing step is an upper bound for (6) from the actual profile equation and bare decay. No impossibility or completeness theorem for the surveyed methods has been established. Existing configured model agent comparison continues; provider runtime is not independently attested.
