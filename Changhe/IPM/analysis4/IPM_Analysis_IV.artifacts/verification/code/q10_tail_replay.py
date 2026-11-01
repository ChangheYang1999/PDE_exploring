"""Fraction-only response inequalities and exact scalar/box replay for topic294."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import comb
import gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from certificate_admission import read,ref,checkref
from certified_prefix_majorant import PrefixMajorant,direct_scalar
from resonance_block_majorant import clean
ROOT=Path('research/294_q10_tail_prefix');BASE=Path('research/282_period_ten_symbolic_response/verification')
def shift(coeffs,K):
 out=[F(0) for _ in coeffs]
 for i,c in enumerate(map(F,coeffs)):
  for j in range(i+1):out[j]+=c*comb(i,j)*K**(i-j)
 return out

def mul(A,B):
 v=[a*b for a in A for b in B];return min(v),max(v)
def evaluate(coeffs,I):
 value=(F(0),F(0))
 for c in reversed(coeffs):
  a,b=mul(value,I);value=(a+c,b+c)
 return value

def upper(v,absolute=False):
 m=F(v[0])*F(2)**v[1];r=F(v[2])*F(2)**v[3];assert r>=0
 return (abs(m) if absolute else m)+r
start=time.monotonic();cp=ROOT/'verification/tail_checks.json.gz';d=read(cp);assert d['all_checks_pass'] and d['bits']==1536
for item in d['inputs']+[d['prefix']]:checkref(item)
p=read(d['prefix']['path']);pr=ROOT/'verification/Q10_root5_polar_replay.json.gz';polar=read(pr)
assert p['all_checks_pass'] and p['maximum_order']==120 and p['bits']==2048
assert polar['all_checks_pass'] and polar['maximum_order']==120 and polar['bits']==3072 and polar['source']==d['prefix']
assert p['exact_prefix_comparisons']==800 and polar['independent_norm_comparisons']==240 and polar['independent_tuning_comparisons']==11
norms={v['n']:v for v in p['norms']};harmonics={v['n']:v for v in p['harmonics']}
gen=read(BASE/'reduced_generic.json.gz');small=read(BASE/'small_responses.json.gz');sm={x['k']:list(map(F,x['coefficients'])) for x in small['small']}
N=[shift(c,21) for c in gen['numerator_by_b_degree']];D=shift(gen['denominator'],21);assert len(D)==110 and all(c>0 for c in D)
rows=[]
for row in d['cases']:
 M=row['M'];n=row['N'];s=F(row['s']);I=tuple(map(F,row['root_interval']));e=row['tail_sign']
 assert (M,n) in [(10,100),(12,120)] and row['K']==21 and e in [-1,1] and s>0
 assert I==tuple(map(F,read(d['inputs'][-1]['path'])['real_roots'][4]['interval']))
 assert [x['degree'] for x in row['tail_coefficients']]==list(range(110))
 minima=[]
 for j in range(110):
  c=[e*col[j]-(s*D[j] if k==0 else 0) for k,col in enumerate(N)]
  interval=evaluate(c,I);assert interval[0]>0;minima.append(interval[0])
 assert [x['k'] for x in row['finite_checks']]==list(range(M,21))
 for item in row['finite_checks']:
  val=evaluate(sm[item['k']],I);sgn=item['sign'];assert sgn in [-1,1]
  assert (val[0] if sgn==1 else -val[1])>s
 checkref(row['box']);box=read(row['box']['path']);assert box['N']==n and box['M']==M and F(box['s'])==s
 density=list(map(F,box['initial_density']));hs=list(map(F,box['initial_harmonics']));assert len(density)==n and len(hs)==M-1 and hs[0]==0
 for k,bound in enumerate(density,1):assert bound==F(norms[k]['density_bound']) and bound>k*upper(norms[k]['F'])
 for k,bound in enumerate(hs[1:],2):assert bound==F(harmonics[10*k]['bound']) and bound>10*k*upper(harmonics[10*k]['H'],True)
 assert F(box['L'])==F(75,29) and F(box['kappa'])==F(208,5)*F(n+1,n)
 model=PrefixMajorant(1,10,4,density,hs,s,F(box['L']),F(box['kappa']));direct_scalar(model,2)
 assert model.constant==list(map(F,box['constant'])) and model.J==[list(map(F,x)) for x in box['J']] and model.Y0==list(map(F,box['Y0']))
 q=row['q'];assert q==box['adaptive']['q'];v=list(map(F,box['adaptive']['box']));image=model.transformed(F(1,2**q),v)
 assert image==list(map(F,box['adaptive']['image']))
 assert all(0<=y<=vv and 0<=z<=vv for y,z,vv in zip(model.Y0,image,v))
 rows.append(dict(N=n,M=M,s=str(s),q=q,positive_tail_coefficients=110,positive_denominator_coefficients=110,finite_inequalities=21-M,scalar_identities=60,box=row['box']))
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,source=ref(cp),polar=ref(pr),rows=rows,method='Fraction polynomial shifts and interval endpoints; exact independently indexed scalar identities and box inequalities.',actual_elapsed_s=time.monotonic()-start)
path=ROOT/'verification/tail_replay.json';path.write_text(json.dumps(clean(out),indent=2)+'\n');(ROOT/'sources/q10_tail_replay.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(clean(out)),flush=True)
