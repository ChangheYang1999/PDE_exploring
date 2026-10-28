# A certified strict separation at alpha = 3/10

For the real Euclidean homogeneous Holder seminorm on R^2 and the quotient
operators defined in ../../01_setup/PROOF.md,

    C_(3/10) <= 2.7748077123 < 2.8051718212 <= D_(3/10).

In particular D_(3/10)-C_(3/10)>=0.0303641089. The same statement holds
when the norms are defined as suprema over real smooth compactly supported
test functions. These inequalities do not assert either norm exactly.

## Complete deduction from the explicit witness

Use the function in ../finite_projection_witness/PROOF.md with a=3/2,
rho=3/14 and alpha=3/10. The extended admissibility proof in
../finite_projection_extended/PROOF.md applies since rho=a/7<1. The full
geometric profile certificate in ../geometric_profile_constant/certified_values/
PROOF.md bounds its seminorm by 1.007.

Set delta=3/56 and R=4096, and write L=R-1/2=8191/2. The finite witness
proof gives its unnormalized diagonal increment at least

    J_regular + 2*A_alpha*delta^alpha/alpha - E_local - E_tail + 1/2,
    A_alpha=Gamma((alpha+2)/2)/(2*sqrt(pi)*Gamma((alpha+3)/2)),
    E_local=2*alpha*delta/(pi*(1-2*delta))
          +2*(1+delta)*delta^(alpha+3)/((1-delta)^4*(alpha+3)),
    E_tail=2^alpha*L^(alpha-1)/((1-alpha)*(1-1/(4*L^2))^2).

The final 1/2 is the exact local identity contribution. Principal values
and the infinity tail are justified in the cited witness proof. Enclose
J_regular on its three disjoint radial patches using 2048 radial and 2048
angular cells per patch, 12582912 cells in total. Every cell is evaluated
by outward Arb inclusion. The four job chunks partition all 6144 rows
exactly once. Their sum has lower endpoint greater than
1.5313375386145729632198103720 and upper endpoint less than
1.5886775388031331882893332298. A separate Gaussian computation gives
1.5600784065, consistent with that enclosure but not used to certify it.

Divide the displayed increment by 1.007. Independent 90-decimal
recombination of adverse input endpoints gives a lower expression greater
than 2.80517183631786508956, so rounding down to 2.8051718212 is safe.
The source files, coverage and analytic terms are independently checked
in data/finite_D_geometric_independent.json. The C upper bound is the
proved paired-local-circle value in ../../08_improved_upper_bounds/
paired_local_circles/certified_more/PROOF.md. Subtracting the exact displayed
decimals gives the asserted positive gap. Finally use the compact smooth
approximation theorem in the setup for the original test class.
