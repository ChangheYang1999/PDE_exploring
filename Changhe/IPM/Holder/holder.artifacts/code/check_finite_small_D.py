"""Independent recomputation for the three small-exponent D certificates."""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
from fractions import Fraction
from flint import arb,ctx
import mpmath as mp,json,hashlib
from finite_projection_diagnostic import evaluate
ctx.prec=256;mp.mp.dps=90

def mp_endpoint(text,upper):
 b=arb(text);q=(b.upper() if upper else b.lower()).fmpq()
 return mp.mpf(str(q.numerator))/mp.mpf(str(q.denominator))

rows=[]
for code,text,cupper in [('001','1/1000','637.0652723887'),('01','1/100','64.1129530993'),('05','1/20','13.2090680608')]:
 rawpath=Path(f'data/finite_projection_fine_a{code}.json');raw=json.loads(rawpath.read_text())
 finalpath=Path(f'data/finite_D_lower_a{code}.json');final=json.loads(finalpath.read_text())
 frac=Fraction(text);alpha=mp.mpf(frac.numerator)/frac.denominator;delta=mp.mpf(1)/24;L=mp.mpf(4096)-mp.mpf('.5')
 A=mp.gamma((alpha+2)/2)/(2*mp.sqrt(mp.pi)*mp.gamma((alpha+3)/2))
 terms=dict(local_leading=2*A*delta**alpha/alpha,local_loss=2*alpha*delta/(mp.pi*(1-2*delta))+2*(1+delta)*delta**(alpha+3)/((1-delta)**4*(alpha+3)),tail_error=2**alpha*L**(alpha-1)/((1-alpha)*(1-1/(4*L*L))**2))
 for key,value in terms.items():assert mp_endpoint(raw[key],False)<value<mp_endpoint(raw[key],True)
 regular=mp_endpoint(raw['regular_interval'],False)
 profile=json.loads(Path('data/profile_constant_positive_certificate.json').read_text())
 K=mp.mpf(next(r['safe_upper'] for r in profile['rows'] if Fraction(r['alpha'])==frac))
 value=(regular+terms['local_leading']-terms['local_loss']-terms['tail_error']+mp.mpf('.5'))/K
 # The combined output has additional outward ball rounding, which can only lower its certified endpoint.
 assert mp.mpf(final['safe_D_lower'])<=value
 gauss=evaluate(float(alpha),a=1.,nr=480,nt=600)['regular']
 assert float(mp_endpoint(raw['regular_interval'],False))<gauss<float(mp_endpoint(raw['regular_interval'],True))
 gap=Decimal(final['safe_D_lower'])-Decimal(cupper);assert gap>0
 rows.append(dict(alpha=text,D_lower=final['safe_D_lower'],C_upper=cupper,certified_gap=str(gap),independent_endpoint=mp.nstr(value,75),regular_gauss=gauss,endpoint_checks='passed at90 decimal digits',input_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [rawpath,finalpath]}))
Path('data/finite_small_D_independent_checks.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows),indent=2)+'\n');print(rows)
