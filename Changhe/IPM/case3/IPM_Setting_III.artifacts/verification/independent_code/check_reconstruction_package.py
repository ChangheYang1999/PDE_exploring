"""Read-only producer package audit, no producer code imported."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,numpy as np
from q_local_checkpoint import QLocalCheckpoint,load_numeric
root=Path('research/reconstruction_package_audit/verification');root.mkdir(parents=True,exist_ok=True)
base=Path('../numerics/artifacts/reconstruction');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
files={}
for n in ['README.md','load_state.py','run_all.sh','SHA256SUMS.txt','RECONSTRUCTION_OUTPUT.txt']:
 p=base/n;raw=p.read_bytes();(root/n).write_bytes(raw);files[n]=sha(p)
states=[]
for line in (base/'SHA256SUMS.txt').read_text().splitlines():
 h,name=line.split(maxsplit=1);p=base/name.lstrip('*');actual=sha(p);assert h==actual;d=load_numeric(p)
 row=dict(file=name,sha256=actual,parameters={k:float(d[k])for k in ['N','M','cl','L','Lf','p','gamma','mu']if k in d and d[k]is not None},keys=sorted(d))
 if 'p'in d:row['map_difference_from_default']=float(d['p'])-1/(1-1/float(d['cl']))
 states.append(row)
assert len(states)==20
srcs=[]
for n in ['ipm3.py','ipm3s.py','ipm3q.py','ipm3ql.py']:
 archive=base.parent/'src'/n;live=base.parent.parent/'src'/n;text=archive.read_text();(root/('source_'+n)).write_text(text);tree=ast.parse(text)
 srcs.append(dict(file=n,archive_sha256=sha(archive),live_sha256=sha(live),same=sha(archive)==sha(live),absolute_live_path_in_archive='numerics/src'in text))
q=QLocalCheckpoint(base/'states/r1C_cl3.0_N64.pt');points=[(.5,.5),(-.5,.5),(.5,-.5),(-.5,-.5),(3.,0.),(0.,3.)];rows=[]
for x,y in points:
 rr=np.hypot(x,y);th=np.clip(np.arctan2(y,x),1e-12,np.pi/2-1e-12);xx=float(rr*np.cos(th));yy=float(rr*np.sin(th));actual=float(q.rho(x,y));clipped=float(q.rho(xx,yy));expected=np.sign(y)*float(q.rho(abs(x),abs(y)))
 assert abs(actual-expected)<1e-10
 rows.append(dict(point=[x,y],actual_density=actual,parity_expected_density=expected,clipped_point=[xx,yy],clipped_density=clipped,absolute_coordinate_error=float(np.hypot(xx-x,yy-y)),absolute_density_error=abs(clipped-actual)))
assert max(r['absolute_density_error']for r in rows)>1
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='COMPUTED',code_sha256=sha(__file__),proof_sha256=sha(root.parent/'PROOF.md'),package_files=files,states=states,sources=srcs,coordinate_checks=rows,verdicts={'manifest':'CONFIRMED, all20 exact hashes','general_full_plane_point_loader':'REFUTED, clipped angle evaluates another point','archived_source_independence':'REFUTED in presence of live path override','historical_bitwise_replay':'OPEN and explicitly disclaimed by producer','continuum_endpoint':'OPEN'})
(root/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
