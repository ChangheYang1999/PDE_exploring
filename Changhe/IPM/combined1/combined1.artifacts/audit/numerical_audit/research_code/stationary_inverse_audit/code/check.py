"""Reproduce T4's finite inverse and small divisor from N4 coefficients."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from math import gcd
import json, sys, time
from flint import fmpq as Q, arb, ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/stationary_inverse_audit'
sys.path.insert(0,str(ROOT/'research/sector_audit/code'))
from sectors_flint import dx,dy,aq
sys.set_int_max_str_digits(0)
def H(p):return sha256(p.read_bytes()).hexdigest()
start=time.monotonic();ctx.prec=768
output=BASE/'verification/results.json';assert not output.exists()
peerpath=BASE/'source/T4_results.json';peer=json.loads(peerpath.read_text())
assert H(BASE/'source/T4_PROOF.md')==peer['hashes']['PROOF.md']
assert H(BASE/'source/T4_check.py')==peer['hashes']['code/check.py']
assert H(BASE/'source/T4_order8_selected.json')==peer['hashes']['data/order8_selected.json']
p,q=4076476460239181,2251799813685248
c=Q(p,q);delta=1-1/c;assert gcd(p,p-q)==1
rows=[];count=0
for j in range(17):
 s=4-(j+1)*delta;pivots=[]
 for n in range(0,20*(j+1),2):
  image={k:-v for k,v in dy({n:s*s-n*n},s-2,'c').items()}
  expected=-s*s*(s-2) if n==0 else -(s*s-n*n)*(s-2-n)/2
  assert image[n+1]==expected and expected!=0
  pivots.append(abs(expected));count+=1
 value=aq(min(pivots));old=peer['pivots'][j]
 assert old['order']==j and Q(old['s'])==s and old['dimension']==len(pivots)
 assert value.overlaps(arb(old['smallest_pivot']))
 rows.append({'order':j,'dimension':len(pivots),'s':str(s),'minimum_diagonal':value.str(90),'peer_overlap':True})
source=ROOT/'research/sector_audit/verification/stationary_principal.json'
data=json.loads(source.read_text());row=next(r for r in data['branches'] if r['index']==8)
C={int(k):Q(v) for k,v in row['potential_cos'].items()};s=4-9*delta
assert Q(row['residual_exponent'])==s-3
selected=json.loads((BASE/'source/T4_order8_selected.json').read_text())
assert all(C[int(k)]==Q(v) for k,v in selected['potential_cos'].items())
G={k:-v for k,v in dy({n:(s*s-n*n)*v for n,v in C.items()},s-2,'c').items()}
stream=dy(dx(C,s,'c'),s-1,'c')
a=-s*s*(s-2)*C[0];b=s*(s*s-4)*C[2]/2
x=s*(s-2)*C[0]/2;y=-(s+4)*(s+2)*C[4]/4
assert G[1]==a+b==Q(row['stationary_density_sin']['1'])==Q(selected['density_sin1'])
assert stream[2]==x+y
values={'pure_mode_velocity_amplification':(1+aq((s-2)**2)/4).sqrt()/abs(aq(s)),
        'density_C0_contribution':aq(a),'density_C2_contribution':aq(b),
        'stream_C0_contribution':aq(x),'stream_C4_contribution':aq(y),'stream_mode2_sum':aq(x+y)}
assert all(v.overlaps(arb(peer['order8'][k])) for k,v in values.items())
assert count==1530
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
     'source_sha256':H(source),'peer_result_sha256':H(peerpath),'code_sha256':H(Path(__file__)),
     'proof_sha256':H(BASE/'PROOF.md'),'angular_code_sha256':H(ROOT/'research/sector_audit/code/sectors_flint.py'),
     'all_1530_pivots_exactly_checked':True,'pivots':rows,
     'order8':{'s':str(s),**{k:v.str(95) for k,v in values.items()}},
     'six_order8_peer_overlaps':True,'selected_coefficients_equal_independent_N4_source':True,
     'elapsed_seconds':time.monotonic()-start,
     'scope':'Finite angular inverse and local homogeneous diagnostic. No infinite-series or full-plane norm conclusion.'}
output.write_text(json.dumps(out,indent=2)+'\n')
print('pivots',count,'amplification',values['pure_mode_velocity_amplification'].str(35),'seconds',out['elapsed_seconds'])
