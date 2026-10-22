"""Two exact cutoff-integral methods, Arb and iv dilated source inverse bounds."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
from time import monotonic
import hashlib,json,math,sys
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_integrated_inverse';E=D/'evidence'
ctx.prec=512;iv.dps=180

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
def trim(p):
 p=list(map(F,p))
 while len(p)>1 and p[-1]==0:p.pop()
 return p or [F(0)]
def add(p,q):return trim([(p[j] if j<len(p) else 0)+(q[j] if j<len(q) else 0) for j in range(max(len(p),len(q)))])
def scale(p,c):return trim([F(c)*z for z in p])
def shift(p,k):return trim([F(0)]*k+list(p))
def mul(p,q):
 v=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):v[i+j]+=a*b
 return trim(v)
def deriv(p,n=1):
 for _ in range(n):p=[j*p[j] for j in range(1,len(p))] or [F(0)]
 return trim(p)
def value(p,t):
 out=F(0)
 for x in reversed(p):out=out*t+x
 return out
def affine(p,a,b):
 out=[F(0)]
 for z in reversed(p):out=add(mul(out,[F(a),F(b)]),[z])
 return out
def square(p):return mul(p,p)
def analytic_K(q):
 d1,d2,d3,d4=[deriv(q,j) for j in range(1,5)]
 return [square(q),scale(shift(square(d1),1),4),
 add(square(add(scale(d1,2),scale(shift(d2,1),4))),square(scale(d1,2))),
 shift(add(square(add(scale(d2,12),scale(shift(d3,1),8))),scale(square(scale(d2,4)),3)),1),
 add(add(square(add(add(scale(d2,12),scale(shift(d3,1),48)),scale(shift(d4,2),16))),scale(square(add(scale(d2,4),scale(shift(d3,1),8))),6)),square(scale(d2,12)))]
def cartesian_K(q,j):
 out=[F(0)]
 for by in range(0,j+1,2):
  rpoly={}
  for n,c in enumerate(q):
   if n<by//2 or 2*n<j:continue
   factor=F(math.comb(n,by//2)*math.factorial(by)*math.factorial(2*n-by),math.factorial(2*n-j))
   rpoly[2*n-j]=rpoly.get(2*n-j,F(0))+c*factor
  for i,c in rpoly.items():
   for k,d in rpoly.items():
    assert (i+k)%2==0;power=(i+k)//2
    if len(out)<=power:out += [F(0)]*(power+1-len(out))
    out[power]+=math.comb(j,by)*c*d
 return trim(out)
def integral_power(p,a,b):return sum((c*(b**(j+1)-a**(j+1))/F(j+1) for j,c in enumerate(p)),F())
def integral_bernstein(p,a,b):
 q=affine(p,a,b-a);n=len(q)-1
 bc=[sum((q[j]*F(math.comb(i,j),math.comb(n,j)) for j in range(i+1)),F()) for i in range(n+1)]
 return (b-a)*sum(bc,F())/F(n+1)
def geometry():
 counts=Counter();a=F(273,64);T=[F(0)]*5+[F(7),F(-14),F(10),F(-5,2)]
 S=deriv(T);assert S==[F(0)]*4+[F(35),F(-84),F(70),F(-20)] and value(T,1)==F(1,2)
 qleft=add([F(1)],scale(affine(T,-16/a,4/a),-F(1,3)))
 qmiddle=[F(7,6)+F(16,3)/a,-F(4,3)/a]
 qright=scale(affine(T,4+16/a,-4/a),F(1,3))
 nodes=[F(0),F(4),F(4)+a/4,F(4)+3*a/4,F(4)+a]
 pieces=[[F(1)],qleft,qmiddle,qright];assert nodes[-1]==F(529,64)
 for i in range(1,5):
  l=pieces[i-1];r=pieces[i] if i<4 else [F(0)]
  for j in range(5):assert value(deriv(l,j),nodes[i])==value(deriv(r,j),nodes[i]);counts['exact_C4_join_checks']+=1
 C=[[F(0)]*3 for _ in range(5)];records=[]
 for i,q in enumerate(pieces):
  K=analytic_K(q);Ks=[cartesian_K(q,j) for j in range(5)]
  for j in range(5):assert K[j]==Ks[j],(i,j);counts['exact_full_tensor_polynomial_equalities']+=1
  vals=[]
  for j in range(5):
   line=[]
   for d in range(3):
    v1=integral_power(shift(K[j],d),nodes[i],nodes[i+1]);v2=integral_bernstein(shift(Ks[j],d),nodes[i],nodes[i+1])
    assert v1==v2 and v1>=0,(i,j,d);C[j][d]+=v1;line.append(str(v1));counts['two_method_exact_integrals']+=1
   vals.append(line)
  records.append({'left':str(nodes[i]),'right':str(nodes[i+1]),'Q_coefficients':list(map(str,q)),'K_coefficients':[list(map(str,p)) for p in K],'integrals':vals})
 assert all(c>0 for row in C for c in row);counts['positive_whole_radial_moments']=15
 return C,records,counts

def fa(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def fi(t):s,m,e,_=t;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def endpoints(x):
 if isinstance(x,arb):assert x.is_finite();return fa(x.lower()),fa(x.upper())
 return fi(x._mpi_[0]),fi(x._mpi_[1])
def box(x):
 lo,hi=endpoints(x);assert lo>0;pad=(1+max(abs(lo),abs(hi)))*F(2)**-400
 return [str(lo-pad),str(hi+pad)]
def qa(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
def qi(v):v=F(v);return iv.mpf(v.numerator)/v.denominator

def evaluate(C,ells,engine):
 Q=qa if engine=='arb' else qi;pi=arb.pi() if engine=='arb' else iv.pi
 sqrt=(lambda x:x.sqrt()) if engine=='arb' else iv.sqrt
 delta=F(33,2000);MV=F(743,2500);MR=F(5059,10000)
 bv=[(MV/2,2),(MV,1),(MV,0),(F(6376),0),(F(87933),0)]
 bq=[(MR,1),(MR,0),(F(505),0),(F(24381),0),(F(3758450),0)]
 alpha=lambda r:1/(2*sqrt(pi*Q(F(r)-1)))
 beta=lambda r:1/(2*sqrt(pi*Q((F(r)-1)*(F(r)-2))))
 phys=[]
 for base in (bv,bq):
  L=[]
  for j in range(5):
   if engine=='arb':
    v=sum((Q(math.comb(j,k)*b)*sqrt(pi*Q(delta**(2+2*d-2*(j-k))*C[j-k][d])) for k,(b,d) in enumerate(base[:j+1])),Q(0))
   else:
    # Factor the common dimensional power first; independent norm evaluation.
    v=sqrt(pi)*Q(delta**(1-j))*sum((Q(math.comb(j,k)*b*delta**(d+k))*sqrt(Q(C[j-k][d])) for k,(b,d) in enumerate(base[:j+1])),Q(0))
   L.append(v)
  phys.append(L)
 def margins(s):return F(1301,200)-F(101,100)*s-delta*((12*s+F(9,2))*MV+3*MR),(101*s-1)/100
 rows=[];unif=[];counts=Counter()
 for ell in ells:
  norms=[]
  for idx,L in enumerate(phys):
   out=[]
   for m in (3,4):
    if engine=='arb':v=Q(ell**(-2 if idx==0 else -1))*sqrt(sum((Q(math.comb(m,j)*ell**(2*j))*L[j]**2 for j in range(m+1)),Q(0)))
    else:
     v=sqrt(sum((Q(math.comb(m,j))*(Q(ell**(j-2 if idx==0 else j-1))*L[j])**2 for j in range(m+1)),Q(0)))
    out.append(v)
   assert endpoints(out[1]-out[0])[0]>0
   norms.append(out)
  (W3,W4),(Q3,Q4)=norms
  for s in map(F,('61/20','153/50','31/10')):
   Ws=W3**Q(4-s)*W4**Q(s-3);Qs=Q3**Q(4-s)*Q4**Q(s-3)
   rr=sqrt(Q(2))*Q(s*(s-1))*Q(2)**Q(s-4)*(alpha(2)*W4+beta(s-1)*Ws)+sqrt(Q(2))*Q(s)*Q(2)**Q(s-2)*(alpha(2)*Q3+alpha(s-1)*Qs)
   aa,dd=margins(s);assert aa>0 and dd>0
   nn=(1+rr/Q(dd))**Q(s)/Q(aa);hh=Q(ell)**Q(-s)*nn
   vals={'W3':W3,'W4':W4,'Q3':Q3,'Q4':Q4,'Ws':Ws,'Qs':Qs,'R':rr,'N_inverse':nn,'H_inverse':hh}
   rows.append({'s':str(s),'ell':str(ell),'a_lower':str(aa),'d_lower':str(dd),'bounds':{k:box(v) for k,v in vals.items()}});counts['named_order_positive_scalars']+=len(vals)
  sm,sp=F(61,20),F(31,10);Ws=W3**Q(4-sp)*W4**Q(sp-3);Qs=Q3**Q(4-sp)*Q4**Q(sp-3)
  rb=sqrt(Q(2))*Q(sp*(sp-1))*Q(2)**Q(sp-4)*(alpha(2)*W4+beta(sm-1)*Ws)+sqrt(Q(2))*Q(sp)*Q(2)**Q(sp-2)*(alpha(2)*Q3+alpha(sm-1)*Qs)
  aa,dd=margins(sp)[0],margins(sm)[1];nn=(1+rb/Q(dd))**Q(sp)/Q(aa);hh=Q(ell)**Q(-sp)*nn
  unif.append({'ell':str(ell),'a_lower':str(aa),'d_lower':str(dd),'bounds':{k:box(v) for k,v in [('R',rb),('N_inverse',nn),('H_inverse',hh)]}});counts['uniform_positive_scalars']+=3
 return {'rows':rows,'uniform':unif,'physical_L2_derivative_bounds':[[box(z) for z in L] for L in phys]},counts

def upper(row,key):return F(row['bounds'][key][1])
def main():
 started=monotonic();C,pieces,counts=geometry();ells=sorted(set([F(1)]+[F(j,4000) for j in range(1,81)]))
 res={};files={}
 for engine in ('arb','iv'):
  res[engine],cc=evaluate(C,ells,engine)
  for k,v in cc.items():counts[engine+'_'+k]=v
  print(engine+' complete',flush=True)
 for name in ('source_explicit_inverse','source_dilation','source_instance','n8_density_hessian','n8_velocity_hessian','source_order_family'):
  p=B/'research'/name/'evidence/verdict.json';v=json.loads(p.read_text());assert v['status'].startswith('CONFIRMED');files[str(p.relative_to(B))]=sha(p)
  for f,h in v['files'].items():assert sha(B/f)==h,f;counts['dependency_pin_checks']+=1
 exact95=json.loads((B/'research/source_explicit_inverse/evidence/checks.json').read_text())
 assert exact95['high_derivative_ceilings']=={'rho3':505,'rho4':24381,'rho5':3758450,'U3':6376,'U4':87933}
 counts['imported_high_derivative_ceilings']=5
 best={}
 for s in map(F,('61/20','153/50','31/10')):
  ar={row['ell']:row for row in res['arb']['rows'] if F(row['s'])==s};ir={row['ell']:row for row in res['iv']['rows'] if F(row['s'])==s};best[str(s)]={}
  for key in ('N_inverse','H_inverse'):
   ell=min(ar,key=lambda e:max(upper(ar[e],key),upper(ir[e],key)));u=max(upper(ar[ell],key),upper(ir[ell],key));best[str(s)][key]={'ell':ell,'upper_exact':str(u),'upper_display':float(u),'integer_strict_ceiling':u.numerator//u.denominator+1}
 ar={row['ell']:row for row in res['arb']['uniform']};ir={row['ell']:row for row in res['iv']['uniform']};best['uniform']={}
 for key in ('N_inverse','H_inverse'):
  ell=min(ar,key=lambda e:max(upper(ar[e],key),upper(ir[e],key)));u=max(upper(ar[ell],key),upper(ir[ell],key));best['uniform'][key]={'ell':ell,'upper_exact':str(u),'upper_display':float(u),'integer_strict_ceiling':u.numerator//u.denominator+1}
 for p in [D/'PROOF.md',E/'proof_first.json',Path(__file__)]:files[str(p.relative_to(B))]=sha(p)
 assert sha(D/'PROOF.md')==json.loads((E/'proof_first.json').read_text())['proof_sha256']
 out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':monotonic()-started,'status':'PASS_INTEGRATED_CUTOFF_AUXILIARY_INVERSE','counts':dict(counts),'scales_exact':list(map(str,ells)),'radial_moments_exact':[[str(c) for c in row] for row in C],'pieces':pieces,'results':res,'best_of_81_scales':best,'files':files,'scope':'Same explicit compact C4 auxiliary operator as95, imported canonical derivative bounds, exact radial cutoff integrals and dilation. No physical rank-one/global IPM inverse.'}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');summary={k:v for k,v in out.items() if k not in ('pieces','results')};(E/'review_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps({'utc':out['utc'],'seconds':out['seconds'],'status':out['status'],'counts':dict(counts),'best':{s:{k:{x:y for x,y in row.items() if x!='upper_exact'} for k,row in b.items()} for s,b in best.items()}},indent=2))
if __name__=='__main__':main()
