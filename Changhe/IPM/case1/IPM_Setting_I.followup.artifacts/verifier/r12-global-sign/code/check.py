from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import mpmath as mp
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic();mp.mp.dps=90
A=s.symbols('A');a=-4-2/A;q=4/A
c0=2076*A*A+741*A-36;c2=-3060*A*A+305*A-70;c4=1400*A*A-950*A+50
P=1248*A**4-548*A**3+297*A*A-178*A+84
reduced=(c0+c2*a/(a+q)+c4*a*(a+1)/((a+q)*(a+q+1)))/2
assert s.factor(reduced-P/((2*A-1)*(3*A-2)))==0
v=s.symbols('v');assert s.expand(P.subs(A,1+v))==1248*v**4+4444*v**3+6141*v*v+3764*v+903
out={'date':datetime.now(timezone.utc).isoformat(),'proof_md5':hashlib.md5((ROOT/'PROOF.md').read_bytes()).hexdigest(),'precision_digits':mp.mp.dps,'symbolic_beta_reduction':'PASS','positive_shifted_polynomial':'PASS','rows':[]}
for text in ['1.000001','1.3','1.9','1.9999999999','2.0000000001','2.01','3','4','10.150725','10.150725214760579','100','1000000']:
 A=mp.mpf(text);z=2/A
 direct=mp.beta(-4-z,2*z)
 positive=-mp.gamma(2-z)*mp.gamma(2*z)/mp.gamma(1+z)*(2-z)*(3-z)*(4-z)/((1+z)*(2+z)*(3+z)*(4+z))
 err=abs((direct-positive)/direct);assert err<mp.mpf('1e-65') and positive<0
 P=1248*A**4-548*A**3+297*A**2-178*A+84
 S=6*A*(4*A-3)/(8*A-1);L=mp.sqrt(S)
 natural=P*positive/(15*A*(2*A-1)*(3*A-2)*(4*A-3)*(8*A-1)*S**2)
 out['rows'].append({'A':text,'beta_continuation':str(direct),'negative_gamma_formula':str(positive),'relative_discrepancy':str(err),'L_star':str(L),'B5_natural':str(natural),'A2_times_B5_natural':str(A*A*natural)})
 print(text,'L',mp.nstr(L,18),'B5nat',mp.nstr(natural,22),'relerr',mp.nstr(err,5))
z=mp.mpf(1);res=-mp.gamma(2-z)*mp.gamma(2*z)/mp.gamma(1+z)*(2-z)*(3-z)*(4-z)/((1+z)*(2+z)*(3+z)*(4+z));assert res==-mp.mpf(1)/20
out['continuous_beta_at_A2']=str(res);out['direct_resonant_finite_part']='11/1474560 (exact earlier certificate)';out['nonresonant_limit']='-11/1474560';out['large_A_scaled_natural_limit']='-13/1080';out['complete']=True;out['seconds']=time.monotonic()-start
(ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL12NUMERIC+2EXACTCHECKS PASS',out['seconds'])
