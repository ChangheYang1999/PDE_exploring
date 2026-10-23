"""Final finite-evidence publication gate. No numerical worker or producer imports."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification'
def main():
 out=V/'FINAL_BINDINGS.json'
 if out.exists():raise ValueError('final result already exists')
 checks=[];bindings={};cache={}
 def ck(n,b):
  checks.append(dict(name=n,passed=bool(b)))
  if not b:raise ValueError(n)
 def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
 def bind(p,h=None):
  p=str(p);actual=cache.setdefault(p,sha(p)) if p not in cache else cache[p]
  ck('binding '+p,h is None or actual==h)
  ck('consistent duplicate '+p,p not in bindings or bindings[p]==actual)
  bindings[p]=actual
  return Path(p)
 def read(p):return json.loads(bind(p).read_text())
 statuses={'DESIGN_ACCEPTANCE.json':'ACCEPTED_FOR_FINITE_COMPUTATION','MP_DESIGN_ACCEPTANCE.json':'ACCEPTED_FOR_FINITE_MP_COMPUTATION','FINAL_DESIGN_ACCEPTANCE.json':'ACCEPTED_CANDIDATE_FREE_FINAL_CHECKER_DESIGN','candidate/COMPLETE.json':'COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW','mp/COMPLETE.json':'COMPLETE_LARGER_NODE_MP_REQUIRES_INDEPENDENT_FINAL_AUDIT','FINAL_ARITHMETIC_CHECKS.json':'PASS_FINITE_LARGER_NODE_ARITHMETIC_REQUIRES_FINAL_REVIEW','PRINTED_COMPARISON_CHECKS.json':'PASS_FINITE_PRINTED_COMPARISONS','CENTER_REUSE_CHECKS.json':'PASS_EXACT_CENTER_REUSE','RESULT_SUPPLEMENT_MANUFACTURES.json':'PASS_MEDIAN_AND_SCOPE_MANUFACTURES','RESULT_SUPPLEMENT.json':'PASS_DESCRIPTIVE_MEDIAN_AND_SCOPE_SUPPLEMENT'}
 data={}
 for f,s in statuses.items():
  d=read(V/f);data[f]=d;ck('status '+f,d['status']==s);ck('complete assertions '+f,d['count']==len(d['checks'])and all(z['passed'] is True for z in d['checks']))
  if 'synthetic_only'in d:ck('synthetic fence '+f,d['synthetic_only']is(f=='RESULT_SUPPLEMENT_MANUFACTURES.json'))
  for p,h in d.get('bindings',{}).items():bind(p,h)
  for p,h in d.get('artifacts',{}).items():bind(p,h)
 x=read(V/'FINAL_SOURCE_AND_RADIAL_INDEX_CHECK.json');ck('source index inspection',x['status']=='PASS_FINITE_SOURCE_AND_RADIAL_INDEX_INSPECTION'and x['original_and_current_residual_and_median_lines_identical']and x['N192_far_absR_max_index']==9180 and x['radial_index_zero_based']==191)
 for p,h in x['bindings'].items():bind(p,h)
 sub=data['RESULT_SUPPLEMENT.json']['outputs'];ck('exactly one disclosed printed mismatch',sub['false_interval_count']==1 and sub['all_inside_printed_intervals']is False and [(z['N'],z['region'],z['metric'])for z in sub['all_false_interval_flags']]==[(192,'r>=100','medianRf')]);ck('all eight normalized increases',len(sub['normalized_cross_resolution'])==8 and all(z['increased']for z in sub['normalized_cross_resolution']))
 job=read(V/'MP_JOB.json');ap=Path(job['admission_path']);bind(ap,job['admission_sha256']);er=read(ap.with_suffix('.result.json'));ck('actual MP wrapper exited zero',er['returncode']==0)
 for f in ['JOB.json','MP_JOB.json']:
  j=read(V/f);proc=Path('/proc')/str(j['pid']);ck('recorded wrapper ceased '+f,not proc.exists()or(proc/'stat').read_text().rsplit(') ',1)[1].split()[0]=='Z')
 model=[]
 for name in ['final_results','final_followup','final_closure']:
  p=V/('opus_'+name);m=read(p/'metadata.json');ck('actual completed requested model '+name,m.get('requested_model')=='us.anthropic.claude-opus-5-5'and m.get('returned_model')=='claude-opus-5-5'and m.get('stop_reason')=='end_turn'and m.get('answer_nonempty')is True)
  req=bind(p/'request.txt',m['request_sha256']);ans=bind(p/'answer.md');ck('nonempty answer '+name,bool(ans.read_text().strip()));bind(p/'response.json');model.append(dict(stage=name,request_id=m['request_id'],actual_model=m['returned_model'],started_utc=m['started_utc'],finished_utc=m['finished_utc']))
 for p in sorted(V.glob('opus_*/metadata.json')):
  for f in ['metadata.json','answer.md','request.txt','response.json']:
   q=p.parent/f
   if q.exists():bind(q)
 for f in ['PROOF.md','FINAL_BINDING_PROOF.md','FINAL_RESULTS_REVIEW_RESOLUTION_PROOF.md','FINAL_FOLLOWUP_RESOLUTION.md','NF_PROSE_CORRECTION.md','FINAL_CLOSURE_RESOLUTION.md','RESULTS_DRAFT.md','RESULTS_DRAFT2.md','RESULTS_DRAFT3.md','RESULTS_DRAFT4.md','RESULTS.md']:bind(R/f)
 bind(__file__)
 text=(R/'RESULTS.md').read_text();ck('explicit finite scope',all(z in text for z in ['CONFIRMED','UNRESOLVED','Nf=abs((2x+V1)g_x)+abs((2y+V2)g_y)+abs(g)','1.6293092347287745e-8','not a full-plane elliptic IPM candidate']))
 ck('no discarded erroneous normalization','Nf=abs(2 X.grad(g))'not in text)
 for p,h in bindings.items():ck('stable '+p,sha(p)==h)
 result=dict(status='CONFIRMED_FINITE_LARGER_NODE_AUXILIARY_AUDIT',utc=datetime.now(timezone.utc).isoformat(),synthetic_only=False,count=len(checks),checks=checks,bindings=bindings,actual_final_reviews=model,scope='Independent finite hydrostatic vertical inverse and descriptive comparisons. No continuum enclosure, historical execution attestation or primary IPM endpoint.')
 out.write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count'],len(bindings),sha(out))
if __name__=='__main__':main()
