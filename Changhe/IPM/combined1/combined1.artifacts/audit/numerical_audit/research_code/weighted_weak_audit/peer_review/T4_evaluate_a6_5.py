from pathlib import Path
from datetime import datetime,timezone
import json,sys,time,hashlib,importlib.util,argparse
from flint import fmpq as Q,arb,ctx
ROOT=Path(__file__).resolve().parents[1]
helper=ROOT.parent/'localized_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('localized_helper',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
ar,integral,fields,squares=m.ar,m.integral,m.fields,m.square_groups
T,W=m.T,m.W
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def maximum(j,b):
 if j==0:return arb(1)
 return ar(Q(j)/(j+b))**j*ar(b/(j+b))**ar(b)
def run(name,aa,ks,bits):
 ctx.prec=bits;start=time.monotonic();a=Q(aa);assert 0<a<2
 src=ROOT/f'data/{name}_canonical.json';prior=ROOT/f'data/{name}_pairings.json'
 if not prior.exists():prior=ROOT/f'data/{name}_unweighted.json'
 base=json.loads(prior.read_text());assert base['canonical_sha256']==sha(src);pairings={r['k']:r for r in base['rows']}
 c,delta,rho,stream=fields(json.loads(src.read_text()));bg,_=squares(stream,delta,2);cg,_=squares(rho,delta,1)
 CU=ar(2/(2-a));certificate='T4-054 odd weighted velocity; C_U=2/(2-a)'
 if aa=='6/5':CU=ar(Q(808233,500000));certificate='T4-072 TP-2 rational Schur certificate at a=6/5'
 if aa=='7/5':CU=ar(Q(2142307,1000000));certificate='T4-072 TP-2 rational Schur certificate at a=7/5'
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'a':str(a),'precision_bits':bits,'velocity_constant':CU.str(60),'velocity_certificate':certificate,'source_sha256':sha(src),'pairing_source_sha256':sha(prior),'proof_sha256':sha(ROOT/'PROOF.md'),'code_sha256':sha(Path(__file__)),'helper_sha256':sha(helper),'rows':[]}
 print('prepared',name,a,'seconds',time.monotonic()-start,flush=True)
 for k in ks:
  tick=time.monotonic();lk=3*c+1+2*c*k*W-4*c*T;gk=1+2*k*W+4*T
  aa2=arb.pi()/2*integral(lk*lk,1-a,2*k+1)
  bb2=arb.pi()/2*sum((integral(v*gk*gk,1+(j+2)*delta/2-a,2*k+1) for j,v in bg.items()),arb(0))
  cc2=arb.pi()/2*sum((integral(v,1+(j+2)*delta/2-a,2*k+1) for j,v in cg.items()),arb(0))
  assert aa2>0 and bb2>0 and cc2>0
  A,B,C=aa2.sqrt(),bb2.sqrt(),cc2.sqrt();D=A+B+CU*C
  if k==0 and a<=Q(3,2):H=arb(1)
  else:H=maximum(k,2-a)+2*k*maximum(k,3-a)+4*maximum(k+1,2-a)
  I=abs(arb(pairings[k]['pairing']));R=2*I/(D+(D*D+4*CU*H*I).sqrt())
  row={'k':k,'pairing':pairings[k]['pairing'],'A':A.str(85),'B_upper':B.str(85),'C_upper':C.str(85),'D':D.str(85),'gradient_sup_upper':H.str(85),'weighted_L2_radius_lower':R.str(85),'elapsed_seconds':time.monotonic()-tick};out['rows'].append(row);out['elapsed_seconds']=time.monotonic()-start
  (ROOT/f'verification/{name}_a{a.numerator}_{a.denominator}_{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
  print('k',k,'weighted radius',R.str(35),'seconds',row['elapsed_seconds'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('--a',default='1');p.add_argument('--k',type=int,nargs='+',default=[0,128,512,1024]);p.add_argument('--bits',type=int,default=2048);args=p.parse_args();run(args.candidate,args.a,args.k,args.bits)
