"""Exact finite-regularity controls for the C-infinity cutoff existence proof.

The smooth cutoff existence is proved separately. These polynomial controls
check the moments, signs and reconstructed differential identity exactly.
"""
from pathlib import Path
from datetime import datetime,timezone
from time import monotonic
import json,hashlib
import sympy as s
root=Path('research/122_global_axis_first_order_realization/verification')
t=s.Symbol('t',real=True);u=s.Symbol('u',real=True)

def ser(poly):return [{'power':int(k[0]),'coefficient':str(v)} for k,v in s.Poly(s.expand(poly),t).terms()]
def de(rows):return sum(s.Rational(z['coefficient'])*t**z['power'] for z in rows)

def construct(k,delta):
    density=u**k*(1-u)**k;norm=s.integrate(density,(u,0,1))
    step=1-s.integrate(density,(u,0,t-1))/norm
    bump=(4*(t-1)*(2-t))**k
    m1=s.Rational(1,2)+s.integrate(t*step,(t,1,2))
    n1=s.Rational(1,3)+s.integrate(t*t*step,(t,1,2))
    mur=s.integrate(t*bump,(t,1,2));nur=s.integrate(t*t*bump,(t,1,2));tr=nur/mur;t1=n1/m1
    A=4
    while True:
        mu2=A*A*mur;mu3=16*A*A*mur;t2=A*tr;t3=4*A*tr
        d2=s.cancel(m1*(t3-t1)/(mu2*(t3-t2)))
        d3=s.cancel(m1*(t2-t1)/(mu3*(t3-t2)))
        if 0<d2<=delta and 0<d3<=1:break
        A*=2
    pieces=[(0,1,s.Integer(1)),(1,2,step),(2,A,s.Integer(0)),(A,2*A,-d2*bump.subs(t,t/A)),(2*A,4*A,s.Integer(0)),(4*A,8*A,d3*bump.subs(t,t/(4*A)))]
    data={'regularity':'finite C^(k-1) control; not itself the C-infinity cutoff in the theorem','k':k,'delta':str(delta),'A':A,'T':8*A,
          'd2':str(d2),'d3':str(d3),'moment_parameters':[str(v) for v in [m1,n1,mur,nur]],
          'pieces':[{'left':l,'right':r,'m':ser(m)} for l,r,m in pieces]}
    path=root/('cutoff_k'+str(k)+'_delta'+str(delta).replace('/','_')+'.json');path.write_text(json.dumps(data,indent=2)+'\n')
    return path

def verify(path):
    d=json.loads(path.read_text());k=d['k'];A=d['A'];delta=s.Rational(d['delta']);d2=s.Rational(d['d2']);d3=s.Rational(d['d3'])
    assert 0<d2<=delta and 0<d3<=1
    pieces=[(z['left'],z['right'],de(z['m'])) for z in d['pieces']]
    assert sum(s.integrate(t*m,(t,l,r)) for l,r,m in pieces)==0
    assert sum(s.integrate(t*t*m,(t,l,r)) for l,r,m in pieces)==0
    I1=0;I2=0;Fs=[]
    for l,r,m in pieces:
        p1=s.integrate(t*m,t);p2=s.integrate(t*t*m,t)
        J1=I1+p1-p1.subs(t,l);J2=I2+p2-p2.subs(t,l)
        F=s.expand(6*t*J1-6*J2)
        assert s.expand(s.diff(F,t,2)-6*t*m)==0
        Fs.append(F)
        I1=s.simplify(J1.subs(t,r));I2=s.simplify(J2.subs(t,r))
    assert I1==I2==0
    assert s.expand(Fs[0]-t**3)==0
    assert Fs[-1].subs(t,8*A)==0 and s.diff(Fs[-1],t).subs(t,8*A)==0
    for idx in range(len(pieces)-1):
        point=pieces[idx][1]
        for order in range(k+1):assert s.diff(Fs[idx]-Fs[idx+1],t,order).subs(t,point)==0,(idx,order)
    # The sign bounds are exact from factorization and a positive beta density.
    step=pieces[1][2]
    assert step.subs(t,1)==1 and step.subs(t,2)==0
    density=(t-1)**k*(2-t)**k;norm=s.integrate(u**k*(1-u)**k,(u,0,1))
    assert s.expand(s.diff(step,t)+density/norm)==0
    assert s.expand(pieces[3][2]+d2*(4*(t/A-1)*(2-t/A))**k)==0
    assert s.expand(pieces[5][2]-d3*(4*(t/(4*A)-1)*(2-t/(4*A)))**k)==0
    return {'certificate':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'A':A,'T':8*A,'delta':str(delta),'d2':str(d2),'d3':str(d3),'moments_exact':True,'differential_identity_exact':True,'sign_bounds_exact_by_factorization':True,'continuity_orders_tested':k,'scope':d['regularity']}

if __name__=='__main__':
    start=monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','cases':[]}
    for k,delta in [(6,s.Rational(1,100)),(8,s.Rational(1,1000))]:
        path=construct(k,delta);out['cases'].append(verify(path));print('passed',k,delta,flush=True)
    out.update(status='CONFIRMED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (root/'cutoff_tests.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
