"""Exact endpoint ordering. No copied peer program or candidate integrals run."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys,time
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads((B/p).read_text())
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');r=read('../candidate016_prefix_hardy_audit/verification/result.json');comp=read('../candidate016_complete_forcing_audit/verification/result.json')
N=p['N'];Ls={a['n']:F(a['q_lower_exact']) for a in r['modes']};Us={a['n']:F(a['q_upper_exact']) for a in r['modes']}
need('complete included prefix',sorted(Ls)==[1,3,5,7] and N==9)
for n in Ls:need('positive width '+str(n),0<Ls[n]<Us[n])
V=F(comp['components']['rF']['strict_upper_exact'])**2
P=V/N**2+sum((F(1,n*n)-F(1,N*N))*Us[n] for n in Us)
Q=sum(Us[n]/(n*n) for n in Us)+(V-sum(Ls.values()))/N**2
width=sum(Us[n]-Ls[n] for n in Us)/N**2
need('strict correct direction',Q-P==width>0)
need('accepted split value',Q==F(r['M2_upper_exact']))
need('positive omitted upper',V-sum(Ls.values())>0)
J=F(r['selected_cross_improvement_strict_lower_exact'])
need('accepted improved split',Q-J==F(r['improved_H_square_upper_exact']))
for name,M in [('positive',P),('split',Q)]:
 need(name+' H upper',0<M-J<F(p['candidate_H_upper'])**2)
 c={k:F(comp['components'][k]['strict_upper_exact']) for k in ['P2','G1','G0']}
 E=c['P2']**2+2**14*c['G1']**2+2**18*c['G0']**2+F(20,21)*2**18*(M-J)
 need(name+' E2 upper',E<F(p['candidate_E2_upper'])**2)
for N in [1,3,5,9,17,33]:
 for width0 in [F(0),F(1,7),F(1,3)]:
  L={n:F(1,n+1) for n in range(1,N,2)};U={n:L[n]+width0 for n in L};V0=2+sum(U.values())
  p0=V0/N**2+sum((F(1,n*n)-F(1,N*N))*U[n] for n in U)
  q0=sum(U[n]/(n*n) for n in U)+(V0-sum(L.values()))/N**2
  need('fixture difference '+str((N,width0)),q0-p0==sum(U[n]-L[n] for n in U)/N**2>=0)
fx=p['fixture'];nn=fx['N'];v,l,u=map(F,[fx[k] for k in ['V','L','U']]);pp=v/nn**2+(1-F(1,nn**2))*u;qq=u+(v-l)/nn**2
need('nonzero exact counterexample',pp==F(fx['P']) and qq==F(fx['Q']) and qq-pp==F(fx['difference'])>0)
src=(B/'source/T2_draft.py').read_text();old=read('source/T2_prior_result.json')
need('frozen work-in-progress reversed check','UM4 - UMs == sum(U6[k] - L6[k] for k in U6) / 81 and UM4 >= UMs' in src)
need('earlier result lacks new G','G' not in old and old['checks']==27 and old['fails']==[])
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'T2_draft_sha256':sha(B/'source/T2_draft.py'),'positive_coefficient_upper_exact':str(P),'split_upper_exact':str(Q),'strict_split_minus_positive_exact':str(width),'foreign_code_executed':False,'candidate_integrals_evaluated':False,'verdict':'CONFIRMED Q-P=sum widths/N^2>0 for the accepted016 endpoints. REFUTED the reversed work-in-progress T2 partG comparison. Both candidate upper displays remain valid; the general474 review is pending.'}
with (B/'verification/result.json').open('x') as out:json.dump(result,out,indent=2);out.write('\n')
print('PASS',len(checks),'checks',result['elapsed_seconds'],'seconds')
