# Additional independent audit, fixed before execution

Read PROOF and ADDENDUM. The fresh artifact audit must check every exact
output against current file hashes, positivity/finiteness, coverage counts,
span maxima, outward integer ceilings and exact product constants. It also
recomputes all final scalar constants at higher precision without importing
the producing module. The named orders are 3.05,3.06,3.1.

A uniform bound on the whole interval follows by separate monotonic bounds:
put s_-=3.05,s_+=3.1. In R_s^*, replace s,s-1,2^(s-4),2^(s-2) by their
values at s_+, and beta_(s-1),alpha_(s-1) by their values at s_-; leave
alpha_2,alpha_3 fixed. This gives Rbar for every order in the interval.
Since a_s^* decreases, use a_(s_+)^*, and since d_s^* increases use
d_(s_-)^*. The base1+Rbar/d_min is at least1, so raising it to s_+ gives
a uniform inverse bound. Each monotonicity follows from the positive
product formulas in PROOF, rather than from sampled parameter values.

The exact Cartesian recurrence will also be tested against direct
polynomial differentiation: choose nu so that
r^(beta+nu) exp(i m theta)=(x^2+y^2)^ell (x+i y)^m,
then evaluate at (3/5,4/5). Direct monomial derivatives use exact rational
Gaussian coefficients. The recurrence expands Q(D_t) on F(t)=exp(nu t),
so Q(nu) times the exact unit-circle phase gives the same value. Testing
all mixed derivatives through order5 avoids relying only on pure-x
identities. This test supports the implementation; the proof of the
recurrence for arbitrary smooth F is the induction in PROOF.

These checks are additional audits, not third independent canonical
integrations or new high-derivative certificates. A coarse upper inverse
bound is not a lower bound, and does not exclude sharper estimates.
