# A smooth flat meridional pair with exact local pressure

Status: LIT227 independently confirmed, with the normalization in Section9 extending its construction to every 0<c<1/2. It is a countermodel to a reduced system, not an Euler profile or an actual helicity-free natural tail.

## 1. Exact original construction

Fix 1/3<c<1/2, p=(1-c)/c in(1,2), b=2-p>0, d=p-1, q=2p/d>2 and omega in R. Put Jx=(-x2,x1,0), A=cI-omega J. On a full sufficiently small polar cap about x0=(0,0,1), with radial variable r in a fixed open interval about1, write

    z=cos(theta), y=1-z, w=1-z2=y(2-y), s=sqrt(w),
    E(y)=exp(-1/y) for y>0, E(0)=0,
    H(z)=E(1-z), R(z)=-E(y)/(b y2),
    V=r^(-p)[R e_r+(H/s)e_theta].

Every quotient involving E is extended by0 at y=0. There exists an explicitly defined smooth flat u(y), constructed below, such that P2=r^(-2p)u(y), W=curl V and S=P2-|V|2/2 satisfy

    div V=0, V.W=0, W.grad S=0,
    -Delta P2=tr((DV)^2).

They have the exact twisted homogeneities under exp(tA) for every omega. All derivatives of V,P2,S vanish at x0, but W is nonzero everywhere sufficiently near x0 off the north ray. The actual-tail rank identity grad((Ax).V) cross grad S=0 fails there. The full similarity momentum residual has nonzero curl for every scalar pressure. These failures are explicitly calculated below.

## 2. Smoothness and supported flat vorticity

Primes in the angular calculations mean derivatives in z. Since H'=bR, the field is divergence free. Its curl is

    W=r^(-p-1)(G/s)e_phi,
    G=wR'-dH, R'=E(y)(1-2y)/(b y4).

Consequently G=(2/b)E y^(-3)(1+O(y))>0 for small y>0. The field is meridional and its curl azimuthal, so V.W=0 and W.grad f=0 for every axisymmetric scalar f.

For Cartesian smoothness let n=x/r. The meridional term equals

    (H/s)e_theta=(Hz/w)(n1,n2,0)-H e3.

Its coefficients and R are smooth flat functions of the smooth variable y=1-x3/|x|. The radial interval avoids0. Products with E dominate every inverse power of y, so all Cartesian derivatives of V and W extend by0 at the north ray. In particular x0 belongs to supp W while every vorticity jet vanishes there.

Ordinary homogeneity and axisymmetry give V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x). The same facts give the required scalar homogeneity for P2 once u is constructed. These are local statements in r and do not presume an extension through the origin or to infinity.

## 3. Exact quadratic pressure source

The spherical derivative matrix M=r^(p+1)DV is

    [-pR,  -sR'-H/s,       0;
     -pH/s, dR-zH/w,       0;
      0,      0,           R+zH/w].

Squaring and taking the trace gives the exact smooth flat source

    T=tr(M2)=2(p2-p+1)R2+2b zRH/w+2z2H2/w2
                         +2pHR'+2pH2/w.

The first and fourth terms have combined leading coefficient

    2(p2-p+1)/b2+2p/b=2(p+1)/b2=:T0.

Every other term is lower by at least one power of y. Hence T=T0 exp(-2/y)y^(-4)(1+O(y)), with T0>0. This source is exact; only the displayed asymptotic is abbreviated.

## 4. The convergent pressure series

Let lambda=2p(2p-1)>0 and define

    (Kf)(y)=integral_0^y [1/(t(2-t))] integral_0^t f(v) dv dt.

For0<delta<=1 its operator norm on C([0,delta]) is at most delta: the inner integral is at most t||f|| and t(2-t)>=t. Choose lambda delta<=1/2. The uniformly convergent series

    u=-sum_(n>=0)(-lambda)^n K^(n+1)T

is the unique continuous solution of u=-K(T+lambda u). On y>0 differentiation gives

    [y(2-y)u_y]_y+lambda u=-T.

Since Delta[r^(-2p)u(y)]=r^(-2p-2)([w u_y]_y+lambda u), this proves the pressure Poisson equation exactly.

If f=O(y^N), then Kf=O(y^(N+1)). Starting from bounded u and flat T, its integral equation successively yields u=O(y^N) for every N. The derivative formula

    u_y=-[1/(y(2-y))]integral_0^y(T+lambda u)

gives the same property for u_y. The differential equation then gives it for u_yy. Repeated differentiation proves that each derivative has every power bound, because T is smooth flat and every coefficient singularity has only finite order. Thus u extends smoothly with every derivative zero at0. P2 and S are smooth and flat in Cartesian variables as well.

## 5. Sharper asymptotic and the pressure ratio

For fixed real alpha, substitution v=2/t followed by integration by parts gives

    integral_0^y exp(-2/t)t^alpha dt
       =(1/2)exp(-2/y)y^(alpha+2)(1+O(y)).

Apply it twice. With B(y)=exp(-2/y)/y,

    KT=(T0/8)B(1+O(y)),
    KB=(1/8)exp(-2/y)y2(1+O(y)).

This asymptotic use of the Neumann series is justified in the weighted norm sup|f|/B. Positivity gives ||K||<=C delta3 in that norm. Shrink delta so lambda C delta3<=1/2. KT belongs to the weighted space, so the same series converges there and, by continuous uniqueness, defines the same u. Therefore u=O(B), Ku=O(exp(-2/y)y2), and

    u=-(p+1)/(4b2) exp(-2/y)y^(-1)(1+O(y)),
    u_z=(p+1)/(2b2) exp(-2/y)y^(-3)(1+O(y)).

The derivative asymptotic follows from its integral formula, not from differentiating an unspecified O(y). Since

    |r^pV|2=E2/(b2y4)(1+O(y3)),

one obtains

    S/|V|2=-1/2-(p+1)y3/4+O(y4).

Thus both fields can be flat while the scalar-to-energy ratio tends to -1/2 from below. There is no pressure deficit bound S>=-epsilon|V|2 for a fixed epsilon<1/2 on a sufficiently small punctured cap. The confirmed full-ball pressure lemma is respected, not contradicted.

## 6. Explicit failure of the rank identity

Since V is meridional, k=(Ax).V=c r^(1-p)R for every omega. Write h=u-(R2+H2/w)/2. The exact formulas above give

    h=-E2/(2b2y4)(1+O(y3)),
    h'=E2/(b2y6)(1+O(y)),
    R h'-q hR'=(q-2)E3/(2b3y8)(1+O(y))>0.

For radial and polar gradients, direct two-by-two determinant expansion gives

    grad k cross grad S
       =c d s r^(-3p-1)[R h'-q hR']e_phi.

It is nonzero throughout a sufficiently small punctured cap, whose points are all vortical. This is an explicit failure of a necessary identity for actual HF/natural tails. The weaker identities W.grad k=0 and grad k cross V=kW do hold: the former follows from axisymmetry, and the latter follows from grad k=X cross W-aV and V.W=0. They do not replace the failed rank identity.

## 7. Explicit failure of every pressure completion to similarity

The critical homogeneity and axisymmetry give

    (1-c)V+DV(Ax)+omega JV=0.

Thus for any scalar pi the similarity residual is (V.grad)V+grad pi. For incompressible V its curl is (V.grad)W-(W.grad)V. Direct differentiation of the azimuthal W gives

    curl((V.grad)V)
      =-r^(-2p-2)/s [(p+2)RG+HG'+2zHG/w]e_phi.

For completeness, the radial derivative in (V.grad)W gives -(p+1)RG/s. The polar derivative gives -(HG'+zHG/w)/s. The derivative of the spherical basis in (W.grad)V contributes (RG+zHG/w)/s, yielding the displayed expression and sign.

Now G'=-(2/b)E y^(-5)(1+O(y)), and

    (p+2)RG+HG'+2zHG/w
       =-8E2/(b2y5)(1+O(y)).

The last summand is lower by one power; the leading coefficient uses p+2+b=4. Hence the momentum curl is strictly positive in the e_phi direction near the pole, independent of every pressure choice and every omega. This is not an Euler profile even locally.

## 8. What is refuted and what remains open

The construction refutes the assertion that smoothness, supported common flatness, twisted homogeneity, divergence freedom, zero helicity, vorticity transport of S and exact pressure Poisson alone exclude a nonzero local pair. Each is satisfied simultaneously. It does not refute nonexistence under the full actual-tail identities, since the rank relation fails explicitly. It also does not construct a profile or prescribe a whole-space canonical pressure. Its pressure is a local solution normalized by flatness at the pole.

The construction is consistent with the polar swirl theorem because it has no swirl, and with the open-k-zero theorem because k is nonzero at every off-axis point sufficiently near the pole. Completing this or any common-flat germ while satisfying the actual rank identity remains OPEN.

## 9. A normalization that includes c=1/3 and every 0<c<1/2

There is no need for a denominator 2-p in this countermodel. For any p>1, put b=2-p, which may be positive, zero or negative, and define instead

    H=bE, R=-E/y2,
    V_tilde=r^(-p)[R e_r+(H/s)e_theta].

One still has H'=bR, so incompressibility holds even at p=2. For p!=2 this is b times the previous velocity and its pressure is b2 times the previous pressure wherever that previous formula is defined. At p=2 use the same exact Volterra construction directly. Its quadratic source has leading coefficient T0=2(p+1)>0, its lambda is positive, and every convergence and flatness argument in Sections3-5 applies without a division by b.

More explicitly,

    G=2E y^(-3)(1+O(y))>0,
    u=-(p+1)E2/(4y)(1+O(y)),
    S/|V_tilde|2=-1/2-(p+1)y3/4+O(y4),
    R h'-q hR'=(q-2)E3/(2y8)(1+O(y))>0,
    (p+2)RG+HG'+2zHG/w=-8E2/y5(1+O(y)).

These formulas follow either by the positive scaling when p<2, or directly from R,H and their derivatives for every p>1. In particular they remain valid at p=2, where H=0 and the field is a purely radial but angularly varying divergence-free field of degree -2. The rank defect and momentum curl remain nonzero. Thus the same reduced-system countermodel exists locally for every 0<c<1/2 and every omega.

## 10. Verification

All seven source sections were read in full. The curl, pressure source, Volterra convergence, endpoint regularity, weighted asymptotic, rank defect and momentum-curl sign were reconstructed by hand above. No numerical series truncation, optimization or formal build is used. The immutable source and its real capture time and hash are in the team records. The all-c normalization in Section9 is an additional independently proved extension.
