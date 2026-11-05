"""Own resumable far cache; never writes the inherited modal source cache."""
import json,math,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
import residual_modal_screen as rm
OUT=HERE/'far_radial_cache.json'
def run():
    tick=time.monotonic();rm.initialize(384)
    data=json.loads(OUT.read_text())if OUT.exists()else{'status':'ARB_RESOLVED_COEFFICIENTS_FLOAT_CACHE','precision':384,'rows':[]}
    old={q['r']for q in data['rows']}
    tasks=np.geomspace(64.,1e10,337)
    for i,r in enumerate(tasks):
        if float(r)in old:continue
        data['rows'].append(rm.row((float(r),0.)))
        data['rows'].sort(key=lambda q:q['r']);OUT.write_text(json.dumps(data)+'\n')
        if i%8==0:print('far_rows',len(data['rows']),'r',r,'seconds',time.monotonic()-tick,flush=True)
    data['elapsed_seconds']=time.monotonic()-tick;OUT.write_text(json.dumps(data)+'\n')
if __name__=='__main__':run()
