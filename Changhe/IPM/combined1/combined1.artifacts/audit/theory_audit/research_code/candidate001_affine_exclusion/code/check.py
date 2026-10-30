"""Independent leading angular construction directly from the raw860 rows."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from collections import defaultdict
import hashlib,json,time
B=Path(__file__).resolve().parents[1]; started=time.monotonic(); checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads((B/p).read_text())
def req(name,value):
 assert bool(value),name
 checks.append(name)
def add(a,n,x):
 if n<0:n=-n;x=-x
 if n:a[n]+=x

def clean(a):return {k:v for k,v in sorted(a.items()) if v}
def serial(a):return {str(k):str(v) for k,v in clean(a).items()}
inputs=read('data/input_sources.json')['inputs']
for x in inputs:req('frozen '+x['local'],sha(B/x['local'])==x['sha256'])
req('proof before checker', (B/'PROOF.md').stat().st_mtime_ns<Path(__file__).stat().st_mtime_ns)
j=read('source/raw.json');peer=read('source/N4_result.json');manifest=read('source/snapshot_manifest.json')
req('immutable raw hash',sha(B/'source/raw.json')=='8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7')
req('snapshot raw binding',manifest['coefficient_files'][0]['sha256']==sha(B/'source/raw.json'))
req('peer raw binding',peer['generator_sha256']==sha(B/'source/raw.json'))
req('peer manifest binding',peer['manifest_sha256']==sha(B/'source/snapshot_manifest.json'))
c=Q(j['cl_exact']);gamma=1/c;delta=1-gamma;q=2*gamma-1
req('exact c',c==Q(4076476460239181,2251799813685248)==Q(peer['c_exact']))
req('exponents',0<q<gamma<1 and q==Q(427123167131315,4076476460239181))
req('zero leading transport',c*gamma==1)
rows=j['generators'];req('all860 rows',len(rows)==860)
C=defaultdict(lambda:defaultdict(Q))
for k,r in enumerate(rows):
 spec=r['spec'];m=r['m'];branch=r['j']
 req('analytic generator '+str(k),isinstance(m,int) and m>=0 and isinstance(branch,int) and 0<=branch<=3 and ((spec[0]=='mono' and len(spec)==2) or (spec[0]=='leg' and len(spec)==3)) and all(isinstance(x,int) and x>=0 for x in spec[1:]))
 # Each mono or Legendre radial factor is exactly1 at t=1.
 C[branch][2*m]+=Q(r['coef'])
G={};S={}
for branch in range(4):
 d=3+gamma-branch*delta;e=d-3;g=defaultdict(Q);s=defaultdict(Q)
 for n,a in C[branch].items():
  add(g,n+1,-a*(d*d-n*n)*(d-2-n)/2)
  add(g,n-1,+a*(d*d-n*n)*(d-2+n)/2)
  add(s,n+2,+a*(d-n)*(d-n-2)/4)
  add(s,n-2,-a*(d+n)*(d+n-2)/4)
 G[branch]=clean(g);S[branch]=clean(s)
 dxrho=defaultdict(Q)
 for n,a in g.items():
  add(dxrho,n-1,a*(e+n)/2);add(dxrho,n+1,a*(e-n)/2)
 lap={n:((d-2)**2-n*n)*a for n,a in s.items()}
 req('canonical Laplacian identity branch '+str(branch),clean(lap)==clean({n:-a for n,a in dxrho.items()}))
req('nonzero leading density',bool(G[0]))
E=defaultdict(Q)
for n,a in G[1].items():E[n]+=(c*q-1)*a
for m,a in S[0].items():
 for n,b in G[0].items():
  add(E,n+m,a*b*(-gamma*m+(gamma+1)*n)/2)
  add(E,n-m,a*b*(-gamma*m-(gamma+1)*n)/2)
E=clean(E);target={int(n):Q(a) for n,a in peer['first_nonzero_sector']['sine_coefficients'].items()}
req('all exact E10 coefficients',E==target)
req('mode21 nonzero',E.get(21,Q(0))!=0)
req('first peer label',peer['first_nonzero_sector']['h']==1 and peer['first_nonzero_sector']['q']==0)
req('first exponent equality',q==Q(peer['first_nonzero_sector']['exponent']))
req('all omitted powers lower',gamma-2*delta<q and gamma-2<q)
req('annular proof reviewed',sha(B/'source/annular_PROOF.md')=='ebf243859dc4e104c71f7414a95e9e38001be51ca65efe3e9abcb5e21f0ffcd4')
req('annular review bound','ebf243859dc4e104c71f7414a95e9e38001be51ca65efe3e9abcb5e21f0ffcd4' in (B/'source/annular_ACCEPTANCE.md').read_text())
req('review digest',sha(B/'source/annular_N4_review.md')=='8edb3e3562299df5c7acc28666c798763015d276968d36382bef5d99568a2bff')
for x in inputs:req('unchanged '+x['local'],sha(B/x['local'])==x['sha256'])
coeff={'c_exact':str(c),'gamma_exact':str(gamma),'q_exact':str(q),'leading_potential':{str(k):{str(n):str(v) for n,v in sorted(a.items()) if v} for k,a in C.items()},'density':{str(k):serial(a) for k,a in G.items()},'stream':{str(k):serial(a) for k,a in S.items()},'E10':serial(E),'E10_sum_squares_exact':str(sum(v*v for v in E.values()))}
with (B/'data/leading_coefficients.json').open('x') as f:json.dump(coeff,f,indent=2);f.write('\n')
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,'check_count':len(checks),'checks':checks,'inputs':{x['local']:x['sha256'] for x in inputs},'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'coefficient_sha256':sha(B/'data/leading_coefficients.json'),'raw_sha256':sha(B/'source/raw.json'),'coefficient_count':len(E),'fixed_c_no_L2_application':'CONFIRMED exact inputs to AUDITED annular theorem; new application awaits Opus review','any_real_c_application':'CONFIRMED same nonzero leading density and gamma>q; new application awaits Opus review','independent_inputs_recomputed':True,'integrals_evaluated':False,'external_code_executed':False}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',len(E),'nonzero residual modes',out['utc'],out['elapsed_seconds'])
