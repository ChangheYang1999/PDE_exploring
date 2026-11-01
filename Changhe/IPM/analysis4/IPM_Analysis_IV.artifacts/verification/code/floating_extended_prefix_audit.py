"""Extended directed prefix comparisons and fits for six frozen floating outputs."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import json, gzip, math, sys, time
sys.dont_write_bytecode=True
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball
from period_polar_prefix_replay import unpack
ROOT=Path('research/263_floating_period_growth_audit')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def ab(x):return ball(mpq(str(x)))
def disp(x):return x.str(32,radius=True)
def fit(rows,Q):
    blocks=[]
    for j in range(max(rows)//Q):
        ns=list(range(j*Q+1,(j+1)*Q+1))
        if all(n in rows for n in ns):blocks.append((F((j+1)*Q),max(rows[n][0] for n in ns),max(rows[n][1] for n in ns)))
    out=[]
    for lo in (100,150,200):
        subset=[x for x in blocks if x[0]>=lo]
        if len(subset)<2:continue
        m=len(subset);sx=sum(x[0] for x in subset);sxx=sum(x[0]**2 for x in subset);dd=m*sxx-sx*sx
        channels=[]
        for col in (1,2):
            sy=sum(x[col] for x in subset);sxy=sum(x[0]*x[col] for x in subset)
            a=(m*sxy-sx*sy)/dd;b=(sy-a*sx)/m;sq=sum((a*x[0]+b-x[col])**2 for x in subset)/m
            A=(ab(a)*arb(10).log()).exp();R=(ab(a*Q/2)*arb(10).log()).exp();rms=ab(sq).sqrt()
            channels.append(dict(channel='density' if col==1 else 'stream',slope=str(a),intercept=str(b),A=disp(A),apparent_radius=disp(R),rms=disp(rms)))
        out.append(dict(window_lower=lo,first_block_end=int(subset[0][0]),block_count=m,last_block_end=int(subset[-1][0]),channels=channels))
    return out
start=time.monotonic();ctx.prec=768;results=[]
for Q in (7,8):
    for index,suffix in [(1,'f64e16'),(3,'f64'),(3,'ld')]:
        src=Path('research/264_floating_response_accuracy/sources')/f'hhf_Q{Q}h1_root{index}_N{301 if Q==7 else 304}_{suffix}.out'
        text=src.read_text();header=text.splitlines()[0];assert f'Q={Q} h=1' in header and '# done,' in text
        parent=Path('research/261_period_seven_eight_prefixes' if index==1 else 'research/262_tail_response_prefix')/'verification'
        prefix=parent/f'Q{Q}_root{index}_checks.json.gz';polar=parent/f'Q{Q}_root{index}_polar_replay.json.gz'
        d=read(prefix);pd=read(polar);assert d['all_checks_pass'] and pd['all_checks_pass'] and pd['source']==ref(prefix)
        rows={};tuning={}
        for line in text.splitlines():
            if line.startswith('n '):
                _,n,f,g=line.split()
                if all(math.isfinite(float(x)) for x in (f,g)):rows[int(n)]=(F(f),F(g))
            elif line.startswith('k '):
                t=line.split();tuning[int(t[1])]=dict(sigma=F(t[6]),Hsign=int(t[8]),Hlog=F(t[9]))
        logrows=[];harmrows=[]
        for r in d['norms']:
            n=r['n'];assert n in rows
            for c,j in [('F',0),('G',1)]:
                value=unpack(r[c]).log()/arb(10).log();error=abs(ab(rows[n][j])-value)
                logrows.append(dict(n=n,channel=c,printed=str(rows[n][j]),directed_log=disp(value),absolute_log_discrepancy=disp(error)))
        for r in d['harmonics']:
            k=r['n']//Q;assert k in tuning;t=tuning[k];H=unpack(r['H']);sigma=unpack(r['sigma'])
            sign=1 if H>0 else -1 if H<0 else 0;assert sign==t['Hsign']
            harmrows.append(dict(k=k,n=r['n'],relative_sigma_discrepancy=disp(abs((ab(t['sigma'])-sigma)/sigma)),absolute_H_log_discrepancy=disp(abs(ab(t['Hlog'])-abs(H).log()/arb(10).log())),H_sign_agrees=True))
        maxima={}
        for name,values in [('log_norm',[arb(x['absolute_log_discrepancy']) for x in logrows]),('log_H',[arb(x['absolute_H_log_discrepancy']) for x in harmrows]),('sigma_relative',[arb(x['relative_sigma_discrepancy']) for x in harmrows])]:
            top=max(values,key=lambda x:float(x.mid()));bound=F(1,10**16)
            while not all(x<ab(bound) for x in values):bound*=10
            maxima[name]=dict(largest_display=disp(top),strict_bound=str(bound))
        result=dict(Q=Q,root_index=index,source=ref(src),header=header,prefix=ref(prefix),polar=ref(polar),maximum_prefix_order=d['maximum_order'],last_printed_order=max(rows),producer_completed=True,log_comparisons=len(logrows),tuning_comparisons=len(harmrows),maxima=maxima,log_rows=logrows,tuning_rows=harmrows,fits=fit(rows,Q))
        results.append(result);print(json.dumps({k:v for k,v in result.items() if k not in ['log_rows','tuning_rows','fits','source','prefix','polar','header']}),flush=True)
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
out=dict(checked_at_utc=now,all_checks_pass=True,bits=768,scope='Finite extended-prefix comparisons and exact fits of frozen printed data; no high-order or asymptotic certificate.',rows=results,actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/extended_checks.json.gz').write_bytes(gzip.compress(json.dumps(out,separators=(',',':')).encode(),mtime=0))
(ROOT/'sources/floating_extended_prefix_audit.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(dict(at=now,actual_elapsed_s=out['actual_elapsed_s'])),flush=True)
