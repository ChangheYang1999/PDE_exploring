# Certified upper bound at exponent one half

For every real homogeneous Holder function f on R^2, modulo constants,
with [f]_(1/2)=sup |f(x)-f(y)|/|x-y|^(1/2), the normalized operators of
../../../01_setup/PROOF.md satisfy

    [T_xx f]_(1/2) <= 2.1970179509 [f]_(1/2),
    [T_xy f]_(1/2) <= 2.1970179509 [f]_(1/2).

The same statements hold for compact smooth test functions. The operators
on the homogeneous space are defined by convergent principal-value
increments as in the setup.

## Proof

Apply the complete paired-local-circle theorem in ../PROOF.md with
alpha=1/2, delta=1/64, 512 angular cells, 256 radial cells and phases
j*pi/32, j=0,...,16. The two local chunk files listed in the manifest
cover every radial and phase index exactly once. Each extracted mass is
a nonnegative multiple of 2^(-44), dominated by the continuous signed
cell mass uniformly on its radial interval. Every greedy flow is checked
in exact integer arithmetic to have precisely those signed marginals.
Its ordering uses floating distances, which affects only the choice of
feasible plan. Arb upper bounds, not those floating distances, determine
the certified costs. Unextracted variation is paired centrally.

Add the already verified middle and exterior phase bounds, without an
additional cross-disk term. The largest phase sum is at j=12 and is
less than 2.043011603939622988942. The omitted small disks contribute
less than 0.151542482124304925090. The theorem's sine interpolation gives

    C_(1/2) <= S + sec(pi/64) max_j(L_j+W_j+E_j)
            < 2.1970179509.

The complete Arb enclosure and an independent 90-decimal recombination
from exact adverse input endpoints are in the manifest. The independent
value is 2.19701795084725022930187889284844229253... . The discrepancy in
last digits from the Arb midpoint is caused by using all adverse input
endpoints. Independent real-coordinate checks tested 63325 extracted
cell masses, 1013200 sign samples and 12792 distance samples. These are
diagnostics supporting the analytic proof, not a replacement for it.

Rotation identifies the two real operator norms. Real projection gives
the same upper inequalities for complex scalar inputs if desired.
