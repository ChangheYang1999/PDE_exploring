"""Reproduce the lead's tightened norm inputs after the independent minima audit."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from general_rational_majorant import RationalMajorant
from general_component_radius import stringify
ROOT=Path('research/164_four_ninths_response_minima')
start=time.monotonic();rows=[]
for index,(a,q) in enumerate(zip(map(F,['133/125','1153/1000','127/100','1423/1000','2857/1000']),[211,201,206,187,160]),1):
 path=ROOT/'verification'/f'root{index}_certificate.json.gz'
 data=json.loads(gzip.decompress(path.read_bytes()));I=list(map(F,data['root_interval']))
 assert a>1+max(map(abs,I))
 m=RationalMajorant(2,9,4,a,F(data['uniform_lower_bound']));box=[2*x for x in m.Y0]
 image=m.transformed(F(1,2**q),box);previous=m.transformed(F(1,2**(q-1)),box)
 assert all(x<y for x,y in zip(image,box));assert any(x>=y for x,y in zip(previous,box))
 row=dict(root_index=index,a=a,s=m.s,q=q,radius_exponent=F(9*q,4),box=box,image=image,previous_image=previous,maximum_ratio=max(x/y for x,y in zip(image,box)))
 rows.append(row)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/sharp_input_radius_replay.json').write_text(json.dumps(stringify(result),indent=2)+'\n')
(ROOT/'sources/sharp_response_radius_replay.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(dict(all_checks_pass=True,q=[r['q'] for r in rows],actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
