# Global axis transport with a closed cubic coefficient

## Statement and scope

This result concerns the scalar axis row of the pure transport operator. It does not assert invertibility of the full two-dimensional IPM operator. In particular, the velocity coupling, its interaction with the jet extension, the remainder realization, and the global flow hypotheses must still be proved separately.

Fix ell>1, D=4ell-1, k=1/ell and lambda=3-k. Suppose the prescribed transport field is C1, even/odd under the IPM reflections, divergence 2ell, and tangent to the vertical axis. For y>0 write

 v(y)=V2(0,y)=y d(log y),    u(y)=partial_x V1(0,y)=2ell-v'(y).

Assume d is positive and C1 on R. For some positive constants dmin,dmax,nu-,nu+,

 dmin<=d(t)<=dmax,
 |d(t)-D|+|d'(t)|<=C- exp(nu- t) for t<=0,
 |d(t)-ell|+|d'(t)|<=C+ exp(-nu+ t) for t>=0.                 (1)

Choose sigma>0 and kappa>0. For comparisons with an explicit cubic cutoff below, additionally assume sigma<nu-. Define

 p(t)=(D-d(t)-2d'(t))/d(t),
 H(t)=exp(-integral_{-infinity}^t p(s) ds),
 omega(t)=exp(-2sigma t) for t<0, exp(2kappa t) for t>=0.      (2)

The improper integral in H is finite at every finite t. H is positive, H(-infinity)=1, and for a positive constant Hplus,

 H(t)=1+O(exp(nu- t)) as t->-infinity,
 H(t)=Hplus exp(-lambda t)(1+O(exp(-nu+ t))) as t->infinity.   (3)

For an axis density coefficient g(y)=y beta(log y), its transport row is

 v g'+(2u-1)g=y A beta,
 A beta=d beta'+(D-d-2d')beta.                              (4)

Define the target Gamma by

 ||gamma||_Gamma=||gamma/(dH)||_{L2(omega dt)}.

Define the domain B as follows. beta=Hz, where z is locally absolutely continuous, z' belongs to L2(omega dt), and z(+infinity)=0. Equip it with

 ||beta||_B^2=|J|^2+||z'||_omega^2
        +||z-J||_{L2((−infinity,0),omega dt)}^2
        +||z||_{L2((0,infinity),omega dt)}^2,
 J=lim_{t->-infinity}z(t).                                  (5)

The endpoint limits are part of the statement, and their existence follows from the derivative condition. B is a Hilbert space. The cubic trace J is a bounded functional. A:B->Gamma is an isomorphism. Its inverse and cubic coefficient are

 beta(t)=-H(t) integral_t^infinity gamma(s)/(d(s)H(s)) ds,
 J=-integral_R gamma(s)/(d(s)H(s)) ds.                       (6)

The following constants are explicit:

 |J| <= [1/(2sigma)+1/(2kappa)]^(1/2) ||gamma||_Gamma,
 ||beta||_B <= [1+1/(2sigma)+1/(2kappa)
                         +max(sigma^(-2),kappa^(-2))]^(1/2)
                    ||gamma||_Gamma.                      (7)

On B0={beta in B:J=0}, the range of A is precisely the closed codimension-one subspace

 Gamma0={gamma in Gamma: integral_R gamma/(dH)=0}.           (8)

Thus the far-tail condition and J=0 cannot both be imposed without the displayed compatibility condition for the pure scalar transport problem. With the far condition alone, J is an output of the equation.

For the theory author's proposed weight a=17/4, radial far exponent -5/4, take

 sigma=a-4=1/4,
 tau=(8-5/4)/2=27/8,
 kappa=tau-lambda=3/8+k>0.                                 (9)

Then the Gamma norm is equivalent, with positive finite constants determined by (1), to the piecewise scalar norm

 integral_{t<0}|gamma|^2 exp(-t/2)dt
       +integral_{t>=0}|gamma|^2 exp(27t/4)dt.               (10)

These are exactly the radial powers in the norm of an x^4 angular remainder produced by lifting the x^2 y axis forcing into the candidate weight. The actual modal field has the required endpoint orders nu-=2 and nu+=1-k by its established expansions. Positivity of d on the entire axis and quantitative bounds in (1) remain numerical certification obligations. This theorem must therefore be used conditionally for the actual background until those obligations are discharged.

## Derivation of the row and homogeneous solution

Incompressibility of the nonscaling velocity gives partial_x V1+partial_y V2=2ell. Hence u=2ell-v'. Since v'=d+d', differentiating g=y beta gives

 v g'+(2u-1)g
 =y[d beta'+(d+4ell-2d-2d'-1)beta]
 =y[d beta'+(D-d-2d')beta].

The function p tends to zero at -infinity at rate exp(nu- t). At +infinity it tends to D/ell-1=3-k=lambda at rate exp(-nu+ t). Integration proves (3). The definition H'=-pH implies

 A(Hz)=dH z'.                                               (11)

An alternative exact formula, useful for coefficient certification, is

 H(t)=[d(t)/D]^2 exp(-integral_{-infinity}^t [D/d(s)-1]ds).

It follows by integrating the logarithmic derivative of d. This formula is well defined because of (1). No sign of d' is required.

## Endpoint traces, Hardy estimates and completeness

The reciprocal weight is integrable:

 integral_R omega^(-1)dt=1/(2sigma)+1/(2kappa).

Thus z' is in L1, by Cauchy-Schwarz, and every locally absolutely continuous z with z' in L2(omega) has finite limits at both ends. The condition z(+infinity)=0 forces z(t)=-integral_t^infinity z'. Its left limit is J=-integral_R z'. This proves the first estimate in (7).

For t<=0, z(t)-J=integral_{-infinity}^t z'(s)ds. Multiplication by exp(-sigma t) turns this into convolution on the line with the one-sided kernel exp(-sigma r)1_{r>=0}, after extending the negative-half-line derivative by zero. Its L1 norm is 1/sigma. Young's inequality yields

 ||z-J||_{omega,t<0} <=sigma^(-1)||z'||_{omega,t<0}.

For t>=0, z(t)=-integral_t^infinity z'(s)ds. The reverse one-sided kernel has L1 norm 1/kappa, giving

 ||z||_{omega,t>0} <=kappa^(-1)||z'||_{omega,t>0}.

The sum of the two squared bounds is at most max(sigma^(-2),kappa^(-2))||z'||_omega^2. These estimates prove (7). They also show that the derivative map from B to L2(omega) is an isomorphism with bounded inverse. Hence B is complete and Hilbert. Formula (11) proves the asserted isomorphism A:B->Gamma.

The trace functional is nonzero: choose a smooth nonnegative compactly supported z' with nonzero integral. Consequently its kernel has codimension one, and (6) proves (8). The restriction to B0 remains an isomorphism onto Gamma0, with the same upper bound.

## Actual cubic trace and far condition

By Cauchy-Schwarz on a half-line,

 |z(t)-J| <= exp(sigma t)/sqrt(2sigma)
                       ||z'||_{omega,(-infinity,t)} as t<0,
 |z(t)| <= exp(-kappa t)/sqrt(2kappa)
                       ||z'||_{omega,(t,infinity)} as t>0.

The restricted norms tend to zero at the relevant endpoints. Combining this with (3) gives

 beta(t)=J+o(exp(sigma t)) as t->-infinity,
 beta(t)=o(exp(-(lambda+kappa)t)) as t->infinity,

where sigma<nu- was used in the first assertion. In particular g(y)/y->J at0, while g(y)=o(y^(k-2)) at infinity. If chi0 is any smooth radial cutoff equal to1 near0 and zero outside a compact set, beta-J chi0(e^t) has the stated small-origin behavior. This makes the central coefficient a classical trace for the one-dimensional axis variable, without asserting pointwise regularity of the independent two-dimensional weighted remainder.

Because d and H are positive, and their normalized endpoint limits are positive, the normalized functions and their reciprocals are bounded on the whole real line. Substituting (3) in the Gamma norm proves (10). This norm comparison is qualitative unless explicit bounds on d and H are supplied.

## What this repairs and what it does not prove

The earlier phrase 'a weighted 1D space adapted to the jet row' does not define a Banach space or establish closedness of J. Equations (2), (5) and (10) supply such a space for the uncoupled row. The normalization is continuous there and its range restriction is explicit.

The full global Fredholm claim still needs all of the following: a specified bounded lifting of the axis variable into the two-dimensional domain; estimates for transport errors of that lifting; bounded jet-to-remainder and remainder-to-jet coupling; closed domains and adjoints for the remainder operator; its margin modulo a compact term; and a block homotopy whose Fredholm index is actually controlled. The local-strip theorem alone proves none of the interactions with input outside the strip or with an independent axis-jet input. The formal assumptions (E) and (H_m') of the present theory author draft do not explicitly include these obligations. Until they are added or proved, its global Theorem C is OPEN, rather than a completed conditional theorem on fully specified spaces.
