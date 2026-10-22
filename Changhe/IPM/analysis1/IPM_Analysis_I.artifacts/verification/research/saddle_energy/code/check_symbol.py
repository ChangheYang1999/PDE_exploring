"""Exact local saddle energy scalars, independently enclosed by Arb and mpmath.iv."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
import flint,mpmath
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/saddle_energy/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0';ctx.prec=256;iv.dps=100
inp=json.loads((E/'inputs.json').read_bytes());rawpath=B/'data_exact/modal_v2.json';assert sha(rawpath)==inp['modal_input_sha256']
k=F(inp['k_exact']);s=F(inp['s_exact']);raw=json.loads(rawpath.read_bytes());assert F.from_float(float.fromhex(raw['scalars_hex']['k']))==k
cl=1/k;A=2*cl-1;D=4*cl-1;assert D==2*A+1 and A>1 and cl>1
values={'c_l':cl,'A':A,'D':D,'S_y':s*D-(1+cl),'S_x':-s*A-(1+cl)}
aa=lambda x:arb(x.numerator)/x.denominator
ac=1/aa(k);av={'c_l':ac,'A':2*ac-1,'D':4*ac-1,'S_y':aa(s)*(4*ac-1)-(1+ac),'S_x':-aa(s)*(2*ac-1)-(1+ac)}
iq=lambda x:iv.mpf(x.numerator)/x.denominator
ki,si=iq(k),iq(s)
ivv={'c_l':1/ki,'A':(2-ki)/ki,'D':(4-ki)/ki,'S_y':(4*si-1)/ki-si-1,'S_x':-(2*si+1)/ki+si-1}
def rf(x):
 sign,m,e,bc=x;assert bc>=0
 return (-1 if sign else 1)*F(int(m))*F(2)**int(e)
def af(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
rows=[]
for key,v in values.items():
 ar=av[key];it=ivv[key];assert ar.is_finite() and not iv.isnan(it) and not iv.isinf(it)
 alo,ahi=af(ar.lower()),af(ar.upper());ilo,ihi=map(rf,it._mpi_)
 assert alo<=v<=ahi and ilo<=v<=ihi
 rows.append({'quantity':key,'exact':str(v),'arb_lower':str(alo),'arb_upper':str(ahi),'iv_lower':str(ilo),'iv_upper':str(ihi),'arb_display':ar.str(28)})
assert values['S_y']>0 and values['S_x']<0
# Independent rational checks at Pythagorean directions reproduce the Rayleigh quotient.
fixtures=0
for x,y in [(F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(5,13),F(12,13))]:
 assert x*x+y*y==1
 assert s*(-A*x*x+D*y*y)-(1+cl)==values['S_x']*x*x+values['S_y']*y*y;fixtures+=1
res={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/saddle_energy/PROOF.md'),'inputs_sha256':sha(E/'inputs.json'),'versions':{'python-flint':flint.__version__,'mpmath':mpmath.__version__},'precision_bits':ctx.prec,'iv_dps':iv.dps,'interval_checks':10,'rayleigh_identities':fixtures,'values':rows,'scope':'Exact normalized modal scalar k and frozen linear saddle energy, no variable-coefficient numerical map.'}
(E/'symbol_audit.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({'utc':res['utc'],'status':'PASS','interval_checks':10,'S_y':av['S_y'].str(24),'S_x':av['S_x'].str(24)}))
