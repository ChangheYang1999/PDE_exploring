"""Exact Hdot^-1 norm, using the finite rational radial Green formula."""
from pathlib import Path
from math import factorial
from datetime import datetime,timezone
from flint import fmpq,fmpq_poly,arb,ctx
import sys,json,time
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import T,U,ZERO,pshift,ar

def negative_norm(D,delta,verbose=True,checkpoint=None,max_seconds=None):
    start=time.monotonic();modes={};bad=[]
    for (ell,kind,n),P in D[0,0].items():
        assert kind=='s' and n>0 and n%2==1
        m=(n-1)//2
        Q=pshift(P,m)(U)
        order=0
        while order<len(Q) and not Q[order]:order+=1
        assert order<len(Q)
        Q=pshift(Q,order);b=ell*delta/2+order
        if b<=fmpq(3,2):bad.append({'ell':ell,'n':n,'b':str(b)})
        modes.setdefault(n,[]).append((b,Q))
    if bad:return {'status':'OPEN','reason':'Sufficient separated-term decay test failed; an infinity verdict needs exact resonance grouping or a separate nonresonance proof.','bad_sectors':bad}
    if checkpoint is not None:
        checkpoint=Path(checkpoint);checkpoint.mkdir(parents=True,exist_ok=True)
    total=fmpq(0);records=[]
    for n,rows in sorted(modes.items()):
        saved=checkpoint/f'mode_{n:03d}.json' if checkpoint else None
        if saved is not None and saved.exists():
            entry=json.loads(saved.read_text());assert entry['n']==n
            value=fmpq(entry['squared_norm_div_pi']);assert value>=0
            total+=value;records.append(entry);continue
        if max_seconds is not None and time.monotonic()-start>max_seconds:
            return {'status':'PARTIAL','completed_modes':len(records),'total_modes':len(modes),
                    'elapsed_seconds':time.monotonic()-start}
        m=(n-1)//2;inner=[(b,U**n*Q) for b,Q in rows]
        outer=[(b,fmpq_poly([coef/(b+m-1+l) for l,coef in enumerate(Q)])) for b,Q in rows]
        groups={}
        for b,A in inner:
            for c,B in outer:groups[b+c]=groups.get(b+c,ZERO)+A*B
        value=fmpq(0)
        for bc,P in groups.items():value+=sum((coef/(bc-3+k) for k,coef in enumerate(P)),fmpq(0))
        value/=4*n
        assert value>=0,(n,value)
        total+=value;entry={'n':n,'squared_norm_div_pi':str(value),'norm':(arb.pi()*ar(value)).sqrt().str(35)}
        records.append(entry)
        if saved is not None:saved.write_text(json.dumps(entry,separators=(',',':'))+'\n')
        if verbose:print('Hminus1 mode',n,'seconds',time.monotonic()-start,flush=True)
    ans=(arb.pi()*ar(total)).sqrt()
    return {'status':'FINITE','norm_lower_ball':ans.str(60),'norm_upper_ball':ans.str(60),
            'norm_lower':str(ans.lower()),'norm_upper':str(ans.upper()),'squared_norm_div_pi':str(total),
            'mode_contributions':records,'elapsed_seconds':time.monotonic()-start}

if __name__=='__main__':
    ctx.prec=256;records=[]
    for n in (1,3,5,11,31,59):
        m=(n-1)//2;b=fmpq(m+3)
        D={(0,0):{(1,'s',n):4*n*(n+1)*T**m}}
        result=negative_norm(D,2*b,False)
        exact=fmpq(2*n*(n+1)*factorial(n)**2,factorial(2*n+1))
        assert fmpq(result['squared_norm_div_pi'])==exact
        records.append({'n':n,'formula':str(exact),'exact_match':True})
    D={(0,0):{(1,'s',1):fmpq_poly([1])}}
    assert fmpq(negative_norm(D,fmpq(6),False)['squared_norm_div_pi'])==fmpq(1,96)
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'manufactured_checks':records,
         'unit_r_over_R3_exact_match_pi_over_96':True}
    (ROOT/'research/exact_negative_norm/verification/manufactured.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out,flush=True)
