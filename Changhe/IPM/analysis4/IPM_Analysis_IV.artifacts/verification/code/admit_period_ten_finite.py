"""Admit exact Q10 compatibility and the independent first potential log."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,json,re,sys
import sympy as sp
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def checkref(r):assert ref(Path(r['path']))['sha256']==r['sha256']
def read(p):return json.loads(p.read_bytes())
p=argparse.ArgumentParser();p.add_argument('--entry',type=int,required=True);args=p.parse_args();entry=args.entry
ledger=Path('VERIFY_REPORT.md');old=ledger.read_text();assert max(map(int,re.findall(r'^## V(\d+) \|',old,re.M)))==entry-1
root=Path('research/281_period_ten_finite_algebra');v=root/'verification';o=read(v/'obstruction_checks.json');c=read(v/'lead_comparison.json')
assert o['all_checks_pass'] and o['independent_exact'] and c['all_checks_pass'];checkref(c['own_obstruction']);assert c['exact_coefficient_comparisons']==21 and c['real_roots']==len(o['real_roots'])==14
assert all(F(x['interval'][1])-F(x['interval'][0])<=F(1,10**60) for x in o['real_roots']);assert not o['modular_irreducibility'][-1]['possible_proper_factor_degrees'];assert o['ordered_low_products']==190 and o['poisson_identity_orders']==list(range(1,20));checkref(o['prefix_polynomials'])
review=root/'sources/lead_review_20261031T203654Z.md';assert review.exists()
r=Path('research/283_period_ten_potential_log');a=read(r/'verification/checks.json');assert a['all_checks_pass'] and a['coprime'] and a['a_Q_degree']==10 and a['compatibility_degree']==20 and a['real_root_count']==14;assert a['exact_density_and_stream_reconstruction'];checkref(a['source']);checkref(a['prefix']);assert (r/'sources'/review.name).exists()
lead_a=Path('../a4-lead/code/tuned/aQ_Q10.out');lead_raw=lead_a.read_bytes();(r/'sources/lead_aQ_Q10.out').write_bytes(lead_raw)
b=sp.Symbol('b');ap=sp.Poly(sp.sympify(next(x.split('a_Q = ',1)[1] for x in lead_raw.decode().splitlines() if x.startswith('a_Q = '))),b,domain=sp.QQ);assert [str(ap.nth(j)) for j in range(11)]==a['a_Q']
(r/'verification/lead_comparison.json').write_text(json.dumps(dict(all_checks_pass=True,coefficient_comparisons=11,source=ref(r/'sources/lead_aQ_Q10.out'),independent_output=ref(r/'verification/checks.json')),indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat(timespec='seconds');coefficient_hash=sha256(','.join(reversed(o['primitive_coefficients'])).encode()).hexdigest();patterns=[(x['prime'],x['factor_degrees']) for x in o['modular_irreducibility']];assert coefficient_hash=='c133c2f4811e855673ffa8f2572a1c04dc8eb1dbe9447779a386463aea6ed720'
results=[(root,entry,'Period-ten exact compatibility algebra',f'The primitive compatibility polynomial at delta1/5 has degree20, is irreducible over the rationals and has exactly fourteen simple real roots.',f'Exact signed Cartesian recurrence through20, coefficientwise Poisson checks through19, rational Sturm intervals, verified finite-field factors and exact comparison with the separate polar recurrence.',f'All21 polynomial coefficients and the exact obstruction scale agree. The modular factor-degree patterns {patterns} exclude every proper rational factor degree. Each of the fourteen roots is isolated to width at most1e-60. The190 ordered nonlinear products took{o["actual_elapsed_s"]:.6f}seconds. Primitive descending coefficient hash:{coefficient_hash}.','PROVED_FINITE_ALGEBRA',v/'obstruction_checks.json'),(r,entry+1,'Period-ten necessary first common-potential logarithm','Every real compatibility root requires a nonzero order-ten r^2 log(r) common-potential correction for nonzero leading amplitude.','Independent polar prefix, exact comparison with the Cartesian coefficients, rational coprimality with the degree20 compatibility polynomial, and reconstruction of both density and stream.',f'All{a["polar_cartesian_coefficients"]} prefix coefficient comparisons and{a["reconstruction_coefficients"]} reconstruction comparisons pass. All11 coefficients of a10 agree with the lead independent polynomial. The degree10 polynomial a10 is nonzero and coprime to the compatibility polynomial; beta10-alpha10=a10/4. The computation used{a["ordered_products"]} ordered products and took{a["actual_elapsed_s"]:.6f}seconds.','PROVED_FINITE_POTENTIAL_LOG',r/'verification/checks.json')]
notes=[]
for base,i,title,claim,method,result,verdict,evidence in results:
 proof=base/'PROOF.md';(base/'sources'/f'PROOF_before_V{i}.md').write_bytes(proof.read_bytes());s=proof.read_text();start=s.index('Status:');end=s.index('\n',start);s=s[:start]+f'Status: PROVED finite statement, admitted V{i}. Infinite convergence is a separate claim.'+s[end:];s+=f'\n## Completed verification\n\nAdmitted {now}. {result}\n';proof.write_text(s);snapshot=base/'sources'/f'PROOF_at_V{i}.md';snapshot.write_bytes(proof.read_bytes())
 data=dict(admitted_at_utc=now,ledger=f'V{i}',verdict=verdict,all_checks_pass=True,evidence=ref(evidence),proof=ref(snapshot),independent_review=ref(base/'sources'/review.name))
 if base==root:data.update(root_count=14,degree=20,primitive_descending_coefficients_sha256=coefficient_hash,independent_comparison=ref(v/'lead_comparison.json'))
 else:data['compatibility']=ref(v/'obstruction_admission.json')
 path=base/'verification'/('obstruction_admission.json' if base==root else 'admission.json');path.write_text(json.dumps(data,indent=2)+'\n')
 old+=f'\n## V{i} | {now} | {title}\n\n**Claim.** {claim}\n\n**Method.** {method}\n\n**Result.** {result}\n\n**Verdict: CONFIRMED and PROVED as a finite statement.** No all-index convergence, explicit radius or nonvanishing of the second possible potential logarithm follows from this entry. Evidence: {path}.\n';notes.append(f'V{i}: {claim} {result}')
ledger.write_text(old);p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: Q10 finite algebra and first logarithm admitted\n\n'+'\n\n'.join(notes)+'\n\nThe all-index response and convergence checks remain separate.\n\n'+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: AdmittedV{entry}/V{entry+1}, exact Q10 finite compatibility algebra and required first common-potential logarithm.\n')
with Path('research/INDEX.md').open('a') as f:f.write(f'\nUpdate {now}:281 and283 finite statements are PROVED inV{entry}/V{entry+1}.\n')
print(json.dumps(dict(at=now,entries=[entry,entry+1],coefficient_hash=coefficient_hash,patterns=patterns)))
