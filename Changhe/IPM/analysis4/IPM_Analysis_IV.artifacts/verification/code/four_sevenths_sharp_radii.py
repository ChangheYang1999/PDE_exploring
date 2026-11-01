"""Exact prefix boxes using independently certified delta4/7 response minima."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from certified_prefix_majorant import PrefixMajorant,direct_scalar
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT=Path('research/247_four_sevenths_exact_minima')
OLD=Path('research/239_four_sevenths_two_mode/verification')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def read(path):
 raw=path.read_bytes();return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def save(path,obj):
 raw=json.dumps(clean(obj),separators=(',',':')).encode();path.write_bytes(gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw)
def receipt(path):return dict(path=str(path),sha256=sha256(path.read_bytes()).hexdigest())
def lower(v):
 m,e,r,re=v;return abs(F(m)*F(2)**e)-F(r)*F(2)**re

def main():
 begin=time.monotonic();replay='--replay' in sys.argv;rows=[]
 for i,s in enumerate([F(347,10**9),F(109,5*10**7),F(1182,25)],1):
  start=time.monotonic();oldpath=OLD/f'root{i}_box.json.gz';old=read(oldpath);oldreview=read(OLD/f'root{i}_review.json');assert oldreview['all_checks_pass']
  minimum=ROOT/f'verification/root{i}.json.gz';mn=read(minimum);mr=read(ROOT/f'verification/root{i}_replay.json.gz');assert mn['all_checks_pass'] and mr['all_checks_pass'] and mr['construction_sha256']==sha256(minimum.read_bytes()).hexdigest();assert lower(mn['target'])>s
  assert (old['h'],old['Q'],old['B'],old['N'])==(2,7,4,7) and old['initial_harmonics']==[]
  density=list(map(F,old['initial_density']));L=F(147,80);kap=F(48,7);m=PrefixMajorant(2,7,4,density,[],s,L,kap)
  path=ROOT/f'verification/root{i}_radius.json.gz'
  if not replay:
   best=None;attempts=[]
   for q in range(old['adaptive']['q'],0,-1):
    found,record=try_box(m,q);attempts.append(record)
    if found is None:break
    best=dict(q=q,box=found['box'],image=found['image'],iterations=record['iterations'])
   assert best is not None
   data=dict(checked_at_utc=stamp(),all_checks_pass=True,h=2,Q=7,B=4,N=7,s=s,L=L,kappa=kap,initial_density=density,initial_harmonics=[],constant=m.constant,J=m.J,Y0=m.Y0,adaptive=best,attempts=attempts,sources=[receipt(oldpath),receipt(minimum)],actual_elapsed_s=time.monotonic()-start)
   save(path,data)
  else:
   data=read(path);assert data['all_checks_pass'] and F(data['s'])==s
   assert data['initial_density']==old['initial_density'] and data['initial_harmonics']==[]
   for source in data['sources']:assert sha256(Path(source['path']).read_bytes()).hexdigest()==source['sha256']
   direct_scalar(m,2)
   assert list(map(F,data['constant']))==m.constant and [list(map(F,row)) for row in data['J']]==m.J and list(map(F,data['Y0']))==m.Y0
   q=data['adaptive']['q'];box=list(map(F,data['adaptive']['box']));image=m.transformed(F(1,2**q),box)
   assert image==list(map(F,data['adaptive']['image'])) and all(0<=v<=y and y>=y0 for v,y,y0 in zip(image,box,m.Y0))
   save(ROOT/f'verification/root{i}_radius_replay.json',dict(checked_at_utc=stamp(),all_checks_pass=True,root=i,q=q,radius_exponent=F(q,4),exact_scalar_identities=42,minimum_lower_bound=s,box_receipt=receipt(path),actual_elapsed_s=time.monotonic()-start))
  row=dict(root=i,q=data['adaptive']['q'],radius_exponent=F(data['adaptive']['q'],4),minimum_lower_bound=s,actual_elapsed_s=time.monotonic()-start);rows.append(row);print(json.dumps(clean(row)),flush=True)
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,replay=replay,rows=rows,actual_elapsed_s=time.monotonic()-begin);save(ROOT/('verification/radii_replay.json' if replay else 'verification/radii_checks.json'),out)
 (ROOT/'sources/four_sevenths_sharp_radii.py').write_bytes(Path('code/four_sevenths_sharp_radii.py').read_bytes());print(json.dumps(clean(out)),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)]);save(ROOT/'verification/radii_FAILURE.json',out);print(json.dumps(out),flush=True);raise SystemExit(1)
