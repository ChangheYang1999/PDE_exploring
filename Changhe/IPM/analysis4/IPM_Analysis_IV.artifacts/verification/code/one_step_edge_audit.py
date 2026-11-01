"""Directed one-step truncation audit using independent signed Laurent products."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,pickle,re,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,arb_poly,ctx
import logarithmic_verify as lv
from cartesian_verify import Q
from stream_precision_audit import unpack
from certified_initial_majorants import pack as pack_ball
ROOT=Path('research/213_one_step_edge_audit')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def text(x):return x.str(45,radius=True)
def put(path,data):
    temp=path.with_name(path.name+'.new');temp.write_text(json.dumps(data,indent=2)+'\n');temp.replace(path)

class Step:
    def __init__(self,state,n):self.state=state;self.n=n;self.stride=4*n+1;self.cache={}
    def field(self,which,n):
        key=which,n
        if key not in self.cache:self.cache[key]=[[v if isinstance(v,arb) else arb(*unpack(v)) for v in col] for col in self.state[which][n]]
        return self.cache[key]
    def encode(self,which,n,op='identity'):
        cols=self.field(which,n);shift=2*n;stride=self.stride;zero=arb(0)
        out=[zero]*(stride*(len(cols)-1)+4*n+1)
        radial=(arb(2) if which=='g' else arb(1))-arb(2*n)/3
        for q,col in enumerate(cols):
            for j,value in enumerate(col):
                m=2*j+(which=='f')
                if not m:assert value.is_zero();continue
                if value.is_zero():continue
                assert m<=shift
                a=q*stride+shift+m;b=q*stride+shift-m;v=value/2
                if op=='E':out[a]+=m*v;out[b]+=m*v
                else:
                    c=radial if op=='radial' else arb(1)
                    out[a]+=c*v;out[b]-=c*v
                    if op=='radial' and q:out[a-stride]+=q*v;out[b-stride]-=q*v
        return arb_poly(out)
    def term(self,i):
        j=self.n-i
        return self.encode('g',i,'radial')*self.encode('f',j,'E')-self.encode('g',i,'E')*self.encode('f',j,'radial')
    def inverse(self,p):
        cols=p.coeffs();lam=2*(self.n-1);s=self.stride
        for k in range(len(cols)-1,-1,-1):
            q=k//s
            if k+s<len(cols):cols[k]+=3*(q+1)*cols[k+s]
            cols[k]/=lam
        return arb_poly(cols)
    def clear(self):self.cache.clear()

def norm(p):return sum(map(abs,p.coeffs()),arb(0))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--order',type=int,default=350);ap.add_argument('--cutoffs',default='1,3,10,30,60,100,174,175');a=ap.parse_args()
    start=time.monotonic();ctx.prec=768
    reference_path=ROOT/'verification/exact_low_order_reference.json'
    if not reference_path.exists():put(reference_path,lv.run(Q(3),{1:Q(1)},12))
    reference=json.loads(reference_path.read_text());assert reference['delta']=='2/3' and reference['orders']==12
    low={'f':{},'g':{}}
    for row in reference['rows']:
        n=row['n']
        for key,label in [('f','density'),('g','stream')]:
            cols=[]
            for q in range(max(map(int,row[label]))+1):
                col=[arb(0)]*(n+(key=='g'))
                for mode,value in row[label].get(str(q),{}).items():
                    mode=int(mode);j=(mode-(key=='f'))//2
                    col[j]=arb(value)
                cols.append(col)
            low[key][n]=cols
    source=Path('../a4-num/ckpt/log_sin1_c3_N350.pkl');raw=source.read_bytes();metadata=dict(path=str(source),sha256=sha256(raw).hexdigest(),bytes=len(raw));state=pickle.loads(raw);del raw
    assert (state['A'],state['B'],state['ring'],state['prec'])==('2','3','arb',512)
    assert max(state['f'])>=a.order
    result=dict(started_at_utc=stamp(),bits=768,source=metadata,scope='Finite arithmetic conditional on reset input through329; discarded uncertainty excluded.',low_order_checks=[],rows=[],low_order_reference=dict(path=str(reference_path),sha256=sha256(reference_path.read_bytes()).hexdigest()))
    for n in [3,6,9,12]:
        step=Step(low,n);target=step.encode('f',n);rhs=sum((step.term(i) for i in range(1,n)),arb_poly());delta=step.inverse(rhs)-target
        assert all(v.contains(0) for v in delta.coeffs()),('low_order',n)
        result['low_order_checks'].append(dict(n=n,coefficient_count=len(delta),all_contain_zero=True));step.clear()
    n=a.order;step=Step(state,n);target=step.encode('f',n);mass=norm(target);assert mass>0
    cutoffs=set(map(int,a.cutoffs.split(',')));assert all(1<=c<=n//2 for c in cutoffs)
    acc=arb_poly();pairs=0
    for m in range(1,n//2+1):
        for i in sorted({m,n-m}):
            if 1<=i<n:acc+=step.term(i);pairs+=1
        step.clear()
        if m in cutoffs:
            computed=step.inverse(acc);delta=target-computed;error=norm(delta)/mass
            row=dict(cutoff=m,ordered_pairs=pairs,relative_error=pack_ball(error),relative_error_display=text(error),relative_truncated_norm_display=text(norm(computed)/mass),residual_coefficients=len(delta),checked_at_utc=stamp(),actual_elapsed_s=time.monotonic()-start)
            if m==n//2:
                assert pairs==n-1
                assert all(v.contains(0) for v in delta.coeffs()),'full equation consistency failed'
                row['all_residual_coefficients_contain_zero']=True
            result['rows'].append(row);put(ROOT/'verification/progress.json',result)
            print(json.dumps(row),flush=True)
    table=Path('../a4-num/notes/onestep_edge_error_350.txt');raw=table.read_bytes();(ROOT/'sources/producer_table.txt').write_bytes(raw)
    result['printed_table']=dict(path=str(table),sha256=sha256(raw).hexdigest());checks=[]
    for line in raw.decode().splitlines():
        match=re.search(r'L =\s*(\d+):.*?=\s*([\d.eE+-]+);',line)
        if match:
            m=int(match[1]);token=match[2];row=next((r for r in result['rows'] if r['cutoff']==m),None)
            if row is not None:
                exponent=int(token.lower().split('e')[1]);tol=arb('0.000051')*arb(10)**exponent
                assert arb(row['relative_error_display']).overlaps(arb(token,tol)),(m,row['relative_error_display'],token)
                checks.append(dict(cutoff=m,reported=token,rounded_comparison_passes=True))
    result.update(completed_at_utc=stamp(),all_checks_pass=True,printed_comparisons=checks,actual_elapsed_s=time.monotonic()-start)
    for name in ['one_step_edge_audit.py','stream_precision_audit.py','certified_initial_majorants.py','logarithmic_verify.py','cartesian_verify.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    peer=Path('../a4-num/code/onestep_edge_error.py');raw=peer.read_bytes();(ROOT/'sources/producer_onestep_edge_error.py').write_bytes(raw);result['producer_code']=dict(path=str(peer),sha256=sha256(raw).hexdigest())
    put(ROOT/'verification/checks.json',result);print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        put(ROOT/'verification/FAILURE.json',out);print(json.dumps(out),flush=True);raise SystemExit(1)
