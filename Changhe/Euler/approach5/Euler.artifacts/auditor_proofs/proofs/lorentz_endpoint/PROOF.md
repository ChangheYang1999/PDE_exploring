# Critical Lorentz, shell and weighted exclusions

## Exact hypotheses and conclusions

Let U,P be C1 on R3, let div U=0, and suppose

    (1-c)U+((cI-omega J)y+U).grad U+omega JU+grad P=0,
    2/5<c<1, omega in R.

Assume Hb: U is bounded and U(R .) tends to zero in distributions as R tends to infinity. Uniform U tending to zero implies Hb. Set

    alpha=5-2/c in (0,3), pstar=3c/(1-c)>2,
    E(R)=integral_(|y|<R)|U|^2.

Each of the following implies U=0:

1. The lower limit of R^(-alpha) times the energy on R<|y|<2R is zero.
2. The lower limit of the weak-L^(pstar) quasi-norm of U on these shells is zero.
3. Integral_(|y|>1) |U|^2 |y|^(-alpha) is finite.
4. U belongs to L^(pstar,q) for some 0<q<infinity.
5. Omega=curl U belongs to L^(3c,q) for some 0<q<infinity.

More generally, item 5 may be replaced by the weaker explicit condition

    lim_(rho->infinity) ||Omega 1_(|y|>rho)||_(3c,infinity)=0.       (V)

All norms refer to the Euclidean magnitude. Items 1-4 and item 5 for q>=1 confirm Theory Agent A C19. Condition (V) and the range 0<q<1 are additional consequences proved here. Neither critical weak-space membership alone nor critical pointwise big-O decay is excluded by these arguments.

## Energy input and elementary weak-space inequalities

A052 gives, under exactly these C1 and Hb hypotheses,

    R^(-alpha)E(R)=L+O(R^(-1)), L>=0,
    L=0 if and only if U=0.                              (1)

This includes canonical pressure normalization; no extra pressure hypothesis is imposed.

For a measurable f let f* be its decreasing rearrangement, K=||f||_(p,infinity)=sup t^(1/p)f*(t), and

    ||f||_(p,q)^q=integral_0^infinity [t^(1/p)f*(t)]^q dt/t.

For 0<r<p and a set A of finite volume, the layer-cake formula gives

    integral_A |f|^r <= [p/(p-r)] |A|^(1-r/p) K^r.        (2)

Indeed the distribution on A is at most min(|A|,K^p s^(-p)); integrate r s^(r-1) times this bound, split at s=K|A|^(-1/p). Also monotonicity of f* gives

    K <= (q/p)^(1/q) ||f||_(p,q), 0<q<infinity.           (3)

To see this, integrate over 0<s<t and use f*(s)>=f*(t).

Finite-q Lorentz norms are absolutely continuous on exterior tails. Write f_rho=f 1_(|y|>rho). For every positive level s its level-set measure decreases to zero and is bounded by the finite level-set measure of f. It follows that f_rho*(t) tends to zero for every t>0 and is at most f*(t). Dominated convergence in the defining integral gives

    ||f_rho||_(p,q)->0.                                  (4)

This argument holds also for 0<q<1; no norm triangle inequality is used.

## Shell, weight and velocity conclusions

By (1),

    R^(-alpha)[E(2R)-E(R)] -> (2^alpha-1)L.                (5)

Thus item 1 forces L=0. The shell has volume (28 pi/3)R^3, and 3(1-2/pstar)=alpha. Applying (2) with r=2 proves item 2 from item 1. Equations (3)-(4) show item 4 implies item 2.

Integration by parts gives

    I(R)=integral_(1<|y|<R)|U|^2 |y|^(-alpha)
        =R^(-alpha)E(R)-E(1)
         +alpha integral_1^R r^(-alpha-1)E(r) dr
        =alpha L log R+O(1).                             (6)

The O(1) error is justified by (1), since the remaining radial error is O(r^(-2)) after the extra dr/r. Finite I(infinity) therefore forces L=0, proving item 3. The same integration with the weight r^(-alpha-epsilon), epsilon>0, gives a finite exterior integral for every such profile, whether zero or not.

## A weak potential estimate, with proof

Let 1<p<3 and define s=3p/(3-p). For f in weak Lp define

    Tf(x)=(4 pi)^(-1) integral f(y) cross (x-y)/|x-y|^3 dy.

Then

    ||Tf||_(s,infinity) <= C_p ||f||_(p,infinity).         (7)

Here and below integrals are defined almost everywhere. To prove (7), let K be the source quasi-norm and M the centered Hardy-Littlewood maximal operator. The usual disjoint-ball covering proof gives the weak-(1,1) maximal estimate. Apply it to f 1_(|f|>lambda/2); the complementary part has maximal function at most lambda/2. Layer-cake and p>1 give

    integral_(|f|>lambda/2)|f| <= C_p K^p lambda^(1-p),
    |{M|f|>lambda}| <= C_p K^p lambda^(-p).               (8)

The disjoint-ball estimate is valid first on compact portions of the level set: choose balls with averages exceeding the threshold, extract disjoint balls whose fivefold dilates cover that portion, and sum their integrals. Increasing compact portions gives the global estimate. Thus no finite total integral of f itself is assumed.

For I1|f|=integral |x-y|^(-2)|f(y)|dy, split at radius R. Dyadic inner shells give at most C R M|f|(x). On each outer shell, (2) with r=1 gives integral |f| at most C_p K times the shell volume to power 1-1/p. Summing the outer geometric series gives C_p K R^(1-3/p), since p<3. Optimize R=(K/M|f|(x))^(p/3) to obtain

    I1|f|(x) <= C_p K^(p/3) [M|f|(x)]^(1-p/3).

Equation (8) now gives (7). The cases K=0 and M|f|=0 are immediate. Finiteness almost everywhere follows from the same bound. This proof avoids any appeal to an uninspected convolution theorem.

## The harmonic ambiguity under Hb

For a continuous weak-Lp field f, 1<p<3, choose 1<p1<p<p2<3 and split f=f_high+f_low at |f|=1. Distribution integration shows f_high is in Lp1 and f_low is in Lp2. The potential estimate in A141, proved there by the maximal-function argument, gives T f_i in Ls_i, where s_i=3p_i/(3-p_i), and

    -Delta T f_i=curl f_i

in distributions. The latter identity follows first for smooth compactly supported fields from the Newton kernel, then by Lp approximation and local L1 convergence of their potentials. The sum agrees almost everywhere with the integral defining Tf, by absolute convergence of its scalar majorants.

Apply this to f=Omega. Since -Delta U=curl Omega distributionally, h=U-T Omega is a smooth harmonic field. Fix a radial smooth compactly supported function phi with integral one. The harmonic mean-value property gives

    h(x)=integral h(x+Rz) phi(z) dz.

Each potential term tends to zero by Holder, with bound C R^(-3/s_i)||T f_i||_(s_i). The velocity term equals integral U(Rw)phi(w-x/R)dw. Its difference from the same expression with phi(w) tends to zero, by bounded U and translation continuity in L1. The latter expression tends to zero by Hb. Therefore h=0, and

    U=T Omega.                                          (9)

This proves the representation without assuming pointwise decay of a Riesz potential or of DU.

## Vanishing weak vorticity tails imply vanishing weak velocity shells

Assume (V), and put p=3c, so 1<p<3 and s=pstar in (7). Continuity of Omega on compact sets and (V) imply global weak-Lp membership, so (9) holds. Fix rho and split Omega into its restriction to B_rho and the exterior tail. The tail potential has weak-L^(pstar) quasi-norm at most C_p||Omega 1_(|y|>rho)||_(p,infinity), by (7).

For |x|>2rho the compact-source potential is bounded by C||Omega||_(L1(B_rho)) |x|^(-2). On R<|x|<2R its weak-L^(pstar) quasi-norm is therefore at most

    C_rho R^(3/pstar-2)=C_rho R^(1/c-3),

which tends to zero because c>2/5>1/3. The elementary weak-space quasi-triangle inequality, obtained by splitting a superlevel set at half its level, now gives

    limsup_(R->infinity) ||U 1_(R<|y|<2R)||_(pstar,infinity)
        <= C_c ||Omega 1_(|y|>rho)||_(3c,infinity).

Let rho tend to infinity. Item 2 applies and gives U=0. Equations (3)-(4) show that finite-q Lorentz vorticity implies (V), proving item 5 in its stated and extended ranges.

## Exact scope of sharpness

For the scalar exterior power f(y)=|y|^(-k)1_(|y|>1), p=3/k, its positive-level distribution for 0<s<1 is (4 pi/3)(s^(-p)-1). Hence

    f*(t)=(1+3t/(4 pi))^(-1/p).

The quantity t^(1/p)f*(t) tends to a positive constant. The field lies in weak Lp and in no finite-q L^(p,q). The velocity and vorticity natural powers correspond to k=(1-c)/c and k=1/c. This verifies the stated function-space borderline. It does not construct a profile with either power, prove that all nonzero profiles belong to the critical weak spaces, or prove a sharp existence threshold. Equation (6) is an exact necessary logarithmic divergence for any hypothetical nonzero profile under Hb.

All arguments are analytic, uniform in finite omega, and use the Euler equation only through (1) and the actual curl relation in (9). There is no new numerical or formal computation.

Audit written: 2026-11-02T20:48:48Z
