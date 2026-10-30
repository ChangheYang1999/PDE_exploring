"""Exact complete radial partitions; frozen publisher source is never executed."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,sys,time,math
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/hessian_radial_partition'
sys.set_int_max_str_digits(0)
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
H=module('n4_partition_hessian',ROOT/'research/scaled_background_hessian/code/check_v2.py')
P=module('n4_partition_poles',ROOT/'research/rational_pole_moments/code/moments.py')
now=lambda:datetime.now(timezone.utc).isoformat()
sha=H.sha;write=H.write;ar=H.ar
R0=Q(1,50);R=Q('4178237423365963/500000000000')
CUTS={'far':1/(1+R*R),'through_middle':1/(1+R0*R0),'whole':Q(1)}

def groups(field):
 angular={};out={};count=0
 for (ell,n),A in field.items():angular.setdefault(n,[]).append((ell,A))
 for terms in angular.values():
  for i,(ell,A) in enumerate(terms):
   for j in range(i+1):
    ell2,B=terms[j];H.W.add(out,ell+ell2,A*B*(1 if i==j else 2));count+=1
 return {k:A for k,A in out.items() if A},count

def primitive(b,A):
 factors=[(a,k) for a,k in zip(H.W.SCALES,A.powers) if k]
 numerator=A.numerator_v()*Poly([1,-1])
 pol,parts,merged,degree=P.decompose(numerator,factors)
 values={};records={}
 for name,V in CUTS.items():
  vpower=ar(V)**ar(b+1)
  total=sum((ar(c)*ar(V)**ar(b+j+1)/ar(b+j+1) for j,c in enumerate(pol)),arb(0))
  cache={};comparisons=[]
  for a,m in merged:
   J=P.pole_moments(b,a*V,m)
   for k in range(1,m+1):
    direct=(-ar(a*V)).hypgeom_2f1(arb(k),ar(b+1),ar(b+2),bc=True,abc=True)/ar(b+1)
    ok=direct.is_finite() and direct.overlaps(J[k]);assert ok,(name,str(b),str(a),k)
    comparisons.append({'a':str(a),'power':k,'recurrence_direct_overlap':ok})
   cache[a]=J
  for a,k,c in parts:total+=ar(c)*vpower*cache[a][k]
  assert total.is_finite() and total.rel_accuracy_bits()>150,(name,str(b),total.str(30))
  values[name]=total
  records[name]={'cut_exact':str(V),'integral':total.str(100),'relative_accuracy_bits':total.rel_accuracy_bits(),'hypergeometric_checks':comparisons}
 return values,{'b':str(b),'factors':[[str(a),m] for a,m in merged],'numerator_degree':numerator.degree(),'denominator_degree':degree,'polynomial_degree':pol.degree(),'principal_parts':len(parts),'exact_decomposition_replayed':True,'primitives':records}

def mesh_audit():
 import numpy as np
 lo=math.log(.02);edges=np.linspace(lo,16.,math.ceil(16.-lo)+1)
 z,w=np.polynomial.legendre.leggauss(32)
 rows=[];selected=0
 for i,(a,b) in enumerate(zip(edges[:-1],edges[1:])):
  nodes=.5*(a+b+(b-a)*z);keep=(np.exp(nodes)>=.02)&(np.exp(nodes)<=float(str(R.numerator))/float(str(R.denominator)))
  n=int(np.count_nonzero(keep));selected+=n
  if n:rows.append({'panel':i,'left_log_FLOAT':float(a),'right_log_FLOAT':float(b),'kept_nodes':n,'total_nodes':32,'complete':n==32})
 return {'status':'FLOAT rule reconstruction only','selected_nodes':selected,'selected_panels':rows,'all_selected_panels_complete':all(x['complete'] for x in rows),'last_panel_radius_FLOAT':math.exp(rows[-1]['right_log_FLOAT']),'nominal_radius_exact':str(R),'binary64_radius':float(str(R.numerator))/float(str(R.denominator)),'foreign_code_executed':False}

def run(num,ps):
 start=time.monotonic();name=f'C1-N1-{num:03d}-legqs{25 if num==16 else 50}-quot013'
 oldp=ROOT/f'research/scaled_background_hessian/verification/{name}.json';old=json.loads(oldp.read_text());H.bind(old)
 directory=ROOT/'research/candidate_audits/data'/name;mp=directory/'MANIFEST.json';manifest=json.loads(mp.read_text());entry=manifest['coefficient_files'][0];src=directory/entry['name']
 assert sha(src)==old['raw_sha256']==entry['sha256'];outp=BASE/f'verification/{name}.json';assert not outp.exists()
 model=H.ScaledRadial(src);fields,mixed=H.build(model)
 assert {k:H.field_hash(f) for k,(_,f) in fields.items()}==old['component_field_sha256']
 components={};details={}
 print('PARTITION_FIELDS',name,'seconds',time.monotonic()-start,flush=True)
 for label,(_,field) in fields.items():
  gs,count=groups(field);previous=old['component_energies'][label]
  assert H.field_hash(gs)==previous['group_sha256'] and count==previous['pair_count'] and len(gs)==previous['group_count']
  pm={row['ell']:row for row in previous['moments']};totals={k:arb(0) for k in CUTS};rows=[]
  for ell,A in sorted(gs.items()):
   b=ell*model.delta/2-1;assert b>-1
   vals,row=primitive(b,A);ok=vals['whole'].overlaps(arb(pm[ell]['integral']));assert ok,(label,ell)
   row.update({'ell':ell,'whole_group_overlap':ok});rows.append(row)
   for k,v in vals.items():totals[k]+=v
  totals={k:arb.pi()/2*v for k,v in totals.items()};assert totals['whole'].overlaps(arb(previous['energy']))
  comp={'origin':totals['whole']-totals['through_middle'],'middle':totals['through_middle']-totals['far'],'far':totals['far'],'whole':totals['whole']}
  assert all(v>0 and v.rel_accuracy_bits()>150 for v in comp.values())
  assert sum((comp[k] for k in ['origin','middle','far']),arb(0)).overlaps(comp['whole'])
  components[label]=comp;details[label]={'group_sha256':H.field_hash(gs),'pair_count':count,'group_count':len(gs),'moments':rows,'energies':{k:v.str(100) for k,v in comp.items()}}
  print('PARTITION_COMPONENT',name,label,{k:v.str(20) for k,v in comp.items()},flush=True)
 metrics={}
 for domain in ['origin','middle','far','whole']:
  X2=components['xx'][domain]+components['xy'][domain];Y2=components['xy'][domain]+components['yy'][domain]
  K2=((arb(2).log()-arb(1)/2)*X2+(3*arb(2).log()-2)*Y2)/(16*arb.pi())
  metrics[domain]={'X2':X2,'Y2':Y2,'D2':X2+Y2,'kappa2':K2,'X':X2.sqrt(),'Y':Y2.sqrt(),'D2rho':(X2+Y2).sqrt(),'kappa':K2.sqrt()}
 for key in ['X','Y','D2rho','kappa']:assert metrics['whole'][key].overlaps(arb(old['values'][key]))
 fp=next(directory.glob('*diag2.json'));diag=json.loads(fp.read_text());assert diag['sha256']==sha(src)
 comparisons={}
 for key,dk in [('X','D_rho_x_L2_inner'),('Y','D_rho_y_L2_inner'),('kappa','kappa_inner')]:
  full=metrics['whole'][key];mid=metrics['middle'][key];fl=arb(str(diag['BL2'][dk]));skey=key+'2'
  omission=metrics['origin'][skey]+metrics['far'][skey]
  comparisons[key]={'saved_FLOAT':str(diag['BL2'][dk]),'full_minus_middle':(full-mid).str(100),'middle_minus_FLOAT':(mid-fl).str(100),'full_minus_FLOAT':(full-fl).str(100),'omitted_squared_fraction':(omission/metrics['whole'][skey]).str(100),'far_fraction_of_omitted_squared':(metrics['far'][skey]/omission).str(100),'omission_norm_difference_fraction_of_total_discrepancy':((full-mid)/(full-fl)).str(100)}
 out={'utc':now(),'candidate':name,'raw_sha256':sha(src),'precision_bits':ctx.prec,'r0_exact':str(R0),'R_exact':str(R),'component_field_sha256':old['component_field_sha256'],'components':details,'domain_metrics':{d:{k:v.str(100) for k,v in val.items()} for d,val in metrics.items()},'FLOAT_comparison':comparisons,'mesh_audit':mesh_audit(),'mixed_derivative_checks':mixed,'all_full_energy_overlaps':True,'exact_partition_verified':True,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in ps+[oldp,src,mp,fp]},'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent candidate-level and partition review; exact own radial decomposition','foreign_code_executed':False}
 write(outp,out);print('PARTITION_DONE',name,'seconds',out['elapsed_seconds'],'kappa_comparison',comparisons['kappa'],flush=True)

if __name__=='__main__':
 ctx.prec=2048;prep=json.loads((BASE/'verification/PREPARE.json').read_text());assert prep['proof_sha256']==sha(BASE/'PROOF.md')
 ps=[Path(__file__),BASE/'PROOF.md',BASE/'verification/PREPARE.json']+H.common()
 for name,info in prep['frozen_publisher_text'].items():
  p=BASE/'source'/name;assert sha(p)==info['sha256'];ps.append(p)
 for num in [16,17]:run(num,ps)
