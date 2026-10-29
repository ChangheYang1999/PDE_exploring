#!/usr/bin/env python3
from pathlib import Path
import datetime,json,time
import numpy as np
from independent_farfield import asymptotic_fixture
from independent_pressure import GreenPoisson
ROOT=Path(__file__).resolve().parents[1]

def run():
    start=time.time();records=[]
    radii=np.array([32.,128.,512.,2048.]);mu=np.linspace(-.99,.99,41)
    r=radii[:,None]*np.sqrt(1-mu**2);z=radii[:,None]*mu
    for a in [.5,.8,1.]:
        row={'alpha':a,'radii':radii.tolist()}
        for corrected in [False,True]:
            f,d=asymptotic_fixture(a,corrected=corrected)
            red=f.reduced(r,z)
            pressure=GreenPoisson(f.source,decay_power=2*a,lmax=24,nangle=56,nradial=40)
            p,g=pressure.on_spheres(radii,mu)
            primitive=f.primitive_cylindrical(r,z,g)
            label='corrected' if corrected else 'uncorrected'
            row[label]={'q_scaled_max':(radii**(2*a+2)*np.max(np.abs(red['q']),axis=1)).tolist(),
                        'eta_scaled_max':(radii**(2*a+3)*np.max(np.abs(red['eta']),axis=1)).tolist(),
                        'primitive_scaled_max':(radii**(2*a+1)*np.max(np.linalg.norm(primitive,axis=-1),axis=1)).tolist()}
            if corrected:
                row['potential_remainder']=np.max(np.abs(d['A1_remainder'])).item()
                row['angular_meridional_error']=float(np.max(np.abs((d['GV']-(2*a-1)*d['A1']).coef)))
        row['passed']=row['potential_remainder']<1e-12 and row['angular_meridional_error']<1e-12
        for key in ['q_scaled_max','eta_scaled_max','primitive_scaled_max']:
            row['passed']=bool(row['passed'] and row['corrected'][key][-1]<.01*row['uncorrected'][key][-1] and row['corrected'][key][-1]<row['corrected'][key][0])
        records.append(row);print(json.dumps(row),flush=True)
    out={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,'records':records,'all_passed':all(x['passed'] for x in records)}
    (ROOT/'results/corrected_tail_tests.json').write_text(json.dumps(out,indent=2)+'\n')
    raise SystemExit(0 if out['all_passed'] else 1)
if __name__=='__main__':run()
