# Two exact mixed strain and vorticity criteria

Independent audit of C63, with C62 as a checked dependency. The source and dependency versions are pinned in the team records. The strain matrix S in this proof is unrelated to the scalar tail Bernoulli function used in other agents.

## 1. Exact profile statement

Let U in C^2(R^3;R^3) and P in C^1(R^3), c>0 and omega real solve

    (1-c)U + ((cI-omega J)y+U).grad U + omega J U + grad P = 0,
    div U = 0,  Jy=e3 x y.

Assume Hb: U is bounded and U(R.) tends to zero in distributions as R tends to infinity. Put G=DU, S=(G+G^T)/2 and W=curl U. Each of the following additional hypotheses implies U=0 and P constant:

1. 0<c<=9/20, |S(y)|^2<=363/200 and |W(y)|<=1 for every y.
2. 0<c<=1/2, lambda_min(S(y))>=-4/5 and |W(y)|^2<=7/10 for every y.

The matrix norm is the Frobenius norm. These are conditional whole-space results for every real omega. They do not derive the displayed strain or vorticity bounds from decay.

## 2. The compact identity and coercivity interface

For 0<c<2/3 set kappa_0=1-3c/2 and beta=max(5-2/c,0)<2. The independently checked canonical pressure and energy theorem under Hb gives

    E(R)=integral_(B_R)|U|^2 <= C R^beta,  R>=2.

No pressure decay assumption is added. Write t=|W|^2 and B=(cI-omega J)y+U. The compactly supported curl transport, kinematic and Betchov identities, rederived in the C62 audit, give

    B.grad t=2(W.SW-t),
    integral phi_R (|S|^2-t/2)=integral U_i U_j partial_ij phi_R,
    |integral phi_R tr G^3|<=C R^(-1)Y(2R),

where phi_R is a nonnegative radial decreasing cutoff, one on B_R and zero outside B_(2R), and Y(R)=integral_(B_R)|G|^2. Here tr G^3=tr S^3+(3/4)W.SW. The second integral is bounded by C R^(beta-2). For g>=0 in C^1, integrating its transport gives a nonpositive contribution

    integral phi_R [2g'(t)(t-W.SW)-3c g(t)]<=0

once R>sup|U|/c. This sign follows from B.y=c|y|^2+U.y on the cutoff shell. All integrals have compact support.

Thus, for constant a,b and

    D=a|S|^2+b tr S^3+(3b/4-2g'(t))W.SW
        +2g'(t)t-3c g(t)-a t/2,

one has

    integral phi_R D <= C R^(beta-2)+C R^(-1)Y(2R).        (1)

For the two present criteria S and W are bounded, so Y(R)<=CR^3. If D>=kappa(|S|^2+t/2)=kappa|G|^2 for some kappa>0, (1) successively gives Y(R)<=C(1+R^2), C(1+R), and C. A final substitution gives Y(R)<=C(R^(beta-2)+R^(-1)), tending to zero. Monotonicity of Y forces G=0 everywhere. Hb removes the constant U, and momentum makes P constant.

In the following take a=1, b>=0 and g(t)=gamma t with gamma>0. Set

    alpha=3b/4-2gamma,  delta=2kappa_0 gamma-1/2.

Then

    D=A(S)+t(alpha s+delta),  A(S)=|S|^2+b tr S^3,          (2)

where s=W.SW/t lies between lambda_min and lambda_max when t>0. Suppose the permitted matrices form a compact set K, delta>0, A(S)>0 for nonzero S in K, and D>0 on K times the closed vorticity ball away from (0,0). Near zero,

    D=|S|^2+delta t+O(|S|^3+|S|t).

Hence D is uniformly coercive near zero. Positivity and compactness give the same conclusion on the remaining set. This proves the interface to (1). For t>0 it suffices to test t=M^2 and both extreme eigenvalues in (2), because the expression is affine in t and then in s. At S=0, D=delta t; at t=0 the condition is A(S)>0. Neither degenerate case is omitted.

## 3. Reduction on a strain norm ball

Let K be the trace-free symmetric matrices with |S|<=sigma, and set r=sqrt(2/3)sigma. Assume br<2. The trace-free cubic bound

    -tr S^3<=|S|^3/sqrt(6)

gives A(S)>=(1-br/2)|S|^2, strictly positive for S!=0.

Write the eigenvalues in decreasing order. At the upper Rayleigh endpoint put x=lambda_1 in [0,r] and p=lambda_2 lambda_3. Trace zero gives

    |S|^2=2x^2-2p,  tr S^3=3xp,
    A(S)=2x^2+(3bx-2)p.

The admissible p interval is

    max{-2x^2,x^2-3r^2/4} <= p <= x^2/4.                 (3)

Indeed x^2/4-p=(lambda_2+x/2)^2, p+2x^2=(x-lambda_2)(2x+lambda_2)>=0, and the norm bound is the other lower bound. Here lambda_2>=-x/2 by ordering. The lower branches meet at x=r/2. The upper endpoint is attained at diag(x,-x/2,-x/2); the first lower branch at diag(x,x,-2x). On the norm boundary branch, the discriminant 3(r^2-x^2) is nonnegative, and (3) ensures the remaining eigenvalues do not exceed x. Thus the reduction loses no admissible extremum.

Since A is affine in p, the upper-endpoint tests are

    f1a(x)=3x^2/2+3bx^3/4+M^2(alpha x+delta),       0<=x<=r,
    f1b(x)=6x^2-6bx^3+M^2(alpha x+delta),           0<=x<=r/2,
    f1c(x)=3bx^3-9br^2 x/4+3r^2/2
                         +M^2(alpha x+delta),      r/2<=x<=r.

At the lower Rayleigh endpoint put y=-lambda_3 in [0,r] and p=lambda_1lambda_2<=y^2/4. Now A=2y^2-(2+3by)p; its p coefficient is negative. The upper p endpoint is attained at diag(y/2,y/2,-y), yielding

    f3(y)=3y^2/2-3by^3/4+M^2(delta-alpha y),        0<=y<=r.

Strict positivity of these four functions and delta>0 proves the coercivity interface of Section 2.

## 4. Reduction with a lower bound on the least eigenvalue

Let K consist of trace-free symmetric matrices with lambda_min>=-l, where l>0. It is compact, since every eigenvalue lies in [-l,2l]. Assume bl<2. The exact trace-free inequality

    -tr S^3<=l|S|^2/2

gives A(S)>=(1-bl/2)|S|^2. To verify the inequality, write the eigenvalues as (-m,x,m-x), with 0<=m<=l. Then tr S^3+(m/2)|S|^2=m(2x-m)^2>=0.

At lambda_1=x in [0,2l], one now has

    max{-2x^2,l(x-l)} <= p <= x^2/4.

The new lower bound follows from p-l(x-l)=(lambda_2+l)(lambda_3+l)>=0. The branches meet at x=l/2. On the second branch the extremizer has eigenvalues (x,l-x,-l), which are correctly ordered and permitted for l/2<=x<=2l. The upper endpoint is again attained at (x,-x/2,-x/2). The lower Rayleigh endpoint still minimizes at (y/2,y/2,-y), now with 0<=y<=l.

Therefore use f1a on [0,2l], f1b on [0,l/2] and f3 on [0,l], and replace f1c by

    f1cL(x)=2x^2+l(x-l)(3bx-2)+M^2(alpha x+delta),
                                                     l/2<=x<=2l.

This last polynomial is quadratic. The same affine and compactness argument applies without a missing matrix or zero-vorticity case.

## 5. Exact certificates for the two instances

For the first instance take c=9/20, r=11/10, M^2=1, b=13/9 and gamma=15/16. Then br=143/90<2, alpha=-19/24 and delta=7/64. The four polynomials are

    f1a=13x^3/12+3x^2/2-19x/24+7/64,
    f1b=-26x^3/3+6x^2-19x/24+7/64,
    f1c=13x^3/3-5669x/1200+3079/1600,
    f3=-13y^3/12+3y^2/2+19y/24+7/64.

For the second take c=1/2, l=4/5, M^2=7/10, b=2 and gamma=29/25. Then bl=8/5<2, alpha=-41/50 and delta=2/25. The polynomials are

    f1a=3x^3/2+3x^2/2-287x/500+7/125,
    f1b=-12x^3+6x^2-287x/500+7/125,
    f1cL=34x^2/5-3007x/500+167/125,
    f3=-3y^3/2+3y^2/2+287y/500+7/125.

The independent exact rational Bernstein check gives the following strictly positive lower bounds on the entire required intervals.

| Instance | Polynomial | Interval | Lower bound | Subintervals |
| --- | --- | --- | --- | --- |
| SF5 | f1a | [0,11/10] | 59/28800 | 3 |
| SF5 | f1b | [0,11/20] | 53/1440 | 2 |
| SF5 | f1c | [11/20,11/10] | 1549/144000 | 3 |
| SF5 | f3 | [0,11/10] | 7/64 | 1 |
| SF6 | f1a | [0,8/5] | 19/3000 | 5 |
| SF6 | f1b | [0,2/5] | 133/7500 | 2 |
| SF6 | f1cL | [2/5,8/5] | 419/80000 | 6 |
| SF6 | f3 | [0,4/5] | 7/125 | 1 |

For completeness, on a rational subinterval [L,R] write x=L+(R-L)u and f(x)=sum_(j=0)^n c_j u^j. The Bernstein coefficients are

    b_k=sum_(j=0)^k c_j choose(k,j)/choose(n,j).

Then f=sum_(k=0)^n b_k choose(n,k)u^k(1-u)^(n-k). These basis functions are nonnegative and sum to one for 0<=u<=1, so f>=min b_k. The retained JSON gives every rational subinterval and coefficient. The verifier reconstructs the power coefficients exactly, checks every b_k>0, and checks adjacent interval endpoints and full coverage. It derives all eight polynomials from Sections 3-4 rather than copying the submitted coefficient list. There is no floating-point sign decision.

For smaller positive c in each stated range, alpha stays fixed and delta increases. All four functions increase by the same positive constant M^2 times the increase in delta. Thus the endpoint certificates prove the entire intervals in Section 1.

## 6. Comparison with the earlier separate criteria

This comparison concerns the already established criteria, not necessity of both bounds for Euler profiles. For SF5, sigma=(11/10)sqrt(3/2) exceeds sqrt(3/2) and equals (3sqrt(6)/2)kappa_0 exactly at c=19/45. Hence the global strain criterion SF and the earlier core norm criterion do not cover the full permitted strain range when 19/45<c<=9/20.

For SF6, l=4/5 exceeds the core threshold 1/2 and equals 3kappa_0 at c=22/45. Hence these separate strain criteria do not cover its full permitted range when 22/45<c<=1/2.

The previously verified NW4 upper brackets give T*(0.41)<99127/100000 and T*(0.48)<83146/100000, and T* decreases with c. These bounds already separate the stated vorticity thresholds from NW3-NW5. To check NW6 without an informal decimal estimate, its exact enlargement in the squared threshold is

    Delta=min{tau, 2tau^3 delta_0/(tau+9c+3)},
    delta_0=min{1,(2048 C_*)^(-2)},
    C_*=A1+A2+2(36+b)^2 >=2592.

Here tau=T*^2<1 and the relevant b is positive. Consequently

    Delta <= 2/[3(2048*2592)^2] = 1/42268920643584.

Exact rational comparison gives

    (99127/100000)^2+1/42268920643584 < 1,
    (83146/100000)^2+1/42268920643584 < 7/10.

Thus NW6 also does not cover the full vorticity ranges of these two windows. The comparison uses the earlier confirmed NW brackets and theorem; it is not a new numerical integration of their defining ODE.

## 7. Source repairs and limitations

The source's Section 6 sentence excluding every SF3 instance other than SF5 is stale after the addition of SF6. It should exclude every instance other than SF5 and SF6.

The final paragraph of Section 4.4 reports finite parameter grids, then says a nonlinear g is needed beyond the observed linear region. The categorical necessity assertion is not proved by those grids. It should remain a numerical suggestion or an open claim. No optimality of the linear or nonlinear weight family is established here.

The numerical region scan, random samples of D, approximate minima and source Sturm implementation are not used for the present exact proof. The independently retained Bernstein certificate is sufficient. No conclusion for unrestricted decaying profiles follows from either instance.

## 8. Verification evidence

All four reduction and instance statements in source Section 4.4, the full source, submitted checker and log, relevant NW comparison formulas, and complete C62 dependency proof were read. The independent exact checker and complete coefficient certificate were also read. All eight sections of this independent proof have been postread before issuing the ledger verdict.

The sole local check for this audit ran on CPU55 with one worker. Its actual UTC start and finish were 2026-11-03T18:50:29.423376+00:00 and 2026-11-03T18:50:29.435365+00:00; the monotonic elapsed time was 0.011991502717137337 seconds. The question and pass/fail criteria were recorded before execution in the team records. All eight interval certificates and both comparison inequalities passed.

Rotation enters only through skew cancellation and tangency to radial cutoffs. No characteristic completeness assumption is used. There is no integration at infinity without a cutoff, no pressure normalization added by hand, no numerical observation called a proof, and no formal build.
