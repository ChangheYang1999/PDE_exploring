import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,gzip,hashlib,time
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(LANE/'proofs/160_family_margin/code'))
import certify as C
G=C.G;aa=C.aa;TARGET=F(12501,10000);THRESH=1250100
OLD=LANE/'proofs/160_family_margin/evidence/production/rows.jsonl.gz'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'date':now(),**kw}),flush=True)
def main():
 ctx.prec=512;ctx.threads=1;start=time.monotonic();c=C.Context();ends=c.end_bounds();assert all(aa(F(ends[s][0]['lower_exact']))>=aa(TARGET) for s in ['inner','outer'])
 meta={'date':now(),'target':str(TARGET),'bits':ctx.prec,'old_journal_sha256':sha(OLD),'old_audit_sha256':sha(LANE/'proofs/160_family_margin/evidence/audit.json'),'input_sha256':c.d.sha,'cache_sha256':sha(G.CACHE),'script_sha256':sha(Path(__file__)),'context_sha256':sha(Path(C.__file__)),'proof_sha256':sha(TOP/'PROOF.md'),'ends':ends}
 (TOP/'evidence/metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
 kept=0;replaced=0;newcount=0;failed=0;minimum=None;witness=None
 jp=TOP/'evidence/replacements.jsonl.gz';assert not jp.exists()
 with gzip.open(OLD,'rt') as old,gzip.open(jp,'wt',compresslevel=3) as out:
  for line in old:
   row=json.loads(line);c.ranges.clear();c.rows.clear();records=[]
   for leaf in row['leaves']:
    if leaf[6]>=THRESH:kept+=1;continue
    replaced+=1;children=[]
    def visit(l,r,a,b,path):
     nonlocal newcount,failed,minimum,witness
     val=c.bounds(row['label'],l,r,a,b)[0];low=F(G.rec(val)['lower_exact'])
     if low>=TARGET or len(path)>=10:
      ok=low>=TARGET;failed+=not ok;newcount+=1
      item=[path,str(l),str(r),str(a),str(b),str(low),int(ok)];children.append(item)
      if minimum is None or low<minimum:minimum=low;witness={'row':row['row'],'parent':leaf,'child':item}
      return
     if arb.pi()*aa(b-a)>=2*aa(r-l):
      m=(a+b)/2;visit(l,r,a,m,path+'a');visit(l,r,m,b,path+'b')
     else:
      m=(l+r)/2;visit(l,m,a,b,path+'l');visit(m,r,a,b,path+'r')
    visit(*map(F,leaf[2:6]),'');records.append({'parent':leaf,'children':children})
   if records:out.write(json.dumps({'row':row['row'],'label':row['label'],'records':records},separators=(',',':'))+'\n');out.flush()
   if row['row']%50==0:emit(row=row['row'],kept=kept,replaced=replaced,new_leaves=newcount,failed=failed,seconds=time.monotonic()-start)
 result={'date':now(),'status':'COMPUTED_PENDING_AUDIT' if not failed else 'UNRESOLVED','target':str(TARGET),'kept':kept,'replaced':replaced,'new_leaves':newcount,'failed':failed,'minimum_exact':str(minimum),'witness':witness,'journal_sha256':sha(jp),'metadata_sha256':sha(TOP/'evidence/metadata.json'),'seconds':time.monotonic()-start}
 (TOP/'evidence/result.json').write_text(json.dumps(result,indent=2)+'\n');emit(**result)
if __name__=='__main__':main()
