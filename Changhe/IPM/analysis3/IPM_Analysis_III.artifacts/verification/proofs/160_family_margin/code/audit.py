"""Exact partition audit and original-data 640-bit replay for family margins."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import defaultdict
import sys,json,gzip,hashlib,time
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(TOP/'code'))
import certify as C
R=C.R;G=C.G;aa=G.aa
DEST=TOP/'evidence/production'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'date':now(),**kw}),flush=True)
def save(x):
    (TOP/'evidence/audit.json').write_text(json.dumps(x,indent=2)+'\n')
def minabs(z):
    return arb(0) if z.contains(0) else min(abs(z.lower()),abs(z.upper()))
def replay_bound(c,label,l,r,a,b):
    # Assemble the angular and margin expressions independently of Context.bounds.
    P,Q,GR,GT=c.radial(label,l,r)
    theta=(arb.pi()*aa(a)).union(arb.pi()*aa(b));sn=theta.sin();cs=theta.cos()
    radial_velocity=c.ell;angular_product=arb(0);grad_r=arb(0);grad_t=arb(0)
    previous=arb(0)
    for n in range(1,262):
        radial_velocity-=P[n-1]*(2*n*theta).cos()
        current=2*sn*((2*n-1)*theta).sin()-previous
        angular_product+=Q[n-1]*current
        previous=current
    for j in range(262):
        grad_r+=GR[j]*((2*j+1)*theta).sin()
        grad_t+=GT[j]*((2*j+1)*theta).cos()
    gx=grad_r*cs-grad_t*sn;gy=grad_r*sn+grad_t*cs
    grad_upper=(arb(grad_r.abs_upper())**2+arb(grad_t.abs_upper())**2).sqrt().upper()
    b_upper=arb((grad_upper-gy.lower())/2)
    if gy>0:
        grad_lower=(minabs(gx)**2+minabs(gy)**2).sqrt().lower()
        other=(arb(gx.abs_upper())**2/(2*(grad_lower+gy.lower()))).upper()
        b_upper=arb(min(b_upper.upper(),other))
    assert r<=0 or l>=0
    mu=F(-17,4) if r<=0 else F(-5,8)
    out=[]
    for angular,delta,target in C.PAIRS:
        coefficient=mu if r<=0 else mu-delta
        out.append(1+c.ell+aa(coefficient)*radial_velocity+aa(angular)*angular_product-b_upper)
    return out

def main():
    start=time.monotonic();ctx.prec=640;ctx.threads=1
    meta=json.loads((DEST/'metadata.json').read_text());result=json.loads((DEST/'result.json').read_text())
    assert result['status']=='COMPUTED_PENDING_AUDIT' and result['failed']==0
    assert sha(DEST/'metadata.json')==result['metadata_sha256']
    assert sha(DEST/'rows.jsonl.gz')==result['journal_sha256']
    assert meta['source_path']==str(C.ORIGINAL) and sha(C.ORIGINAL)==meta['input_sha256']
    assert sha(Path(C.__file__))==meta['script_sha256']
    assert sha(Path(R.__file__))==meta['refine_sha256']
    assert sha(Path(G.__file__))==meta['global_sha256']
    assert sha(G.CACHE)==meta['cache_sha256']
    bp=LANE/'proofs/68_independent_global_coefficients/evidence/full.json'
    ep=LANE/'proofs/68_independent_global_coefficients/evidence/ends.json'
    assert sha(bp)==meta['base_sha256'] and sha(ep)==meta['ends']['ends_input_sha256']
    base=json.loads(bp.read_text());ends=json.loads(ep.read_text())
    assert base['input_sha256']==ends['input_sha256']==meta['input_sha256']
    assert base['cache_sha256']==ends['cache_sha256']==meta['cache_sha256']
    assert meta['bits']==512 and meta['angular_count']==128 and meta['max_depth']==14
    assert meta['pairs']==[[str(v) for v in row] for row in C.PAIRS]
    c=R.Context();assert c.d.sha==meta['input_sha256']
    expected=[]
    for i in c.d.spans:
        a,b=c.d.knots[i:i+2];m=(a+b)/2
        expected.extend([(a,m),(m,b)])
    expected.extend([(c.d.tp+F(j,20),c.d.tp+F(j+1,20)) for j in range(160)])
    assert len(expected)==3276==len(base['records'])==meta['radial_count']
    assert F(ends['inner_through_exact'])==c.d.tm and F(ends['outer_from_exact'])==c.d.tp+8
    for i,(a,b) in enumerate(expected):
        assert (F(base['records'][i]['left_exact']),F(base['records'][i]['right_exact']))==(a,b)
        if i:assert expected[i-1][1]==a
    witnesses={(w['row'],w['leaf'][0],w['leaf'][1]) for w in result['witnesses']}
    representative={0,1000,1500,2000,2600,3000,3115,3116,3150,3275}
    zero_roots={i for i,(a,b) in enumerate(expected) if a<=0<=b}
    representative|=zero_roots
    replay=[];count=0;root_count=0;maxdepth=0;lowest=[None,None];matched=set()
    with gzip.open(DEST/'rows.jsonl.gz','rt') as f:
        for idx,line in enumerate(f):
            row=json.loads(line);assert row['row']==idx
            a,b=expected[idx];br=base['records'][idx]
            assert (F(row['t0']),F(row['t1']))==(a,b) and row['label']==br['label']
            crossing=a<0<b;trees=defaultdict(dict)
            for leaf in row['leaves']:
                assert len(leaf)==9
                j,path,sl,sr,sa,sb,v0,v1,ok=leaf
                assert type(j) is int and 0<=j<128 and ok==1
                l,r=a,b
                if crossing:
                    assert path and path[0] in 'LR'
                    prefix=path[0];address=path[1:]
                    if prefix=='L':r=F(0)
                    else:l=F(0)
                else:prefix='';address=path
                al,ar=F(j,256),F(j+1,256)
                assert len(address)<=14
                for ch in address:
                    if ch=='a':ar=(al+ar)/2
                    elif ch=='b':al=(al+ar)/2
                    elif ch=='l':r=(l+r)/2
                    elif ch=='r':l=(l+r)/2
                    else:raise AssertionError(('branch',ch))
                assert (F(sl),F(sr),F(sa),F(sb))==(l,r,al,ar)
                assert l<r and al<ar and (r<=0 or l>=0)
                tree=trees[(j,prefix)];assert address not in tree;tree[address]=leaf
                for k,v in enumerate((v0,v1)):
                    assert type(v) is int and F(v,1000000)>=C.PAIRS[k][2]
                    lowest[k]=v if lowest[k] is None else min(lowest[k],v)
                key=(idx,j,path)
                choose=key in witnesses or (idx in representative and j in (0,63,127))
                if choose:
                    replay.append((idx,row['label'],leaf))
                if key in witnesses:matched.add(key)
                maxdepth=max(maxdepth,len(address));count+=1
            expectedtrees={(j,prefix) for j in range(128) for prefix in (('L','R') if crossing else ('',))}
            assert set(trees)==expectedtrees
            for key,tree in trees.items():
                allprefixes={p[:i] for p in tree for i in range(len(p)+1)}
                def check(p):
                    children={q[len(p)] for q in allprefixes if len(q)==len(p)+1 and q.startswith(p)}
                    if p in tree:assert not children;return
                    assert children in ({'a','b'},{'l','r'})
                    for ch in children:check(p+ch)
                check('')
            root_count+=1
            if idx%400==0:emit(stage='coverage',row=idx,leaves=count)
    assert root_count==result['row_count']==3276 and count==result['leaf_count']
    assert matched==witnesses
    for k,w in enumerate(result['witnesses']):
        assert w['leaf'][6+k]==lowest[k]
        lo=F(w['bound']['lower_exact'])
        assert lo==F(result['minima_exact'][k]) and lo>=C.PAIRS[k][2]
        assert lo*1000000//1==lowest[k]
    audit={'date':now(),'status':'COVERAGE_PASS_REPLAY_PENDING','source_sha256':meta['input_sha256'],
           'metadata_sha256':sha(DEST/'metadata.json'),'journal_sha256':sha(DEST/'rows.jsonl.gz'),
           'root_count':root_count,'leaf_count':count,'max_depth':maxdepth,'minimum_millionths':lowest,
           'replay_count':len(replay),'replays':[],'script_sha256':sha(Path(__file__)),
           'source_loader_sha256':sha(Path(G.M.__file__)),'radial_series_sha256':sha(Path(G.C.__file__))}
    save(audit)
    for idx,label,leaf in replay:
        j,path,sl,sr,sa,sb,v0,v1,_=leaf
        c.ranges.clear();c.rows.clear()
        bounds=replay_bound(c,label,F(sl),F(sr),F(sa),F(sb))
        for k,z in enumerate(bounds):assert z>=aa(F((v0,v1)[k],1000000))
        audit['replays'].append({'row':idx,'leaf':leaf,'bounds':[G.rec(z) for z in bounds],'status':'PASS'})
        save(audit)
    # Reassemble both entire half-line bounds from exact saved error endpoints.
    audit['end_replays']={}
    for side in ('inner','outer'):
        err=[aa(F(ends[side][name]['upper_exact'])) for name in ('P_error_upper','T_error_upper','gradient_upper')]
        epv,etv,egv=err;vals=[]
        for angular,delta,target in C.PAIRS:
            if side=='inner':
                value=1+c.ell+aa(F(17,4))*(2*c.ell-1)-aa(F(17,4)-angular)*(6*c.ell-2)-aa(F(17,4))*epv-aa(angular)*etv-egv
            else:
                value=1+c.ell-aa(F(5,8)+delta)*(c.ell+epv)-aa(angular)*etv-egv
            assert value>=aa(target)
            vals.append(G.rec(value))
        audit['end_replays'][side]=vals
    audit['status']='CONFIRMED';audit['date']=now();audit['seconds']=time.monotonic()-start
    audit['proof_sha256']=sha(TOP/'PROOF.md');save(audit)
    emit(stage='complete',status=audit['status'],roots=root_count,leaves=count,replays=len(replay),seconds=audit['seconds'])
if __name__=='__main__':main()
