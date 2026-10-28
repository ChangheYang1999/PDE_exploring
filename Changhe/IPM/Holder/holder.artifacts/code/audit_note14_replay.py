"""Independent exact recombination of a completed sequential polar replay.

The integration driver is not imported. Geometry coverage is verified directly
from its manifest. Remainders are evaluated independently at 256 bits, and every
accepted decimal is rounded down using integer arithmetic.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds(v):
 lo,hi=Q(v['lower']),Q(v['upper']);assert lo<=hi;return lo,hi
def arb_bounds(v):
 assert v.is_finite();return Q(str(v.lower().fmpq())),Q(str(v.upper().fmpq()))
def decimal_floor(v,n=10):
 k=(v*10**n).__floor__();sign='-' if k<0 else '';k=abs(k)
 return f'{sign}{k//10**n}.{k%10**n:0{n}d}'
def interval_record(pair):
 lo,hi=pair
 return dict(lower=str(lo),upper=str(hi),lower_decimal=decimal_floor(lo,16),upper_decimal=decimal_floor(hi+Q(1,10**16),16))
def check_profile(alpha,lam):
 if alpha in [Q(3,10),Q(1,2)]:
  paths=[ROOT/f'data/geometric_profile_a{30 if alpha==Q(3,10) else 50}_tight.json'];key='certified_upper'
 elif alpha in [Q(3,4),Q(9,10)]:
  tag='a75_k106' if alpha==Q(3,4) else 'a90_k110'
  paths=[ROOT/f'07_diagonal_identity_term/full_range_profile/verification/{tag}_{mode}.json' for mode in ['same','opposite']];key='target'
 else:raise ValueError('No audited profile certificate registered for this exponent')
 result={}
 for path in paths:
  p=json.loads(path.read_text());assert Q(p['alpha'])==alpha
  assert lam*Q(p[key])<=1
  assert p['checked_boxes']==2*p['accepted_boxes']-1
  for name,h in p['source_hashes'].items():assert sha(ROOT/name)==h,(name,'profile source')
  result[str(path.relative_to(ROOT))]=sha(path)
 return result

def main():
 parser=argparse.ArgumentParser();parser.add_argument('directory');parser.add_argument('--claimed');args=parser.parse_args()
 directory=(ROOT/args.directory).resolve();assert directory.is_relative_to(ROOT)
 manifest=json.loads((directory/'manifest.json').read_text());params=manifest['params'];sources=manifest['source_hashes']
 for name,h in sources.items():assert sha(ROOT/name)==h,(name,'integration source')
 alpha=Q(params['alpha']);lam=Q(params['lam']);assert 0<alpha<1 and Q(params['b'])>0 and lam>0
 assert params['prec']>=80 and params['depth']>=0
 low=Q(str(params['rho_min']));middle=Q(str(params['rho_m']));high=Q(str(params['rho_max']))
 assert 0<low<Q(1,2) and 0<middle<1<high
 profile=check_profile(alpha,lam)
 sums={'near':[Q(0),Q(0)],'middle':[Q(0),Q(0)]};covers={'near':[],'middle':[]};cells=0;records=[]
 expected={f'task_{i:05d}.json' for i in range(len(manifest['tasks']))}
 assert {p.name for p in directory.glob('task_*.json')}==expected,'missing or unexpected tasks'
 for idx,task in enumerate(manifest['tasks']):
  path=directory/f'task_{idx:05d}.json';rec=json.loads(path.read_text())
  assert rec['index']==idx and rec['task']==task and rec['source_hashes']==sources
  kind=task['kind'];assert kind in covers and task['depth']==params['depth']
  nt=task['ntheta'];assert isinstance(nt,int) and nt>=4 and nt%2==0
  edges=list(map(Q,task['edges']));assert len(edges)>=2
  for a,b in zip(edges,edges[1:]):assert 0<a<b;covers[kind].append((a,b))
  lo,hi=bounds(rec['interval']);sums[kind][0]+=lo;sums[kind][1]+=hi
  assert isinstance(rec['cells'],int) and rec['cells']>=0;cells+=rec['cells']
  for value in rec['errors'].values():
   elo,ehi=bounds(value);assert elo>=0
  records.append(dict(index=idx,sha256=sha(path),cells=rec['cells']))
 for kind,start,stop in [('near',low,Q(1,2)),('middle',middle,high)]:
  cursor=start
  for a,b in sorted(covers[kind]):assert a==cursor,(kind,'gap or overlap',a,cursor);cursor=b
  assert cursor==stop,(kind,'wrong endpoint')
 remainder_path=directory/'remainders.json';saved=json.loads(remainder_path.read_text());assert saved['source_hashes']==sources
 ctx.prec=256;a=arb(str(alpha));eps=arb(str(low));eta=arb(str(middle));R=arb(str(high));half=arb(1)/2
 # Independent arrangement of the three analytic formulas.
 values=dict(inner=(a*eps*eps*(half+eps**a)+2*(1-eps)**2*eps**a)/(2*a*(1-eps)**2),
             sliver=arb(2)**(a+3)*eta**(a+3)/(arb.pi()*(a+3)*(1-eta*eta).sqrt()),
             tail=arb(2)**a*R**(a+2)/((1-a)*(R-half)**3))
 remainders={}
 for name,value in values.items():
  checked=arb_bounds(value);old=bounds(saved[name]);assert old[0]>=0
  assert old[0]<=checked[0] and checked[1]<=old[1],(name,'independent remainder outside saved enclosure')
  remainders[name]=checked
 total_error=2*remainders['inner'][1]+remainders['sliver'][1]+remainders['tail'][1]
 lo=2*sums['near'][0]+sums['middle'][0]-total_error
 hi=2*sums['near'][1]+sums['middle'][1]+total_error
 absolute_lower=max(Q(0),lo,-hi);d_lower=absolute_lower+Q(1,2);safe=decimal_floor(d_lower)
 if args.claimed:assert Q(args.claimed)<=d_lower,('claimed lower exceeds independently recombined bound',args.claimed,safe)
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(alpha),b=str(Q(params['b'])),shift=str(Q(params['c'])),lam=str(lam),
  task_count=len(records),cells=cells,radial_intervals={k:len(v) for k,v in covers.items()},source_hashes=sources,
  manifest_sha256=sha(directory/'manifest.json'),task_files=records,profile_certificate_sha256=profile,
  near=interval_record(sums['near']),middle=interval_record(sums['middle']),remainders={k:interval_record(v) for k,v in remainders.items()},
  I0=interval_record((lo,hi)),exact_D_lower=str(d_lower),safe_D_lower_10_places=safe,
  claimed=args.claimed,verdict='CONFIRMED: full independent sequential replay, complete once-only exact radial coverage, profile dependencies, 256-bit independent remainders, and exact rational recombination under the repaired analytic cell proof.')
 result['auditor_sha256']=sha(Path(__file__))
 (directory/'independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['time_utc','alpha','task_count','cells','safe_D_lower_10_places','claimed']},indent=2))
if __name__=='__main__':main()
