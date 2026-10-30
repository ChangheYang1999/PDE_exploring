"""Finite reciprocal comparison; no peer execution and no source integration."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import json,re,sys,time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3]; B=R/'research/candidate016_final_reciprocal'
def sha(p):return sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic(); mf=json.loads((B/'source/MANIFEST.json').read_text()); inputs={};external={};checks={}
 def need(k,v):
  assert v,k
  checks[k]=True
 def bind(p,h=None):
  p=p.resolve();actual=sha(p)
  need('hash '+str(p),h is None or actual==h)
  (inputs if p.is_relative_to(R) else external)[str(p.relative_to(R)) if p.is_relative_to(R) else str(p)]=actual
 def read(name):
  e=mf['files'][name];p=R/e['local_path'] if 'local_path' in e else B/'source'/name
  bind(p,e['sha256']);return json.loads(p.read_text())
 for name,e in mf['files'].items():bind(R/e['local_path'] if 'local_path' in e else B/'source'/name,e['sha256'])
 need('proof precedes checker',not mf['checker_exists'] and sha(B/'PROOF.md')==mf['proof_sha256'])
 for p in [B/'PROOF.md',B/'source/MANIFEST.json',Path(__file__)]:bind(p)
 for n in ['486','488']:
  m=read(f'T4_{n}_manifest.json');root=(R/mf['files'][f'T4_{n}_manifest.json']['original_base']).resolve()
  for row in m:bind(root/row['local'],row['sha256'])
 a=read('T4_486_result.json');b=read('T4_488_result.json');c=read('N4_418');d=read('N4_417');prod=read('N4_416');base=read('N4_252')
 for name,x,count in [('486',a,13380),('488',b,121),('418',c,4430),('417',d,2065),('416',prod,6925)]:
  need(name+' count',x['check_count']==len(x['checks'])==count)
  if isinstance(x['checks'],dict):need(name+' passed',all(x['checks'].values()))
  need(name+' candidate',x['candidate']=='C1-N1-016-legqs25-quot013' and x['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42')
 need('2130groups1224labels',a['saved_group_count']==c['pairing_group_count']==2130 and a['coefficient_count']==1224)
 need('no peer execution',a['foreign_code_executed'] is False and b['foreign_code_executed'] is False and c['peer_code_executed'] is False)
 need('no new integrals',a['candidate_moment_integrals_repeated'] is False and b['new_candidate_integrals'] is False and c['new_source_integrals'] is False)
 need('full160tail144',b['complete_field_mode_count']==160 and b['omitted_modes_retained']==144 and c['all160_source_modes_covered'] is True and c['general_and_tail_reviews_completed'] is True)
 need('sixteen distinct frequencies',[r['n'] for r in a['rows']]==[r['n'] for r in c['selected_modes']]==list(range(1,32,2)))
 L=J=Q(0)
 for x,y in zip(a['rows'],c['selected_modes']):
  n=x['n'];lo=Q(x['selected_lower_floor']);im=Q(x['selected_cross_floor'])
  need(f'n{n} same positive lower',lo==Q(y['selected_lower'])>0)
  need(f'n{n} same positive improvement',im==Q(y['selected_improvement'])>0)
  L+=lo**2;J+=im
 need('same lower square',L==Q(a['H_lower_square_exact'])==Q(b['H_lower_square_exact'])==Q(c['H_lower_square_exact'])==Q(d['H_lower_square_exact']))
 need('same improvement',J==Q(a['improvement_sum_strict_lower_exact'])==Q(c['selected_improvement_sum_lower_exact'])==Q(d['selected_improvement_sum_lower_exact']))
 V0=Q(a['M2_upper_exact']);V=Q(c['complete_M2_upper_exact']);delta=V-V0
 need('positive sub1e500 difference',0<delta<Q(1,10**500) and delta==Q(b['producer_M2_minus_independent_M2_exact']))
 need('producer upper identity',V-J==Q(b['H_upper_square_exact'])==Q(c['H_upper_square_exact'])==Q(d['improved_H_square_upper_exact']))
 need('independent upper identity',V0-J==Q(a['H_upper_square_exact']))
 need('upper energy difference',Q(c['E2_upper_square_exact'])-Q(a['E2_upper_square_exact'])==Q(20,21)*2**18*delta)
 for key in ['H_lower_square_exact','H_upper_square_exact','E2_lower_square_exact','E2_upper_square_exact','H_strict_lower_exact','H_strict_upper_exact','E2_strict_lower_exact','E2_strict_upper_exact']:
  need('488418same '+key,Q(b[key])==Q(c[key]))
 need('lower energy identity',Q(a['E2_lower_square_exact'])==Q(c['E2_lower_square_exact']))
 for name,x in [('486',a),('488',b),('418',c)]:
  for norm in ['H','E2']:
   lo,up=[Q(x[norm+'_strict_'+s+'_exact']) for s in ['lower','upper']]
   need(name+' '+norm+' strict squares',0<lo**2<Q(x[norm+'_lower_square_exact'])<Q(x[norm+'_upper_square_exact'])<up**2)
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',base['H_input_lower_ball']);need('007Hexactball',m is not None)
 h07=Q(m[1])-Q(m[2]);e07=Q(base['E_upper']['strict_upper_exact'])
 need('007E2same',e07==Q('606.820219')==Q(a['007_E2_upper_exact']))
 hg=h07-Q(c['H_strict_upper_exact']);eg=Q(c['E2_strict_lower_exact'])-e07
 need('complete E2gap',eg==Q('21.759869526341')==Q(b['strict_E2_gap_lower'])==Q(c['E2016_minus_E2007_strict_lower_exact']))
 need('complete Hgap',hg==Q(b['strict_H_gap_lower'])==Q(c['H007_minus_H016_strict_lower_exact'])>Q('.017571422145091'))
 # The proof establishes these slightly shorter display intervals independently.
 need('short completeHdisplay',Q('.616733500')**2<L<V-J<Q('.617952954')**2)
 need('short completeE2display',Q('628.580088')**2<Q(c['E2_lower_square_exact'])<Q(c['E2_upper_square_exact'])<Q('628.879025')**2)
 for p,h in inputs.items():assert sha(R/p)==h
 for p,h in external.items():assert sha(Path(p))==h
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'inputs':inputs,'external_readonly_bindings':external,'candidate':c['candidate'],'raw_sha256':c['raw_sha256'],'H_lower_square_exact':str(L),'H_upper_square_exact':str(V-J),'upper_enclosure_difference_exact':str(delta),'strict_H_gap_lower':str(hg),'strict_E2_gap_lower':str(eg),'verdict':'CONFIRMED reciprocal finite comparison of T4-486/488 and N4-416/417/418. No source integral or peer program was executed; existing source and analytic premises retained.'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'local',len(external),'readonly peer bindings',out['elapsed_seconds'],'seconds','sha',sha(p))
if __name__=='__main__':main()
