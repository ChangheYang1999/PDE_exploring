"""Independent decoupled-family margin enclosures from original modal data."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,gzip,hashlib,time,argparse
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(LANE/'proofs/82_margin_refinement/code'))
import refine as R
G=R.G;aa=G.aa
ORIGINAL=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
assert G.M.SOURCE.resolve()==ORIGINAL.resolve()
PAIRS=((F(4),F(3,10),F(113,100)),(F(18,5),F(3,10),F(18,25)))
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def emit(**x):print(json.dumps({'date':now(),**x}),flush=True)
def floor_micro(x):
    q=F(G.rec(x)['lower_exact'])*1000000
    return q.numerator//q.denominator
def dot(x,y):return sum((u*v for u,v in zip(x,y)),arb(0))
class Context(R.Context):
    def bounds(self,label,l,r,a,b):
        P,Q,GR,GT=self.radial(label,l,r);sn,cs,c2,tang,sj,cj=self.ang.get(a,b)
        q=self.ell-dot(P,c2);tv=dot(Q,tang);gr=dot(GR,sj);gt=dot(GT,cj)
        gx=gr*cs-gt*sn;gy=gr*sn+gt*cs
        gu=(arb(gr.abs_upper())**2+arb(gt.abs_upper())**2).sqrt().upper()
        bp=arb((gu-gy.lower())/2)
        if gy>0:
            gl=(R.alo(gx)**2+R.alo(gy)**2).sqrt().lower();den=2*(gl+gy.lower())
            assert den>0
            bp=arb(min(bp.upper(),(arb(gx.abs_upper())**2/arb(den)).upper()))
        assert r<=0 or l>=0
        left=r<=0;mu=F(-17,4) if left else F(-5,8)
        ans=[1+self.ell+aa(mu-(0 if left else delta))*q+aa(ang)*tv-bp for ang,delta,_ in PAIRS]
        assert all(x.is_finite() for x in ans)
        return ans
    def end_bounds(self):
        epth=LANE/'proofs/68_independent_global_coefficients/evidence/ends.json'
        e=json.loads(epth.read_text());assert e['input_sha256']==self.d.sha and e['cache_sha256']==sha(G.CACHE)
        out={}
        for side in ('inner','outer'):
            ep=aa(F(e[side]['P_error_upper']['upper_exact']));et=aa(F(e[side]['T_error_upper']['upper_exact']));gr=aa(F(e[side]['gradient_upper']['upper_exact']))
            vals=[]
            for ang,delta,target in PAIRS:
                if side=='inner':
                    A=2*self.ell-1;Sigma=6*self.ell-2
                    value=1+self.ell+aa(F(17,4))*A-aa(F(17,4)-ang)*Sigma-aa(F(17,4))*ep-aa(ang)*et-gr
                else:
                    value=1+self.ell-aa(F(5,8)+delta)*self.ell-aa(F(5,8)+delta)*ep-aa(ang)*et-gr
                assert value>=aa(target)
                vals.append(G.rec(value))
            out[side]=vals
        out['ends_input_sha256']=sha(epth)
        return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');ap.add_argument('--bits',type=int,default=512);ap.add_argument('--max-depth',type=int,default=14);args=ap.parse_args()
    ctx.prec=args.bits;ctx.threads=1;start=time.monotonic();c=Context()
    basep=LANE/'proofs/68_independent_global_coefficients/evidence/full.json';base=json.loads(basep.read_text())
    assert base['input_sha256']==c.d.sha
    tag='pilot' if args.pilot else 'production';dest=TOP/'evidence'/tag;dest.mkdir(exist_ok=True)
    meta={'date':now(),'source_path':str(ORIGINAL),'input_sha256':c.d.sha,'cache_sha256':sha(G.CACHE),'base_sha256':sha(basep),'script_sha256':sha(Path(__file__)),'refine_sha256':sha(Path(R.__file__)),'global_sha256':sha(Path(G.__file__)),'bits':args.bits,'pairs':[[str(z) for z in row] for row in PAIRS],'radial_count':len(base['records']),'angular_count':128,'max_depth':args.max_depth,'ends':c.end_bounds()}
    (dest/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    selected=list(range(len(base['records'])))
    if args.pilot:selected=[0,1000,1500,2000,2600,3000,3115,3116,3150,3275]
    jp=dest/'rows.jsonl.gz';assert not jp.exists(),'Use a new tag or audit the existing journal; no overwrite.'
    mins=[None,None];witness=[None,None];count=0;failed=0
    with gzip.open(jp,'wt',compresslevel=3) as journal:
        for idx in selected:
            row=base['records'][idx];l=F(row['left_exact']);r=F(row['right_exact']);label=row['label'];c.ranges.clear();c.rows.clear();leaves=[]
            def visit(l,r,a,b,depth,j,path):
                nonlocal count,failed
                vals=c.bounds(label,l,r,a,b)
                if all(val>=aa(pair[2]) for val,pair in zip(vals,PAIRS)) or depth>=args.max_depth:
                    ok=all(val>=aa(pair[2]) for val,pair in zip(vals,PAIRS));failed+=not ok
                    ints=[floor_micro(val) for val in vals]
                    leaves.append([j,path,str(l),str(r),str(a),str(b),*ints,int(ok)])
                    count+=1
                    for k,val in enumerate(vals):
                        lo=F(G.rec(val.lower())['lower_exact'])
                        if mins[k] is None or lo<mins[k]:mins[k]=lo;witness[k]={'row':idx,'leaf':leaves[-1],'bound':G.rec(val)}
                    return
                if arb.pi()*aa(b-a)>=2*aa(r-l):
                    mid=(a+b)/2;visit(l,r,a,mid,depth+1,j,path+'a');visit(l,r,mid,b,depth+1,j,path+'b')
                else:
                    mid=(l+r)/2;visit(l,mid,a,b,depth+1,j,path+'l');visit(mid,r,a,b,depth+1,j,path+'r')
            parts=[(l,F(0),'L'),(F(0),r,'R')] if l<0<r else [(l,r,'')]
            for pl,pr,prefix in parts:
                for j in range(128):visit(pl,pr,F(j,256),F(j+1,256),0,j,prefix)
            journal.write(json.dumps({'row':idx,'label':label,'t0':str(l),'t1':str(r),'leaves':leaves},separators=(',',':'))+'\n');journal.flush()
            if idx%20==0 or args.pilot:emit(row=idx,selected=len(selected),leaves=count,failed=failed,minima=[float(x) for x in mins],seconds=time.monotonic()-start)
    result={'date':now(),'status':'PILOT' if args.pilot else ('COMPUTED_PENDING_AUDIT' if not failed else 'UNRESOLVED'),'row_count':len(selected),'leaf_count':count,'failed':failed,'minima_exact':[str(x) for x in mins],'witnesses':witness,'journal_sha256':sha(jp),'metadata_sha256':sha(dest/'metadata.json'),'seconds':time.monotonic()-start}
    (dest/'result.json').write_text(json.dumps(result,indent=2)+'\n');emit(stage='finished',status=result['status'],rows=len(selected),leaves=count,failed=failed,seconds=result['seconds'])
if __name__=='__main__':main()
