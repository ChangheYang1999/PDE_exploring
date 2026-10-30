"""Bind the complete017 cover and verify its finite tree and strict rate."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import fmpq as Q,arb,ctx
import json,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate017_background_margin';ctx.prec=1536
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def rectangle(path):
 a,b,c,d=map(Q,[0,1,-1,1])
 for ch in path:
  if ch=='t':b=(a+b)/2
  elif ch=='T':a=(a+b)/2
  elif ch=='z':d=(c+d)/2
  elif ch=='Z':c=(c+d)/2
  else:raise AssertionError(ch)
 return a,b,c,d

def main():
 tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or actual==h,(str(p),actual,h);inputs[str(p.relative_to(R))]=actual
  return json.loads(p.read_text()) if p.suffix=='.json' else None
 bind(B/'PROOF.md');bind(Path(__file__))
 cp=R/'research/scaled_rational_background_cover/verification/C1-N1-017-legqs50-quot013_theta_2_25_1536.json';cover=bind(cp);frozen=B/'source/complete_cover.json'
 with frozen.open('xb') as f:f.write(cp.read_bytes())
 bind(frozen,sha(cp))
 for section in ['inputs','reconstruction_inputs']:
  for rel,h in cover[section].items():bind(R/rel,h)
 recon=bind(R/'research/scaled_background_cover/verification/C1-N1-017-legqs50-quot013_reconstruction.json')
 accepted=bind(R/'research/scaled_hessian_peer/verification/result.json','0de14e144d06ad09cbf02fbc02844b467771aa0ad4ff2d821bd6bc9ce6131dfd')
 for rel,h in accepted['own_inputs'].items():bind(R/rel,h)
 for rel,info in accepted['frozen_or_retained_sources'].items():bind(R/rel,info['stored_sha256'])
 row=next(r for r in accepted['rows'] if r['candidate']==cover['candidate']);raw=R/'research/candidate_audits/data/C1-N1-017-legqs50-quot013/quot013_legqs50_m9to15_cpu_m16_exact.json'
 shared=R.parent/'c1-shared/candidate_snapshots/C1-N1-017-legqs50-quot013'/raw.name
 checks['immutable_raw']=sha(raw)==sha(shared)==cover['raw_sha256']==recon['raw_sha256']==row['raw_sha256']=='7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114'
 checks['complete_flags']=cover['all_pass'] and cover['complete_partition'] and not cover['pending'] and cover['all_denominator_coefficients_positive'] and cover['no_spatial_quadrature']
 checks['degree_identity']=(cover['degree_t'],cover['degree_z'],cover['J'])==(103,80,8)==(recon['degree_t'],recon['degree_z'],recon['J'])
 checks['reconstruction_origin_denominator']=recon['origin_checks'] and recon['denominator_positive_on_unit_interval'] and recon['denominator_powers']==[0,0,19,0]
 paths=[r['path'] for r in cover['accepted']];leaves=set(paths);assert len(paths)==len(leaves)==247
 nodes=set();children={}
 for path in paths:
  for k in range(len(path)):
   parent=path[:k];assert parent not in leaves;children.setdefault(parent,set()).add(path[k]);nodes.add(parent)
 checks['binary_tree_complete']=all(cs in [{'t','T'},{'z','Z'}] for cs in children.values()) and '' in children
 checks['internal_node_count']=len(nodes)==len(leaves)-1
 rects=[rectangle(p) for p in paths];area=Q(0);paircount=0;minimum=None
 for i,((a,b,c,d),leaf) in enumerate(zip(rects,cover['accepted'],strict=True)):
  assert Q(0)<=a<b<=1 and Q(-1)<=c<d<=1;area+=(b-a)*(d-c)
  v=arb(leaf['bound']);den=arb(leaf['denominator_coefficient_lower']);assert leaf['pass'] and v.is_finite() and v.lower()>=0 and den.lower()>0
  if minimum is None or v.lower()<minimum.lower():minimum=v
  for aa,bb,cc,dd in rects[:i]:assert max(a,aa)>=min(b,bb) or max(c,cc)>=min(d,dd);paircount+=1
 checks['exact_area']=area==2;checks['all_leaf_bounds_nonnegative']=True;checks['all_leaf_denominators_positive']=True;checks['all_pair_interiors_disjoint']=True
 c=Q(recon['c_exact']);tau=Q(cover['tau']);cap=Q(row['strict_kappa_upper_exact']);rate=c+1-tau-cap;floor=Q(200123867,10**8)
 checks['exact_constants']=c==Q(4076476460239181,2251799813685248) and tau==Q(2,25) and cap==Q(729080538628955349,10**18)
 checks['accepted_kappa_strict']=all(accepted['checks'].values()) and arb(row['values_reassembled']['kappa'])<arb(cap.numerator)/cap.denominator
 checks['strict_rate_arithmetic']=rate>floor>2
 logs=[]
 for k in range(1,7):
  p=R/f'logs/scaled017_rational_stage{k}.log';bind(p);line=p.read_text().splitlines()[-1];assert line.startswith('STAGE_DONE');logs.append({'stage':k,'completion_log':line,'sha256':sha(p)})
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for rel,h in inputs.items():assert sha(R/rel)==h
 result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':cover['candidate'],'raw_sha256':cover['raw_sha256'],'checks':checks,'check_count':len(checks),'inputs':inputs,'cover_sha256':sha(cp),'cover_utc':cover['utc'],'leaf_count':len(paths),'internal_node_count':len(nodes),'exact_area':str(area),'disjoint_pairs_checked':paircount,'minimum_stored_eigenvalue_lower_ball':minimum.str(90),'tau_exact':str(tau),'kappa_strict_upper_exact':str(cap),'rate_strict_lower_exact':str(rate),'rate_strict_decimal_lower_exact':str(floor),'stage_logs':logs,'recorded_cover_total_elapsed_seconds':cover['total_elapsed_seconds'],'cover_stage6_elapsed_seconds':cover['stage_elapsed_seconds'],'no_actual_leaf_replay_in_this_summary':True,'verdict':'CONFIRMED complete finite cover summary and conditional rate; independent reconstruction and leaf replay OPEN','elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('CHECKED',len(checks),'leaves',len(paths),'rate>',float(floor),'sha',sha(out),'utc',result['utc'],'seconds',result['elapsed_seconds'])
if __name__=='__main__':main()
