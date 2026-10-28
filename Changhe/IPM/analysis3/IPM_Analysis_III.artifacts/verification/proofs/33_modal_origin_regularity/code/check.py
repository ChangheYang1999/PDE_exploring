from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
import numpy as np
P=Path(__file__).resolve().parents[1];R=P.parents[1]
s=R/'research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
with np.load(s,allow_pickle=False) as f:
 M=int(f['M']);d=Q(float(f['D'][M-1,0]));bi=Q(float(f['bi']));tm=Q(float(f['knots'][0]));assert M==260 and d!=0 and bi>50
out={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','source':str(s.relative_to(R)),'source_sha256':hashlib.sha256(s.read_bytes()).hexdigest(),'top_mode':M-1,'degree_five_angular_frequency':2*(M-1)+3,'coefficient_before_positive_exp_factor':str(d/8),'positive_exp_factor':'exp(-2*t_minus)','t_minus':str(tm),'bi':str(bi),'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest()}
(P/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
