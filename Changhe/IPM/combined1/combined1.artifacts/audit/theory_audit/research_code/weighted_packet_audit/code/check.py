"""Independent polar Hessian point certificates for the TP-4 matrix."""
from pathlib import Path
from datetime import datetime,timezone
import importlib.util,hashlib,json,time,sys
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
helper=ROOT.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('packet_polar',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
ctx.prec=1024;start=time.monotonic();src=ROOT/'data/state131.json';data=json.loads(src.read_text())
c,delta,rho,stream=m.fields(data);ar=m.ar;td=m.td;U=P([1,-1]);ca=ar(c)
rho_data=[(j,n,V(U),td(V,(j+1)*delta/2,1)(U)) for (j,n),V in rho.items()]
stream_data=[]
for (j,n),V in stream.items():
    b=(j+1)*delta/2;D=td(V,b,2)
    stream_data.append((j,n,V(U),D(U),td(D,b,1)(U),(n*(D-V))(U),(D-n*n*V)(U)))
maxmode=max(n for j,n in set(rho)|set(stream))
def fields(x,y):
    r2=x*x+y*y;assert r2>0
    rr=ar(r2).sqrt();ct=ar(x)/rr;st=ar(y)/rr;z=1/(1+r2)
    sn=[arb(0),st];cn=[arb(1),ct]
    for n in range(2,maxmode+1):
        sn.append(sn[-1]*ct+cn[-1]*st);cn.append(cn[-1]*ct-sn[-2]*st)
    pw={j:ar(z)**ar((j+1)*delta/2) for j,n in set(rho)|set(stream)}
    dr=arb(0);dt=arb(0);ur=arb(0);ut=arb(0);Hrr=arb(0);Hrt=arb(0);Htt=arb(0)
    for j,n,V,D in rho_data:
        dr+=pw[j]*ar(D(z))*sn[n];dt+=pw[j]*ar(n*V(z))*cn[n]
    for j,n,V,D,DD,RT,TT in stream_data:
        ur-=rr*pw[j]*ar(n*V(z))*cn[n];ut+=rr*pw[j]*ar(D(z))*sn[n]
        Hrr+=pw[j]*ar(DD(z))*sn[n];Hrt+=pw[j]*ar(RT(z))*cn[n];Htt+=pw[j]*ar(TT(z))*sn[n]
    Hxx=ct*ct*Hrr-2*ct*st*Hrt+st*st*Htt
    Hxy=ct*st*(Hrr-Htt)+(ct*ct-st*st)*Hrt
    Hyy=st*st*Hrr+2*ct*st*Hrt+ct*ct*Htt
    return {'rho_x':ct*dr-st*dt,'rho_y':st*dr+ct*dt,'u1':ct*ur-st*ut,'u2':st*ur+ct*ut,
            'u1_x':-Hxy,'u1_y':-Hyy,'u2_x':Hxx,'u2_y':Hxy}
fixtures=[('B4','1','power','0','1','500','500','99116/100000'),
          ('W2_k1','1','power','-1/5','1','707','707','63089/100000'),
          ('B5','2','omega','4/5','1/2','251','251','61151/100000'),
          ('B6','3','omega','4/5','1/2','316','316','-120662/100000'),
          ('unweighted_q2','2','power','0','1','500','500','-82741/100000'),
          ('omega_q2plus','2049/1024','omega','4/5','1/2','251','251','60974/100000'),
          ('omega_q5half','5/2','omega','4/5','1/2','283','283','0'),
          ('R16_p1half','2','power','1/2','16','0','5','0'),
          ('R16_p4fifths','2','power','4/5','16','0','5','0'),
          ('R16_p1','2','power','1','16','0','5','0'),
          ('R16_p3half','2','power','3/2','16','0','4','0'),
          ('R1_p1','2','power','1','1','0','7/10','748/1000')]
rows=[]
for name,sq,kind,sp,sR,sx,sy,bound in fixtures:
    q,p,R,x,y=map(Q,[sq,sp,sR,sx,sy]);f=fields(x,y);r2=x*x+y*y
    vx=ca*ar(r2)+ar(x)*f['u1']+ar(y)*f['u2'];dlog=ar(p)*vx/ar(R*R+r2)
    aa=1+ca+dlog-ar(q)*(ca+f['u1_x'])+f['rho_y']
    bb=1+ca+dlog-ar(q)*(ca+f['u2_y'])
    off=-ar(q)*(f['u1_y']+f['u2_x'])/2-f['rho_x']/2
    eig=(aa+bb-((aa-bb)**2+4*off**2).sqrt())/2
    assert eig<ar(Q(bound)),(name,eig,bound)
    rows.append({'name':name,'q':str(q),'p':str(p),'R':str(R),'point':[str(x),str(y)],
                 'weight':kind,'fields':{k:v.str(85) for k,v in f.items()},'matrix':[aa.str(85),bb.str(85),off.str(85)],
                 'lambda_min':eig.str(100),'strict_upper_cap':bound})
    print(name,eig.str(36),'upper',bound,flush=True)
leading={n:V(Q(1)) for (j,n),V in rho.items() if j==0 and V(Q(1))}
angular=sum((v*v for v in leading.values()),Q(0));assert angular>0
rho_radial2_energy=(1/c)**2*(1/c-1)**2*angular
assert rho_radial2_energy>0 and Q(3,2)>2-1/c
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(src),'helper_sha256':sha(helper),'code_sha256':sha(Path(__file__)),'proof_sha256':sha(ROOT/'PROOF.md'),'precision_bits':ctx.prec,'rows':rows,
     'origin_vertical_caps':{str(q):str(c+1-q) for q in [Q(-1),Q(1),Q(2),Q(3)]},
     'leading_density_angular_energy_over_pi':str(angular),
     'leading_radial_second_derivative_angular_energy_over_pi':str(rho_radial2_energy),
     'finite_weighted_D2rho_necessary_p_at_most':str(2-1/c),'p3half_violates_background_sup_condition':True,
     'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n');print('complete seconds',out['elapsed_seconds'],flush=True)
