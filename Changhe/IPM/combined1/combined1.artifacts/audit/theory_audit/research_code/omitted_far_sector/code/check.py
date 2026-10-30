from pathlib import Path
from datetime import datetime,timezone
import importlib.util,json,hashlib,sys,time
from flint import fmpq as Q
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1];RESEARCH=BASE.parent
P=RESEARCH/'weak_probe_audit/code/reproduce.py'
s=importlib.util.spec_from_file_location('omitted_polar',P);M=importlib.util.module_from_spec(s);s.loader.exec_module(M)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def choose(x,q):
 b=Q(1)
 for k in range(q):b*=Q(x-k)/Q(k+1)
 return b
def main():
 start=time.monotonic();src=RESEARCH/'taylor_projection/source/canonical007.json';state=json.loads(src.read_text());peerpath=BASE/'source/N4_result.json';peer=json.loads(peerpath.read_text())
 pick=[(o,v) for o,v in zip(state['order'],state['coefficients'],strict=True) if o[0]==0 and o[1] in [0,1]]
 subset={**state,'order':[o for o,v in pick],'coefficients':[v for o,v in pick]}
 c,delta,rho,stream=M.fields(subset);a=delta/2;R=rho[0,1];rows=[]
 for q in range(7):
  density=sum((b*choose(-a-k,q) for k,b in enumerate(R)),Q(0));residual=-2*c*q*density;old=peer['rows'][q]
  assert density==Q(old['rho_sine1_exact']) and residual==Q(old['linear_residual_sine1_exact'])
  rows.append({'q':q,'density_exact':str(density),'residual_exact':str(residual),'peer_exact_agreement':True,'residual_float_diagnostic':float(residual)})
 assert Q(rows[4]['residual_exact'])!=0
 assert all((((ell-1)*delta/2).denominator!=1) for ell in range(2,17))
 inputs=[src,peerpath,P,BASE/'PROOF.md',Path(__file__)]
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'C1-N1-007-d2w-j7-e2bal','method':'Exact density polynomial, then expansion of (1+z)^(-a) R(1/(1+z)); independent of homogeneous potential derivatives','inputs':{str(p):sha(p) for p in inputs},'selected_potential_coefficients':len(pick),'density_polynomial_degree':R.degree(),'rows':rows,'nonresonance_ell_2_to_16':True,'q4_nonzero':True,'elapsed_seconds':time.monotonic()-start}
 with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'q4',rows[4]['residual_float_diagnostic'],'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
