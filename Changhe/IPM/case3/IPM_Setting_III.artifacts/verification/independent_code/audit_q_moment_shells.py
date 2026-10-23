"""Freeze exact shell polynomials and evaluate them at common physical radii."""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import mpmath as mp
from q_canonical_moment_shells import polynomials,shell_values
from q_mp_primitives import guard_digits
sys.set_int_max_str_digits(0)
parser=argparse.ArgumentParser();parser.add_argument('input');parser.add_argument('--tag',required=True)
args=parser.parse_args()
gate=Path('research/q_canonical_moment_shells/verification/checks.json')
assert json.loads(gate.read_text())['verdict']=='PASS'
ip=Path(args.input);data=json.loads(ip.read_text());src=Path(data['source'])
assert hashlib.sha256(src.read_bytes()).hexdigest()==data['source_sha256']
cc=data['coefficients'];kappa=F(data['kappa']);length=F(data['L'])
rows=polynomials(cc,kappa,3)
previous=ip.parent/'diagnostic.json';old=json.loads(previous.read_text())
assert old['source_sha256']==data['source_sha256']
for row,hm in zip(rows,old['harmonic']):assert row['total_core']==4*row['n']*F(hm['stream_harmonic_core'])
radii=['0','0.000001','0.00001','0.0001','0.001','0.003','0.01','0.03','0.1','0.3','1','3','10','100',None]
dps=70+guard_digits(max(map(len,cc))-1,len(cc),kappa)
with mp.workdps(dps):first=shell_values(rows,length,kappa,radii)
with mp.workdps(dps+50):
 second=shell_values(rows,length,kappa,radii);checks=[]
 for a,b in zip(first,second):
  for key in ['total','shells','tails']:
   aa=a[key]if isinstance(a[key],list)else[a[key]];bb=b[key]if isinstance(b[key],list)else[b[key]]
   for j,(x,y)in enumerate(zip(aa,bb)):
    err=abs(x-y)/(1+abs(y));assert err<mp.mpf('1e-55'),(a['n'],key,j,err)
    checks.append(dict(n=a['n'],field=key,index=j,normalized_difference=mp.nstr(err,20)))
  assert abs(b['telescoping_error'])/(1+abs(b['total']))<mp.mpf('1e-55')
 def s(v):return mp.nstr(v,70)
 evaluated=[dict(n=b['n'],frequency=2*b['n'],total=s(b['total']),shells=list(map(s,b['shells'])),tails=list(map(s,b['tails'])),telescoping_error=s(b['telescoping_error']),sum_absolute_signed_shells=s(mp.fsum(abs(v)for v in b['shells'])))for b in second]
 exact=[dict(n=r['n'],q_exact=str(r['q']),E_w_exact=list(map(str,r['E'])),total_core_exact=str(r['total_core']),physical_factor=f'(L*2^(-({kappa})))^({2-2*r["n"]})')for r in rows]
 record=dict(utc=datetime.now(timezone.utc).isoformat(),verdict='COMPUTED',tag=args.tag,source=data['source'],source_sha256=data['source_sha256'],input=str(ip),input_sha256=hashlib.sha256(ip.read_bytes()).hexdigest(),previous_high_jet_record=str(previous),radii_physical=['infinity'if r is None else r for r in radii],ell_exact=data['ell'],kappa_exact=str(kappa),L_exact=str(length),dps=[dps,dps+50],exact_polynomials=exact,evaluated=evaluated,precision_checks=checks,command=[sys.executable,*sys.argv],scope='Signed shell source moments of the frozen finite density under the canonical full-plane inverse. Decimal evaluations are not interval enclosures. Not a profile or limiting regularity claim.')
 record['sha256']={p:hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in ['independent_code/q_canonical_moment_shells.py',__file__,'research/q_canonical_moment_shells/PROOF.md']}
 dest=Path('evidence/q_canonical_moment_shells')/args.tag;dest.mkdir(parents=True,exist_ok=True)
 (dest/'diagnostic.json').write_text(json.dumps(record,indent=2)+'\n')
 lines=[f'# Canonical moment shells: {args.tag}','',record['utc'],'',record['scope'],'',f'Source SHA256: {data["source_sha256"]}. Exact binary kappa retained. Precision comparison: {dps} and {dps+50} decimal digits.','', '| physical radial shell | I2 contribution | I4 contribution | I6 contribution |','|---|---:|---:|---:|']
 for j,(lo,hi)in enumerate(zip(record['radii_physical'],record['radii_physical'][1:])):lines.append('| '+lo+' to '+hi+' | '+' | '.join(mp.nstr(b['shells'][j],15)for b in second)+' |')
 lines.append('| total, including core and infinity | '+' | '.join(mp.nstr(b['total'],15)for b in second)+' |')
 lines+=['','The sum of absolute signed shell contributions is a lower bound on the absolute weighted source integral. It is not that integral and does not bound a profile residual.']
 (dest/'TABLE.md').write_text('\n'.join(lines)+'\n')
 print(json.dumps(dict(utc=record['utc'],tag=args.tag,totals=[r['total']for r in evaluated],precision_checks=len(checks),dps=record['dps'])))
