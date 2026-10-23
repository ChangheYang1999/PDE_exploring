from pathlib import Path
from datetime import datetime,timezone
import json
import mpmath as mp
from q_high_precision_density import MPQDensity
mp.mp.dps=100
rows=[]
for kap in [2.,6.,11.]:
    coeff=[[1.75,-.125,.03125],[.375,.0625],[-.125]]
    model=MPQDensity(coeff,1.,kap,kap/(kap-1))
    def value(s,t):
        f=mp.fsum(s**j*mp.fsum(mp.mpf(v)*mp.chebyt(k,2*s-1) for k,v in enumerate(cc))*mp.cos(2*j*t) for j,cc in enumerate(coeff))
        return (1-s)*mp.sin(t)*f
    for ss in ['1e-60','.1','.5','.99','0.'+'9'*60]:
        s=mp.mpf(ss);r=mp.sqrt(s)/(2*(1-s))**kap;theta=mp.mpf('.319')
        rho,gx,gy=model.at(r,theta);v=value(s,theta)
        rad=v+mp.diff(lambda q:value(q,theta),s)/(1/(2*s)+kap/(1-s))
        tang=mp.diff(lambda t:value(s,t),theta)
        ref=[v,mp.cos(theta)*rad-mp.sin(theta)*tang,mp.sin(theta)*rad+mp.cos(theta)*tang]
        scale=1-s;err=max(abs(a-b)/scale for a,b in zip([rho,gx,gy],ref))
        assert err<mp.mpf('1e-85'),(kap,ss,err)
        rows.append({'kappa':kap,'sigma':ss,'scaled_error':mp.nstr(err,25)})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','precision':100,'cases':rows,'scope':'Independent Chebyshev sum and automatic high-precision scalar differentiation in compact coordinates, compared with Clenshaw/implicit-map formulas.'}
p=Path('research/complementary_inverse_charts/verification/mp_density_checks.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
