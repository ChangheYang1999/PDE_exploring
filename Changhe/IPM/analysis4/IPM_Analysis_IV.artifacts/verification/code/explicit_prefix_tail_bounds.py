"""Evaluate exact geometric tail bounds from complete retained supersolutions."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from certified_prefix_majorant import PrefixMajorant
from resonance_block_majorant import clean
ROOT=Path('research/184_explicit_prefix_tail_bounds')
def A(d,m,Q,K,t):
    a=m+Q*K;u=1-t
    if d==0:return t**K/(a*u)
    if d==1:return t**K/u
    if d==2:return t**K*(a/u+Q*t/u**2)
    if d==3:return t**K*(a*a/u+2*a*Q*t/u**2+Q*Q*t*(1+t)/u**3)
    raise ValueError('Only derivative orders zero through three are evaluated')
def symbolic_check():
    import sympy as s
    t,m,Q,K=s.symbols('t m Q K',positive=True)
    expr=t**K/(1-t);checks=0
    for d in range(1,4):
        assert s.simplify(expr-A(d,m,Q,K,t))==0;checks+=1
        expr=m*expr+Q*t*s.diff(expr,t)
    return checks

def one(path,data):
    prefix_source=None
    if 'initial_density' not in data:
        for name,expected in data.get('inputs',{}).items():
            candidate=Path(name)
            if candidate.suffix!='.json':continue
            raw=candidate.read_bytes();assert sha256(raw).hexdigest()==expected
            source=json.loads(raw)
            if 'initial_density' in source:
                data={**data,'initial_density':source['initial_density'],'initial_harmonics':source['initial_harmonics']}
                prefix_source=dict(path=name,sha256=expected);break
        assert prefix_source is not None,'No hash-matched prefix input'
    model=PrefixMajorant(data['h'],data['Q'],data['B'],list(map(F,data['initial_density'])),list(map(F,data['initial_harmonics'])),F(data['s']),F(data['L']),F(data['kappa']))
    boxdata=data.get('adaptive',data);q=boxdata['q'];box=list(map(F,boxdata['box']));w0=F(1,2**q)
    assert model.Y0==list(map(F,boxdata['Y0'] if 'Y0' in boxdata else data['Y0']))
    image=model.transformed(w0,box);assert image==list(map(F,boxdata['image']))
    assert all(0<=v<=b and 0<=y<=b for v,y,b in zip(image,model.Y0,box))
    Q=data['Q'];h=data['h'];B=data['B'];N=len(data['initial_density']);L=F(data['L']);delta=F(2*h,Q)
    ell=(q+Q-1)//Q+1;z=F(1,2**ell);t=z**Q/w0;assert 0<t<1
    rows=[]
    for J in [N,N+Q,N+2*Q]:
        row=dict(J=J,bounds=[])
        for d in range(4):
            density=F(0)
            for r in range(1,Q+1):
                m=N+r;K=max(0,(J+1-m+Q-1)//Q);density+=box[Q+r-1]*z**m*A(d,m,Q,K,t)
            K=max(0,(J+1-N+Q-1)//Q);harmonic=box[Q-1]*z**N*A(d,N,Q,K,t)
            derivative=[]
            for a in range(d+1):
                b=d-a;derivative.append(dict(radial_Euler_order=a,angular_order=b,density_weighted_bound=max(delta,1-delta)**a*B**b*density,stream_weighted_bound=(2-delta)**a*B**b*(L*density+harmonic)))
            row['bounds'].append(dict(total_derivative_order=d,D=density,E=harmonic,derivatives=derivative))
        rows.append(row)
    return dict(path=str(path),sha256=sha256(path.read_bytes()).hexdigest(),prefix_source=prefix_source,q=q,N=N,Q=Q,h=h,z=z,t=t,radius_dyadic_exponent=F(ell*Q,2*h),rows=rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--topics',default='176,178,179,181,182');args=ap.parse_args();start=time.monotonic();identity_checks=symbolic_check();selected={}
    for topic in args.topics.split(','):
        for root in Path('research').glob(topic+'_*/verification'):
            for path in root.glob('*_N*.json'):
                data=json.loads(path.read_text())
                if 'initial_density' not in data or 'adaptive' not in data:continue
                key=topic+':'+path.name.split('_N')[0];rank=(data['adaptive']['q'],-len(data['initial_density']))
                if key not in selected or rank<selected[key][0]:selected[key]=(rank,path,data)
    extra=Path('research/174_adaptive_majorant_boxes/verification/prefix_N90_sharp.json')
    if extra.exists():selected['174:two_mode5']=(None,extra,json.loads(extra.read_text()))
    rows=[one(p,data) for rank,p,data in selected.values()]
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_checks_pass=True,symbolic_identity_checks=identity_checks,profiles=len(rows),rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Exact bounds conditional on the tail theorem184; independent proof review pending.')
    raw=(json.dumps(clean(result),indent=2)+'\n').encode();archive=gzip.compress(raw,compresslevel=6,mtime=0)
    (ROOT/'verification/checks.json.gz').write_bytes(archive)
    (ROOT/'verification/summary.json').write_text(json.dumps(dict(checked_at_utc=result['checked_at_utc'],all_exact_checks_pass=True,profiles=len(rows),raw_sha256=sha256(raw).hexdigest(),raw_bytes=len(raw),archive_sha256=sha256(archive).hexdigest(),archive_bytes=len(archive),actual_elapsed_s=result['actual_elapsed_s']),indent=2)+'\n')
    for name in ['explicit_prefix_tail_bounds.py','certified_prefix_majorant.py','resonance_block_majorant.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(dict(profiles=len(rows),symbolic_identity_checks=identity_checks,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
