"""Record audited local-circle and finite-D improvements; run once."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
p=root/'08_improved_upper_bounds/paired_local_circles/certified_more';(p/'verification').mkdir(parents=True,exist_ok=True)
(p/'PROOF.md').write_text('''# Three further paired-local-circle upper bounds

For the real Euclidean homogeneous Holder seminorm on R^2, with operators
and compact smooth test supremum as defined in ../../../01_setup/PROOF.md,

    C_(3/10) <= 2.7748077123,
    C_(3/4)  <= 2.6442935978,
    C_(9/10) <= 5.0137426873.

The same constants bound T_xx and T_xy. These are certified upper bounds,
not asserted exact norms. No new bound for R_1^2 is claimed here.

## Proof

Apply the paired local-circle theorem ../PROOF.md with delta=1/64,
512 angular cells per circle, 256 radial intervals, and the 17 phases
j*pi/32, 0<=j<=16. Use the already audited middle-circle and exterior-circle
bounds on the same phase grid. Their sum covers the whole plane. The two
small disks are bounded by

    S=2*a_2(alpha)*delta^alpha/alpha
      +(1+2*delta)^alpha*delta^2/(2*(1-delta)^2),
    a_2(alpha)=2^(1+alpha/2)/(pi*(alpha+2)).

The remaining phase-grid maximum is multiplied by sec(pi/64), as in the
local theorem. No extra cross-disk term is added: it is already present in
the exact paired local-circle density.

The new implementation shares the exact integer flow plans across the
three exponents. This is legitimate because an admissible transport plan
does not have to be optimal. Every flow is nonnegative and every marginal
is checked with exact integer arithmetic. The plan's ordering uses only
Euclidean distance, whose order agrees with its positive alpha powers.
Same-circle edges with the same circular index distance k have the same
certified chord bound 2*sin(pi*min(k+1,256)/512). Summing their integer
masses before multiplication by this cost leaves the exact cost unchanged.
Opposite-circle distances are separately enclosed on each angular product
and at both radial endpoints. The unassigned variation is transported to
its antipodal copy as in the original proof.

The two radial chunks for each alpha cover rows 0 through 255 exactly
once at every phase. The merger checks this coverage and all source
hashes. An independent 90-decimal computation of adverse input endpoints
gives, respectively,

    2.7748077122371975546310730905897626754969584265...,
    2.6442935977670703615149429514531714778975101186...,
    5.0137426872952893321797759044826610065403189972....

Each is below the stated upward-rounded decimal. Independent checks of
96 grouped costs against the original edge-by-edge formula pass, and a
whole alpha=1/2 phase agrees with the earlier implementation. The exact
marginal checks, analytical cost bounds and outward arithmetic supply the
certificate; floating candidate ordering is not used as mathematical
proof of optimality. All inputs are hashed in verification/manifest.json.
''')
cfiles=[f'data/local_circle_composite_a{s}.json' for s in ['30','75','90']]
cpaths=cfiles+['data/local_composites_more_independent.json','code/check_local_composites_more.py','code/certify_local_circles_multi.py','08_improved_upper_bounds/paired_local_circles/PROOF.md','08_improved_upper_bounds/paired_local_circles/certified_more/PROOF.md']
(p/'verification/manifest.json').write_text(json.dumps(dict(time_utc=now,verdict='CONFIRMED',sha256={x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in cpaths}),indent=2)+'\n')
p=root/'07_diagonal_identity_term/finite_geometric_value';(p/'verification').mkdir(parents=True,exist_ok=True)
(p/'PROOF.md').write_text('''# A certified strict separation at alpha = 3/10

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
''')
dpaths=['data/finite_D_lower_a30_geometric_fine.json','data/finite_D_geometric_independent.json','data/geometric_profile_certificate.json','code/check_finite_D_geometric.py','07_diagonal_identity_term/finite_geometric_value/PROOF.md','07_diagonal_identity_term/finite_projection_witness/PROOF.md','07_diagonal_identity_term/finite_projection_extended/PROOF.md']
(p/'verification/manifest.json').write_text(json.dumps(dict(time_utc=now,verdict='CONFIRMED',sha256={x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in dpaths}),indent=2)+'\n')
with (root/'VERIFY_REPORT.md').open('a') as f:f.write(f'''
## V065: Paired local-circle certificates at three more exponents

Date: {now}

Claim: C_(3/10)<=2.7748077123, C_(3/4)<=2.6442935978, and C_(9/10)<=5.0137426873.

Method: Rechecked the shared-plan implementation against the original exact flow and distance formulas, checked complete radial-by-phase coverage, all input hashes and exact integer marginals. Independently recombined all adverse endpoints at90 decimal digits and checked96 grouped costs against edge-by-edge costs. A whole alpha=1/2 pilot phase overlaps the previous implementation.

Result: The independent upper expressions lie below each displayed decimal. Full statement and proof are in08_improved_upper_bounds/paired_local_circles/certified_more/. This improves only the C column; the previously certified D upper bounds are unchanged.

Verdict: **CONFIRMED**.

## V066: Strict finite separation at alpha = 3/10

Date: {now}

Claim: D_(3/10)>=2.8051718212>C_(3/10), with D_(3/10)-C_(3/10)>=0.0303641089.

Method: Applied the extended finite projection theorem with a=3/2, rho=3/14 and the V064 profile factor1.007. Recomputed the regular integral on12582912 interval cells. Checked the exact6144-row covering, all source hashes, analytic local and tail terms, and a separate90-decimal adverse-endpoint calculation. Independent Gaussian value1.5600784065 is inside the regular enclosure.

Result: The independent lower expression exceeds2.80517183631; the conservative displayed lower decimal exceeds the V065 upperC decimal by0.0303641089. Standalone proof and manifest:07_diagonal_identity_term/finite_geometric_value/. The older geometric recombination2.7752393297 is superseded by this stronger certified value.

Verdict: **CONFIRMED**.
''')
with (root/'NOTES_FOR_TEAM.md').open('a') as f:f.write(f'''
## {now}: V065/V066, improved upper bounds and C_.3<D_.3

CONFIRMED C_.3<=2.7748077123, C_.75<=2.6442935978, C_.9<=5.0137426873. New files data/local_circle_composite_a30/a75/a90.json; standalone proof under paired_local_circles/certified_more. Shared exact plans checked independently, full90-digit endpoint recombination passed. D upper values unchanged.

CONFIRMED D_.3>=2.8051718212, so D_.3-C_.3>=0.0303641089. File data/finite_D_lower_a30_geometric_fine.json is now audited and may enter the report and table. Proof07_diagonal_identity_term/finite_geometric_value/PROOF.md. It uses the geometric factor1.007 and12582912 certified cells. This is the sixth listed finite strict separation. The weaker data/finite_D_lower_a30_geometric.json is superseded. I am next testing the identity-redistributed paired local-circle upper method for D, with full phase interval[0,pi] and the required interpolation correction.
''')
file=root/'code/build_verified_table.py';text=file.read_text().replace("['local_circle_composite_a50.json']","['local_circle_composite_a30.json','local_circle_composite_a50.json','local_circle_composite_a75.json','local_circle_composite_a90.json']").replace("'finite_D_lower_a30.json']","'finite_D_lower_a30.json','finite_D_lower_a30_geometric_fine.json']");file.write_text(text)
