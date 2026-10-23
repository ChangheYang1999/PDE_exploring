# A general symbol inverse and the cascade from a finite leading far field

Written 2026-10-21 before the new supporting checks. Status: complete informal proof, 8392 exact supporting checks passed 04:19Z, and actual lead Claude Opus5.5 hand review confirmed 04:28Z. Three wording repairs from that review were applied at the time recorded in the audit JSON; the frozen review and earlier proof are in verification/opus_20261021T0428. This gives necessary conditions and quantitative approximation obstructions. It does not prove primary existence or nonexistence.

## 1. Statement, notation and dependencies

Let ell>1, p=1/ell, delta=1-p and D=ell-1. Suppose rho is a smooth real function on R^2, even in x and odd in y, and U is its canonical velocity:

    -Delta psi=rho_x,  U=(-psi_y,psi_x),  U=o(r),

with the parity-preserving gauge. Assume, outside a disc,

    (ell X+U).grad rho=rho,
    |D^alpha rho|+|D^alpha U| <= C_alpha r^{p-|alpha|},
    r^{-p}rho(r,theta) -> Theta0(theta) uniformly.       (1)

Assume Theta0 is a nonzero finite sum of odd sine modes. Let n be its highest frequency and a!=0 its coefficient of sin(n theta). Define

    n_k=(k+1)(n+1)-1,  s_k=(k+1)p-k=p-k delta.          (2)

The conclusion is that, for every integer k>=0, there are epsilon_k>0 and a real A_k!=0 such that the Fourier coefficient

    rho_j(r)=(1/pi) integral_0^{2pi} rho(r,theta)sin(j theta)dtheta

satisfies

    rho_(n_k)(r)=A_k r^{s_k}+O(r^{s_k-epsilon_k}),        (3)

with the corresponding order-j radial derivative remainder O(r^{s_k-epsilon_k-j}) for every j>=0. Moreover

    A_0=a,
    kD A_k=sum_(i+j=k-1) c_ij A_i A_j,
    c_ij=(1/4)[1-2(j+1)(n+1)/((i+1)(n+p)+2)],
    A_k=(-1)^k a^{k+1} b_k,  b_k>0.                    (4)

There is no assumption of finite angular support for rho, or for any remainder in (1). Its angular support can be infinite at every positive radius. The finite support assumption concerns Theta0 alone.

Let Pi_N be the projection onto the odd sine modes at most N, where N>=n is odd, and choose the first k with n_k>N. Then

    liminf_(r->infinity) r^{-s_k} ||rho-Pi_N rho||_(L^infinity(S^1))
        >= (pi/4)|A_k|,
    liminf_(r->infinity) r^{-s_k} ||rho-Pi_N rho||_(L^2(S^1))
        >= sqrt(pi)|A_k|.                              (5)

In particular the omitted angular tail is not o(r^{s_k}), and cannot be O(r^b) for b<s_k. The error of a fixed finite angular approximation cannot decay faster than every power. These statements permit general infinite-mode profiles and do not assert convergence of an infinite asymptotic expansion.

Dependencies. The canonical mode Green formula and its uniqueness are established in the canonical-inverse research and report3.1. For an exact primary SettingIII profile, the all-order symbol bounds in (1) are report3.23, independently proved in ../local_ipm_continuation/PROOF.md; the nonzero trace is report3.7, independently proved in ../nonzero_far_field/PROOF.md. Finiteness of Theta0 is the only additional hypothesis for such a profile. Here (1) is an explicit hypothesis, so the theorem also covers exterior solutions with those bounds. The finite-threshold and angular-grading strategy was proved with a finite-angular remainder in ../exterior_finite_angular/PROOF.md. Section2 below removes that restriction; Sections3-5 give the argument again with the new lemma. No regularity theorem or numerical residual is assumed beyond the displayed hypotheses.

Write S^b for functions or vector fields on an exterior region with every Cartesian derivative of order j bounded by C_j r^{b-j}. This is equivalent to bounds O(r^b) for every product of r d_r and d_theta: each Cartesian derivative is r^{-1} times such polar derivatives with smooth angular coefficients. Constants can depend on b and on derivative order.

## 2. Weighted canonical inverse without finite angular support

Lemma. Let f be smooth on R^2, even in x and odd in y, and f in S^b outside a disc, where b<1 and b is not -m-1 for any positive even integer m. Its canonical stream has the expansion

    psi=sum_(m even>=2, -m-1>b) [J_m/(2m)] r^{-m}sin(m theta)
                 +psi_rem,
    J_m=integral_0^infinity s^{m+1} g_m(s)ds,
    g=f_x=sum_(m even>=2) g_m(r)sin(m theta),            (6)

where psi_rem is in S^{b+1}. In particular the velocity remainder is in S^b. The sum is finite and all J_m in it converge. The velocity belongs to S^b if and only if every displayed J_m vanishes. No restriction on angular support is required.

Proof. Choose gamma with max(b,0)<gamma<1. Smoothness on a disc and the exterior symbol estimates give |f|+(1+r)|grad f|<=C(1+r)^gamma. The complete canonical construction and origin regularity in ../inverse/PROOF.md therefore apply to f; they give a smooth parity-preserving canonical stream, unique in the sublinear velocity gauge. The source g has the displayed parities and belongs to S^{b-1} outside a disc. Its canonical radial Green mode is

    psi_m(r)=(1/(2m))[r^{-m} integral_0^r s^{m+1}g_m(s)ds
                       +r^m integral_r^infinity s^{1-m}g_m(s)ds]. (7)

The second integral converges because b<1<=m-1. Put t=log r and

    H_m(t)=exp((1-b)t) g_m(exp t).

For every pair of nonnegative integers j,L,

    sup_(t real) |d_t^j H_m(t)| <= C_(j,L) m^{-L}.      (8)

For t large this follows from the symbol bounds and integration by parts L times in theta in the Fourier coefficient. On compact annuli it follows from smoothness. As t tends to minus infinity, angular derivatives and r d_r are smooth vector fields with coefficients bounded by powers of r on a disc, g is smooth, and exp((1-b)t) tends to zero since b<1. All the needed products are bounded. These observations prove (8) globally; no uniform bound on Cartesian derivatives at infinity is asserted beyond S^{b-1}.

Put lambda=m+b+1 and mu=m-b-1>0. If lambda>0, substitute s=r exp(-v) in the inner integral and s=r exp(v) in the outer integral to obtain the exact formula

    r^{-b-1} psi_m(r)=(1/(2m))[
        integral_0^infinity exp(-lambda v) H_m(t-v)dv
       +integral_0^infinity exp(-mu v) H_m(t+v)dv].      (9)

Both integrals and all t derivatives are absolutely bounded, by (8). In particular

    |d_t^j (r^{-b-1}psi_m)|
        <= (C_(j,L) m^{-L}/(2m))(1/lambda+1/mu).       (10)

For all sufficiently large m the right side is at most C'_(j,L,b) m^{-L-2}. There are only finitely many smaller positive lambda, and each is nonzero. Angular differentiation contributes a power of m, so choosing L sufficiently large proves absolute, locally uniform convergence of every differentiated high-mode series, with an S^{b+1} bound.

If lambda<0, the integral defining J_m converges at infinity because m+b<-1, and at zero by smoothness. Subtract J_m r^{-m}/(2m) from (7). The resulting exact formula is

    r^{-b-1}[psi_m-J_m r^{-m}/(2m)]=(1/(2m))[
       -integral_0^infinity exp(lambda v) H_m(t+v)dv
       +integral_0^infinity exp(-mu v) H_m(t+v)dv].      (11)

Its every t derivative is bounded by (C_(j,L)m^{-L}/(2m))(1/(-lambda)+1/mu). There are only finitely many such m. Summing (9) and (11) proves (6), including all derivative bounds. The Green modes are those of the actual canonical solution, so no harmonic strain has been inserted.

If every displayed J_m vanishes, the velocity is in S^b. Conversely, its radial polar component at frequency m in (6) has cosine coefficient

    -(J_m/2) r^{-m-1}+O(r^b).

If U belongs to S^b and -m-1>b, angular projection forces J_m=0. This proves the equivalence and the lemma.

The excluded thresholds are real obstructions, not a technical omission. The smooth density f=y/(1+r^2)^2 belongs to S^{-3}. Its only stream mode is

    psi_2(r)=-(1/(4r^2))[log(1+r^2)+(1+r^2)^(-1)-1].   (12)

It follows either by direct differentiation or by (7) that this is the canonical stream. The formula is smooth at zero and gives psi_2=-(1/2)r^{-2}log r+O(r^{-2}) at infinity. Its velocity is not in S^{-3}. Thus the resonant log cannot in general be discarded.

## 3. Finite expansions to arbitrary depth

A finite expression means a finite sum of r^s P_s(log r,theta), with polynomial dependence on log r and trigonometric-polynomial angular coefficients. We first extend the inverse lemma to such expressions. Suppose a smooth sublinear density has the form Phi+E outside a disc, where Phi is a finite expression with degrees below1 and E in S^b, b<1 avoiding the thresholds of Section2 and all radial degrees of Phi. Multiply each term of Phi by a common smooth radial cutoff that is one in the exterior. The remainder is a global smooth parity-preserving function in S^b, so (6) applies to it without any angular support hypothesis.

For a cutoff density term r^s(log r)^d sin(j theta), its x derivative has modes j-1 and j+1 and radial degree s-1, with polynomial logs. For one positive even mode m, a particular stream r^{s+1}Q(log r)sin(m theta) is determined by

    -[Q''+2(s+1)Q'+((s+1)^2-m^2)Q]=P.                 (13)

The map is triangular on polynomials with a nonzero diagonal except when s+1=+-m. The positive resonance is impossible because s<1<=m-1. At s+1=-m the equation is -Q''+2mQ'=P and has a polynomial solution with one additional log power. The canonical exterior stream differs from that particular solution by alpha r^m+beta r^{-m}. Green formula (7) gives it the bound O(r^{s+1}(1+log r)^{d+1}+r^{-m}); the particular solution has the same bound. Since s+1<m, alpha=0. Retain beta r^{-m} if its velocity degree -m-1 exceeds b; otherwise absorb it in S^b. Therefore U has a finite expression above b, with remainder S^b, whose terms are either induced with the same degree s as their density source, or decaying harmonic streams. Resonant logs are retained. The finite number of moments from (6) is part of this expression.

From (1), with B=U.grad rho in S^{2p-1}, radial integration gives

    rho=r^p Theta0+T B,
    T f(X)=(1/ell) integral_1^infinity t^{-p-1}f(tX)dt. (14)

The sign is positive: d_r(r^{-p}rho)=-(1/ell)r^{-p-1}B. The endpoint is the assumed trace and the source is integrable since 2p-1<p. T maps S^b to S^b for b<p, including every derivative, because its derivative-order-j integrand is bounded by C r^{b-j}t^{b-p-1}. It also maps a power-log term of degree s<p to a term of the same degree and frequency, by

    T[r^s(log r)^d G]=(r^s G/ell)
        sum_(i=0)^d binom(d,i)i!(log r)^{d-i}/(p-s)^{i+1}. (15)

In particular rho=r^p Theta0+S^{2p-1}. Choose b strictly between 2p-1 and p. Given a density expression above a noncritical threshold b<p with S^b remainder, the inverse just proved yields such a velocity expression too. Their leading terms of degree p are logfree. Every lower term with logs is in S^p, and the error in their product U.grad rho is in S^{p+b-1}=S^{b-delta}; the product of two remainders is smaller because b<p. Apply (14)-(15), then choose b' in (b-delta,b-delta/2) avoiding the finite expression's degrees and all critical thresholds. Terms below b' are in S^{b'}, including logs, because the degree inequality is strict. This gives the next density expression with S^{b'} remainder. The process lowers the threshold by at least delta/2 each time, so finitely many steps reach any prescribed finite depth. Every use of the inverse allows infinitely many angular modes in the remainder.

The collected coefficients of rho and of the total U above a threshold are unique. Otherwise the largest power and then the largest log power in a nonzero finite difference could be divided out, leaving a nonzero trigonometric polynomial tending to zero. The division of a stream into particular and harmonic parts need not be unique at a resonance: for density r^{-3}sin(theta), all r^{-2}[-(1/2)log r+C]sin(2theta) are particular exterior streams. Choosing zero constant term for the resonant polynomial Q fixes one such division. No conclusion depends on this choice. The collected expansions at different depths agree on their shared degrees. This is a statement about finite expressions at each depth. It asserts no convergence of an infinite series.

## 4. Angular grading and the nonzero coefficients

For a term of radial degree p-t call t its cost. All density costs belong to the locally finite set

    Lambda={k delta+2l: k,l nonnegative integers}.      (16)

The leading term has cost0. Induced velocity terms have the cost of their density source. A harmonic stream of even frequency m has velocity degree -m-1, hence cost p+m+1. In U.grad rho the induced product has cost delta+t1+t2, whereas a harmonic term acting on density cost t2 has cost m+2+t2. These operations give (16), since m is even. Each source density cost is strictly smaller than the resulting cost. Thus induction over the ordered locally finite set is legitimate, even when different representations give the same cost. Logarithms do not change cost.

Set C=(n+1)/delta>2. By induction every density term at cost t has frequency at most n+C t, and every induced polar velocity term has frequency at most n+1+C t. For an induced product, the sum-frequency bound is

    (n+1+C t1)+(n+C t2)=n+C(delta+t1+t2).

For a harmonic product at output cost t it is

    m+n+C(t-m-2)<n+C t,

since m<C(m+2). Angular differences are no larger than sums. The inverse changes a density frequency only by plus or minus1, so it respects the induced bound, including resonant logs.

Equality in the density bound requires two earlier equality cases and the sum frequency. It cannot use a harmonic term. Starting from the leading top mode n, equality is possible only at cost k delta and frequency n_k in (2). Every actual interaction other than the maximal-frequency induced sum chain is strictly below it, by at least two in frequency because density frequencies are odd. Different representations of one numerical cost in Lambda, for example 2=4 delta when delta=1/2, are not separate contributions. In particular actual lower-frequency interactions cannot affect the top coefficient through collisions of radial powers. Its induced stream frequency is n_k+1 and can come only from that top density frequency: the other possible density source n_k+2 is forbidden by the bound. Nor can a harmonic term reach that stream frequency at that cost.

Let A_k(z) be the polynomial-log coefficient of r^{s_k}sin(n_k theta), with A_0=a. At a boundary term

    n_k-s_k=(k+1)(n+2-p)-2>0,
    n_k+s_k+2=(k+1)(n+p)+2>0.

Thus its upper stream mode is never resonant. If A_k is constant, the corresponding stream is

    beta_k r^{s_k+1} sin((n_k+1)theta),
    beta_k=-A_k/[2(n_k+s_k+2)].                        (17)

This follows by applying rho_x and (13), with upper source coefficient A_k(s_k-n_k)/2. Suppose all earlier boundary coefficients are constant. Only their products can reach n_k, so (15) shows A_k is constant as well. The polar velocity of a stream beta_i r^{sigma_i}sin(M_i theta) is

    U_r=-beta_i M_i r^{sigma_i-1}cos(M_i theta),
    U_theta=beta_i sigma_i r^{sigma_i-1}sin(M_i theta),

where sigma_i=s_i+1 and M_i=n_i+1. Its product with the gradient of A_j r^{s_j}sin(n_j theta) has sum-frequency coefficient

    (beta_i A_j/2)(sigma_i n_j-M_i s_j) r^{s_k},
    i+j=k-1.

Writing u=i+1 and v=j+1 gives

    sigma_i n_j-M_i s_j=2v(n+1)-[u(n+p)+2].

Together with (17) and ell(p-s_k)=kD, this gives the recurrence (4).

To prove its nonzero sign, put S=u+v>=2, P=uv, B=n+p and A=n+1. Then

    c_ij+c_ji=1/2-(A/2)[v/(uB+2)+u/(vB+2)].

The bracket equals [B(S^2-2P)+2S]/[B^2P+2BS+4]. At fixed S its derivative in P is negative, and P<=S^2/4, so the bracket is at least 2S/(BS+4)>1/A. The last inequality is equivalent to S(n+2-p)>4, which holds. Hence c_ij+c_ji<0, including 2c_ii<0. Pairing i,j in the recurrence proves A_k=(-1)^k a^{k+1}b_k with b_k>0 by induction, for either sign of a. No assertion about the sign of each unpaired c_ij is needed.

## 5. Radial asymptotics and approximation bounds

Fix k. At costs t<k delta the angular grade is strictly smaller than n_k. The projection onto sin(n_k theta) therefore has no coefficient at a degree greater than s_k. At degree s_k its coefficient is the nonzero constant A_k just proved. Choose a finite expansion threshold below s_k. It has only finitely many lower degrees. Choosing epsilon_k>0 smaller than every positive gap from s_k to those degrees and to the remainder threshold absorbs all their polynomial logs in O(r^{s_k-epsilon_k}). All derivative remainders have the corresponding order by the symbol estimates. This proves (3).

For the tail g=rho-Pi_N rho and n_k>N, its n_k coefficient is rho_(n_k). Since integral_0^{2pi}|sin(n_k theta)|dtheta=4,

    |rho_(n_k)| <= (4/pi)||g||_infinity.

Orthogonality and Cauchy-Schwarz also give |rho_(n_k)|<=||g||_2/sqrt(pi). Divide by r^{s_k}, use (3), and take liminf to obtain (5). Thus each mode n_k is nonzero for all sufficiently large radii, though the threshold radius and epsilon_k may depend on k. A fixed exterior angular cutoff is impossible, recovering the earlier restricted theorem, but the stronger statement here applies whenever only the leading trace is finite.

## 6. Scope

The general symbol inverse lemma is a smooth weighted estimate with finitely many explicit moments. It is not a numerical certification method or an interval bound. The cascade theorem assumes the all-order symbol estimates and a nonzero finite leading trace. An arbitrary smooth infinite leading trace is not covered by the top-mode argument. Infinite angular tails forced by (3) are consistent with smoothness at each radius and with the primary growth bounds. Neither their existence nor any possible divergence of the full formal series decides global profile existence. The quantitative inequalities describe finite angular approximation at infinity; they do not forbid accurate numerical approximations on bounded regions.
