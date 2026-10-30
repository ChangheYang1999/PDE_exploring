from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import importlib.util,json,time,sys
from flint import fmpq as Q,arb,ctx
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/candidate020_origin_peer';PEER=ROOT.parent/'c1-t4/research/candidate020_origin'
sys.set_int_max_str_digits(0);ctx.prec=1024
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic();dest=B/'verification/result.json';assert not dest.exists();inputs={};frozen={}
 def bind(p):inputs[str(p.relative_to(ROOT))]=sha(p);return p
 def freeze(p,n,h=None):
  blob=p.read_bytes();actual=sha256(blob).hexdigest();assert h is None or h==actual
  target=B/'source'/n
  if target.exists():assert target.read_bytes()==blob
  else:
   with target.open('xb') as f:f.write(blob)
  bind(target);frozen[n]={'original':str(p),'sha256':actual}
  return json.loads(blob) if p.suffix=='.json' else None
 peer=freeze(PEER/'verification/result.json','T4_result.json')
 for i,(p,h) in enumerate(peer['inputs'].items()):
  p=Path(p);freeze(p,f'input_{i:03d}{p.suffix}',h)
 name='C1-N1-020-legqs25p50-quot013'
 raw=bind(ROOT/f'research/candidate_audits/data/{name}/quot013_legqs25p50_m9to15_cpu_m16_exact.json')
 direct=bind(ROOT/f'research/generator_sector_audit/verification/{name}_direct.json')
 data=json.loads(raw.read_text());old=json.loads(direct.read_text())
 assert sha(raw)==old['generator_sha256']=='bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf'
 code=bind(ROOT/'research/generator_sector_audit/code/direct.py')
 spec=importlib.util.spec_from_file_location('n4_origin_020',code);D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
 fields=D.origin(data);c=Q(data['cl_exact']);gamma=1/c;delta=1-gamma
 sums=[Q(0)]*3;touched=0;terms=0
 for g in data['generators']:
  m=int(g['m']);w,n,q,R=D.spec_parts(g['spec'])
  if m+w>2:continue
  touched+=1;terms+=min(n,2-m-w)+1;p=(3+gamma-int(g['j'])*delta)/2
  sums[m]+=Q(g['coef'])*D.origin_radial(p,m,g['spec'],2-m)[2-m]
 b0,b1,b2=sums;quartic={'x4':b0+b1+b2,'x2y2':2*b0-6*b2,'y4':b0-b1+b2}
 checks={k:fields[k]==Q(old['origin'][k])==Q(peer['origin'][k]) for k in fields}
 checks.update({'quartic_'+k:v==Q(peer['quartic_coefficients'][k]) for k,v in quartic.items()})
 checks['normalization']=c+fields['strain']==Q(peer['c_plus_strain'])==1
 checks['positive']=fields['a0']>0 and peer['a0_positive']
 checks['counts']=len(data['generators'])==peer['raw_count']==2426 and touched==peer['contributing_generators']==24 and terms==peer['contributing_summands']==24
 checks['identities']=fields['strain']==4*quartic['x2y2'] and fields['a0']==-4*quartic['x2y2']-24*quartic['y4']
 ar=lambda q:arb(q.numerator)/q.denominator
 ball=ar(fields['a0']);checks['outward']=ball.overlaps(arb(peer['a0_arb'])) and ball.overlaps(arb(old['a0_arb'])) and ball>0
 checks['peer_flags']=all(peer['N4_exact_comparisons'].values());assert all(checks.values()),checks
 for p in [B/'PROOF.md',B/'verification/PREPARE.json',Path(__file__),ROOT/'research/generator_sector_audit/PROOF.md',ROOT/'research/multiscale_generators/code/moments.py',ROOT/'research/multiscale_generators/code/cartesian.py',ROOT/'research/sector_audit/code/sectors_flint.py']:bind(p)
 assert all(sha(ROOT/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'raw_sha256':sha(raw),'inputs':inputs,'frozen_peer_sources':frozen,'checks':checks,'origin':{k:str(v) for k,v in fields.items()},'quartic_coefficients':{k:str(v) for k,v in quartic.items()},'slope':ball.str(100),'contributing_generators':touched,'contributing_summands':terms,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED exact N4-291 origin normalization through independent T4-361'}
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',sha(dest),'seconds',out['elapsed_seconds'])
if __name__=='__main__':main()
