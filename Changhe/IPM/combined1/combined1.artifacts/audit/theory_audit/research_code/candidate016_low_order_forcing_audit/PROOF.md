# Candidate 016: independent audit of the low-order forcing obstruction

## Statement

Use Lebesgue measure on R^2 and the unitary Fourier transform. Let F be a
real H^1(R^2) function, J=(1-Delta)^(1/2), Lambda=(-Delta)^(1/2), and
omega(X)=(1+4|X|^2)^(2/5). D denotes the weak Cartesian gradient and D^2
the ordered Cartesian Hessian. For s>=0 and positive weights w1,w2 put

 X_(s,w)(F)^2 = ||omega D^2 J^s F||_2^2
                 + w1 ||D J^s F||_2^2 + w2 ||J^s F||_2^2,
 N_s(F)^2 = X_(s,(16384,262144))(F)^2
                 + 262144*(20/21)||Lambda^(-1)J^s F||_2^2.

An entry not represented by the indicated weighted L^2 function has
value +infinity. Suppose ||F||_2>ell0>0 and ||DF||_2>ell1>0. Then

 X_(s,w)(F)>sqrt(w1*ell1^2+w2*ell0^2),
 N_s(F)>sqrt(16384*ell1^2+262144*ell0^2).                 (1)

For the exact candidate C1-N1-016-legqs25-quot013, coefficient hash
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42,
set c=4076476460239181/2251799813685248, rho=-partial_y Delta chi,
u=(-chi_xyy,chi_xxy), and F=(cX+u).grad rho-rho. N4-341 and N4-373
supply the separately checked whole-plane H^1 component enclosures
frozen in source/G1_acceptance.json. Their strict rational lower
endpoints in data/components.json are

 ell0=0.308886445142524736777066916039,
 ell1=3.726906948019883998020959016407.

With these endpoints, every one of the ten sufficient scalar forcing
tests in data/parameters.json fails. This conclusion is an application
of the independently proved inequality (1) to previously accepted
integrations. The present check does not perform a third integration.

## Proof

Plancherel and the definition of weak derivatives give

 ||J^s F||_2^2 = integral (1+|xi|^2)^s |Fhat(xi)|^2 dxi,
 ||D J^s F||_2^2 = integral |xi|^2(1+|xi|^2)^s |Fhat(xi)|^2 dxi.

For s>=0 the multiplier is at least one. Thus the two norms dominate
||F||_2 and ||DF||_2 respectively. Dropping the nonnegative Hessian
entry gives the first inequality in (1), strictly because both weights
are positive and both lower endpoints are strict. Dropping also the
nonnegative homogeneous negative-norm entry gives the second. If an
entry is infinite the conclusion holds in the extended real order.
No weighted commutator, derivative recovery, inverse, normalization
change or regularity upper bound is needed.

## Finite verification and dependencies

The checker binds all ten frozen sources, this proof and its code. It
also attests, read-only, every source hash of N4-374's 59-input graph;
that attestation is separate from portable reproduction using the
frozen data. It checks the exact candidate, c, endpoints, both containing
norm balls and the wider N3 endpoint balls. For each norm it checks the
31 recorded groups, endpoint integrability b>-1, exact reconstruction
flags, pair counts and recorded precision; it sums the saved group
balls and compares pi/2 times that sum with the saved norm square.
This is a finite consistency audit of accepted moments, not a new proof
of the moment integrals. The underlying N3 and N4 algorithms are the
explicit numerical dependencies of the application.

For each registered row the checker compares s, weights and the exact
threshold to the accepted source-formula audit, computes the positive
rational square in (1), and encloses its square root and threshold
ratio in Arb at 1024 bits. Every integer factor and decimal lower bound
printed by N4-374 must lie strictly below the independent ball. The
rebalanced threshold is exactly 3/327680 and the legacy X3 threshold
is exactly 1/163840; rounded decimal substitutes are not used. All
hashes are rechecked after arithmetic. No peer implementation is run.

## Scope and open work

The scalar sufficient smallness conditions fail at this exact reference.
Their failure neither proves nonexistence nor gives a correction-distance
lower bound. The separate weak-distance theorem has its own hypotheses.
The two named low-order component enclosures suffice: P2, the actual
homogeneous negative norm, Q3 and fractional upper enclosures are unused.
No conclusion transfers to a decaying-weight dyadic norm. Agreement of
all 1024 endpoint bits in the older N3 record remains OPEN because the
frozen N4 balls retain only 100 decimal digits. The enclosing balls and
strict rational endpoints used here are independently consistent. No
existence closure or background inverse is established.
