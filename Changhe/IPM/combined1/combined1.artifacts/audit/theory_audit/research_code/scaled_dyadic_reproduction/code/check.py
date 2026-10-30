"""Independent polar rational Laplacians and CRT moments at eight weights."""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
import hashlib,importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];R=B.parent
spec=importlib.util.spec_from_file_location('t4_scaled_polar',R/'scaled_polar_weak/code/check_v2.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
Rat,T,V=p.Rat,p.T,p.V
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest()
ar=p.ar

def write(path,value):
 with path.open('x') as f:json.dump(value,f,indent=2);f.write('\n')

def prepare(A,label):
 tick=time.monotonic();N=V*A.numerator_v();D,rows=p.crt_data(A.powers)
 pol,rem=divmod(N,D);replay=pol*D;principal=[]
 for a,k,Di,E,inv in rows:
  Ri=divmod(rem*inv,Di)[1];local=Ri(Poly([-1/a,1/a]))
  for j,q in enumerate(local):
   if q:assert k-j>0;principal.append((q,a,k-j))
  replay+=Ri*E
 assert replay==N
 print('CRT',label,'degree',pol.degree(),'parts',len(principal),'seconds',time.monotonic()-tick,flush=True)
 return pol,principal,{'label':label,'denominator_powers':list(A.powers),'polynomial_degree':pol.degree(),'principal_parts':len(principal),'exact_CRT_replay':True,'seconds':time.monotonic()-tick}

def integrate(pre,b):
 assert b>-1
 pol,principal,record=pre
 value=sum((ar(q/(b+i+1)) for i,q in enumerate(pol)),arb(0))
 for q,a,k in principal:value+=ar(q)*p.pole(str(b),str(a),k)
 assert value.is_finite() and value.rel_accuracy_bits()>150,(record['label'],str(b),value.rel_accuracy_bits())
 return value

def main():
 start=time.monotonic();ctx.prec=2048
 frozen=json.loads((B/'source/FROZEN.json').read_text())
 for k,v in frozen['files'].items():assert sha(B/k)==v['sha256']
 peerpath=B/'source/result_modes_001_003.json';peer=json.loads(peerpath.read_text())
 raw=R/'multiscale_point_010/data/candidate010.json';pointpath=R/'multiscale_point_010/source/N4_result.json'
 pt=json.loads(pointpath.read_text());data=json.loads(raw.read_text())
 c,delta,rho,stream=p.fields(data);assert 1<c<2
 fields=p.evaluation(c,delta,rho,stream,*pt['point'])
 pointchecks={k:bool(v.overlaps(arb(pt['fields'][k]))) for k,v in fields.items()};assert all(pointchecks.values())
 assert all(A.exact_value(0)==0 for (j,n),A in rho.items() if n!=1)
 assert all(A.exact_value(0)==0 for (j,n),A in stream.items() if n!=2)
 a0=sum((A.exact_value(0) for (j,n),A in rho.items() if n==1),Q(0))
 strain=2*sum((A.exact_value(0) for (j,n),A in stream.items() if n==2),Q(0))
 assert a0==Q(peer['a0_exact']) and a0>=5*c-4 and strain==1-c
 print('010 independent polar fields',len(rho),len(stream),'origin+points OK',time.monotonic()-start,flush=True)
 Dr={k:p.td(A,(k[0]+1)*delta/2,1) for k,A in rho.items()}
 Ds={k:p.td(A,(k[0]+1)*delta/2,2) for k,A in stream.items()}
 dependencies=[Path(__file__),B/'PROOF.md',R/'scaled_polar_weak/code/check_v2.py',R/'scaled_field_audit/source/fields.py',raw,pointpath,B/'source/FROZEN.json',peerpath]
 common={'candidate':peer['candidate'],'precision_bits':ctx.prec,'inputs':{str(q):sha(q) for q in dependencies}}
 energies={};modehash={}
 for mode in [1,3]:
  dest=B/f'verification/mode_{mode:03}.json';ref=B/f'source/mode_{mode:03}.json';pr=json.loads(ref.read_text())
  assert sha(ref)==peer['mode_result_sha256'][str(mode)]
  if dest.exists():
   out=json.loads(dest.read_text());assert out['inputs']==common['inputs'] and out['peer_sha256']==sha(ref)
  else:
   tick=time.monotonic();residual={};pairs=0
   def add(ell,A):
    if A:residual[ell]=residual.get(ell,Rat())+A
   for (j,n),A in rho.items():
    if n==mode:add(j+1,c*Dr[j,n]-A)
   for (j,m),S in stream.items():
    for (k,n),A in rho.items():
     if m+n!=mode and abs(n-m)!=mode:continue
     if m+n==mode:add(j+k+2,(n*A*Ds[j,m]-m*S*Dr[k,n])/2)
     if abs(n-m)==mode:add(j+k+2,(-n*A*Ds[j,m]-m*S*Dr[k,n])*(1 if n>m else -1)/2)
     pairs+=1
   print('mode',mode,'all residual pairs',pairs,time.monotonic()-tick,flush=True)
   terms=[];endpoint=[];projection={}
   for ell,A in sorted(residual.items()):
    if not A:continue
    projection[ell]=A.record();z=ell*delta/2
    L=(p.td(p.td(A,z,1),z,1)-mode*mode*A).divide_t(1)
    if not L:continue
    Lv=L.numerator_v();order=next(i for i,v in enumerate(Lv) if v)
    assert ell*delta+2*order-2>0
    reduced=Rat(Poly(list(Lv)[order:])(V),L.powers)
    terms.append((ell,order,reduced));endpoint.append({'ell':ell,'order':order,'degree':Lv.degree(),'powers':list(L.powers),'margin':str(ell*delta+2*order-2)})
   groups={}
   for i,(ell,q,A) in enumerate(terms):
    for j in range(i,len(terms)):
     k,s,C=terms[j];key=(ell+k,q+s)
     groups[key]=groups.get(key,Rat())+A*C*(1 if i==j else 2)
   prepared={key:prepare(A,f'{mode}:{key}') for key,A in sorted(groups.items()) if A}
   weights=[];minimum_bits=100000
   for ka,row in enumerate(pr['weights']):
    a=Q(ka,4);assert Q(row['a'])==a
    total=arb(0)
    for (ell,q),pre in prepared.items():
     value=integrate(pre,a+ell*delta/2+q-3);minimum_bits=min(minimum_bits,value.rel_accuracy_bits());total+=value
    energy=arb.pi()/2*total;assert energy>0 and energy.rel_accuracy_bits()>150
    norm=energy.sqrt();flags={k:bool(v.overlaps(arb(row[k]))) for k,v in [('energy',energy),('norm',norm)]};assert all(flags.values()),(mode,a,flags)
    weights.append({'a':str(a),'energy':energy.str(110),'norm':norm.str(110),'comparisons':flags})
    print('mode',mode,'weight',a,'norm',norm.str(20),'seconds',time.monotonic()-tick,flush=True)
   projectionfile=B/f'data/mode_{mode:03}_projection.json';write(projectionfile,projection)
   out={**common,'utc':datetime.now(timezone.utc).isoformat(),'mode':mode,'peer_sha256':sha(ref),'all_residual_pairs':pairs,'endpoint':endpoint,'projection_sha256':sha(projectionfile),'CRT_records':[pre[2] for pre in prepared.values()],'minimum_bits':minimum_bits,'weights':weights,'elapsed_seconds':time.monotonic()-tick}
   write(dest,out)
  modehash[str(mode)]=sha(dest);energies[mode]={Q(row['a']):arb(row['energy']) for row in out['weights']}
 d=c-1;sstar=(ar(2*d-3)+ar((2*d-3)**2+16*d).sqrt())/8;assert 0<sstar<ar(d)
 H=(ar(d)-sstar)*(4*arb.pi()*sstar*(1+sstar)).sqrt();assert H.overlaps(arb(peer['H_max']))
 edges=[Q(k,4) for k in range(7)]+[1+1/c];assert Q(3,2)<edges[-1]<Q(7,4)
 cells=[]
 for k,(l,h) in enumerate(zip(edges,edges[1:])):
  e=Q(k+1,4);assert e>=h
  J=sum((energies[n][e] for n in energies),arb(0)).sqrt();lower=arb(5)**ar((l-2)/2)*J;upper=H*ar((1+c-c*l)/(1+l));gap=lower-upper;ratio=lower/upper
  vals={'projected_norm':J,'lower':lower,'upper':upper,'gap':gap,'ratio':ratio};pr=peer['seven_cells'][k]
  assert Q(pr['left'])==l and Q(pr['right'])==h and Q(pr['norm_evaluation_at'])==e
  flags={name:bool(value.overlaps(arb(pr[name]))) for name,value in vals.items()};assert all(flags.values()) and gap>0
  floor=Q(pr['strict_ratio_floor']);assert ratio>ar(floor)
  cells.append({'left':str(l),'right':str(h),'norm_evaluation_at':str(e),**{name:value.str(100) for name,value in vals.items()},'strict_ratio_floor':str(floor),'comparisons':flags})
 out={**common,'utc':datetime.now(timezone.utc).isoformat(),'a0_approx':ar(a0).str(60),'origin_identities_exact':True,'point_checks':pointchecks,'mode_hashes':modehash,'H_max':H.str(100),'s_maximizer':sstar.str(100),'seven_cells':cells,'all_seven_excluded':True,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED independent candidate-level N4-231 reproduction; scheme interpretation is conditional'}
 write(B/'verification/result.json',out);print('DONE',out['utc'],out['verdict'],out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
