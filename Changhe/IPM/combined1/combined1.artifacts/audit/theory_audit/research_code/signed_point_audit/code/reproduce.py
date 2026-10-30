from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'weak_probe_audit/code'))
from reproduce import fields,rat,ar,td
ctx.prec=1024

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def run(name):
 start=time.monotonic();src=ROOT/f'data/{name}_canonical.json';tp=ROOT/f'source/{name}_signed_scan.json'
 target=json.loads(tp.read_text());assert sha(src)==target['source_sha256']
 c,delta,rho,stream=fields(json.loads(src.read_text()));x,y=map(rat,target['best']['point'])
 r2=x*x+y*y;r=ar(r2).sqrt();t=r2/(1+r2);u=1/(1+r2);ct=ar(x)/r;st=ar(y)/r
 sn=[arb(0),st];cn=[arb(1),ct]
 for n in range(2,max(n for j,n in rho)+1):
  sn.append(sn[-1]*ct+cn[-1]*st);cn.append(cn[-1]*ct-sn[-2]*st)
 powers={j:ar(u)**ar((j+1)*delta/2) for j,n in rho}
 rr=arb(0);rt=arb(0)
 for (j,n),v in rho.items():
  rr+=powers[j]*ar(td(v,(j+1)*delta/2,1)(t))*sn[n]
  rt+=powers[j]*n*ar(v(t))*cn[n]
 rx=ct*rr-st*rt;ry=st*rr+ct*rt
 theta=((rx*rx+ry*ry).sqrt()-ry)/2;gap=theta-ar(c-1)
 assert gap>0 and theta.overlaps(arb(target['best']['theta'])) and gap.overlaps(arb(target['best']['failure_gap']))
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'point':list(map(str,[x,y])),
      'rho_x':rx.str(100),'rho_y':ry.str(100),'theta':theta.str(100),'failure_gap':gap.str(100),
      'strict_failure_for_all_nonnegative_kappa':True,'N4_selected_witness_overlap':True,
      'source_sha256':sha(src),'target_sha256':sha(tp),'code_sha256':sha(Path(__file__)),
      'independent_helper_sha256':sha(ROOT.parent/'weak_probe_audit/code/reproduce.py'),
      'elapsed_seconds':time.monotonic()-start}
 (ROOT/f'verification/{name}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(name,theta.str(24),gap.str(24),out['elapsed_seconds'],flush=True)

if __name__=='__main__':
 for name in ['C1-N1-002-7branch-frf','C1-N1-003-8branch-frf','C1-N1-004-4branch-l2fw']:run(name)
