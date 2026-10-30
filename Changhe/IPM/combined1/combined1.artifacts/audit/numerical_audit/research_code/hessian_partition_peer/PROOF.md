# Acceptance of the independent exact radial Hessian partition

## Exact statement and hypotheses

Fix the raw reference016 or017, rho, delta, and endpoint hypotheses of
../scaled_hessian_peer/PROOF.md. Its complete-plane certificate is a
required accepted dependency. Let r0=1/50 and
R=4178237423365963/500000000000, both exact rationals. Set
D0={r<r0}, Dm={r0<=r<=R}, Df={r>R}, and

    E_ab(D)=integral_D |partial_a partial_b rho|^2, ab=xx,xy,yy,
    X_D^2=E_xx(D)+E_xy(D), Y_D^2=E_xy(D)+E_yy(D),
    H_D^2=X_D^2+Y_D^2,
    kappa_D^2=((log(2)-1/2)X_D^2+(3log(2)-2)Y_D^2)/(16pi).

We accept the complete finite partition in N4-273 through T4-367. The
squared energies and squared metrics add over these disjoint domains.
Their square roots do not add. The restricted kappa_D are energy
quantities; only the full-plane kappa has the previously proved
Hilbert-Schmidt interpretation. No localized kernel identity is used.
For both candidates more than99.998percent of the kappa-squared energy
omitted from Dm is in Df. This compares exact energies of the nominal
rational annulus. It is not a quadrature error certificate.

## Complete primitive proof

The complete Hessian proof gives

    E_ab=(pi/2) sum_ell integral_0^1 v^b N_ell(v)/D_ell(v) dv,
    b=ell delta/2-1>-1, v=1/(1+r^2),
    N_ell(v)=(1-v) numerator(W_ell(1-v)).

Each denominator is a product of positive factors(1+av)^k with a>0.
Exact division and partial fractions, checked by multiplication back,
write N/D=P(v)+sum c_(a,k)/(1+av)^k. For0<V<=1, the substitution v=Vu
and Euler's integral yield

    integral_0^V v^b/(1+av)^k dv
      =V^(b+1) 2F1(k,b+1;b+2;-aV)/(b+1).

The term p_j v^j has primitive p_j V^(b+j+1)/(b+j+1).
Since b>-1 and a>0, all these integrals converge and their denominators
never vanish. Direct outward Arb evaluation gives a containing interval.
Our independent calculation obtains the same primitive from the
pole-order recurrence; the exact field and angular-product proofs are
separate. The acceptance checks all270 primitives for45groups at3cuts
per candidate, with every exact identity and exponent retained.

Let T_ab(V) be pi/2 times the full sum of primitives. Define
Vf=1/(1+R^2) and Vm=1/(1+r0^2). Reversing radial order proves

    E_ab(Df)=T_ab(Vf),
    E_ab(Dm)=T_ab(Vm)-T_ab(Vf),
    E_ab(D0)=T_ab(1)-T_ab(Vm).

The endpoints have zero area. Their exact sum is T_ab(1), agreeing with
the accepted complete-plane result group by group. Positivity follows
from the spatial integral definitions and the actual containing balls
are strictly positive. Signed branch groups need not be positive.
Scalar metrics follow from their definitions, and squaring additivity
follows from linearity. Recompute all domain metrics, square roots and
positive logarithmic weights from the component energies.

## Omission and mesh diagnostics

For Q equal to X,Y or kappa, let O=Q_D0^2+Q_Df^2. Then the omitted
squared fraction is O/Q_whole^2 and the far fraction of that omission
is Q_Df^2/O. The accepted balls show O>0 and the kappa far fraction is
greater than49999/50000. Subtracting Q_Dm from Q_whole gives the actual
norm difference caused by omitting those two exact domains. Comparing
Q_Dm with the saved FLOAT diagnostic yields a signed numerical
difference, which also includes rounded coefficients and operations.
It supplies no general bound on that FLOAT evaluator.

The selected Gaussian nodes in the diagnostic have a separate FLOAT
mesh audit. The two independently reconstructed rules select416nodes
in13complete32-node panels. Binary64 panel endpoints are not identified
with the exact rational cutoff R. Compare the rows and endpoints as
FLOAT records only. No quadrature enters the exact energy integration.

## Dependencies, binding and limits

Bind the raw files, own complete partition, T4 whole-plane result, both
manifests, frozen publisher diagnostic and mesh source, and every code
and proof input by SHA256. Recheck exact cuts, all group maps, the270
primitive overlaps, component telescoping,64 domain scalars, positive
ratios and the separately labeled mesh rows. Retain all source files
locally or by an already frozen identical content hash. Execute only
the own acceptance code. The full informal argument precedes execution.

This confirms the stated energy partition only. It establishes no
global theta bound, no inverse estimate, and no existence theorem. There
are no formal sources or formal-build claims; the accompanying numerical
certificates and analytic dependencies specify the scope completely.
