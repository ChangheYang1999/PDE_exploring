# An exact bracket for one linear-weight threshold

## 1. Statement and exact scope

Let S be a real symmetric trace-free 3 by3 matrix, W in R^3, t=|W|^2, ell=6/5 and M^2=103/100. The norm on matrices is the Frobenius norm. Put

    K={S: S=S^T, tr S=0, lambda_min(S)>=-ell},
    kappa_0(c)=1-3c/2,
    D_c[a,b,g](S,W)=a|S|^2+b tr S^3+(3b/4-2g'(t))W.SW
                      +2g'(t)t-3c g(t)-a t/2.

For 0<c<2/3 define I to be the set of parameters for which there are constants a>0, b real and gamma real such that g(t)=gamma t, gamma>a/(4kappa_0(c)), and D_c[a,b,g]>0 on K times {|W|<=M} away from (0,0). These conditions also imply g>=0 and g(0)=0. This is the linear subfamily of the previously audited mixed-density criterion.

Theorem. The set I is closed downward within (0,2/3), contains 447/1000 and contains no c>=179/400. Consequently

    447/1000 <= sup I <= 179/400.

At c=447/1000 the parameters a=1, b=329/250 and gamma=4653/5000 work. At every 179/400<=c<2/3, no a>0 and real b,gamma make D_c[a,b,gamma t] nonnegative on the entire product. In particular, the latter conclusion includes the source's part(iv), which states it only up to c=1/2.

This is a statement about one product of strain and vorticity bounds and one multiplier family. It neither determines sup I exactly nor excludes other methods. The profile consequence, with all its analytic hypotheses, is stated in Section6.

## 2. The reduction to four exact polynomials

Normalize a=1 by dividing a,b,g by a. For a linear weight put

    alpha=3b/4-2gamma, delta=(2-3c)gamma-1/2,
    A(S)=|S|^2+b tr S^3.

Then D=A(S)+t(alpha s+delta), where s=W.SW/t when t>0. Suppose b>=0 and b ell<2. For ordered eigenvalues lambda_1>=lambda_2>=lambda_3 of S,

    tr S^3=3lambda_1lambda_2lambda_3,
    -tr S^3 <= ell |S|^2/2.

The latter follows from |S|^2/2-3lambda_1lambda_2=(lambda_1-lambda_2)^2 and lambda_3>=-ell. Thus A(S)>0 for S!=0. The case S=0 is covered by delta>0. For each nonzero S, D is affine in t and in the Rayleigh quotient s, so it suffices to check t=M^2 and s=lambda_1 or lambda_3.

At lambda_1=x in [0,2ell], set p=lambda_2lambda_3. Then

    A(S)=2x^2+(3bx-2)p,
    max(-2x^2,ell(x-ell)) <= p <= x^2/4.

Indeed x^2/4-p=(lambda_2+x/2)^2. The lower inequalities follow from eigenvalue ordering and (lambda_2+ell)(lambda_3+ell)>=0. The two lower bounds cross at x=ell/2. Since A is affine in p, both endpoints suffice. At lambda_3=-y, 0<=y<=ell, put p=lambda_1lambda_2<=y^2/4; then A=2y^2-(2+3by)p is minimized at p=y^2/4.

The required four polynomials are therefore

    f1a(x)=(3/2)x^2+(3b/4)x^3+M^2(alpha x+delta),  0<=x<=2ell,
    f1b(x)=6x^2-6bx^3+M^2(alpha x+delta),          0<=x<=ell/2,
    f1c(x)=2x^2+ell(x-ell)(3bx-2)+M^2(alpha x+delta), ell/2<=x<=2ell,
    f3(y)=(3/2)y^2-(3b/4)y^3+M^2(delta-alpha y),   0<=y<=ell.

Strict positivity on these closed intervals, together with b ell<2 and delta>0, proves all required product inequalities, including t=0 and S=0. No eigenvalue sign or angular orientation is omitted. This independently reconstructs the sufficient reduction of SF.4'. It is not used to prove necessity in Section5.

## 3. Independent rational positivity certificate

At c=447/1000, b=329/250 and gamma=4653/5000 one has

    b ell=987/625<2,
    1/(4kappa_0)=500/659<gamma,
    alpha=-4371/5000, delta=566327/5000000>0.

Substitution gives exactly the four coefficient lists retained in the team records. They coincide with the source polynomials, including the quadratic f1c. All inputs are exact fractions in the team records and are reconstructed from the density formulas by in the team records.

Here is the certificate's soundness argument. For each closed subinterval [l,r], write f(l+(r-l)u)=sum q_j u^j, with degree d. Define

    B_k=sum_{j<=k} q_j binom(k,j)/binom(d,j), 0<=k<=d.

Then f(l+(r-l)u)=sum B_k binom(d,k)u^k(1-u)^(d-k). The independent checker expands the right side back into power coefficients and verifies every coefficient identity. The basis functions are nonnegative and sum to one on [0,1], so strictly positive B_k prove f>0 on the whole closed interval.

Exact midpoint subdivision gives the following complete certificates:

| Polynomial | Positive closed subintervals | Maximum subdivision depth |
|---|---:|---:|
| f1a | 7 | 6 |
| f1b | 2 | 1 |
| f1c | 8 | 7 |
| f3 | 1 | 0 |

All18 subintervals and every rational Bernstein coefficient are retained. Sorted adjacent endpoints agree, the outer endpoints equal the prescribed interval, and the total rational length equals its length. These checks establish complete coverage, without gaps or assumed sampling density. Every coefficient is strictly positive. Thus Section2 proves 447/1000 in I.

The independent process took0.013413355220109224 actual seconds on CPU55 at nice19 with OMP1. It also checks the certificate in Section5. No source script, floating point minimum or optimization result is used. The source script's separate Sturm computation and random samples were read, but no random sample is part of this proof.

## 4. Downward monotonicity

For c'<c and the same a,b,gamma,

    D_c'[a,b,gamma t]=D_c[a,b,gamma t]+3(c-c')gamma t.

An admissible weight has gamma>a/(4kappa_0(c))>0, so strict positivity persists when c decreases. Also a/(4-6c) is strictly increasing in c, and hence the strict origin condition persists. This proves I is closed downward. In particular the parameters of Section3 work for every 0<c<=447/1000. This phrase means downward closure of the order ideal; no topological closedness of I is asserted.

## 5. A necessary obstruction from three points

At c_+=179/400 and a=1 take W=M e1 and the three diagonal matrices

    S1=diag(6/25,-3/25,-3/25),
    S2=diag(121/500,-121/1000,-121/1000),
    S3=diag(333/500,267/500,-6/5).

They are trace free and lie in K; all three W have norm M. For a diagonal point S=diag(s1,s2,s3), the coefficients of D in the order constant,b,gamma are

    sum s_j^2-M^2/2,
    sum s_j^3+(3/4)M^2 s1,
    M^2(2-3c-2s1).

The independent checker reconstructs these three rows directly from the matrices. With positive weights

    1, 1296637500/130604989, 367900655/130604989,

the b and gamma coefficients cancel exactly, leaving

    -8996656119/816281181250<0.

Thus at c_+ no real b,gamma can make D nonnegative everywhere on the product. This certificate tests the original density itself, not merely the sufficient reduction of Section2.

For c>=c_+ and gamma>0, every pointwise D_c is at most D_c+, so the same positive combination stays negative. For arbitrary gamma<=0, take S=0 and any W!=0 with |W|<=M. Since c<2/3 and a>0,

    D_c[a,b,gamma t](0,W)=[(2-3c)gamma-a/2]t<0.

This directly excludes the remaining coefficients. It proves the stronger nonnegativity obstruction throughout [179/400,2/3); the source's part(iv) on [179/400,1/2] also follows. The source instead uses the previously confirmed c=1/2 certificate for gamma<0. That argument is valid, but no second certificate is needed for the direct zero-strain argument just given. No new computation was required for this observation.

Together with Section4 this proves the stated bracket. Its width is1/2000. The decimal optimization suggestion near0.44722 does not determine the threshold and is not asserted here.

## 6. Exact analytic profile consequence and dependencies

For clarity, the algebra applies to a full profile only under the following hypotheses. Let U in C^2(R^3;R^3), P in C^1(R^3), 0<c<=447/1000 and omega in R satisfy

    (1-c)U+((Ay+U).grad)U+omega J U+grad P=0,
    div U=0, A=cI-omega J, J y=e3 cross y.

Assume Hb: U is bounded and U(R.) tends to zero in distributions as R tends to infinity. If S=sym DU obeys -lambda_min(S)<=6/5 everywhere and |curl U|^2<=103/100 everywhere, then U=0 and P is constant by the linear weight above. No bound is deduced from Hb alone.

Here are the analytic dependencies and the cutoff argument. The energy estimate under exactly Hb is proved in the team records; it supplies int_{B_R}|U|^2<=C R^beta, beta=max(5-2/c,0)<2, R>=2. The exact identities and the mixed criterion are reconstructed in the team records, Sections2-3, fully reread for this audit. For a nonnegative nonincreasing radial cutoff phi_R, equal to one on B_R and zero outside B_(2R), write G=DU, t=|curl U|^2 and Y(R)=int_{B_R}|G|^2. Incompressibility, the vorticity transport and the compactly supported Betchov identity give

    int phi_R D <= C R^(beta-2)+C R^(-1)Y(2R).

The scalar transport term has favorable sign because (Ay+U).y=c|y|^2+U.y>0 on sufficiently distant shells. The rotation term is tangent to spheres for every finite omega. The other two errors follow from two derivatives on the cutoff in the kinetic identity and one derivative on it in the Betchov identity. Thus no boundary limit for DU is assumed.

The strict origin condition gives D=a|S|^2+[(2-3c)gamma-a/2]t+o(|S|^2+t) with positive quadratic coefficients. Compactness of K and the W-ball gives D>=kappa(|S|^2+t/2) globally on that product for some kappa>0. Both bounds make G bounded, so initially Y(R)<=CR^3. Substitution in the displayed estimate successively gives O(1+R^2), O(1+R), O(1), then O(R^(beta-2)+R^(-1)), which tends to zero. Nonnegative monotonic Y must vanish. U is constant, Hb makes it zero, and momentum makes P constant. Pressure enters through the stated energy dependency, with its canonical normalization consequence; no new pressure assumption or characteristic completeness is used.

## 7. Audit scope and source revision

The initial source had parts(i)-(iii); during review part(iv) was added. The pinned source SHA is c4ccda4ddb95d4bc30650d807e17fd5eea61753cb98351826aafc0d033491cdb. Its complete Section4.7, the defining density, SF.3, SF.4 and SF.4', the full source checker, and the retained log were read. The retained rerun log was copied while its random-sampling stage was still running; it contains the complete exact L1-L4 output, and no completed rerun time is inferred from it. The earlier complete source log showed39.0seconds; that is a separate source execution, not the independent runtime. The independent certificate and its finished log establish the finite algebra used here.

The entire prior seven-section mixed-criterion proof was reread, and all seven sections of this reconstruction were checked. The exact threshold, other pairs, other identities and any deduction of the two bounds from decay remain open. The unrestricted nonexistence conjecture remains open. Existing configured model collaboration proceeds through the integral-estimates and coordinator files; actual provider execution is independently unattested. No new model client, formal build or prohibited execution was used.
