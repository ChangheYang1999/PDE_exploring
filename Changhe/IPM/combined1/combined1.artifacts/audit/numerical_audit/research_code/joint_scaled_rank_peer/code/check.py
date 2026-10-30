from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import comb
import json,time,gzip,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/joint_scaled_rank_peer';T=R.parent/'c1-t4/research/joint_scaled_rank_audit'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={};frozen={}
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or actual==h,(p,h,actual);inputs[str(p.relative_to(R))]=actual;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 own=read(R/'research/joint_scaled_density_rank/verification/result.json')
 for p,h in own['inputs'].items():bind(R/p,h)
 known={h:R/p for p,h in inputs.items()}
 def freeze(p,wanted=None):
  p=Path(p);blob=p.read_bytes();h=sha256(blob).hexdigest();assert wanted is None or h==wanted
  if h in known:out=known[h];compressed=False
  else:
   assert p.is_relative_to(T);out=B/'source'/p.relative_to(T);compressed=len(blob)>1000000
   if compressed:out=out.with_name(out.name+'.gz')
   out.parent.mkdir(parents=True,exist_ok=True);payload=gzip.compress(blob,mtime=0) if compressed else blob
   with out.open('xb') as f:f.write(payload)
  frozen[str(p)]={'local':str(out.relative_to(R)),'source_sha256':h,'stored_sha256':sha(out),'gzip':compressed}
  return json.loads(blob) if p.suffix=='.json' else blob.decode()
 peer=freeze(T/'verification/result.json')
 for p,h in peer['inputs'].items():freeze(p,h)
 assert peer['verdict'].startswith('CONFIRMED N4-274') and peer['potential_dimension']==peer['density_dimension']==2426 and peer['actual_candidate_shape_match'] is None
 old=read(R/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json');shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 actual=list(map(shape,old['generators']))+[(j,m,('legqs',0,N,4,S)) for S in [25,50] for j in [1,2,3] for m in range(9,16) for N in range(12)]
 abstract=read(R/'research/joint_scaled_density_rank/verification/abstract_shapes.json');assert set(actual)==set(map(shape,abstract['generators'])) and len(actual)==len(set(actual))==2426
 c=Q(4076476460239181,2251799813685248);gamma=1/c;delta=1-gamma;ps=[(3+gamma-j*delta)/2 for j in range(8)]
 assert list(map(str,ps))==own['branch_exponents'] and all(p.denominator!=1 for p in ps)
 diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)];assert list(map(str,diffs))==own['noninteger_differences'] and all(p.denominator!=1 for p in diffs)
 assert 3+gamma<4 and gamma-1<0
 targets={(r['scale'],r['m'],r['N']):r for r in peer['witnesses']};ownw={(r['scale'],r['m'],r['N']):r for r in own['Laurent_witnesses']};assert len(targets)==len(ownw)==168
 checks=[]
 for S,Sother in [(25,50),(50,25)]:
  a=Q(S*S-1);v=-1/a;t=1-v;other=1-Q(Sother*Sother-1)/a
  row=next(r for r in peer['cross_poles'] if r['scale']==S);row0=next(r for r in own['cross_pole_analyticity'] if r['scale']==S)
  assert other!=0 and Q(row['other_denominator'])==other==Q(row0['other_denominator_at_pole_exact'])
  for m in range(9,16):
   for N in range(12):
    v0=S**8*v**4*comb(2*N,N)*t**(m+N)/a**(4+N)
    assert v0!=0 and Q(targets[S,m,N]['coefficient'])==v0==Q(ownw[S,m,N]['Laurent_coefficient']) and targets[S,m,N]['nonzero']
    checks.append({'scale':S,'m':m,'N':N,'coefficient':str(v0),'independent_equal':True})
 assert all(sha(R/p)==h for p,h in inputs.items()) and all(sha(R/d['local'])==d['stored_sha256'] for d in frozen.values())
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'frozen_sources':frozen,'witnesses':checks,'potential_dimension':2426,'density_dimension':2426,'abstract_shapes':2426,'actual_candidate_shape_match':None,'own_result_sha256':sha(R/'research/joint_scaled_density_rank/verification/result.json'),'peer_result_sha256':sha(T/'verification/result.json'),'foreign_code_executed':False,'verdict':'CONFIRMED N4-274 through full independent T4-348 proof and exact witness reproduction'}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],out['verdict'],sha(B/'verification/result.json'),out['elapsed_seconds'])
if __name__=='__main__':main()
