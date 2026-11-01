"""Audit polar modular continuation against independent exact Cartesian data."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
from contextlib import redirect_stdout
import io,json,re,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
ROOT=Path('research/197_high_harmonic_tuning')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
 start=time.monotonic();src=ROOT/'sources/lead_hh_tune_mod_1802.py';raw=src.read_bytes();text=raw.decode()
 old='return x.numerator % PR * pow(x.denominator, PR - 2, PR) % PR'
 assert text.count(old)==1;text=text.replace(old,'return x.numerator % PR * inv(x.denominator) % PR')
 old="def inv(a):\n    assert a % PR != 0, 'division by a zero residue'\n    return pow(a, PR - 2, PR)"
 new="""division_checks = {'calls': 0, 'units': set()}
def inv(a):
    a %= PR
    assert a != 0, 'division by a zero residue'
    v = pow(a, PR - 2, PR)
    assert a * v % PR == 1, 'proposed modular inverse is not an inverse'
    division_checks['calls'] += 1
    division_checks['units'].add(a)
    return v"""
 assert text.count(old)==1;text=text.replace(old,new)
 instrumented=ROOT/'sources/lead_hh_tune_mod_checked.py';instrumented.write_text(text)
 exact={};inputs=[]
 for k in range(1,5):
  p=ROOT/f'verification/sin15_block{k}.json';b=p.read_bytes();d=json.loads(b)
  exact[('R',k)]=F(d['constant_exact']);exact[('sigma',k)]=F(d['response_exact'])
  if k<4:exact[('H',9*k)]=F(d['tuned_harmonic_exact'])
  inputs.append(dict(path=str(p),sha256=sha256(b).hexdigest()))
 assert len(exact)==11 and exact['sigma',4]==0 and all(exact['sigma',k] for k in range(1,4))
 assert F(37559,10000)<exact['R',4]<F(3756,1000)
 S={15*s+e for s in range(-9,10,2) for e in range(-8,9,2)}
 assert 1 not in S and 3 not in S and 31 not in S
 rows=[]
 for ix,mod in enumerate([2305843009213693951,4611686018427387847],1):
  begin=time.monotonic();print(json.dumps(dict(started=stamp(),modulus=mod)),flush=True)
  args=sys.argv[:];sys.argv=['lead_hh_tune_mod_checked.py','9','2','15','4',str(mod)]
  ns={'__name__':'__main__'};buf=io.StringIO()
  try:
   with redirect_stdout(buf):exec(compile(text,'lead_hh_tune_mod_checked.py','exec'),ns)
  finally:sys.argv=args
  result=buf.getvalue();out=ROOT/f'verification/sin15_mod_replay_p{ix}.out';out.write_text(result)
  original=ROOT/f'sources/lead_sin15_mod_p{ix}.out'
  def parse(s):
   d={}
   assert re.search(r'first obstruction O_9 residue 0(?:\n|$)',s)
   for k,r,sig in re.findall(r'k=(\d+) \(order \d+\): R_k residue (\d+), sigma_k residue (\d+)',s):d['R',int(k)]=int(r);d['sigma',int(k)]=int(sig)
   for n,h in re.findall(r'H_(\d+) residue (\d+)',s):d['H',int(n)]=int(h)
   return d
  values=parse(result);assert values==parse(original.read_text()) and set(values)==set(exact)
  checks=[]
  for label,v in exact.items():
   inv=pow(v.denominator,-1,mod);assert v.denominator*inv%mod==1
   residue=v.numerator*inv%mod;assert residue==values[label]
   checks.append(dict(kind=label[0],index=label[1],residue=residue,exact_denominator_unit=True))
  assert values['R',4]!=0 and all(values['sigma',k]!=0 for k in range(1,4)) and values['sigma',4]==0
  units=ns['division_checks']['units'];calls=ns['division_checks']['calls']
  row=dict(modulus=mod,all_checks_pass=True,division_calls=calls,distinct_units=len(units),unit_list_sha256=sha256(json.dumps(sorted(units)).encode()).hexdigest(),rational_checks=checks,source_log=dict(path=str(original),sha256=sha256(original.read_bytes()).hexdigest()),replay_log=dict(path=str(out),sha256=sha256(out.read_bytes()).hexdigest()),actual_elapsed_s=time.monotonic()-begin)
  rows.append(row);print(json.dumps(dict(finished=stamp(),modulus=mod,division_calls=calls,elapsed_s=row['actual_elapsed_s'])),flush=True)
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,moduli=rows,exact_rationals_per_modulus=11,first_compatibility_support_zero=True,fourth_response_support_zero=True,fourth_constant_interval=['37559/10000','939/250'],source=dict(path=str(src),sha256=sha256(raw).hexdigest()),instrumented_source=dict(path=str(instrumented),sha256=sha256(instrumented.read_bytes()).hexdigest()),exact_inputs=inputs,actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/sin15_modular_audit.json').write_text(json.dumps(out,indent=2)+'\n')
 (ROOT/'sources/sin15_modular_audit.py').write_bytes(Path('code/sin15_modular_audit.py').read_bytes())
 print(json.dumps(out),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/sin15_modular_FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)
