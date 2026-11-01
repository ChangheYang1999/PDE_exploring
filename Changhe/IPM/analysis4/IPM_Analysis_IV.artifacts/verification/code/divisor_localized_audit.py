"""Independent targeted Poisson-weight diagnostics with exact algebra checks."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as Q
import argparse, gzip, json, pickle, sys, time
sys.dont_write_bytecode=True

ROOT=Path('research/104_divisor_localized_criterion')
def inverse(h,s):
    if not s:return [Q(0)]+[v/Q(k+1) for k,v in enumerate(h)]
    y=[Q(0)]*(len(h)+1)
    for k in range(len(h)-1,-1,-1):y[k]=(h[k]-(k+1)*y[k+1])/s
    return y[:-1]
def monomial_weight(k,s):
    if not s:return Q(1,k+1)
    w=1/abs(s)
    for j in range(1,k+1):w=(1+j*w)/abs(s)
    return w

def exact():
    import logarithmic_verify as lv
    from cartesian_verify import sin_field, Q as CQ
    start=time.monotonic();count=0;normchecks=0;resonances=0
    for delta in map(Q,['1/2','2/3','3/4','2/5','4/7']):
        gap=Q(__import__('math').gcd(delta.numerator,2),delta.denominator)
        C0=1/gap
        for n in range(1,19):
            P=2-n*delta
            for m in [1,3,5,7,9]:
                for k in range(5):
                    h=[Q(0)]*k+[Q(1)]
                    terms={}; E=Q(0)
                    for q,s in [(m+1,P+m+1)]+([(m-1,P-m+1)] if m>1 else []):
                        ys=[-v/2 for v in inverse(h,s)]
                        if q*q==P*P:
                            ys[0]=Q(0);resonances+=1
                        for j,v in enumerate(ys):
                            if v:terms.setdefault(str(j),{})[str(q)]=v
                        W=monomial_weight(k,s)
                        assert W==sum(map(abs,inverse(h,s)))
                        if s and abs(s)<2*k:E+=W/2
                        else:assert W<=C0
                    norm=sum((abs(Q(v)) for row in terms.values() for v in row.values()),Q(0))
                    assert norm<=C0+E;normchecks+=1
                    f=lv.LogField(CQ(str(P-1)),{k:sin_field(CQ(str(P-1)),{m:CQ(1)}).modes})
                    g,_=lv.poisson(f)
                    observed={j:{q:Q(v) for q,v in row.items() if Q(v)} for j,row in g.amplitudes('sine').items()}
                    observed={j:row for j,row in observed.items() if row}
                    assert observed==terms,(str(delta),n,m,k,observed,terms)
                    count+=1
    # Resonant constant: the entire stream mode is normalized, not one branch.
    f=lv.LogField.pure(sin_field(CQ(-3),{3:CQ(1)}))
    g,_=lv.poisson(f)
    assert g.amplitudes('sine')=={'0':{'4':'-1/4'}}
    out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),exact_cartesian_comparisons=count,
             exact_norm_inequalities=normchecks,resonant_branch_cases=resonances,
             resonant_counterexample=dict(delta='2/3',n=6,density='sin(3 theta)',actual_stream=g.amplitudes('sine'),
                 unnormalized_q2_constant='1/8',canonical_q2_constant='0'),
             actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)

def numeric(checkpoint,select):
    from flint import arb,ctx
    from stream_precision_audit import unpack
    ctx.prec=640;start=time.monotonic()
    path=Path(checkpoint);raw=path.read_bytes()
    if path.suffix=='.gz':raw=gzip.decompress(raw)
    digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
    assert (state['A'],state['B'],state['prec'])==('2','3',512)
    text=lambda v:v.str(35,radius=True)
    log=lambda v:text(v.log()/arb(10).log()) if v>0 else None
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),input_path=str(path),
                input_sha256=digest,precision_bits=640,definition='E = half sum |a_nmk| W_k(s) over 0 < |s| < 2k, each incidence',
                base_constant='3/2',source_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),rows=[])
    for n in (sorted(state['f']) if select is None else select):
        if n not in state['f']:continue
        F=[[arb(*unpack(v)) for v in row] for row in state['f'][n]]
        G=[[arb(*unpack(v)) for v in row] for row in state['g'][n]]
        M=sum((abs(v) for row in F for v in row),arb(0))
        N=sum((abs(v) for row in G for v in row),arb(0))
        maxj=max(map(len,F));weights={};E=arb(0);total=arb(0);mode_terms={};bad=0;maxrel=arb(0)
        for k,row in enumerate(F):
            for j,v in enumerate(row):
                if v.is_exact() and v==0:continue
                if not abs(v)>0:bad+=1
                m=2*j+1
                for q,snum in [(m+1,3*(2+m+1)-2*n)]+([(m-1,3*(2-m+1)-2*n)] if m>1 else []):
                    key=abs(snum)
                    if key not in weights:
                        if key:
                            s=arb(key)/3; w=[1/s]
                            for h in range(1,len(F)):w.append((1+h*w[-1])/s)
                        else:w=[arb(1)/(h+1) for h in range(len(F))]
                        weights[key]=w
                    term=abs(v)*weights[key][k]/2;total+=term
                    if key and key<6*k:
                        E+=term;mode_terms[q]=mode_terms.get(q,arb(0))+term
        bound=3*M/2+E
        assert N<=bound or N.overlaps(bound)
        top=sorted(mode_terms.items(),key=lambda kv:float(kv[1].log()) if kv[1]>0 else -float('inf'),reverse=True)[:5]
        rec=dict(n=n,density_norm=text(M),stream_norm=text(N),targeted_weight=text(E),absolute_inverse_weight=text(total),
                 log10_E=log(E),log10_E_over_M=log(E/M),log10_absolute_over_N=log(total/N),
                 E_root=text((E.log()/n).exp()) if E>0 else '0',unresolved_input_coefficients=bad,
                 bound_strictly_verified=bool(N<bound),largest_stream_modes=[dict(q=q,weight=text(v),log10_weight=log(v)) for q,v in top])
        result['rows'].append(rec);result['actual_elapsed_s']=time.monotonic()-start
        (ROOT/'verification/targeted_weights_N315.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(rec),flush=True)
    result['complete']=True;result['actual_elapsed_s']=time.monotonic()-start
    (ROOT/'verification/targeted_weights_N315.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(complete=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--exact',action='store_true');ap.add_argument('--checkpoint');ap.add_argument('--all',action='store_true');ap.add_argument('--select',default='30,60,90,120,150,180,210,240,260,280,290,300,310,315');a=ap.parse_args()
    for name in ['sources','verification']:(ROOT/name).mkdir(parents=True,exist_ok=True)
    (ROOT/'sources/divisor_localized_audit.py.txt').write_bytes(Path(__file__).read_bytes())
    if a.exact:exact()
    if a.checkpoint:numeric(a.checkpoint,None if a.all else list(map(int,a.select.split(','))))
