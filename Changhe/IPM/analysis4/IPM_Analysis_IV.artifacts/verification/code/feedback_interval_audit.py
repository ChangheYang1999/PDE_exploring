"""Independent interval check of edge feedback using signed Laurent products."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, json, pickle, sys, time
from flint import arb, arb_poly, ctx
from stream_precision_audit import unpack
from read_checkpoint_archive import read_bytes
sys.dont_write_bytecode = True
ap = argparse.ArgumentParser()
ap.add_argument('--checkpoint', default='research/82_weighted_loss_criterion/update_N310_20261031T0708Z/verification/input_checkpoint.pkl.gz')
ap.add_argument('--orders', default='3,4,5,8,12,30,60,100,170,200,230,260,280,290')
ap.add_argument('--seconds', type=float, default=480)
a = ap.parse_args()
ctx.prec = 640
start = time.monotonic()
root = Path('research/97_feedback_interval_audit/verification') / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
root.mkdir(parents=True); (root/'sources').mkdir()
raw = read_bytes(a.checkpoint); digest = sha256(raw).hexdigest(); state = pickle.loads(raw); del raw
assert (state['A'], state['B'], state['prec']) == ('2','3',512)
peer_raw = Path('../a4-lead/logs/feedback_term_c3.json').read_bytes()
peer = json.loads(peer_raw)['orders']; (root/'peer_feedback.json').write_bytes(peer_raw)
(root/'sources/peer_feedback_term.py.txt').write_bytes(Path('../a4-lead/code/feedback_term.py').read_bytes())
values = {}
text = lambda v: v.str(35, radius=True)
for name in ['feedback_interval_audit.py','read_checkpoint_archive.py','stream_precision_audit.py']:
    (root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
record = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'), checkpoint_path=a.checkpoint, checkpoint_sha256=digest, peer_table_sha256=sha256(peer_raw).hexdigest(), precision_bits=640, orders=[])

def field(which, n):
    key = which,n
    if key not in values:
        values[key] = [[arb(*unpack(z)) for z in row] for row in state[which][n]]
    return values[key]

def pack(which, n, stride, op='identity', radial=None):
    cols = field(which,n); shift=2*n
    out=[arb(0) for _ in range(stride*(len(cols)-1)+4*n+1)]
    for q,row in enumerate(cols):
        for k,v in enumerate(row):
            m=2*k+(which=='f')
            if m==0:
                assert v.is_zero(); continue
            if v.is_zero(): continue
            assert m<=shift
            plus,minus=q*stride+shift+m,q*stride+shift-m
            v=v/2
            if op=='E': out[plus]+=m*v; out[minus]+=m*v
            else:
                s=arb(1) if radial is None else radial
                out[plus]+=s*v; out[minus]-=s*v
                if op=='radial' and q:
                    out[plus-stride]+=q*v; out[minus-stride]-=q*v
    return arb_poly(out)

def inverse(p,n,stride):
    out=p.coeffs(); lam=2*(n-1)
    for k in range(len(out)-1,-1,-1):
        q=k//stride
        if k+stride<len(out):out[k]+=3*(q+1)*out[k+stride]
        out[k]/=lam
    return arb_poly(out)

def norm(p): return sum(map(abs,p.coeffs()),arb(0))

for n in map(int,a.orders.split(',')):
    if time.monotonic()-start>a.seconds:break
    order_start=time.monotonic(); stride=4*n+1
    f=pack('f',n,stride); M=norm(f)
    prev=norm(pack('g',n-1,stride)); cache={}
    def term(i):
        if i not in cache:
            j=n-i
            p=pack('g',i,stride,'radial',arb(2)-arb(2*i)/3)*pack('f',j,stride,'E')-pack('g',i,stride,'E')*pack('f',j,stride,'radial',arb(1)-arb(2*j)/3)
            cache[i]=inverse(p,n,stride)
        return cache[i]
    row=dict(n=n,log10M=text(M.log()/arb(10).log()),log10N_prev=text(prev.log()/arb(10).log()))
    edge=arb_poly()
    for i in sorted({1,2,3,n-3,n-2,n-1}):
        if 1<=i<n:
            x=term(i);edge+=x
            row['log10_term_i%d_over_M'%(i if i<=3 else i-n)]=text((norm(x)/M).log()/arb(10).log())
    feedback=term(n-1); low=term(1)
    row.update(log10_feedback_g_prev_f1=text(norm(feedback).log()/arb(10).log()),log10_term_g1_f_prev=text(norm(low).log()/arb(10).log()),log10_ratio_feedback_over_M=text((norm(feedback)/M).log()/arb(10).log()),log10_edge_sum_over_M=text((norm(edge)/M).log()/arb(10).log()),feedback_over_N_prev=text(norm(feedback)/prev),low_stream_over_M=text(norm(low)/M),middle_over_M=text(norm(f-edge)/M))
    if n>6:
        row['log10_remainder_over_M']=text((norm(f-edge)/M).log()/arb(10).log())
    if n>3:
        row['log10_linear_pair_remainder_over_M']=text((norm(f-low-feedback)/M).log()/arb(10).log())
    if n<=12:
        total=sum((term(i) for i in range(1,n)),arb_poly());residual=total-f
        failures=[k for k,v in enumerate(residual.coeffs()) if not v.contains(0)]
        assert not failures,(n,failures[:10])
        row.update(complete_nonlinear_residual_checks=len(residual),all_residual_coefficients_contain_zero=True,relative_residual=text(norm(residual)/M))
    comparisons=[]
    for key,value in row.items():
        if key.startswith('log10_') or key in ['log10M','log10N_prev']:
            if key in peer[str(n)]:
                diff=abs(arb(value)-arb(peer[str(n)][key]));assert diff<arb('1e-12'),(n,key,text(diff))
                comparisons.append(dict(key=key,absolute_difference=text(diff)))
    row['peer_comparisons']=comparisons;row['actual_elapsed_s']=time.monotonic()-order_start
    record['orders'].append(row);record['actual_elapsed_s']=time.monotonic()-start
    (root/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(row),flush=True)
record['complete_requested_orders']=len(record['orders'])==len(a.orders.split(','));record['actual_elapsed_s']=time.monotonic()-start
(root/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),complete=record['complete_requested_orders'],actual_elapsed_s=record['actual_elapsed_s'])),flush=True)
