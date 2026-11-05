"""Exact Cartesian-polynomial check of the positive modal energy identities."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json

def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():out[k]=out.get(k,Q(0))+v
    return {k:v for k,v in out.items()if v}
def scale(p,a,dx=0,dy=0):return {(i+dx,j+dy):a*v for(i,j),v in p.items()}
def derivative(p,d):
    out={}
    for(i,j),v in p.items():
        n=(i,j)[d]
        if n:out[i-(d==0),j-(d==1)]=n*v
    return out
def mul(p,q):
    out={}
    for(i,j),v in p.items():
        for(k,l),w in q.items():out[i+k,j+l]=out.get((i+k,j+l),Q(0))+v*w
    return out
def J2(p):return add(p,scale(derivative(derivative(p,0),0),-1),scale(derivative(derivative(p,1),1),-1))
def angular_over_pi(p,r):
    out=Q(0)
    for(i,j),v in p.items():
        if i%2 or j%2:continue
        a,b=i//2,j//2
        coefficient=Q(2*factorial(2*a)*factorial(2*b),4**(a+b)*factorial(a)*factorial(b)*factorial(a+b))
        out+=coefficient*v*r**(i+j)
    return out

def exact_modal_density(modes,r):
    e2=e3=Q(0)
    for n,terms in modes.items():
        fs=[]
        for d in range(4):
            fs.append(sum((a*Q(factorial(p),factorial(p-d))*r**(p-d)for p,a in terms.items()if p>=d),Q(0)))
        f,f1,f2,f3=fs
        g=f-f2-f1/r+n*n*f/r**2
        g1=f1-f3-f2/r+(1+n*n)*f1/r**2-2*n*n*f/r**3
        s2=g*g;s3=s2+g1*g1+n*n*g*g/r**2
        for s in[-1,1]:
            a=r*g-2*f1+s*2*n*f/r
            a1=g+r*g1-2*f2+s*2*n*(f1/r-f/r**2)
            s2+=2*a*a;s3+=2*(a*a+a1*a1+(n+s)**2*a*a/r**2)
        e2+=s2;e3+=s3
    return e2,e3

# F = (1+r²+r⁴)y + (1+2r²)(3x²y−y³) + (5x⁴y−10x²y³+y⁵).
s={ (2,0):Q(1),(0,2):Q(1)}
y={(0,1):Q(1)}
mode3={(2,1):Q(3),(0,3):Q(-1)}
mode5={(4,1):Q(5),(2,3):Q(-10),(0,5):Q(1)}
F=add(y,mul(s,y),mul(mul(s,s),y),mode3,scale(mul(s,mode3),2),mode5)
V=[F,scale(F,2,1,0),scale(F,2,0,1)]
G=list(map(J2,V))
P2=add(*(mul(g,g)for g in G))
P3=add(P2,*(mul(derivative(g,d),derivative(g,d))for g in G for d in[0,1]))
modes={1:{1:Q(1),3:Q(1),5:Q(1)},3:{3:Q(1),5:Q(2)},5:{5:Q(1)}}
rows=[]
for r in map(Q,['1/10','1','3/2','10']):
    c2,c3=angular_over_pi(P2,r),angular_over_pi(P3,r)
    m2,m3=exact_modal_density(modes,r)
    assert(c2,c3)==(m2,m3)
    rows.append({'r_exact':str(r),'E2_angular_integral_div_pi_exact':str(c2),'E3_angular_integral_div_pi_exact':str(c3),'exact_match':True})
output={'status':'PASS_EXACT_CARTESIAN_MODAL_IDENTITY_CHECK','method':'Independent rational Cartesian polynomial differentiation and exact monomial angular integration; multiple overlapping modes1,3,5.','rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
