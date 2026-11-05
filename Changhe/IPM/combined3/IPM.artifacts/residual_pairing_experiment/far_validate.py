"""READONLY authoritative evaluator at large radii; exact F before float."""
import json,math,sys,time
from pathlib import Path
from flint import arb
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
import residual_modal_screen as rm

def run():
    tick=time.monotonic();rm.initialize(384)
    asym=json.loads((HERE/'exact_far_result.json').read_text())
    lead=asym['powers'][0];p=lead['power'];a={c['n']:c['float'] for c in lead['coefficients']}
    out={'status':'ARB_POINT_EVALUATION_FLOAT_COMPARISON','leading_power':p,'rows':[]}
    for r in [64.,128.,256.,512.,1e3,1e4,1e5,1e6,1e8,1e10,1e14]:
        row=rm.row((r,0));fv=row['F'];scaled=[v/r**p for v in fv]
        error=math.sqrt(math.pi*sum((v-a.get(2*i+1,0.))**2 for i,v in enumerate(scaled)))
        norm=math.sqrt(math.pi*sum(v*v for v in scaled))
        result={'r':r,'scaled_angular_L2':norm,'leading_coefficient_L2':lead['angular_l2_coefficient'],'scaled_remainder_L2':error,'leading_n111':a[111],'scaled_n111':scaled[55],'radial_arb_error':row['radial_roundoff'],'F':fv,'Fr':row['Fr'],'Frr':row['Frr']}
        out['rows'].append(result)
        print({k:v for k,v in result.items()if k not in ['F','Fr','Frr']},flush=True)
        (HERE/'far_validation.json').write_text(json.dumps(out,indent=2)+'\n')
    out['elapsed_seconds']=time.monotonic()-tick
    (HERE/'far_validation.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
