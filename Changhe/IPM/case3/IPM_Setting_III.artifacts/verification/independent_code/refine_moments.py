import json,time,argparse
from pathlib import Path
from datetime import datetime,timezone
from candidate_reader import Candidate
from candidate_moments import strain
ap=argparse.ArgumentParser();ap.add_argument('--tag',default='_corrected');ap.add_argument('--files',nargs='+');args=ap.parse_args()
out=[]
for stem in args.files or ['coupled_N48_a1','res_p23_N96M16','res_p23_N192M24','res_p23_N256M32']:
 c=Candidate('evidence/'+stem+'.npz',project_center=True)
 checks=[strain(c,n,128,1e-16,16.) for n in [128,256,512]]
 row={'utc':datetime.now(timezone.utc).isoformat(),'checkpoint':c.meta,'checks':checks}
 out.append(row);print(json.dumps(row),flush=True)
Path('evidence/candidate_moments_refined'+args.tag+'.json').write_text(json.dumps(out,indent=2)+'\n')
