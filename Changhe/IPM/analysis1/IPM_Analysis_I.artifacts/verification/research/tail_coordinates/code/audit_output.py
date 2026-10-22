"""Fresh high-precision layer moments, trigonometric integrals and adjugates."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,hashlib,time,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/tail_coordinates/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(z):z=F(z);return arb(fmpq(z.numerator,z.denominator))
def ends(z):
 def dyad(m,e):return F(int(m))*F(2)**int(e)
 return tuple(dyad(*v.man_exp()) for v in (z.lower(),z.upper()))
def rec(z):l,u=ends(z);return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def det(M):
 if len(M)==1:return M[0][0]
 return sum(((-1)**j*M[0][j]*det([r[:j]+r[j+1:] for r in M[1:]]) for j in range(len(M))),F())
def inverse(M):
 dd=det(M);assert dd!=0;n=len(M)
 return [[(-1)**(i+j)*det([r[:i]+r[i+1:] for k,r in enumerate(M) if k!=j])/dd for j in range(n)] for i in range(n)]
def trace(nu,N):
 lam=aa(F(nu,2));end=(-lam).exp();J=[(1-end)/lam]
 for n in range(1,15+N):J.append((n*J[-1]-end)/lam)
 norm=F(math.factorial(15),math.factorial(7)**2);integ=arb(0)
 for m in range(N+1):
  for l in range(m+1):
   for a in range(8):integ+=aa(norm*F(nu,2)**m/F(math.factorial(m))*math.comb(m,l)*(-1)**a*math.comb(7,a))*J[7+a+l]
 integ*=end
 return aa(F(math.factorial(N),nu**N))*(1-integ)
def main():
 start=time.monotonic();ctx.prec=1536;ctx.threads=1;r=json.loads((E/'checks.json').read_text());assert r['status']=='PASS'
 assert r['proof_sha256']==sha(B/'research/tail_coordinates/PROOF.md') and r['code_sha256']==sha(B/'research/tail_coordinates/code/check_tail.py')
 raw=B/'data_exact/modal_v2.json';assert sha(raw)==r['data_sha256']=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 hx=json.loads(raw.read_text())['scalars_hex']['k'];sig,expo=hx.split('p');a,b=sig[2:].split('.');k=F(int(a+b,16))*F(2)**(int(expo)-4*len(b));assert k==F(1615536043799051,9007199254740992)
 gamma=F(1129,1000);beta=2-gamma;rad=1/beta
 for i in range(1,4):rad*=F(i)/(beta+i)
 angular_over_pi=-16*F(math.comb(18,9),4**9)+24*F(math.comb(16,8),4**8)-9*F(math.comb(14,7),4**7)+F(math.comb(12,6),4**6)
 ell2_pi=2*rad*angular_over_pi;H=[[F(9,20),F(1,5)],[F(1,10),F(3,10)]];hi=inverse(H);CH=max(sum(map(abs,row)) for row in hi);bc=[F(1,7),F(-1,11)];cb=[F(1,13),F(1,17)];S=2-sum(cb[i]*hi[i][j]*bc[j] for i in range(2) for j in range(2));border=[[H[0][0],H[0][1],bc[0]],[H[1][0],H[1][1],bc[1]],[cb[0],cb[1],F(2)]];tail=[[F(2),F(1),F(-1)],[F(3),F(-2),F(7)],[F(5),F(4),F(6)]];mats={'tail_block':tail,'border':border};inv={n:inverse(M) for n,M in mats.items()}
 exact={'k':k,'gamma':gamma,'a':F(6),'tail_power':2*k-1,'zeroth_far_margin':gamma-2*k,'radial_tail_divergence_power':2*k+1-2*gamma,'tail_x4_angular':(2-k)/2,'tail_x6_cartesian':-(k-3)*(k-5)/8,'transport_gap':1-(gamma-1)/k,'strain_squared_times_pi':ell2_pi,'flat_trace_squared_constant':F(math.factorial(12),2**13),'closure_theta':F(4,27),'closure_bound':CH,'border_S':S,'border_bound':CH+(1+CH*max(map(abs,bc)))/S*(1+sum(map(abs,cb))*CH),'border_actual_inverse_norm':max(sum(map(abs,row)) for row in inv['border'])}
 assert r['exact_parameters']=={n:str(v) for n,v in exact.items()} and r['matrix_inputs']=={n:[[str(v) for v in row] for row in M] for n,M in mats.items()} and r['exact_inverse']=={n:[[str(v) for v in row] for row in M] for n,M in inv.items()}
 count=0
 def contain(val,row1,row2):
  nonlocal count
  l,u=ends(val)
  for row in [row1,row2]:assert F(row['lower_exact'])<=l<=u<=F(row['upper_exact']);count+=1
 vals={n:aa(v) for n,v in exact.items()};pi=16*aa(F(1,5)).atan()-4*aa(F(1,239)).atan();vals['strain_squared']=aa(ell2_pi)/pi;vals['strain_constant']=vals['strain_squared'].sqrt()
 for n,v in vals.items():contain(v,r['values']['arb'][n],r['values']['iv'][n])
 tr={}
 for N in [2,4]:
  for nu in [4,16,64]:
   v=trace(nu,N);main=aa(F(math.factorial(N),nu**N));q=aa(F(nu,2));err=main*(-q).exp()*sum((q**i/math.factorial(i) for i in range(N+1)),arb(0));row={'multiplier':v,'leading':main,'tail_error_bound':err,'relative_gap':(main-v)/main};key=f'{N}:{nu}'
   for n,v in row.items():contain(v,r['trace_integrals']['arb'][key][n],r['trace_integrals']['iv'][key][n])
   tr[key]={n:rec(v) for n,v in row.items()}
 for n,M in inv.items():
  for i,row in enumerate(M):
   for j,v in enumerate(row):contain(aa(v),r['matrix_inverses']['arb'][n][i][j],r['matrix_inverses']['iv'][n][i][j])
 assert count==120 and len(r['exact_identities'])==38 and set(r['exact_identities'].values())=={'0'}
 o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'check_code_sha256':r['code_sha256'],'proof_sha256':r['proof_sha256'],'checks_sha256':sha(E/'checks.json'),'fresh_containments':count,'fresh_values':{n:rec(v) for n,v in vals.items()},'fresh_traces':tr,'method':'Arb1536 layer-cake cutoff identity with integration-by-parts moments, cosine even-power angular integral, Machin atan pi, exact adjugate inverses and independent hex parse.','seconds':time.monotonic()-start,'scope':'Illustrative scalar and finite matrix verification, no global operator bounds.'}
 (E/'output_audit.json').write_text(json.dumps(o,indent=2)+'\n');s=json.loads((E/'review_summary.json').read_text());s['audit_sha256']=sha(E/'output_audit.json');s['audit']={k:v for k,v in o.items() if k not in ['fresh_values','fresh_traces']};(E/'review_summary.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps({k:v for k,v in o.items() if k in ['utc','status','seconds','fresh_containments']}))
if __name__=='__main__':main()
