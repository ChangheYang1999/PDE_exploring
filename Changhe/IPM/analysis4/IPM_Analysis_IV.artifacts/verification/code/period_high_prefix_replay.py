"""Exact reassembly of all longer-prefix rational radius certificates."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from certified_prefix_majorant import PrefixMajorant,direct_scalar
from resonance_block_majorant import clean
ROOT=Path('research/261_period_seven_eight_prefixes')
def decode(p):
 raw=p.read_bytes();return raw,json.loads(gzip.decompress(raw))
def upper(p,absolute=False):
 mid=F(p[0])*F(2)**p[1];rad=F(p[2])*F(2)**p[3];assert rad>=0
 return (abs(mid) if absolute else mid)+rad
ap=argparse.ArgumentParser();ap.add_argument('--Q',type=int,required=True);ap.add_argument('--root',type=int,required=True);a=ap.parse_args();start=time.monotonic()
p=ROOT/f'verification/Q{a.Q}_root{a.root}_checks.json.gz';raw,d=decode(p);assert d['all_checks_pass'] and d['Q']==a.Q and d['root_index']==a.root
for entry in d['inputs']+[d['exact_prefix']]:assert sha256(Path(entry['path']).read_bytes()).hexdigest()==entry['sha256']
norms={v['n']:v for v in d['norms']};hs={v['n']:v for v in d['harmonics']};rows=[]
for row in d['cases']:
 bp=Path(row['box']['path']);br,b=decode(bp);assert sha256(br).hexdigest()==row['box']['sha256'];Q=a.Q;N=row['N'];delta=F(2,Q)
 assert (b['h'],b['Q'],b['B'],b['N'])==(1,Q,4,N) and F(b['s'])==F(d['s'])
 assert F(b['L'])==F(3*Q*Q,4*(3*Q-1)) and F(b['kappa'])==4*(2-delta+max(delta,1-delta))*(1-delta)/delta*F(N+1,N)
 density=list(map(F,b['initial_density']));harmonics=list(map(F,b['initial_harmonics']));assert len(density)==N and len(harmonics)==N//Q-1 and harmonics[0]==0
 for n,bound in enumerate(density,1):assert bound==F(norms[n]['density_bound']) and bound>n*upper(norms[n]['F'])
 for j,bound in enumerate(harmonics[1:],2):assert bound==F(hs[j*Q]['bound']) and bound>j*Q*upper(hs[j*Q]['H'],True)
 m=PrefixMajorant(1,Q,4,density,harmonics,F(b['s']),F(b['L']),F(b['kappa']));direct_scalar(m,2)
 assert m.constant==list(map(F,b['constant'])) and m.J==[list(map(F,r)) for r in b['J']] and m.Y0==list(map(F,b['Y0']))
 q=b['adaptive']['q'];v=list(map(F,b['adaptive']['box']));image=m.transformed(F(1,2**q),v)
 assert q==row['q'] and image==list(map(F,b['adaptive']['image'])) and all(y<=z and 0<=w<=z for y,z,w in zip(m.Y0,v,image))
 rows.append(dict(N=N,q=q,radius_exponent=F(q,2),box=row['box'],exact_scalar_identities=6*Q))
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,Q=a.Q,root_index=a.root,maximum_order=d['maximum_order'],cases=rows,source=dict(path=str(p),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-start)
(ROOT/f'verification/Q{a.Q}_root{a.root}_review.json').write_text(json.dumps(clean(out),indent=2)+'\n');(ROOT/'sources/period_high_prefix_replay.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(clean(out)),flush=True)
