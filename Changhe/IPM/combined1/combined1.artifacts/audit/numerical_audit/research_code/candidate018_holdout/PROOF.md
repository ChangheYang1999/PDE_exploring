# Recorded objective-span audit for candidate 018

## Statement and hypotheses

For odd n and integer K >= (n-1)/2 define
phi_(n,K) = r(1+r^2)^(-2) [r^2/(1+r^2)]^K sin(n theta).
The recorded continuation from immutable candidate 016 to 018 retains
its 67 analytic weak objective rows: 27 rows with n = 1 and the 40 rows
n in {3,5,...,17}, K = (n-1)/2 + s, s in {0,8,32,128,512}.
The exact list and preceding history from 007 through 013 and its
quotient to 016 are in ../candidate016_holdout/PROOF.md and its accepted
result. The same 2174 generator shapes are retained in the continuation.

Every probe with n in {19,23,25,29,31} and
K in {600,900,1200,1800,2400}, the 25 registered extension probes, lies
outside the real span of these objective rows. The additional diagnostic
(21,522) also lies outside their span but is not among these 25 probes.
This is a statement about analytic weak rows, not sampled residual or
derivative information, statistical independence, or unrecorded history.

## Proof

For r > 0 divide any proposed linear relation by the positive common
factor r(1+r^2)^(-2), and take the full-circle sine-n Fourier coefficient.
Every objective row has n <= 17 and its projection vanishes. The proposed
probe has coefficient t^K > 0 for 0 < t = r^2/(1+r^2) < 1, a contradiction.
Appending another copy of the same objective rows does not enlarge the
span. The inherited 007-to-016 proof therefore applies also to 018.
Smoothness of the probes at zero follows by factoring the degree-n
harmonic polynomial from r^(2K+1) sin(n theta). Their rational radial
factors and derivatives decay at infinity. The complete conditional
weak-distance theorem is ../scaled_factored_weak/PROOF.md.

## Recorded-computation checks

Compare the immutable 018 coefficient metadata, the actual continuation
shell command and the finished run log. Check the parent filename and
exact row list, the retained generator shapes, step count, and recorded
output hash. Bind the accepted 016 objective result and its dependencies.
The current optimizer source is read as text and compared with the
previously frozen 017 source. The launch has no generator-addition setting
and the final metadata records no additions. A current source hash is not
claimed to prove which byte version executed historically; the launch,
finished metadata, and log jointly fix the recorded objective row list.
The inherited public register predates 018. Selection after a FLOAT screen
is permitted and does not imply a maximum over all registered probes.
No publisher code is executed. This result provides no residual bound or
optimizer convergence claim by itself.
