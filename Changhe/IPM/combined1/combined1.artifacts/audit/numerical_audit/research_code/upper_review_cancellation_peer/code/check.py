"""Own exact cancellation example and reciprocal T4-475 fixture checks."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,os,time
from flint import fmpq as Q,fmpq_poly as P
R=Path(__file__).resolve().parents[3];B=R/'research/upper_review_cancellation_peer'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic();checks={};inputs={};external={}
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or h==v,(p,h,v);inputs[str(p.relative_to(R))]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 m=read(B/'source/MANIFEST.json');ck('proof before code',not m['checker_exists']);bind(B/'PROOF.md',m['proof_sha256']);bind(Path(__file__))
 for v in m['files'].values():bind(R/v['path'],v['sha256'])
 def f(k):return R/m['files'][k]['path']
 result=read(f('T4_result.json'),'b38a40ce5a1fc2147cf5c43a178b986b1f96c8932527be00f36c5a40ffac85fb')
 ck('T4 193 distinct successes',result['check_count']==len(result['checks'])==len(set(result['checks']))==193)
 peerroot=Path(m['files']['T4_result.json']['original']).parents[1]
 for row in read(f('T4_manifest.json')):
  p=(peerroot/row['local']).resolve();ck('external:'+row['local'],sha(p)==row['sha256']);external[str(p)]=row['sha256']
 own=read(R/'research/candidate016_upper_opus_primary/verification/result.json','94c9b9cdf6c6aac7f831a23253ba4b8bae7c576942390b17fd77aabf38d780ea')
 ck('own404 accepted',own['check_count']==77 and all(own['checks'].values()))
 for rel,h in own['inputs'].items():bind(R/rel,h)
 lib=bind(R/'research/candidate016_upper_opus_primary/code/check_v02.py','ae63d919f60b458b074df764cf7f94e35109a13e9828fe8949c0ccbb29b30eeb')
 spec=importlib.util.spec_from_file_location('own404',lib);W=importlib.util.module_from_spec(spec);spec.loader.exec_module(W)
 p=read(f('parameters.json'));n=p['n'];T=P([0,1]);v=1-T;raw=P([Q(x) for x in p['raw_P']]);b=Q(p['grouped_b']);A=P([Q(x) for x in p['grouped_P']])
 ck('raw boundary beta',Q(p['ungrouped_beta'])==Q(3,2));ck('leading cancellation',raw==v and A==T and T*raw==v*A)
 ck('smooth harmonic numerator',n==3 and A[0]==0 and A.degree()==1)
 ck('grouped sufficient exponent',b>Q(1,2));e,S=W.source(n,b,A)
 d=W.energy(n,b,A,b,A);a=W.energy(n,b,A,b,A,'a');M=W.mass(n,e,S)
 vals={'d':d,'a':a,'M':M}
 for k,outkey in [('d','d_over_pi'),('a','a_over_pi'),('M','M2_over_pi')]:
  ck('own exact cancellation:'+k,vals[k]==Q(p[outkey])>0)
  ck('peer exact cancellation:'+k,vals[k]==Q(result['counterexample_energies_over_pi'][k]))
 ck('manufactured identity',M==d+a and W.pair(n,e,S,b,A)==-a and W.pair(n,e,S,b,A,'p')==d)
 for key,ownkey in [('psi1','mode1'),('psi3','mode3')]:
  for term in ['d','a','M2','b','p']:ck('fixture:'+key+':'+term,Q(result['fixtures'][key][term])==Q(own['fixtures'][ownkey][term]))
 for key in ['combined','single']:
  for term,v0 in own[key].items():ck(key+':'+term,Q(v0)==Q(result[key][term]))
 for term,v0 in own['gram'].items():ck('Gram:'+term,Q(v0)==Q(result['two_mode'][term]))
 for k,j in [('rational','constant'),('sqrt3_pi','sqrt3_pi_coefficient')]:ck('pole:'+k,Q(own['positive_pole_closed_form_coefficients'][k])==Q(result['positive_pole_closed_form'][j]))
 t2=read(R/'research/candidate016_upper_opus_primary/source/T2_result.json')
 ck('same actual T2 result',sha(peerroot/'source/T2_result.json')==sha(R/'research/candidate016_upper_opus_primary/source/T2_result.json'))
 ck('two exponent exact fixture',Q(result['two_exponent_a_over_pi'])==Q(t2['C']['two_exponent_a_over_pi']))
 frozen=f('T4_T2_review.md').read_text();current=(R/'research/candidate016_upper_opus_primary/source/T2_REVIEW.md').read_text()
 ck('both frozen reviews carry necessity wording','exactly when' in frozen and 'exactly when' in current)
 ck('scope explicit',not result['candidate_integrals_evaluated'] and not result['candidate_H_upper_asserted'] and not result['foreign_code_executed'])
 for rel,h in inputs.items():assert sha(R/rel)==h
 out={'utc':datetime.now(timezone.utc).isoformat(),'check_count':len(checks),'checks':checks,'inputs':inputs,'external_inputs':external,'counterexample_energies_over_pi':{k:str(v) for k,v in vals.items()},'elapsed_seconds':time.monotonic()-start,'peer_code_executed':False,'candidate_integrals_evaluated':False,'verdict':'CONFIRMED exact cancellation counterexample and reciprocal T4-475 rational fixtures; REFUTED only ungrouped beta necessity. General sufficient-domain theorem and actual candidate inputs unchanged. Numerical improved upper remains separately gated.'}
 o=B/'verification/result.json'
 with o.open('x') as f0:json.dump(out,f0,indent=2);f0.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'bindings',sha(o),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
