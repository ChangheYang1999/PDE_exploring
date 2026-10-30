"""Independent exact-radius endpoint row; no peer program or spatial integral."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];ctx.prec=768
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();read=lambda rel:json.loads((B/rel).read_text())
def A(q):q=Q(q);return arb(q.numerator)/q.denominator
def main():
 tick=time.monotonic();checks={}
 def ck(k,t):assert k not in checks and t,k;checks[k]=True
 m=read('data/manifest.json')
 for z in m:ck('binding:'+z['local'],sha(B/z['local'])==z['sha256'])
 p=read('data/parameters.json');ep=read('data/endpoint_parameters.json');peer=read('source/T2_result.json');old=read('source/reach_result.json');families=read('source/family_result.json');external=read('data/external_bindings.json')
 ck('peer17checks',peer['checks']==17 and peer['fails']==[])
 ck('external_observation',len(external['inputs'])==len(peer['inputs'])==12 and external['all_matched'] and all(x['sha256']==x['observed'] for x in external['inputs']))
 ck('accepted_reach_pair',old['proof_sha256']==sha(B/'source/reach_PROOF.md') and old['check_count']==948)
 ck('accepted_family_pair',families['proof_sha256']==sha(B/'source/family_PROOF.md') and families['check_count']==166)
 c=Q(ep['c']);q=1/c-4;d=1-1/c;D=5*c-1;alpha=-2*q-2;S=2*d*d/(alpha*(alpha+d)*(alpha+2*d));emin=(-q-1)/(2*(-q)*(-q-3));exponent=d/(-q-1)
 ck('positive_constants',-5<q<-3 and min(d,D,alpha,S,exponent)>0)
 ck('exact_shape_identity',S==1/alpha-2/(alpha+d)+1/(alpha+2*d))
 ck('universal_floor',emin>Q(p['test_floor']))
 bsq=4*Q(297,1000)**3/(27*4800*25*512**2);b=A(bsq).sqrt();f=next(r for r in families['rows'] if r['name']=='TB-rebal')
 ck('independent_exact_supremum_square',bsq==Q(p['exact_square'])==Q(f['supremum_square_exact']))
 lo,hi=map(Q,p['new']);ck('exact_bracket_by_squares',0<lo and lo*lo<bsq<hi*hi);ck('peer_exact_radius',b.overlaps(arb(peer['at_exact_b_fam']['b_fam'])) and b.overlaps(arb(f['supremum'])))
 ranges={'old_interval':tuple(A(x) for x in p['old']),'new_interval':tuple(A(x) for x in p['new']),'at_exact_b_fam':(b,b)};rows=[];displaycount=0
 for name,angle in ep['angles'].items():
  z=read(f'data/{name}_endpoint.json');coef={int(n):Q(v) for n,v in z['F12'].items()};pol={int(n):Q(v) for n,v in z['P'].items()};theta={int(n):Q(v) for n,v in z['Theta0'].items()}
  ck(name+':same_c',Q(z['c'])==c)
  ns=set(coef)|set(pol);pp=sum(pol.get(n,0)**2 for n in ns);proj=sum(coef.get(n,0)**2 for n in ns)-sum(coef.get(n,0)*pol.get(n,0) for n in ns)**2/pp
  ck(name+':positive_projection',pp>0 and proj>0);bv=(arb.pi()*A(proj)).sqrt()/(4*A(c));ang=A(angle)
  def ev(dic,deriv=False):return sum((A(v)*n*(n*ang).cos() if deriv else A(v)*(n*ang).sin()) for n,v in dic.items())
  av,ad,pv,pd=ev(coef),ev(coef,True),ev(pol),ev(pol,True);den=A(q*q)*pv*pv+pd*pd;ck(name+':Phi_denominator',den>0)
  phi=abs(A(q)*(av*pd-ad*pv))/(4*A(c)*den.sqrt());g0=sum(n*v for n,v in theta.items());power=1/c+2;v0=abs((power-1)*sum(n*v/(power*power-n*n) for n,v in theta.items()));H0=A(ep['H0'][name])
  ck(name+':positive_endpoint_data',phi>H0>0 and g0>0 and v0>0)
  prior=next(x for x in old['rows'] if x['candidate']==name)
  ck(name+':prior_B_Phi',bv.overlaps(arb(prior['B'])) and phi.overlaps(arb(prior['Phi'])))
  ck(name+':prior_exact_g0_v0',g0==Q(prior['g0_exact']) and v0==Q(prior['v0_exact']))
  def crit(beta,H,v,shape=True):return A(D)*bv/((2*arb.pi()).sqrt()*H*A(g0))*(bv*(A(S).sqrt() if shape else 1/A(alpha).sqrt())/beta)**A(exponent)-A(v/g0)
  def values(l,h):return {'shape_H0_V0_upper':crit(l,H0,Q(0)),'shape_Phi_V0_upper':crit(l,phi,Q(0)),'shape_Phi_V0_lower_at_beta_upper':crit(h,phi,Q(0)),'shape_Phi_Vv0_upper':crit(l,phi,v0),'shape_Phi_Vv0_lower_at_beta_upper':crit(h,phi,v0),'crude_Phi_V0_upper':crit(l,phi,Q(0),False),'crude_H0_V0_upper':crit(l,H0,Q(0),False)}
  results={label:values(l,h) for label,(l,h) in ranges.items()}
  for label,vs in results.items():
   saved=peer[label]['per_candidate'][name]
   for key,v in vs.items():
    bound=Q(saved[key]);lower='lower' in key;ck(name+':'+label+':'+key,v>A(bound) if lower else v<A(bound));displaycount+=1
   ck(name+':'+label+':retained_shape_exclusion',saved['class_1'] and vs['shape_Phi_V0_upper']<A(p['test_floor'])<A(emin))
   ck(name+':'+label+':crude_insufficient',crit(ranges[label][1],phi,Q(0),False)>A(emin))
  for lab,caps in [('new_interval',p['new_common']),('at_exact_b_fam',p['exact_common'])]:
   vs=results[lab]
   for key,bound,lower in [('shape_Phi_V0_upper',caps[0],False),('shape_Phi_Vv0_lower_at_beta_upper',caps[1],True),('shape_Phi_Vv0_upper',caps[2],False),('crude_Phi_V0_upper',caps[3],False)]:ck(name+':'+lab+':common:'+key,vs[key]>A(bound) if lower else vs[key]<A(bound))
  for key in results['old_interval']:
   ck(name+':monotone_repair:'+key,results['old_interval'][key]>results['new_interval'][key])
  ck(name+':old_upper_conservative_at_exact',results['old_interval']['shape_Phi_V0_upper']>results['at_exact_b_fam']['shape_Phi_V0_upper'])
  if name=='007':ck('007:old_lower_refuted',results['at_exact_b_fam']['shape_Phi_Vv0_upper']<A('0.6372612')<A('0.6372628'))
  rows.append({'candidate':name,'B':bv.str(90),'Phi':phi.str(90),'g0_exact':str(g0),'v0_exact':str(v0),'rows':{lab:{key:v.str(90) for key,v in vals.items()} for lab,vals in results.items()}})
 ck('all63_displayed_bounds',displaycount==63)
 note=(B/'source/revision3.md').read_text()
 for literal in ['0.6720590','0.6372593','0.6372977','1.000026','0.6720573','0.6372611','0.6372960','1.000024','The old upper bounds remain valid','No verdict changes']:ck('printed_note:'+literal,literal in note)
 for z in m:ck('unchanged:'+z['local'],sha(B/z['local'])==z['sha256'])
 result={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'exact_ceiling_square':str(bsq),'exact_ceiling':b.str(100),'Emin_exact':str(emin),'displayed_endpoint_count':displaycount,'rows':rows,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'elapsed_seconds':time.monotonic()-tick,'foreign_code_executed':False,'spatial_integrals_repeated':False,'verdict':'CONFIRMED TB-rebal revision3 directed row repair and retained-shape certificate obstruction at exact ceiling. REFUTED old007 lower endpoint at exact ceiling. Crude test insufficient; no profile nonexistence or existence.'}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],'CHECKS',len(checks),'SECONDS',result['elapsed_seconds'],'SHA',sha(B/'verification/result.json'))
if __name__=='__main__':main()
