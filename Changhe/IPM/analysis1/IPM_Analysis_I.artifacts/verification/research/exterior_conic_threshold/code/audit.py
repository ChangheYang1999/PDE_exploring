"""Independent saved-number checks; no producer or transcendental imports."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from datetime import datetime,timezone
import sys,json,hashlib
sys.set_int_max_str_digits(200000)
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/exterior_conic_threshold';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
counts={}
def check(t,tag):
 if not t:raise ValueError(tag)
 counts[tag]=counts.get(tag,0)+1
p=E/'scalars.json';s=load(p);check(s['status']=='PASS_TWO_METHOD_EXTERIOR_CONIC_SCALARS_REQUIRES_REVIEW','producer_completed')
for name,h in s['files'].items():check(sha(B/name)==h,'input_hash')
par={k:F(v) for k,v in s['parameters_exact'].items()};old=load(B/'research/exterior_flow/evidence/checks.json')
for k,v in [('k','k'),('c_l','cl'),('omega','omega'),('t_b','tb')]:check(par[k]==F(old['parameters_exact'][v]),'inherited_parameter')
row=next(x for x in old['cases'] if F(x['T_exact'])==1);check(s['inherited_row']==row,'complete_inherited_row')
for k in ['P','Q']:check(par[k]==max(F(row[k+'_arb']['upper_exact']),F(row[k+'_iv']['upper_exact']))==F(row['joint_'+k+'_upper_exact']),'exact_joint_upper')
check(par['c_l']*par['k']==1 and par['omega']==1-par['k']>0,'scaling');check(par['a']==F(129,20) and par['b']==F(307,100) and par['S']==par['a']+par['b']==F(238,25) and par['gamma']==F(1129,1000),'conic_parameters')
expboxes={}
for key,rec in s['rational_exponential_series'].items():
 x=F(rec['x']);N=rec['N'];check(N==192 and 0<x<N+2,'series_ratio_domain')
 want=4*par['omega'] if key=='exp_four_omega' else par['t_b']+5;check(x==want,'series_argument')
 terms=[x**j/F(factorial(j)) for j in range(N+1)];sm=sum(reversed(terms),F(0));nt=x**(N+1)/factorial(N+1);ratio=x/(N+2);tail=nt/(1-ratio)
 for field,value in [('sum_exact',sm),('next_term_exact',nt),('ratio_exact',ratio),('tail_majorant_exact',tail)]:check(F(rec[field])==value,'exact_series_identity')
 check(list(map(F,rec['range']))==[sm,sm+tail] and tail>0,'series_interval');expboxes[key]=(sm,sm+tail)
ref={k:tuple(map(F,v)) for k,v in s['methods']['fraction_positive_series192'].items()};rr=expboxes['R'];ex=expboxes['exp_four_omega'];ee=(1/ex[1],1/ex[0]);cl=par['c_l'];G=par['gamma'];S=par['S'];P=par['P'];Q=par['Q']
check(ref['R']==rr and ref['E']==ee,'series_input_binding');check(ref['P5']==tuple(P*x for x in ee) and ref['Q5']==tuple(Q*x for x in ee),'scaled_errors')
mu=(G+(S-G)/(1+(rr[1]/6)**4),G+(S-G)/(1+(rr[0]/6)**4));check(ref['muR']==mu,'mu_monotone_endpoints')
bd=tuple(-1+(G-1)*cl+cl*(S-G)/(1+(r/6)**4)+e*(S*Q+(S-G)*P) for r,e in [(rr[1],ee[0]),(rr[0],ee[1])]);check(ref['B5']==bd,'complete_conic_endpoints')
check(ref['s_lower']==(cl-P*ee[1],cl-P*ee[0]) and ref['vi_lower']==(cl-Q*ee[1],cl-Q*ee[0]),'drift_endpoints')
margins={}
for method,raw in s['methods'].items():
 vals={k:tuple(map(F,v)) for k,v in raw.items()};check(set(vals)=={'R','E','P5','Q5','muR','B5','s_lower','vi_lower'},'scalar_key_set')
 for key,(l,u) in vals.items():check(l<=u,'endpoint_order')
 ms={'R_above20':vals['R'][0]-20,'R_below510000':510000-vals['R'][1],'T_below_minus22':-F(11,50)-vals['B5'][1],'s_above557':vals['s_lower'][0]-F(557,100),'vi_above557':vals['vi_lower'][0]-F(557,100),'E_positive':vals['E'][0],'E_below1':1-vals['E'][1],'mu_above_gamma':vals['muR'][0]-G,'mu_below_S':S-vals['muR'][1]}
 for key,v in ms.items():check(v>0,'strict_public_comparison')
 margins[method]={k:str(v) for k,v in ms.items()}
 for key in vals:check(max(vals[key][0],ref[key][0])<=min(vals[key][1],ref[key][1]),'comparison_overlap_only')
check(F(float(6.82))<7 and F(float(2.85))<3 and 7**2+3**2<20**2,'strict_box_radius');check(1<5<9<17,'logarithmic_join_order')
proofrec=load(E/'proof_first.json');check(proofrec['proof_sha256']==sha(D/'PROOF.md') and proofrec['utc']<s['start_utc']<=s['end_utc'],'proof_chronology')
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_SAVED_NUMBER_AND_DEPENDENCY_AUDIT','counts':counts,'strict_margins_exact':margins,'scalar_sha256':sha(p),'producer_sha256':sha(D/'code/compute.py'),'audit_sha256':sha(__file__),'scope':'Saved-number scalar checks only, inherited53tail theorem; not fresh modal reconstruction or full finite-flow proof.'}
p=E/'audit.json';check(not p.exists(),'immutable_new_output');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'utc':result['utc'],'status':result['status'],'counts':counts,'sha256':sha(p)}))
