from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,time
from flint import ctx,arb
from radial import Radial
ROOT=Path(__file__).resolve().parents[3]
if __name__=='__main__':
    ctx.prec=384;start=time.monotonic()
    model=Radial(ROOT/'research/baseline/data/state131_independent.json')
    old=json.loads((ROOT/'research/baseline/data/prior_state131_points.json').read_text())
    points=[]
    for record in old['points']:
        x,y=record['x'],record['y'];new=model.evaluate(x,y)
        checks={name:new[name].overlaps(arb(record['fields'][name])) for name in new if name in record['fields']}
        assert all(checks.values()),(x,y,checks)
        points.append({'x':x,'y':y,'fields':{k:v.str(65) for k,v in new.items()},'prior_enclosures_overlap':checks})
        print(x,y,'F',new['residual'].str(30),'Mmin',new['lambda_min_M'].str(25),flush=True)
    result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
            'method':'Independent radial Fourier polynomial recurrence, validated point evaluation',
            'scope':'Individual points, not continuum bounds','elapsed_seconds':time.monotonic()-start,'points':points}
    (ROOT/'research/radial_fourier/verification/state131_points.json').write_text(json.dumps(result,indent=2)+'\n')
