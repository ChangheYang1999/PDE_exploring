from pathlib import Path
from datetime import datetime,timezone
import hashlib,importlib.util,json,re,sys,time
from flint import fmpq as Q, fmpq_poly as P, arb, ctx
sys.set_int_max_str_digits(0);ctx.prec=2048
B=Path(__file__).resolve().parents[1];start=time.monotonic()
helper=B.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('own_polar_repair',helper);f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ar=lambda q:arb(q.numerator)/q.denominator
c=Q(4076476460239181,2251799813685248);delta=1-1/c;b=4*delta-1;W=P([1,-1])
peertext=(B/'source/T1_result.out').read_text();peers=re.findall(r'D  \|\|eta\|\|_2 = (\[.*?\])',peertext)
assert len(peers)==3
rows=[]
for name,peer in zip(['007','013','014'],peers):
 src=B/f'data/{name}.json';data=json.loads(src.read_text());terms=data['potential_correction']
 canonical={'cl':str(c),'order':[t['order'] for t in terms],'coefficients':[t['coefficient'] for t in terms]}
 cc,dd,rho,stream=f.fields(canonical);assert cc==c and dd==delta
 energy=arb(0);moments=[]
 for (j,n),D in sorted(rho.items()):
  assert j==3
  E,rem=divmod(D,W);assert not rem
  sq=E*E; beta=Q(1)/((b+1)*(b+2)); val=arb(0)
  for k,coef in enumerate(sq):
   val+=ar(coef*beta);beta*=Q(k+2)/(k+b+3)
  assert val>0 and val.rel_accuracy_bits()>200
  energy+=val
  moments.append({'n':n,'E_degree':E.degree(),'integral':val.str(100),'accuracy_bits':val.rel_accuracy_bits()})
 nrm=(arb.pi()*energy/2).sqrt();assert nrm.overlaps(arb(peer)) and nrm>ar(Q(218667,50))
 row={'candidate':name,'source_sha256':sha(src),'norm':nrm.str(100),'peer_norm':peer,'overlap':True,'strictly_above_4373_34':True,'moments':moments}
 rows.append(row);print(name,nrm.str(50),'seconds',time.monotonic()-start,flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in [B/'PROOF.md',Path(__file__),helper,B/'source/T1_result.out']},'rows':rows,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED all three particular global repair norms'}
with (B/'verification/result.json').open('x') as fp:json.dump(out,fp,indent=2);fp.write('\n')
print('DONE',out['utc'],out['elapsed_seconds'],flush=True)
