import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,gzip,time,heapq,importlib.util
from flint import ctx
from cover import reconstruct,sha,LANE
TOP=Path(__file__).resolve().parents[1]
p=LANE/'proofs/193_old_margin_refinement/code/audit.py';s=importlib.util.spec_from_file_location('audit193',p);A=importlib.util.module_from_spec(s);s.loader.exec_module(A)
R=A.R;G=A.G;aa=G.aa

def now():return datetime.now(timezone.utc).isoformat()
def save(x):(TOP/'evidence/audit.json').write_text(json.dumps(x,indent=2)+'\n')
def emit(**kw):print(json.dumps(dict(date=now(),**kw)),flush=True)
def main():
 start=time.monotonic();ctx.prec=640;ctx.threads=1;base,parents,prior=reconstruct();meta=json.loads((TOP/'evidence/metadata.json').read_text());res=json.loads((TOP/'evidence/result.json').read_text())
 assert res['status']=='COMPUTED_PENDING_AUDIT' and res['failed']==0 and meta['target']==res['target']=='3' and meta['bits']==512
 assert meta['prior']==prior and sha(TOP/'evidence/metadata.json')==res['metadata_sha256']
 assert sha(TOP/'code/certify.py')==meta['script_sha256'];assert sha(TOP/'code/cover.py')==meta['cover_code_sha256'];assert sha(Path(R.__file__))==meta['context_sha256'];assert sha(Path(G.__file__))==meta['global_sha256']
 proof=TOP/'evidence/proof_before_certificate.md';assert sha(proof if proof.exists() else TOP/'PROOF.md')==meta['proof_sha256']
 assert sha(G.M.SOURCE)==meta['source_sha256'] and sha(G.CACHE)==meta['cache_sha256']
 jp=TOP/'evidence/replacements.jsonl.gz';assert sha(jp)==res['journal_sha256']
 expected={(p['row'],*p['id']):p for p in parents};assert len(expected)==len(parents)==meta['parent_count']==res['parents'];seen=set();rowseen=set();count=0;minimum=None;worst=[];rep={}
 with gzip.open(jp,'rt') as stream:
  for line in stream:
   row=json.loads(line);idx=row['row'];assert idx not in rowseen;rowseen.add(idx);assert row['label']==base['records'][idx]['label']
   for rec in row['records']:
    parent=rec['parent'];key=(parent['row'],*parent['id']);assert key in expected and key not in seen and parent==expected[key] and parent['row']==idx;seen.add(key);tree={}
    for child in rec['children']:
     assert len(child)==7;path,sl,sr,sa,sb,lower,ok=child;assert isinstance(path,str) and len(path)<=12 and ok==1 and path not in tree;tree[path]=child
     l,r,a,b=map(F,parent['box'])
     for ch in path:
      if ch=='a':b=(a+b)/2
      elif ch=='b':a=(a+b)/2
      elif ch=='l':r=(l+r)/2
      elif ch=='r':l=(l+r)/2
      else:raise AssertionError(ch)
     assert tuple(map(F,(sl,sr,sa,sb)))==(l,r,a,b) and l<r and a<b and (r<=0 or l>=0)
     lo=F(lower);assert lo>=3;minimum=lo if minimum is None else min(minimum,lo);count+=1
     item=dict(row=idx,label=row['label'],parent=parent,child=child);ident=json.dumps([key,path],separators=(',',':'));entry=(-lo,ident,item)
     if len(worst)<24:heapq.heappush(worst,entry)
     elif lo<-worst[0][0]:heapq.heapreplace(worst,entry)
     band=(idx//600,0 if a<F(1,8) else 1 if a<F(3,8) else 2)
     if band not in rep:rep[band]=item
    pref={p[:i] for p in tree for i in range(len(p)+1)}
    def walk(path):
     branches={v[len(path)] for v in pref if len(v)==len(path)+1 and v.startswith(path)}
     if path in tree:assert not branches;return
     assert branches in ({'a','b'},{'l','r'})
     for ch in branches:walk(path+ch)
    walk('')
 assert seen==set(expected) and len(rowseen)==meta['row_count'] and count==res['new_leaves'] and minimum==F(res['minimum_exact'])
 audit=dict(date=now(),status='COVERAGE_PASS_REPLAY_PENDING',target='3',bits=640,source_sha256=meta['source_sha256'],journal_sha256=sha(jp),production_metadata_sha256=sha(TOP/'evidence/metadata.json'),production_result_sha256=sha(TOP/'evidence/result.json'),script_sha256=sha(Path(__file__)),alternate_replay_sha256=sha(Path(A.__file__)),parent_count=len(seen),new_leaves=count,kept_radial_roots=len(prior['kept_roots']),kept_old_leaves=prior['kept_leaves'],minimum_replacement_exact=str(minimum),minimum_kept_exact=prior['lowest_kept_exact'],replays=[])
 save(audit);emit(stage='coverage_pass',parents=len(seen),leaves=count);c=R.Context();assert c.d.sha==meta['source_sha256'];samples={}
 for item in [v[2] for v in worst]+list(rep.values()):samples[json.dumps([item['row'],item['parent']['id'],item['child'][0]],separators=(',',':'))]=item
 for ident,item in sorted(samples.items()):
  c.ranges.clear();c.rows.clear();child=item['child'];v=A.replay(c,item['label'],*map(F,child[1:5]));assert v>=3
  audit['replays'].append(dict(identity=ident,child=child,bound=G.rec(v),status='PASS',at_least_stored_lower=bool(v>=aa(F(child[5])))));save(audit)
 ep=LANE/'proofs/68_independent_global_coefficients/evidence/ends.json';e=json.loads(ep.read_text());assert sha(ep)==meta['ends_sha256'];assert F(e['inner_through_exact'])==c.d.tm and F(e['outer_from_exact'])==c.d.tp+8;audit['ends']={}
 for side in ('inner','outer'):
  pv,tv,gv=[aa(F(e[side][k]['upper_exact'])) for k in ('P_error_upper','T_error_upper','gradient_upper')]
  v=1+c.ell+aa(F(17,4))*(2*c.ell-1-pv-tv)-gv if side=='inner' else 1+c.ell-aa(F(5,8))*(c.ell+pv)-aa(F(17,4))*tv-gv
  assert v>=3;audit['ends'][side]=G.rec(v)
 audit.update(date=now(),status='CONFIRMED',replay_count=len(samples),seconds=time.monotonic()-start,proof_sha256=sha(TOP/'PROOF.md'));save(audit);emit(stage='finished',status='CONFIRMED',seconds=audit['seconds'])
if __name__=='__main__':main()
