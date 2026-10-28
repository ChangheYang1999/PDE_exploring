from pathlib import Path
import json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]
entries=[('V208',R/'05_team_audit/report_v30/decimal_checks.json','Version30 numerical changes',
'All ten D upper endpoints, all upper/lower ratio ceilings, the independent lead endpoint strings and the 0.8680 endpoint remainder ceiling are valid. Exact rational arithmetic checks rounding; the remainder uses384-bit balls. The alpha3/10 ratio1.0666 is conservative:1.0665 already suffices for the exact stored endpoints. The frozen input table is table_v198.json. The first validator required the least ceiling and failed on this harmless extra rounding; it was corrected to test validity, retaining the least ceiling in the output. No endpoint value was changed. The three prose findings in PROOF.md remain required corrections; no blanket acceptance of those sentences is implied.'),
('V209',R/'08_improved_upper_bounds/explicit_second_term/sharp_deficiency/numerical_values/accepted.json','Directed sharper deficiency constants',
'The exact512-term positive rational Catalan enclosure contains an independent768-bit Catalan ball. Every finite and uniform expression is enclosed at384bits and independently regrouped at768bits. Rational adverse endpoints and upward decimal rounding pass. For0<alpha<=1/100 the linear coefficients are at most2.4944998518 for C and2.7441857685 for D; combining V206 retained reflection lowers the latter to2.7440079435. Thus simplified coefficients2.4945 and2.74401 are certified. Finite C upper at1/1000 is637.0245793941; finite D uppers with reflection at1/1000,1/200,1/100 are637.4271544033,128.1422791836,64.4940265223. These are fixed rational evaluations, with no radius optimality claim.'),
('V210',R/'08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/numerical_values/accepted.json','Directed exact radial reflection gains',
'Exact rational binomial sums recover J_* and K_*. A256-term positive atanh series encloses log(4/3); all propagated rational gain intervals lie inside384-bit balls, and independent768-bit regrouping lies inside those same balls. All ten positive gains and adverse endpoint subtractions pass. Each uses the original translation-cost base, not an already improved endpoint. Stronger small-alpha V209 values may supersede these two cutoff rows. No new quadrature or global optimization is asserted.')]
with (R/'VERIFY_REPORT.md').open('a') as f:
 for label,path,title,result in entries:
  d=json.loads(path.read_text());time=d['time_utc']
  f.write(f'\n## {label} | {time} | {title}\n\n**Claim.** The displayed numerical conclusions follow from the named accepted analytic bounds.\n\n**Method.** Independent directed evaluation and exact rational endpoint comparison; all registered source hashes checked.\n\n**Result.** {result} Evidence: `{path.relative_to(R)}`.\n\n**Verdict: CONFIRMED** within the stated scope.\n')
p=R/'code/build_verified_table.py';s=p.read_text();anchor='    LD={a:list(values) for a,values in L.items()}';assert s.count(anchor)==1
block='''    path=Path('08_improved_upper_bounds/explicit_second_term/sharp_deficiency/numerical_values/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V209'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        if row['mode']=='finite':
            add(C if row['operator']=='C' else D,row['alpha_or_epsilon'],Fraction(row['safe_upper']),'sharper local deficiency with optional retained reflection, V209',path)
    path=Path('08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/numerical_values/accepted.json')
    approval=load(path)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V210'
    for filename,digest in approval['sha256'].items():
        assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==digest
    for row in approval['rows']:
        add(D,row['alpha'],Fraction(row['safe_upper_D']),'exact radial minorant with symmetric fourth moment, V210',path)
'''
p.write_text(s.replace(anchor,block+anchor))
