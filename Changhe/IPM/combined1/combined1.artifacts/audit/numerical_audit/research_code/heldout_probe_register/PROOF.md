# A fixed family of independent held-out weak probes

## Statement and exact test family

For an odd integer n>=1 and integer K>=(n-1)/2, define on R^2

    phi_(n,K)(r,theta)=r(1+r^2)^(-2)
                       [r^2/(1+r^2)]^K sin(n theta).

Fix the25 pairs in

    n in {19,23,25,29,31}, K in {600,900,1200,1800,2400}.  (1)

This family is registered before candidate015 and candidate016 snapshots
are inspected by this lane. The intended role is a held-out test of the
optimizer's output, following theory_v04 section6. It does not by itself
supply any residual or correction-distance value.

Let A be the complete finite set of probe rows actually used by an
optimizer. Suppose each row is a finite linear combination of
phi_(m,L), and in angular frequency n its nonzero polynomial powers L
belong to a finite set E_n which excludes K. Then phi_(n,K) does not
belong to the real linear span of A. In particular, if every objective
row has degree at most527 in each frequency, every probe in(1) lies
outside that span. The actual objective list must be checked and bound
to each candidate before this conclusion is attached to that candidate.
A declaration alone is not an objective audit.

## Proof

For r>0 put t=r^2/(1+r^2), so0<t<1 and r(1+r^2)^(-2)>0. If a linear
combination of objective probes equalled phi_(n,K), divide by this common
positive radial factor and take the full-circle sine n coefficient.
Angular orthogonality removes every other frequency and gives

    t^K=sum_(L in E_n) a_L t^L, for every0<t<1.

The difference is a polynomial which vanishes on an interval, so all its
coefficients vanish. Its coefficient of t^K is1 because K is not in E_n,
a contradiction. This proves the statement for arbitrary finite linear
combinations within the declared objective space. The same argument
proves linear independence of distinct pairs(n,K).

The probes are smooth at the origin: r^(2K+1)sin(n theta) is a homogeneous
harmonic polynomial of degree n times the even power r^(2K+1-n). Their
denominator is a positive integer power of1+r^2. They decay asr^-3 and
have bounded gradient. Thus they are admissible in the conditional L2
weak-test theorem in ../scaled_factored_weak/PROOF.md. That theorem, with
its canonical velocity, distributional products and fixed-c hypotheses,
explains how a complete residual pairing and full weak norms produce a
necessary distance. It does not follow from choosing a held-out probe.

## Provenance and limits

The immutable register records the exact integer pairs, the real UTC
registration time, the hash of theory_v04 and the optimizer information
available then. Candidate-specific audits must verify all objective rows,
including rows from earlier optimization stages when claims concern the
whole training history. Every tested probe and its status as a design or
held-out row is recorded. Reporting a largest certified value means the
maximum over the finite set actually certified, never a maximum over all
possible probes. Selecting the strongest member after evaluating the
registered family is permitted, but does not change its finite scope.

Different radial powers alone do not prove independence if an objective
contains higher polynomial combinations that span them. The polynomial
coefficient test above must therefore use the full objective space.
No convergence, optimizer-quality, span-floor or existence assertion is
made by this register.
