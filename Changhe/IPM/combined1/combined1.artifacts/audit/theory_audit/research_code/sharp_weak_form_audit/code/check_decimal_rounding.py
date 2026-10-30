from pathlib import Path
from flint import arb,ctx
import json,hashlib
from datetime import datetime,timezone
ctx.prec=512
root=Path(__file__).resolve().parents[1]
p=root/'source/weighted_weak_sharp_results.json'
data=json.loads(p.read_text());rows=[]
for kind,ls in data.items():
    for x in ls:
        I=abs(arb(x['pairing']));M=arb(x['M']);C=arb(x['C']);H=arb(x['H_upper'])
        cu=arb(2) if x['a']=='1' else arb(808233)/500000
        D=M+cu*C;r=2*I/(D+(D*D+4*cu*H*I).sqrt());stored=arb(x['m_lower'])
        state='above_formula_upper' if stored>r else ('below_formula_lower' if stored<r else 'overlap')
        rows.append({'kind':kind,'candidate':x['candidate'],'a':x['a'],'k':x.get('k'),'stored_m_lower':x['m_lower'],'formula':r.str(45),'verdict':state})
print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rows':rows},indent=2))
