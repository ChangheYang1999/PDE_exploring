#!/usr/bin/env python3
"""Independent exact manufactured DR field and coefficient mass tests."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/dynamic_rescaling_discretization/verification'
assert (OUT/'PROOF_WRITTEN_BEFORE_CODE.txt').exists()
TSTART=time.monotonic();COUNT=0

def check(v,label):
    global COUNT
    COUNT+=1
    if not v:raise AssertionError(label)

def cheb(t,n):
    out=[F(1)]
    if n:out.append(t)
    for j in range(2,n+1):out.append(2*t*out[-1]-out[-2])
    return out

def solve(A,b):
    M=[list(row)+[rhs] for row,rhs in zip(A,b)];n=len(M)
    for j in range(n):
        piv=next(i for i in range(j,n) if M[i][j])
        M[j],M[piv]=M[piv],M[j]
        v=M[j][j];M[j]=[t/v for t in M[j]]
        for i in range(n):
            if i!=j:
                v=M[i][j];M[i]=[a-v*c for a,c in zip(M[i],M[j])]
    return [row[-1] for row in M]

witnesses=[]
for C in (F(3,2),F(5,2),F(3),F(4)):
    cw=1/(4*(C-1));cx=C*cw
    for t in (F(1,11),F(1,4),F(2,5),F(3,5),F(4,5),F(9,10)):
        sig=t*t;w=1-sig;r=t/(2*w);s=r*r;omega=-2*sig/(1+sig)
        h=(s+2)/(2*(1+s)**2);hp=-(s+3)/(2*(1+s)**3)
        f=-1/(4*(1+s));fp=1/(4*(1+s)**2);fpp=-1/(2*(1+s)**3)
        for z in (F(1,7),F(1,3),F(1,2),F(4,5),F(1)):
            cosine=(1-z*z)/(1+z*z);sine=2*z/(1+z*z)
            x=r*cosine;y=r*sine
            check(x*x+y*y==s,('geometry',C,t,z))
            rho=y*h;rhox=2*x*y*hp;rhoy=h+2*y*y*hp
            u1=-x*(f+2*y*y*fp);u2=y*(f+2*x*x*fp)
            lap= x*y*(4*s*fpp+12*fp)
            check(-lap==rhox,('Poisson',C,t,z))
            R=(cx*x+u1)*rhox+(cx*y+u2)*rhoy-rho
            physical_derivative=cw*rho-(cx*x+u1)*rhox-(cx*y+u2)*rhoy
            b=h/w;rb_r=(2*s*hp-omega*h)/w
            Ur_over_r=(x*u1+y*u2)/s
            Uth_over_r=(x*u2-y*u1)/s
            E=(cx+Ur_over_r)*rb_r+(cx-1+u2/y+(cx+Ur_over_r)*omega)*b
            check(E==R/(y*w),('residual conversion',C,t,z))
            bprime=-E+(cw-1)*b
            check(y*w*bprime==physical_derivative,('fixed map DR',C,t,z))
            check(Uth_over_r==2*x*y*(f+s*fp)/s,('polar angular velocity',C,t,z))
            check(Ur_over_r==(y*y-x*x)*f/s,('polar radial velocity',C,t,z))
            wrong=-E-(cw-1)*b
            if cw!=1:check(y*w*wrong!=physical_derivative,('wrong sign detected',C,t,z))
            if C==3 and t==F(2,5) and z==F(1,2):
                witnesses.append({'kind':'canonical manufactured field','C':str(C),'x':str(x),'y':str(y),'rho':str(rho),'U1':str(u1),'U2':str(u2),'w':str(w),'E':str(E),'b_tau':str(bprime),'rho_tau':str(physical_derivative),'wrong_sign_rho_tau':str(y*w*wrong)})
    a=F(1);b=e=F(-3,2);c=F(-1,4);d=f=F(1,4)
    adot=(cw-cx-c)*a
    bdot=(cw-3*cx+c)*b-3*a*d
    edot=(cw-3*cx-3*c)*e-a*f
    check(adot==0,('slope gauge',C))
    check(edot==-2*cw*e-f,('cubic e gauge',C))
    check(d+f==-b/3,('center Poisson',C))
    if C==3:
        check(bdot==F(9,8) and edot==F(1,8),'manufactured cubic derivative')
        witnesses.append({'kind':'center derivative at C3','a_tau':str(adot),'b_tau':str(bdot),'e_tau':str(edot),'steady':False})

mass_tests=[]
for N in (3,4,6,8):
    nodes=[-1+F(2*i,N+1) for i in range(N+1)]
    for k in range(min(4,N+1)):
        degree=N-k
        V=[cheb(t,degree) for t in nodes[k:]]
        for seed in (1,2,3):
            coefficients=[F((-1)**j*(k+seed)*(j+2),j+3) for j in range(degree+1)]
            beta_values=[sum(c*tj for c,tj in zip(coefficients,row)) for row in V]
            sigma=[(1+t)/2 for t in nodes[k:]]
            Fvalues=[sk**k*bv for sk,bv in zip(sigma,beta_values)]
            divided=[fv/(sk**k) for sk,fv in zip(sigma,Fvalues)]
            recovered=solve(V,divided)
            check(recovered==coefficients,('coefficient mass recovery',N,k,seed))
            mass=[[sk**k*v for v in row] for sk,row in zip(sigma,V)]
            check(solve(mass,Fvalues)==coefficients,('direct mass system',N,k,seed))
            wrong=solve(V,Fvalues)
            check((wrong==coefficients)==(k==0),('missing sigma detected',N,k,seed))
            if N==4 and k==2 and seed==1:
                mass_tests.append({'N':N,'k':k,'nodes':[str(t) for t in nodes[k:]],'correct_coefficients':[str(v) for v in coefficients],'field_mode_values':[str(v) for v in Fvalues],'recovered_coefficients':[str(v) for v in recovered],'wrong_without_sigma_division':[str(v) for v in wrong]})

result={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-TSTART,'checks':COUNT,'passed':True,'proof_sha256':hashlib.sha256((OUT.parent/'PROOF.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'frozen_producer_sources_used_read_only':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.glob('READ_ONLY_*.py')},'canonical_manufactured_witnesses':witnesses,'mass_matrix_witnesses':mass_tests,'scope':'Exact instantaneous field identities and mass map. No producer code imported, no simulation or stability assertion, no endpoint.'}
(OUT/'EXACT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
