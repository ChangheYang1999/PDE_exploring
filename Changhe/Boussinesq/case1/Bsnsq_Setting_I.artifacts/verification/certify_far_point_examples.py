"""Pinned-source rational far points; no claim of an angular upper bound."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,json,hashlib,time
from flint import fmpq as Q,fmpq_poly as Poly
from checked_core_source import bind
from far_section_rational import construct,endpoint_polynomials

def main():
 ap=argparse.ArgumentParser();ap.add_argument('folder');ap.add_argument('--out',required=True);args=ap.parse_args()
 start=time.monotonic();p=Path(args.folder);inp=json.loads((p/'input.json').read_text())
 data,binding=bind(inp['source_json']);r=construct(endpoint_polynomials(data),data['s'],data['alpha'])
 assert binding['source_sha256']==inp['source_binding']['source_sha256']
 assert r['K']==inp['common_power'] and r['final_orders']==inp['final_orders']
 for k,poly in [('A',r['A'])]+[('N'+str(j+1),q) for j,q in enumerate(r['numerators'])]:
  assert Poly([Q(q) for q in inp['polynomials'][k]])==poly
 # Separate exact exponential remainder computation, no producer bounds import.
 alpha=F(data['alpha']);N=int(inp['exponential']['terms_through']);term=F(1);lo=term
 for j in range(1,N+1):term*=alpha/j;lo+=term
 hi=lo+term*alpha/(N+1)/(1-alpha/F(N+2))
 assert N+2>alpha and lo>1
 c12=[((1-1/lo)/alpha)**2,((1-1/hi)/alpha)**2]
 assert list(map(F,inp['c12']))[0]<=c12[0]<=c12[1]<=list(map(F,inp['c12']))[1]
 a=F(data['a']);rows=[]
 for w in ['803/1000','1/40','4/5','7/16','221317/10000000']:
  vals=[F(str(q(Q(w)))) for q in r['numerators']];A=F(str(r['A'](Q(w))))
  s=sum(vals[:3]);cl,ch=sorted([c12[0]*s+a*vals[3],c12[1]*s+a*vals[3]])
  dl=c12[0]*sum(map(abs,vals[:3]))+abs(a*vals[3]);du=c12[1]*sum(map(abs,vals[:3]))+abs(a*vals[3]);assert A>0 and dl>0
  al=F(0) if cl<=0<=ch else min(abs(cl),abs(ch));ah=max(abs(cl),abs(ch))
  rows.append({'w':w,'ratio_lower':str(al/du),'ratio_upper':str(ah/dl),'display':[float(al/du),float(ah/dl)],'A':str(A),'denominator_lower':str(dl)})
 out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
 paths=[Path(__file__),p/'input.json',Path(inp['source_json']),Path(data['source']),Path('code/checked_core_source.py'),Path('code/far_section_rational.py'),Path('research/interval_far_section/PROOF.md')]
 report={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXACT_POINT_INTERVALS','source_binding':binding,'rows':rows,'seconds':time.monotonic()-start,'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'scope':'Exact source-reconstructed limiting-section points only. No between-point upper bound or finite-radius error bound. Same derivative constructor as closed result72, distinct exact exponential and point inequalities.'}
 (out/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k not in ['hashes','source_binding','rows']},indent=2))
 for v in rows:print(v['w'],v['display'])
if __name__=='__main__':main()
