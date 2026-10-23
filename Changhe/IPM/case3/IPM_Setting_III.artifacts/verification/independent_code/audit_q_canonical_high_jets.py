"""Registered exact Q input and higher physical/core Taylor tables."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,hashlib,json,sys
import mpmath as mp
from q_checkpoint_reader import QCheckpoint
from q_canonical_high_jets import solve,rat
sys.set_int_max_str_digits(1000000)
ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);ap.add_argument('--order',type=int,default=3);args=ap.parse_args()
gate=Path('research/q_canonical_high_jets/verification/checks.json');assert json.loads(gate.read_text())['status']=='PASS'
q=QCheckpoint(args.snapshot);dest=Path('evidence/q_canonical_high_jets')/args.tag;dest.mkdir(parents=True,exist_ok=True)
inputs={'source':str(Path(args.snapshot).resolve()),'source_sha256':q.meta['sha256'],'ell':str(rat(q.cl)),'kappa':str(rat(q.kappa)),'L':str(rat(q.L)),'coefficients':[[str(rat(v))for v in row]for row in q.coeff]}
inp=dest/'exact_input.json';inp.write_text(json.dumps(inputs,indent=2)+'\n')
z=solve(inputs['coefficients'],F(inputs['kappa']),F(inputs['ell']),args.order);mp.mp.dps=90
mf=lambda v:mp.mpf(v.numerator)/v.denominator
length=mf(F(inputs['L']))*mp.power(2,-mf(z['kappa']));rows=[]
for field in ['rho','psi','R']:
 for(i,j),v in sorted(z[field].items(),key=lambda item:(sum(item[0]),-item[0][0])):
    degree=i+j;exponent=(degree-1)if field!='psi'else degree-2
    exact_physical=None;kp=z['kappa']*exponent
    if kp.denominator==1:exact_physical=v*F(2)**int(kp)/F(inputs['L'])**exponent
    rows.append(dict(field=field,x_power=i,y_power=j,degree=degree,core_exact=str(v),physical_exact=str(exact_physical)if exact_physical is not None else None,physical_factor=f'2^({z["kappa"]}*{exponent})/L^{exponent}',physical_decimal=mp.nstr(mf(v)/length**exponent,70)))
record=dict(utc=datetime.now(timezone.utc).isoformat(),status='COMPUTED_EXACT_CORE',source=inputs['source'],source_sha256=q.meta['sha256'],input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),a_exact=str(z['a']),c_exact=str(z['c']),delta_exact=str(z['delta']),degree=2*args.order+1,poisson_exact_zero=not z['poisson'],harmonic=[{key:str(v)for key,v in h.items()}for h in z['harmonic']],rows=rows,command=[sys.executable,*sys.argv],hashes={p:hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in ['independent_code/q_canonical_high_jets.py',__file__,'research/q_canonical_high_jets/PROOF.md']},scope='Exact Taylor coefficients of the frozen finite formula and canonical inverse. Physical exact rationals provided when scaling allows them. No limiting regularity or uniform residual claim.')
(dest/'diagnostic.json').write_text(json.dumps(record,indent=2)+'\n')
lines=[f'# Canonical center jets: {args.tag}','',record['utc'],'',record['scope'],'',f'Source SHA256 {q.meta["sha256"]}. Poisson exact zero: {record["poisson_exact_zero"]}.','','| field | degree | monomial | physical coefficient |','|---|---:|---|---:|']
for row in rows:lines.append(f'| {row["field"]} | {row["degree"]} | x^{row["x_power"]} y^{row["y_power"]} | {mp.nstr(mp.mpf(row["physical_decimal"]),14)} |')
(dest/'TABLE.md').write_text('\n'.join(lines)+'\n');print(json.dumps({'utc':record['utc'],'tag':args.tag,'rows':len(rows),'a':float(z['a']),'delta':float(z['delta']),'poisson_exact_zero':record['poisson_exact_zero']}))
