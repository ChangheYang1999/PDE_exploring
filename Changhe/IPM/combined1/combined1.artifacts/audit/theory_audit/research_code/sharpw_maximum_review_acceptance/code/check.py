"""Exact fixed-norm optimization review; no peer execution."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import ast,gzip,hashlib,json,time
from flint import arb,fmpq,ctx
B=Path(__file__).resolve().parents[1];tick=time.monotonic();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[]
def need(k,v):
 assert v,k
 checks.append(k)
def read(p):return json.loads((B/p).read_text())
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');ctx.prec=p['precision_bits'];Aq=lambda q:arb(fmpq(str(q)));first=read('data/PROOF_FIRST.json');need('proof before checker',not first['checker_exists'] and first['proof_sha256']==sha(B/'PROOF.md'))
need('budget clarification present','X(F)<=r(mu-Ar)' in (B/'ERRATA_v01.md').read_text())
peer=read('source/T2_result.json');need('17 peer checks and no failure',peer['checks']==17 and peer['fails']==[] and '17 checks, 0 FAIL' in (B/'source/T2_log.txt').read_text())
mp={'c1-coord/coordination/frozen/FINAL_REPORT_frozen_1630.md':'../frozen_report_1630_audit/source/FINAL_REPORT.md','c1-t2/notes/T2_T4L2_sharp.md':'source/T2_framework.md'}
for key,h in peer['input'].items():need('peer input '+key,sha(B/mp[key])==h)
tree=ast.parse((B/'source/T2_check.py').read_text());pins=[n.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets)];need('peer pinned same two constants',len(pins)==1 and isinstance(pins[0],ast.Dict) and set(ast.literal_eval(x) for x in pins[0].values)==set(peer['input'].values()))
framework=(B/'source/T2_framework.md').read_text();need('reviewed conditional framework','Status after T4-042' in framework and 'not a necessary one' in framework and 'beta = mu0 - C\' s - (8/5) r/sqrt(s)' in framework)
s=Q(p['s']);mu0=Q(p['mu0']);C=Q(p['C']);cU=Q(p['cU']);sqrt_s=Q(p['sqrt_s']);need('exact fractional index',sqrt_s**2==s and 0<s<=Q(1,1024));mu=mu0-C*s;A=cU/sqrt_s;rs=mu/(2*A);eps=mu**2/(4*A);r0=Q(p['r_selected']);eta0=Q(p['eta_selected']);beta0=mu-A*r0
for key,val in [('mu',mu),('A',A),('eta_star',eps),('r_star',rs)]:need('exact peer '+key,val==Q(peer[key])==Q(p[key]))
need('positive rate at maximum',mu>0 and A>0 and 0<rs<mu/A and mu-A*rs==mu/2)
# Equality of all three polynomial coefficients, not sampling alone.
need('quadratic constant',eps-A*rs**2==0)
need('quadratic linear',2*A*rs==mu)
need('quadratic maximum value',(mu-A*rs)*rs==eps)
need('selected exact rate',beta0==Q('63092119/405000000')>=Q('1557/10000'))
need('selected sufficient budget',eta0<=Q('1557/10000')*r0<=beta0*r0<eps)
need('old radius already admits larger floor',eta0<Q('2.1046e-4')<beta0*r0<eps<Q('2.1047e-4'))
loss=eps-beta0*r0;need('exact old-radius loss',loss==A*(r0-rs)**2>0)
ratio=eps/eta0;need('relative gain directed',Q('1.0005')<ratio<Q('1.0006'))
need('pi strict bound',arb.pi()>Aq(Q(p['pi_lower'])))
cs2up=1/(4*Q(p['pi_lower'])*s*(1+s));x2=cs2up*rs**2;need('peer contraction square',x2==Q(peer['cs_r_star_sq_upper'])==Q('40722836401/54043470895104'))
need('contraction and slope budgets',0<x2<Q('.02746')**2 and Q('.02746')/2==Q('.01373')<1 and Q(7,10)-Q('.02746')==Q('.67254')>0)
cs=1/(4*arb.pi()*Aq(s)*Aq(1+s)).sqrt();need('actual containing contraction square',0<cs*Aq(rs)<Aq(Q('.02746')))
need('defect zero specialization',((mu-A*0-0)**2-4*A*0*0)/(4*A)==eps)
s0=mu0/(5*C);need('other fractional index',s0==Q(peer['s0'])==Q('97/496250') and 0<s0<=Q(1,1024) and s0!=s)
# Derivative sign factors follow from positive s and 0<s<mu0/C.
need('s derivative critical equation',mu0-C*s0==4*C*s0 and mu0-5*C*s0==0)
emax2=Q(25,4)*C**4*s0**5;need('other norm maximum exact square',emax2==Q(25,1024)*(mu0-C*s0)**4*s0)
need('other norm directed display',Q('.0002104742925')**2<emax2<Q('.0002104742926')**2 and emax2>eps**2)
need('peer other norm ball contains square root',arb(peer['sup_over_s_arb']).contains(Aq(emax2).sqrt()))
base=read('../frozen_report_1630_audit/verification/result.json');need('own479 accepted check',base['check_count']==823 and len(base['checks'])==823)
forcing=Q(p['forcing007_lower']);factor=forcing/eps;need('007 new factor',factor>3594606 and forcing/eta0>Q('3596535.57'))
current=gzip.decompress((B/'source/coordinator_report.md.gz').read_bytes()).decode();source=read('data/initial_sources.json')['sources'][-1];need('frozen current report identity',hashlib.sha256(current.encode()).hexdigest()==source['raw_sha256'])
for phrase in ['40722836401/193491763200000','201799/149299200','factor above 3594606','the exact optimum of the same estimate','At r = 1351/1000000','already admits 2.1046e-4']:need('current repair '+phrase,phrase in current)
for phrase in ['At the same s and weights','different norm','No candidate exclusion and no framework verdict changes.']:
 # The first wording in the peer review uses a lowercase sentence continuation.
 need('review scope '+phrase,phrase.lower() in (B/'source/T2_review.md').read_text().lower())
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'erratum_sha256':sha(B/'ERRATA_v01.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'eta_star_exact':str(eps),'radius_star_exact':str(rs),'old_radius_rate_exact':str(beta0),'old_radius_tolerance_exact':str(beta0*r0),'old_radius_tolerance_loss_exact':str(loss),'relative_tolerance_gain_exact':str(ratio),'other_norm_optimum_square_exact':str(emax2),'007_forcing_failure_factor_strict_lower_exact':str(factor),'frozen_current_report_raw_sha256':source['raw_sha256'],'foreign_code_executed':False,'candidate_integrals':False,'verdict':'CONFIRMED T2 reciprocal T4-479 review and current g=0 repair. Maximum is of the stated sufficient self-map expression at fixed s and weights; inverse/background premises and normalized domain retained. No candidate closure, global theorem optimum or cross-norm ranking.'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',result['elapsed_seconds'],'seconds')
