import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import defaultdict
import sys,json,gzip,hashlib,time,heapq
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(LANE/'proofs/82_margin_refinement/code'))
import refine as R
G=R.G;aa=G.aa;TARGET=F(2927,1000)
BASE=LANE/'proofs/68_independent_global_coefficients/evidence/full.json'
OLD=LANE/'proofs/82_margin_refinement/evidence/refinement.json.gz'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'date':now(),**kw}),flush=True)
def save(x):(TOP/'evidence/audit.json').write_text(json.dumps(x,indent=2)+'\n')
def replay(c,label,l,r,a,b):
 P,Q,GR,GT=c.radial(label,l,r);th=(arb.pi()*aa(a)).union(arb.pi()*aa(b));sn=th.sin();cs=th.cos()
 q=c.ell;tv=arb(0);gr=arb(0);gt=arb(0);prev=arb(0)
 for n in range(1,262):
  q-=P[n-1]*(2*n*th).cos();cur=2*sn*((2*n-1)*th).sin()-prev;tv+=Q[n-1]*cur;prev=cur
 for j in range(262):gr+=GR[j]*((2*j+1)*th).sin();gt+=GT[j]*((2*j+1)*th).cos()
 gx=gr*cs-gt*sn;gy=gr*sn+gt*cs;gu=(arb(gr.abs_upper())**2+arb(gt.abs_upper())**2).sqrt().upper();bp=arb((gu-gy.lower())/2)
 def amin(x):return arb(0) if x.contains(0) else min(abs(x.lower()),abs(x.upper()))
 if gy>0:
  gl=(amin(gx)**2+amin(gy)**2).sqrt().lower();second=(arb(gx.abs_upper())**2/(2*(gl+gy.lower()))).upper();bp=arb(min(bp.upper(),second))
 assert r<=0 or l>=0
 return 1+c.ell-aa(F(17,4) if r<=0 else F(5,8))*q+aa(F(17,4))*tv-bp

def main():
 start=time.monotonic();ctx.prec=640;ctx.threads=1
 meta=json.loads((TOP/'evidence/metadata.json').read_text());result=json.loads((TOP/'evidence/result.json').read_text());oa=LANE/'proofs/82_margin_refinement/evidence/audit.json';oldaud=json.loads(oa.read_text())
 assert result['status']=='COMPUTED_PENDING_AUDIT' and result['failed']==0 and oldaud['status']=='PASS'
 assert meta['target']==result['target']==str(TARGET) and meta['bits']==512
 assert sha(BASE)==meta['base_sha256']==oldaud['base_result_sha256'] and sha(OLD)==meta['old_sha256']==oldaud['full_result_sha256'] and sha(oa)==meta['old_audit_sha256']
 assert sha(G.M.SOURCE)==meta['source_sha256']==oldaud['source_sha256'] and sha(G.CACHE)==meta['cache_sha256']
 assert sha(TOP/'code/certify.py')==meta['script_sha256'] and sha(Path(R.__file__))==meta['context_sha256'] and sha(Path(G.__file__))==meta['global_sha256']
 proof=TOP/'evidence/proof_before_certificate.md';assert sha(proof if proof.exists() else TOP/'PROOF.md')==meta['proof_sha256']
 assert sha(TOP/'evidence/metadata.json')==result['metadata_sha256'];jp=TOP/'evidence/replacements.jsonl.gz';assert sha(jp)==result['journal_sha256']
 base=json.loads(BASE.read_text());old=json.loads(gzip.decompress(OLD.read_bytes()));selected=set(old['selected_radial_indices']);expected={};kept_roots=[];kept_leaves=0;lowest_kept=None
 for idx,row in enumerate(base['records']):
  if idx in selected:continue
  lo=F(row['ma_lower']['lower_exact'])
  if lo>=TARGET:kept_roots.append(idx);lowest_kept=lo if lowest_kept is None else min(lowest_kept,lo);continue
  for j in range(128):expected[(idx,'base',j)]=['base',j,row['left_exact'],row['right_exact'],str(F(j,256)),str(F(j+1,256))]
 for j,leaf in enumerate(old['leaves']):
  lo=F(leaf['ma_lower']['lower_exact'])
  if lo>=TARGET:kept_leaves+=1;lowest_kept=lo if lowest_kept is None else min(lowest_kept,lo);continue
  idx=leaf['root'][0];expected[(idx,'refined',j)]=['refined',j,leaf['t0'],leaf['t1'],leaf['a0'],leaf['a1']]
 assert kept_roots==meta['kept_roots'] and kept_leaves==meta['kept_old_leaves'] and len(expected)==meta['parent_count']==result['parent_count']
 seen=set();rowseen=set();count=0;minimum=None;worst=[];rep={}
 with gzip.open(jp,'rt') as f:
  for line in f:
   row=json.loads(line);idx=row['row'];assert idx not in rowseen;rowseen.add(idx);assert row['label']==base['records'][idx]['label']
   for record in row['records']:
    parent=record['parent'];key=(idx,parent[0],parent[1]);assert key in expected and key not in seen and parent==expected[key];seen.add(key);tree={}
    for child in record['children']:
     assert len(child)==7;path,sl,sr,sa,sb,lower,ok=child;assert isinstance(path,str) and len(path)<=12 and ok==1 and path not in tree;tree[path]=child
     l,r,a,b=map(F,parent[2:])
     for ch in path:
      if ch=='a':b=(a+b)/2
      elif ch=='b':a=(a+b)/2
      elif ch=='l':r=(l+r)/2
      elif ch=='r':l=(l+r)/2
      else:raise AssertionError(ch)
     assert (F(sl),F(sr),F(sa),F(sb))==(l,r,a,b) and l<r and a<b and (r<=0 or l>=0)
     lo=F(lower);assert lo>=TARGET;minimum=lo if minimum is None else min(minimum,lo);count+=1
     ident=(*key,path);item={'row':idx,'label':row['label'],'parent':parent,'child':child};entry=(-lo,ident,item)
     if len(worst)<24:heapq.heappush(worst,entry)
     elif lo<-worst[0][0]:heapq.heapreplace(worst,entry)
     band=(idx//400,0 if a<F(1,8) else 1 if a<F(3,8) else 2)
     if band not in rep:rep[band]=item
    pref={p[:i] for p in tree for i in range(len(p)+1)}
    def walk(p):
     branches={v[len(p)] for v in pref if len(v)==len(p)+1 and v.startswith(p)}
     if p in tree:assert not branches;return
     assert branches in ({'a','b'},{'l','r'})
     for ch in branches:walk(p+ch)
    walk('')
 assert seen==set(expected) and len(rowseen)==meta['row_count'] and count==result['new_leaves'] and minimum==F(result['minimum_exact'])
 audit={'date':now(),'status':'COVERAGE_PASS_REPLAY_PENDING','source_sha256':meta['source_sha256'],'journal_sha256':sha(jp),'production_metadata_sha256':sha(TOP/'evidence/metadata.json'),'production_result_sha256':sha(TOP/'evidence/result.json'),'script_sha256':sha(Path(__file__)),'parent_count':len(seen),'new_leaves':count,'kept_radial_roots':len(kept_roots),'kept_old_leaves':kept_leaves,'minimum_replacement_exact':str(minimum),'minimum_kept_exact':str(lowest_kept),'replays':[]}
 save(audit);emit(stage='coverage_pass',parents=len(seen),new_leaves=count)
 c=R.Context();assert c.d.sha==meta['source_sha256'];samples={}
 for item in [v[2] for v in worst]+list(rep.values()):samples[(item['row'],*item['parent'][:2],item['child'][0])]=item
 for key,item in sorted(samples.items()):
  c.ranges.clear();c.rows.clear();child=item['child'];val=replay(c,item['label'],*map(F,child[1:5]));assert val>=aa(TARGET)
  audit['replays'].append({'identity':key,'child':child,'bound':G.rec(val),'status':'PASS','at_least_stored_lower':bool(val>=aa(F(child[5])))})
  save(audit)
 ep=LANE/'proofs/68_independent_global_coefficients/evidence/ends.json';e=json.loads(ep.read_text());assert sha(ep)==meta['ends_sha256']==oldaud['ends_sha256']
 assert F(e['inner_through_exact'])==c.d.tm and F(e['outer_from_exact'])==c.d.tp+8
 audit['ends']={}
 for side in ('inner','outer'):
  pv,tv,gv=[aa(F(e[side][k]['upper_exact'])) for k in ('P_error_upper','T_error_upper','gradient_upper')]
  if side=='inner':v=1+c.ell+aa(F(17,4))*(2*c.ell-1-pv-tv)-gv
  else:v=1+c.ell-aa(F(5,8))*(c.ell+pv)-aa(F(17,4))*tv-gv
  assert v>=aa(TARGET);audit['ends'][side]=G.rec(v)
 audit.update(status='CONFIRMED',date=now(),target=str(TARGET),replay_count=len(samples),proof_sha256=sha(TOP/'PROOF.md'),seconds=time.monotonic()-start);save(audit);emit(stage='finished',status='CONFIRMED',replays=len(samples),seconds=audit['seconds'])
if __name__=='__main__':main()
