from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,time
from flint import arb,fmpq as Q,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/successor_dyadic_probes';D=BASE/'reviews/T4_008_009'
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):
 q=Q(q);return arb(q.numerator)/arb(q.denominator)
def main():
 start=time.monotonic();ctx.prec=1024
 manifest=json.loads((D/'MANIFEST.json').read_text())
 for name,row in manifest['files'].items():assert H(D/name)==row['sha256']
 results=[]
 for label,name in [('008','C1-N1-008-d2w-j7-x3bal'),('009','C1-N1-009-d2w-j7-x3balk')]:
  ownbase=BASE/'verification'/name
  own=json.loads((ownbase/'result.json').read_text())
  peer=json.loads((D/f'{label}_result.json').read_text())
  pm=json.loads((D/f'{label}_input_MANIFEST.json').read_text())
  assert peer['manifest_sha256']==H(D/f'{label}_input_MANIFEST.json')
  assert peer['code_sha256']==H(D/'check.py') and peer['helper_sha256']==H(D/'polar_helper.py')
  assert peer['proof_sha256']==H(D/'PROOF.md')
  assert peer['candidate']==own['candidate']==name
  assert pm[f'{label}_canonical.json']['sha256']==H(ROOT/f'research/candidate_audits/data/{name}/canonical.json')
  assert pm[f'{label}_peer_result.json']['sha256']==H(ownbase/'result.json')
  assert pm[f'{label}_peer_manifest.json']['sha256']==H(ownbase/'manifest.json')
  checks={}
  for n in [1,3,7]:
   op=ownbase/f'mode_{n:03d}.json';pp=D/f'{label}_mode{n}.json'
   assert pm[f'{label}_peer_mode{n}.json']['sha256']==H(op)
   assert peer['mode_hashes'][str(n)]==H(pp)
   om=json.loads(op.read_text());pmod=json.loads(pp.read_text())
   assert pmod['peer_sha256']==H(op)
   for i,(a,b) in enumerate(zip(om['weights'],pmod['weights'],strict=True)):
    assert Q(a['a'])==Q(b['a'])==Q(i,4)
    for key in ['energy','norm']:
     checks[f'mode{n}_a{i}_{key}']=bool(arb(a[key]).overlaps(arb(b[key])))
   assert all(row['comparisons'].get('energy') and row['comparisons'].get('norm') for row in pmod['weights'])
  c=Q(peer['c_exact']);d=c-1
  star=(ar(2*d-3)+ar((2*d-3)**2+16*d).sqrt())/8
  hm=(ar(d)-star)*(4*arb.pi()*star*(1+star)).sqrt()
  checks['H_formula']=bool(hm.overlaps(arb(peer['H_max'])))
  floors=[]
  for i,(a,b) in enumerate(zip(own['seven_cells'],peer['seven_cells'],strict=True)):
   for key in ['left','right','norm_evaluation_at']:assert Q(a[key])==Q(b[key])
   for key in ['projected_norm','lower','upper','gap','ratio']:
    checks[f'cell{i}_{key}']=bool(arb(a[key]).overlaps(arb(b[key])))
   ratio=arb(b['lower'])/arb(b['upper'])
   checks[f'cell{i}_ratio_formula']=bool(ratio.overlaps(arb(b['ratio'])))
   floor=Q(b['strict_ratio_floor'])
   checks[f'cell{i}_peer_floor']=bool(arb(b['ratio'])>ar(floor))
   checks[f'cell{i}_own_floor']=bool(arb(a['ratio'])>ar(floor))
   assert arb(b['gap'])>0 and floor>1 and a['excluded'] and b['excluded']
   floors.append(floor)
  assert all(checks.values()) and peer['all_seven_excluded']
  results.append({'candidate':name,'checks':checks,'minimum_strict_ratio_floor':str(min(floors)),
                  'peer_elapsed_seconds':peer['elapsed_seconds'],'peer_result_sha256':H(D/f'{label}_result.json'),
                  'own_result_sha256':H(ownbase/'result.json')})
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','rows':results,'manifest_sha256':H(D/'MANIFEST.json'),
      'code_sha256':H(__file__),'proof_sha256':H(D/'ACCEPTANCE_PROOF.md'),'elapsed_seconds':time.monotonic()-start}
 with (D/'ACCEPTANCE.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED',[(r['candidate'],r['minimum_strict_ratio_floor']) for r in results],out['elapsed_seconds'])
if __name__=='__main__':main()
