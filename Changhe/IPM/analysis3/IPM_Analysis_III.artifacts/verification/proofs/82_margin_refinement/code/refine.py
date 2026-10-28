"""Targeted original-data energy-margin refinement. No sampled acceptance."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,gzip,hashlib,time,argparse
from flint import arb,arb_mat,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(LANE/'proofs/68_independent_global_coefficients/code'))
import global_check as G
aa=G.aa;rec=G.rec

def now():return datetime.now(timezone.utc).isoformat()
def emit(**x):print(json.dumps({'date':now(),**x}),flush=True)
def alo(x):
    return arb(0) if x.contains(0) else arb(min(abs(x.lower()),abs(x.upper())))

class Angles:
    def __init__(self):self.cache={}
    def get(self,a,b):
        key=(a,b)
        if key in self.cache:return self.cache[key]
        theta=(arb.pi()*aa(a)).union(arb.pi()*aa(b));s=theta.sin();c=theta.cos()
        cos2=[(2*n*theta).cos() for n in range(1,262)]
        sinj=[((2*j+1)*theta).sin() for j in range(262)]
        cosj=[((2*j+1)*theta).cos() for j in range(262)]
        tang=[];last=arb(0)
        for n in range(1,262):
            last=-last+2*s*sinj[n-1];tang.append(last)
        value=(s,c,cos2,tang,sinj,cosj);self.cache[key]=value;return value
    def bounds(self,radial,l,r,a,b,ell):
        P,Q,GR,GT=radial;s,c,c2,tang,sj,cj=self.get(a,b)
        def dot(x,y):return sum((v*w for v,w in zip(x,y)),arb(0))
        q=ell-dot(P,c2);tv=dot(Q,tang);gr=dot(GR,sj);gt=dot(GT,cj)
        gx=gr*c-gt*s;gy=gr*s+gt*c
        gu=(arb(gr.abs_upper())**2+arb(gt.abs_upper())**2).sqrt().upper()
        bp=arb((gu-gy.lower())/2)
        if gy>0:
            gl=(alo(gx)**2+alo(gy)**2).sqrt().lower()
            den=2*(gl+gy.lower())
            assert den>0
            rat=(arb(gx.abs_upper())**2/arb(den)).upper()
            bp=arb(min(bp.upper(),rat))
        muv=G.hull_rationals(G.mu_values(l,r))
        mua=G.hull_rationals(([F(-17,2)] if l<=0 else [])+([F(-5,4)] if r>=0 else []))
        ka=1+ell+mua*q/2+aa(F(17,4))*tv
        ma=ka-bp;mr=1+ell+muv*q/2-bp
        assert all(x.is_finite() for x in (ma,mr,ka,bp))
        return ma.lower(),mr.lower()

class Context:
    def __init__(self):
        self.d=G.M.Data();G.check_hash(self.d);self.cache=G.load_cache(self.d)
        self.ell=1/aa(self.d.k);self.ang=Angles();self.rows={};self.ranges={};self.outer=None
    def radial(self,label,l,r):
        key=(tuple(label[:2]),l,r)
        if key in self.ranges:return self.ranges[key]
        mid=(l+r)/2;rad=(r-l)/2
        if label[0]=='outer':
            if self.outer is None:self.outer=G.outer_eps(self.d,self.cache)
            value=tuple([ep.range(mid-self.d.tp,rad) for ep in seq] for seq in self.outer)
        else:
            i=label[1]
            if i not in self.rows:
                idx=self.d.spans.index(i)
                self.rows[i]=(self.d.poly(i).tolist(),list(map(arb,self.cache['I_left'][idx])),list(map(arb,self.cache['J_right'][idx])))
            rows,IL,JR=self.rows[i];a,b=self.d.knots[i:i+2]
            H,S,rem=G.C.local_series(rows,IL,JR,a,b,aa(mid),aa(rad))
            vv=arb(0,aa(rad).upper());r2=(2*aa(l)).union(2*aa(r)).exp();P=[];Q=[]
            for n in range(1,262):
                ss=G.C.horner(S[n-1],vv)+arb(0,rem[n-1][0])
                sp=G.C.horner([(j+1)*S[n-1][j+1] for j in range(G.C.N)],vv)+arb(0,rem[n-1][1])
                P.append(2*n*r2*ss);Q.append(r2*(4*ss+sp))
            GR=[];GT=[]
            for j in range(262):
                h=G.C.horner([H[p][j] for p in range(8)],vv)
                hp=G.C.horner([(p+1)*H[p+1][j] for p in range(7)],vv)
                GR.append(r2*(3*h+hp));GT.append(r2*(2*j+1)*h)
            value=(P,Q,GR,GT)
        self.ranges[key]=value;return value

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');ap.add_argument('--bits',type=int,default=512)
    ap.add_argument('--max-depth',type=int,default=14);args=ap.parse_args();ctx.prec=args.bits;ctx.threads=1
    start=time.monotonic();basepath=LANE/'proofs/68_independent_global_coefficients/evidence/full.json'
    base=json.loads(basepath.read_text());target=F(5,2);c=Context();leaves=[];roots=[];unresolved=[];preserved=[];best=[arb.pos_inf(),arb.pos_inf()]
    selected=[i for i,row in enumerate(base['records']) if min(F(row[k]['lower_exact']) for k in ('ma_lower','mr_lower'))<target]
    if args.pilot:selected=sorted(selected,key=lambda i:min(F(base['records'][i][k]['lower_exact']) for k in ('ma_lower','mr_lower')))[:1]
    def refine(label,l,r,a,b,depth,root):
        ma,mr=c.ang.bounds(c.radial(label,l,r),l,r,a,b,c.ell)
        item={'root':root,'t0':str(l),'t1':str(r),'a0':str(a),'a1':str(b),'depth':depth,'ma_lower':rec(ma),'mr_lower':rec(mr)}
        if min(ma,mr)>=aa(target):
            item['verdict']='ACCEPTED';leaves.append(item);best[0]=min(best[0],ma);best[1]=min(best[1],mr);return
        if depth>=args.max_depth:
            item['verdict']='UNRESOLVED';leaves.append(item);unresolved.append(item);return
        if arb.pi()*aa(b-a)>=2*aa(r-l):
            m=(a+b)/2;refine(label,l,r,a,m,depth+1,root);refine(label,l,r,m,b,depth+1,root)
        else:
            m=(l+r)/2;refine(label,l,m,a,b,depth+1,root);refine(label,m,r,a,b,depth+1,root)
    for idx,row in enumerate(base['records']):
        if idx not in selected:
            if not args.pilot:
                assert min(F(row[k]['lower_exact']) for k in ('ma_lower','mr_lower'))>=target
                preserved.append(idx)
            continue
        c.ranges.clear();c.rows.clear();label=row['label'];l=F(row['left_exact']);r=F(row['right_exact'])
        for j in range(128):
            root=[idx,j];roots.append(root);refine(label,l,r,F(j,256),F(j+1,256),0,root)
        if len(roots)//128%10==0 or args.pilot:
            emit(stage='refining',radial_done=len(roots)//128,total=len(selected),leaves=len(leaves),unresolved=len(unresolved),ma=arb(best[0]).str(14),mr=arb(best[1]).str(14),seconds=time.monotonic()-start)
    out={'date':now(),'status':'PILOT' if args.pilot else ('COMPUTED_PENDING_AUDIT' if not unresolved else 'UNRESOLVED'),'bits':ctx.prec,'target':str(target),
         'input_sha256':c.d.sha,'base_sha256':hashlib.sha256(basepath.read_bytes()).hexdigest(),'cache_sha256':hashlib.sha256(G.CACHE.read_bytes()).hexdigest(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest(),
         'preserved_radial_indices':preserved,'selected_radial_indices':selected,'roots':roots,'leaves':leaves,'unresolved_count':len(unresolved),'ma_lower':rec(best[0]),'mr_lower':rec(best[1]),'seconds':time.monotonic()-start}
    dest=TOP/'evidence'/('pilot.json.gz' if args.pilot else 'refinement.json.gz')
    with gzip.open(dest,'wt') as f:json.dump(out,f)
    emit(stage='finished',status=out['status'],radial=len(selected),leaves=len(leaves),unresolved=len(unresolved),seconds=out['seconds'])
