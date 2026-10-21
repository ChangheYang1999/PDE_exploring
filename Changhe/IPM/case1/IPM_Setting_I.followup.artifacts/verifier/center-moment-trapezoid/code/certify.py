from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,time
import numpy as np
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'exact-data/code'))
from nodal_input import load

def binary(x):
 p,q=float(x).as_integer_ratio();return arb(p)/q

def integrated_coefficients(table):
 N=len(table)-1;M=len(table[0]);assert N>0 and M>0
 pi=arb.pi();alpha=lambda j:arb(1)/2 if j in (0,N) else arb(1)
 lam=[2*alpha(j)/N*sum((alpha(n)*(pi*n*j/N).cos()/(1-n*n) for n in range(0,N+1,2)),arb(0)) for j in range(N+1)]
 assert sum(lam,arb(0)).contains(1)
 d=[sum((lam[j]*binary(table[N-j][a]) for j in range(N+1)),arb(0)) for a in range(M)]
 return [(arb(1) if m==0 else arb(2))/M*sum((d[a]*(pi*m*(2*a+1)/(2*M)).cos() for a in range(M)),arb(0)) for m in range(M)]

def enclose(coeffs,L,cl,beta,J=512):
 assert L>0 and cl>1 and abs(beta)<1 and J>0
 k=1/cl;pi=arb.pi();total=arb(0)
 for j in range(J):
  phi=2*pi*j/J;cphi=phi.cos();sphi=phi.sin();C=sum((c*(phi*m).cos() for m,c in enumerate(coeffs)),arb(0));T=phi+beta*sphi
  total+=C*(1+beta*cphi)*(1+T.cos()-(2*T).cos()-(3*T).cos())/4
 a=arb(1)/4;D=sum((c.abs_upper()*(m*a).exp() for m,c in enumerate(coeffs)),arb(0));t=a+abs(beta)*a.sinh()
 M=D*(1+abs(beta)*a.cosh())*(1+t.exp()+(2*t).exp()+(3*t).exp())/4
 remainder=(L*L/(1-k)*2*M/((J*a).exp()-1)).abs_upper()
 main=L*L/(1-k)*total/J;value=main+arb(0,remainder)
 return value,{'J':J,'strip_a':'1/4','strip_bound':M.str(40),'quadrature_remainder':remainder.str(40),'quadrature_sum_contribution':main.str(45),'c':value.str(45)}

def tests():
 # Constant table and radial q: exact binary Lobatto samples for N=2.
 c=integrated_coefficients(np.ones((3,4)));assert c[0].contains(1) and all(t.contains(0) for t in c[1:])
 for beta in [arb(0),binary(.9)]:
  z,row=enclose(c,arb(2),arb(6),beta);assert (z-arb(6)/5).contains(0)
 # T2(2q-1)-1 has samples 0,-2,0 and radial mean -4/3.
 table=np.array([[1.]*4,[-1.]*4,[1.]*4]);c=integrated_coefficients(table);assert (c[0]+arb(1)/3).contains(0)
 z,row=enclose(c,arb(2),arb(6),arb(0));assert (z+arb(2)/5).contains(0)
 # q*cos(2phi), M=3 midpoint cos(2phi) samples 1/2,-1,1/2.
 vals=np.array([[1.,1.,1.],[1.25,.5,1.25],[1.5,0.,1.5]])
 c=integrated_coefficients(vals);assert c[0].contains(1) and c[1].contains(0) and (c[2]-arb(1)/2).contains(0)
 z,row=enclose(c,arb(2),arb(6),arb(0));assert (z-arb(9)/10).contains(0)
 print('MANUFACTURED_PERIODIC_MOMENT_PASS',flush=True)

if __name__=='__main__':
 ctx.prec=256;tests()
 if '--test' in sys.argv:raise SystemExit
 primary=ROOT.parent/'center-moment/verification/certificates.json';data=json.loads(primary.read_text());assert data['complete']
 records=[(ROOT.parent/'center-moment'/r['exact_json'],r) for r in data['rows']]
 extra=ROOT.parent/'center-moment/verification/dnB_n96m40SL16_certificate.json';e=json.loads(extra.read_text())
 # The L16 supplement records its own exact JSON path.
 er=e['rows'][0] if 'rows' in e else e
 ep=ROOT.parent/'center-moment'/er['exact_json']
 records.append((ep,er))
 out={'date_start':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'method':'cardinal radial integrals and entire periodic trapezoid with strip bound, no Bessel evaluation','rows':[]}
 for path,old in records:
  start=time.monotonic();o,b,p,sha=load(path);assert np.all(b[0]==1)
  cfs=integrated_coefficients(b);value,row=enclose(cfs,binary(p['L']),binary(p['c_l']),binary(p['beta']))
  oldc=arb(old.get('c96',old.get('c','nan')));assert (value-oldc).contains(0),(value,oldc)
  defect=3*binary(p['c_l'])-1-value
  row.update(source=o['source'],source_sha256=o['source_sha256'],exact_json=str(path),json_sha256=sha,first_method_c=str(oldc),certificates_overlap=True,self_consistency_ball=defect.str(45),self_consistency_contains_zero=defect.contains(0),seconds=time.monotonic()-start)
  out['rows'].append(row);print(json.dumps(row),flush=True)
 out['complete']=True;out['date_end']=datetime.now(timezone.utc).isoformat()
 deps=[Path(__file__),ROOT/'PROOF.md',ROOT.parent/'exact-data/code/nodal_input.py',primary,extra]
 out['dependencies']=[{'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in deps]
 (ROOT/'verification/certificates.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['date_end'],flush=True)
