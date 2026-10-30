"""Own exact fixture reconstruction and primary-review source acceptance."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from flint import fmpq as Q,fmpq_poly as P
import json,os,time,sys
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_upper_opus_primary'
sha=lambda p:sha256(p.read_bytes()).hexdigest();T=P([0,1]);W=1-T
sys.set_int_max_str_digits(0)
def D(b,A):return (1-2*b*T)*A+2*T*W*A.derivative()
def integral(A,q):
 assert q>-1
 return sum((a/(q+j+1) for j,a in enumerate(A(W))),Q(0))
def energy(n,b,A,c,C,kind='d'):
 num=D(b,A)*D(c,C)
 num+=n*n*A*C if kind=='d' else D(b,D(b,A))*D(c,D(c,C))/(n*n)
 return integral(num,b+c-2)/2
def source(n,b,A):
 N=n*n*A-D(b,D(b,A));S,rem=divmod(N,T);assert not rem;return b+1,S
def pair(n,e,S,b,A,kind='b'):
 return integral(T*S*(D(b,D(b,A))/(n*n) if kind=='b' else A),e+b-3)/2
def mass(n,e,S):return integral(T*T*S*S,2*e-4)/(2*n*n)
def main():
 start=time.monotonic();checks={};inputs={};external={};rows={}
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or v==h,(p,h,v);key=str(p.relative_to(R));assert key not in inputs or inputs[key]==v;inputs[key]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 mf=read(B/'source/MANIFEST.json');ck('proof_before_checker',not mf['checker_exists']);bind(B/'PROOF.md',mf['proof_sha256']);bind(Path(__file__))
 for rec in mf['files'].values():bind(R/rec['path'],rec['sha256'])
 def frozen(k):return R/mf['files'][k]['path']
 review=frozen('T2_REVIEW.md').read_text();peer=read(frozen('T2_result.json'));fix=read(frozen('T4_upper_parameters.json'));old=read(frozen('T4_upper_result.json'));pole=read(frozen('T4_upper_scope.json'))
 ck('peer59checked',peer['checks']==59 and peer['fails']==[])
 for rel,h in peer['A']['inputs'].items():
  p=R.parent/rel;ck('source:'+rel,sha(p)==h);external[str(p)]=h
 ck('peer75checked',old['check_count']==len(old['checks'])==len(set(old['checks']))==75 and all(isinstance(x,str) and x for x in old['checks']))
 ck('review_carries_R4',all(s in review for s in ['R4 (hypothesis to carry','M2 to use is that of the full source','Not reviewed: no candidate value','r Delta psi in L^2']))
 ck('review_carries_directed_use','an upper bound U >= M2 over ALL modes' in review)
 fx={}
 for case in fix['cases']:
  n=case['n'];b=Q(case['b']);A=P([Q(x) for x in case['P']]);e,S=source(n,b,A)
  vals={'d':energy(n,b,A,b,A),'a':energy(n,b,A,b,A,'a'),'M2':mass(n,e,S),'b':pair(n,e,S,b,A),'p':pair(n,e,S,b,A,'p')}
  for k,v in vals.items():ck(f'{case["name"]}:{k}',v==Q(peer['C'][case['name']][k]))
  for k in ['d','a','M2','b']:ck(f'{case["name"]}:original:{k}',vals[k]==Q(case[k+'_over_pi']))
  ck(case['name']+':manufactured',vals['b']==-vals['a'] and vals['p']==vals['d'] and vals['M2']-vals['a']==vals['d'])
  ck(case['name']+':positive',vals['d']>0 and vals['a']>0)
  fx[n]=(b,A,vals);rows[case['name']]={k:str(v) for k,v in vals.items()}
 b1,A1,x1=fx[1];b3,A3,x3=fx[3];M=x1['M2']+x3['M2'];H=x1['d']+x3['d']
 am=x1['a']+4*x3['a'];bm=x1['b']+2*x3['b'];combined={'H2':H,'one_test':M-x1['a'],'gap':x3['a'],'mixed_a':am,'mixed_b':bm,'mixed_opt':M-bm*bm/am}
 for k,v in combined.items():ck('combined:'+k,v==Q(peer['C']['combined'][k]))
 ck('mixed_incomplete_not_exact',combined['mixed_opt']>H)
 tt=Q(fix['rational_test_coefficient']);ck('mixed_completed_square',M+2*tt*bm+tt*tt*am-H==(1-tt)**2*x1['a']+(1-2*tt)**2*x3['a'])
 two=[(Q(3,2),T-2*T*T),(Q(2),T/2+T**3)]
 aa=sum((energy(3,b,A,c,C,'a') for b,A in two for c,C in two),Q(0));ck('two_exponent_a',aa==Q(peer['C']['two_exponent_a_over_pi']) and aa>0)
 bf,Af=Q(2),P([1]);ef,Sf=source(1,bf,Af);Hf=energy(1,bf,Af,bf,Af);Mf=mass(1,ef,Sf);bv=pair(1,ef,Sf,b1,A1);pv=pair(1,ef,Sf,b1,A1,'p');av=x1['a'];dv=x1['d']
 gf=energy(1,bf,Af,b1,A1);Hg=Hf+dv-2*gf;Ag=Mf+x1['M2']+2*(bv-pv)
 single={'H2':Hf,'M2':Mf,'b':bv,'a':av,'bound4':Mf-bv*bv/av,'p':pv,'Hg2':Hg,'Ag2':Ag,'t1_value':Mf+2*bv+av}
 for k,v in single.items():ck('single:'+k,v==Q(peer['D']['single'][k]))
 ck('single_strict_bounds',Hf<single['bound4']<Mf);ck('energy_identity',Hf==2*pv-dv+Hg and single['t1_value']==2*pv-dv+Ag and Ag>=Hg)
 for tt in [Q(-1),Q(0),Q(1,2),Q(3,4),Q(1),Q(2),-bv/av]:ck('completed_square:'+str(tt),Mf+2*tt*bv+tt*tt*av-single['bound4']==av*(tt+bv/av)**2)
 uh=A1/2;ph=pv/2;dh=dv/4;ah=av/4;bh=bv/2;Agh=Mf+x1['M2']/4+bv-pv;Hgh=Hf+dh-gf
 ck('half_test_energy',ph>dh and Hf==2*ph-dh+Hgh and Mf+2*bh+ah==2*ph-dh+Agh and dh*Agh>=(ph-dh)**2)
 U=Q(152381,250000);Upa=Q(3,8);Lb=Q(326073,10**6)
 ck('directed_candidate_pattern',U>=Mf and Upa>=av and 0<Lb<=abs(bv) and U-Lb**2/Upa>=single['bound4']>=Hf)
 bg,Agp=Q(5,2),T;eg,Sg=source(3,bg,Agp);Mg=mass(3,eg,Sg);Hgsource=energy(3,bg,Agp,bg,Agp);bvg=pair(3,eg,Sg,b3,A3)
 b2,A2=Q(3),P([1]);g11=av;g12=energy(1,b1,A1,b2,A2,'a');g22=energy(1,b2,A2,b2,A2,'a');s2=pair(1,ef,Sf,b2,A2);det=g11*g22-g12*g12
 correction=(g22*bv*bv-2*g12*bv*s2+g11*s2*s2)/det
 gram={'H2':Hf+Hgsource,'bound_gram':Mf+Mg-correction-bvg*bvg/x3['a'],'M2':Mf+Mg,'gram_det':det}
 for k,v in gram.items():ck('two_mode:'+k,v==Q(peer['D']['two_mode'][k]))
 ck('Gram_positive_and_strict',g11>0 and det>0 and gram['H2']<gram['bound_gram']<Mf+Mg-bv*bv/av-bvg*bvg/x3['a']<gram['M2'])
 s=T;t=1-s*s;L=1+3*s*s;Dp2=9*t-48*t*t+48*t**3;N=s**4*t*(t*(1-2*t))*Dp2/9
 pol,rem=divmod(N,L*L);ck('pole_even_remainder',rem.degree()<=3 and rem[1]==rem[3]==0)
 C=rem[2]/3;DD=rem[0]-C;ck('pole_exact_reconstruction',pol*L*L+C*L+DD==N)
 rational=sum((a/Q(j+1) for j,a in enumerate(pol)),Q(0))+DD/8;irr=C/9+DD/18
 ck('pole_exact_closed_form',rational==Q(-28442,9009) and irr==Q(34256,59049) and irr!=0)
 ck('pole_peer_display',peer['E']['b_over_pi_closed_form']=='-28442/9009 + 34256*sqrt(3)*pi/59049')
 accept=read(R/'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json','a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc')
 ck('392_accepted',all(accept['checks'].values()))
 for rel,h in accept['inputs'].items():bind(R/rel,h)
 prod=read(R/'research/candidate016_scaled_norm_peer/source/N4_norms_partial_v01.json','7e7b51a4473936d0ee9803fb12df45851ab42a10c0974787feed7c6728e0a58c');full=prod['fields']['D0_0'];comp=full['components']
 ck('R4_full_finite_source',len(comp)==full['component_count']==1360 and all(c['key'][1]=='s' for c in comp) and sorted({c['key'][2] for c in comp})==list(range(1,320,2)))
 ck('R4_full_rF_finite',0<Q(accept['norms']['rF']['accepted_lower_exact'])<Q(accept['norms']['rF']['accepted_upper_exact']))
 arc=read(R/'research/candidate016_pairing_archive/verification/result.json','c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6')
 ck('399_actual_pairings_accepted',all(arc['checks'].values()))
 for rel,h in arc['inputs'].items():bind(R/rel,h)
 tail=read(R/'research/candidate016_angular_tail_bound/verification/result_v01.json','8a6bc15f52acec01664df0e69f47888f6bd422dad3b954962978450d1e59bea1')
 ck('403_complete_tail_pattern',all(tail['checks'].values()) and tail['complete_uncomputed_tail_retained'] and not tail['all160_individual_mode_integrals_replayed'])
 for rel,h in tail['inputs'].items():bind(R/rel,h)
 for rel,h in inputs.items():assert sha(R/rel)==h
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'external_inputs':external,'check_count':len(checks),'checks':checks,'fixtures':rows,'combined':{k:str(v) for k,v in combined.items()},'single':{k:str(v) for k,v in single.items()},'gram':{k:str(v) for k,v in gram.items()},'positive_pole_closed_form_coefficients':{'rational':str(rational),'sqrt3_pi':str(irr)},'configured_peer_model':'us.anthropic.claude-opus-5-5','actual_provider_response_identity_observable':False,'peer_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED primary Opus general review, exact fixtures and candidate finite-source premise. Numerical improved upper and reciprocal review remain separate.'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'bindings',sha(p),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
