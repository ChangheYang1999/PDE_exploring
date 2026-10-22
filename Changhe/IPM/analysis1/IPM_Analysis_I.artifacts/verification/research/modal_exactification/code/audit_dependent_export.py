"""Actual dependent JSON import versus exact rational endpoint recurrences."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[v]='1'
import json,math,hashlib,time,ast
from types import SimpleNamespace
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];ctx.prec=256;ctx.threads=1
E=BASE/'research/modal_exactification/evidence';S=E/'coeff_export_1453'
start=time.monotonic()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(v):return F.from_float(float.fromhex(v))
def dyad(v):
 m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def bounds(v):return dyad(v.lower()),dyad(v.upper())
d=json.loads((BASE/'data_exact/modal_v2.json').read_text());assert sha(BASE/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
cj=json.loads((S/'cert_coeffs.json').read_text());assert cj['prec']==256
# Execute the actual frozen reader assignments, without the expensive Cert construction.
tree=ast.parse((S/'cert_green_outer.py').read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
assignments=[n for n in fn.body if isinstance(n,ast.Assign) and ast.unparse(n.targets[0]) in ('C.Ei','C.Eo','C.A[0][0]')]
assert len(assignments)==3
C=SimpleNamespace(A=[[arb(0)]]);ns={'C':C,'cj':cj,'arb':arb}
exec(compile(ast.Module(body=assignments,type_ignores=[]),str(S/'cert_green_outer.py'),'exec'),ns)
reader_lines=[ast.get_source_segment((S/'cert_green_outer.py').read_text(),n) for n in assignments]
a=d['arrays'];sc={k:exact(v) for k,v in d['scalars_hex'].items()};k,bi,bo=(sc[v] for v in ('k','bi','bo'))
t=[exact(v) for v in a['knots']['hex']];M,nb=a['S']['shape']
assert d['degree']==7 and len(t)==nb+8 and t[:8]==[t[0]]*8 and t[-8:]==[t[-1]]*8 and all(t[i]<t[i+1] for i in range(7,nb))
def get(name,m,j):return exact(a[name]['hex'][m*a[name]['shape'][1]+j])
def jet(c,t,right):
 v=[]
 for p in range(7,0,-1):
  v.append(c[-1] if right else c[0]);c=[p*(c[i+1]-c[i])/(t[i+p+1]-t[i+1]) for i in range(len(c)-1)];t=t[1:-1]
 return v
def corr(J,P,b):return [sum(((-b)**(i-j)*(J[j]-P[j])/math.factorial(j)/math.factorial(i-j) for j in range(i+1)),F(0)) for i in range(7)]
alpha=[k-3-j*(1-k)-2*l for j,l in d['outer_jl']]
count={'Ei':0,'Eo_m_ge_1':0};samples=[];checked={'Ei':0,'Eo_m_ge_1':0};jumps=[];relative=[]
for m in range(M):
 ji=jet([get('S',m,i) for i in range(8)],t[:16],False)
 jo=jet([get('S',m,i) for i in range(nb-8,nb)],t[-16:],True)
 pi=[sum((get('D',m,j)*(2*j+2)**n for j in range(7)),F(int(m==0 and n==0))) for n in range(7)]
 po=[sum((get('Aout',m,j)*alpha[j]**n for j in range(len(alpha))),F(0)) for n in range(7)]
 ei,eo=corr(ji,pi,bi),corr(jo,po,-bo)
 for label,actual,vals in [('Ei','Ei',ei),('Eo_m_ge_1','Eo',eo)]:
  if actual=='Eo' and m==0:continue
  for j,true in enumerate(vals):
   checked[label]+=1;received=getattr(C,actual)[m][j];lo,hi=bounds(received)
   if true:relative.append((abs(F(cj[actual][m][j])-true)/abs(true),actual,m,j))
   if not lo<=true<=hi:
    count[label]+=1
    if len(samples)<8:samples.append({'array':actual,'mode':m,'power':j,'exact_coefficient':str(true),'exported_decimal':cj[actual][m][j],'imported_lower_exact':str(lo),'imported_upper_exact':str(hi),'distance_lower':str(max(lo-true,true-hi))})
 if m<4:
  jump=C.Ei[m][0]+arb(pi[0].numerator)/pi[0].denominator-arb(ji[0].numerator)/ji[0].denominator
  jumps.append({'mode':m,'jump_ball':jump.str(35),'excludes_zero':not jump.contains(0)})
# A00 is a real scalar-dependent quantity, enclosed by the independent Gauss certificate.
v=json.loads((BASE/'research/modal_repair/evidence/independent_gauss_iv.json').read_text())['values']['A00_correction']
zlo,zhi=F(v['lower_exact_dyadic']),F(v['upper_exact_dyadic']);true_lo,true_hi=get('Aout',0,0)+zlo,get('Aout',0,0)+zhi
lo,hi=bounds(C.A[0][0]);a00disjoint=max(lo,true_lo)>min(hi,true_hi)
assert count['Ei']>0 and count['Eo_m_ge_1']>0
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED false enclosures of exact dependent coefficients in the actual JSON reader','precision_bits':256,'actual_frozen_reader_assignments_executed':reader_lines,'max_relative_decimal_midpoint_errors':[{'relative_error':str(v),'display':float(v),'array':name,'mode':m,'power':j} for v,name,m,j in sorted(relative,reverse=True)[:8]],'coefficients_with_relative_midpoint_error_gt_1e_minus59':sum(v>F('1e-59') for v,_,_,_ in relative),'checked':checked,'exact_coefficients_outside_imported_balls':count,'examples':samples,'first_inner_value_jumps':jumps,'A00':{'disjoint_from_independent_exact_definition_enclosure':a00disjoint,'exported_decimal':cj['A00'],'true_lower':str(true_lo),'true_upper':str(true_hi),'imported_lower':str(lo),'imported_upper':str(hi)},'scope':'Refutes the dependent input enclosure and exact joins after this actual import. Does not by itself give a numerically false final residual supremum.','source_hashes':{p.name:sha(p) for p in S.iterdir() if p.is_file()},'own_code_sha256':sha(Path(__file__)),'seconds':time.monotonic()-start}
(E/'dependent_export_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['utc','checked','exact_coefficients_outside_imported_balls','first_inner_value_jumps','seconds']}));print('A00_disjoint',a00disjoint)
