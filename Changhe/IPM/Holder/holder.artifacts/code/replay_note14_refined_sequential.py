"""Single-process independent replay of audited polar cell formulas.

Uses the immutable refined snapshot audited in V119. Task enumeration, accumulation,
checkpointing and exact rational endpoints are local verifier code.
No process pool, server, cluster, or remote computation is used.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json, math, os, sys, time
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'05_team_audit/note14_certificate/sources_refined_0732'
sys.path.insert(0,str(SOURCE))
import certify_note14 as C
from flint import arb,ctx

def stamp():return datetime.now(timezone.utc).isoformat()
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 tmp=p.with_suffix(p.suffix+'.tmp');tmp.write_text(json.dumps(d,indent=2)+'\n');tmp.replace(p)
def interval(x):
 assert x.is_finite()
 return dict(lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()),display=x.str(55,more=True))
def geom(lo,hi,delta):
 n=max(1,math.ceil(math.log(hi/lo)/math.log1p(delta)))
 # Floating grid choices are exact decimal endpoints after repr. They are
 # mesh parameters, not approximations to mathematically prescribed nodes.
 v=[repr(lo*(hi/lo)**(j/n)) for j in range(n+1)]
 v[0]=repr(lo);v[-1]=repr(hi)
 assert all(Q(x)<Q(y) for x,y in zip(v,v[1:]));return v

def main():
 p=argparse.ArgumentParser();p.add_argument('--alpha',required=True);p.add_argument('--b',required=True);p.add_argument('--c',required=True);p.add_argument('--lam',required=True)
 p.add_argument('--delta',type=float,default=.01);p.add_argument('--rho-min',type=float,default=1e-6);p.add_argument('--rho-m',type=float,default=.01);p.add_argument('--rho-max',type=float,default=1e8)
 p.add_argument('--depth',type=int,default=3);p.add_argument('--prec',type=int,default=80);p.add_argument('--out',required=True);a=p.parse_args()
 assert 0<Q(a.alpha)<1 and Q(a.b)>0 and Q(a.lam)>0
 assert 0<a.rho_min<.5 and 0<a.rho_m<1<a.rho_max and 0<a.delta<1 and a.depth>=0 and a.prec>=80
 ctx.prec=a.prec;C.setup(a.alpha,a.b,a.c,a.lam)
 # Ensure all imported geometric constants were initialized at the target precision.
 C.CL.PI=arb.pi()
 out=ROOT/a.out;out.mkdir(parents=True,exist_ok=True)
 params=vars(a);src={str(z.relative_to(ROOT)):digest(z) for z in [Path(__file__),SOURCE/'certify_note14.py',SOURCE/'certify_lb.py',SOURCE/'zcurve.py']}
 tasks=[]
 def chunk(edges,kind,nt):
  step=max(1,4000//nt)
  for j in range(0,len(edges)-1,step):
   tasks.append(dict(kind=kind,edges=edges[j:j+step+1],ntheta=nt,depth=a.depth))
 nt=math.ceil(2*math.pi/a.delta);nt+=nt%2
 chunk(geom(a.rho_min,.5,a.delta),'near',nt)
 chunk(geom(a.rho_m,1.,a.delta),'middle',nt)
 rlo=1.
 while rlo<a.rho_max:
  rhi=min(10*rlo,a.rho_max);delta=min(.2,a.delta*rlo**((1-float(Q(a.alpha)))/4))
  n=math.ceil(2*math.pi/delta);n+=n%2
  chunk(geom(rlo,rhi,delta),'middle',n);rlo=rhi
 manifest=dict(time_utc=stamp(),params=params,source_hashes=src,tasks=tasks)
 man=out/'manifest.json'
 if man.exists():
  old=json.loads(man.read_text());assert old['params']==params and old['source_hashes']==src and old['tasks']==tasks
 else:save(man,manifest)
 started=time.monotonic();print(stamp(),'tasks',len(tasks),'PID',os.getpid(),flush=True)
 for idx,tk in enumerate(tasks):
  path=out/f'task_{idx:05d}.json'
  if path.exists():
   old=json.loads(path.read_text());assert old['task']==tk and old['source_hashes']==src;continue
  C.ERR.clear();edges=list(map(arb,tk['edges']));total=arb(0);count=0;begin=time.monotonic()
  center=(arb(1),arb(0)) if tk['kind']=='near' else (arb(1)/2,arb(0))
  for r0,r1 in zip(edges,edges[1:]):
   for k in range(tk['ntheta']):
    theta0=2*C.PI*k/tk['ntheta'];theta1=2*C.PI*(k+1)/tk['ntheta']
    if tk['kind']=='near':v,n=C.polar_value(center,r0,r1,theta0,theta1,0,tk['depth'],'near')
    else:v,n=C.m_cell(center,r0,r1,theta0,theta1,0,tk['depth'])
    assert v.is_finite();total+=v;count+=n
  rec=dict(time_utc=stamp(),index=idx,task=tk,source_hashes=src,interval=interval(total),cells=count,elapsed_seconds=time.monotonic()-begin,errors={k:interval(v) for k,v in C.ERR.items()})
  save(path,rec)
  print(stamp(),idx+1,'/',len(tasks),'cells',count,'task_seconds',round(rec['elapsed_seconds'],3),'total_seconds',round(time.monotonic()-started,1),flush=True)
 # Remainders recomputed separately here from the proved formulas.
 al=arb(str(Q(a.alpha)));rm=arb(repr(a.rho_min));rho=arb(repr(a.rho_m));R=arb(repr(a.rho_max));pi=arb.pi()
 inner=rm**al/al+rm*rm*(arb(1)/2+rm**al)/(2*(1-rm)**2)
 sliver=16*2**(al-1)*rho**(al+3)/(pi*(al+3)*(1-rho*rho).sqrt())
 tail=2**al*(R/(R-arb(1)/2))**3*R**(al-1)/(1-al)
 save(out/'remainders.json',dict(time_utc=stamp(),inner=interval(inner),sliver=interval(sliver),tail=interval(tail),source_hashes=src))
 print(stamp(),'ALL TASKS COMPLETE; exact recombination required',flush=True)
if __name__=='__main__':main()
