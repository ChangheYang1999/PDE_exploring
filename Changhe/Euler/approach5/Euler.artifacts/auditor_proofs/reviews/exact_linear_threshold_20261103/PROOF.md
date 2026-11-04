# The exact threshold for the fixed linear strain-vorticity weight family

## 1. Exact statement and definitions

Let S be a real symmetric trace-free 3 by 3 matrix, W in R3, t=|W|^2, ell=6/5 and M^2=103/100. Matrix norms are Frobenius norms. Define

    K={S: S=S^T, tr S=0, lambda_min(S)>=-ell},
    kappa0(c)=1-3c/2,
    D_c[a,b,g](S,W)=a|S|^2+b tr S^3+(3b/4-2g'(t))W.SW
                      +2g'(t)t-3c g(t)-a t/2.

For 0<c<2/3, let I be the set of c for which some a>0 and real b,gamma satisfy gamma>a/(4kappa0(c)) and D_c[a,b,gamma t]>0 at every point of K times {|W|<=M} other than (0,0). These conditions imply g>=0 and g(0)=0. The family and product set are fixed throughout this result.

Let c* be the unique root in (447/1000,179/400) of

    p(c)=32613201079776000000000 c^9-131904663087801600000000 c^8
         +245809292016421080000000 c^7-280040751027642690000000 c^6
         +216403031159118479784375 c^5-118328096260590827028750 c^4
         +45728290242647648759250 c^3-11925811879607129942700 c^2
         +1819502005156115675495 c-108013798893014552614.

Theorem. I=(0,c*), where c*=0.4472205742139192930041582... . At c=c* an explicitly specified weight with a=1 has D>=0 on the entire product and vanishes at two nonzero points. At every c*<c<2/3, no a>0 and real b,gamma make D_c[a,b,gamma t] nonnegative throughout that product.

The five algebraic numbers b*,gamma*,x_a,x_c,rho used below are defined by the descending rational coefficient lists named b*,gam*,x_a,x_c,rho in the team records, evaluated at c*. Those exact lists are part of the statement's data. They were parsed from the complete retained source log, not inferred from decimal approximations. The independent modular checks below verify every imported mathematical claim. Their approximate values, solely for orientation, are 1.316484929462233,0.930287852870058,0.241985669968106,0.666728166412001,0.258276217041382, respectively.

## 2. Reduction on the complete matrix-vector product

Normalize a=1 by dividing a,b,gamma by a. For linear g put

    alpha=3b/4-2gamma, delta=(2-3c)gamma-1/2,
    A(S)=|S|^2+b tr S^3, L(s)=alpha s+delta.

For t>0, s=W.SW/t belongs to [lambda3,lambda1], and D=A+tL(s). Assume b>=0 and b ell<2. Since tr S^3=3lambda1 lambda2 lambda3 and

    |S|^2/2-3lambda1 lambda2=(lambda1-lambda2)^2,

one has -tr S^3<=ell|S|^2/2. If lambda1 lambda2<0 the left side is nonpositive; otherwise multiply the displayed bound by -lambda3<=ell. Consequently A(S)>0 for S!=0.

It suffices to check D at t=M^2 and s=lambda1,lambda3, because D is affine separately in t and s and is positive at t=0,S!=0. At lambda1=x in [0,2ell], write p=lambda2 lambda3. Then

    A=2x^2+(3bx-2)p,
    max(-2x^2,ell(x-ell))<=p<=x^2/4.

The upper bound follows by completing the square. The first lower bound follows from lambda2<=x and lambda3=-x-lambda2; the second follows from (lambda2+ell)(lambda3+ell)>=0. The lower bounds cross at x=ell/2. Since A is affine in p, its two endpoint values suffice. At lambda3=-y, 0<=y<=ell, use lambda1 lambda2<=y^2/4 and A=2y^2-(2+3by)lambda1 lambda2. Thus the four sufficient endpoint tests are

    f1a(x)=(3/2)x^2+(3b/4)x^3+M^2(alpha x+delta),       0<=x<=2ell,
    f1b(x)=6x^2-6bx^3+M^2(alpha x+delta),               0<=x<=ell/2,
    f1c(x)=2x^2+ell(x-ell)(3bx-2)+M^2(alpha x+delta),    ell/2<=x<=2ell,
    f3(y)=(3/2)y^2-(3b/4)y^3+M^2(delta-alpha y),        0<=y<=ell.

Nonstrict inequalities here give D>=0 on the whole product, provided delta>0 deals with S=0. Strict inequalities imply the strict criterion. This proves the required nonstrict extension of the earlier reduction, without assuming that its sufficient tests are necessary.

## 3. Exact algebraic certificate and its soundness

The independent check does not perform the source's resultant elimination. It imports the six exact coefficient lists, including p, from JSON and verifies the following facts.

First, reduction modulo 13 makes p monic with coefficients

    [1,7,8,4,9,4,11,3,6,10].

In the quotient by this polynomial over F13, c^(13^9)=c and gcd(c^(13^3)-c,p)=1. The degree-9 finite-field irreducibility criterion therefore proves irreducibility modulo 13, hence irreducibility over Q. For completeness, the two conditions say that every irreducible factor has degree dividing9, while no factor has degree dividing3. The only remaining possible factor degree is9, so the polynomial is irreducible. Its leading coefficient is nonzero modulo13.

A rational Sturm sequence gives exactly one root in (447/1000,179/400), with opposite endpoint signs. Rational bisection produces an enclosure of width less than10^(-70), retained in the team records. Horner interval arithmetic evaluates each algebraic representative on this enclosure, giving

    b*>0, b*ell<2, gamma*>1/(4-6c*), delta*>0,
    0<x_a<2ell, -ell<x_c<2ell, rho>0.

Every inequality is verified between exact rational endpoints. In particular r=-2/b*-2x_a<0. No rounded interval endpoint is used.

Reduction in Q[c]/(p), with the denominators inverted there, verifies coefficient by coefficient

    f1a(x;b*,gamma*,c*)=(3b*/4)(x-x_a)^2(x-r),
    f1c(x;b*,gamma*,c*)=(2+3b*ell)(x-x_c)^2,
    f1a(x_a;b,gamma,c*)+rho f1c(x_c;b,gamma,c*)=0

for all real b,gamma. The last identity is checked in each of its three affine coefficients, namely the constant,b,gamma coefficients. Independently the defining ratio

    rho=-(2-3c*-2x_a)/(2-3c*-2x_c)

is checked. Its denominator is nonzero: the exact sign bounds give 2-3c*-2x_c<0. Alternatively the checked positive rho and the explicit nonzero numerator give the same conclusion. The cubic and quadratic identities make f1a>=0 for x>=0 and f1c>=0 on R.

For f1b and f3, the rational enclosure of (b*,gamma*,c*) is a box. Each polynomial is affine in each parameter separately, so at each fixed x its value is a convex combination of the eight vertex values. The independent check verifies positivity of all16 vertex polynomials using Bernstein coefficients. For a polynomial q on [u,v], expand q(u+(v-u)z)=sum q_j z^j and set

    B_k=sum_{j<=k} q_j binom(k,j)/binom(d,j).

Then q=sum B_k binom(d,k)z^k(1-z)^(d-k). The checker expands this identity back into power coefficients, checks them exactly, and requires every B_k>0. Every f1b vertex uses the two half-intervals of [0,ell/2]; every f3 vertex uses the whole [0,ell]. The24 closed intervals cover their prescribed intervals without gaps. Thus f1b>0 and f3>0 on the full required ranges.

The original matrix density is also reconstructed directly at S=diag(x,-x/2,-x/2) and S=diag(x,ell-x,-ell), with W=M e1. It equals f1a and f1c, respectively, identically in x,b,gamma,c. This necessary obstruction below is therefore a test of the original density, not merely of sufficient reduced conditions.

The one-worker exact reconstruction passed in0.21626945724710822 actual seconds, from2026-11-03T21:06:52.795443+00:00 to2026-11-03T21:06:53.011720+00:00, on CPU55 at nice19 with OMP1. in the team records retains all rational inputs, interval certificates, modular evidence, checks and timing. The source's floating point stage X6 is not used. The source exact script and its entire log were read but not executed.

## 4. Endpoint nonnegativity and strict positivity below it

Section3 gives all nonstrict endpoint tests of Section2 at c*. Hence D_c*[1,b*,gamma*t]>=0 on the whole product. If S!=0 and t<M^2, write it as the convex combination

    (1-t/M^2)A(S)+(t/M^2)(A(S)+M^2 L(s)).

The first term is strictly positive, so D>0 there. If S=0 and t>0, D=delta*t>0. At the two points

    P_a=(diag(x_a,-x_a/2,-x_a/2),M e1),
    P_c=(diag(x_c,ell-x_c,-ell),M e1),

the factorization gives D=0. The exact bounds in Section3 put both matrices in K, and W has norm M, so these are nonzero points of the required product. No claim that these are the only zeros, or that the endpoint weight is unique, is made.

For any 0<c<c*, with the same parameters,

    D_c=D_c*+3(c*-c)gamma*t.

This is strictly positive whenever t>0, and at t=0,S!=0 it equals A(S)>0. Also gamma*>1/(4-6c*)>1/(4-6c). Hence the weight meets every defining condition of I at c, proving (0,c*) is contained in I.

## 5. Excluding all other linear weights at and above the threshold

At c*, Section3 gives D(P_a)+rho D(P_c)=0 for every real b,gamma after normalization a=1. Since rho>0, both nonzero points cannot have strictly positive density. Therefore c* is not in I.

For c>c*, first suppose gamma<=0. At S=0,W!=0,

    D_c[1,b,gamma t]=[(2-3c)gamma-1/2]t<0,

because c<2/3. Next suppose gamma>0. If D_c were nonnegative throughout the product, then at both P_a and P_c,

    D_c*=D_c+3(c-c*)gamma M^2>0,

contradicting their positive weighted sum being zero. Thus no nonnegative linear density with a>0 exists above c*. In particular no strict one exists, and I=(0,c*). This proof covers arbitrary real b and gamma and makes the distinction between strict failure at c* and nonnegative failure only above c* explicit.

## 6. Profile consequence, analytic dependencies and limitations

The algebra yields a profile theorem only with the analytic hypotheses of TheoremSF.3. Let 0<c<c*, omega real, U in C2(R3;R3) and P in C1(R3), with div U=0 and

    (1-c)U+((Ay+U).grad)U+omega JU+grad P=0,
    A=cI-omega J, Jy=e3 cross y.

Assume Hb: U is bounded and U(R.) tends to zero in distributions as R tends to infinity. Suppose also -lambda_min(sym DU)<=6/5 and |curl U|^2<=103/100 everywhere. Then U=0 and P is constant.

Here the compact product and strict origin condition give D>=epsilon|DU|^2 for some epsilon>0. The energy, kinematic, transport and Betchov estimates, proved with precisely Hb in the team records, Section6, give for Y(R)=int_(B_R)|DU|^2

    epsilon Y(R)<=C R^(beta-2)+C R^(-1)Y(2R),
    beta=max(5-2/c,0)<2.

Both global bounds imply DU bounded and Y(R)=O(R^3). Successive substitution gives O(R^2),O(R),O(1), then Y(R) tending to zero. Monotonicity implies Y=0. The resulting constant U is zero by Hb, and momentum gives constant P. Pressure is used only through the separately proved energy estimate; no new pressure normalization, derivative decay or boundary-flux assumption is introduced. The rotational field is tangent to the cutoff spheres for every omega. No characteristic-completeness assertion is used here.

This improves only the exact range of the fixed linear multiplier family. The nonlinear C65 weight already gives the same profile consequence for0<c<=1/2 under these two global bounds. No deduction of either bound from decay, no assertion about other products or multiplier families, no endpoint weight uniqueness, and no unrestricted nonexistence theorem follows. Those questions remain open.

## 7. Sources and verification scope

The submitted source is pinned at SHA25626016c743e44408154b83eca184cd3719eced7038b7cb1ec37e75a3fb4cbe79c. Its complete Section4.8, defining identities, SF.3 and SF.4' were read, together with the full source checker and log. The earlier seven-section independent C66 audit was reread. All seven sections of this proof were checked after drafting. The finite data are registered by relative paths and hashes in the team records and in the team records. There is no formal proof-assistant verification. Existing configured model collaboration continues through the integral-estimates and coordinator files; actual provider execution is independently unattested.
