"""Fresh audit of serialized constants and split exponential integrals."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/frozen_holder/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ends(v):return [F(int(m))*F(2)**int(e) for m,e in [x.man_exp() for x in (v.lower(),v.upper())]]
def scalar_exact(A,g):
 D=A-1;H=g-D;av=g/D;qv=(g+1)/A
 return {'A':A,'g':g,'a':av,'b':1-1/A,'p':1+1/D,'q':qv,'r_2_5':(5*A-3)/(2*A),'r_q':((g+1)*D+A)/(A*A),'r_2':(2*A-1)/A,'alpha_for_two_derivatives':1/D,'s_fast':(2*g+A+3)/(2*A),'alpha_sobolev_window':(2*g-5*A+3)/(2*A),'source_for_2_5':(5*A-2)/(2*D),'gap_a_minus_1':H/D,'gap_A_plus_1_minus_a':(A*A-1-g)/D,'gap_a_minus_q':H/(D*A),'gap_q_minus_1':H/A,'dyadic_integral_constant':A*D*D/(H*(A*A-1-g)),'L2_inverse_upper':2/(A+3),'C1_tail_integral_upper':2*g/H}
def main():
 start=time.monotonic();ctx.prec=1536;ctx.threads=1;data=json.loads((E/'checks.json').read_text());inputs=json.loads((E/'inputs.json').read_text())
 assert data['status']=='PASS' and data['code_sha256']==sha(B/'research/frozen_holder/code/check_exponents.py') and data['proof_sha256']==sha(B/'research/frozen_holder/PROOF.md') and data['inputs_sha256']==sha(E/'inputs.json')
 assert len(data['symbolic_identities'])==data['symbolic_identity_count']==20
 contain=0;exact_count=0;finite=0;selected=0;dig=hashlib.sha256();ln2=arb(2).log()
 for inp,row in zip(inputs['parameter_sets'],data['parameter_sets'],strict=True):
  assert inp['name']==row['name'];A=F(inp['A']);g=F(inp['g']);sc=scalar_exact(A,g);a=sc['a'];q=sc['q']
  assert set(sc)==set(row['exact']) and A>1 and 1<a<A+1
  for key,x in sc.items():
   assert x==F(row['exact'][key]);exact_count+=1;l,h=ends(aa(x))
   for method in ['arb','iv']:
    box=row['values'][method][key];assert F(box['lower_exact'])<=l<=x<=h<=F(box['upper_exact']),(inp['name'],key,method);contain+=1
  examples={(r['J'],r['j']):r for r in row['integral_examples']};expected=set()
  for J in range(1,33):
   for j in range(J+1):
    left=F(J-j)/A;right=F(J-j);turn=F(J)/A;cuts=sorted({left,right,*([turn] if left<turn<right else [])});value=arb(0)
    for x,y in zip(cuts,cuts[1:]):
     rate=a-1 if (x+y)/2<=turn else a-A-1;extra=0 if (x+y)/2<=turn else J
     value+=(ln2*aa(a*(j-J)+extra+rate*x)).exp()*((ln2*aa(rate*(y-x))).exp()-1)/aa(rate)
    target=aa(sc['dyadic_integral_constant'])*(ln2*aa(min(F(j-J),a*j-q*J))).exp();ratio=value/target;lo,hi=ends(ratio);assert hi<1;finite+=1
    dig.update(f"{inp['name']}:{J}:{j}\n".encode())
    if J in (1,2,4,8,16,32) and j in {0,J//2,int((1-1/A)*J),J-1,J}:
     expected.add((J,j));r=examples[(J,j)];selected+=1
     for method in ['arb','iv']:
      box=r['values'][method];assert F(box['lower_exact'])<=lo<=hi<=F(box['upper_exact']),(inp['name'],J,j,method);contain+=1
  assert set(examples)==expected
 assert 2*finite==data['finite_integral_inequalities']==2240 and selected==data['selected_integral_examples'] and dig.hexdigest()==data['coverage_sha256']
 obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','precision':1536,'scalar_exact_checks':exact_count,'fresh_integral_inequalities':finite,'selected_integral_examples':selected,'containments':contain,'input_sha256':sha(E/'checks.json'),'inputs_sha256':sha(E/'inputs.json'),'code_sha256':sha(__file__),'proof_sha256':data['proof_sha256'],'seconds':time.monotonic()-start,'scope':data['scope']}
 (E/'output_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj))
if __name__=='__main__':main()
