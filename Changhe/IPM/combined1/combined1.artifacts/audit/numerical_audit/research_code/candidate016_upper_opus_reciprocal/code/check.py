"""Independent finite composition of primary and reciprocal analytic reviews."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
from flint import fmpq as Q,arb,ctx
import ast,importlib.util,json,os,sys,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_upper_opus_reciprocal'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
sys.set_int_max_str_digits(0)
def main():
 start=time.monotonic();ctx.prec=4096;checks={};inputs={};external={}
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);v=sha(p);key=str(p.relative_to(R));assert h is None or v==h,(key,h,v);assert key not in inputs or inputs[key]==v;inputs[key]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 def aq(v):v=Q(v);return arb(v.numerator)/arb(v.denominator)
 mf=read(B/'source/MANIFEST.json');ck('proof_before_code',not mf['checker_exists']);bind(B/'PROOF.md',mf['proof_sha256']);bind(Path(__file__))
 for rec in mf['files'].values():bind(R/rec['path'],rec['sha256'])
 frozen=lambda k:R/mf['files'][k]['path']
 par=read(frozen('parameters.json'));peer=read(frozen('T4_result.json'));review=frozen('T1_REVIEW.md').read_text()
 ck('both_reviews_full',all(s in review for s in ['R1-048','R1-049','7/10','CONFIRMED']))
 ck('peer209checks',peer['check_count']==len(peer['checks'])==209 and all(isinstance(x,str) and x for x in peer['checks']))
 for name,count in [('T1_dual.out',1368),('T1_upper.out',65)]:ck('completed_log:'+name,'checks passed '+str(count)+' ; elapsed ' in frozen(name).read_text())
 dependencies={
 'candidate016_upper_opus_primary':'94c9b9cdf6c6aac7f831a23253ba4b8bae7c576942390b17fd77aabf38d780ea',
 'upper_review_cancellation_peer':'58e8e50e27a652e87963b0cfc4bcf9620d96317449b0aedadcb3f69b8338efc9',
 'candidate016_prefix_reciprocal':'eae57c4cdecf828199e5481ede1f22b7863d0c25b90ea683f420139d9740fed9',
 'candidate016_archive_peer':'5335104171fdc0d7b92aa15daabca72d2c3dd3febea0ac1007e2b01a80cc5b10',
 'candidate016_pairing_archive':'c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6'}
 accepted={}
 for topic,h in dependencies.items():
  j=read(R/'research'/topic/'verification/result.json',h);accepted[topic]=j;ck('accepted:'+topic,all(j['checks'].values()))
  for rel,hh in j['inputs'].items():bind(R/rel,hh)
 lib=bind(R/'research/candidate016_upper_opus_primary/code/check_v02.py','ae63d919f60b458b074df764cf7f94e35109a13e9828fe8949c0ccbb29b30eeb')
 spec=importlib.util.spec_from_file_location('own404',lib);M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
 vals={}
 for ns,f in par['fixtures'].items():
  n=int(ns);b=Q(f['b']);P=M.P([Q(x) for x in f['P']]);e,S=M.source(n,b,P)
  row={'d':M.energy(n,b,P,b,P),'a':M.energy(n,b,P,b,P,'a'),'M':M.mass(n,e,S),'p':M.pair(n,e,S,b,P,'p'),'b':M.pair(n,e,S,b,P)}
  for k in ['d','a','M']:ck('fixture:'+ns+':'+k,row[k]==Q(f[k]))
  ck('fixture:'+ns+':signed',row['a']>0 and row['p']==row['d'] and row['b']==-row['a'] and row['M']-row['a']==row['d'])
  for q in [Q(1,3),Q(1,2),Q(3,4),Q(3,2)]:
   aa=q*q*row['a'];bb=q*row['b'];ck('gain:'+ns+':'+str(q),row['M']+2*bb+aa-(row['M']-bb*bb/aa)==(aa+bb)**2/aa)
  vals[n]=row
 ck('fixture_complete_H',vals[1]['d']+vals[3]['d']==Q(par['H2_over_pi']))
 ck('fixture_one_test',vals[1]['M']+vals[3]['M']-vals[1]['a']==Q(par['one_test_over_pi']))
 ck('fixture_gap',vals[3]['a']==Q(par['gap_over_pi']))
 for i,(n,k,bs) in enumerate(par['shift_parameters']+[[1,-1,'7/4'],[1,0,'5/2']]):
  beta=Q(bs);a=3+2*k;s=beta+k;b=beta-1;P=M.T**(k+1)
  ck('shift_origin:'+str(i),a>=n and (a-n)%2==0 and beta>Q(3,2))
  L=a*P-2*s*M.T*P;L2=a*a*P-4*s*(a+1)*M.T*P+4*s*(s+1)*M.T*M.T*P
  ck('shift_L:'+str(i),M.D(b,P)==L);ck('shift_L2:'+str(i),M.D(b,M.D(b,P))==L2)
  ck('shift_r2Delta:'+str(i),M.D(b,M.D(b,P))-n*n*P==L2-n*n*P)
 mapping={
 'N3_016_hdual_m13deep.json':'candidate016_dual_lower/source/N3_exact_vectors.json',
 'N4396_mode_001.json':'candidate016_dual_lower/verification/mode_001.json',
 'N4396_mode_003.json':'candidate016_dual_lower/verification/mode_003.json',
 'N4396_result.json':'candidate016_dual_lower/verification/result.json',
 'N4392_comparison.json':'candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json',
 'N4252_result.json':'negative_norm_forcing_assembly/verification/result.json',
 'N4398_mode_001.json':'candidate016_solenoidal_upper/verification/mode_001.json',
 'N4398_mode_003.json':'candidate016_solenoidal_upper/verification/mode_003.json',
 'N4398_result.json':'candidate016_solenoidal_upper/verification/result.json'}
 sources={}
 for name in ['T1_dual.py','T1_upper.py']:
  tree=ast.parse(frozen(name).read_text());nodes=[n.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HASH' for t in n.targets)]
  ck('single_source_map:'+name,len(nodes)==1);hm=ast.literal_eval(nodes[0])
  for filename,h in hm.items():sources[filename]=read(R/'research'/mapping[filename],h)
  ck('source_map_complete:'+name,len(hm)==(6 if name=='T1_dual.py' else 4))
 upper_tree=ast.parse(frozen('T1_upper.py').read_text());nodes=[n.value for n in ast.walk(upper_tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='delta_e' for t in n.targets)]
 ck('literal_exponent_assignment',len(nodes)==1 and isinstance(nodes[0],ast.Call) and isinstance(nodes[0].func,ast.Name) and nodes[0].func.id=='Fr' and not nodes[0].keywords)
 exponent=Q(*[ast.literal_eval(a) for a in nodes[0].args]);ck('exponent_attribution_repair',exponent==Q(par['exponent_executed'])==Q(7,5) and exponent!=Q(par['exponent_description']))
 vectors=sources['N3_016_hdual_m13deep.json'];dual=sources['N4396_result.json'];cross=sources['N4398_result.json'];archive=accepted['candidate016_pairing_archive'];coefcount=0
 ck('candidate_hash',vectors['id']==dual['candidate']=='C1-N1-016-legqs25-quot013' and vectors['source_sha256']==dual['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42')
 ck('distinct_angular_modes',[m['n'] for m in vectors['modes']]==[1,3]);h2=Q(0);jtotal=Q(0)
 arcby={(r['n'],r['kind']):r for r in archive['rows']}
 for v in vectors['modes']:
  n=v['n'];labels=[]
  for label,coefficient in v['x_rational'].items():
   bs,ks=label.split(',');beta=Q(bs);k=int(ks);labels.append((beta,k));Q(coefficient)
   ck('admissible:'+str(n)+':'+label,beta>Q(3,2) and k>=-1 and 3+2*k>=n and (3+2*k-n)%2==0)
  ck('labels:'+str(n),len(labels)==len(set(labels))==v['basis_size']);coefcount+=len(labels)
  drec=sources[f'N4396_mode_{n:03d}.json'];crec=sources[f'N4398_mode_{n:03d}.json'];d=Q(drec['gradient_energy_over_pi_exact']);a=Q(crec['a_over_pi_exact'])
  ck('candidate_d_exact:'+str(n),d==Q(v['grad_psi_sq_over_pi_exact'])==Q(crec['old_d_over_pi_exact']) and d>0 and a>0)
  dr=arcby[n,'dual'];cr=arcby[n,'cross'];p=arb(dr['pairing_replayed_ball']);b=arb(cr['pairing_replayed_ball']);peerp=arb(v['F_psi'])
  ck('actual_directed_pair_containment:'+str(n),peerp.lower()<p.lower() and p.upper()<peerp.upper())
  q=abs(p)/(arb.pi()*aq(d)).sqrt();im=b*b/(arb.pi()*aq(a));floor=Q(dual['mode_strict_floors'][str(n)]);jf=Q(crec['improvement_strict_lower_exact'])
  ck('dual_floor:'+str(n),aq(floor)<q.lower() and Q(dr['strict_floor_exact'])==floor)
  ck('cross_floor:'+str(n),aq(jf)<im.lower() and Q(cr['strict_floor_exact'])==jf)
  ck('archive_high_accuracy:'+str(n),p.rel_accuracy_bits()>600 and b.rel_accuracy_bits()>600)
  h2+=floor*floor;jtotal+=jf
 ck('all663labels',coefcount==663);ck('lower_square',h2==Q(dual['H_lower_square_exact']))
 ck('cross_sum',jtotal==Q(cross['improvement_sum_strict_lower_exact'])==Q(archive['improvement_sum_strict_lower_exact']))
 norms=sources['N4392_comparison.json']['norms'];lo={k:Q(norms[k]['accepted_lower_exact']) for k in ['G0','G1','P2']}
 e2=lo['P2']**2+2**14*lo['G1']**2+2**18*lo['G0']**2+Q(20,21)*2**18*h2
 hf=Q(dual['H_strict_lower_exact']);ef=Q(dual['E2_strict_lower_exact']);base=Q(sources['N4252_result.json']['E_upper']['strict_upper_exact'])
 ck('strict_H_lower',0<hf and hf*hf<h2 and hf==Q(peer['H_lower_exact']))
 ck('strict_E2_lower',0<ef and ef*ef<e2 and e2==Q(dual['E2_lower_square_exact']) and ef==Q(peer['E2_lower_exact']))
 ck('same_E2_order',ef-base==Q(dual['strict_E2_separation_exact'])==Q(peer['strict_E2_gap']) and ef>base)
 for rel,h in inputs.items():assert sha(R/rel)==h
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'check_count':len(checks),'checks':checks,'fixtures_over_pi':{str(n):{k:str(v) for k,v in row.items()} for n,row in vals.items()},'H_strict_lower_exact':str(hf),'E2_strict_lower_exact':str(ef),'strict_E2_gap_exact':str(ef-base),'improvement_sum_strict_lower_exact':str(jtotal),'both_general_Opus_reviews_accepted':True,'separate_tail_review_still_pending':True,'refuted_prose_exponent':par['exponent_description'],'actual_script_exponent':str(exponent),'configured_peer_model':'us.anthropic.claude-opus-5-5','actual_provider_response_identity_observable':False,'peer_code_executed':False,'candidate_integrals_repeated':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED reciprocal analytic reviews and exact candidate lower/cross composition; REFUTED only FLOAT exponent attribution. Final prefix-tail upper acceptance is separate.'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'bindings',sha(p),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
