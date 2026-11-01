"""Compare the independent polar log with directed Cartesian responses and tuning."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re,time
from flint import arb,ctx
from extremal_single_probe import ExtremalResponse
from unpack_dyadic4 import unpack
from certified_initial_majorants import pack
ROOT=Path('research/241_single_seven_four_fifths')
def tol(text):
 mantissa,exponent=text.lower().split('e');places=len(mantissa.split('.')[1]);return arb('0.51')*arb(10)**(int(exponent)-places)
start=time.monotonic();ctx.prec=1024
path=Path('../a4-lead/code/tuned/hh_tune_Q5h2_sin7.out');raw=path.read_bytes();text=raw.decode();sigmas={int(k):v for k,v in re.findall(r'k=(\d+) .*?sigma_k = ([+-]?[0-9.]+e[+-]\d+)',text)}
Hs={int(n):v for n,v in re.findall(r'H_(\d+) = ([+-]?[0-9.]+e[+-]\d+)',text)}
probe_path=Path('research/231_extremal_single_harmonics/verification/h2_Q5_probe.json');probe=json.loads(probe_path.read_text());assert len(sigmas)>=5 and all(n in Hs for n in [5,10,15,20])
comparisons=[]
for k in range(1,6):
 value=arb(*unpack(probe['rows'][k-1]['enclosure']));assert value.overlaps(arb(sigmas[k],tol(sigmas[k])));comparisons.append(dict(k=k,printed=sigmas[k],enclosure=pack(value)))
r=ExtremalResponse(2,5);t=r.solver;harmonics=[]
for n in range(5,21):
 fn=r.f[n] if n==5 else t.order(n,r.f,r.g)
 if t.resonant(n):
  fn=fn.project(t.B*n-1,1,t.counts,zero_mode=t.frequency(n)-1);r.f[n]=fn
  R=t.continuation(n,r.f,r.g,arb(0));S=t.continuation(n,r.f,r.g,arb(1))-R;assert not S.contains(0)
  H=-R/S;r.g[n]=t.poisson(fn,n,H);assert H.overlaps(arb(Hs[n],tol(Hs[n])))
  assert S.overlaps(arb(*unpack(probe['rows'][n//5-1]['enclosure'])))
  harmonics.append(dict(n=n,H=pack(H),H_display=H.str(55,radius=True),printed=Hs[n],sigma=pack(S)))
 else:r.f[n]=fn;r.g[n]=t.poisson(fn,n)
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,arithmetic_bits=1024,response_comparisons=comparisons,harmonic_comparisons=harmonics,source=dict(path=str(path),sha256=sha256(raw).hexdigest()),probe=dict(path=str(probe_path),sha256=sha256(probe_path.read_bytes()).hexdigest()),actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/polar_comparison.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/lead_polar_sin7.out').write_bytes(raw);(ROOT/'sources/single_seven_polar_comparison.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in out.items() if k not in ['response_comparisons','harmonic_comparisons']}),flush=True)
