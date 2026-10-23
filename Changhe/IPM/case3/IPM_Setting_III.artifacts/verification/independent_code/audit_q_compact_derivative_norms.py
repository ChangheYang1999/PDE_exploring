"""Independent whole-plane derivative norms using compact positive quadrature."""
import argparse,json,hashlib,sys,time
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import mpmath as mp
from polar_derivative_norms import QNormEvaluator
from compact_norm_quadrature import nodes,radius_and_jacobian
sys.set_int_max_str_digits(1000000)
ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--tag',required=True);ap.add_argument('--dps',type=int,default=80);ap.add_argument('--nodes',type=int,required=True);ap.add_argument('--node-digits',type=int,default=50);ap.add_argument('--kmax',type=int,default=6);args=ap.parse_args()
gate=Path('research/compact_derivative_quadrature/verification/manufactured.json');gd=json.loads(gate.read_text());assert gd['status']=='PASS'
for file,key in [('independent_code/compact_norm_quadrature.py','code_sha256'),('independent_code/polar_derivative_norms.py','norm_code_sha256')]:assert hashlib.sha256(Path(file).read_bytes()).hexdigest()==gd[key]
p=Path(args.input);raw=json.loads(p.read_text());dest=Path('evidence/q_compact_derivative_norms')/args.tag;dest.mkdir(parents=True,exist_ok=True);out=dest/f'nodes{args.nodes}_dps{args.dps}.json'
record=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',input=str(p),input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),source_sha256=raw['source_sha256'],dps=args.dps,nodes=args.nodes,node_digits=args.node_digits,kmax=args.kmax,command=[sys.executable,*sys.argv],gate_sha256=hashlib.sha256(gate.read_bytes()).hexdigest(),code_sha256=gd['code_sha256'],norm_code_sha256=gd['norm_code_sha256'],auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=[],totals={},scope='Positive full ordered Cartesian derivative norm, exact finite angular identity, and independent canonical full-plane inverse. Gauss-Legendre approximates the complete compactified radial integral; no finite physical-domain boundary or omitted tail is imposed. Numerical quadrature is not an interval enclosure or a limiting regularity theorem. Shell tallies use the same global nodes and are only diagnostic.')
def pack(v):return mp.nstr(v,min(args.dps-10,65))
def save():record['updated_utc']=datetime.now(timezone.utc).isoformat();out.write_text(json.dumps(record,indent=2)+'\n')
save();qs,meta=nodes(args.nodes,args.node_digits);record['node_metadata']=meta;save()
model=QNormEvaluator(raw['coefficients'],raw['L'],raw['kappa'],raw['ell'],dps=args.dps,kmax=args.kmax);record['inverse_working_dps']=model.workdps;save()
with mp.workdps(args.dps):
 mf=lambda s:mp.mpf(Fraction(s).numerator)/Fraction(s).denominator
 L=mf(raw['L']);kappa=mf(raw['kappa']);totals={k:{f:mp.mpf(0) for f in ['rho','residual']} for k in range(2,args.kmax+1)}
 shell_edges=list(map(mp.mpf,['0','.0001','.001','.01','.1','1','10','100','10000']))+[mp.inf];shells=[{k:{f:mp.mpf(0) for f in ['rho','residual']} for k in totals} for i in range(len(shell_edges)-1)]
 for index,(s,w) in enumerate(qs):
  r,jac=radius_and_jacobian(s,L,kappa);start=time.monotonic();values=model.at_radius(r);elapsed=time.monotonic()-start
  row=dict(index=index,s=pack(s),r=pack(r),weight=pack(w),jacobian=pack(jac),elapsed_seconds=elapsed,values={str(k):{f:pack(v) for f,v in z.items()} for k,z in values.items()});record['rows'].append(row)
  shell=next(i for i in range(len(shells)) if shell_edges[i]<=r<shell_edges[i+1])
  for k in totals:
   for f in totals[k]:v=w*jac*values[k][f];totals[k][f]+=v;shells[shell][k][f]+=v
  save()
  if index%10==0 or index==len(qs)-1:print(json.dumps(dict(utc=record['updated_utc'],tag=args.tag,index=index,nodes=args.nodes,r=row['r'],seconds=elapsed)),flush=True)
 for k,z in totals.items():record['totals'][str(k)]=dict(rho_norm_squared=pack(z['rho']),residual_norm_squared=pack(z['residual']),rho_norm=pack(mp.sqrt(z['rho'])),residual_norm=pack(mp.sqrt(z['residual'])),eta=pack(mp.sqrt(z['residual']/z['rho'])))
 record['sampled_radii']=[record['rows'][0]['r'],record['rows'][-1]['r']]
 record['shells']=[dict(r_lo=pack(shell_edges[i]),r_hi=pack(shell_edges[i+1]),norm_squared={str(k):{f:pack(v) for f,v in z.items()} for k,z in sh.items()}) for i,sh in enumerate(shells)]
record['status']='COMPUTED';record['finished_utc']=datetime.now(timezone.utc).isoformat();save();print(json.dumps(dict(tag=args.tag,nodes=args.nodes,status=record['status'],totals=record['totals'])),flush=True)
