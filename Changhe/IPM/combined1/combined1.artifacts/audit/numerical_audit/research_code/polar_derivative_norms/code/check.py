"""Exact polar gradient/Hessian and complete outward moment integration."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_poly,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/polar_derivative_norms'
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from pipeline import load,source
from norms import ar,T,U,weight_poly

def H(p):
 h=sha256()
 with Path(p).open('rb') as stream:
  for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def new(path,data):
 with path.open('x') as s:json.dump(data,s,indent=2);s.write('\n')
def main():
 p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('--seconds',type=float,default=430);p.add_argument('--labels',nargs='+',default=['rF','G1','P2']);args=p.parse_args()
 assert set(args.labels)<=set(['rF','G1','P2']);start=time.monotonic();ctx.prec=2048
 src=source(args.candidate);cache=ROOT/f'research/whole_plane_norms/data/{args.candidate}_D0.json.gz';assembly=ROOT/f'research/whole_plane_norms/verification/{args.candidate}_assembly.json'
 assembled=json.loads(assembly.read_text());assert assembled['source_sha256']==H(src) and assembled['polynomial_sha256']==H(cache)
 delta=1-1/Q(json.loads(src.read_text())['cl']);F=load(args.candidate,0)[0,0]
 assert all(kind=='s' and n>0 and n%2 for ell,kind,n in F)
 modes=sorted({n for ell,kind,n in F});D=BASE/'verification'/args.candidate;D.mkdir(exist_ok=True);(D/'modes').mkdir(exist_ok=True)
 paths=[src,cache,assembly,Path(__file__),BASE/'PROOF.md',ROOT/'research/whole_plane_norms/code/pipeline.py',ROOT/'research/whole_plane_norms/code/norms.py',ROOT/'research/radial_fourier/code/radial.py']
 manifest={'candidate':args.candidate,'labels':args.labels,'modes':modes,'components':len(F),'precision_bits':ctx.prec,'weight_degree':112,'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths}}
 mp=D/'manifest.json'
 if mp.exists():assert json.loads(mp.read_text())==manifest
 else:new(mp,manifest)
 mh=H(mp);W,eps=weight_poly(112);W=arb_poly([ar(x) for x in W]);unit=arb_poly([1,-1]);saved={};fresh=0
 print('loaded',len(F),'components',len(modes),'modes',time.monotonic()-start,flush=True)
 def form(E,ell):
  if not E:return None
  end=E(U);q=next(i for i,z in enumerate(end) if z)
  return ell,q,arb_poly([ar(z) for z in list(end)[q:]])
 for n in modes:
  path=D/f'modes/mode_{n:03d}.json'
  if path.exists():
   rec=json.loads(path.read_text());assert rec['manifest_sha256']==mh and rec['mode']==n;saved[n]=rec;continue
  if time.monotonic()-start>=args.seconds:continue
  tick=time.monotonic();parts={'rF':[[]],'G1':[[],[]],'P2':[[],[],[]]};identities=0
  for (ell,kind,nn),P in sorted(F.items()):
   if nn!=n:continue
   d=ell*delta/2
   def td(V):return (1-2*d*T)*V+2*T*U*V.derivative()
   TP=td(P)
   if 'rF' in args.labels:parts['rF'][0].append(form(P,ell))
   if 'G1' in args.labels:
    parts['G1'][0].append(form(TP,ell));parts['G1'][1].append(form(n*P,ell))
   if 'P2' in args.labels:
    A=-2*d*TP+2*U*TP.derivative();B=n*(-2*d*P+2*U*P.derivative());C,rem=divmod(TP-n*n*P,T);assert not rem
    assert T*(A+C)==td(TP)-n*n*P;identities+=1
    for bucket,V in zip(parts['P2'],[A,B,C]):bucket.append(form(V,ell))
  result={};endpointrows={}
  for label in args.labels:
   groups={};endpoints=[]
   offset={'rF':Q(-4),'G1':Q(-2),'P2':Q(-9,5)}[label]
   for part,bucket in enumerate(parts[label]):
    rows=[row for row in bucket if row is not None]
    for ell,q,P in rows:
     b=ell*delta+2*q+offset;assert b>-1,(label,n,ell,q,b)
     endpoints.append({'part':part,'ell':ell,'q':q,'diagonal_exponent':str(b)})
    for i,(ell,q,P) in enumerate(rows):
     for j in range(i,len(rows)):
      ell2,q2,V=rows[j];b=(ell+ell2)*delta/2+q+q2+offset;assert b>-1
      factor=(1 if i==j else 2)*(2 if label=='P2' and part==1 else 1)
      product=P*V*factor
      if label=='rF':product*=unit*unit
      elif label=='P2':product*=unit
      groups[b]=groups.get(b,arb_poly([]))+product
   def integ(V,b):return sum((z/ar(b+j+1) for j,z in enumerate(V)),arb(0))
   S=sum((integ(V,b) for b,V in groups.items()),arb(0));assert S>0 and S.rel_accuracy_bits()>150,(n,label,S)
   lo=hi=S;factor=arb.pi()/2
   if label=='P2':
    hi=sum((integ(V*W,b) for b,V in groups.items()),arb(0));lo=hi-ar(eps)*S;factor*=arb(4)**ar(Q(4,5))
   lo*=factor;hi*=factor;assert lo>0 and hi>0 and lo.rel_accuracy_bits()>150 and hi.rel_accuracy_bits()>150
   result[label]={'energy_lower_ball':lo.str(100),'energy_upper_ball':hi.str(100),'norm_lower_ball':lo.sqrt().str(90),'norm_upper_ball':hi.sqrt().str(90),'groups':len(groups)};endpointrows[label]=endpoints
  rec={'utc':now(),'mode':n,'manifest_sha256':mh,'trace_identities':identities,'norms':result,'endpoints':endpointrows,'elapsed_seconds':time.monotonic()-tick}
  new(path,rec);saved[n]=rec;fresh+=1;print('mode',n,'seconds',rec['elapsed_seconds'],'total',time.monotonic()-start,flush=True)
 complete=len(saved)==len(modes);totals={}
 for label in args.labels:
  lo=sum((arb(row['norms'][label]['energy_lower_ball']) for row in saved.values()),arb(0));hi=sum((arb(row['norms'][label]['energy_upper_ball']) for row in saved.values()),arb(0))
  totals[label]={'norm_lower_ball':lo.sqrt().str(80),'norm_upper_ball':hi.sqrt().str(80) if complete else None}
 out={'utc':now(),'candidate':args.candidate,'complete':complete,'manifest_sha256':mh,'completed_modes':sorted(saved),'missing_modes':[n for n in modes if n not in saved],'norms':totals,'mode_sha256':{str(n):H(D/f'modes/mode_{n:03d}.json') for n in saved},'stage_elapsed_seconds':time.monotonic()-start,'status':'N4-origin OPEN peer' if complete else 'Partial norm lower bounds only'}
 if complete:new(D/'full.json',out)
 else:(D/'progress.json').write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',len(saved),'/',len(modes),complete,flush=True)
 for label,row in totals.items():print(label,row,flush=True)
if __name__=='__main__':main()
