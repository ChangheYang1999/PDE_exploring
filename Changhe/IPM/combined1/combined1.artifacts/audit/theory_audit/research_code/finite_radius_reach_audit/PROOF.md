# Finite-radius bound for the endpoint certificate, and audit of its quantifiers

This is the independent T4 audit of sections 1 to 4 of T2's
The T2 falsification review of the endpoint and the report summary revision 1. The proof was written before
this topic's checker. Numerical values below are claims to be verified by
that checker. No existence or nonexistence theorem is asserted.

## Setting and exact claim

Use the stationary S1 endpoint setting and canonical velocity, including
its contact term, of T4-335, T4-414 and T4-425. A real C1 correction h has
finite H_q(h), the maximum of the two weighted suprema of h and its
Euclidean gradient with weights (1+r)^(-q) and (1+r)^(1-q). All endpoint
expansion and radial-error hypotheses of those results remain required.
Set c=4076476460239181/2251799813685248, q=1/c-4,
delta=1-1/c, kappa=1-q=4+delta, D=c*kappa=5c-1 and
alpha=-2q-2. They satisfy delta,kappa,D,alpha>0 and q+1<0.
Let B,Hmin,g0 be positive and vmin>=0. For a measurable nonnegative
coefficient e(s), define

 T[e](r)=kappa*r^kappa*integral_r^infinity e(s)s^(-kappa-1)ds.

For some R>=2 the nonnegative chosen radial-error majorant obeys

 ehat(r)>=(Hmin/D)(vmin+g0*T[e](r))r^(-delta), r>=R.

This is a lower bound on a chosen upper error estimate, not on the
actual error of h. The CI certificate produces

 J^2=integral_R^infinity [B-sqrt(2*pi)*ehat(r)]_+^2 r^(2q+1)dr.

Suppose e(s)>=f(s)=min(Ef,lambda*(5/s)^delta) for s>=R,
where Ef>0, lambda=1/2+5*2^(1-q), and all integrals defining T[e]
are finite. For any M>0 put E1=T[f](M),

 S=2*delta^2/[alpha*(alpha+delta)*(alpha+2*delta)],
 r0(E)=[sqrt(2*pi)*Hmin*(vmin+g0*E)/(D*B)]^(1/delta),
 C(E)=B*r0(E)^(q+1)*sqrt(S).

Then, including when M<R,

 J <= sqrt(C(E1)^2+B^2*M^(2q+2)/alpha).                 (1)

This theorem also applies when e is an infimum of an explicitly listed
family of valid coefficients, provided every listed coefficient has
the stated floor. It does not assert that Ef is a lower bound on every
possible valid coefficient.

## Proof

T is positive, so T[e](r)>=T[f](r) wherever it is used. Changing variables
s=rt gives T[f](r)=kappa*integral_1^infinity f(rt)t^(-kappa-1)dt.
As f is nonincreasing, T[f] is nonincreasing. Thus for R<=r<=M,
T[e](r)>=E1. The inner integrand is at most the constant-E1 integrand.
Its integral can be extended from [R,M] to (0,infinity).
Substitute r=r0*u. The positive part vanishes for u<=1, and the
remaining integral is

 B^2*r0^(2q+2)*[1/alpha-2/(alpha+delta)+1/(alpha+2*delta)]
 =C(E1)^2.

For r>=max(R,M) discard the nonnegative subtracted error. The remaining
integral is at most B^2*integral_M^infinity r^(2q+1)dr
=B^2*M^(2q+2)/alpha. Adding proves (1). If M<R, the first region is
empty and the second estimate alone suffices. Nonnegativity avoids any
cancellation issue; the convergence uses q+1<0.

For numerical evaluation let u=5*(lambda/Ef)^(1/delta). Direct
integration, splitting at u, gives

 T[f](r)=Ef*[1-delta/(kappa+delta)*(r/u)^kappa], r<=u;
 T[f](r)=lambda*(5/r)^delta*kappa/(kappa+delta), r>=u.

The formulas agree at u and are decreasing. Checking one M establishes
(1); an optimization or a claim of a globally optimal M is unnecessary.

## Endpoint data and constant-coefficient test

For each of 007, 013 and 014, use its exact sine coefficient dictionaries
A=F12, P and Theta0. Circle measure is dtheta on [0,2*pi]. Then

 B=sqrt(pi*(sum A_n^2-(sum A_n*P_n)^2/sum P_n^2))/(4*c),
 g0=sum n*Theta0_n,
 Phi=abs(q*(A*P'-A'*P))/(4*c*sqrt(q^2*P^2+(P')^2))

at the stored rational angle theta_star. The denominator is positive.
The audited endpoint equation implies H>=Phi>H0, where H0 is respectively
999775,999745,999748. With p=1/c+2, the exact leading reference velocity
at angle zero has magnitude

 v0=abs((p-1)*sum n*Theta0_n/(p^2-n^2)).

For constant coefficient E, the upper bound C(E) implies the necessary
condition, for reaching a target beta,

 E <= D*B/(sqrt(2*pi)*Hmin*g0)
          *(B*sqrt(S)/beta)^(delta/(-q-1))-vmin/g0.      (2)

Replacing sqrt(S) by 1/sqrt(alpha) gives the weaker cutoff test.
The universal-class lower bound is
Emin=(-q-1)/[2*(-q)*(-q-3)]>0.7930365. It is a lower bound on a valid
universal coefficient, not a proved valid coefficient itself.

## Verified consequences to be checked

Use exact printed target radii in data/parameters.json. Auxiliary
one-decimal-unit brackets from T2 are checked as mathematical intervals;
the bare words 'rounded up' do not prove that an unprinted exact family
ceiling lies in those brackets. No such location is assumed here.
For constant coefficients, (2) excludes every admissible universal
coefficient at the listed targets from 3.5125e-7 upwards. At 2^-23 it
also excludes them if V>=v0 is retained. At 2^-25 and 6.8626e-8 the
optimistic threshold using Hmin=Phi and vmin=v0 is above Emin. This
leaves the test inconclusive there; it does not construct a valid E,
a stationary correction, or a successful certificate. Larger actual
H or V can lower the threshold.

Formula (1) with M=114000, Ef=Emin, Hmin=H0, vmin=0 gives J<1.43912e-7.
With M=122000, Ef=Emin, Hmin=Phi, vmin=v0 it gives J<1.14141e-7<2^-23.
With M=108000, Ef=1747261/1000000, Hmin=H0, vmin=0 it gives
J<2.66323e-8<2^-25. Thus the currently chosen list consisting of the
coefficient 1.747261 and T4-410 estimates, whose pointwise floors are
proved in T4-425, cannot reach any of the thirteen printed target
radii. This does not exclude a smaller as-yet unproved universal
constant at the two smallest targets, nor an additional stronger
coefficient absent from the list. The statement concerns the ability
of this CI certificate to reach the specified target, not the
existence of a solution in a smaller ball of the family.

The constant 1.747261 alone gives a crude cap below 1.66122e-8 and a
retained-shape cap below 1.89061e-9. The older inputs B<=85020,
H>=33917, E>=133, G>=28.5227 give the historical crude cap below
9.28e-11. Updating these inputs yields a weaker proved upper bound.
It does not logically refute the proposition that the actual full CI
value is below 9.28e-11, because neither a lower bound on that value
nor realizability of the optimistic majorant has been supplied.

The R1-038 threshold for E*sqrt(2*pi)*Hmax/B is
D*(B/(beta*sqrt(alpha)))^(delta/(-q-1))/g0. At beta=25/54684 it is
below 7.9417, while at the exact graded ceiling 50/(651*sqrt(28248))
it exceeds 7.942167. These targets must not be interchanged.
If Hmax is a budget for a nonempty set of stationary corrections,
Hmax>=H0>=999745; then Emin*sqrt(2*pi)*H0/B>23.37502 exceeds all three
R1-038 thresholds, including the exact graded target. A smaller
budget would exclude those corrections by the endpoint lower bound.

## Audit verdicts and dependencies

CONFIRMED: the new finite-radius integral bound, the finite arithmetic
replayed by this topic, the scoped constant-coefficient obstructions,
the current-list failure, and the exact-versus-rounded graded distinction.
REFUTED: 'excluded exactly when the threshold is below Emin' as a
claimed equivalence from these premises; 'Emin itself is in the class'
if 'class' means actual admissible universal estimates; and the inference
that a passed necessary test disproves the universal obstruction.
OPEN: whether some valid improved universal coefficient permits either
small target; whether the full current certificate exceeds 9.28e-11.
The stale use of the historical proof must be withdrawn, without claiming
a counterexample to its conclusion for different current inputs.

All dependencies are copied with hashes: T2 revision 1 and its code,
results and log, T4-414/425/432 proofs and endpoint data, and theory_v03/04.
T2's code is inspected but never executed or imported. The independent
checker reconstructs B, Phi, v0 and all analytic quantities from exact
JSON at 768 bits, and checks T2's displayed bounds by rational comparison.
No web service, model client, server, JavaScript, cluster or Lean build
is run. Opus collaboration is the continuing exchange with the configured
Opus 5.5 theory lanes; runtime provider identity is not independently
observable here.
