from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
p=root/'08_improved_upper_bounds/paired_local_circles/certified_half';(p/'verification').mkdir(parents=True,exist_ok=True)
(p/'PROOF.md').write_text('''# Certified upper bound at exponent one half

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
''')
paths=['08_improved_upper_bounds/paired_local_circles/PROOF.md','08_improved_upper_bounds/paired_local_circles/certified_half/PROOF.md','code/certify_local_circles_greedy.py','code/local_circle_greedy.py','code/combine_local_circle_upper.py','code/check_local_circle_cells.py','code/check_local_composite.py','data/local_circle_chunks/a50_p0_8.json','data/local_circle_chunks/a50_p8_17.json','data/middle_circle_certificate_n512.json','data/far_circle_certificate_fine.json','data/local_circle_composite_a50.json','data/local_circle_independent_checks.json','data/local_circle_composite_independent.json']
manifest=dict(time_utc=now,verdict='CONFIRMED',claim='C_(1/2) <= 2.1970179509',sha256={x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in paths})
(p/'verification/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
with (root/'VERIFY_REPORT.md').open('a') as f:f.write(f'''\n## V063: Complete paired-local-circle upper certificate at one half

Date: {now}

Claim: C_(1/2)<=2.1970179509 for the homogeneous seminorm and compact smooth test supremum.

Method: Applied V058, checked the exact radial-by-phase covering and every source hash, and audited exact integer marginal checks and Arb distance costs. Independently recombined all adverse source endpoints at90 decimal digits. Real-coordinate diagnostics checked63325 masses,1013200 sign samples and12792 distances.

Result: Independent upper endpoint2.19701795084725022930187889284844229253... is below the displayed decimal. The maximizing certified grid phase is3pi/8. Complete standalone statement, proof and input manifest are in08_improved_upper_bounds/paired_local_circles/certified_half/. This improves V054's C value; its D value remains unchanged.

Verdict: **CONFIRMED**.
''')
with (root/'NOTES_FOR_TEAM.md').open('a') as f:f.write(f'''\n## {now}: V063, improved C at one half

CONFIRMED C_(1/2)<=2.1970179509, replacing2.2179196588. Paired local-circle method V058, complete512-angle by256-radius by17-phase coverage, combined with the existing middle/exterior certificates. No separate cross-disk term. Independent90-digit endpoint2.19701795084725. The safe decimal and provenance are in data/local_circle_composite_a50.json; standalone proof and manifest in08_improved_upper_bounds/paired_local_circles/certified_half/. D upper is still2.6482833363. I am extending this local method to other exponents and checking the new sharper projection-profile factors1.007 at.3 and1.021 at.5. Please audit the full-geometry profile reduction in07_diagonal_identity_term/geometric_profile_constant/PROOF.md.
''')
# Make the already-audited new family available to the table selector.
f=root/'code/build_verified_table.py';s=f.read_text();old='    LD={a:list(values) for a,values in L.items()}';new='''    for name in ['local_circle_composite_a50.json']:
        path=Path('data')/name
        if (ROOT/path).exists():
            for row in load(path)['rows']:
                add(C,row['alpha'],Fraction(row['safe_upper_C']),'paired local, middle and exterior circles',path)
    LD={a:list(values) for a,values in L.items()}''';assert old in s;s=s.replace(old,new);f.write_text(s)
