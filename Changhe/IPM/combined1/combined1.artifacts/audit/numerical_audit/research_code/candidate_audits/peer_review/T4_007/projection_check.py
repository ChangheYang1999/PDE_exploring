from pathlib import Path
from datetime import datetime,timezone
import argparse,gzip,hashlib,json,time,sys
sys.set_int_max_str_digits(0)
from polar_fields import fields,td,ZERO
from flint import fmpq as Q,fmpq_poly as Poly
ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def add(d,k,v):
 if v:d[k]=d.get(k,ZERO)+v
 if k in d and not d[k]:del d[k]
def run(name):
 start=time.monotonic();source=ROOT/'data'/f'{name}_canonical.json';peer=ROOT/'source'/f'{name}_first_mode.json.gz'
 c,delta,rho,stream=fields(json.loads(source.read_text()));out={};pairs=0
 for (j,n),rr in rho.items():
  if n==1:add(out,j+1,c*td(rr,(j+1)*delta/2,1)-rr)
 for (j,m),ss in stream.items():
  ds=td(ss,(j+1)*delta/2,2)
  for (i,n),rr in rho.items():
   if abs(n-m)!=1:continue
   sign=1 if n>m else -1
   add(out,i+j+2,-Q(sign,2)*(m*ss*td(rr,(i+1)*delta/2,1)+n*rr*ds));pairs+=1
 with gzip.open(peer,'rt') as f:target=json.load(f)
 assert target['source_sha256']==digest(source),(name,'source mismatch')
 expected={r['ell']:Poly([int(v) for v in r['numerator']])/Q(r['denominator']) for r in target['rows']}
 assert out==expected,(name,'polynomial mismatch')
 result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'canonical_sha256':digest(source),'peer_sha256':digest(peer),'code_sha256':digest(Path(__file__)),'helper_sha256':digest(ROOT/'code/polar_fields.py'),'proof_sha256':digest(ROOT/'PROOF.md'),'exact_polynomial_equality':True,'branches':len(out),'coefficients_compared':sum(len(p) for p in out.values()),'nonlinear_polar_pairs':pairs,'elapsed_seconds':time.monotonic()-start}
 (ROOT/'verification'/f'{name}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('candidates',nargs='+');a=p.parse_args()
 for n in a.candidates:run(n)
