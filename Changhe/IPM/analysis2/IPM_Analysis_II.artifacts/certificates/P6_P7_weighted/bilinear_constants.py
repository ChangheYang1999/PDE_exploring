from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from flint import arb,ctx
import json
ctx.prec=256
s=arb(11)/5
assert arb(64)**s<2**14
assert (arb(5)/2+s)*arb(64)**s<2**17
assert (arb(5)/2+s)*arb(2)**s<2**6
assert 9000*2**12<2**26
assert 2000*4<2**14
assert 1-arb(2)**(-arb(4)/5)>arb(1)/4
assert 9*2**23+2**28+2**15<2**29
assert 24*2**29<2**34
assert 216<15**2 and 226<16**2
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':256,'weighted_velocity_bound':2**35,'bilinear_Hstar_bound':2**39,'neighbor_source_bound':2**17,'neighbor_output_bound':2**6,'outer_block_bound':2**26,'inner_block_bound':2**14,'cylinder_embedding':'sqrt(6)','multiplier_constant':'15','all_rounding_checks':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
