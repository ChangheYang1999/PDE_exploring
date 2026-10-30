# Objective-span audit for candidate015

## Exact statement and audited history

For odd n and integer K with 2K+1>=n define

    phi_(n,K)(r,theta)=r(1+r^2)^(-2)
                       [r^2/(1+r^2)]^K sin(n theta).

Let A be the analytic weak-probe rows declared in the two recorded
optimization stages taking candidate007 to candidate013 and then its
exact quotient representation to candidate015. The first stage has27
first-sine rows. The second has the same27 rows together with75 rows

    n in {3,5,...,31}, K=(n-1)/2+s, s in {0,8,32,128,512}.

Then every probe in the pre-registered25-element family

    n in {19,23,25,29,31}, K in {600,900,1200,1800,2400}

lies outside the real linear span of A. This statement concerns analytic
probe functions. It does not concern the rank of their sampled vectors,
statistical independence, or the completeness of an optimization method.
The historical scope starts with candidate007 as the initial input.
Earlier campaigns and unrecorded exploratory choices are not audited here.

## Proof

Set t=r^2/(1+r^2) for r>0 and divide a proposed linear relation by the
strictly positive factor r(1+r^2)^(-2). The sine-n Fourier coefficient
would give t^K as a linear combination of powers with exponents at most
(n-1)/2+512<=527. The polynomial coefficient of t^K is one on the left
and zero on the right, since K>=600. A polynomial that vanishes on(0,1)
is identically zero, so this is impossible. The first-sine rows, including
those with K as large as4096, disappear under the sine-n projection.
This proves the claim. The same argument in
../heldout_probe_register/PROOF.md proves the probes' smoothness and
linear independence.

## Provenance checks

The computation verifies the exact candidate hashes against their
immutable manifests. It parses both frozen shell commands as data and
compares the complete declared probe lists with each output's exact JSON
metadata. The actual run logs must contain the corresponding output
hashes and reported row counts. Candidate015's input must be the exact
quotient of013, whose function identity was independently established in
N4-218. The stored quotient metadata and that audit's input hashes are
checked again. Candidate013's frozen command explicitly starts from the
candidate007 coefficient file. Candidate015's generic manifest parent
field is not used as evidence for this actual initialization chain.

The inspected frozen Problem3 implementation constructs only the stated
weak rows, with the exact analytic functions above before quadrature;
its parent Problem2 adds weighted sampled residual and derivative
squares and sampled background Hessian penalties. These are not extra
analytic weak-probe rows. We do not claim that a new test is independent
of the information in a sufficiently rich sampled residual objective.
The metadata and logs establish the recorded computation, not a complete
historical record of every experiment. The registration time is checked
to precede the immutable015 snapshot time. This audit claims independence
from the declared objective span only, not blindness of the optimizer to
a publicly shared test register.

No numerical weak-test value follows from this algebraic audit. A
necessary L2 correction-distance certificate separately requires the
whole-plane integrals, canonical velocity, fixed-c chart, distributional
products and all hypotheses in ../scaled_factored_weak/PROOF.md.
