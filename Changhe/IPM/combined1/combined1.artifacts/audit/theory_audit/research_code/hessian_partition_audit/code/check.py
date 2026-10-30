"""Independent direct-hypergeometric radial partition of polar Hessians."""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
from hashlib import sha256
import importlib.util,json,time,math
from flint import fmpq as Q,arb,ctx
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
spec=importlib.util.spec_from_file_location('independent_hessian',BASE.parent/'scaled_hessian_audit/code/check.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
f=h.f;ar=h.ar
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
@lru_cache(None)
def direct(btext,atext,vtext,k):
 b,a,V=map(Q,(btext,atext,vtext));assert b>-1 and a>0 and 0<V<=1
 z=(-ar(a*V)).hypgeom_2f1(arb(k),ar(b+1),ar(b+2),bc=True,abc=True)/ar(b+1)
 assert z.is_finite();return z

def primitive(A,b,cuts,label):
 N=f.V*A.numerator_v();D,rows=f.crt_data(A.powers);pol,rem=divmod(N,D);replay=pol*D;parts=[]
 for a,k,Di,E,inv in rows:
  Ri=divmod(rem*inv,Di)[1];local=Ri(f.Poly([-1/a,1/a]))
  for j,q in enumerate(local):
   if q:parts.append((a,k-j,q))
  replay+=Ri*E
 assert replay==N
 vals={};records={}
 for name,V in cuts.items():
  vp=ar(V)**ar(b+1)
  value=sum((ar(q)*ar(V)**ar(b+j+1)/ar(b+j+1) for j,q in enumerate(pol)),arb(0))
  for a,k,q in parts:value+=ar(q)*vp*direct(str(b),str(a),str(V),k)
  assert value.is_finite() and value.rel_accuracy_bits()>150,(label,name,value)
  vals[name]=value;records[name]={'cut_exact':str(V),'value':value.str(100),'accuracy_bits':value.rel_accuracy_bits()}
 return vals,{'label':label,'b':str(b),'powers':A.powers,'polynomial_degree':pol.degree(),'principal_parts':len(parts),'exact_CRT_replay':True,'primitives':records}

def mesh():
 import numpy as np
 lo=math.log(.02);edges=np.linspace(lo,16.,math.ceil(16.-lo)+1);z,w=np.polynomial.legendre.leggauss(32)
 R=4178237423365963/500000000000;rows=[]
 for i,(left,right) in enumerate(zip(edges[:-1],edges[1:])):
  nodes=np.exp((left+right+(right-left)*z)/2);n=int(np.count_nonzero((nodes>=.02)&(nodes<=R)))
  if n:rows.append({'index':i,'selected_nodes':n,'left_log':float(left),'right_log':float(right)})
 return {'status':'FLOAT reconstruction only','rows':rows,'selected_nodes':sum(row['selected_nodes'] for row in rows),'all_panels_complete':all(row['selected_nodes']==32 for row in rows),'last_edge_radius':math.exp(rows[-1]['right_log'])}

def one(num,manifest):
 tick=time.monotonic();hp=BASE.parent/'scaled_hessian_audit/verification'/f'{num:03d}.json';whole=json.loads(hp.read_text())
 rawp=BASE.parent/'scaled_hessian_audit/data'/f'{num:03d}.json';pp=BASE/'source'/f'N4_{num:03d}.json';peer=json.loads(pp.read_text())
 assert sha(rawp)==whole['raw_sha256']==peer['raw_sha256']
 r0,R=Q(manifest['r0']),Q(manifest['R']);assert r0==Q(peer['r0_exact']) and R==Q(peer['R_exact'])
 cuts={'far':1/(1+R*R),'through_middle':1/(1+r0*r0),'whole':Q(1)}
 c,delta,fields=h.build(json.loads(rawp.read_text()));details={};energies={}
 print('FIELDS',num,'seconds',time.monotonic()-tick,flush=True)
 for label,(kind,field) in fields.items():
  assert f.F.field_hash(field)==whole['components'][label]['field_hash']
  gs,count=h.groups(field);pc=peer['components'][label];pm={r['ell']:r for r in pc['moments']};wm={r['ell']:r for r in whole['components'][label]['moments']}
  assert set(gs)==set(pm)==set(wm)
  totals={key:arb(0) for key in cuts};records=[]
  for ell,A in sorted(gs.items()):
   b=ell*delta/2-1;assert b==Q(pm[ell]['b'])
   vals,record=primitive(A,b,cuts,f'{num}:{label}:{ell}');record['ell']=ell
   for name,value in vals.items():
    overlap=value.overlaps(arb(pm[ell]['primitives'][name]['integral']));assert overlap,(num,label,ell,name)
    record['primitives'][name]['peer_overlap']=overlap;totals[name]+=value
   assert vals['whole'].overlaps(arb(wm[ell]['value']));record['own_whole_overlap']=True;records.append(record)
  totals={key:arb.pi()/2*v for key,v in totals.items()}
  comp={'origin':totals['whole']-totals['through_middle'],'middle':totals['through_middle']-totals['far'],'far':totals['far'],'whole':totals['whole']}
  assert all(v>0 and v.rel_accuracy_bits()>150 for v in comp.values())
  assert all(v.overlaps(arb(pc['energies'][key])) for key,v in comp.items())
  assert sum((comp[k] for k in ['origin','middle','far']),arb(0)).overlaps(comp['whole'])
  energies[label]=comp;details[label]={'group_count':len(gs),'pair_count':count,'moments':records,'energies':{k:v.str(100) for k,v in comp.items()},'all_peer_energy_overlaps':True}
  print('COMPONENT',num,label,'seconds',time.monotonic()-tick,flush=True)
 metrics={}
 for dom in ('origin','middle','far','whole'):
  X2=energies['xx'][dom]+energies['xy'][dom];Y2=energies['xy'][dom]+energies['yy'][dom];H2=X2+Y2
  K2=((arb(2).log()-arb(1)/2)*X2+(3*arb(2).log()-2)*Y2)/(16*arb.pi())
  vals={'X2':X2,'Y2':Y2,'D2':H2,'kappa2':K2,'X':X2.sqrt(),'Y':Y2.sqrt(),'D2rho':H2.sqrt(),'kappa':K2.sqrt()}
  assert all(v.overlaps(arb(peer['domain_metrics'][dom][k])) for k,v in vals.items())
  metrics[dom]=vals
 diag=json.loads((BASE/'source'/f'diag_{num:03d}.json').read_text());assert diag['sha256']==sha(rawp)
 diagkeys={'X':'D_rho_x_L2_inner','Y':'D_rho_y_L2_inner','kappa':'kappa_inner'}
 comparison={}
 for key in ('X','Y','kappa'):
  assert str(diag['BL2'][diagkeys[key]])==peer['FLOAT_comparison'][key]['saved_FLOAT']
  sk=key+'2';full,mid=metrics['whole'][key],metrics['middle'][key];fl=arb(peer['FLOAT_comparison'][key]['saved_FLOAT']);omit=metrics['origin'][sk]+metrics['far'][sk]
  v={'full_minus_middle':full-mid,'middle_minus_FLOAT':mid-fl,'full_minus_FLOAT':full-fl,'omitted_squared_fraction':omit/metrics['whole'][sk],'far_fraction_of_omitted_squared':metrics['far'][sk]/omit}
  assert all(z.overlaps(arb(peer['FLOAT_comparison'][key][k])) for k,z in v.items())
  comparison[key]={k:z.str(100) for k,z in v.items()}
 ma=mesh();assert ma['selected_nodes']==peer['mesh_audit']['selected_nodes'] and ma['all_panels_complete']==peer['mesh_audit']['all_selected_panels_complete']
 result={'utc':now(),'candidate':num,'raw_sha256':sha(rawp),'peer_sha256':sha(pp),'whole_result_sha256':sha(hp),'precision_bits':ctx.prec,'r0':str(r0),'R':str(R),'components':details,'domain_metrics':{d:{k:v.str(100) for k,v in vs.items()} for d,vs in metrics.items()},'FLOAT_comparison':comparison,'mesh_FLOAT':ma,'all_peer_and_whole_comparisons':True,'no_quadrature_error_global_theta_or_inverse_claim':True,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in [BASE/'PROOF.md',BASE/'data/manifest.json',Path(__file__),BASE.parent/'scaled_hessian_audit/code/check.py',BASE.parent/'scaled_hessian_audit/code/polar.py',BASE.parent/'scaled_hessian_audit/code/rational.py']},'elapsed_seconds':time.monotonic()-tick}
 with (BASE/'verification'/f'{num:03d}.json').open('x') as fd:json.dump(result,fd,indent=2);fd.write('\n')
 print('DONE',num,'seconds',result['elapsed_seconds'],'kappa',comparison['kappa'],flush=True)
if __name__=='__main__':
 ctx.prec=2048;m=json.loads((BASE/'data/manifest.json').read_text());assert sha(BASE/'PROOF.md')==m['proof_sha256']
 for rel,digest in m['files'].items():assert sha(ROOT/rel)==digest
 for num in (16,17):one(num,m)
