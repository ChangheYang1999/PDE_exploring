# A nonlinear mixed strain and vorticity criterion

Status: independent audit of C65, source section 4.6. The conclusions below concern profiles satisfying both stated global bounds. They do not derive these bounds from decay. In this proof S denotes the strain matrix.

## 1. Exact statement and dependencies

Let U in C^2(R^3;R^3), P in C^1(R^3), 0<c<=1/2 and omega in R satisfy

    (1-c)U + ((Ay+U).grad)U + omega J U + grad P = 0,
    div U = 0,  A=cI-omega J,  J y=e3 x y.

Assume Hb: U is bounded and U(R.) tends to zero in distributions as R tends to infinity. Set G=DU, S=(G+G^T)/2, W=curl U and kappa_0=1-3c/2. Thus tr S=0 and |G|^2=|S|^2+|W|^2/2.

Theorem. If, at every y,

    -lambda_min(S(y)) <= 6/5,       |W(y)|^2 <= 103/100,          (1)

then U=0 and P is constant. The same conclusion holds if the strain hypothesis in (1) is replaced by |S(y)|^2<=54/25 everywhere.

Additional algebraic statement. Let K={S symmetric, tr S=0, lambda_min(S)>=-6/5} and M^2=103/100. For every 9/20<=c<=1/2 there are no constants a>0, b and gamma for which D[a,b,g] is nonnegative on K times {|W|<=M} with g(t)=gamma t, where D is defined in Section 2. This is an obstruction within that family, not a theorem about all multipliers or profile existence.

The analytic dependency is the energy estimate under Hb, independently proved in the team records and used in the team records: for beta=max(5-2/c,0)<2,

    int_{B_R}|U|^2 <= C R^beta, R>=2.                         (2)

Its pressure normalization is a consequence of the full momentum equation and Hb. No separate decay or normalization condition on P is imposed here. The scalar density and cutoff argument are reconstructed next. The polynomial certificate is in the team records; its exact rational inputs are in the team records.

## 2. The density and its implication for a full profile

Put t=|W|^2 and B=Ay+U. The curl equation gives B.grad t=2(W.SW-t), since the rotation terms are skew. Choose a smooth radial cutoff phi_R=chi(|y|/R), with chi nonnegative and nonincreasing, one on [0,1] and zero on [2,infinity). Twice integrating by parts using div U=0 gives

    int phi_R (|S|^2-t/2) = int U_i U_j partial_i partial_j phi_R,
    |int phi_R (|S|^2-t/2)| <= C R^(beta-2).                  (3)

The compactly supported Betchov identity is

    tr G^3 = div(Q-(1/2)U tr G^2),  Q_j=U_i G_jk G_ki,
    tr G^3 = tr S^3+(3/4)W.SW.

It follows by differentiating Q and using partial_i U_i=0; the terms with second derivatives give (1/2)U.grad tr G^2. Consequently, writing Y(R)=int_{B_R}|G|^2,

    |int phi_R [tr S^3+(3/4)W.SW]| <= C R^(-1)Y(2R).         (4)

For g in C^1([0,M^2]), g>=0, the scalar transport identity and div B=3c imply

    int phi_R [2g'(t)(t-W.SW)-3c g(t)] <= 0                 (5)

for R>sup|U|/c. Indeed the left side is int g(t)B.grad phi_R, and B.y=c|y|^2+U.y>0 on the cutoff shell. The rotation is tangent to every sphere, for arbitrary finite omega. The identity is valid for the polynomial g used below; no extension outside [0,M^2] is required under (1).

For constants a,b define

    D[a,b,g](S,W) = a|S|^2+b tr S^3+(3b/4-2g'(t))W.SW
                    +2g'(t)t-3c g(t)-a t/2.                (6)

Combining (3)-(5), with constants depending on a,b and the profile, gives

    int phi_R D <= C R^(beta-2)+C R^(-1)Y(2R).              (7)

Suppose S belongs to a compact set K, |W|<=M, g(0)=0, a>0 and g'(0)>a/(4kappa_0), and D>0 on that compact product away from (0,0). Continuity of g' gives

    D=a|S|^2+(2kappa_0 g'(0)-a/2)t+o(|S|^2+t).

The quadratic part is positive. On a small neighborhood of zero and then on its compact complement one obtains D>=kappa(|S|^2+t/2) for a fixed kappa>0. Bounded S and W give Y(R)<=CR^3. In (7) this yields successively Y(R)<=C(1+R^2), Y(R)<=C(1+R), and Y(R)<=C. A final substitution gives Y(R)<=C(R^(beta-2)+R^(-1)), tending to zero. Since Y is nonnegative and nondecreasing, G=0. Hb excludes a nonzero constant U, and momentum then makes P constant. Every integration had compact support. No completeness of a characteristic flow or boundary limit for DU was used.

## 3. Reduction to four polynomials, including the zero cases

Let ell>0, b>=0 and b ell<2. On K_ell={S symmetric, tr S=0, lambda_min(S)>=-ell}, the eigenvalues lie in [-ell,2ell], so K_ell is compact. Write ordered eigenvalues lambda_1>=lambda_2>=lambda_3. The identity

    tr S^3=3 lambda_1 lambda_2 lambda_3

and |S|^2/2-3lambda_1lambda_2=(lambda_1-lambda_2)^2 imply

    A(S):=|S|^2+b tr S^3 >= (1-b ell/2)|S|^2.               (8)

Thus D[1,b,g](S,0)>0 for S nonzero. For t>0 set

    alpha(t)=3b/4-2g'(t),
    delta(t)=2g'(t)-3c g(t)/t-1/2.

The Rayleigh quotient s=W.SW/t belongs to [lambda_3,lambda_1], and

    D[1,b,g]=A(S)+t(alpha(t)s+delta(t)).                     (9)

The minimum over s occurs at one of the two endpoints, irrespective of the sign of alpha.

For the endpoint lambda_1=x in [0,2ell], put p=lambda_2lambda_3. Then

    A(S)=2x^2+(3bx-2)p,
    max{-2x^2,ell(x-ell)} <= p <= x^2/4.                   (10)

To verify the lower endpoint, use lambda_2+lambda_3=-x and lambda_2 in [-x/2,min{x,ell-x}]. The product -x lambda_2-lambda_2^2 decreases on that interval. Its lower value is -2x^2 when x<=ell/2 and ell(x-ell) when x>=ell/2. The upper value occurs at equal lower eigenvalues. The affine expression (10) is minimized at an endpoint of that product interval, so it suffices to check both resulting endpoint values.

For the endpoint lambda_3=-y, 0<=y<=ell, put p=lambda_1lambda_2<=y^2/4. Here

    A(S)=2y^2-(2+3by)p >= (3/2)y^2-(3b/4)y^3.              (11)

Equations (9)-(11) reduce strict positivity for t>0 to

    F1a(x,t)=(3/2)x^2+(3b/4)x^3+t(alpha(t)x+delta(t)),        0<=x<=2ell,
    F1b(x,t)=6x^2-6bx^3+t(alpha(t)x+delta(t)),                0<=x<=ell/2,
    F1c(x,t)=2x^2+ell(x-ell)(3bx-2)+t(alpha(t)x+delta(t)),    ell/2<=x<=2ell,
    F3(y,t)=(3/2)y^2-(3b/4)y^3+t(delta(t)-alpha(t)y),        0<=y<=ell.

All four must be strictly positive for every 0<t<=M^2 on their respective intervals. No endpoint test in t is substituted for this two-variable requirement. When S=0, F1a(0,t)=t delta(t), so that case is included. Together with (8), these tests imply the compact strict positivity required in Section 2. This proves Lemma SF.8 with its stated C^1, nonnegative-g and strict derivative hypotheses.

## 4. Exact nonlinear certificate

Take c=1/2, ell=6/5, M^2=103/100, b=169/200, and

    g(t)=t[501/500+(2217/10000)t-(317/2000)t^2+(421/2500)t^3].

Then b ell=507/500<2 and g'(0)=501/500>1=1/(4kappa_0). Direct differentiation gives

    alpha(t)=-5481/4000-(2217/2500)t+(951/1000)t^2-(842/625)t^3,
    delta(t)=1/1000+(2217/4000)t-(2853/4000)t^2+(5473/5000)t^3.

The Bernstein coefficients of g(t)/t on [0,103/100] are

    501/500, 1078117/1000000, 65890987/60000000, 1557766971/1250000000.

They are positive, so g is positive when t>0.

Here is the exact positivity argument used by the independent checker. On a rectangle [x0,x1] times [t0,t1], substitute x=x0+(x1-x0)u, t=t0+(t1-t0)v. If the local power coefficients are q_ij and the respective degrees are d,e, the tensor Bernstein coefficients are

    B_kl=sum_{i<=k,j<=l} q_ij binom(k,i)/binom(d,i) binom(l,j)/binom(e,j).

The checker independently reconstructs every local power coefficient by expanding the Bernstein basis. Thus each change of basis is checked as an exact polynomial identity. The basis functions are nonnegative and sum to one on [0,1]^2. Positive coefficients imply strict positivity on the closed rectangle.

An initial 8 by 8 grid, with four equal children for any box failing this sufficient test, gives the following complete certificates. The depth is counted after the initial grid.

| Polynomial | Noncorner positive boxes | Corner boxes | Maximum depth |
|---|---:|---:|---:|
| F1a | 105 | 1 | 2 |
| F1b | 63 | 1 | 0 |
| F1c | 70 | 0 | 2 |
| F3 | 63 | 1 | 0 |

All 301 noncorner boxes and all their positive exact rational coefficients are retained in the team records. Coverage follows from the grid and four-child subdivisions; additionally the checker verifies disjoint interiors, containment and equality of total rational area to the full rectangle area.

Each corner box has t1=103/800. Its x1 is 3/10, 3/40 or 3/20 for F1a, F1b or F3 respectively. On that box,

    F(x,t) >= a0 x^2 + alpha0 tx + t delta(t).

The choices are

| Polynomial | a0 | alpha0 |
|---|---:|---:|
| F1a | 3/2 | -235445828317/160000000000 |
| F1b | 22479/4000 | -235445828317/160000000000 |
| F3 | 22479/16000 | 5481/4000 |

For F1a the omitted strain term is nonnegative. For F1b and F3 it is respectively 6b x^2(x1-x) and (3b/4)x^2(x1-x). The alpha0 values follow from exact Bernstein lower or upper bounds on g' on [0,t1]. The checker verifies that every Bernstein coefficient of

    4a0 delta(t)-alpha0^2 t

on [0,t1] is positive, independently of the source's Sturm calculation. Completing the square proves the lower quadratic is positive whenever t>0. At t=0 and x>0 its strain part is positive. Thus the only permitted zero in each corner is the origin.

All parameters and polynomial operations in this certificate are rational. No sampled minimum, approximate optimization result, or positive floating point tolerance enters the proof. The independent check took 2.6907982123084366 actual seconds on CPU 55 at nice 19 with OMP_NUM_THREADS=1; its log records real start and finish times.

## 5. Every c in the stated interval and comparison with earlier sufficient bounds

At fixed b,g, differentiating any of the four endpoint functions with respect to c gives -3g(t)<=0. Consequently each function for 0<c<1/2 is at least its value at 1/2. Also kappa_0 increases as c decreases, so the strict derivative condition remains true. Sections 2-4 prove the theorem for every 0<c<=1/2 and arbitrary real omega.

The strain threshold 3kappa_0 equals 6/5 at c=2/5 and is strictly smaller for c>2/5. The separate core estimate -lambda_min<1/2 does not cover the full set in (1). For the previously audited vorticity family, T*(c) is nonincreasing and T*(2/5)<1.01272. With U0=12659/12500, the exact check gives

    103/100-U0^2-2U0^4/(2048*2592)^2
      =1512916946628650727439421039/343985356800000000000000000000 > 0.

The certified NW.6 improvement obeys Delta<=2tau^3 delta0/(tau+9c+3)<2tau^2 delta0, with tau=T*(c)^2 and delta0<=(2048*2592)^(-2). Hence even that improvement lies below the vorticity bound in (1) for every c>=2/5. This comparison does not assume tau<1. The NW bounds and their hypotheses were checked in the team records. This establishes the precise comparison window; it does not exclude a stronger sufficient theorem by another method.

## 6. Exact obstruction for linear g

Because (6) is homogeneous in (a,b,g), a>0 can be normalized to one, without restricting b or gamma. At a diagonal S=diag(s1,s2,s3) and W=M e_i, the coefficients of D[1,b,gamma t], in the order constant, b, gamma, are

    sum s_j^2-M^2/2,
    sum s_j^3+(3/4)M^2 s_i,
    M^2(2-3c-2s_i).                                       (12)

For c=1/2 use

    S1=diag(27/100,-27/200,-27/200), W1=M e1,
    S2=diag(63/100,57/100,-6/5),     W2=M e1,
    S3=0,                         W3=M e3.

They are all admissible. Their evaluations are

    D1=(893349/4000000)b-(103/2500)gamma-8113/20000,
    D2=-(161217/200000)b-(1957/2500)gamma+4117/2500,
    D3=(103/200)gamma-103/200.

The positive combination D1+(33087/119420)D2+(748073/1492750)D3 is exactly -24775659/119420000, independently of b and gamma. Thus nonnegativity throughout the product set is impossible.

For c=9/20 use S1=diag(23/100,-23/200,-23/200), S2=diag(8/25,-4/25,-4/25), S3=diag(31/50,29/50,-6/5), all with W=M e1. Formula (12) gives

    D1=(747201/4000000)b+(1957/10000)gamma-8713/20000,
    D2=(8493/31250)b+(103/10000)gamma-1807/5000,
    D3=-(81561/100000)b-(6077/10000)gamma+8229/5000.

The positive combination with weights 1, 5967167/20292232 and 6635925/20292232 is exactly -188599149/50730580000. The checker recomputes (12) from the six matrices and verifies both coefficient cancellations and both negative constants.

For an interior c, D at c' equals D at c plus 3(c-c')gamma t. If gamma>=0, nonnegativity at c would imply nonnegativity at c'=9/20. If gamma<0, it would imply nonnegativity at c'=1/2. Both are impossible. This proves the entire closed interval [9/20,1/2], including unrestricted real b and gamma.

## 7. Norm formulation, inclusions and open scope

Since lambda_1+lambda_2+lambda_3=0,

    |S|^2-(3/2)lambda_3^2=(lambda_1-lambda_2)^2/2>=0.

Therefore |S|^2<=54/25 implies -lambda_min<=sqrt((2/3)(54/25))=6/5. This proves the norm version. At c=2/5 its norm threshold equals (3sqrt(6)/2)kappa_0, and for larger c it exceeds that earlier sufficient threshold. It also exceeds the separate core norm threshold sqrt(3/2).

The new minimum-eigenvalue theorem contains SF.6 and rows 2-6 of SF.7 because their ell and M^2 are no larger and their c ranges are contained. Its norm version contains SF.5 because 54/25>=363/200 and 103/100>=1. Row 1 of SF.7 is not contained: its M^2=11/10 is larger. That row supplies a linear weight for the present smaller product set when 0<c<=11/25. No claim is made about the linear-weight interval 11/25<c<9/20, other pairs of bounds, or optimality among nonlinear weights.

Both global bounds, the full profile equations and Hb are essential premises of this proof. Bounded decay alone supplies neither bound here. The bare-decay nonexistence question remains OPEN. All four source assertions SF.8-SF.11, their supporting source checker and log, and every section of this proof have been read; exact checks are retained separately from the analytic argument. No formal build was performed.
