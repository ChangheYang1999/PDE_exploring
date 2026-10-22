"""Independent exact-Cox / scaled-series scalar certificate for the modal repair."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,math,hashlib,time,bisect,resource,argparse
from pathlib import Path
from fractions import Fraction as F
from types import SimpleNamespace
from datetime import datetime,timezone
from flint import arb,ctx,fmpq,fmpq_mat
BASE=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from exact_audit import exact_poly
sys.path.insert(0,str(BASE/'research/exponential_moments/code'))
from moments import integral,aa

def utc():return datetime.now(timezone.utc).isoformat()
def fq(v):return fmpq(v.numerator,v.denominator)
def frac(v):return F(str(v))
def ball(v):return {'ball':v.str(40),'lower':v.lower().str(50),'upper':v.upper().str(50)}
def exact(v):return F.from_float(float.fromhex(v))
def output(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=320);args=ap.parse_args();ctx.prec=args.bits;ctx.threads=1;ctx.cap=8
 resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic();path=BASE/'data_exact/modal_v2.json';source=path.read_bytes();sha=hashlib.sha256(source).hexdigest();assert sha=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 d=json.loads(source);sc={k:exact(v) for k,v in d['scalars_hex'].items()};k,L,bi,bo=(sc[v] for v in ('k','L','bi','bo'));assert L>0 and 0<k<F(1,2) and bi>4 and bo>4-2*k
 arrays=d['arrays'];t=[exact(v) for v in arrays['knots']['hex']];M,nb=arrays['S']['shape'];assert d['degree']==7 and M>=4 and len(t)==nb+8
 assert t[:8]==[t[0]]*8 and t[-8:]==[t[-1]]*8 and all(t[i]<t[i+1] for i in range(7,len(t)-8))
 for name,expected in [('S',[M,nb]),('D',[M,7]),('Aout',[M,len(d['outer_jl'])]),('Ei',[M,7]),('Eo',[M,7])]:
  assert arrays[name]['shape']==expected and len(arrays[name]['hex'])==math.prod(expected)
 def get(name,m,j):return exact(arrays[name]['hex'][m*arrays[name]['shape'][1]+j])
 assert all(isinstance(j,int) and isinstance(l,int) and j>=0 and l>=0 for j,l in d['outer_jl'])
 assert d['outer_jl'][0]==[0,0] and len({tuple(v) for v in d['outer_jl']})==len(d['outer_jl'])
 alpha=[(k-3)-j*(1-k)-2*l for j,l in d['outer_jl']];assert alpha[0]==k-3 and all(v<-2 for v in alpha) and alpha[0]+bo>0
 assert all(v<=2*k-4 for v in alpha[1:])
 w=[F(1,4),F(1,8),F(-1,8),F(-1,8)]
 S=[sum((w[m]*get('S',m,j) for m in range(4)),F(0)) for j in range(nb)]
 D=[sum((w[m]*get('D',m,j) for m in range(4)),F(0)) for j in range(7)]
 A=[sum((w[m]*get('Aout',m,j) for m in range(4)),F(0)) for j in range(len(alpha))]
 dummy=SimpleNamespace(t=t,deg=7);cells=[(t[i],t[i+1]) for i in range(7,nb) if t[i]<t[i+1]]
 assert len(cells)==nb-7
 def endpoint_jets(a,b,z):
  span,B=exact_poly(dummy,a,b)
  C=fmpq_mat([[fq(get('S',m,i)) for m in range(M)] for i in range(span-7,span+1)])
  T=B*C
  return [[sum((frac(T[q,m])*F(math.factorial(q),math.factorial(q-n))*z**(q-n) for q in range(n,8)),F(0)) for m in range(M)] for n in range(7)]
 ji=endpoint_jets(*cells[0],-(cells[0][1]-cells[0][0])/2)
 jo=endpoint_jets(*cells[-1],(cells[-1][1]-cells[-1][0])/2)
 def correction(jets,powers,b):return [sum(((-b)**(i-j)*(jets[j]-powers[j])/math.factorial(i-j)/math.factorial(j) for j in range(i+1)),F(0)) for i in range(7)]
 Ei=[];Eo=[]
 for m in range(M):
  pi=[sum((get('D',m,j)*(2*(j+1))**n for j in range(7)),F(int(m==0 and n==0))) for n in range(7)]
  po=[sum((get('Aout',m,j)*alpha[j]**n for j in range(len(alpha))),F(0)) for n in range(7)]
  Ei.append(correction([ji[n][m] for n in range(7)],pi,bi));Eo.append(correction([jo[n][m] for n in range(7)],po,-bo))
 # Exact consistency of all endpoint derivatives, independent of any interval solve.
 for m in range(M):
  for n in range(7):
   ci=sum((Ei[m][j]*F(math.factorial(n),math.factorial(n-j))*bi**(n-j) for j in range(n+1)),F(0))
   pi=sum((get('D',m,j)*(2*(j+1))**n for j in range(7)),F(int(m==0 and n==0)))
   co=sum((Eo[m][j]*F(math.factorial(n),math.factorial(n-j))*(-bo)**(n-j) for j in range(n+1)),F(0))
   po=sum((get('Aout',m,j)*alpha[j]**n for j in range(len(alpha))),F(0))
   assert ci+pi==ji[n][m] and co+po==jo[n][m]
 eip=[sum((w[m]*Ei[m][j] for m in range(4)),F(0)) for j in range(7)]
 eop=[sum((w[m]*Eo[m][j] for m in range(4)),F(0)) for j in range(7)]
 inner=F(1,8)+sum((D[j]/(2+2*(j+1)) for j in range(7)),F(0))+sum((eip[j]*(-1)**j*math.factorial(j)/(2+bi)**(j+1) for j in range(7)),F(0))
 outer=sum((A[j]/(-2-alpha[j]) for j in range(len(alpha))),F(0))+sum((eop[j]*math.factorial(j)/(bo-2)**(j+1) for j in range(7)),F(0))
 c0=aa(inner)*(2*aa(t[0])).exp()+aa(outer)*(2*aa(t[-1])).exp();middle=arb(0)
 output(stage='start',cells=len(cells),bits=args.bits,exact_join_equations=2*7*M)
 for count,(a,b) in enumerate(cells,1):
  span,B=exact_poly(dummy,a,b);T=B*fmpq_mat([[fq(v)] for v in S[span-7:span+1]]);h=b-a
  assert 2*h<F(1)  # |rate| times full cell width; hence N=64 meets the proved series-tail condition.
  midco=[frac(T[j,0]) for j in range(8)]
  local=[sum((math.comb(l,j)*midco[l]*(-h/2)**(l-j) for l in range(j,8)),F(0)) for j in range(8)]
  middle+=(2*aa(a)).exp()*integral(2,local,F(0),h,N=64)
  if count%100==0:output(stage='scalar_cells',done=count,total=len(cells),seconds=time.monotonic()-start)
 c0+=middle
 srat=F(1,4)/(-alpha[0]-2)*((alpha[0]+bo)/(bo-2))**7
 # Independent exact finite-geometric-sum evaluation of the same slope.
 s2=F(1,4)*(1/(-alpha[0]-2)-sum(((alpha[0]+bo)**j/(bo-2)**(j+1) for j in range(7)),F(0)))
 assert srat==s2 and srat>0
 slope=aa(srat)*(2*aa(t[-1])).exp();target=3/aa(k)-1;z=(target-c0)/slope
 R=(aa(t[-1])).exp();Rm=aa(t[0]).exp();WR=(1+(R/aa(L))**2)**((aa(k)-3)/2);Wm=(1+(Rm/aa(L))**2)**((aa(k)-3)/2)
 correction_distance=abs(z)/WR
 # Rigorous global factor distance caused by replacing the stored Ei,Eo with exact jets,
 # under the common knot-endpoint convention. Triangle inequality over all modes.
 Di=[sum((abs(Ei[m][j]-get('Ei',m,j)) for m in range(M)),F(0)) for j in range(7)]
 Do=[sum((abs(Eo[m][j]-get('Eo',m,j)) for m in range(M)),F(0)) for j in range(7)]
 def epmax(j,b):return arb(1) if j==0 else (arb(j)/aa(b))**j*arb(-j).exp()
 join_distance=sum((aa(Di[j])*epmax(j,bi) for j in range(7)),arb(0))/Wm+sum((aa(Do[j])*epmax(j,bo-(3-k)) for j in range(7)),arb(0))/WR
 out={'utc':utc(),'input_json_sha256':sha,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'moments_source_sha256':hashlib.sha256((BASE/'research/exponential_moments/code/moments.py').read_bytes()).hexdigest(),'exact_Cox_source_sha256':hashlib.sha256((BASE/'research/canonical_inverse/code/exact_audit.py').read_bytes()).hexdigest(),'bits':args.bits,'series_terms':64,'cells':len(cells),'exact_join_equations_checked':2*7*M,'finite_exponent_sign_conditions':'PASS exact rational','inner_integral':ball(aa(inner)*(2*aa(t[0])).exp()),'middle_integral':ball(middle),'outer_integral':ball(aa(outer)*(2*aa(t[-1])).exp()),'c_before_scalar_repair':ball(c0),'target':ball(target),'target_minus_c0':ball(target-c0),'normalization_slope':ball(slope),'A00_correction':ball(z),'exact_joins_cost_in_factor_norm':ball(join_distance),'scalar_correction_cost_in_factor_norm':ball(correction_distance),'total_exactification_cost_common_endpoints':ball(join_distance+correction_distance),'canonical_c_after_definition':ball(target),'seconds':time.monotonic()-start,'status':'COMPUTED_REQUIRES_INDEPENDENT_AUDIT','scope':'Exactified modal trial under endpoint-knot convention. Distance is to the literal modal trial under the same endpoints, not directly to X3. No residual certificate.'}
 E=BASE/'research/modal_repair/evidence';(E/'scalar_result.json').write_text(json.dumps(out,indent=2)+'\n');output(stage='done',**out)
 definition={'status':'EXACT_DEFINITION_WITH_COMPUTED_ENCLOSURES_REQUIRING_INDEPENDENT_AUDIT','exact_base_input':'modal_v2.json','input_sha256':sha,'boundary_convention':'Physical inner/outer radii are exp(first/last exact stored knot).','dependent_coefficients':'Ei and Eo are defined by the exact six-jet formulas in the modal_repair proof; A00_star=A00+(3/k-1-c0)/s with s given by its strictly positive closed form. Recompute Eo mode zero after this change.','proof':'../research/modal_repair/PROOF.md','enclosures':'../research/modal_repair/evidence/scalar_result.json','rounded_coefficients_are_not_definitions':True}
 (BASE/'data_exact/modal_v2_repair.json').write_text(json.dumps(definition,indent=2)+'\n')
if __name__=='__main__':main()
