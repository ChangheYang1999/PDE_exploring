from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import json
ctx.prec=384
rows=[]
for sn,sd,mn,md,margin,inverse in [(1,1,27,10,'5/2','2/5'),(2,1,4,5,'3/5','5/3'),(11,5,2,5,'1/5','5')]:
 s=arb(sn)/sd
 C=arb(32+65536)+s*(9*32+2*32+arb(32768)/arb(2).sqrt())+arb(2)**53*65536
 error=C*(arb(2)**179)**(-arb(2)/5)
 assert error<arb(1)/5
 baseline=arb(mn)/md
 exactlow=baseline-error
 a,b=map(int,margin.split('/'));assert exactlow>arb(a)/b
 rows.append({'s':f'{sn}/{sd}','baseline':f'{mn}/{md}','C_upper':str(C),'R':'2^179','error':str(error),'coercivity_lower':str(exactlow),'rounded_margin':margin,'inverse_bound':inverse})
 # Threshold for error < baseline/2.
 log2threshold=((2*C/baseline).log()/arb(2).log())*arb(5)/2
 rows[-1]['log2_R_threshold_for_half_baseline']=str(log2threshold)
 if sn==11:
  assert log2threshold>178 and log2threshold<179
  assert C*(arb(2)**178)**(-arb(2)/5)>arb(1)/5
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,'rows':rows,'scope':'Sufficient bound for the original exact backgrounds, not for an uncertified repaired background.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
