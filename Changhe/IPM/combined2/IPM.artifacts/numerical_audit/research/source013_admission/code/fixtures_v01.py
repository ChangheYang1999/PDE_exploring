from pathlib import Path
from datetime import datetime,timezone
from copy import deepcopy
from math import factorial
import importlib.util,json,sys,time
from flint import ctx,arb,fmpq as Q,fmpq_poly as Poly
import identity_v01 as identity,plans_v01 as plans,import_v01 as admission
R=Path(__file__).resolve().parents[3];B=R/'research/source013_admission';checks=0

def need(x):
 global checks
 assert x;checks+=1

def rejects(fn):
 try:fn()
 except (AssertionError,KeyError,ValueError):need(True)
 else:raise AssertionError('mutation not rejected')

def main():
 start,tick=admission.stamp(),time.monotonic();ctx.prec=1024
 spec=importlib.util.spec_from_file_location('fixture_table_engine',R/'research/compact_radial_jets/code/engine_v01.py');engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
 groups=[]
 for i in range(24):
  s=[Q(1),Q(1,2),Q(2)][i%3];fields={}
  for j,name in enumerate(identity.NAMES):
   fields[name]=(i%2,Q(i%5-2,1)+Q(1,3),i%4,{n:Poly([Q((i+1)*(j+1)*(n+1),7),Q(i-j,5),Q(1,11)]) for n in [-3,1,5]})
  groups.append((None,s,fields))
 table=engine.compile_groups(groups);evidence=identity.verify(groups,table);need(evidence['exact_equality'])
 changed=deepcopy(table)
 row=next(r for r in changed['rows']if r['coefficients']['linear']);key=next(iter(row['coefficients']['linear']));row['coefficients']['linear'][key]=str(Q(row['coefficients']['linear'][key])+1)
 rejects(lambda:identity.verify(groups,changed))
 changed=deepcopy(table);changed['rows'].append(changed['rows'][0]);rejects(lambda:identity.verify(groups,changed))
 changed=deepcopy(table);changed['combined_nonzero_coefficients']+=1;rejects(lambda:identity.verify(groups,changed))
 changed=deepcopy(table);changed['rows'][0]['scale_exact']='0';rejects(lambda:identity.verify(groups,changed))
 M=322;rows=[]
 for i,(c,h) in enumerate(plans.geometry()):
  D1,D2=c/5,c/4;BF=Q(i+1,17);Bg=arb(BF)*arb(Q(1,2))**arb(-1)*arb(Q(1,4)+(c+D2)**2)**arb(Q(1,2))
  weights=[[Q(1)],[Q(M),Q(1)],[Q(M*(M+2)),Q(2*M+1),Q(1)],[Q(M*(M+2)*(M+4)),Q(3*M*M+9*M+3),Q(3*M+3),Q(1)]]
  H=[]
  for j,w in enumerate(weights):
   mult=sum((v*(c-D1)**(ell-j)*factorial(ell)/(D2-D1)**ell for ell,v in enumerate(w)),Q(0))
   H.append((2*arb.pi()*arb(c+D1)*2**j*(Bg*arb(mult))**2).upper().fmpq())
  K=48;q=h/D1;errors=[2*h*v*q**(K+1)/(1-q)for v in H]
  while any(x>y for x,y in zip(errors,plans.TAU)):K+=1;errors=[v*q for v in errors]
  rows.append({'parent_index':i,'policy':'six_per_doubling','all_analytic_remainders_within_budget':True,'request':{'center_exact':str(c),'half_width_exact':str(h),'inner_disk_exact':str(D1),'outer_disk_exact':str(D2),'sigma_exact':'1','r0_exact':'1/2','order':K},'order':K,'source_majorant_upper_exact':str(BF),'integrand_majorant_upper_exact':list(map(str,H)),'remainder_upper_exact':list(map(str,errors)),'tolerances_exact':list(map(str,plans.TAU))})
 a={'job':'planner_a','source':{},'center':{},'safe_structural_bandwidth':M,'rows':rows[::2],'majorant_calibration':{'overlap':True}};b={**a,'job':'planner_b','rows':rows[1::2]}
 result=plans.verify(a,b);need(len(result['panels'])==114);need(result['all_114_indices_once']);checks_before=checks
 for key,value in [('order',2049),('parent_index',1),('all_analytic_remainders_within_budget',False),('integrand_majorant_upper_exact',['0']*4),('remainder_upper_exact',['0']*4),('tolerances_exact',['1']*4)]:
  changed=deepcopy(a);changed['rows'][0][key]=value;rejects(lambda:plans.verify(changed,b))
 changed=deepcopy(a);changed['rows']=changed['rows'][:-1];rejects(lambda:plans.verify(changed,b))
 changed=deepcopy(b);changed['safe_structural_bandwidth']+=2;rejects(lambda:plans.verify(a,changed))
 m=json.loads((R/'research/source013_startup/verification/manifest_v01.json').read_text());j=m['jobs'][2]
 center={'fields_sha256':m['source']['fields_sha256'],'fixed_c_exact':m['source']['fixed_c_exact'],'input_sha256':'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21','phi':{'input_sha256':m['source']['canonical_sha256']}}
 ins={'job':'table','owner':'numerics_agent_1','cpu':45,'manifest_sha256':admission.MANIFEST,'review_sha256':admission.REVIEW,'worker_root':'research/source013_startup/worker_table','installed_utc':'2026-11-03T11:43:00.000001Z'}
 exe={**ins,'schema':'source013-startup-execution-v1','status':'COMPLETED','exit_code':0,'stop_reason':None,'result_sha256':'a'*64,'guard_sha256':m['files']['research/source013_startup/code/guard_v01.py'],'started_utc':'2026-11-03T11:44:00.000001Z','finished_utc':'2026-11-03T11:47:00.000001Z','elapsed_seconds':180.0,'initial_resources':{'owner_lane_bytes':2_000_000_000,'filesystem_free_bytes':30_000_000_000}}
 out={**ins,'schema':'source013-startup-result-v1','status':'COMPLETED','role':'table','source':m['source'],'precision_bits':1024,'center':center,'started_utc':'2026-11-03T11:44:01.000001Z','finished_utc':'2026-11-03T11:46:59.000001Z','elapsed_seconds':178.0,'source_bindings':{},'table':'output/source013_table_v01.json.zst','table_sha256':'b'*64,'statistics':{'exact_reverse_accumulation_passed':True}}
 admission.validate_receipts(m,j,ins,exe,out,'a'*64);need(True)
 for target,key,value in [('execution','finished_utc','2026-11-04T17:05:30.000001Z'),('execution','started_utc','2026-11-04T17:05:00.000001Z'),('execution','stop_reason','cutoff'),('execution','cpu',44),('execution','result_sha256','c'*64),('result','source',{}),('result','precision_bits',768),('result','elapsed_seconds',float('nan')),('result','table','../escape'),('installation','review_sha256','d'*64)]:
  aa,bb,cc=deepcopy(ins),deepcopy(exe),deepcopy(out)
  {'installation':aa,'execution':bb,'result':cc}[target][key]=value
  rejects(lambda:admission.validate_receipts(m,j,aa,bb,cc,'a'*64))
 result={'status':'PASS','started_utc':start,'finished_utc':admission.stamp(),'elapsed_seconds':time.monotonic()-tick,'checks':checks,'synthetic_identity':evidence,'synthetic_panels':114,'exact_remainder_checks':456,'receipt_mutations':10,'scope':'Synthetic algebra, geometry and receipt fixtures only; no actual source013 startup output is imported.'}
 admission.put(B/'verification/fixtures_v01.json',result);print(json.dumps(result))
if __name__=='__main__':main()
