"""Exact rational reassembly of the sharper sin17 supersolution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time
sys.dont_write_bytecode=True
from certified_prefix_majorant import PrefixMajorant,direct_scalar
from resonance_block_majorant import clean
ROOT=Path('research/255_seventeen_exact_minimum')
start=time.monotonic();p=ROOT/'verification/checks.json.gz';raw=p.read_bytes();data=json.loads(gzip.decompress(raw));assert data['all_checks_pass'] and data['minimizing_index']==2380
bp=Path(data['box']['path']);br=bp.read_bytes();assert sha256(br).hexdigest()==data['box']['sha256'];b=json.loads(gzip.decompress(br))
assert (b['h'],b['Q'],b['B'],b['N'])==(3,13,18,13)
assert F(b['s'])==F(data['s'])==F(277,10**14) and F(b['L'])==F(507,152) and F(b['kappa'])==F(7938,169)
m=PrefixMajorant(3,13,18,list(map(F,b['initial_density'])),[],F(b['s']),F(b['L']),F(b['kappa']));direct_scalar(m,2)
assert m.constant==list(map(F,b['constant'])) and m.J==[list(map(F,r)) for r in b['J']] and m.Y0==list(map(F,b['Y0']))
q=b['adaptive']['q'];bx=list(map(F,b['adaptive']['box']));image=m.transformed(F(1,2**q),bx)
assert q==data['q'] and image==list(map(F,b['adaptive']['image'])) and all(y<=z and 0<=v<=z for y,z,v in zip(m.Y0,bx,image))
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,q=q,s=b['s'],radius_exponent=F(q,6),amplitude_exponent=F(13,6),exact_scalar_identities=78,box_reassembled=True,input=dict(path=str(p),sha256=sha256(raw).hexdigest()),box=data['box'],actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/review.json').write_text(json.dumps(clean(out),indent=2)+'\n');(ROOT/'sources/seventeen_minimum_box_replay.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(clean(out)),flush=True)
