import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import defaultdict
import sys,json,gzip,hashlib,time
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
def main():
 ctx.prec=512;ctx.threads=1;start=time.monotonic();c=R.Context()
 base=json.loads(BASE.read_text());old=json.loads(gzip.decompress(OLD.read_bytes()));oa=LANE/'proofs/82_margin_refinement/evidence/audit.json';oa0=json.loads(oa.read_text())
 assert oa0['status']=='PASS' and sha(OLD)==oa0['full_result_sha256'] and sha(BASE)==oa0['base_result_sha256']
 assert base['input_sha256']==old['input_sha256']==c.d.sha
 ep=LANE/'proofs/68_independent_global_coefficients/evidence/ends.json';e=json.loads(ep.read_text());ends={}
 assert sha(ep)==oa0['ends_sha256'] and e['input_sha256']==c.d.sha and e['cache_sha256']==sha(G.CACHE)
 for side in ('inner','outer'):
  pv,tv,gv=[aa(F(e[side][k]['upper_exact'])) for k in ('P_error_upper','T_error_upper','gradient_upper')]
  if side=='inner':v=1+c.ell+aa(F(17,4))*(2*c.ell-1)-aa(F(17,4))*(pv+tv)-gv
  else:v=1+c.ell-aa(F(5,8))*(c.ell+pv)-aa(F(17,4))*tv-gv
  assert v>=aa(TARGET);ends[side]=G.rec(v)
 selected=set(old['selected_radial_indices']);parents=defaultdict(list);kept_roots=[];kept_leaf_count=0
 for i,row in enumerate(base['records']):
  if i in selected:continue
  if F(row['ma_lower']['lower_exact'])>=TARGET:kept_roots.append(i);continue
  l,r=F(row['left_exact']),F(row['right_exact'])
  for j in range(128):parents[i].append(['base',j,str(l),str(r),str(F(j,256)),str(F(j+1,256))])
 for j,leaf in enumerate(old['leaves']):
  if F(leaf['ma_lower']['lower_exact'])>=TARGET:kept_leaf_count+=1;continue
  parents[leaf['root'][0]].append(['refined',j,leaf['t0'],leaf['t1'],leaf['a0'],leaf['a1']])
 meta={'date':now(),'target':str(TARGET),'bits':ctx.prec,'source_sha256':c.d.sha,'cache_sha256':sha(G.CACHE),'base_sha256':sha(BASE),'old_sha256':sha(OLD),'old_audit_sha256':sha(oa),'ends_sha256':sha(ep),'proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(Path(__file__)),'context_sha256':sha(Path(R.__file__)),'global_sha256':sha(Path(G.__file__)),'kept_roots':kept_roots,'kept_old_leaves':kept_leaf_count,'parent_count':sum(map(len,parents.values())),'row_count':len(parents),'ends':ends}
 (TOP/'evidence/metadata.json').write_text(json.dumps(meta,indent=2)+'\n');emit(stage='start',parents=meta['parent_count'],rows=len(parents),kept_roots=len(kept_roots),kept_leaves=kept_leaf_count)
 jp=TOP/'evidence/replacements.jsonl.gz';assert not jp.exists()
 count=failed=done=0;minimum=None;witness=None
 with gzip.open(jp,'wt',compresslevel=3) as out:
  for idx,pp in sorted(parents.items()):
   c.ranges.clear();c.rows.clear();label=base['records'][idx]['label'];records=[]
   for parent in pp:
    children=[]
    def visit(l,r,a,b,path):
     nonlocal count,failed,minimum,witness
     ma=R.Angles.bounds(c.ang,c.radial(label,l,r),l,r,a,b,c.ell)[0];lo=F(G.rec(ma)['lower_exact'])
     if lo>=TARGET or len(path)>=12:
      ok=lo>=TARGET;count+=1;failed+=not ok;child=[path,str(l),str(r),str(a),str(b),str(lo),int(ok)];children.append(child)
      if minimum is None or lo<minimum:minimum=lo;witness={'row':idx,'parent':parent,'child':child}
      return
     if arb.pi()*aa(b-a)>=2*aa(r-l):
      m=(a+b)/2;visit(l,r,a,m,path+'a');visit(l,r,m,b,path+'b')
     else:
      m=(l+r)/2;visit(l,m,a,b,path+'l');visit(m,r,a,b,path+'r')
    visit(*map(F,parent[2:]),'');records.append({'parent':parent,'children':children});done+=1
   out.write(json.dumps({'row':idx,'label':label,'records':records},separators=(',',':'))+'\n');out.flush()
   if idx%20==0:emit(row=idx,parents_done=done,leaves=count,failed=failed,seconds=time.monotonic()-start)
 result={'date':now(),'status':'COMPUTED_PENDING_AUDIT' if not failed else 'UNRESOLVED','target':str(TARGET),'parent_count':done,'new_leaves':count,'failed':failed,'minimum_exact':str(minimum),'witness':witness,'journal_sha256':sha(jp),'metadata_sha256':sha(TOP/'evidence/metadata.json'),'seconds':time.monotonic()-start}
 (TOP/'evidence/result.json').write_text(json.dumps(result,indent=2)+'\n');emit(stage='finished',status=result['status'],parents=done,leaves=count,failed=failed,seconds=result['seconds'])
if __name__=='__main__':main()
