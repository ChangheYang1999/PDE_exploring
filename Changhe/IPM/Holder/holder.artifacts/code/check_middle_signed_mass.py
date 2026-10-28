"""Independent nonrigorous sanity check of the proved signed-mass identity."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];mp.mp.dps=60
rows=[]
for frac in ['0.01','0.1','0.3','0.5','0.8','0.99']:
 t=mp.pi*mp.mpf(frac)/2;r=mp.sin(t)
 def G(theta):
  z=r*mp.exp(1j*theta)
  return z/(mp.pi*(z*z-mp.mpf('0.25'))**2)
 raw=r*mp.cos(t)*mp.quad(G,[mp.pi/2-t,mp.pi/2,mp.pi/2+t])
 s=r*r;J=mp.log(1+8*s)+8*s*(1-4*s)/(1+8*s)
 expected=2j*r*mp.cos(t)*J/mp.pi
 err=abs(raw-expected);assert err<mp.mpf('1e-48')
 rows.append(dict(t_over_pi_half=frac,raw_real=mp.nstr(raw.real,50),raw_imag=mp.nstr(raw.imag,50),expected_imag=mp.nstr(expected.imag,50),error=mp.nstr(err,10)))
base=ROOT/'08_improved_upper_bounds/middle_circle_transport/balanced_residual/verification';base.mkdir(parents=True,exist_ok=True)
result=dict(time_utc=datetime.now(timezone.utc).isoformat(),scope='Floating quadrature sanity check only; analytic proof and outward replay are independent requirements',rows=rows,
 code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(base/'signed_mass_sanity.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
