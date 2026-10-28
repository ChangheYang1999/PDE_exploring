"""Reconstruct source polynomials and audit stronger derivative weights.
Uses the already certified exact partition but recomputes every enclosure.
No sampling or sibling evaluator supplies an inequality.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime, timezone
import json,hashlib,time
from flint import arb,ctx
import extra_coefficients as ec
import sharp_coefficients as sc
HERE=Path(__file__).resolve().parent
ctx.prec=384; start=time.monotonic()
pfile=HERE/'extra_coefficient_polynomials.json'; cfile=HERE/'extra_coefficient_certificate.json'; afile=HERE/'extra_coefficient_audit.json'
a=json.loads(afile.read_text()); raw=json.loads(pfile.read_text()); cert=json.loads(cfile.read_text())
assert a['verdict']=='CONFIRMED' and cert['status']=='COMPLETE'
assert hashlib.sha256(pfile.read_bytes()).hexdigest()==a['polynomial_sha256']
assert hashlib.sha256(cfile.read_bytes()).hexdigest()==a['certificate_sha256']
s,delta,P,kinds=ec.construct()
saved={(k.rsplit('_',1)[0],int(k.rsplit('_',1)[1])):{(i,j):Q(v) for i,j,v in vals} for k,vals in raw['polynomials'].items()}
assert P==saved and kinds==raw['kinds'] and delta==Q(raw['delta'])
assert s['canonical_serialization_sha256']==a['source_sha256']==cert['source_sha256']==raw['source_sha256']
B=sc.make_blocks(P,cert['nt'],cert['nz']); Lt,Rt=sc.cc.split_matrices(cert['nt']); Lz,Rz=sc.cc.split_matrices(cert['nz'])
paths={x['path']:x for x in cert['accepted']};assert len(paths)==len(cert['accepted'])
assert not cert['failed'] and not cert['pending']
maxima={'r2_rho4':arb(0),'r1_u3':arb(0)};leaves=[]
def bounds(b,tl,th,zl,zh):
    wl=(1-sc.A(th))**(sc.A(delta)/2);wu=(1-sc.A(tl))**(sc.A(delta)/2);W=sc.cc.wcoeff(wl,wu);ab={}
    for label,kind in kinds.items():
        lo,hi=sc.cc.hull((W*sc.arb_mat([b[label,j].entries() for j in range(4)])).entries());v=abs(lo).max(abs(hi))
        if kind=='sin':v*=sc.A((1-zl)/2).sqrt()
        elif kind=='cos':v*=sc.A((1+zh)/2).sqrt()
        elif kind=='sin2':v*=arb(1) if zl<=0<=zh else sc.A(1-min(abs(zl),abs(zh))**2).sqrt()
        ab[label]=v
    u3=sum((comb(3,i)*ab[f'u3_{u}_{i}']**2 for u in range(2) for i in range(4)),arb(0)).sqrt()
    r4=sum((comb(4,i)*ab[f'r4_{i}']**2 for i in range(5)),arb(0)).sqrt()
    return {'r2_rho4':sc.A(th).sqrt()*sc.A(1-tl).sqrt()*r4,'r1_u3':sc.A(1-tl).sqrt()*u3}
def visit(path,b,tl,th,zl,zh):
    if path in paths:
        row=paths[path]; assert list(map(Q,row['t']))==[tl,th] and list(map(Q,row['z']))==[zl,zh]
        assert not any(p!=path and p.startswith(path) for p in paths)
        vals=bounds(b,tl,th,zl,zh)
        assert all(v.is_finite() for v in vals.values())
        for k,v in vals.items():maxima[k]=maxima[k].max(v)
        leaves.append({'path':path,'upper':{k:v.str(60) for k,v in vals.items()}})
        if len(leaves)%100==0:print('leaves',len(leaves),'seconds',time.monotonic()-start,flush=True)
        return
    kids={p[len(path)] for p in paths if p.startswith(path)};assert kids in ({'t','T'},{'z','Z'})
    axis='t' if kids=={'t','T'} else 'z';left,right=sc.cc.split(b,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
    if axis=='t':
        m=(tl+th)/2;visit(path+'t',left,tl,m,zl,zh);visit(path+'T',right,m,th,zl,zh)
    else:
        m=(zl+zh)/2;visit(path+'z',left,tl,th,zl,m);visit(path+'Z',right,tl,th,m,zh)
print('source reconstruction PASS',time.monotonic()-start,flush=True)
visit('',B,Q(0),Q(1),Q(-1),Q(1));assert len(leaves)==len(paths)
target={}
for k,v in maxima.items():
    m=1
    while not v<m:m*=2
    target[k]=m
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'PENDING_PROOF_AUDIT','precision_bits':ctx.prec,'source_sha256':s['canonical_serialization_sha256'],'input_hashes':{x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in (pfile,cfile,afile)},'maxima':{k:v.str(70) for k,v in maxima.items()},'safe_power_two_bounds':target,'leaves':leaves,'elapsed_seconds':time.monotonic()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('bounds',target,{k:v.str(20) for k,v in maxima.items()},'seconds',out['elapsed_seconds'],flush=True)
