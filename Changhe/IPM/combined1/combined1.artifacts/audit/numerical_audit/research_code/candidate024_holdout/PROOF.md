# Candidate 024: exact basis, recorded objective and held-out provenance

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
Candidate C1-N1-024-rulem32-legqs25 is the exact rational generator sum
whose raw SHA256 is 3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d.
The generator conventions are those of ../scaled_product_norms/PROOF.md:
chi is the potential, rho=-partial_y Delta chi is the density. A shape
means the tuple (j,m,spec), without its coefficient. The old 1922-shape
list is the exact quotient of candidate013. The added252 shapes have
j in{1,2,3},m=9,...,15 and spec=(legqs,0,N,4,25),N=0,...,11.

The claims to check are: the ordered024 shape list is precisely this
2174-element list, identical to016; its potential and density dimensions
are2174; its recorded initialization is the013 quotient with the252 new
coefficients zero before the recorded Taylor projection; and its12 recorded optimizer iterations use the same
67 analytic weak rows as016 with the radial middle order changed to32.
Counts of attempted and accepted iterations are different and will both
be recorded. The finite run does not identify the optimizer minimum.

For n odd and K integer with2K+1>=n, define

 phi_(n,K)(r,theta)=r(1+r^2)^(-2)[r^2/(1+r^2)]^K sin(n theta).

The67 rows are the27 first-sine exponents listed in the exact metadata
and the40 pairs n=3,5,...,17,K=(n-1)/2+s,s in{0,8,32,128,512}.
Every member of the25 public register and all35 diagnostic pairs
n=19,21,...,31,K=(n-1)/2+s is outside their real analytic linear span.
The historical scope is recorded007 to013 to its exact quotient to024.
No assertion concerns earlier or unrecorded experiments or blindness.

## Basis and density proof

The accepted two-scale theorem in ../joint_scaled_rank_peer/PROOF.md
proves independence and density injectivity for the old1922 shapes plus
252 radius25 and252 radius50 shapes. Its exact abstract list is frozen
and hashed. The proposed024 list is the subset obtained by deleting all
radius50 shapes. A linear relation among a subset extends by zero
coefficients to a relation in the full independent list, so all its
coefficients vanish. The restriction of an injective density map is
injective. Hence both dimensions are2174 once the actual ordered tuples
are checked against this subset. This invokes the already accepted
complete analytic theorem; it does not infer rank from the coefficient
count or a floating matrix. All inputs of that acceptance are rebound.

## Objective span proof and recorded history

For r>0 divide a proposed dependence by the positive factor
r(1+r^2)^(-2). Project onto sine frequency n>=19 over the full circle.
Every recorded objective row has frequency at most17 and projects to
zero; the proposed probe projects to t^K, t=r^2/(1+r^2), which is strictly
positive for0<t<1. This contradiction proves the span claim. The
smooth extension at0 follows from the harmonic polynomial of degree n
and the even nonnegative radial power2K+1-n. The functions decay at
infinity. This statement says nothing about discrete sampled-vector
independence, the residual penalties or statistical independence.

The accepted016 history binds the earlier007/013 rows and exact quotient.
The new024 shell command, raw metadata, run log and literal parser source
are read as text only. They must agree on the input filename, output
SHA256, row list, weights, middle order32 and12 iteration numbers.
The radius25 source branch must append zero-valued coefficients once.
The subsequent a_start=taylor_project(a0,iters=8) is part of the recorded
optimizer preparation; no unchanged post-projection input is asserted.
The old and new commands otherwise specify the same tested parameters.
This checks the recorded comparison, not every floating operation in it.
The016 command specifies IPM_DEVICE=cpu and the024 command specifies
IPM_DEVICE=cuda. Thus their recorded execution environments also differ.
The frozen current024 source is inspected and its modification time
retained, but it is not claimed to be a launch-time source archive.
These records support a finite trial comparison, not an isolated
one-variable experiment or an attribution of the stopping mechanism.

## Hash and chronology check

Freeze the current held-out file, snapshot index, publisher notes and
all immutable snapshot files before comparison. Check every SHA256SUMS
entry. Compute the held-out file's actual SHA256 and locate both the
58586004... claim and the earlier e171c051... claim in the records. A
hash inequality refutes only that claimed byte identity. It does not
show what older bytes existed or whether a probe list was changed.
The manifest may truncate the description, so membership of a hash in
the manifest and in the index must be checked separately.

Compare all60 current pairs with the explicit mathematical list and all
67 actual rows. The public25-probe register has a separately recorded
prelaunch timestamp. The date written in the35-probe document and the
publisher's launch time are recorded assertions, not a new observation
of that earlier event. No unavailable58586004... preimage is invented.

## Scope

All current coefficients and provenance inputs are exact frozen files.
No publisher code, optimizer, GPU or quadrature is executed. No norm,
background margin, numerical conditioning, inverse or existence claim
follows from this basis and history audit. A lower sampled objective
or a short run comparison does not establish why an earlier run stopped.
