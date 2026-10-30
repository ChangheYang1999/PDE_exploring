from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,sys,time,os,signal
from flint import arb,ctx,fmpq as Q
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/candidate018_point_peer';PEER=ROOT.parent/'c1-t4/research'
sys.set_int_max_str_digits(0);ctx.prec=2048
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
def canonical(d):return {tuple(k):Q(v) for k,v in zip(d['order'],d['coefficients'],strict=True) if Q(v)}
def main():
 start=time.monotonic();name='C1-N1-018-legqs25-cont12';dest=BASE/'verification/result.json';assert not dest.exists()
 ownpoint=ROOT/f'research/generator_sector_audit/verification/{name}_direct.json'
 ownweak=ROOT/f'research/scaled_factored_weak/verification/{name}_n019_K01800.json'
 owncan=ROOT/f'research/candidate_audits/data/{name}/canonical.json'
 ownraw=ROOT/f'research/candidate_audits/data/{name}/quot013_legqs25_cont12_cpu_m16_exact.json'
 retained=[ownpoint,ownweak,owncan,ownraw,ROOT/'research/scaled_factored_weak/PROOF.md',ROOT/'research/scaled_factored_weak/code/check_candidates.py',ROOT/'research/candidate018_holdout/verification/result.json',ROOT/'research/candidate_audits/reviews/T4_014/source/localized_probe_audit/code/reproduce.py']
 known={sha(p):p for p in retained if p.exists()};bindings={};frozen={}
 def freeze(p,expected=None):
  p=Path(p);b=p.read_bytes();h=sha256(b).hexdigest();assert expected is None or h==expected,(p,h,expected)
  if h in known:
   target=known[h];compressed=False
  else:
   rel=p.relative_to(PEER);compressed=len(b)>1000000;target=BASE/'source'/str(rel)
   if compressed:target=target.with_name(target.name+'.gz')
   target.parent.mkdir(parents=True,exist_ok=True)
   packed=gzip.compress(b,compresslevel=6,mtime=0) if compressed else b
   if target.exists():assert target.read_bytes()==packed
   else:
    with target.open('xb') as f:f.write(packed)
   if not compressed:known[h]=target
  local=str(target.relative_to(ROOT));frozen[local]={'original':str(p),'sha256':h,'stored_sha256':sha(target),'gzip':compressed}
  bindings[str(p)]=True
  return json.loads(b) if p.suffix=='.json' else None
 pp=PEER/'candidate018_point';pr=freeze(pp/'verification/results.json');point=json.loads(ownpoint.read_text())
 for rel,h in pr['inputs'].items():freeze(pp/rel,h)
 checks={'same_candidate':pr['candidate']==point['candidate']==name,'same_point':pr['point']==point['point'],'same_c':Q(pr['c_exact'])==Q(point['c_exact']),'raw_identity':sha(ownraw)==point['generator_sha256']}
 for k,z in pr['fields'].items():checks['point_'+k]=arb(z).overlaps(arb(point['fields'][k]))
 for k in ['uniform_graded_upper','uniform_graded_gap']:checks[k]=arb(pr[k]).overlaps(arb(point[k]))
 checks['graded_positive']=arb(pr['uniform_graded_gap'])>0
 assert len(pr['ball_exclusions'])==len(point['ball_exclusions'])==6
 for row,old in zip(pr['ball_exclusions'],point['ball_exclusions'],strict=True):
  key=row['framework'];checks[key+'_framework']=key==old['framework'];checks[key+'_s']=Q(row['s'])==Q(old['s'])
  if old.get('radius_squared') is not None:checks[key+'_radius']=Q(row['radius_squared'])==Q(old['radius_squared'])
  else:checks[key+'_radius']=Q(row['radius'])==Q(old['radius'])
  for k in ['upper','gap','necessary_H2s_radius_lower']:
   if k in old:checks[key+'_'+k]=arb(row[k]).overlaps(arb(old[k]))
  checks[key+'_positive']=arb(row['gap'])>0
 checks['peer_point_flags']=all(pr['field_overlaps'].values())
 theta=(arb(point['fields']['gradient_norm'])-arb(point['fields']['rho_y']))/2
 checks['theta']=theta.overlaps(arb(pr['theta']))
 checks['theta_gap']=(theta-ar(Q(point['c_exact'])-1)).overlaps(arb(pr['theta_minus_c_minus_one']))
 freeze(pp/'PROOF.md',pr['inputs']['PROOF.md'])
 freeze(PEER/'graded_point_009/PROOF.md')
 checks['peer_complete_fields']=set(pr['fields'])==set(point['fields'])=={'rho','u1','u2','rho_x','rho_y','residual','velocity_norm','gradient_norm'}
 exactrows=[('A2-Db','1/262144','1/65536'),('FW-T-TB-rebal-v1','1/65536','3/32768'),('FW-T-TB-sharp-v1','1/8192','43/50000'),('T4-019-no-H','1/131072','1/16384'),('FW-T-T4L2-sharp-v1','1/7744','147/200000'),('FW-T-T4L2-sharpw-v1','1/5184','1351/1000000')]
 fields={k:arb(v) for k,v in point['fields'].items()};c=Q(point['c_exact']);x,y=map(Q,point['point'])
 vx,vy=ar(c*x)+fields['u1'],ar(c*y)+fields['u2']
 checks['residual_identity']=(vx*fields['rho_x']+vy*fields['rho_y']-fields['rho']).overlaps(fields['residual'])
 checks['velocity_identity']=(vx*vx+vy*vy).sqrt().overlaps(fields['velocity_norm'])
 checks['gradient_identity']=(fields['rho_x']**2+fields['rho_y']**2).sqrt().overlaps(fields['gradient_norm'])
 I=abs(fields['residual']);roots={}
 for spec,row in zip(exactrows,pr['ball_exclusions'],strict=True):
  key,ss,rr=spec;s0=Q(ss);rad=ar(rr)
  checks[key+'_registered']=(row['framework'],row['s'],row['radius'])==spec
  C0=1/(4*arb.pi()*ar(1+s0)).sqrt();C1=1/(8*arb.pi()*ar(s0*(1+s0))).sqrt()
  D=C1*fields['velocity_norm']+C0*(1+fields['gradient_norm'])
  upper=rad*D+C0*C1*rad*rad;gap=I-upper
  root=2*I/(D+(D*D+4*C0*C1*I).sqrt())
  checks[key+'_recomputed']=upper.overlaps(arb(row['upper'])) and gap.overlaps(arb(row['gap'])) and root.overlaps(arb(row['necessary_H2s_radius_lower'])) and gap>0 and root>rad
  roots[key]=root.str(90)
 b0=ar(Q(50,651))/(28248*4*arb.pi()).sqrt();b1=ar(Q(25,217))/(8*arb.pi()).sqrt()
 ub=b1*fields['velocity_norm']+b0*(1+fields['gradient_norm'])+b0*b1
 checks['graded_recomputed']=ub.overlaps(arb(pr['uniform_graded_upper'])) and (I-ub).overlaps(arb(pr['uniform_graded_gap'])) and I-ub>0
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 owninputs={str(p.relative_to(ROOT)):sha(p) for p in retained if p.exists()}
 owninputs.update({str(p.relative_to(ROOT)):sha(p) for p in [Path(__file__),BASE/'PROOF.md']})
 for local,item in frozen.items():assert sha(ROOT/local)==item['stored_sha256']
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'checks':checks,'comparison_count':len(checks)+len(bindings),'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen,'own_inputs':owninputs,'point_residual':pr['fields']['residual'],'uniform_graded_gap':pr['uniform_graded_gap'],'necessary_point_radii':roots,'peer_point_runtime_seconds':pr['elapsed_seconds'],'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED point and six scalar plus original graded exclusions of N4-270 via T4-342; global moments and asymptotic flags have separate status'}
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(dest),'seconds',out['elapsed_seconds'])
if __name__=='__main__':main()
