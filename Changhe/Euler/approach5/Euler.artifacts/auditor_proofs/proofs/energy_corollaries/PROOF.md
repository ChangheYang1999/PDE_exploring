# Energy theorem under weak dilation decay and its corollaries

## Hypotheses and audited base theorem

Let c>0, omega real, U,P in C^1(R^3), div U=0, and suppose the complete
profile equation holds pointwise. Assume Hb: U is bounded and U(R .)
converges to zero in distributions as R tends to infinity. Uniform velocity
decay implies Hb. Bounded membership in any finite L^p also implies Hb.
Set E(R)=int_(|y|<R)|U|^2, beta=5-2/c and Z(R)=R^-beta E(R).

For 0<c<1 the base energy theorem under Hb is:

- If c<2/5, U=0.
- If c=2/5, E has a finite limit L and L-E(R)=O(R^-1).
- If c>2/5, Z has a limit L>=0, |Z(R)-L|<=C/R, and L=0 only if U=0.

This is the same theorem as in the team records with H1 weakened to Hb,
but without the little-o error. Its complete proof is that file's pressure
split, shell estimate and finite dyadic bootstrap. To check the weaker
hypothesis rather than merely assert it, the only uses of H1 in that proof
are (a) canonical pressure normalization, which the exact theorem in
in the team records already proves under Hb, and (b) the final
little-o refinement, which is omitted here. Every intervening estimate uses
only bounded U. In particular, if E(R)<=K R^mu, 0<=mu<=3, the pressure split
gives shell flux bounded by C R^mu, hence

    |Z(R2)-Z(R1)| <= C R^(mu-beta-1), R<=R1<R2<=2R.

Summing dyadically improves the exponent until E<=C R^beta (or yields zero
if beta<0), then gives |Z-L|<=C/R. When L=0, summing from infinity improves
mu by one repeatedly until E has a negative power bound, hence is zero.
The critical beta=0 case first yields bounded E and then the tail O(R^-1).
Thus every step genuinely retains only Hb.

Under H1, the three-way shell pressure split improves the error to

    |Z(R)-L| <= C[epsilon(R/2)/R + R^((beta-5)/2)],
    epsilon(R)=sup_(|y|>=R)|U(y)|,

for 0<=beta<3. This is o(1/R), consistent with A040.

## Sharp energy-class exclusions, 2/5<c<1

If liminf R^-beta E(R)=0, the base theorem gives L=0 and U=0. In particular,
if U=o(R^-(1-c)/c), integration in spherical shells gives E(R)=o(R^beta),
since beta=3-2(1-c)/c>0.

If U belongs to L^p for some 0<p<=p*=3c/(1-c), then U=0. For p<=2,
boundedness gives U in L^2. For p>2, split off a fixed ball B_R0 and use
Hölder outside it:

    R^-beta E(R) <= R^-beta E(R0)
      + C R^(3-6/p-beta) ||U||^2_(L^p(|y|>R0)).

The exponent is nonpositive exactly when p<=p*. First let R tend to
infinity and then R0 tend to infinity to get L=0. This includes the endpoint
p=p*. It does not apply at c=2/5, where finite energy alone is not excluded.

For a nonzero U, shell energy is

    E(2R)-E(R)=(2^beta-1)L R^beta+O(R^(beta-1)).

For sufficiently large R this is at least half its leading term. Dividing
by shell volume (28pi/3)R^3 gives

    sup_(R<|y|<2R)|U| >=
      [3(2^beta-1)L/(56pi)]^(1/2) R^-(1-c)/c.

This lower bound is on each large shell, not at every point.

## Vorticity-decay corollary with corrected kernel

Assume also U->0 and |Omega(y)|<=C(1+|y|)^-gamma, with
 gamma>max(1/c,2). Since c>2/5, choose a smaller exponent, still denoted
gamma, in (max(1/c,2),3). Define

    V(y)=(4pi)^-1 int Omega(z) cross (y-z)/|y-z|^3 dz.

The order of the cross product is essential. The reverse order in the first
submitted proof gives curl V=-Omega. The corrected integral converges
absolutely. A split into |z|<|y|/2, |z-y|<|y|/2, the remaining comparable
region and |z|>2|y| proves |V(y)|<=C(1+|y|)^(1-gamma): the kernel has size
|y-z|^-2, the source has size (1+|z|)^-gamma, and 2<gamma<3.

The fundamental-solution identity and div Omega=0 give div V=0 and
curl V=Omega in distributions. One can justify the latter by truncating the
integral and integrating by parts; the tail boundary terms are
O(R^(1-gamma)) and tend to zero. Equivalently, V=curl(G*Omega), where
G=(4pi|.|)^-1 and -Delta G=delta, interpreted through the differentiated
convergent integral. Therefore U-V is bounded, divergence-free and curl-free,
and is constant by harmonic Liouville. Its decay makes the constant zero.
Since gamma>1/c, this gives U=o(R^-(1-c)/c), and the previous result applies.

## Physical local-energy limit

Put s=T-t>0, theta=-omega log s and
u(x,t)=s^(c-1) R_theta U(R_-theta x/s^c). A change of variables gives

    int_(|x|<rho)|u(x,t)|^2 = s^(5c-2) E(rho s^-c)
       = L rho^beta + O(rho^(beta-1) s^c)

for each fixed rho>0 and 2/5<c<1. This is a local energy statement. It does
not assert a pointwise limit of u or an asymptotic expansion of U.

## Critical tail improves to the exact fifth power

At c=2/5 define T(R)=int_(|y|>R)|U|^2. The base theorem gives T(R)->0.
For each R, split pressure into the source on R/2<|z|<4R, the source on
|z|<R/2, and the renormalized source on |z|>4R. The shell estimate is

    int_(R<|y|<2R) |q+P-p_R||U|
       <= C[T(R/2)+R^-3/2 T(R)^1/2].

Indeed, the middle-source L^2 estimate is bounded by sup|U| times
T(R/2)^1/2 and is paired with the shell L^2 norm; the cubic term is bounded
by sup|U| T(R). The inner pressure has size C R^-3 ||U||_2^2 and is paired
with the shell L^1 norm C R^3/2 T(R)^1/2. The outer pressure has size at most
C R^-3 T(4R) and obeys the same bound. Constants depend on the finite total
energy and velocity bound.

The signed integrated identity is

    T(R)=-(2/c) int_R^infinity rho^-1 F(rho) d rho,
    F(rho)=int_(|y|=rho)(q+P-p)U.n.

The first submitted version had the opposite sign. Taking absolute values,
then summing the shell estimates and using monotonicity of T, gives

    T(R) <= C R^-1 T(R/2)+C R^-5/2 sqrt(T(R)).

Young's inequality absorbs the final square-root term:

    T(R) <= C1 R^-1 T(R/2)+C2 R^-5.

Starting from bounded T, this implication improves T=O(R^-k) to
T=O(R^-min(k+1,5)). Five finite steps give

    T(R)=O(R^-5).

Thus the submitted O(R^-5+delta) for every delta>0 is valid and can be
strengthened to the endpoint O(R^-5). There is no forced zero at this
critical exponent. A hypothesized lower bound |U(y)|>=c0 R^-4+delta at
all sufficiently large radii, delta>0, contradicts the tail estimate
(and, for large delta, finite energy itself).

## Scope

These results verify the main theorem and classical corollaries in
 in the team records after the two local sign repairs. The optional distributional
energy-defect extension and novelty claims are not certified here. The full
conjecture in 2/5<c<1/2 remains open: positive L is compatible with decay and
infinite total energy. No pointwise derivative decay has been inferred.

Audit recorded: 2026-11-02T18:47:25Z
