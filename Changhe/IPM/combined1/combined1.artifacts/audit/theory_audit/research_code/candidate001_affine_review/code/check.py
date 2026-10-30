"""Finite acceptance of two independent reviews and the explicit changed-c test."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from hashlib import sha256
from datetime import datetime,timezone
import json,time
B=Path(__file__).resolve().parents[1]
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def read(s):return json.loads((B/s).read_text())
def main():
 tick=time.monotonic();checks={}
 def ck(k,t):assert k not in checks and t,k;checks[k]=True
 manifest=read('data/manifest.json')
 for z in manifest:ck('binding:'+z['local'],sha(B/z['local'])==z['sha256'])
 own=read('source/application_result.json');peer=read('source/T2_result.json');obs=read('data/external_bindings.json');lc=read('source/leading_coefficients.json');raw=read('source/raw.json');n4=read('source/N4_result.json')
 ck('application_proof_hash',own['proof_sha256']==sha(B/'source/application_PROOF.md')=='771ad6b4af564e1b3a0acf1284184fd8f36c15d2dd090212370122d433789a3e')
 ck('application_checker',own['checker_sha256']==sha(B/'source/application_check.py'))
 ck('application_coefficients',own['coefficient_sha256']==sha(B/'source/leading_coefficients.json')=='9829a3563bea97194c50ac752643a658a59112c6bbf5a050e7c4e774c9db371a')
 ck('application_raw',own['raw_sha256']==sha(B/'source/raw.json')=='8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7')
 ck('application_pass',own['check_count']==len(own['checks'])==len(set(own['checks']))==896 and own['fixed_c_no_L2_application'].startswith('CONFIRMED') and own['any_real_c_application'].startswith('CONFIRMED'))
 mapping={'PROOF.md':'application_PROOF.md','verification/result.json':'application_result.json','code/check.py':'application_check.py','data/leading_coefficients.json':'leading_coefficients.json','source/raw.json':'raw.json','source/annular_PROOF.md':'annular_PROOF.md','source/generator_PROOF.md':'generator_PROOF.md','source/N4_result.json':'N4_result.json'}
 for rel,h in peer['inputs'].items():
  suffix=rel.split('candidate001_affine_exclusion/',1)[1];ck('T2_target:'+suffix,sha(B/'source'/mapping[suffix])==h)
 ck('ten_external_observations',len(obs['inputs'])==10 and obs['all_matched'] and all(x['sha256']==x['observed'] for x in obs['inputs']))
 for i,z in enumerate(obs['inputs']):ck('external_is_frozen:'+str(i),z['sha256'] in [v['sha256'] for v in manifest])
 ck('T2_pass',peer['checks']==30 and peer['fails']==[])
 t1=(B/'source/T1_review.md').read_text();t2=(B/'source/T2_review.md').read_text();log1=(B/'source/T1_check.out').read_text();log2=(B/'source/T2_check.log').read_text()
 for literal in ['checks passed 912','RESULT PASS','[21, 23, 25, 27, 29, 31, 33, 35, 37, 39]']:ck('T1_log:'+literal,literal in log1)
 ck('T2_log_pass','checks: 30, failed: 0' in log2 and 'FAIL ' not in log2)
 for name,txt in [('T1',t1),('T2',t2)]:
  ck(name+':same_PROOF',sha(B/'source/application_PROOF.md') in txt)
  ck(name+':verdict','CONFIRMED' in txt and 'every real c' in txt)
 ck('T1_script_and_log_named',sha(B/'source/T1_check.py') in t1 and sha(B/'source/T1_check.out') in t1)
 ck('T1_explicit_G0_test','with E replaced by G_0 and q by gamma' in t1)
 ck('T2_wording_request','angular factor of the test' in t2 and 'G_0 instead of E' in t2)
 c=Q(raw['cl_exact']);g=1/c;d=1-g;q=2*g-1
 ck('exact_parameters',c==Q(lc['c_exact'])==Q(4076476460239181,2251799813685248) and g==Q(lc['gamma_exact']) and q==Q(lc['q_exact'])==Q(427123167131315,4076476460239181))
 ck('ordered_exponents',0<q<g<1 and d>0 and g-1<q)
 ck('leading_linear_cancellation',c*g==1)
 ck('all_lower_labels_by_two_extrema',max(g-2*d,g-2)<q)
 gens=raw['generators'];ck('860_generators',len(gens)==860)
 C=defaultdict(lambda:defaultdict(Q))
 for i,z in enumerate(gens):
  s=z['spec'];ck('generator:'+str(i),z['j'] in range(4) and z['m'] in range(10) and ((s[0]=='mono' and len(s)==2) or (s[0]=='leg' and len(s)==3)) and all(isinstance(x,int) and x>=0 for x in s[1:]))
  C[z['j']][2*z['m']]+=Q(z['coef'])
 for j in range(4):ck('raw_branch_sum:'+str(j),{str(n):str(v) for n,v in sorted(C[j].items()) if v}==lc['leading_potential'][str(j)])
 E={int(n):Q(v) for n,v in lc['E10'].items() if Q(v)};G={int(n):Q(v) for n,v in lc['density']['0'].items() if Q(v)};G1={int(n):Q(v) for n,v in lc['density']['1'].items() if Q(v)}
 ck('all_E_modes',sorted(E)==list(range(21,40,2))==peer['E_modes'])
 ck('all_G0_modes',sorted(G)==list(range(1,20,2))==peer['G0_modes'])
 ck('all_G1_modes',sorted(G1)==list(range(1,20,2)))
 ck('full_sector_agreement',E=={int(n):Q(v) for n,v in n4['first_nonzero_sector']['sine_coefficients'].items() if Q(v)})
 ck('full_sector_exponent',Q(n4['first_nonzero_sector']['exponent'])==q and (n4['first_nonzero_sector']['h'],n4['first_nonzero_sector']['q'])==(1,0))
 e2=sum(v*v for v in E.values());g2=sum(v*v for v in G.values());cross=sum(v*G.get(n,0) for n,v in E.items())
 ck('positive_E_square',e2==Q(lc['E10_sum_squares_exact']) and e2>0 and E[21]!=0)
 ck('positive_G0_square',g2>0)
 ck('wrong_test_leading_pairing_zero',cross==0)
 ck('changed_c_right_pairing_positive',g*g2>0)
 ck('constant_velocity_lower_order',g-1<q<g and g-2<0)
 err=(B/'source/application_ERRATA_v01.md').read_text()
 for s in ['phi_R=R^-1 eta(r/R)G0(theta)','replacing both q by','gamma and E by G0','absolute value diverges']:ck('erratum:'+s,s in err)
 for z in manifest:ck('unchanged:'+z['local'],sha(B/z['local'])==z['sha256'])
 result={'utc':datetime.now(timezone.utc).isoformat(),'check_count':len(checks),'checks':checks,'elapsed_seconds':time.monotonic()-tick,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'original_application_sha256':sha(B/'source/application_PROOF.md'),'erratum_sha256':sha(B/'source/application_ERRATA_v01.md'),'T1_review_sha256':sha(B/'source/T1_review.md'),'T2_review_sha256':sha(B/'source/T2_review.md'),'E_norm_square_div_pi_exact':str(e2),'G0_norm_square_div_pi_exact':str(g2),'E_G0_inner_product_div_pi_exact':str(cross),'exponents':{'c0':str(c),'gamma':str(g),'q':str(q)},'external_code_executed':False,'derivative_calculi_repeated':False,'field_integrals_evaluated':False,'FLOAT_diagnostics_used_as_proof':False,'verdict':'CONFIRMED both Opus reviews, entire affine L2 exclusion at every real c, and constant velocity extension. Explicit G0 changed-c test accepted; keeping E would have zero leading pairing. No existence closure or exclusion of non-L2 classes.'}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],'CHECKS',len(checks),'SECONDS',result['elapsed_seconds'],'SHA',sha(B/'verification/result.json'))
if __name__=='__main__':main()
