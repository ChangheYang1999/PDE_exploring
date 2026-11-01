"""Complete discrete response certificate for sin9 at delta4/7."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import ctx
from extremal_single_probe import ExtremalResponse
from discrete_response_cover import cover
from taylor_response_enclosure import enclose
from certified_initial_majorants import pack,endpoints,round_up
from certified_prefix_majorant import PrefixMajorant,certificate
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT=Path('research/233_single_nine_four_sevenths')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def put(path,obj):
    raw=json.dumps(clean(obj),separators=(',',':')).encode();saved=gzip.compress(raw,compresslevel=6,mtime=0) if path.suffix=='.gz' else raw
    path.write_bytes(saved);return dict(path=str(path),sha256=sha256(saved).hexdigest(),raw_sha256=sha256(raw).hexdigest())
def low(v):
    m,e,r,re=v;return abs(F(m)*F(2)**e)-F(r)*F(2)**re

def main():
    from discrete_cover_checks import check
    check()
    started=time.monotonic();ctx.prec=768;src=Path('research/231_extremal_single_harmonics/verification/h2_Q7_probe.json');probe=json.loads(src.read_text())
    assert probe['all_checks_pass'] and probe['all_separated'] and (probe['h'],probe['Q'],probe['mode'],probe['K'])==(2,7,9,18)
    least=min([low(v['enclosure']) for v in probe['rows']]+[low(probe['limit'])]);assert least>0
    s=F(1)
    while s>=least/4:s/=2
    response=ExtremalResponse(2,7)
    cov=cover(response,18,s,progress=lambda d:put(ROOT/'verification/cover_partial.json.gz',d),interval_encloser=lambda a,b:enclose(response,a,b,degree=2),enclosure_metadata=dict(method='taylor',degree=2),point_split_width=8);s=F(cov['s']);cv=put(ROOT/'verification/cover.json.gz',cov)
    initial=[];density=[]
    for n in range(1,8):
        norm=response.f[n].norm();d=round_up(n*endpoints(norm)[1]);assert d>n*endpoints(norm)[1];density.append(d);initial.append(dict(n=n,enclosure=pack(norm),bound=d))
    delta=F(4,7);L=F(147,80);kap=10*(2-delta+max(delta,1-delta))*(1-delta)/delta*F(8,7)
    m=PrefixMajorant(2,7,10,density,[],s,L,kap);base=certificate(m,2);best=None
    for q in range(base['w_dyadic_exponent'],max(0,base['w_dyadic_exponent']-100),-1):
        found,record=try_box(m,q)
        if found is None:break
        best=dict(q=q,box=found['box'],image=found['image'],iterations=record['iterations'])
    assert best is not None
    bx=put(ROOT/'verification/box.json.gz',dict(h=2,Q=7,B=10,N=7,s=s,L=L,kappa=kap,input_enclosures=initial,initial_density=density,initial_harmonics=[],constant=m.constant,J=m.J,Y0=m.Y0,baseline=base,adaptive=best))
    out=dict(checked_at_utc=stamp(),all_checks_pass=True,h=2,Q=7,B=10,mode=9,N=7,K=18,s=s,q=best['q'],radius_exponent=F(best['q'],4),amplitude_exponent=F(7,4),arithmetic_bits=768,coverage=cv,box=bx,
      counts={status:sum(n['status']==status for n in cov['nodes']) for status in ['empty','singleton','interval']},probe=dict(path=str(src),sha256=sha256(src.read_bytes()).hexdigest()),actual_elapsed_s=time.monotonic()-started)
    put(ROOT/'verification/checks.json',out)
    for name in ['single_nine_certificate.py','discrete_response_cover.py','extremal_single_probe.py','compact_response_bounds.py','pure_cartesian_ball.py','certified_prefix_majorant.py','adaptive_majorant_boxes.py','taylor_response_enclosure.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    p=ROOT/'verification/cover_partial.json.gz'
    if p.exists():p.unlink()
    print(json.dumps(clean(out)),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        put(ROOT/'verification/FAILURE.json',failure);print(json.dumps(failure),flush=True);raise SystemExit(1)
