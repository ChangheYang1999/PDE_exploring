"""Independent exact endpoint composition and reciprocal T4-476 scalars."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import fmpq as Q,arb,ctx
import json,os,sys,time
from fractions import Fraction
def decimal(text):return Q(str(Fraction(text)))
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_prefix_reciprocal';sha=lambda p:sha256(p.read_bytes()).hexdigest()
sys.set_int_max_str_digits(0)
def endpoint(x,upper=False):
 m,e=(x.upper() if upper else x.lower()).man_exp();m,e=int(m),int(e)
 return Q(m*2**e) if e>=0 else Q(m,2**(-e))
def main():
 ctx.prec=4096;start=time.monotonic();checks={};inputs={};external={}
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or h==v,(p,h,v);inputs[str(p.relative_to(R))]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 m=read(B/'source/MANIFEST.json');ck('proof before code',not m['checker_exists']);bind(B/'PROOF.md',m['proof_sha256']);bind(Path(__file__))
 for row in m['files'].values():bind(R/row['path'],row['sha256'])
 def f(k):return R/m['files'][k]['path']
 peer=read(f('T4_result.json'),'1c91f2e3507891bf04ec694147022c0c837fee06b0ab489f4dffab7833b08a37');p=read(f('T4_parameters.json'))
 ck('T4 2297 distinct successes',peer['check_count']==len(peer['checks'])==len(set(peer['checks']))==2297)
 root=Path(m['files']['T4_result.json']['original']).parents[1]
 for row in read(f('T4_manifest.json')):
  path=(root/row['local']).resolve();ck('external:'+row['local'],sha(path)==row['sha256']);external[str(path)]=row['sha256']
 accepted={}
 for k,rel,h in [('392','candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json','a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc'),('403','candidate016_angular_tail_bound/verification/result_v01.json','8a6bc15f52acec01664df0e69f47888f6bd422dad3b954962978450d1e59bea1'),('399','candidate016_pairing_archive/verification/result.json','c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6'),('404','candidate016_upper_opus_primary/verification/result.json','94c9b9cdf6c6aac7f831a23253ba4b8bae7c576942390b17fd77aabf38d780ea'),('406','upper_review_cancellation_peer/verification/result.json','58e8e50e27a652e87963b0cfc4bcf9620d96317449b0aedadcb3f69b8338efc9')]:
  d=read(R/'research'/rel,h);ck('accepted:'+k,all(d['checks'].values()));accepted[k]=d
  for rel0,h0 in d['inputs'].items():bind(R/rel0,h0)
 old=accepted['403'];full=read(R/'research/candidate016_scaled_norm_peer/source/N4_norms_partial_v01.json')['fields']['D0_0'];branches=full['components'];delta=Q(p['delta'])
 ck('complete finite source',len(branches)==full['component_count']==1360 and sorted({b['key'][2] for b in branches})==list(range(1,320,2)))
 ck('source identity',peer['candidate']==old['candidate']==p['candidate'] and peer['raw_sha256']==old['raw_sha256']==p['raw_sha256'] and peer['complete_field_hash']==full['representation_sha256']==old['F_representation_sha256'])
 pi=arb.pi();pl,pu=endpoint(pi),endpoint(pi,True);modes=[]
 for oldrow,prow in zip(old['modes'],peer['modes']):
  n=oldrow['n'];ck('prefix mode:'+str(n),n==prow['n'] and n in [1,3,5,7]);row=read(R/oldrow['record'],oldrow['sha256']);br=[b for b in branches if b['key'][2]==n];ell=[b['key'][0] for b in br]
  ck(f'n{n}:pairs',row['component_count']==len(br) and row['ordered_pair_count']==len(br)**2)
  ck(f'n{n}:complete groups',[g['ell_sum'] for g in row['groups']]==sorted({a+b for a in ell for b in ell}) and len(row['groups'])==prow['group_count']==oldrow['group_count'])
  lo=hi=Q(0)
  for j,g in enumerate(row['groups']):
   key=f'n{n}:g{j}';ball=arb(g['integral_ball']);a,b=endpoint(ball),endpoint(ball,True);e=Q(g['b']);de=g['decomposition']
   ck(key+':endpoint',g['endpoint_v_order']>=0 and e==Q(g['ell_sum'])*delta/2-4+g['endpoint_v_order'] and e>-1)
   ck(key+':source enclosure',de['exact_reconstruction'] and Q(de['b'])==e and g['integral_accuracy_bits']>150 and ball.is_finite() and ball.rel_accuracy_bits()>150 and a<=b)
   ck(key+':positive poles',g['powers'][0]==g['powers'][2]==g['powers'][3]==0 and all(k>=0 for k in g['powers']) and de['factors']==([[str(624),g['powers'][1]]] if g['powers'][1] else []))
   lo+=a;hi+=b
  ck(f'n{n}:cancellation resolved',0<lo<=hi and hi-lo<Q(1,10**100));lo=lo*pl/2;hi=hi*pu/2
  ck(f'n{n}:own403 endpoints valid',Q(oldrow['q_lower_exact'])<=lo<=hi<=Q(oldrow['q_upper_exact']))
  ck(f'n{n}:T4 positive containment in403',Q(oldrow['q_lower_exact'])<=Q(prow['q_lower_exact'])<=Q(prow['q_upper_exact'])<=Q(oldrow['q_upper_exact']))
  modes.append({'n':n,'q_lower_exact':str(lo),'q_upper_exact':str(hi),'group_count':len(row['groups'])})
 ck('all124groups',len(modes)==4 and sum(r['group_count'] for r in modes)==peer['group_count']==124)
 L={k:Q(v['accepted_lower_exact']) for k,v in accepted['392']['norms'].items()};U={k:Q(v['accepted_upper_exact']) for k,v in accepted['392']['norms'].items()}
 S=U['rF']**2;my= S/81+sum(((Q(1,r['n']**2)-Q(1,81))*Q(r['q_upper_exact']) for r in modes),Q(0))
 theirs=S/81+sum(((Q(1,r['n']**2)-Q(1,81))*Q(r['q_upper_exact']) for r in peer['modes']),Q(0))
 ck('T4 exact complete M2 formula',theirs==Q(peer['M2_upper_exact']))
 ck('own safe tail',S-sum((Q(r['q_lower_exact']) for r in modes),Q(0))>0 and my<=Q(old['M2_upper_exact']))
 J=sum((Q(r['strict_floor_exact']) for r in accepted['399']['rows'] if r['kind']=='cross'),Q(0));h2=sum((Q(r['strict_floor_exact'])**2 for r in accepted['399']['rows'] if r['kind']=='dual'),Q(0))
 ck('same cross floor',J==Q(peer['selected_cross_improvement_strict_lower_exact'])==Q(p['improvement'])==Q(old['selected_improvement_sum_lower_exact']))
 ck('same dual square',h2==Q(peer['H_lower_square_exact'])==Q(old['H_lower_square_exact']))
 ck('T4 improved square',theirs-J==Q(peer['improved_H_square_upper_exact']))
 ck('whole-field strict H bounds',0<decimal(p['H_lower'])**2<h2<my-J<decimal(p['improved_H_upper'])**2 and my<decimal(p['plain_H_upper'])**2)
 El=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*h2
 Eu=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2+Q(20,21)*2**18*(my-J)
 Et=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2+Q(20,21)*2**18*(theirs-J)
 ck('T4 energy exact',Et==Q(peer['E2_upper_square_exact']))
 ck('whole-field strict E2 bounds',0<decimal(p['E2_lower'])**2<El<Eu<decimal(p['E2_upper'])**2 and decimal(p['E2_lower'])>decimal(p['baseline007_E2_upper']))
 ck('same qualified scope',not peer['foreign_code_executed'] and not peer['candidate_moment_integrals_repeated'] and not peer['exact_full_residual_reconstructed_in_this_checker'])
 for rel,h in inputs.items():assert sha(R/rel)==h
 out={'utc':datetime.now(timezone.utc).isoformat(),'check_count':len(checks),'checks':checks,'inputs':inputs,'external_inputs':external,'modes':modes,'M2_upper_exact':str(my),'conditional_improved_H_square_upper_exact':str(my-J),'H_lower_square_exact':str(h2),'conditional_E2_upper_square_exact':str(Eu),'E2_lower_square_exact':str(El),'peer_code_executed':False,'integrals_repeated':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED reciprocal T4-476 finite exact-endpoint composition and full omitted-mode coverage. Plain Hardy upper accepted; improved numerical upper retains this lane announced reciprocal T1 analytic gate. No exactH, inverse, contraction or existence.'}
 path=B/'verification/result.json'
 with path.open('x') as f0:json.dump(out,f0,indent=2);f0.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'bindings',sha(path),'seconds',out['elapsed_seconds'])
if __name__=='__main__':main()
