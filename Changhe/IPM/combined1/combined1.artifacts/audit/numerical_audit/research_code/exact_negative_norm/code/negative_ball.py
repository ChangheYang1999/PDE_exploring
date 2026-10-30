"""Ball evaluation of the exact finite Green formula, without rational denominator growth."""
from pathlib import Path
from datetime import datetime,timezone
import time,sys,json,hashlib
from flint import ctx,arb,arb_poly,fmpq
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import pshift,U,ar

def negative_ball(D,delta,exact_directory=None):
    start=time.monotonic();modes={};bad=[]
    for (ell,kind,n),P in D[0,0].items():
        assert kind=='s' and n>0 and n%2==1
        m=(n-1)//2;Q=pshift(P,m)(U);order=0
        while order<len(Q) and not Q[order]:order+=1
        assert order<len(Q)
        Q=pshift(Q,order);b=ell*delta/2+order
        if b<=fmpq(3,2):bad.append({'ell':ell,'n':n,'b':str(b)})
        modes.setdefault(n,[]).append((b,Q))
    if bad:return {'status':'OPEN','reason':'Sufficient separated-term decay test failed; an infinity verdict needs exact resonance grouping or a separate nonresonance proof.','bad_sectors':bad}
    print('endpoint and origin checks complete',time.monotonic()-start,flush=True)
    total=arb(0);records=[]
    for n,rows in sorted(modes.items()):
        m=(n-1)//2;Un=arb_poly([ar(q) for q in U**n]);inner=[];outer=[]
        for b,Q in rows:
            Aq=arb_poly([ar(q) for q in Q]);inner.append((b,Un*Aq))
            outer.append((b,arb_poly([ar(coef)/ar(b+m-1+l) for l,coef in enumerate(Q)])))
        groups={}
        for b,A in inner:
            for c,B in outer:groups[b+c]=groups.get(b+c,arb_poly([]))+A*B
        value=arb(0)
        for bc,P in groups.items():value+=sum((coef/ar(bc-3+k) for k,coef in enumerate(P)),arb(0))
        value/=4*n
        assert value>0,(n,value,ctx.prec)
        entry={'n':n,'squared_norm_div_pi':value.str(80),'norm':(arb.pi()*value).sqrt().str(60)}
        if exact_directory:
            path=Path(exact_directory)/f'mode_{n:03d}.json'
            if path.exists():
                exact=json.loads(path.read_text());a=ar(fmpq(exact['squared_norm_div_pi']))
                assert value.overlaps(a),(n,value,a)
                entry['exact_rational_mode_overlap']=True
                entry['exact_mode_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
        total+=value;records.append(entry)
        if n<10 or n%20==1:print('ball H mode',n,'seconds',time.monotonic()-start,flush=True)
    ans=(arb.pi()*total).sqrt()
    return {'status':'FINITE','norm_ball':ans.str(80),'norm_lower_ball':ans.str(80),'norm_upper_ball':ans.str(80),
            'squared_norm_div_pi':total.str(90),'mode_contributions':records,'elapsed_seconds':time.monotonic()-start}

def run(name,bits=2048):
    ctx.prec=bits
    sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
    from pipeline import load,source,digest,DATA
    begin=time.monotonic();path=source(name);raw=json.loads(path.read_text());delta=1-1/fmpq(raw['cl'])
    D=load(name,0);sha=digest(DATA/f'{name}_D0.json.gz')
    print('loaded',time.monotonic()-begin,flush=True)
    out=negative_ball(D,delta,DATA/f'{name}_negative_{sha[:16]}')
    out.update({'candidate':name,'source_sha256':digest(path),'polynomial_sha256':sha,'precision_bits':bits,
                'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'total_elapsed_seconds':time.monotonic()-begin})
    dest=ROOT/f'research/whole_plane_norms/verification/{name}_Hminus1_ball_{bits}.json'
    dest.write_text(json.dumps(out,indent=2)+'\n');print(out['norm_ball'],flush=True)

if __name__=='__main__':run(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 2048)
