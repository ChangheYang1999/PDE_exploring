"""Independently audit a frozen polar record without importing its programs.

This checks the finite enclosure and the analytic tails. A separate geometric
replay is required before this lane accepts a new operator lower bound.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,hashlib,json
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
ctx.prec=320

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def interval(v):
 assert v.is_finite()
 return Q(str(v.lower().fmpq())),Q(str(v.upper().fmpq()))
def save_interval(v):
 a,b=v
 return dict(lower=str(a),upper=str(b))
def floor_decimal(v,n=10):
 k=(v*10**n).__floor__()
 assert k>=0
 return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
 p=argparse.ArgumentParser();p.add_argument('directory');p.add_argument('record');a=p.parse_args()
 base=(ROOT/a.directory).resolve();assert base.is_relative_to(ROOT)
 src=base/'source';path=src/a.record;d=load(path);par=d['params']
 side=load(src/(a.record+'.tasks.json'))
 assert d['source_unchanged_during_run'] is True
 assert d['source_sha256']==d['source_sha256_at_end']==side['source_sha256_at_start']
 for name,h in d['source_sha256'].items():assert sha(src/name)==h
 # Every integration function must match the previously audited snapshot.
 old=ROOT/'05_team_audit/note14_certificate/sources_refined_0732'
 for name in ['certify_lb.py','zcurve.py']:assert (src/name).read_bytes()==(old/name).read_bytes()
 prefix=lambda z:z.read_text().split('\ndef main():')[0]
 assert prefix(src/'certify_note14.py')==prefix(old/'certify_note14.py')
 alpha=Q(d['alpha']);lam=Q(d['lam']);assert 0<alpha<1 and Q(d['b'])>0 and lam>0 and d['prec_bits']>=80
 assert alpha==Q(1,2), 'Only the half-exponent profile is registered here'
 prof=ROOT/'data/geometric_profile_a50_tight.json';pd=load(prof)
 assert Q(pd['alpha'])==alpha and Q(pd['certified_upper'])*lam<=1
 assert pd['checked_boxes']==2*pd['accepted_boxes']-1
 for name,h in pd['source_hashes'].items():assert sha(ROOT/name)==h
 sums={k:[Q(0),Q(0)] for k in ['near_e1','m_system']};covers={k:[] for k in sums};cells=0;input_hashes={}
 for idx,r in enumerate(side['tasks']):
  tk=r['task'];kind=tk['kind'];assert kind in sums
  for key,name in [('alpha_q','alpha'),('b_q','b'),('c_q','c'),('lam_q','lam')]:assert Q(tk[key])==Q(d[name])
  assert tk['maxdepth']==par['maxdepth'] and isinstance(tk['ntheta'],int) and tk['ntheta']>=4 and tk['ntheta']%2==0
  edges=list(map(Q,tk['rho_edges']));assert len(edges)>=2
  for lo,hi in zip(edges,edges[1:]):assert 0<lo<hi;covers[kind].append((lo,hi))
  mid=arb(r['mid']);rad=arb(r['rad']);assert rad>=0
  # Use the upper endpoint of the serialized radius, independently of the
  # producer's constructor convention for a ball-valued radius argument.
  v=mid+arb(0,str(rad.upper().fmpq()));lo,hi=interval(v)
  sums[kind][0]+=lo;sums[kind][1]+=hi
  assert isinstance(r['cells'],int) and r['cells']>=0;cells+=r['cells']
  for e in r['errors'].values():assert arb(e)>=0
 for kind,lo,hi in [('near_e1',Q(str(par['rho_min'])),Q(1,2)),('m_system',Q(str(par['rho_m'])),Q(str(par['rho_max'])))]:
  cursor=lo
  for x,y in sorted(covers[kind]):assert x==cursor,(kind,'gap or overlap',x,cursor);cursor=y
  assert cursor==hi
 assert cells==d['cells']
 aa=arb(str(alpha));eps=arb(str(par['rho_min']));eta=arb(str(par['rho_m']));R=arb(str(par['rho_max']));half=arb(1)/2
 rem=dict(inner=eps**aa/aa+eps**2*(half+eps**aa)/(2*(1-eps)**2),
          sliver=2**(aa+3)*eta**(aa+3)/(arb.pi()*(aa+3)*(1-eta**2).sqrt()),
          tail=2**aa*R**(aa+2)/((1-aa)*(R-half)**3))
 bounds={k:interval(v) for k,v in rem.items()};err=2*bounds['inner'][1]+bounds['sliver'][1]+bounds['tail'][1]
 lo=2*sums['near_e1'][0]+sums['m_system'][0]-err;hi=2*sums['near_e1'][1]+sums['m_system'][1]+err
 dl=max(Q(0),lo,-hi)+Q(1,2);safe=floor_decimal(dl)
 reported=interval(arb(d['D_lower']))
 reported_il=interval(arb(d['I0_lower']));reported_iu=interval(arb(d['I0_upper']))
 # Exact endpoint summation avoids magnitude-radius inflation in a long
 # 80-bit Arb accumulation. Require containment, not decimal agreement.
 assert reported_il[1]<=lo<=hi<=reported_iu[0]
 assert reported[1]<=dl
 excess=dl-reported[1]
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,
  alpha=str(alpha),b=d['b'],shift=d['c'],lam=d['lam'],task_count=len(side['tasks']),cells=cells,
  sums={k:save_interval(v) for k,v in sums.items()},remainders={k:save_interval(v) for k,v in bounds.items()},
  I0=save_interval((lo,hi)),exact_D_lower=str(dl),safe_D_lower_10_places=safe,
  producer_enclosure_contains_independent_interval=True,exact_gain_over_reported_upper=str(excess),
  inputs={str(z.relative_to(ROOT)):sha(z) for z in [path,src/(a.record+'.tasks.json'),prof]},
  source_sha256=d['source_sha256'],auditor_sha256=sha(Path(__file__)),
  verdict='Finite record and source audit CONFIRMED; independent geometric replay pending')
 (base/'independent_record_audit.json').write_text(json.dumps(result,indent=2)+'\n')
 print(result['time_utc'],len(side['tasks']),cells,safe,result['verdict'])
if __name__=='__main__':main()
