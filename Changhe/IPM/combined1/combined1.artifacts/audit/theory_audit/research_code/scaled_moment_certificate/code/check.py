from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,argparse
from flint import fmpq as Q,arb,ctx
from moments import integral,ar
ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(case):
 label=case['exact'];factors=[(Q(z),Q(nu)) for z,nu in case['factors']]
 if label=='single_elementary':
  z,nu=factors[0]
  if nu==1:return -(1-ar(z)).log()/ar(z)
  return (1-ar(1-z)**ar(1-nu))/ar(z*(1-nu))
 if label=='two_logs':
  (z,_),(w,_)=factors
  return (ar(1-w)/ar(1-z)).log()/ar(z-w)
 return ar(Q(label))
def run(N,bits):
 start=time.monotonic();ctx.prec=bits;src=ROOT/'data/manufactured.json';cases=json.loads(src.read_text())['cases'];rows=[]
 for case in cases:
  tick=time.monotonic();value,details=integral(Q(case['alpha']),Q(case['beta']),[(Q(z),Q(nu)) for z,nu in case['factors']],N)
  target=exact(case);assert value.contains(target),(case['name'],value,target)
  row={'name':case['name'],'enclosure':value.str(80),'independent_closed_form':target.str(80),'contains_closed_form':True,'relative_radius':(value.rad()/abs(target)).str(30),'intervals':details,'elapsed_seconds':time.monotonic()-tick};rows.append(row)
  print(case['name'],'cells',len(details),'value',value.str(30),'relative_radius',row['relative_radius'],'seconds',row['elapsed_seconds'],flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':digest(ROOT/'PROOF.md'),'input_sha256':digest(src),'code_sha256':digest(ROOT/'code/moments.py'),'check_sha256':digest(Path(__file__)),'degree':N,'precision_bits':bits,'cases':rows,'elapsed_seconds':time.monotonic()-start}
 (ROOT/'verification'/f'manufactured_N{N}_{bits}.json').write_text(json.dumps(out,indent=2)+'\n');print('complete',out['elapsed_seconds'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--degree',type=int,default=192);p.add_argument('--bits',type=int,default=768);args=p.parse_args();run(args.degree,args.bits)
