"""One extra exact nodal state, using the proved full-plane finite moment."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
from flint import ctx
from certify import moment,binary,tensor_coefficients,export,load,ROOT
ctx.prec=192
src=Path(sys.argv[1]).resolve();target=ROOT/'data'/(src.stem+'.json');export(src,target);o,b,p,jhash=load(target)
assert all(x==1 for x in b[0]);co=tensor_coefficients(b);L=binary(p['L']);cl=binary(p['c_l']);beta=binary(p['beta'])
assert L>0 and cl>1 and abs(beta)<1
c64=moment(co,L,cl,beta,64);c96=moment(co,L,cl,beta,96);assert (c64-c96).contains(0);defect=3*cl-1-c96
row={'date':datetime.now(timezone.utc).isoformat(),'source':str(src),'source_sha256':o['source_sha256'],'source_md5':hashlib.md5(src.read_bytes()).hexdigest(),'exact_json':str(target),'json_sha256':jhash,'N':o['N'],'M':o['M'],'c64':c64.str(40),'c96':c96.str(40),'c_midpoint_float':float(c96.mid()),'self_consistency_ball':defect.str(40),'self_consistency_contains_zero':defect.contains(0),'self_consistency_midpoint_float':float(defect.mid()),'dependencies':[{'file':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in [Path(__file__),ROOT/'code/certify.py',ROOT/'PROOF.md',ROOT.parent/'inner-cutoff/code/hessian.py',ROOT.parent/'exact-data/code/nodal_input.py']],'scope':'Rigorous full-plane center strain of this exact binary ideal-node field only.'}
(ROOT/'verification'/(src.stem+'_certificate.json')).write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row,indent=2))
