"""Independent exact composition and width allocation audit. No peer execution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,time,sys
sys.set_int_max_str_digits(0);B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();hx=lambda q:hashlib.sha256(str(q).encode()).hexdigest()
def ck(v,label):
 assert v,label
 checks.append(label)
def read(p):return json.loads((B/p).read_text())
for r in read('data/manifest.json'):ck(sha(B/r['local'])==r['sha256'],'binding '+r['local'])
ck(read('data/PROOF_FIRST.json')['checker_exists'] is False,'proof before checker')
x=read('source/T1_extract.json');widths=[];accepted=[];split_names=[];old=read('../candidate016_complete_bounds_reciprocal/verification/result.json')
for P,topic,kt,km in [(47,'candidate016_prefix47_replay_audit','tail_v04','multi_v02'),(63,'candidate016_prefix63_replay_audit','tail_v05','multi_v03')]:
 v=str(4 if P==47 else 5).zfill(2);w=str(2 if P==47 else 3).zfill(2)
 t=read('../'+topic+'/source/N4_prefix_v'+v+'.json');m=read('../'+topic+'/source/N4_complete_v'+w+'.json');a=read('../'+topic+'/verification/result.json');N=P+2
 for key,z in [(kt,t),(km,m)]:
  source=B/('../'+topic+'/source/'+('N4_prefix_v'+v+'.json' if key==kt else 'N4_complete_v'+w+'.json'));ck(sha(source)==x['sources'][key]['sha256'],'T1 original hash '+key)
  for k,val in x['records'][key].items():
   if k.endswith('_exact_sha256'):ck(hx(Q(z[k[:-7]]))==val,'long exact extract '+key+'/'+k)
   elif k in z and k not in ['inputs','display_bounds_exact']:ck(z[k]==val,'verbatim extract '+key+'/'+k)
  for k,val in x['records'][key]['inputs'].items():ck(z['inputs'][k]==val,'producer input '+key+'/'+k)
  if key==km:ck(z['display_bounds_exact']==x['records'][key]['display_bounds_exact'],'display extract '+key)
 q={int(z['n']):(Q(z['q_lower_exact']),Q(z['q_upper_exact'])) for z in t['modes']};qx={int(n):(Q(lo),Q(lo)+Q(wd)) for n,lo,wd in x['q_modes_tail_v05']};ck(set(q)==set(range(1,P+1,2)),'complete prefix '+str(P))
 for n,(lo,hi) in q.items():ck((lo,hi)==qx[n] and 0<lo<hi and hi-lo<Q(1,10**510),'exact mode '+str(P)+'/'+str(n))
 sr=Q(t['full_rF_square_upper_exact']);sl=Q(t['full_rF_square_lower_exact']);vl=sr/N**2+sum((Q(1,n*n)-Q(1,N*N))*hi for n,(lo,hi) in q.items());sp=sum(hi/n**2 for n,(lo,hi) in q.items())+(sr-sum(lo for lo,hi in q.values()))/N**2
 ck(vl==Q(t['M2_upper_exact'])==Q(m['complete_M2_upper_exact'])==Q(a['M2_producer_upper_exact']),'positive complete upper '+str(P));ck(sp-vl==sum(hi-lo for lo,hi in q.values())/N**2>0,'strict split difference '+str(P));stored=Q(t['split_formula_upper_exact']);ck(stored in [sp,vl],'stored split field identified '+str(P));split_names.append({'prefix':P,'stored_is_split':stored==sp,'stored_is_positive':stored==vl,'strict_difference_exact':str(sp-vl)})
 ck(sl-sum(hi for lo,hi in q.values())==Q(t['tail_rF_square_lower_exact'])>0,'tail lower '+str(P));ck(sr-sum(lo for lo,hi in q.values())==Q(t['tail_rF_square_upper_exact']),'tail upper '+str(P))
 selected=m['selected_modes'];ell={int(z['n']):Q(z['selected_lower']) for z in selected};j={int(z['n']):Q(z['selected_improvement']) for z in selected};ck(set(ell)==set(j)==set(range(1,32,2)),'sixteen distinct trial modes '+str(P));low=sum(z*z for z in ell.values());upper=vl-sum(j.values());ck(low==Q(m['H_lower_square_exact'])==Q(a['H_lower_square_exact']),'dual lower square '+str(P));ck(upper==Q(m['H_upper_square_exact'])==Q(a['H_upper_square_exact']),'solenoidal upper square '+str(P));g={n:q[n][1]/n**2-j[n]-ell[n]**2 for n in ell}
 for n,gap in g.items():
  ck(gap>0,'positive retained gap '+str(P)+'/'+str(n));base=ell[n]**2;top=q[n][1]/n**2-j[n]
  for frac in [Q(1,4),Q(3,4)]:
   value=base+frac*gap;ck(base<value<top and (top-value)+(value-base)==gap,'interval allocation '+str(P)+'/'+str(n)+'/'+str(frac))
 retained=sum(g.values());rest=(sr-sum(q[n][1] for n in ell))/N**2+sum((Q(1,n*n)-Q(1,N*N))*q[n][1] for n in range(33,P+1,2));total=upper-low;ck(total==retained+rest and rest>0,'exact width decomposition '+str(P));share=retained/total;lo,hi=(Q('.681'),Q('.682')) if P==47 else (Q('.682'),Q('.6835'));ck(lo<share<hi,'strict rational share bracket '+str(P));ck(Q(2,3)<share<Q(7,10),'two thirds of present width retained '+str(P))
 for k in ['H_strict_lower_exact','H_strict_upper_exact','E2_strict_lower_exact','E2_strict_upper_exact','E2_lower_square_exact','E2_upper_square_exact']:ck(Q(m[k])==Q(a[k]),'accepted endpoint '+str(P)+'/'+k)
 ck(0<Q(m['H_strict_lower_exact'])**2<low<upper<Q(m['H_strict_upper_exact'])**2,'strict H enclosure '+str(P));ck(Q(m['E2_strict_lower_exact'])**2<Q(m['E2_lower_square_exact'])<Q(m['E2_upper_square_exact'])<Q(m['E2_strict_upper_exact'])**2,'strict E2 enclosure '+str(P))
 ck(Q(m['H007_minus_H016_strict_lower_exact'])==Q(a['strict_H_gap_lower']) and Q(m['E2016_minus_E2007_strict_lower_exact'])==Q(a['strict_E2_gap_lower']),'accepted actual norm gaps '+str(P));widths.append({'prefix':P,'width_exact':str(total),'retained_gap_exact':str(retained),'other_terms_exact':str(rest),'share_exact':str(share),'strict_share_lower':str(lo),'strict_share_upper':str(hi),'share_approximate':float(share),'attribution_to_lower_or_upper_slack':'OPEN'});accepted.append(a)
ck(Q(accepted[1]['H_strict_upper_exact'])<Q(accepted[0]['H_strict_upper_exact'])<Q(old['H_strict_upper_exact']),'H upper nested');ck(Q(accepted[1]['E2_strict_upper_exact'])<Q(accepted[0]['E2_strict_upper_exact'])<Q(old['E2_strict_upper_exact']),'E2 upper nested')
text=(B/'source/R1_054.md').read_text();ck('so the remaining width comes mostly from the lower bound (the dual' in text,'exact attribution under review');ck('272 checks' in text and 'RESULT PASS' in (B/'source/T1_checker.log').read_text(),'producer execution identified');ck(all(z['stored_is_split'] for z in split_names),'R1-054 stored split value statement true')
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'review_sha256':sha(B/'source/R1_054.md'),'widths':widths,'stored_split_fields':split_names,'confirmed':'Exact finite recomposition, retained tail, accepted H/E2 endpoints and ordering, exact width identity and more than two thirds retained in modes1..31.','refuted_inference':'The width identity by itself identifies the majority as dual lower slack. Actual division between upper and lower slack is OPEN.','new_candidate_integrals':False,'foreign_code_executed':False}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',r['utc'],r['elapsed_seconds'],'seconds')
for z in widths:print(z['prefix'],z['share_approximate'],z['strict_share_lower'],z['strict_share_upper'])
