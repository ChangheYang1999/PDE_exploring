"""Outward scalar cover conditional on the proposed actual origin inverse floor."""
from datetime import datetime,timezone
from pathlib import Path
from hashlib import sha256
import json,time,sys
from flint import arb,ctx,fmpq as Q,fmpq_poly as P
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3]; B=R/'research/origin_dyadic_ceiling'
def H(p):return sha256(p.read_bytes()).hexdigest()
def ar(x):return arb(x.numerator)/arb(x.denominator)
start=time.monotonic();ctx.prec=1024
name='C1-N1-007-d2w-j7-e2bal'
src=R/f'research/candidate_audits/data/{name}/canonical.json'
assert H(src)=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
state=json.loads(src.read_text());c=Q(state['cl']);d=c-1;A=1+1/c
assert 1<c<2
a0=Q(0);strain=Q(0)
for (j,m,k),coef in zip(state['order'],state['coefficients']):
 if k>2 or m>2:continue
 p=(3+1/c-j*(1-1/c))/2;rad=Q(1)
 for z in range(2-k):rad*= (p-k-z)/(z+1)
 bcoef,ccoef=[(2,1),(0,-1),(-6,1)][m]
 a0-=(4*bcoef+24*ccoef)*rad*Q(coef)
 strain+=4*bcoef*rad*Q(coef)
assert a0==Q(state['a0']) and strain==1-c and a0>=5*c-4
S=P([0,1]);f=(d-S)**2*S*(1+S)
assert f.derivative()==(d-S)*(d+(2*d-3)*S-4*S*S)
sstar=(ar(2*d-3)+(ar((2*d-3)**2+16*d)).sqrt())/8
assert sstar>0 and sstar<ar(d)
Hmax=(ar(d)-sstar)*(4*arb.pi()*sstar*(1+sstar)).sqrt()
anchor=R/'research/projected_laplacian_audit/verification/candidate007_modes13.json'
old=json.loads(anchor.read_text());assert old['source_sha256']==H(src)
vals={(row['mode'],Q(row['a'])):arb(row['norm']) for row in old['rows']}
points=[Q(k,4) for k in range(7)]+[A]
cells=[]
for l,h in zip(points[:-1],points[1:]):
 e=Q(7,4) if h==A else h
 J=(vals[1,e]**2+vals[3,e]**2).sqrt()
 low=arb(5)**ar((l-2)/2)*J
 high=Hmax*ar((1+c-c*l)/(1+l))
 gap=low-high;ratio=low/high
 assert gap>0 and ratio>1
 cells.append({'left':str(l),'right':str(h),'norm_evaluation_at':str(e),'lower':low.str(100),
               'upper':high.str(100),'gap':gap.str(100),'ratio':ratio.str(100)})
inputs=[src,anchor,Path(__file__),B/'PROOF.md',B/'source/T4_origin_dyadic_inverse_PROOF.md',B/'source/T4_origin_spectral_line_PROOF.md']
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'precision_bits':ctx.prec,
     'c':str(c),'a0':str(a0),'a0_margin':str(a0-(5*c-4)),'strain':str(strain),
     'maximizer':sstar.str(100),'Hmax':Hmax.str(100),'derivative_identity_exact':True,'cells':cells,
     'inputs':{str(p.relative_to(R)):H(p) for p in inputs},'elapsed_seconds':time.monotonic()-start,
     'status':'All seven scalar cells pass. N4-origin OPEN peer. Scheme exclusion conditional on independently reviewed actual origin inverse theorem.'}
p=B/'verification/candidate007_modes13.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('Hmax',Hmax.str(30),'sstar',sstar.str(30),flush=True)
for row in cells:print(row['left'],row['right'],row['ratio'],flush=True)
print(out['status'],out['elapsed_seconds'],flush=True)
