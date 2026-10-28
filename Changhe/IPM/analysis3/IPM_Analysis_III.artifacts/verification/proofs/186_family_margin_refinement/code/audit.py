"""Independent exact partition audit and 640-bit angular replay."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import defaultdict
import sys,json,gzip,hashlib,time,heapq
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(LANE/'proofs/160_family_margin/code'))
import audit as A
C=A.C;G=A.G;aa=G.aa
OLD=LANE/'proofs/160_family_margin/evidence/production/rows.jsonl.gz'
TARGET=F(12501,10000);THRESH=1250100

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'date':now(),**kw}),flush=True)
def save(x):(TOP/'evidence/audit.json').write_text(json.dumps(x,indent=2)+'\n')

def main():
 start=time.monotonic();ctx.prec=640;ctx.threads=1
 meta=json.loads((TOP/'evidence/metadata.json').read_text());result=json.loads((TOP/'evidence/result.json').read_text())
 oldaudit=json.loads((LANE/'proofs/160_family_margin/evidence/audit.json').read_text())
 oldmeta=json.loads((LANE/'proofs/160_family_margin/evidence/production/metadata.json').read_text())
 assert oldaudit['status']=='CONFIRMED' and result['status']=='COMPUTED_PENDING_AUDIT' and result['failed']==0
 assert meta['target']==result['target']==str(TARGET)
 assert sha(OLD)==meta['old_journal_sha256']==oldaudit['journal_sha256']
 assert sha(LANE/'proofs/160_family_margin/evidence/audit.json')==meta['old_audit_sha256']
 assert sha(C.ORIGINAL)==meta['input_sha256']==oldaudit['source_sha256']
 assert sha(G.CACHE)==meta['cache_sha256']==oldmeta['cache_sha256']
 assert sha(Path(C.__file__))==meta['context_sha256']==oldmeta['script_sha256']
 assert sha(TOP/'code/certify.py')==meta['script_sha256']
 proof_input=TOP/'evidence/proof_before_certificate.md'
 assert sha(proof_input if proof_input.exists() else TOP/'PROOF.md')==meta['proof_sha256']
 assert sha(TOP/'evidence/metadata.json')==result['metadata_sha256']
 jp=TOP/'evidence/replacements.jsonl.gz';assert sha(jp)==result['journal_sha256']
 expected={};kept=0;total=0;labels={};lowest_kept=None
 with gzip.open(OLD,'rt') as f:
  for line in f:
   row=json.loads(line);labels[row['row']]=row['label']
   for leaf in row['leaves']:
    total+=1
    if leaf[6]>=THRESH:
     kept+=1;lowest_kept=leaf[6] if lowest_kept is None else min(lowest_kept,leaf[6])
    else:
     key=(row['row'],leaf[0],leaf[1]);assert key not in expected;expected[key]=leaf
 assert total==423719==oldaudit['leaf_count'] and kept==result['kept']
 assert len(expected)==8419==result['replaced']
 seen=set();newcount=0;minimum=None;witness=None;worst=[];representative={};rowset=set()
 with gzip.open(jp,'rt') as f:
  for line in f:
   row=json.loads(line);idx=row['row'];assert idx not in rowset;rowset.add(idx)
   assert row['label']==labels[idx]
   for record in row['records']:
    parent=record['parent'];key=(idx,parent[0],parent[1]);assert key in expected and key not in seen
    assert parent==expected[key];seen.add(key);tree={}
    for child in record['children']:
     assert len(child)==7
     path,sl,sr,sa,sb,bound,ok=child;assert isinstance(path,str) and len(path)<=10 and ok==1
     assert path not in tree;tree[path]=child
     l,r,a,b=map(F,parent[2:6])
     for ch in path:
      if ch=='a':b=(a+b)/2
      elif ch=='b':a=(a+b)/2
      elif ch=='l':r=(l+r)/2
      elif ch=='r':l=(l+r)/2
      else:raise AssertionError(('branch',ch))
     assert (F(sl),F(sr),F(sa),F(sb))==(l,r,a,b) and l<r and a<b and (r<=0 or l>=0)
     low=F(bound);assert low>=TARGET;newcount+=1
     identity=(idx,parent[0],parent[1],path)
     item={'row':idx,'label':row['label'],'parent':parent,'child':child}
     if minimum is None or low<minimum:minimum=low;witness=item
     entry=(-low,identity,item)
     if len(worst)<24:heapq.heappush(worst,entry)
     elif low<-worst[0][0]:heapq.heapreplace(worst,entry)
     band=(idx//160,0 if a<F(1,8) else 1 if a<F(3,8) else 2)
     if band not in representative:representative[band]=item
    prefixes={p[:i] for p in tree for i in range(len(p)+1)}
    def check(path):
     children={p[len(path)] for p in prefixes if len(p)==len(path)+1 and p.startswith(path)}
     if path in tree:assert not children;return
     assert children in ({'a','b'},{'l','r'})
     for ch in children:check(path+ch)
    check('')
 assert seen==set(expected) and newcount==result['new_leaves']
 assert minimum==F(result['minimum_exact'])
 assert witness['row']==result['witness']['row'] and witness['parent']==result['witness']['parent'] and witness['child']==result['witness']['child']
 audit={'date':now(),'status':'COVERAGE_PASS_REPLAY_PENDING','input_sha256':meta['input_sha256'],'old_journal_sha256':sha(OLD),'new_journal_sha256':sha(jp),'production_metadata_sha256':sha(TOP/'evidence/metadata.json'),'production_result_sha256':sha(TOP/'evidence/result.json'),'script_sha256':sha(Path(__file__)),'angular_replay_sha256':sha(Path(A.__file__)),'kept':kept,'replaced':len(seen),'new_leaves':newcount,'refined_rows':len(rowset),'total_final_leaves':kept+newcount,'lowest_kept_millionths':lowest_kept,'minimum_replacement_exact':str(minimum),'replays':[]}
 save(audit);emit(stage='coverage_pass',kept=kept,replaced=len(seen),new_leaves=newcount,refined_rows=len(rowset))
 c=A.R.Context();assert c.d.sha==meta['input_sha256']
 replay={}
 for item in [v[2] for v in worst]+list(representative.values()):
  p=item['parent'];ch=item['child'];replay[(item['row'],p[0],p[1],ch[0])]=item
 for key,item in sorted(replay.items()):
  c.ranges.clear();c.rows.clear();child=item['child']
  value=A.replay_bound(c,item['label'],*map(F,child[1:5]))[0]
  assert value>=aa(TARGET)
  comparison={'at_least_stored_lower':bool(value>=aa(F(child[5])))}
  if not comparison['at_least_stored_lower']:
   original_formula=C.Context.bounds(c,item['label'],*map(F,child[1:5]))[0]
   assert value.overlaps(original_formula) and original_formula>=aa(TARGET)
   comparison.update(replayed_production_formula=G.rec(original_formula),difference_from_stored_lower=G.rec(value-aa(F(child[5]))))
  audit['replays'].append({'identity':key,'child':child,'bound':G.rec(value),'comparison':comparison,'status':'PASS'})
  save(audit)
 ends=json.loads((LANE/'proofs/68_independent_global_coefficients/evidence/ends.json').read_text())
 assert sha(LANE/'proofs/68_independent_global_coefficients/evidence/ends.json')==oldmeta['ends']['ends_input_sha256']
 assert F(ends['inner_through_exact'])==c.d.tm and F(ends['outer_from_exact'])==c.d.tp+8
 audit['end_replays']={}
 for side in ('inner','outer'):
  epv,etv,egv=[aa(F(ends[side][name]['upper_exact'])) for name in ('P_error_upper','T_error_upper','gradient_upper')]
  if side=='inner':value=1+c.ell+aa(F(17,4))*(2*c.ell-1)-aa(F(1,4))*(6*c.ell-2)-aa(F(17,4))*epv-4*etv-egv
  else:value=1+c.ell-aa(F(37,40))*(c.ell+epv)-4*etv-egv
  assert value>=aa(TARGET);audit['end_replays'][side]=G.rec(value)
 audit.update(status='CONFIRMED',date=now(),target=str(TARGET),replay_count=len(replay),proof_sha256=sha(TOP/'PROOF.md'),seconds=time.monotonic()-start)
 save(audit);emit(stage='complete',status='CONFIRMED',target=str(TARGET),replays=len(replay),seconds=audit['seconds'])
if __name__=='__main__':main()
