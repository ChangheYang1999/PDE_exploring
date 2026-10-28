"""Independent aggregate, endpoint and algebra checks for the D certificates."""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
from flint import arb,ctx
import numpy as np,mpmath as mp,json,hashlib
from finite_projection_diagnostic import evaluate
ctx.prec=192;mp.mp.dps=70
rng=np.random.default_rng(434932);z=rng.uniform(-10,10,30000)+1j*rng.uniform(0,10,30000)
X=z.real;Y=z.imag
nu=(X-.5)*Y/(np.pi*((X-.5)**2+Y*Y)**2)-(X+.5)*Y/(np.pi*((X+.5)**2+Y*Y)**2)
complex_nu=-(z/(np.pi*(z*z-.25)**2)).imag
kernel_error=float(np.max(abs(nu-complex_nu)));assert kernel_error<1e-10
rows=[]
for code,text,cupper in [('10','1/10','6.8771683924'),('20','1/5','3.7712855933')]:
    inputpath=Path(f'data/finite_projection_fine_a{code}.json');raw=json.loads(inputpath.read_text());alpha=mp.mpf(text.split('/')[0])/int(text.split('/')[1])
    delta=mp.mpf(1)/24;R=mp.mpf(4096);L=R-mp.mpf('.5');A=mp.gamma((alpha+2)/2)/(2*mp.sqrt(mp.pi)*mp.gamma((alpha+3)/2))
    terms={'local_leading':2*A*delta**alpha/alpha,'local_loss':2*alpha*delta/(mp.pi*(1-2*delta))+2*(1+delta)*delta**(alpha+3)/((1-delta)**4*(alpha+3)),'tail_error':2**alpha*L**(alpha-1)/((1-alpha)*(1-1/(4*L*L))**2)}
    for key,value in terms.items():
        enclosure=arb(raw[key]);assert enclosure.contains(arb(str(value)))
    quad=evaluate(float(alpha),a=1.,nr=480,nt=600)
    enclosure=arb(raw['regular_interval']);assert float(enclosure.lower())<quad['regular']<float(enclosure.upper())
    finalpath=Path(f'data/finite_D_lower_a{code}.json');final=json.loads(finalpath.read_text());dlower=Decimal(final['safe_D_lower']);gap=dlower-Decimal(cupper);assert gap>0
    rows.append(dict(alpha=text,regular_quad=float(quad['regular']),regular_enclosure=raw['regular_interval'],endpoint_checks='all passed at 70 decimal digits',D_lower=str(dlower),C_upper=cupper,certified_gap=str(gap),input_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [inputpath,finalpath]}))
Path('data/finite_D_independent_checks.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),kernel_algebra_max_error=kernel_error,rows=rows),indent=2)+'\n')
print(rows)
