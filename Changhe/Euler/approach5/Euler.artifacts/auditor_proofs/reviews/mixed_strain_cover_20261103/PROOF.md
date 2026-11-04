# Exact mixed strain windows across the target interval

Status: CONFIRMED A2121-A2125 at the stated conditional scope. Optimality and unrestricted-profile extensions remain OPEN A2126. Exact data and verification are in the JSON inputs and certificate alongside this proof.

## 1. Exact whole-space statement

Let U in C2(R3;R3), P in C1(R3), c>0 and omega a finite real number satisfy

    (1-c)U+DU((cI-omega J)y+U)+omega JU+grad P=0,
    div U=0, Jy=e3 cross y.

Assume Hb: U is bounded and U(R.) tends to zero in distributions on R3 as R tends to infinity. Set G=DU, S=(G+G^T)/2 and W=curl U. For any row of the following table, the three additional hypotheses

    0<c<=c_row,
    lambda_min(S(y))>=-ell for every y,
    |W(y)|^2<=M^2 for every y

imply U=0 and P constant. The last column describes a comparison window, not an additional hypothesis for this vanishing theorem.

| c_row | ell | M^2 | b | gamma | Comparison window |
| --- | --- | --- | --- | --- | --- |
| 11/25 | 6/5 | 11/10 | 13/10 | 9/10 | (2/5,11/25] |
| 9/20 | 23/20 | 1 | 7/5 | 9/10 | (37/90,9/20] |
| 47/100 | 1 | 9/10 | 8/5 | 49/50 | (4/9,47/100] |
| 12/25 | 9/10 | 81/100 | 9/5 | 1 | (7/15,12/25] |
| 49/100 | 43/50 | 3/4 | 19/10 | 21/20 | (107/225,49/100] |
| 1/2 | 4/5 | 7/10 | 2 | 29/25 | (22/45,1/2] |

Within a row's comparison window, its full permitted strain range and its full permitted vorticity range are each beyond the corresponding previously confirmed separate criteria SF, SF.1 and NW.3-NW.6. The six windows cover (2/5,1/2]. This is a comparison with named sufficient criteria, not a proof that neither bound alone could imply vanishing by another argument. The last row is the already confirmed SF.6 instance; the first five are new.

## 2. The compact density and its analytic implication

Write kappa0=1-3c/2>0, t=|W|^2, alpha=3b/4-2gamma and delta=2kappa0 gamma-1/2. The density obtained from the curl transport, kinematic and Betchov identities is

    D=|S|^2+b tr S^3+t(alpha s+delta),
    s=W.SW/t when t>0.                              (2.1)

The exact C62/C63 compact-cutoff identity gives, for a radial nonincreasing cutoff phi_R which is one on B_R and zero outside B_(2R),

    integral phi_R D <= C R^(beta-2)+C R^(-1)Y(2R),
    beta=max(5-2/c,0)<2, Y(R)=integral_(B_R)|G|^2.    (2.2)

Here pressure enters only through the confirmed Hb energy estimate integral_(B_R)|U|^2<=C R^beta. The transport weight is g(t)=gamma t>=0. Its cutoff term is nonpositive since ((cI-omega J)y+U).y=c|y|^2+U.y>0 on a sufficiently large shell. The kinematic error is bounded by C R^(-2) integral_(B_(2R))|U|^2. The Betchov boundary term is at most C R^(-1)Y(2R). All integrations have compact support, and rotation is tangent to the radial cutoff. No pressure decay is imposed separately.

The permitted trace-free symmetric matrices form a compact set K_ell: every eigenvalue lies in [-ell,2ell]. Both S and W are thus bounded, giving Y(R)<=CR^3. If D>0 off (S,W)=(0,0) throughout K_ell times the closed vorticity ball and delta>0, then

    D=|S|^2+delta t+O(|S|^3+|S|t)

is uniformly coercive near zero. Continuity and compactness give D>=kappa(|S|^2+t/2)=kappa|G|^2 everywhere on the allowed set for some kappa>0. Insert this into (2.2). Successive substitution of Y(R)<=CR^3 gives Y(R)<=C(1+R^2), then C(1+R), then C. A final substitution gives Y(R)<=C(R^(beta-2)+R^(-1)), which tends to zero. Since Y is nonnegative and nondecreasing, G=0. Hb removes constant U; momentum gives constant P.

This proves the analytic implication used below, retaining every global assumption. It uses no characteristic-flow completeness or helicity hypothesis.

## 3. Exact reduction to four polynomial inequalities

Let A(S)=|S|^2+b tr S^3 with b>=0. For trace-free S with lambda_min>=-ell, the exact inequality

    -tr S^3<=ell |S|^2/2

gives A(S)>=(1-b ell/2)|S|^2. Thus b ell<2 handles t=0,S!=0. For S=0,t>0, (2.1) is delta t>0. For t>0 the density is affine in t and in the Rayleigh value s. It is enough to test t=M^2 at s=lambda_max and lambda_min.

At the upper endpoint put x=lambda_max in [0,2ell] and p=lambda_2 lambda_3. Trace zero gives A=2x^2+(3bx-2)p. Ordering and the least-eigenvalue bound give the exact interval

    max(-2x^2,ell(x-ell))<=p<=x^2/4.

The lower branches meet at x=ell/2; the endpoint spectra (x,-x/2,-x/2), (x,x,-2x), and (x,ell-x,-ell) are allowed on their respective intervals. Since A is affine in p, its three tests are

    f1a=3x^2/2+3bx^3/4+M^2(alpha x+delta), 0<=x<=2ell,
    f1b=6x^2-6bx^3+M^2(alpha x+delta), 0<=x<=ell/2,
    f1cL=2x^2+ell(x-ell)(3bx-2)
                        +M^2(alpha x+delta), ell/2<=x<=2ell.

At the lower endpoint set y=-lambda_min in [0,ell]. Writing p=lambda_1 lambda_2<=y^2/4 gives A=2y^2-(2+3by)p, minimized at p=y^2/4. The permitted spectrum (y/2,y/2,-y) yields

    f3=3y^2/2-3by^3/4+M^2(delta-alpha y), 0<=y<=ell.

Strict positivity of these four polynomials on the stated closed intervals, together with delta>0 and b ell<2, proves the full compact-density hypothesis. Repeated eigenvalues, zero strain and zero vorticity have all been included.

## 4. Exact rational positivity certificates

For each row take c=c_row and the listed b,gamma. The independent checker derives the power coefficients from Section 3 using the exact JSON inputs. It verifies b ell<2, delta>0 and gamma>1/(4kappa0). The delta values in row order are

    14/125, 17/200, 391/5000, 3/50, 113/2000, 2/25.

For each polynomial and rational subinterval [L,R], substitute x=L+(R-L)u and write the result as sum_j a_j u^j of degree n. Its Bernstein coefficients are

    B_k=sum_(j=0)^k a_j choose(k,j)/choose(n,j).

The identity

    f(L+(R-L)u)=sum_(k=0)^n B_k choose(n,k)u^k(1-u)^(n-k)

is verified by reconstructing the power coefficients with exact fractions. The Bernstein basis is nonnegative and sums to one on [0,1]. Hence strictly positive coefficients give a strictly positive lower bound for f on the full subinterval.

The retained certificate gives all coefficients on a total of 83 rational subintervals. Every coefficient is strictly positive; each polynomial's intervals meet exactly, start and end at its prescribed endpoints, and leave no gap. All 24 polynomial inequalities pass. The submitted Sturm calculation and random samples are not used for this independent sign proof.

For a smaller positive c, alpha is unchanged while delta increases by 3gamma(c_row-c). Each polynomial increases by M^2 times that nonnegative amount. Thus the endpoint certificates prove every c in the whole range stated in Section 1, including its closed upper endpoint. Section 2 completes the vanishing proof.

## 5. Exact comparison windows and coverage

The separate SF strain criterion is -lambda_min<3kappa0. For the full permitted range lambda_min>=-ell this does not apply when

    c>c_ell=(2/3)(1-ell/3).

The separate core eigenvalue criterion of SF.1 requires -lambda_min<1/2 in this comparison; each listed ell exceeds 1/2. The norm and largest-eigenvalue versions also fail to cover the full allowed strain set: it contains diag(2ell,-ell,-ell). The comparison concerns full ranges; an individual profile satisfying a stronger bound may of course fall under an earlier theorem.

For vorticity, the previously confirmed upper brackets in NW.4 and monotonicity of T*(c) give T*(c)<U_k for c>=c_k. The first tabulated choices with U_k^2<M^2 are, in row order,

    (c_k,U_k)=(2/5,101272/100000),
                (41/100,99127/100000),
                (43/100,94744/100000),
                (23/50,87909/100000),
                (47/100,85550/100000),
                (12/25,83146/100000).

These are exact rational upper bounds, not the numerical values of T*. They already exclude coverage of the full M range by NW.3-NW.5. For NW.6 put tau=T*(c)^2. Its exact enlargement of the squared threshold satisfies

    Delta<=2tau^3 delta0/(tau+9c+3)<2tau^2 delta0,
    delta0<=1/(2048*2592)^2.

The last estimate follows from its defined C_*=A1+A2+2(36+b_*)^2>=2592, with b_*>=0. The inequality does not require tau<1, which is useful in the first row. Since tau<U_k^2, the exact check

    U_k^2+2U_k^4/(2048*2592)^2<M^2

puts the entire NW.6 enlarged threshold strictly below M. All six rational margins are positive in the certificate. No ODE integration or decimal epsilon estimate enters this comparison.

For each row c_ell>=c_k, so its stated window is (c_ell,c_row]. Direct rational calculation gives exactly the last column of the table. Consecutive windows overlap: 37/90<11/25, 4/9<9/20, 7/15<47/100, 107/225<12/25 and 22/45<49/100. The first starts at 2/5 and the last ends at 1/2. Hence their union is precisely (2/5,1/2]. This proves the stated interval coverage without claiming maximality of any window.

## 6. Evidence, assumptions and open extensions

The independent check ran once, on CPU55 with priority19 and one numerical thread. Its actual UTC start and finish were 2026-11-03T19:08:00.979991+00:00 and 2026-11-03T19:08:01.003961+00:00; monotonic runtime was 0.02397441864013672 seconds. The theoretical question and pass criteria were recorded before execution. All source polynomials, input rows, upper brackets, the full checker and all 83 certificate subintervals were read. No numerical sign test or formal build is used.

The exact compact identities and energy input are the previously confirmed C62/C63 foundations, reread for this audit. The NW.4 brackets and NW.6 formulas are pinned dependencies, not new conjectured bounds. These six criteria require Hb and the two global inequalities in the relevant row. Decay alone does not imply either inequality. Optimality, improved nonlinear-weight regions, necessity of using two bounds, and unrestricted bare-decay nonexistence remain open. The upper endpoint c=1/2 is valid for the conditional theorem, although the campaign's main target has c<1/2.
