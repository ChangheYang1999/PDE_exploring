"""Independent conditional endpoint composition; no candidate integrals."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import gzip,hashlib,json,re,sys,time
B=Path(__file__).resolve().parents[1];tick=time.monotonic();sys.set_int_max_str_digits(0)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[]
def need(k,v):
 assert v,k
 checks.append(k)
def read(p):
 p=B/p
 return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
for row in read('data/manifest.json'):need('hash '+row['local'],sha(B/row['local'])==row['sha256'])
initial=read('data/initial_sources.json');par=read('data/parameters.json');first=read('data/PROOF_FIRST.json')
need('proof before checker',not first['checker_exists'] and first['proof_sha256']==sha(B/'PROOF.md'))
rawhash={}
for row in initial['sources']:
 raw=(B/row['local']).read_bytes();raw=gzip.decompress(raw) if row['gzip'] else raw;h=hashlib.sha256(raw).hexdigest();need('lossless '+row['local'],h==row['raw_sha256']);rawhash[row['source'].split('/c1-n4/')[1]]=h
peer=read('source/N4_result.json');need('peer complete finite check',peer['check_count']==len(peer['checks'])==441 and all(peer['checks'].values()))
need('full source graph captured',len(initial['checked_peer_graph'])==len(peer['inputs'])==29)
for row in initial['checked_peer_graph']:need('peer graph '+row['source'],peer['inputs'][row['source'].split('/c1-n4/')[1]]==row['sha256'])
for rel,h in rawhash.items():
 if rel in peer['inputs']:need('frozen peer binding '+rel,h==peer['inputs'][rel])
D=read('source/N3_dual.json.gz');R=read('source/N3_hres.json.gz');Y=read('source/N3_hardy.json.gz');C=read('source/N3_norms.json.gz')
for name,d in [('dual',D),('residual',R),('Hardy',Y),('components',C)]:need('candidate '+name,d['source_sha256']==par['raw_sha256']==peer['raw_sha256'])
need('exact c and delta',Q(C['cl'])==Q(par['c']) and Q(C['delta'])==1-1/Q(par['c']))
need('dual program identity',D['code_sha256']==sha(B/'source/N3_legqs_hdual.py'))
need('historical residual identity explicit',R['code_sha256']==par['historical_hres_sha256'] and sha(B/'source/N3_legqs_hres.py')==par['current_hres_sha256'] and R['code_sha256']!=sha(B/'source/N3_legqs_hres.py'))
def ball(text):
 m=re.fullmatch(r'\[([+\-0-9.eE]+) \+/- ([+\-0-9.eE]+)\]',text)
 if m:
  c,r=map(Q,m.groups());assert r>=0;return c-r,c+r
 if re.fullmatch(r'[+\-0-9.eE]+',text):return Q(text),Q(text)
 raise ValueError('incomplete or non-real exact ball')
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
def square(a):
 assert 0<=a[0]<=a[1]
 return a[0]**2,a[1]**2
sumlow=lambda rows:sum((z[0] for z in rows),Q(0));sumhigh=lambda rows:sum((z[1] for z in rows),Q(0))
dm={r['n']:r for r in D['modes']};rm={r['n']:r for r in R['modes']};ym={r['n']:r for r in Y['modes']}
need('distinct dual frequencies',list(dm)==list(range(1,32,2)) and len(D['modes'])==16)
need('distinct residual frequencies',list(rm)==list(range(1,32,2)) and len(R['modes'])==16 and R['modes_computed']==list(rm))
need('full 160 sine frequencies',list(ym)==list(range(1,320,2)) and len(Y['modes'])==160)
q={n:ball(r['rF_n_sq']) for n,r in ym.items()};UL={};dual=[];rows=[];trial_labels=0
for n,(ql,qu) in q.items():
 need('positive energy '+str(n),0<ql<=qu)
 need('Hardy primitive consistency '+str(n),overlap((ql,qu),square(ball(ym[n]['rF_n']))) and overlap((ql/n**2,qu/n**2),square(ball(ym[n]['H_n_UB']))))
 if n not in rm:UL[n]=qu/n**2;continue
 d,r=dm[n],rm[n];lo,hi=ball(d['LB']);g=ball(r['grad_psi']);rr=ball(r['residual_r_g']);need('positive selected intervals '+str(n),0<lo<=hi and 0<g[0]<=g[1] and 0<rr[0]<=rr[1])
 up=(g[0]+rr[0]/n,g[1]+rr[1]/n);reverse=(g[0]-rr[1]/n,g[1]-rr[0]/n)
 need('residual displayed division '+str(n),overlap((rr[0]/n,rr[1]/n),ball(r['residual_over_n'])))
 need('residual upper consistency '+str(n),overlap(up,ball(r['UB_n'])))
 need('reverse bound consistency '+str(n),overlap(reverse,ball(r['LB2_n'])))
 need('dual within Hardy upper '+str(n),lo**2<qu/n**2)
 UL[n]=min(up[1]**2,qu/n**2);dual.append((lo**2,hi**2))
 need('different trial families '+str(n),len(d['betas'])==9 and len(r['betas'])==8 and set(r['betas'])<set(d['betas']) and set(d['betas'])-set(r['betas'])=={'2'})
 for family,z in [('dual',d),('residual',r)]:
  need('positive saved exact d '+family+str(n),Q(z['grad_psi_sq_over_pi_exact'])>0)
  need('trial sparse nonempty '+family+str(n),0<len(z['x_rational'])<=z['basis_size'])
  for key,x in z['x_rational'].items():
   be,ks=key.split(',');beta=Q(be);k=int(ks);trial_labels+=1
   need('admissible '+family+str(n)+' '+key,beta>Q(3,2) and be in z['betas'] and -1<=k<=z['kmax'] and 3+2*k>=n and (3+2*k-n)%2==0 and Q(x)!=0)
 rows.append({'n':n,'dual_lower_exact':str(lo),'residual_upper_exact':str(up[1]),'mode_H_square_upper_exact':str(UL[n]),'actual_integral_reproduced_here':False})
L2=sumlow(dual);U2=sum(UL.values(),Q(0));tail=sum((UL[n] for n in UL if n>=33),Q(0));QL=sumlow(list(q.values()));QU=sumhigh(list(q.values()));MY=(sum((l/n**2 for n,(l,u) in q.items()),Q(0)),sum((u/n**2 for n,(l,u) in q.items()),Q(0)))
need('complete 144 omitted modes',len([n for n in UL if n>=33])==peer['uncomputed_tail_mode_count']==144 and len(UL)==160)
need('exact modal arithmetic agrees',str(L2)==peer['conditional_H_square_lower_exact'] and str(U2)==peer['conditional_H_square_upper_exact'])
for row,pr in zip(rows,peer['modes']):
 for k in ['n','dual_lower_exact','residual_upper_exact','mode_H_square_upper_exact']:need('peer modal '+str(row['n'])+' '+k,row[k]==pr[k])
need('Hardy sum consistency',overlap(MY,square(ball(Y['H_upper_ball']))))
need('dual sum consistency',overlap((sumlow(dual),sumhigh(dual)),square(ball(D['H_lower_ball']))))
need('whole rF consistency',overlap((QL,QU),(square(ball(C['norms']['rF']['norm_lower']))[0],square(ball(C['norms']['rF']['norm_upper']))[1])))
tailball=(sum((q[n][0]/n**2 for n in q if n>=33),Q(0)),tail)
need('all144 tail consistency',overlap(tailball,ball(R['other_modes_hardy_sq'])))
slack=Q(R['H_upper_new'])**2-U2
need('stored upper conservative',0<slack<Q('1e-30') and slack==Q(peer['stored_H_upper_square_conservative_slack_exact']))
need('H directed squared displays',0<Q(par['H_lower'])**2<L2<U2<Q(R['H_upper_new'])**2<Q(par['H_upper'])**2)
low={};high={}
for k in ['G0','G1','P2']:
 low[k]=ball(C['norms'][k]['norm_lower'])[0];high[k]=ball(C['norms'][k]['norm_upper'])[1];need('positive complete component '+k,0<low[k]<high[k] and C['norms'][k]['status']=='FINITE')
energy=lambda w,h:w['P2']**2+2**14*w['G1']**2+2**18*w['G0']**2+Q(20,21)*2**18*h
EL=energy(low,L2);EU=energy(high,U2)
need('E2 exact primitive recomposition',EL==Q(peer['conditional_E2_square_lower_exact']) and EU==Q(peer['conditional_E2_square_upper_exact']))
need('E2 directed squared displays',0<Q(par['E2_lower'])**2<EL<EU<Q(par['E2_upper'])**2)
old=read('../candidate016_dual_replay_audit/source/baseline007.json');need('accepted007 source',sha(B/'../candidate016_dual_replay_audit/source/baseline007.json')==peer['inputs']['research/negative_norm_forcing_assembly/verification/result.json'] and all(old['checks'].values()))
gap=Q(old['E_lower']['strict_lower_exact'])-Q(par['E2_upper']);need('conditional pairwise gap',gap==Q('.8591964')==Q(peer['conditional007_minus017_gap_exact'])>Q(par['gap_lower']))
rejected=[]
for family,z in [('dual',D),('residual',R)]:
 for key in ['H_upper_hardy','E2_lower_without_H','E2_upper_with_mode_hardy_H']:
  if key in z:
   try:ball(z[key])
   except ValueError:rejected.append(family+'.'+key)
need('all incomplete diagnostic strings rejected',rejected==peer['diagnostic_incomplete_strings_rejected'] and len(rejected)==4)
for k in ['source_premises_C1_C2_C3_accepted_here','actual017_H_or_E2_certified_here','actual017_less_than007_certified_here','peer_code_executed','new_integrals','historical_hres_code_observed']:need('scope '+k,peer[k] is False)
# Exact manufactured radial fixture, independent of candidate numerical inputs.
def plus(a,b):return [sum((p[i] if i<len(p) else Q(0) for p in (a,b)),Q(0)) for i in range(max(len(a),len(b)))]
def scale(a,c):return [c*x for x in a]
def times(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def derivative(a):return [(i+1)*a[i+1] for i in range(len(a)-1)] or [Q(0)]
def Dpoly(P,b):return plus(times([Q(1),-2*b],P),times([Q(0),Q(2),Q(-2)],derivative(P)))
def beta_integral(P,m):
 # Integral of t^i (1-t)^m on [0,1], m a nonnegative integer.
 from math import factorial
 return sum((p*Q(factorial(i)*factorial(m),factorial(i+m+1)) for i,p in enumerate(P)),Q(0))
f=par['fixture'];P=[Q(1)];b=Q(f['beta'])-1;n=f['n'];dp=Dpoly(P,b);ddp=Dpoly(dp,b)
need('fixture original power',n==1 and f['k']==-1 and b==2)
need('first radial derivative',dp==[Q(1),Q(-4),Q(0)])
# Trailing zero coefficients are harmless in the exact polynomial representation.
trim=lambda p:tuple(p[:next((i+1 for i in range(len(p)-1,-1,-1) if p[i]),1)])
need('second radial derivative',trim(ddp)==(Q(1),Q(-16),Q(24)))
d=beta_integral(plus(times(dp,dp),scale(times(P,P),n*n)),2)/2
a=beta_integral(plus(times(dp,dp),scale(times(ddp,ddp),Q(1,n*n))),2)/2
need('fixture exact d',d==Q(f['d_over_pi']))
need('fixture exact a',a==Q(f['a_over_pi']))
# Direct Cartesian Laplacian: Delta(y/(1+r^2)^2)=8y(r^2-2)/(1+r^2)^4.
qdelta=32*beta_integral(times([Q(0),Q(0),Q(1)],times([Q(-2),Q(3)],[Q(-2),Q(3)])),2)
need('independent weighted Delta square',qdelta==Q(f['Qdelta_over_pi'])==n*n*(a+d))
for text in f['lambda_values']:
 lam=Q(text);pp=-lam*d;bb=lam*a;qq=lam*lam*qdelta;res=qq+2*n*n*(bb-pp)+n*n*(a+d)
 need('manufactured residual identity '+text,res==(lam+1)**2*qdelta and res>=0)
 need('manufactured zero iff minusone '+text,(res==0)==(lam==-1))
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'frozen_peer_result_sha256':sha(B/'source/N4_result.json'),'modes':rows,'admissible_saved_nonzero_trial_labels':trial_labels,'complete_Hardy_modes':160,'retained_untested_modes':144,'conditional_H_square_lower_exact':str(L2),'conditional_H_square_upper_exact':str(U2),'conditional_E2_square_lower_exact':str(EL),'conditional_E2_square_upper_exact':str(EU),'stored_upper_square_slack_exact':str(slack),'conditional_E2007_minus_E2017_lower_exact':str(gap),'source_C1_C2_C3_accepted_here':False,'candidate_integrals_repeated':False,'foreign_code_executed':False,'fixture_exact':{'d_over_pi':str(d),'a_over_pi':str(a),'Qdelta_over_pi':str(qdelta)},'verdict':'CONFIRMED N4-413 conditional arithmetic and queued017 analytic residual identity. Saved exact trial labels satisfy the sufficient admissibility conditions. OPEN actual017 source integrals, complete norms and actual ordering; no inverse or existence.'}
with (B/'verification/result.json').open('x') as out:json.dump(result,out,indent=2);out.write('\n')
print('PASS',len(checks),'checks',trial_labels,'trial labels',result['elapsed_seconds'],'seconds')
