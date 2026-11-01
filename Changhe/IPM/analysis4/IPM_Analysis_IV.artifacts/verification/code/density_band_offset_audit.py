"""Compare the stated and implemented density distances using exact membership."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip,json,time,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
start=time.monotonic();ctx.prec=640
source=Path('research/64_log_precision_updates/verification/log_sin1_c3_p512_N320_20261031T084011Z/selected_packed_coefficients.json.gz')
raw=gzip.decompress(source.read_bytes());data=json.loads(raw)
assert data['delta']=='2/3'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
root=Path('research/75_diagonal_mass/verification')/('density_offset_'+stamp)
(root/'sources').mkdir(parents=True)
peer=Path('../a4-num/code/diagonal_bands.py').read_bytes()
report=Path('../a4-num/notes/bands_320.txt').read_bytes()
assert b'bf = bands(F[q], q, nd, 3, 2)' in peer
(root/'sources/peer_diagonal_bands.py.txt').write_bytes(peer)
(root/'sources/peer_bands_320.txt').write_bytes(report)
rows=[];comparisons=0;count=0
printed={}
for line in report.decode().splitlines():
 parts=line.split('|')
 if len(parts)==3 and parts[0].strip().isdigit():
  printed[int(parts[0])]=[v for v in parts[1].split()]
for q in sorted(printed):
 col=data['f']['320'][q];tot=arb(0);old=[arb(0) for _ in range(3)];correct=[arb(0) for _ in range(3)]
 for k,packed in enumerate(col):
  value=abs(arb(*unpack(packed)));tot+=value;count+=1
  for offset,bands in [(3,old),(4,correct)]:
   distance=abs(3*(2*k+offset)-640)
   b=(0 if distance<=6 else 2) if q==0 else (0 if 4*distance<=3*q else 1 if distance<=3*q else 2)
   bands[b]+=value
 assert tot>0
 old=[v/tot for v in old];correct=[v/tot for v in correct]
 for value,text in zip(old,printed[q]):
  assert abs(value-arb(text))<arb('0.000500000001'),(q,value,text)
  comparisons+=1
 rows.append(dict(q=q,implemented_offset3=[v.str(30,radius=True) for v in old],stated_offset4=[v.str(30,radius=True) for v in correct],printed=printed[q],stated_excludes_printed_rounding=[bool(abs(v-arb(t))>arb('0.0005')) for v,t in zip(correct,printed[q])]))
assert any(any(row['stated_excludes_printed_rounding']) for row in rows)
record=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),source_path=str(source),source_uncompressed_sha256=sha256(raw).hexdigest(),checkpoint_sha256=data['checkpoint_sha256'],precision_bits=640,coefficient_positions=count,printed_comparisons=comparisons,all_implemented_offset_comparisons_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
(root/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
for name in ['density_band_offset_audit.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
manifest={str(p.relative_to(root)):{'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()} for p in root.rglob('*') if p.is_file()}
(root/'MANIFEST.json').write_text(json.dumps({'files':manifest},indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),**record),indent=2))
