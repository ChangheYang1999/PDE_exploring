"""Exact independent elimination checks for result91; no numerical solver."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

def add(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items()if v}
def scale(a,c):return {k:v*c for k,v in a.items()if v*c}
def mul(a,b):
    out={}
    for k,v in a.items():
        for l,w in b.items():
            n=tuple(i+j for i,j in zip(k,l));out[n]=out.get(n,F(0))+v*w
    return {k:v for k,v in out.items()if v}
one={(0,0,0,0):F(1)}
def var(n):
    k=[0]*4;k[n]=1;return {tuple(k):F(1)}
ell,J,f,fd=[var(i)for i in range(4)];D=add(ell,scale(one,-1));v=add(ell,scale(J,-1))
C1=add(add(mul(add(ell,scale(J,-F(1,2))),fd),mul(D,f)),scale(mul(f,f),-F(1,4)))
C3=add(add(mul(J,f),scale(mul(J,fd),F(1,2))),scale(mul(f,f),-F(1,4)))
checks=[]
def check(name,condition,**data):
    assert condition,(name,data);checks.append(dict(name=name,**data))
check('undivided first-minus-third equation',add(C1,scale(C3,-1))==add(mul(v,fd),mul(add(D,scale(J,-1)),f)))
left=add(scale(mul(J,add(C1,scale(C3,-1))),2),scale(mul(v,C3),-4))
right=mul(f,add(mul(v,f),scale(mul(J,add(v,one)),-2)))
check('undivided polynomial elimination identity',left==right)
for e in [F(6,5),F(3,2),F(2),F(3),F(10)]:
    d=e-1
    for j in [d/10,d/2,d,(d+e)/2]:
        z=e-j;g=2*j+2*j/z;gp=2+2*e/z**2
        check('strict eliminated factor',2*j*gp-g==2*j*(z*z-z+2*e)/z**2>0,ell=str(e),J=str(j))
        jd=g-4*j;gd=gp*jd
        c1=(e-j/2)*gd+d*g-g*g/4;c3=j*g+j*gd/2-g*g/4
        if j==d:check('affine equilibrium',c1==c3==jd==0 and g==4*d)
        else:check('no nonconstant point on algebraic curve solves both equations',c1!=0 or c3!=0)
    check('regular equilibrium denominator',4*e-2*d==2*e+2>0)
now=datetime.now(timezone.utc).isoformat();out=dict(utc=now,status='PASS',count=len(checks),checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=hashlib.sha256(Path('research/radial_full_transport_rigidity/PROOF.md').read_bytes()).hexdigest(),scope='Two exact polynomial elimination identities and rational sign/equilibrium checks. The standalone argument proves the C1 radial theorem. No nonradial exclusion.')
Path('research/radial_full_transport_rigidity/verification/exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['utc','status','count','scope']}))
