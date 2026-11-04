# Final check of the gradient-growth and pressure interface

This is a final-phase reconstruction of existing A498 and its bounded-gradient corollary A492. It keeps the growth premises and does not advance a new nonexistence theorem.

## 1. Exact statements

Let J(y1,y2,y3)=(-y2,y1,0), fix 0<c<1 and any finite real omega, and put A=cI-omega J and L=(1-c)I+omega J. Suppose U in C2(R3;R3) and P in C1(R3) solve

    LU+G B+grad P=0, div U=0,
    G=DU, B=Ay+U, W=curl U.

Each of the following hypotheses implies that G tends uniformly to zero:

1. U is bounded and ||G(y)||=o(|y|^(1/2)) uniformly at infinity.
2. U tends uniformly to zero and ||G(y)||<=C0(1+|y|)^(1/2) for a finite C0.

In case1 the actual grad P is bounded. In case2 grad P tends uniformly to zero. The matrix norm is the operator norm. Constants may depend on c, omega, the profile and compact C2 norms; no smallness of C0 or uniformity in omega is claimed. No pressure gauge, helicity sign, finite energy or vorticity integrability is assumed.

In particular, bounded U and bounded G suffice. Once G tends to zero, A3249 gives the Dini condition and, for any c<kappa<1, |W|<=C r^(-kappa/c) and ||G||<=C(r^(-kappa/c)log r+r^-1), hence both are O(r^-1). With the additional vanishing distributional blow-down and1/3<c<1, it also gives ||G||=O(r^-1/c). These are downstream consequences, not premises. A decaying profile which fails derivative decay must therefore have limsup infinity ||G(y)||/sqrt(|y|)=infinity. This last statement concerns failure of derivative decay, not every nonzero profile.

The complete source proofs of A498, A492 and its pressure dependency A485 are captured with reading evidence. The argument below rechecks A498 directly, so A492 is used only as an independently read comparison, not as a premise in its own bounded-gradient corollary.

## 2. A single pressure field and the initial growth bound

Write M=sup|U|<infinity. If M=0 the theorem is immediate. Both cases have G=O(sqrt r). Divergence of momentum, including cancellation of the two skew terms, gives

    f=Delta P=-tr(G^2)=-partial_i partial_j F_ij,
    F_ij=U_i U_j.

The equation makes grad P continuously differentiable. Initially f=O(1+r), F is bounded and grad P=O((1+r)^(3/2)). Let N(x)=-1/(4pi|x|), Delta N=delta0, and N_d=chi(x/d)N for a fixed smooth cutoff equal to1 near0 and zero outside radius2. Define

    Q_d=grad N_d*f-partial_i partial_j grad(N-N_d)*F_ij.

The near kernel has L1 norm C d and the far kernel has L1 norm C/d and tail O(|x|^-4). Each integral is absolutely convergent and locally continuous. If a_d=Delta N_d-delta0, then div Q_d=f+a_d*f+partial_i partial_j a_d*F_ij=f and curl Q_d=0, by compactly supported distributional integration by parts. For d,e>0, N_d-N_e is smooth and compactly supported away from zero, so the same integration by parts gives Q_d=Q_e. Denote this one field by Q. Choosing a point-dependent d below estimates this fixed field and does not change the pressure normalization.

At |y|=R, use d=R^-1/2 to obtain Q=O(sqrt R). In case1, for fixed epsilon>0 and sufficiently large R use d=epsilon^-1 R^-1/2 and |f|<=C epsilon^2 R on the sampled ball. Then |Q(y)|<=C(1+M^2)epsilon sqrt R with C independent of epsilon. Hence Q=o(sqrt R) in case1.

The field grad P-Q is distributionally harmonic and has growth O((1+r)^(3/2)). Interior harmonic estimates give zero second derivatives by letting the radius grow, so grad P-Q=K y+b. In momentum at Rz divide by R. Bounded U gives G(Rz)=D_z(U(Rz)/R)->0 in distributions; the GU/R term is O(R^-1/2), the LU/R term vanishes, and Q(Rz)/R->0. Thus Kz=0 on an open annulus, and K=0. Put

    p(R)=sup_(|y|<=R)|grad P(y)|.

We have grad P=Q+b and p(R)<=C(1+sqrt R). In case1 grad P=o(sqrt r). The constant b remains until momentum removes it in case2. This growth bound will justify the outward iteration.

## 3. Projection along the actual carrier

For large r=|y|, |B|>=cr/2. Define e=B/|B|, Pi=I-e tensor e, T=Pi G Pi, g=Pi G^T e, h=Ge and sigma=W.e. Direct differentiation and momentum give

    h=-(LU+grad P)/|B|, |h|<=C(1+p(r))/r,
    De=Pi(A+G)/|B|,
    G=T+e tensor g+h tensor e,
    W=g cross e+e cross h+sigma e.

In an oriented frame with e=e3, write G=((a,b,h1),(d,f,h2),(g1,g2,h3)). Then W=(g2-h2,h1-g1,d-b), so

    g.W=(Pi W).h, e.GW=W.h,
    tr(G^2)=tr(T^2)+2g.h+(e.h)^2.

The initial growth bound gives g=O(sqrt r) and h=O(r^-1/2). Therefore |f|<=C(1+|T|^2), with C fixed before choosing a small epsilon. The curl equation is B.grad W=G W-W-omega J W. Since D_B e=-omega Je+Pi h, the skew terms cancel and

    B sigma=-sigma+e.GW+W.Pi h,
    |e.GW+W.Pi h|<=C|G||h|,
    B|W|<=-(1-||T||-2|h|)|W|.

The last inequality follows by inserting the displayed matrix decomposition into W.GW and using g.W=(Pi W).h. Zeros are preserved by the linear vorticity ODE, so the integrated comparison also covers them. This is a homogeneous damping bound, with no uncontrolled additive source.

The complete B flow has linear growth, and cr-M<=r'<=cr+M. Every exterior point has a finite backward crossing of a sphere S>2M/c. With k=M/c, its exterior segment satisfies

    k+(S-k)e^(ct)<=r(t)<=(S+k)e^(ct)-k,
    r(t)/r(s)<=3e^(c(t-s)) for 0<=s<=t.

Integrating the scalar sigma equation with this ratio, using 1>c/2 and the monotonicity of p, gives |sigma(y)|<=C(1+p(R))R^-1/2 at |y|=R. In case1, choose S large enough that |G|<=epsilon sqrt r. The sphere contribution is C_epsilon R^-1/c and can be absorbed after increasing the radius threshold. Thus in case1

    |sigma|+|h|<=C epsilon(1+p(R))R^-1/2,
    |De|<=C epsilon R^-1/2,

with C independent of epsilon. The same convolution proves that an o(r^-theta) source yields an o(r^-theta) solution when the damping rate exceeds c theta. Sphere data are always finite-time data; no boundary condition at infinite backward time is used.

## 4. The local Holder bound and its coefficient

In both cases,

    log(2+[G]_(1/2,B(y,R/8)))=O(sqrt R), R=|y|.

In case1 the right side improves to o(sqrt R). Here is the local proof, which needs no global bound on G. Set tau=1-t, s=-log tau, Q_s=exp(omega sJ), y=exp(sA)x. The physical fields u=tau^(-(1-c))Q_s U(y), xi=tau^-1 Q_s W(y) satisfy Euler and |u|<=M tau^(-(1-c)). On the fixed annulus1/16<|x|<16, both ||grad u|| and |xi| are at most C_e tau^(-1-c/2). In case1 C_e=C epsilon after a sufficiently late initial time t0, with C independent of epsilon and t0.

For an inner ball E and margin0<d<=1/16, subtract BS(chi0 xi) using a fixed annular cutoff. Its kernel has degree minus two; u-BS(chi0 xi) is harmonic in the inner annulus, even though the cutoff source need not be solenoidal. Interior harmonic estimates and a second cutoff give

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
       +Cw d^-1/2(1+log(1/d))+CZ,
    w=C_e tau^(-1-c/2), Z=M tau^(-(1-c))+w.

To see the seminorm bound, the derivative kernel has zero spherical mean and degree minus three. Subtraction in the near part gives the Holder term by integrating r^-1/2. The remaining source is at distance at least d/2; its derivative supremum is Cw(1+log(1/d)) and its next derivative is Cw/d. Interpolating these two bounds gives the displayed margin cost.

For |x_*|=1 put r0(t)=1/4+(2M/c)tau^c and Theta(t)=[xi(t)]_(1/2,B(x_*,r0(t))). Choose t0 late enough that (2M/c)(1-t0)^c<=1/8. Earlier points on two particle paths ending in that ball move by at most d(q,t)=(M/c)((1-q)^c-(1-t)^c), with d>=M(t-q), d<=1/16, and r0(q)=r0(t)+2d. Their joining segment stays in the inner annulus and leaves exactly the required margin. The physical paths exist on every finite preterminal interval by bounded velocity and local C1 uniqueness; global gradient boundedness is unnecessary.

Let ell(v)=v^-1/2(1+|log v|), l=C_e tau^(-1-c/2), E0(t)=exp(integral_(t0)^t l). Pair separation is bounded by E0(t)/E0(q). Integrate the difference of xi'=(grad u)xi along the pair, divide by E0(t)^1/2, and use the local estimate. The coefficient of Theta/E0^1/2 is l+Cw. The inhomogeneous integral is bounded by C_(epsilon,t0)tau^-4, since ell is integrable and w^2=O(tau^(-2-c)), with2+c<3<4. Integral Gronwall and integral(l+Cw)<=C_* C_e tau^-c/2 give

    Theta(t)<=C_(epsilon,t0)tau^-4 exp(C_* C_e tau^-c/2).

C_* does not depend on epsilon or t0; compact initial seminorms enter only the prefactor. The seminorms are finite, locally bounded and Borel before t=1, so this is an estimate on actual functions. At a fixed margin, rescale by the exact factor tau^(1+c/2), with tau=R^-1/c, to get the asserted logarithmic bound. In case1 first divide by sqrt R and take a limsup with epsilon fixed, then send epsilon to zero. No uniform control of the initial prefactor in epsilon is needed.

## 5. Projected div-curl estimates and pressure contraction

Put V=U-e(e.U) and q=U.e. Exact Euclidean differentiation cancels the large shear:

    |div V|+|curl V|<=C(|h|+|sigma|+|U||De|),
    Pi(DV)Pi=T-q Pi(De)Pi.

There is no integrability assumption on the plane distribution perpendicular to e. Moreover, DV is linear in G with coefficients built from U,B,|B|^-1 and fixed matrices. On B(y,R/8) these coefficients have polynomial supremum and Lipschitz bounds from G=O(sqrt R) and |B|>=cR/4. Product and reciprocal Holder estimates bound [DV]_(1/2) by C R^N(1+[G]_(1/2)); smooth cutoff data have the same property. Their logarithms are therefore O(sqrt R), and o(sqrt R) in case1. No pressure seminorm occurs.

For a C2 field v cut off inside a ball of radius2ell and equal to v in radius ell, let F collect its divergence and antisymmetric derivative data. The compact-support Newtonian formula gives

    |Dv(0)|<=C[K eta^1/2+epsilon_F(1+log(2ell/eta))],
    K=[F]_(1/2), epsilon_F=||F||_infinity, 0<eta<=1.

The local term is bounded by epsilon_F; the degree-minus-three kernel is integrated after subtracting F(0) below eta and by its supremum above eta. Compact support eliminates a harmonic remainder. Set ell=R/32 and eta=(R^2 max(1,K))^-2. The near term is at most R^-2. Applying this to V and using the preceding logarithmic bounds yields

    |T(y)|<=C(1+p(2R)) in case2,
    |T(y)|<=1+C epsilon^2(1+p(2R)) in case1,

for sufficiently large R, with the latter C independent of epsilon. The two epsilon factors come from the small div-curl supremum and the small logarithmic Holder bound; polynomial cutoff factors only add O(log R), absorbed at a larger threshold.

Set K_y=1+sup_(|z-y|<=2)||T(z)||. In case1 choose d=1/K_y in the same field Q. Since |f|<=C K_y^2 on the sampled ball, the two kernel norms give |grad P(y)|<=D0 K_y. The projected estimate, compact adjustment and p(2|z|)<=p(4R) imply

    p(R)<=C_epsilon+q_0 p(4R), q_0=C epsilon^2<1/2

after choosing one fixed small epsilon. In case2 write a(R)=sup_(|z|>=R)|U(z)|->0 and mu_R=a(R/2)+R^-1. Choose d=mu_R/K_y<=1. The near part of Q is at most C d K_y^2. Split its far part at distance R/2 from y: the inner contribution is at most C mu_R^2/d and the outer contribution at most C M^2/R. Thus

    |Q(y)|<=C mu_R K_y+C M^2/R.

Choose a fixed large S with C mu_R<=q_0<1/2 for all R>=S. Taking the ball supremum again gives p(R)<=C_S+q_0 p(4R). In both cases the n-fold iteration has remainder q_0^n p(4^n R)<=Cq_0^n+C(2q_0)^n sqrt R, tending to zero by the initial growth bound. Hence p is globally bounded. No unknown supremum at infinity is used. It follows that T and f are bounded.

## 6. Pressure limit and the final derivative conclusion

In case2, F tends to zero and f is now bounded. For each fixed d>0, the far L1 convolution defining Q tends to zero while its near part is bounded by C d||f||_infinity. Letting d decrease to zero shows Q->0 and grad P->b. On an escaping B orbit integrate dU/dt=-LU-grad P over [t,t+1]. Uniform decay of U makes the left difference and the LU integral tend to zero, so b=0. This is a consequence of momentum, not a pressure normalization. Therefore h=o(r^-1) in case2; in case1 h=O(r^-1).

The sigma forcing is now o(r^-1/2): in case1 use G=o(sqrt r), and in case2 use h=o(r^-1). Exterior scalar transport gives sigma=o(r^-1/2). Also |U||De|=o(r^-1/2), using small De in case1 and small U in case2. Thus the projected div-curl data are o(r^-1/2). Multiplying their supremum by the O(sqrt R) logarithmic bound in the local estimate gives DV->0, hence T->0.

The homogeneous vorticity inequality now gives |W(y)|<=C_beta r^(-beta/c) for every fixed0<beta<1 by integration from a finite exterior sphere. Choose beta>c/2. A cutoff of U on a ball of radius comparable to R has div-curl supremum C(R^(-beta/c)+R^-1) and Holder logarithm O(sqrt R). The same local estimate gives

    ||G(y)||<=R^-2+C(R^(-beta/c)+R^-1)sqrt R ->0.

This proves both exact statements. Only afterward use the derivative conclusions of A3249 described in Section1. The bounded-gradient special case follows because a bounded G is o(sqrt r). No derivative-growth bound has been deduced from velocity decay alone, and no claim about all nonzero profiles follows.

## 7. Verification scope

The source readings are complete:269lines for A498,233lines for A492 and198lines for A485. This reconstruction rechecks the small-parameter coefficient in the Holder bound, the use of one pressure field at varying cutoff radii, both outward contraction remainders and the homogeneous stretching cancellation. The complete 152-line existing A comparison has been read and its six focus points and remaining derivations independently checked. A3256 confirms this final reconstruction at the stated scope; no growth premise has been removed. No numerical diagnostic or formal build supports this document.
