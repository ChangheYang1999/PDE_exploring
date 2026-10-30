from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time
from flint import arb,ctx,fmpq as Q
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE.parent/'weak_probe_audit/code'))
from reproduce import fields,ar
sys.set_int_max_str_digits(0)
start=time.monotonic();ctx.prec=1024
canpath=BASE.parent/'projected_laplacian/data/candidate007_canonical.json'
can=json.loads(canpath.read_text())
assert all(k>=m for (j,m,k),x in zip(can['order'],can['coefficients']) if Q(x))
c,delta,rho,stream=fields(can)
a0=sum((p[0] for (j,n),p in rho.items() if n==1),Q(0))
strain=2*sum((p[0] for (j,n),p in stream.items() if n==2),Q(0))
assert all(not p[0] for (j,n),p in rho.items() if n!=1)
assert all(not p[0] for (j,n),p in stream.items() if n!=2)
assert a0==Q(can['a0']) and strain==Q(can['strain']) and c+strain==1
assert 1<c<2 and a0>=5*c-4
paths=[BASE.parent/f'projected_laplacian/verification/candidate007_mode{n}.json' for n in (1,3)]
mode={}
for n,p in zip((1,3),paths):
 data=json.loads(p.read_text());assert data['angular_modes']==[n]
 mode[n]={Q(r['a']):arb(r['projected_norm']) for r in data['rows']}
d=ar(c-1);ss=(2*d-3+((2*d-3)**2+16*d).sqrt())/8
H=(d-ss)*(4*arb.pi()*ss*(1+ss)).sqrt();Hup=Q(57,50)
assert H<ar(Hup)
A=1+1/c;edges=[Q(k,4) for k in range(7)]+[A]
assert Q(3,2)<A<Q(7,4)
rows=[]
for i,(l,h) in enumerate(zip(edges,edges[1:])):
 e=h if i<6 else Q(7,4)
 n=(mode[1][e]**2+mode[3][e]**2).sqrt()
 lower=arb(5)**ar((l-2)/2)*n
 upper=ar(Hup*(1+c-c*l)/(1+l))
 margin=lower-upper;assert margin>0
 rows.append({'left':str(l),'right':str(h),'evaluation':str(e),'N13':n.str(85),'lower':lower.str(85),'upper':upper.str(85),'margin':margin.str(85),'ratio':(lower/upper).str(85),'pass':True})
inputs=paths+[canpath,BASE/'PROOF.md',BASE/'APPLICATION_007.md',Path(__file__),BASE.parent/'weak_probe_audit/code/reproduce.py']
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'C1-N1-007-d2w-j7-e2bal','status':'OPEN pending independent analytic and arithmetic review','precision_bits':ctx.prec,'inputs':{str(p.relative_to(BASE.parent)):sha256(p.read_bytes()).hexdigest() for p in inputs},'c':str(c),'a0':ar(a0).str(85),'strain':str(strain),'a0_minus_5c_minus4':ar(a0-(5*c-4)).str(85),'all_origin_checks_pass':True,'s_star':ss.str(85),'H':H.str(85),'H_upper':str(Hup),'A':str(A),'rows':rows,'all_pass':True,'elapsed_seconds':time.monotonic()-start}
target=BASE/'verification/candidate007_origin_cover.json';assert not target.exists();target.write_text(json.dumps(out,indent=2)+'\n')
print('a0',out['a0'],'H',out['H'])
for r in rows:print(r['left'],r['right'],'ratio',r['ratio'])
print('elapsed',out['elapsed_seconds'])
