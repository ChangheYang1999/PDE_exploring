from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
from flint import fmpq as Q,arb,ctx
B=Path(__file__).resolve().parents[1]
def ar(q):q=Q(q);return arb(q.numerator)/arb(q.denominator)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ctx.prec=512;start=time.monotonic();s,t=Q(1,262144),Q(1,5184);ea,ew=Q(1,1572864),Q(4207,20000000)
assert 0<s<t and t<=Q(1,2) and s<Q(1,34)
rows=[]
for e in [None,3,6,12,100,11500]:
 K=0 if e is None else 10**e
 kappa=2*((arb(2*K*K+16410)**ar(t/2))+ar(34*t))/ar(1-34*s)
 enlargement=ar(ew/ea)/kappa
 if e==6:assert enlargement>ar(Q(4097,25))
 if e==11500:assert enlargement>1
 rows.append({'K_label':'0' if e is None else f'10^{e}','kappa':kappa.str(100),'threshold_enlargement':enlargement.str(100)})
 print(rows[-1]['K_label'],kappa.str(30),enlargement.str(30))
inputs=[B/'PROOF.md',Path(__file__),*sorted((B/'source').iterdir())]
out={'utc':datetime.now(timezone.utc).isoformat(),'s_exact':str(s),'t_exact':str(t),'eta_A_exact':str(ea),'eta_w_exact':str(ew),'inputs':{str(p):sha(p) for p in inputs},'rows':rows,'strict_factor_163_88_at_K_1e6':True,'strict_factor_above_one_at_K_10power11500':True,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED conditional forcing-test conversion; no background or existence conclusion'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('DONE',out['utc'],out['elapsed_seconds'])
