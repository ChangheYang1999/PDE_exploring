# Objective-span audit for candidate017

## Statement and exact scope

For odd n and integer K with 2K+1>=n, define
phi_(n,K)=r(1+r^2)^(-2)[r^2/(1+r^2)]^K sin(n theta).
Let A consist of the analytic weak-probe rows in the recorded stages
007 to013, followed by the exact quotient of013 to017. The first stage
has27 first-sine rows; the second has those27 rows and the40 rows
n=3,5,...,17, K=(n-1)/2+s, s in{0,8,32,128,512}.
Every probe with n in{19,23,25,29,31} and
K in{600,900,1200,1800,2400} lies outside span_R A. The extra diagnostic
(21,522) also lies outside this span, but is not a member of that25-probe
register. The historical scope starts at007; no earlier or unrecorded
experiment, blindness, sampled-vector independence or statistical
independence is claimed.

## Proof

For r>0 divide a proposed linear dependence by the positive function
r(1+r^2)^(-2) and take its full-circle sine-n Fourier coefficient.
Every objective row vanishes under this projection because n>=19
whereas each objective angular frequency is at most17. The proposed
probe has coefficient t^K>0 for0<t<1, a contradiction. This proves the
claim without relying on the relative sizes of K. Smoothness at zero
follows because r^(2K+1)sin(n theta) is a harmonic polynomial of degree n
times a nonnegative even radial power. The probe and its gradient decay
at infinity. The full conditional weak theorem and cutoff justification
are in ../scaled_factored_weak/PROOF.md; no residual value follows from
the span argument.

## Binding the recorded computation

The verifier reads the immutable raw coefficients and their manifests,
compares complete row lists against both frozen shell commands and JSON
metadata, and binds completed run logs containing the output hashes and
row counts. It checks that013 started from007 and017 from the exact
quotient of013. The independent quotient identity N4-218 and all its
inputs are rehashed. The generic snapshot parent field is not substituted
for the actual initialization chain. The radius50 addition appends252
zero-initialized generators in21 blocks (j=1..3,m=9..15); its declared
specification is checked separately and no claim of independence of the
252 new directions is inferred from the old quotient rank.

The inspected Problem3 source constructs precisely the stated analytic
weak probes before numerical quadrature. Its parent Problem2 contains
sampled residual and derivative penalties; these are not analytic weak
rows, but they still contain information about the residual. This audit
does not establish independence from that information or accuracy of the
optimization quadrature. The register time must precede the snapshot.
The register is public and choosing its best member after a FLOAT screen
is allowed, with no maximum over uncomputed probes claimed.

All original publisher code is read as text only. The exact register,
source hashes, proof, own verifier and result are retained alongside.
