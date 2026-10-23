"""Confirm exact saved density identity for result187 extension; no producer imports."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,numpy as np
from q_local_checkpoint import QLocalCheckpoint
r=Path('research/hydrostatic_state_audit/verification')
tags=['hsB_cl2.5chain_N96','hsC_c3.0_N64_fine','hsC_c3.0_N96_fine','hsC_c2.0_N64_fine','hsC_cl3chain_N64_fine','hsD_c3.0_N64_keep','hsD_c3.0_N96_keep','hsD_c3.0_N64_keep_fine','hsD_c3.0_N64_keep_cfree']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for tag in tags:
 p=r/'states'/(tag+'.pt'); live=Path('../numerics/runs')/(tag+'.pt')
 a,b=QLocalCheckpoint(p),QLocalCheckpoint(live)
 scalar={k:getattr(a,k)==getattr(b,k)for k in ['N','M','basis','L','kappa','cl']}
 u=np.array_equal(a.u,b.u);nodes=np.array_equal(a.tk,b.tk)
 assert all(scalar.values())and u and nodes
 assert 'tk'in a.data and 'basis_nodes'in a.data and 'inverse_options'in a.data
 row=dict(tag=tag,frozen_sha256=sha(p),live_sha256=sha(live),scalar_identity=scalar,u_bit_equal=u,nodes_bit_equal=nodes,basis_nodes_source=a.meta['basis_nodes_source'],basis_nodes=str(a.data['basis_nodes']),inverse_options=a.data['inverse_options'],verdict='CONFIRMED same finite density with explicit stored nodes')
 rows.append(row)
out=dict(utc=datetime.now(timezone.utc).isoformat(),code_sha256=sha(Path(__file__)),states=rows)
(r/'METADATA_EXTENSION.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['utc'],'PASS',len(rows),'metadata identity checks')
