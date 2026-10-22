"""Exact source and chart-pinned horizontal far compatibility and center comparison."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,ast,json,datetime,hashlib
import numpy as np
ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('root');args=ap.parse_args()
source=Path(args.source);ROOT=Path(args.root);OUT=ROOT/'far_axis_exact';OUT.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
# Own previously symbolically checked coefficient functions, extracted without running its source-specific audit.
orig=Path('code/certify_logarithmic_far_axis.py');names={'endpoint','interval','scaled','coefficient'};nodes=[n for n in ast.parse(orig.read_text()).body if isinstance(n,ast.FunctionDef) and n.name in names];assert len(nodes)==len(names)
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(orig),'exec'))
with np.load(source,allow_pickle=False) as z:
 if set(z.files)-set('c a0 J Kw m beta hist Nt Ns tmin gauge alpha se gam l gpu_port init'.split()):raise ValueError('Unknown source fields')
 if float(z['beta'])!=3 or int(z['m'])!=3 or float(z['alpha'])!=3 or float(z['gam'])!=0:raise ValueError('Unsupported parameters')
 for key in ['c','a0','alpha','se']:
  if z[key].dtype!=np.dtype('float64') or not np.all(np.isfinite(z[key])):raise ValueError('Expected finite dyadic storage')
 c=z['c'].reshape(int(z['J'])+1,int(z['Kw'])+1);a=F.from_float(float(z['a0']));s=F.from_float(float(z['se']))
if s<=0 or a==0:raise ValueError('Degenerate source')
chart=ROOT/'chart_certificate/replay.json';cr=json.loads(chart.read_text())
if cr['status']!='CONFIRMED' or cr['pinned_source_sha256']!=sha(source) or F(cr['delta'])<=0 or cr['manufacture_mode']:raise ValueError('Matching positive chart certificate required')
for file,digest in cr['hashes'].items():
 if sha(file)!=digest:raise ValueError('Chart dependency changed: '+file)
N=100;lo=sum(F(3**k,factorial(k)) for k in range(N+1));hi=lo+F(3**(N+1),factorial(N+1))/(1-F(3,N+2));c1=((1-1/lo)/3,(1-1/hi)/3);c1sq=(c1[0]**2,c1[1]**2)
p={(i,j):sum(F.from_float(float(c[n,k]))*endpoint(n,i)*endpoint(k,j) for n in range(c.shape[0]) for k in range(c.shape[1])) for i,j in [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]}
hc=sum(F.from_float(float(c[n,k]))*(-1)**k for n in range(c.shape[0]) for k in range(c.shape[1]));ptc=sum(F.from_float(float(c[n,k]))*2*n*n*(-1)**k for n in range(c.shape[0]) for k in range(c.shape[1]));qc=sum(F.from_float(float(c[n,k]))*2*(-1)**(k+1)*k*k for n in range(c.shape[0]) for k in range(c.shape[1]))/s**2
ell=(-(hi-1)/18,-(lo-1)/18);pc0=scaled(ell,ptc);pc=(pc0[0]+hc/3,pc0[1]+hc/3)
if hc<=0 or pc[0]<=0<=pc[1]:raise ValueError('Cannot divide by center coefficient')
reciprocal=tuple(sorted(1/v for v in pc));correction=scaled(reciprocal,14*qc/hc);acenter=(70*hc+correction[0],70*hc+correction[1])
h,K=coefficient(p,s,F(3));forcing=2*a/(3*h);terms=scaled(c1sq,K);value=(terms[0]+forcing,terms[1]+forcing);target=scaled(c1sq,-3*h*K/2)
row=dict(utc=now(),source=str(source),source_sha256=sha(source),script_sha256=sha(__file__),coefficient_script_sha256=sha(orig),chart_replay_sha256=sha(chart),delta=cr['delta'],exp3=interval((lo,hi)),c1_squared=interval(c1sq),p={str(k):str(v) for k,v in p.items()},s=str(s),a=str(a),h=str(h),K=str(K),forcing=str(forcing),F_axis=interval(value),amplitude_required_by_axis=interval(target),center_h=str(hc),center_p=interval(pc),center_q=str(qc),amplitude_required_by_center=interval(acenter),center_far_amplitude_intervals_disjoint=(acenter[1]<target[0] or target[1]<acenter[0]),sign='negative' if value[1]<0 else 'positive' if value[0]>0 else 'unresolved',scope='Necessary horizontal far coefficient and center identity for this fixed shape. Disjoint intervals exclude amplitude-only repairs, not changes of shape or beta. Chart/source exact rational certificate required. Formulas and proof in research/logarithmic_far_compatibility.')
(OUT/'audit.json').write_text(json.dumps(row,indent=2)+'\n');print(json.dumps({k:row[k] for k in ['F_axis','amplitude_required_by_axis','amplitude_required_by_center','center_far_amplitude_intervals_disjoint','sign']}))
