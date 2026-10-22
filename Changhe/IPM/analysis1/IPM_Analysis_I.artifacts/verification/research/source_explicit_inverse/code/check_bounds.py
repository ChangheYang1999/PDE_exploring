"""Whole-source-disc high derivative and auxiliary inverse enclosures."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,math,time
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from datetime import datetime,timezone
from functools import lru_cache
from flint import arb,ctx,fmpq
from mpmath import iv
import mpmath
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/source_explicit_inverse';E=D/'evidence'
@lru_cache(None)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def qa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def qi(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def af(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def vf(x):s,m,e,_=x;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 if isinstance(x,arb):assert x.is_finite();return af(x.lower()),af(x.upper())
 assert not any(mpmath.isinf(z) or mpmath.isnan(z) for z in (x.a,x.b));return tuple(map(vf,x._mpi_))
def upper(x):return ends(x)[1]
def mag(x):lo,hi=ends(x);return max(abs(lo),abs(hi))
def box(lo,hi,Q):assert lo<=hi;return qa(lo).union(qa(hi)) if Q==qa else iv.mpf([qi(lo).a,qi(hi).b])
def decode(z):
 assert z['schema']=='arb-dyadic-mid-radius-v1'
 m=F(int(z['mid_m']))*F(2)**int(z['mid_e']);r=F(int(z['rad_m']))*F(2)**int(z['rad_e']);assert r>=0
 return m-r,m+r

def poly_deriv(p,j):return [c*(math.factorial(k)//math.factorial(k-j)) for k,c in enumerate(p) if k>=j]
def poly_mag(p,h,eng):
 Q=qa if eng=='arb' else qi
 if not p:return Q(0)
 N=len(p)-1
 if eng=='arb':
  power=[sum((p[k]*qa(h**k*math.comb(k,l)*(-1)**(k-l)*2**l) for k in range(l,N+1)),arb(0)) for l in range(N+1)]
  bc=[sum((power[l]*qa(F(math.comb(k,l),math.comb(N,l))) for l in range(k+1)),arb(0)) for k in range(N+1)]
  return qa(max(mag(x) for x in bc))
 return qi(upper(sum((qi(mag(c))*qi(h**k) for k,c in enumerate(p)),iv.mpf(0))))

def mul_aff(p,c):
 out=[F(0)]*(len(p)+1)
 for j,x in enumerate(p):out[j]+=c*x;out[j+1]+=x
 return out
@lru_cache(None)
def ladder(beta,m,k):
 out=[]
 for u in range(k+1):
  p=[F(1)]
  for j in range(u):p=mul_aff(p,beta-m-2*j)
  for j in range(k-u):p=mul_aff(p,beta+m-2*j)
  out.append(tuple(p))
 return tuple(out)
@lru_cache(None)
def cartesian(beta,m,k,xcount):
 terms={m:[F(1)]}
 for step in range(k):
  y=step>=xcount;out={}
  for nu,p in terms.items():
   for dn,c,sg in [(1,beta-step-nu,1),(-1,beta-step+nu,-1 if y else 1)]:
    pp=[sg*v/2 for v in mul_aff(p,c)];dest=out.setdefault(nu+dn,[F(0)]*len(pp))
    for j,x in enumerate(pp):dest[j]+=x
  terms=out
 return tuple(tuple(p) for _,p in sorted(terms.items()))

def independent_weight_identity():
 # Sum the ladder branches for x derivatives and compare every frequency.
 checks=0
 for beta in (3,4):
  for m in (1,2,3,17,522):
   for k in range(6):
    got=cartesian(beta,m,k,k)
    expected=[]
    # Cartesian keys run from m-k to m+k: u=number of plus derivatives.
    for u,p in enumerate(ladder(beta,m,k)):expected.append(tuple(F(math.comb(k,u),2**k)*c for c in p))
    assert got==tuple(expected),(beta,m,k);checks+=1
 return checks

def pbound(weights,der,Q):return sum((Q(abs(w))*d for w,d in zip(weights,der)),Q(0))
def derivative_modes(beta,modes,derivs,k,eng,a,b):
 Q=qa if eng=='arb' else qi;exp=lambda x:x.exp() if eng=='arb' else iv.exp(x)
 power=beta-k;rad=exp(Q(power*(b if power>=0 else a)))
 if eng=='arb':
  total=Q(0)
  for m,ds in zip(modes,derivs):total+=Q(max(upper(pbound(w,ds,Q)) for w in ladder(beta,m,k)))
  return Q(2)**Q(F(k,2))*rad*total
 components=[]
 for xc in range(k+1):
  total=Q(0)
  for m,ds in zip(modes,derivs):total+=sum((pbound(w,ds,Q) for w in cartesian(beta,m,k,xc)),Q(0))
  components.append(rad*total)
 return sum((math.comb(k,xc)*v*v for xc,v in enumerate(components)),Q(0))**Q(F(1,2))

def cutoff_constants():
 S=[F(0)]*4+[F(35),F(-84),F(70),F(-20)]
 def ev(p,x):return sum((v*x**j for j,v in enumerate(p)),F())
 assert ev(S,F(0))==0 and ev(S,F(1))==1
 for j in (1,2,3):assert ev(poly_deriv(S,j),F(0))==ev(poly_deriv(S,j),F(1))==0
 assert poly_deriv(S,1)==[F(0),F(0),F(0),F(140),F(-420),F(420),F(-140)]
 assert sum((c/F(j+1) for j,c in enumerate(S)),F())==F(1,2)
 L=[F(1),F(4,3)]+[F(4,3)*4**(j-1)*sum((abs(c)*(math.factorial(k)//math.factorial(k-j+1)) for k,c in enumerate(S) if k>=j-1),F()) for j in (2,3,4)]
 aa=F(273,64);nu=F(23,4)/aa;vv=3/aa
 C=[F(1)]+[sum((F(math.factorial(j),2**l*math.factorial(l)*math.factorial(j-2*l))*L[j-l]*nu**(j-2*l)*vv**l for l in range(j//2+1)),F()) for j in range(1,5)]
 assert C[1]==F(1472,819)<2
 return L,C

def main():
 start=time.monotonic();inp=B/'research/n8_velocity_hessian/evidence/moment_inputs.json';data=json.loads(inp.read_text());files={};counts=Counter()
 for rel in ['research/n8_density_hessian/evidence/verdict.json','research/n8_velocity_hessian/evidence/verdict.json','research/n8_coefficient_closure/evidence/verdict.json','research/source_instance/evidence/verdict.json','research/source_order_family/evidence/verdict.json']:
  p=B/rel;v=json.loads(p.read_text());files[rel]=sha(str(p))
  for f,h in v['files'].items():assert sha(str(B/f))==h,f;counts['dependency_pins']+=1
 for f,h in data['files'].items():assert sha(str(B/f))==h,f;counts['moment_input_pins']+=1
 files[str(inp.relative_to(B))]=sha(str(inp));assert files[str(inp.relative_to(B))]=='6f7d3dcf4f1f09256970c0796dc461bc3262cc109051305aa40e9da76a7aa61c'
 spans=data['spans'];pmin,pmax=map(F,data['source_center_bracket_exact']);delta=F(data['delta_exact']);assert delta==F(33,2000);r0=3*delta
 assert [s['span'] for s in spans]==list(range(663,670))
 for s,t in zip(spans,spans[1:]):assert s['b_exact']==t['a_exact']
 counts['ladder_cartesian_weight_identities']=independent_weight_identity();L,C=cutoff_constants();rows=[];maxima={'arb':{},'iv':{}}
 for eng in ('arb','iv'):
  Q=qa if eng=='arb' else qi;ex=lambda x:x.exp() if eng=='arb' else iv.exp(x)
  assert upper(ex(Q(F(spans[0]['a_exact']))))<pmin-r0 and ends(ex(Q(F(spans[-1]['b_exact']))))[0]>pmax+r0;counts['whole_disc_radial_coverage']+=1
  for sp in spans:
   a,b=F(sp['a_exact']),F(sp['b_exact']);h=(b-a)/2;length=b-a;assert F(sp['polynomial_mid_exact'])==(a+b)/2
   HP=[[box(*decode(z),Q) for z in p] for p in sp['density_polynomials']];assert len(HP)==262 and all(len(p)==8 for p in HP)
   assert all(decode(z)==(F(0),F(0)) for z in sp['density_polynomials'][-1])
   HD=[[poly_mag(poly_deriv(p,j),h,eng) for j in range(6)] for p in HP];counts[eng+'_polynomial_derivative_envelopes']+=262*6
   derivs=[]
   for n in range(1,262):
    vals=[]
    for side,lam,hl,anchor in [('I',-2*n-4,HD[n-1],sp['i_left'][n-1]),('J',2*n-4,HD[n],sp['j_right'][n-1])]:
     y0=Q(max(map(abs,decode(anchor))));lam_e=lam if side=='I' else -lam
     if eng=='arb':
      z=ex(Q(lam_e*length));integ=Q(length) if lam_e==0 else (z-1)/lam_e
      env=z*y0+integ*hl[0];Y=Q(max(upper(y0),upper(env)))
     else:Y=ex(Q(abs(lam_e)*length))*(y0+Q(length)*hl[0])
     vv=[Y]
     for j in range(1,6):vv.append(abs(lam)**j*Y+sum((abs(lam)**(j-1-l)*hl[l] for l in range(j)),Q(0)))
     vals.append(vv);counts[eng+'_moment_whole_span_envelopes']+=1
    derivs.append([x+y for x,y in zip(*vals)])
   result={}
   for j in (3,4,5):result['rho'+str(j)]=upper(derivative_modes(3,range(1,522,2),HD[:261],j,eng,a,b))
   for j in (3,4):result['U'+str(j)]=upper(derivative_modes(4,range(2,523,2),derivs,j+1,eng,a,b)/2)
   for k,v in result.items():assert v>=0;maxima[eng][k]=max(maxima[eng].get(k,F(0)),v)
   rows.append({'engine':eng,'span':sp['span'],'bounds_exact':{k:str(v) for k,v in result.items()}})
   print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'engine':eng,'span':sp['span'],'seconds':time.monotonic()-start,'bounds_display':{k:float(v) for k,v in result.items()}}),flush=True)
 upperboth={k:max(maxima['arb'][k],maxima['iv'][k]) for k in maxima['arb']}
 # Outward integer ceilings simplify the final scalar computation.
 ceilings={k:(v.numerator//v.denominator+1) for k,v in upperboth.items()};MV=F(743,2500);MR=F(5059,10000)
 bv=[MV*r0*r0/2,MV*r0,MV,F(ceilings['U3']),F(ceilings['U4'])];bq=[MR*r0,MR]+[F(ceilings['rho'+str(j)]) for j in (3,4,5)]
 BW=[sum((math.comb(j,k)*C[k]*delta**(-k)*bv[j-k] for k in range(j+1)),F()) for j in range(5)];BQ=[sum((math.comb(j,k)*C[k]*delta**(-k)*bq[j-k] for k in range(j+1)),F()) for j in range(5)]
 scalar={}
 for eng in ('arb','iv'):
  Q=qa if eng=='arb' else qi;pi=arb.pi() if eng=='arb' else iv.pi;sqrt=lambda x:x**Q(F(1,2));alpha=lambda t:1/(2*sqrt(pi*(Q(t)-1)));beta=lambda t:1/(2*sqrt(pi*(Q(t)-1)*(Q(t)-2)))
  HW=sqrt(pi*Q(r0*r0*sum((math.comb(4,j)*x*x for j,x in enumerate(BW)),F())));HQ=sqrt(pi*Q(r0*r0*sum((math.comb(4,j)*x*x for j,x in enumerate(BQ)),F())))
  sr={}
  for s in (F(61,20),F(153,50),F(31,10)):
   K=F(1301,200)-F(101,100)*s;Es=delta*((12*s+F(9,2))*MV+3*MR);aa=K-Es;dd=(101*s-1)/100;assert aa>0 and dd>0
   RR=sqrt(Q(2))*Q(s*(s-1))*Q(2)**Q(s-4)*(alpha(2)+beta(s-1))*HW+sqrt(Q(2))*Q(s)*Q(2)**Q(s-2)*(alpha(3)+alpha(s-1))*HQ
   norm=(1+RR/Q(dd))**Q(s)/Q(aa)
   sr[str(s)]={'R_upper':str(upper(RR)),'inverse_upper':str(upper(norm)),'R_display':float(upper(RR)),'inverse_display':float(upper(norm)),'a_lower_exact':str(aa),'d_lower_exact':str(dd)}
  scalar[eng]={'H_w_upper':str(upper(HW)),'H_q_upper':str(upper(HQ)),'H_w_display':float(upper(HW)),'H_q_display':float(upper(HQ)),'rows':sr}
 for p in (Path(__file__),D/'PROOF.md',D/'ADDENDUM.md',E/'proof_first.json'):files[str(p.relative_to(B))]=sha(str(p))
 assert sha(str(D/'PROOF.md'))==json.loads((E/'proof_first.json').read_text())['proof_sha256']
 output={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXPLICIT_AUXILIARY_INVERSE_BOUND','counts':dict(counts),'cutoff_L_exact':list(map(str,L)),'cutoff_C_exact':list(map(str,C)),'delta_exact':str(delta),'high_derivative_ceilings':ceilings,'high_derivative_maxima_exact':{e:{k:str(v) for k,v in z.items()} for e,z in maxima.items()},'cutoff_product_Bw_exact':list(map(str,BW)),'cutoff_product_Bq_exact':list(map(str,BQ)),'scalar_results':scalar,'span_rows':rows,'files':files,'seconds':time.monotonic()-start,'scope':'Explicit chosen compact C4 coefficients only; canonical archive imported; full IPM inverse/rank-one/outer matching still OPEN.'}
 (E/'checks.json').write_text(json.dumps(output,indent=2)+'\n');print(json.dumps({'status':output['status'],'seconds':output['seconds'],'ceilings':ceilings,'counts':dict(counts)}),flush=True)
if __name__=='__main__':main()
