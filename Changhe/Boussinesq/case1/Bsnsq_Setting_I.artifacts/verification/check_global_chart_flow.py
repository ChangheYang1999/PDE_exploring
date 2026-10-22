"""Independent generating-flow algebra and application of already audited source certificates."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import sympy as s
import numpy as np
r=Path('research/global_chart_flow');assert (r/'PROOF.md').exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
paths=[Path(__file__),r/'PROOF.md',r/'source_contract/snapshot.json'];assertions=[]
def ck(name,z):
 q=s.cancel(s.expand(z));assert q==0,(name,q);assertions.append(name)
x,e=s.symbols('x e',real=True);beta,k=s.symbols('beta k',real=True)
G=s.Function('G')(x,e);A=s.diff(G,x,e);B=s.diff(G,x,2);C=s.diff(G,e,2)
a=beta+2;b=beta-2;V=beta*x*s.diff(G,x)+b*e*s.diff(G,e)-2*beta*G
Dx=lambda f:s.diff(f,x)-B/A*s.diff(f,e)
Dy=lambda f:s.diff(f,e)/A
W1=beta*x-Dy(V);W2=beta*s.diff(G,x)+Dx(V)
ck('general W1',W1-(a*s.diff(G,e)-b*e*C)/A)
ck('general W2',W2-B*W1-b*e*A)
ck('general eta transport',W1*Dx(e)+W2*Dy(e)-b*e)
ck('general xi transport',W1*Dx(s.diff(G,e))+W2*Dy(s.diff(G,e))-a*s.diff(G,e))
J=s.Matrix([[Dx(s.diff(G,e)),Dy(s.diff(G,e))],[Dx(e),Dy(e)]])
ck('general area determinant',J.det()-1)
ck('general divergence U',Dx(-Dy(V))+Dy(Dx(V)))
ck('general temperature transport',W1*Dx(k*e)+W2*Dy(k*e)-b*k*e)
cases=[]
for be in [s.Rational(21,10),s.Rational(5,2),s.Rational(3),s.Rational(4)]:
 for h in [s.Rational(1,3),s.Rational(1),s.Rational(7,2)]:
  GG=h*x*e+x**3*e/5+2*x*e**3/7+x**3*e**3/11
  AA=s.diff(GG,x,e);BB=s.diff(GG,x,2);CC=s.diff(GG,e,2)
  assert all(c>=0 and all(v%2==0 for v in p) for p,c in s.Poly(AA-h,x,e).terms())
  VV=be*x*s.diff(GG,x)+(be-2)*e*s.diff(GG,e)-2*be*GG
  xx=lambda f:s.diff(f,x)-BB/AA*s.diff(f,e)
  yy=lambda f:s.diff(f,e)/AA
  ww1=be*x-yy(VV);ww2=be*s.diff(GG,x)+xx(VV)
  ck(f'manufacture eta {be,h}',ww1*xx(e)+ww2*yy(e)-(be-2)*e)
  ck(f'manufacture xi {be,h}',ww1*xx(s.diff(GG,e))+ww2*yy(s.diff(GG,e))-(be+2)*s.diff(GG,e))
  ck(f'manufacture strain {be,h}',xx(yy(VV)).subs({x:0,e:0})+2)
  ck(f'manufacture physical slope {be,h}',yy(k*e).subs({x:0,e:0})-k/h)
  for i,w in enumerate([ww1,ww2]):
   for j,d in enumerate([xx,yy]):ck(f'manufacture DW {be,h,i,j}',d(w).subs({x:0,e:0})-((be+2 if i==0 else be-2) if i==j else 0))
  cases.append({'beta':str(be),'h':str(h),'positive_chart_lower':str(h),'DW':['%s'%(be+2),'0','0','%s'%(be-2)]})
ss=s.symbols('s', positive=True);EE=1+x**2+(e/ss)**6
assert (EE-1).is_nonnegative is True
source_hashes={'num_c20sedge_inner128':'62df5606c929d8ae86620cff1cce4b79c6180c2214883a3922751a306ba81688','num_resolution_J96K80':'134d909825dab1e1e4856d67f4b38525c7f348e5fb61929133bf3261e073f919','num_resolution_J96K64':'fb05ac9a8c903f2c3b1a9e2587c4b8d5f2859eba20296d8ed3cdbfa8625a4ff0','num_resolution_J80K64':'bd1ad1d636634e20593c4270893af434d16d9e0535461775624295a04a9bab25'}
applications=[]
for name,original_sha in source_hashes.items():
 root=Path('candidate_audits')/name
 closure=root/'source_application_bindings.json';c=json.loads(closure.read_text());paths.append(closure)
 for p,h in c['hashes'].items():assert sha(p)==h,p
 lp=root/'source_schema/link.json';link=json.loads(lp.read_text());paths.append(lp)
 assert link['original_sha256']==original_sha and sha(link['original'])==original_sha
 assert sha(link['view'])==link['view_sha256']
 with np.load(link['view'],allow_pickle=False) as d:
  assert float(d['beta'])==3 and float(d['alpha'])==3 and float(d['a0'])==600
  assert all(np.isfinite(d[z]).all() for z in ['c','cc','se','core'])
  assert float(d['se'])>0 and np.asarray(d['core']).shape==(1,4)
  assert np.all(np.asarray(d['core'])[0,2:]>0)
  positive_parameters={'s':float(d['se']),'R':float(d['core'][0,2]),'L':float(d['core'][0,3]),'alpha':float(d['alpha'])}
 cp=root/'full_chart_sharp009/link.json';chart=json.loads(cp.read_text());paths.append(cp)
 assert chart['status']=='CONFIRMED_SOURCE_LINK' and chart['source_sha256']==link['view_sha256']
 assert F(chart['outer_normalized_margin'])==F(1,10) and F(chart['patch_normalized_bound'])==F(9,100)
 assert F(chart['actual_patch_bound'])<F(9,100) and F(chart['full_normalized_margin'])==F(1,100)
 # Every already bound chart link is itself in the source closure.
 assert any(Path(p).resolve()==cp.resolve() and h==sha(cp) for p,h in c['hashes'].items())
 delta=F(chart['outer_normalized_margin'])-F(chart['patch_normalized_bound']);assert delta==F(chart['full_normalized_margin']) and delta>0
 applications.append({'positive_parameters':positive_parameters,'name':name,'original_sha256':original_sha,'view_sha256':link['view_sha256'],'source_closure_files':len(c['hashes']),'delta':str(delta),'beta':3,'DW_at_origin':[[5,0],[0,1]],'zero_set':'{(0,0)}','backward_basin':'R^2','claim_method':'theorem consequences, not numerically computed: proved global conjugacy, explicit smooth parity formula, and prior exact source/chart certificate'})
snap=json.loads((r/'source_contract/snapshot.json').read_text())
for v in snap['sources'].values():assert sha(v['copy'])==v['sha256'];paths.append(Path(v['copy']))
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_GLOBAL_CHART_FLOW_ALGEBRA_AND_FOUR_APPLICATION_BINDINGS','assertion_count':len(assertions),'assertions':assertions,'manufactured_cases':cases,'applications':applications,'hashes':{str(p):sha(p) for p in paths},'scope':'Exact symbolic identities and re-application of already certified fixed-source chart hypotheses. No new chart solver, vorticity PDE, finite residual accuracy, continuum solution or endpoint.'}
(r/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],len(assertions),'symbolic assertions',len(cases),'manufactures',len(applications),'source applications')
