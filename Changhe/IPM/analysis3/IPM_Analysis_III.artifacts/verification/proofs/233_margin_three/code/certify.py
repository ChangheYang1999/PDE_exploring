import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import defaultdict
import sys,json,gzip,time
from flint import arb,ctx
from cover import reconstruct,sha,LANE
sys.path.insert(0,str(LANE/'proofs/82_margin_refinement/code'))
import refine as R
G=R.G;aa=G.aa;TOP=Path(__file__).resolve().parents[1]
def now():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps(dict(date=now(),**kw)),flush=True)
def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;base,parents,prior=reconstruct();byrow=defaultdict(list)
 for p in parents:byrow[p['row']].append(p)
 c=R.Context();ep=LANE/'proofs/68_independent_global_coefficients/evidence/ends.json';e=json.loads(ep.read_text());assert e['input_sha256']==c.d.sha and e['cache_sha256']==sha(G.CACHE);ends={}
 for side in ('inner','outer'):
  pv,tv,gv=[aa(F(e[side][k]['upper_exact'])) for k in ('P_error_upper','T_error_upper','gradient_upper')]
  v=1+c.ell+aa(F(17,4))*(2*c.ell-1-pv-tv)-gv if side=='inner' else 1+c.ell-aa(F(5,8))*(c.ell+pv)-aa(F(17,4))*tv-gv
  assert v>=3;ends[side]=G.rec(v)
 meta=dict(date=now(),bits=512,target='3',source_sha256=c.d.sha,cache_sha256=sha(G.CACHE),ends_sha256=sha(ep),proof_sha256=sha(TOP/'PROOF.md'),script_sha256=sha(Path(__file__)),cover_code_sha256=sha(TOP/'code/cover.py'),context_sha256=sha(Path(R.__file__)),global_sha256=sha(Path(G.__file__)),parent_count=len(parents),row_count=len(byrow),prior=prior,ends=ends)
 (TOP/'evidence/metadata.json').write_text(json.dumps(meta,indent=2)+'\n');jp=TOP/'evidence/replacements.jsonl.gz';assert not jp.exists();count=failed=done=0;minimum=None;witness=None;emit(stage='start',parents=len(parents),rows=len(byrow))
 with gzip.open(jp,'wt',compresslevel=3) as out:
  for idx,pp in sorted(byrow.items()):
   c.ranges.clear();c.rows.clear();label=base['records'][idx]['label'];records=[]
   for parent in pp:
    children=[]
    def visit(l,r,a,b,path):
     nonlocal count,failed,minimum,witness
     ma=R.Angles.bounds(c.ang,c.radial(label,l,r),l,r,a,b,c.ell)[0];lo=F(G.rec(ma)['lower_exact'])
     if lo>=3 or len(path)>=12:
      ok=lo>=3;count+=1;failed+=not ok;child=[path,str(l),str(r),str(a),str(b),str(lo),int(ok)];children.append(child)
      if minimum is None or lo<minimum:minimum=lo;witness=dict(row=idx,parent=parent,child=child)
      return
     if arb.pi()*aa(b-a)>=2*aa(r-l):
      m=(a+b)/2;visit(l,r,a,m,path+'a');visit(l,r,m,b,path+'b')
     else:
      m=(l+r)/2;visit(l,m,a,b,path+'l');visit(m,r,a,b,path+'r')
    visit(*map(F,parent['box']),'');records.append(dict(parent=parent,children=children));done+=1
   out.write(json.dumps(dict(row=idx,label=label,records=records),separators=(',',':'))+'\n');out.flush()
   if idx%20==0:emit(row=idx,parents_done=done,leaves=count,failed=failed,seconds=time.monotonic()-start)
 result=dict(date=now(),status='COMPUTED_PENDING_AUDIT' if failed==0 else 'UNRESOLVED',target='3',parents=done,new_leaves=count,failed=failed,minimum_exact=str(minimum),witness=witness,journal_sha256=sha(jp),metadata_sha256=sha(TOP/'evidence/metadata.json'),seconds=time.monotonic()-start)
 (TOP/'evidence/result.json').write_text(json.dumps(result,indent=2)+'\n');emit(stage='finished',status=result['status'],seconds=result['seconds'])
if __name__=='__main__':main()
