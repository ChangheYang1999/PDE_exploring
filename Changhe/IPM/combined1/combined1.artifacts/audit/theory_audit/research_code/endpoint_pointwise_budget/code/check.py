from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib, json, time
from flint import arb, ctx

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((ROOT/'data/manifest.json').read_text())
assert sha(ROOT/'PROOF.md')==m['proof_sha256']
for path,digest in m['files'].items():assert sha(ROOT/path)==digest,path
p=json.loads((ROOT/'data/parameters.json').read_text())
peer=json.loads((ROOT/'source/T2_result.json').read_text())
a=lambda x:arb(Q(x).numerator)/Q(x).denominator
c=Q(p['c']);q=1/c-4;delta=1-1/c;D=1-c*(q-delta)
C,Qa,Da,Dd=map(a,(c,q,delta,D));pi=arb.pi();s=1/c+2

def val(cf,t,der=0):
    return sum((a(v)*n*(n*t).cos() if der else a(v)*(n*t).sin()) for n,v in cf.items())
def parse(x):
    if x.startswith('['):
        mid,rad=x.strip('[]').split('+/-');return arb(mid.strip(),rad.strip())
    return arb(x)
rows=[]
for name,angle in p['angles'].items():
    ep=json.loads((ROOT/'data'/f'{name}_endpoint.json').read_text())
    A={int(k):Q(v) for k,v in ep['F12'].items()}
    P={int(k):Q(v) for k,v in ep['P'].items()}
    th={int(k):Q(v) for k,v in ep['Theta0'].items()}
    nset=set(A)|set(P)
    aa=sum(A.get(n,0)**2 for n in nset);ap=sum(A.get(n,0)*P.get(n,0) for n in nset);pp=sum(P.get(n,0)**2 for n in nset)
    assert pp>0
    proj=aa-ap*ap/pp;assert proj>0
    B=(pi*a(proj)).sqrt()/(4*C)
    t=a(angle);av,ad,pv,pd=val(A,t),val(A,t,1),val(P,t),val(P,t,1)
    normv=Qa*Qa*pv*pv+pd*pd;assert normv>0
    det=Qa*(av*pd-ad*pv)
    Phi=abs(det)/(4*C*normv.sqrt());assert Phi>999745
    tbest=-(Qa*Qa*av*pv+ad*pd)/normv
    reconstructed=((Qa*(av+tbest*pv))**2+(ad+tbest*pd)**2).sqrt()/(4*C)
    assert Phi.overlaps(reconstructed)
    assert Phi.overlaps(parse(peer['D'][name]['Phi_theta_star']))
    g0=sum(n*v for n,v in th.items());assert g0>0
    psi0=sum(n*v/(s*s-n*n) for n,v in th.items())
    v0=abs((s-1)*psi0);assert a(v0)>a('99148/100000')
    # Using the entire interval of Phi is safe for evaluation of a monotone cap:
    # lower endpoints yield upper endpoints of the result, with Arb outward rounding.
    result={'candidate':name,'theta_exact':angle,'H_point':str(Phi),'G_lower_exact':str(g0),'V_lower_exact':str(v0),'B':str(B),'versions':{}}
    for label,v in [('without_velocity_asymptotic',Q(0)),('with_velocity_asymptotic',v0)]:
        ecs={}
        for bl,beta in p['betas'].items():
            ec=(Dd*B/( (2*pi).sqrt()*Phi)*(B/(a(beta)*(-2*Qa-2).sqrt()))**(Da/(-Qa-1))-a(v))/a(g0)
            if bl=='sharpw_rounded_ceiling':assert ec<a('682/1000')
            if bl=='TB_sharp_rounded_ceiling':assert ec<a('648/1000')
            if bl=='original_graded_ceiling':assert ec<a('27/100')
            ecs[bl]=str(ec)
        E=a(p['hypothetical_E']);r0=((2*pi).sqrt()*Phi*(a(v)+E*a(g0))/(Dd*B))**(1/Da)
        cap=B*r0**(Qa+1)/(-2*Qa-2).sqrt()
        assert cap<a('2/100000000')
        if v: assert cap<a('165/10000000000')
        result['versions'][label]={'necessary_Ecrit':ecs,'hypothetical_E':p['hypothetical_E'],'r0':str(r0),'cap':str(cap)}
    rows.append(result)
out={'completed_utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'proof_sha256':sha(ROOT/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(ROOT/'data/manifest.json'),'q':str(q),'delta':str(delta),'D':str(D),'rows':rows,'verdict':'CONFIRMED pointwise estimate and conditional thresholds; folded-kernel E not certified here'}
(ROOT/'verification/result.json').write_text(json.dumps(out,indent=2)+'\n')
for row in rows:print(row['candidate'],row['H_point'],row['versions']['without_velocity_asymptotic']['necessary_Ecrit']['fixed_sharpw_ball'])
print('PASS',out['completed_utc'],out['elapsed_s'])
