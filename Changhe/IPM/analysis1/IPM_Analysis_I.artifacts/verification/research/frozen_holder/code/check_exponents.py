"""Independent exact identities and two interval systems for frozen-source exponents."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as sp
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/frozen_holder/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ii(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ends(x):
 if isinstance(x,arb):return [F(int(m))*F(2)**int(e) for m,e in [a.man_exp() for a in (x.lower(),x.upper())]]
 return [(-1 if s else 1)*F(int(m))*F(2)**int(e) for s,m,e,_ in x._mpi_]
def rec(x):l,u=ends(x);return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def scalars(A,g):
 a=g/(A-1);b=(A-1)/A;q=(1+g)/A;p=A/(A-1);r=lambda s:b*s+1/A;half=(0*A+1)/2
 return {'A':A,'g':g,'a':a,'b':b,'p':p,'q':q,'r_2_5':r(5*half),'r_q':r(q),'r_2':r(2),'alpha_for_two_derivatives':1/(A-1),'s_fast':(g+(A+3)/2)/A,'alpha_sobolev_window':(g+(A+3)/2)/A-3,'source_for_2_5':(A*5*half-1)/(A-1),'gap_a_minus_1':a-1,'gap_A_plus_1_minus_a':A+1-a,'gap_a_minus_q':a-q,'gap_q_minus_1':q-1,'dyadic_integral_constant':1/(a-1)+1/(A+1-a),'L2_inverse_upper':2/(A+3),'C1_tail_integral_upper':2+2/(a-1)}
def integrated(A,g,J,j,method):
 cv=aa if method=='arb' else ii;pow2=(lambda x:arb(2)**aa(x)) if method=='arb' else (lambda x:iv.exp(iv.ln(2)*ii(x)))
 a=g/(A-1);q=(g+1)/A;l=F(J-j)/A;u=F(J-j);tstar=F(J)/A;cut=min(u,tstar);v=cv(0)
 if cut>l:v+=(pow2((a-1)*cut)-pow2((a-1)*l))/cv(a-1)
 cut=max(l,tstar)
 if u>cut:v+=pow2(J)*(pow2((a-A-1)*u)-pow2((a-A-1)*cut))/cv(a-A-1)
 total=pow2(a*(j-J))*v;target=cv(1/(a-1)+1/(A+1-a))*pow2(min(F(j-J),a*j-q*J))
 return total/target

def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180
 A,a,s,beta,xi,eta=sp.symbols('A a sigma beta xi eta',positive=True);g=a*(A-1);b=(A-1)/A;p=A/(A-1);q=(1+g)/A;r=lambda x:b*x+1/A
 identities={
 'q_conjugate':q-a+(a-1)/A,'q_crossover':q-1-(a-1)*b,'r_alternate':r(s)-s+(s-1)/A,
 'first_dyadic_power':-q+b*(a-s)+r(s),'second_dyadic_power':-1+b*(1-s)+r(s),
 'low_lambda_power':1-a+(a-A-1)/A+q,'low_N_power':a+1-(a-A-1)/A-q-2,
 'packet_N_prefactor':1/(A-1)+2*p-a*p+a+(a-A-2)/(A-1)-1,
 'packet_fast_input':p-A/(A-1),'packet_slow_input':p-1/(A-1)-1,
 'packet_v_power':-(a-A-2)+a-1-(A+1),
 'lower_critical_exponent':p*r(s)-s-1/(A-1),
 'same_order_growth':p*s-s-1/(A-1)-(s-1)/(A-1),
 'inverse_source_order':r((A*beta-1)/(A-1))-beta,
 'cusp_scale_prefactor':q+1+1/A-a+(a-A-2)/A,
 'cusp_positive_tail':a-A-2-a-1+A+3,
 'fourier_generator':a-A-2-a*(A*xi**2+eta**2)/(xi**2+eta**2)+A+2+g*xi**2/(xi**2+eta**2),
 'r_at_a':r(a)-q,'r_2_alpha':r(2+s)-2-((A-1)*s-1)/A,
 'L2_rate':-1-(A+1)/2+(A+3)/2}
 for name,x in identities.items():assert sp.cancel(x)==0,name
 exact=json.loads((E/'inputs.json').read_text());rows=[];finite=0;digest=hashlib.sha256();selected_count=0
 for inp in exact['parameter_sets']:
  A=F(inp['A']);g=F(inp['g']);sc=scalars(A,g);assert A>1 and 1<sc['a']<A+1 and 1<sc['q']<sc['a']
  row={'name':inp['name'],'exact':{k:str(v) for k,v in sc.items()},'values':{},'integral_examples':[]}
  for method,cv in [('arb',aa),('iv',ii)]:
   if method=='arb':vals=scalars(cv(A),cv(g))
   else:
    av=cv(g)/cv(A-1);bv=1-1/cv(A);qv=1+(av-1)*bv
    vals={'A':cv(A),'g':cv(g),'a':av,'b':bv,'p':1+1/cv(A-1),'q':qv,'r_2_5':cv(F(5,2))-cv(F(3,2))/cv(A),'r_q':qv-(qv-1)/cv(A),'r_2':2-1/cv(A),'alpha_for_two_derivatives':1/cv(A-1),'s_fast':cv(F(1,2))+cv(g+F(3,2))/cv(A),'alpha_sobolev_window':cv(g+F(3,2))/cv(A)-cv(F(5,2)),'source_for_2_5':cv(F(5,2))+cv(F(3,2))/cv(A-1),'gap_a_minus_1':cv(g-A+1)/cv(A-1),'gap_A_plus_1_minus_a':cv(A*A-1-g)/cv(A-1),'gap_a_minus_q':cv(g-A+1)/(cv(A-1)*cv(A)),'gap_q_minus_1':cv(g+1-A)/cv(A),'dyadic_integral_constant':cv(A)/((av-1)*(cv(A+1)-av)),'L2_inverse_upper':2/cv(A+3),'C1_tail_integral_upper':2*av/(av-1)}
   row['values'][method]={k:rec(v) for k,v in vals.items()}
   for k,v in sc.items():lo,hi=ends(vals[k]);assert lo<=v<=hi,(inp['name'],method,k)
  for J in range(1,33):
   for j in range(J+1):
    rr={}
    for method in ['arb','iv']:
     val=integrated(A,g,J,j,method);lo,hi=ends(val);assert hi<1,(inp['name'],J,j,method);finite+=1;rr[method]=rec(val)
    digest.update(f"{inp['name']}:{J}:{j}\n".encode())
    if J in (1,2,4,8,16,32) and j in {0,J//2,int(sc['b']*J),J-1,J}:
     row['integral_examples'].append({'J':J,'j':j,'values':rr});selected_count+=1
  rows.append(row)
 obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','proof_sha256':sha(B/'research/frozen_holder/PROOF.md'),'code_sha256':sha(__file__),'inputs_sha256':sha(E/'inputs.json'),'symbolic_identities':list(identities),'symbolic_identity_count':len(identities),'parameter_sets':rows,'finite_integral_inequalities':finite,'selected_integral_examples':selected_count,'coverage_sha256':digest.hexdigest(),'seconds':time.monotonic()-start,'scope':'Exact exponent identities and illustrative constants only; integrals are finite diagnostic checks of a separately proved universal estimate. Not a computed global inverse or residual bound.'}
 (E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k not in ['parameter_sets','symbolic_identities']}))
if __name__=='__main__':main()
