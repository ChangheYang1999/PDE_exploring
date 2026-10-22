"""Independent Fourier algebra, beta integrals, rational pi and integer roots.
Does not import Arb, mpmath, the first checker, or numerical-lane code.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt,factorial
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_strain'
def check(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
Z=(Q(0),Q(0))
def ca(a,b):return a[0]+b[0],a[1]+b[1]
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def mul(a,b):
 d={}
 for n,x in a.items():
  for m,y in b.items():d[n+m]=ca(d.get(n+m,Z),cm(x,y))
 return {n:z for n,z in d.items() if z!=Z}
def sn(m):return {m:(Q(0),-Q(1,2)),-m:(Q(0),Q(1,2))}
def cs(m):return {m:(Q(1,2),Q(0)),-m:(Q(1,2),Q(0))}
def integ(a):
 z=a.get(0,Z);check(z[1]==0,'real mean');return 2*z[0]
def beta(p,q):
 v=Q(1,q+1)
 for j in range(1,p+1):v*=Q(j,j+q+1)
 check(v==Q(factorial(p)*factorial(q),factorial(p+q+1)),'beta formula agreement');return v
p=mul(mul(cs(1),cs(1)),sn(1));phip={n:cm((0,Q(n)),z) for n,z in p.items()}
angles={'sin3_squared':integ(mul(sn(3),sn(3))),'p_times_sin3':integ(mul(p,sn(3))),'p_squared':integ(mul(p,p)),'p_theta_squared':integ(mul(phip,phip)),'cos3_squared':integ(mul(cs(3),cs(3)))}
check(angles=={'sin3_squared':1,'p_times_sin3':Q(1,4),'p_squared':Q(1,8),'p_theta_squared':Q(5,8),'cos3_squared':1},'Fourier angular coefficients')
modal={}
for m in [1,3]:
 hp=integ(mul(mul(cs(1),sn(m)),sn(2)));hv=-m*integ(mul(mul(sn(1),cs(m)),sn(2)));modal[m]=[hp,hv]
check(modal=={1:[Q(1,2),-Q(1,2)],3:[Q(1,2),Q(3,2)]},'derivative sine2 projection')
# Integrate hprime/r=[h/r]+integral h/r^2. The density coefficients follow.
density={m:(hp+hv)/2 for m,(hp,hv) in modal.items()};check(density=={1:0,3:1},'canonical strain modal sign and factor')
rad=[beta(0,12)/2,-6*beta(1,11),72*beta(2,10)];total=15*rad[0]+6*rad[1]+rad[2];check(total==Q(123,286),'beta energy')
bump=angles['p_times_sin3']*beta(0,6)/2;gs=bump*Q(3,4);comp=Q(4,3);check(comp*gs==bump==Q(1,56) and gs==Q(3,224),'fixed strain compensation');check(comp*Q(3,2)==2,'norm compensation')
# k and L are explicit theorem parameters. Evaluate the squared constant first.
k=Q(1615536043799051,9007199254740992);L=Q(8614738245908811,1125899906842624);alpha=Q(1,2)-k;check(alpha>0,'tail convergence')
radial=1/(2*L**4*alpha);check(radial==1/(L**4*(1-2*k)),'radial primitive')
# Machin identity: tan(2a)=5/12,tan(4a)=120/119 and tan(4a-b)=1.
ta=Q(1,5);tb=Q(1,239);t2=2*ta/(1-ta*ta);t4=2*t2/(1-t2*t2);check(t2==Q(5,12) and t4==Q(120,119) and (t4-tb)/(1+t4*tb)==1,'Machin angle algebra')
def atan(q,N=96):
 terms=[(-1)**j*q**(2*j+1)/Q(2*j+1) for j in range(N)];s=sum(reversed(terms),Q(0));t=(-1)**N*q**(2*N+1)/Q(2*N+1);return min(s,s+t),max(s,s+t)
a=atan(ta);b=atan(tb);pi=(16*a[0]-4*b[1],16*a[1]-4*b[0]);check(3<pi[0]<pi[1]<4,'pi enclosure')
def sqrtbox(q,P=512):
 check(q>0,'root input');n=isqrt((q.numerator<<(2*P))//q.denominator);check(n*n*q.denominator<=q.numerator*(1<<(2*P))<(n+1)*(n+1)*q.denominator,'root bracket');return Q(n,1<<P),Q(n+1,1<<P)
vals={}
for name,f in [('C0',1),('Cang',10)]:vals[name]=(sqrtbox(radial/(f*pi[1]))[0],sqrtbox(radial/(f*pi[0]))[1])
vals['speed_variation']=tuple(x/3 for x in vals['Cang']);vals['speed_cost_lower_factor']=(3/vals['Cang'][1],3/vals['Cang'][0])
# Independent vector representation: (sin3,3cos3)/10 has norm-square 1/10.
check((angles['sin3_squared']+9*angles['cos3_squared'])/100==Q(1,10),'angular dual representation')
first=D/'evidence/compute.json';s=json.loads(first.read_text());check(s['status']=='PASS_ARBITRARY_PRECISION_BALLS_CARTESIAN_POLYNOMIALS_AND_GREEN_IDENTITY','first status')
for n,h in s['files'].items():check(sha(B/n)==h,'first file pin')
for n in ['sin3_squared','p_times_sin3','p_squared']:check(Q(s['angular_over_pi'][n])==angles[n],'independent angular agreement')
check(list(map(Q,s['radial_bump_integrals']))==rad and Q(s['bump_energy_radial'])==total,'independent beta agreement');check(Q(s['bump_sigma_over_epsilon_squared'])==bump and Q(s['g_sigma_over_L_squared'])==gs and Q(s['compensation_over_epsilon_squared_L_inverse_squared'])==comp,'saved compensation');check(Q(s['k_exact'])==k and Q(s['L_exact'])==L and Q(s['radial_dual_exact'])==radial,'saved exact parameters')
comparisons=[]
for n,iv in vals.items():
 lo,hi=map(Q,s['arb512'][n]);check(max(lo,iv[0])<=min(hi,iv[1]),'overlap only');pub=s['public'][n];a0=Q(pub['strict_lower_exact']);b0=Q(pub['strict_upper_exact']);check(a0<iv[0]<=iv[1]<b0 and a0<lo<=hi<b0,'two independent strict public bounds');check(Q(pub['lower_decimal'])==a0 and Q(pub['upper_decimal'])==b0,'display exactness');comparisons.append({'name':n,'rational_lower_margin':str(iv[0]-a0),'rational_upper_margin':str(b0-iv[1]),'arb_lower_margin':str(lo-a0),'arb_upper_margin':str(b0-hi)})
proof=json.loads((D/'evidence/proof_first.json').read_text());check(proof['proof_sha256']==sha(D/'PROOF.md') and proof['utc']<s['utc'],'proof chronology')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_FOURIER_BETA_MACHIN_INTEGER_ROOT_AND_OUTPUT_AUDIT','angular_over_pi':{n:str(v) for n,v in angles.items()},'derivative_modal_coefficients':{str(n):list(map(str,v)) for n,v in modal.items()},'strain_density_coefficients':{str(n):str(v) for n,v in density.items()},'beta_radial_integrals':list(map(str,rad)),'rational_pi96':list(map(str,pi)),'rational_integer_root512':{n:list(map(str,iv)) for n,iv in vals.items()},'strict_comparisons':comparisons,'files':{str(p.relative_to(B)):sha(p) for p in [first,D/'PROOF.md',Path(__file__)]},'scope':'Independent analytic-constant arithmetic. Overlap is a consistency check; each method proves the same strict display enclosure independently. No full dual norm optimality, actual PDE or matrix claim.'}
p=D/'evidence/independent.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'strict_comparisons':len(comparisons)*4,'sha256':sha(p)}))
