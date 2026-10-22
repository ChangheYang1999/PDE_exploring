"""Exact finite-basis tail coefficients versus finite-radius samples.

Independent coefficient decoder and long-double endpoint sums, no fitting
routines and no numerical Poisson matrix. All maxima are sampled, not certified.
"""
import json,hashlib,time,sys
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from profile_data import CoefficientProfile,snapshot
from far_coefficients import evaluate

def run():
    start=time.monotonic();stamp=lambda:datetime.now(timezone.utc).isoformat()
    rec={'timestamp_start':stamp(),'method':'Independent Clenshaw decoder, long-double endpoint sums, exact finite trigonometric inverse',
         'warning':'Sampled angles only. Literal stored envelope powers used for finite-radius normalization; PDE matching assumes intended exact powers. No claim of a continuum residual bound.',
         'rows':[]}
    jobs=[('R4_fix3_N112M28.npz','published_gauss_N112'),('R5_fix3_N144M36.npz','published_gauss_N144'),
          ('R6_fix3_N176M44.npz','published_gauss_N176'),('B2_p_gauss_N112.npz','published_beta2_N112')]
    phi=np.linspace(0,np.pi/2,257);dirs=np.column_stack([np.cos(phi),np.sin(phi)])
    rec['angles']=phi.tolist()
    for name,tag in jobs:
        source=Path('../numerics/states')/name
        target=Path('data/control_snapshots')/(tag+'.npz')
        if not target.is_file():
            if not source.is_file():
                rec['rows'].append({'tag':tag,'missing_source':str(source)});continue
            snapshot(source,target)
        obj=CoefficientProfile(target);val=evaluate(obj,phi)
        ampT=float(np.max(np.abs(val['T0'])));ampO=float(np.max(np.abs(val['O0'])))
        row={'tag':tag,'snapshot':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'metadata':obj.metadata(),
             'sampled_T0_max':ampT,'sampled_O0_max':ampO,
             'sampled_T1_matching_defect':float(np.max(abs(val['D_T']))),
             'sampled_O1_matching_defect':float(np.max(abs(val['D_O']))),
             'coefficient_vectors':{k:val[k].tolist() for k in ['A0','A1','B0','B1','omega_sine_modes','stream_sine_modes']},
             'radii':[]}
        tq=3-2*obj.sigma_a;op=2-2*obj.sigma_g
        for r in 10.**np.arange(2,37,2):
            tv=obj.theta(r*dirs)/r**tq;ov=obj.omega(r*dirs)/r**op
            et=float(np.max(abs(tv-val['T0'])));eo=float(np.max(abs(ov-val['O0'])))
            row['radii'].append({'r':float(r),'temperature_abs_leading_error':et,'vorticity_abs_leading_error':eo,
                'temperature_relative_to_global_sampled_amplitude':et/ampT if ampT else None,
                'vorticity_relative_to_global_sampled_amplitude':eo/ampO if ampO else None})
        # A statement about all later sampled radii, never every continuum radius.
        for key in ['temperature','vorticity']:
            errs=[r[key+'_relative_to_global_sampled_amplitude'] for r in row['radii']]
            ok=[i for i in range(len(errs)) if all(e is not None and e<.01 for e in errs[i:])]
            row[key+'_first_radius_below_1pct_at_all_later_samples']=row['radii'][ok[0]]['r'] if ok else None
        stored_d=2*obj.sigma_g-2;stored_alpha=2-stored_d
        modes=2*np.arange(1,len(val['omega_sine_modes'])+1)
        stored_stream=val['omega_sine_modes']/(modes*modes-stored_alpha*stored_alpha)
        row['literal_tail_energy']={'normalizing_power':4-2*stored_d,
            'coefficient':float((2**(4-2*stored_d)-1)/(4-2*stored_d)*np.pi*
                np.sum((modes*modes+stored_alpha*stored_alpha)*stored_stream**2)),
            'interpretation':'Exact finite-basis asymptotic form evaluated in floating arithmetic, with the literal stored exponent; no interval certificate.'}
        rec['rows'].append(row)
    rec['timestamp_end']=stamp();rec['elapsed_seconds']=time.monotonic()-start
    rec['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path('runs/tail_onset.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps({'elapsed_seconds':rec['elapsed_seconds'],'rows':[{k:v for k,v in r.items() if k not in ['radii','coefficient_vectors']} for r in rec['rows']]},indent=2))
if __name__=='__main__':run()
