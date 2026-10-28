"""Independent 90-decimal endpoint and Gaussian check at alpha=3/10."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import mpmath as mp
from finite_projection_extended_diagnostic import evaluate
ctx.prec=256;mp.mp.dps=90
rawpath=Path('data/finite_projection_fine_a30.json');finalpath=Path('data/finite_D_lower_a30.json');raw=json.loads(rawpath.read_text());final=json.loads(finalpath.read_text())
def endpoint(text,upper):
    b=arb(text);q=(b.upper() if upper else b.lower()).fmpq()
    return mp.mpf(str(q.numerator))/mp.mpf(str(q.denominator))
a=mp.mpf(3)/10;delta=mp.mpf(3)/56;L=mp.mpf(8191)/2
A=mp.gamma((a+2)/2)/(2*mp.sqrt(mp.pi)*mp.gamma((a+3)/2))
terms=dict(local_leading=2*A*delta**a/a,local_loss=2*a*delta/(mp.pi*(1-2*delta))+2*(1+delta)*delta**(a+3)/((1-delta)**4*(a+3)),tail_error=2**a*L**(a-1)/((1-a)*(1-1/(4*L*L))**2))
for key,v in terms.items():assert endpoint(raw[key],False)<v<endpoint(raw[key],True)
value=(endpoint(raw['regular_interval'],False)+terms['local_leading']-terms['local_loss']-terms['tail_error']+mp.mpf('.5'))/mp.mpf('1.026981110219')
assert mp.mpf(final['safe_D_lower'])<=value
gauss=evaluate(.3,1.5,nr=480,nt=600)['regular'];assert float(endpoint(raw['regular_interval'],False))<gauss<float(endpoint(raw['regular_interval'],True))
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),independent_endpoint=mp.nstr(value,75),regular_gauss=gauss,D_lower=final['safe_D_lower'],input_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [rawpath,finalpath,Path(__file__)]},status='All endpoint and independent quadrature consistency checks passed')
Path('data/finite_D_a30_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
