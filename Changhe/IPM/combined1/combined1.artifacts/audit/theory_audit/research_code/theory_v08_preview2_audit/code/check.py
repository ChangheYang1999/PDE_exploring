from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,re,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[]
def check(s,v):
 assert bool(v),s
 checks.append(s)
def C(x):
 v=Q(str(x));return arb(v.numerator)/v.denominator
def enc(x):return x.str(65)
p=json.loads((B/'data/parameters.json').read_text());m=json.loads((B/'data/manifest.json').read_text())
for f,h in m['inputs'].items():check('hash '+f,sha(B/f)==h)
check('proof created before checker',m['proof_written_before_code'])
prev=(B/'source/preview2.md').read_text();flat=' '.join(prev.split());proof=(B/'PROOF.md').read_text()
check('exact preview',sha(B/'source/preview2.md')==p['preview_sha256']);check('868 lines',len(prev.splitlines())==868)
changes=(B/'source/word_changes.txt').read_text();check('127 changed blocks',len(re.findall(r'^CHANGE ',changes,re.M))==127)
old={r['row']:r for r in json.loads((B/'source/preview1_result.json').read_text())['factor_rows']};rows={r['id']:r for r in p['table_rows']}
check('24 rows',len(rows)==24)
for rid,r in rows.items():
 for k in ['p','t','factor']:check(rid+' unchanged '+k,Q(r[k])==Q(old[rid][k]))
 k=len(r['factor'].split('.')[1]);ratio=Q(r['p'])/Q(r['t']);fl=(ratio*10**k).__floor__()/Q(10**k)
 check(rid+' downward rounding',fl==Q(r['factor']) and fl>1)
 check(rid+' appears in text',any(x.startswith('| '+rid+' |') and r['factor'] in x for x in prev.splitlines()))
par=json.loads((B/'data/reach_parameters.json').read_text());c=Q(par['c']);q=1/c-4;d=1-1/c;D=5*c-1;a=-2*q-2;e=d/(-q-1);S=2*d*d/(a*(a+d)*(a+2*d));emin=(-q-1)/(2*(-q)*(-q-3))
check('positive constants',-5<q<-3 and min(d,D,a,e,S)>0);check('exact integral identity',S==1/a-2/(a+d)+1/(a+2*d))
peer=json.loads((B/'source/thresholds_result.json').read_text());t2=json.loads((B/'source/T2_factors_result.json').read_text())
check('peer thresholds source matches T2',sha(B/'source/thresholds_result.json')==t2['inputs']['c1-t2/artifacts/data/falsify_section0_results.json'])
selected={x['label']:x for x in par['targets'] if x['label'] in ['sharpw_fixed','sharpw_family','TB_sharp','graded']};check('four target labels',len(selected)==4)
values={};outputs=[]
for name in ['007','013','014']:
 ep=json.loads((B/f'data/{name}_endpoint.json').read_text());check(name+' c',Q(ep['c'])==c)
 A={int(n):Q(v) for n,v in ep['F12'].items()};P={int(n):Q(v) for n,v in ep['P'].items()};ns=set(A)|set(P)
 pp=sum(P.get(n,0)**2 for n in ns);proj=sum(A.get(n,0)**2 for n in ns)-sum(A.get(n,0)*P.get(n,0) for n in ns)**2/pp
 check(name+' projection positive',pp>0 and proj>0);bb=(arb.pi()*C(proj)).sqrt()/(4*C(c));angle=C(par['angles'][name])
 def v(t,der=False):return sum((C(x)*n*(n*angle).cos() if der else C(x)*(n*angle).sin()) for n,x in t.items())
 av,ap,pv,pd=v(A),v(A,True),v(P),v(P,True);den=C(q*q)*pv*pv+pd*pd;check(name+' denominator',den>0)
 phi=abs(C(q)*(av*pd-ap*pv))/(4*C(c)*den.sqrt());g0=C(sum(int(n)*Q(x) for n,x in ep['Theta0'].items()));h0=C(par['H0'][name]);check(name+' H0 Phi',phi>h0>0 and g0>0)
 def crit(beta,H,shape=True):return C(D)*bb/((2*arb.pi()).sqrt()*H*g0)*(bb*(C(S).sqrt() if shape else 1/C(a).sqrt())/C(beta))**C(e)
 output={'candidate':name,'B':enc(bb),'Phi':enc(phi),'targets':{}}
 for label,t in selected.items():
  pr=peer['B']['radii'][t['peer_label']]['per_candidate'][name];lo,hi=Q(t['lower']),Q(t['upper']);vv={'crude_H0_V0_upper':crit(lo,h0,False),'shape_H0_V0_upper':crit(lo,h0),'shape_Phi_V0_upper':crit(lo,phi)}
  for k,val in vv.items():check(name+' '+label+' bound '+k,val<C(pr[k]))
  check(name+' '+label+' universal exclusion',vv['crude_H0_V0_upper']<C(emin))
  values[(name,label)]=(vv,pr,lo,hi);output['targets'][label]={k:enc(v) for k,v in vv.items()}
 outputs.append(output)
br=json.loads((B/'source/brackets_result.json').read_text());check('brackets accepted',br['check_count']==166)
for label,n in [('sharpw_family','sharpw'),('TB_sharp','TB-sharp')]:
 rr=next(r for r in br['rows'] if r['name']==n);t=selected[label];lo,hi=Q(t['lower']),Q(t['upper']);sq=Q(rr['supremum_square_exact'])
 check(label+' exact rational bracket',lo*lo<sq<hi*hi)
gsq=Q(2500,651**2*28248);gg=selected['graded'];check('graded rational-square bracket',Q(gg['lower'])**2<gsq<Q(gg['upper'])**2)
spec={'U2':('sharpw_family','crude_H0_V0_upper'), 'U3':('TB_sharp','crude_H0_V0_upper'), 'U4':('graded','crude_H0_V0_upper'),'P1':('graded','shape_H0_V0_upper'),'P2':('graded','shape_H0_V0_upper'),'P4':('sharpw_family','shape_H0_V0_upper'),'P5':('TB_sharp','shape_H0_V0_upper'),'R2':('sharpw_family','shape_Phi_V0_upper'),'R3':('TB_sharp','shape_Phi_V0_upper')}
factors={}
for rid,(label,key) in spec.items():
 r=rows[rid];vv,pr,lo,hi=values[('007',label)];room=rid.startswith('R');t=max(Q(r['t']),Q(pr[key])-(Q('0.372') if room else 0));pl=C(r['p'])*((C(lo/hi)**C(e)) if room else 1);ratio=pl/C(t);target=p['new_factors'][rid]
 check(rid+' exact-ceiling factor',ratio>C(target));check(rid+' peer factor agreement',Q(t2['C'][rid]['factor_lo'])==Q(target));factors[rid]={'lower_ratio':enc(ratio),'printed_floor':target,'threshold_upper_exact':str(t),'numerator_lower':enc(pl)}
 if room:
  th=max(Q(r['t']),Q(pr['shape_H0_V0_upper'])-Q('0.372'));rh=pl/C(th);target=p['H0_factors'][rid];check(rid+' H0-only factor',rh>C(target));check(rid+' H0 peer agreement',Q(t2['C'][rid]['factor_lo_H0'])==Q(target));factors[rid]['H0_only_ratio']=enc(rh)
r1=C(rows['R1']['p'])/C(Q(rows['P3']['t'])-Q('0.372'));check('R1 H0-only',r1>C(p['H0_factors']['R1']));check('R1 H0 peer agreement',Q(t2['C']['R1']['factor_lo_H0'])==Q(p['H0_factors']['R1']))
for s in ['registered scalar ball and original graded box','No dyadic verdict is promised in advance','which are requirements of those certificates, not of every framework','c1-t4 T4-443 has audited','change no candidate exclusion or verdict','DK is the derivative of the velocity kernel K','K2 and K3 are not evaluated below the printed targets','Emin is a lower bound on valid constants, not a proved admissible constant']:
 check('scope repair '+s,s in flat)
w=json.loads((B/'source/026_result.json').read_text());flo=Q(w['strict_lower_exact']);check('026 accepted raw hash in proof',w['source_sha256'] in proof)
check('026 floor',flo==Q('0.001355907204057457'));check('026 scalar floor',flo>Q('3.7930e-6'));check('026 graded floor',flo>Q(25,54684))
check('026 preview floor',str('0.001355907204057457') in flat);check('026 n K',w['n']==19 and w['K']==1800 and w['precision_bits']==2048)
force=json.loads((B/'source/forcing_result.json').read_text());check('451 accepted finite count',force['check_count']==318)
app=json.loads((B/'data/appendix_bindings.json').read_text())['rows'];matches=0
for r in app:
 if r['status']=='matched':check('appendix '+r['source'],sha(B/r['local'])==r['claimed_sha256']);matches+=1
 else:check('mutable report recorded '+r['source'],r['status']=='changed since generation' and r['current_sha256']!=r['claimed_sha256'])
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'factor_count':len(rows),'exact_ceiling_factors':factors,'R1_H0_only':enc(r1),'candidate_thresholds':outputs,'appendix_count':len(app),'appendix_matches':matches,'historical_mutable_references':[r for r in app if r['status']!='matched'],'preview_sha256':p['preview_sha256'],'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED changed mathematics and scoped exact-ceiling factors; publication status updates identified'}
(B/'verification/result.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS',len(checks),result['utc'],result['elapsed_seconds'])
for rid,r in factors.items():print(rid,r['printed_floor'],r['lower_ratio'])
