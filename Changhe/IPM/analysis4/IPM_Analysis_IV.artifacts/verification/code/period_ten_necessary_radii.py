"""Directed necessary radii and exact highest-sector check for period ten."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from pure_cartesian_ball import refine_root,ball
from certified_initial_majorants import pack
ROOT=Path('research/288_period_ten_necessary_radii')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def fresh(q):return arb(q.numerator)/q.denominator
def ref(p,r=None):
    if r is None:r=p.read_bytes()
    return dict(path=str(p),sha256=sha256(r).hexdigest(),bytes=len(r))
def main():
    start=time.monotonic();src=Path('research/281_period_ten_finite_algebra/verification/obstruction_checks.json');raw=src.read_bytes();data=json.loads(raw);assert data['all_checks_pass']
    entry=data['prefix_polynomials'];packed=Path(entry['path']).read_bytes();assert sha256(packed).hexdigest()==entry['sha256'];decoded=gzip.decompress(packed);assert sha256(decoded).hexdigest()==entry['raw_sha256'];exact=json.loads(decoded)
    delta=F(1,5);d=F(1,4);eta=4-delta;a=2/eta;beta=6/eta;assert (a,beta,1-1/beta)==(F(10,19),F(30,19),F(11,30))
    hs=[F(0),F(1)];tops=[]
    for n in range(1,21):
        if n>1:hs.append(sum((8*(n-j)/(eta*j+2)-1)*hs[j]*hs[n-j] for j in range(1,n))/(4*d*(n-1)))
        coeff=list(map(F,exact['fields']['f'][str(n)]['sine_polynomials'][str(4*n-1)]));assert coeff==[F(0)]*n+[(-1)**(n-1)*hs[n]] and hs[n]>0
        tops.append(dict(n=n,frequency=4*n-1,coefficient=str(hs[n])))
    values=[]
    for bits in [512,1024]:
        ctx.prec=bits;ball.cache_clear();aa=fresh(a);bb=fresh(beta);RH=4*fresh(d)*((aa*aa.gamma()*bb.gamma()/(aa+bb).gamma()).log()/aa).exp();roots=[]
        for row in data['real_roots']:
            b,I=refine_root(list(map(int,data['primitive_coefficients'])),row['interval'],bits+64);assert not b.contains(0)
            radius=((abs(b)/RH).log()/fresh(delta)).exp();roots.append((b,I,radius))
        values.append((RH,roots))
    assert values[0][0].overlaps(values[1][0]);RH=values[-1][0];assert abs(RH-arb('0.584583758269'))<arb('5e-13')
    quoted=['3.233134','.0001669378','2.744523e-8','3.332518e-12','3.377585e-8','6.475182e-7','3.917716e-6','1.372728e-5','4.005399e-5','.0001084217','.0002990101','.0009698174','.005090875','.1529914'];rows=[]
    for i,(old,new,q) in enumerate(zip(values[0][1],values[1][1],quoted),1):
        b,I,radius=new;assert old[0].overlaps(b) and old[2].overlaps(radius);assert arb(q)<radius and (radius-arb(q))/radius<arb('1e-6')
        den=10**35;lo=int((radius.lower()*den).floor().unique_fmpz());hi=int((radius.upper()*den).ceil().unique_fmpz());assert fresh(F(lo,den))<radius<fresh(F(hi,den))
        rows.append(dict(root_index=i,root_interval=I,root=b.str(55,radius=True),necessary_radius=radius.str(65,radius=True),radius_ball=pack(radius),radius_bounds_exact=[str(F(lo,den)),str(F(hi,den))],quoted_lower=q))
    nmax=1500;hv=[arb(0),arb(1)];inv=[arb(0)]+[8/(fresh(eta)*j+2) for j in range(1,nmax+1)];diagnostics=[];quoted_scalars={100:'0.295682',400:'0.29309',800:'0.292492',1500:'0.29215'}
    for n in range(2,nmax+1):
        v=arb(0)
        for j in range(1,(n+1)//2):
            k=n-j;v+=(inv[j]*k+inv[k]*j-2)*hv[j]*hv[k]
        if n%2==0:
            j=n//2;v+=(inv[j]*j-1)*hv[j]*hv[j]
        hv.append(v/(4*fresh(d)*(n-1)))
        if n in quoted_scalars:
            x=hv[n]*RH**n*((1+1/fresh(beta))*arb(n).log()).exp();assert abs(x-arb(quoted_scalars[n]))<arb('5e-'+str(len(quoted_scalars[n].split('.')[1])+1))
            diagnostics.append(dict(n=n,scaled=x.str(55,radius=True),quoted=quoted_scalars[n]))
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,arithmetic_bits=[512,1024],a=str(a),beta=str(beta),four_d=str(4*d),boundary_power=str(1-1/beta),R_H=RH.str(65,radius=True),R_H_ball=pack(RH),rows=rows,exact_top_checks=tops,source=ref(src,raw),prefix_source=entry,scalar_diagnostics=diagnostics,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['period_ten_necessary_radii.py','pure_cartesian_ball.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    for name in ['rh_top_Q10.py','rh_top_Q10.out']:(ROOT/'sources'/('lead_'+name)).write_bytes(Path('../a4-lead/code/tuned',name).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k not in ['R_H_ball','rows','exact_top_checks']}),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as e:
        r=dict(at=stamp(),error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(v.filename).name,line=v.lineno) for v in traceback.extract_tb(e.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(r)+'\n');print(json.dumps(r),flush=True);raise SystemExit(1)
