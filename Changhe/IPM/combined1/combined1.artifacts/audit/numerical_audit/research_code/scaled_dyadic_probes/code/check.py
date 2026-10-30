"""Exact positive-pole projected Laplacian norms and conditional cells."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/scaled_dyadic_probes'
sys.set_int_max_str_digits(0);sys.path.insert(0,str(ROOT/'research/scaled_weak_backend/code'))
from fields import Rat,ScaledRadial,T,V,TR,VR,SCALES,ar,field_hash

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
W=module('n4_scaled_weak_dyadic',ROOT/'research/scaled_weak_backend/code/weak_v3.py')
OLD=module('n4_polynomial_dyadic',ROOT/'research/successor_dyadic_probes/code/check.py')
MOM=W.moments
WEIGHTS=[Q(k,4) for k in range(8)]
CALNAME='C1-N1-007-d2w-j7-e2bal';SCALEDNAME='C1-N1-010-d2w-j7-x3bal-legqs'
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def new(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')

def derivative(field,d,axis,delta):
 out={}
 for (ell,kind,n),A in field.items():
  P=A*TR**(d//2)
  radial=(1-d-ell*delta*TR)*P+2*TR*VR*P.derivative()
  minus=((radial+n*P)/2).divide_t((d+1)//2)
  plus=((radial-n*P)/2).divide_t((d+1)//2)
  target=kind
  if axis=='y':
   target='s' if kind=='c' else 'c';minus*=1 if kind=='s' else -1;plus*=-1 if kind=='s' else 1
  W.put(out,ell,target,n-1,minus);W.put(out,ell,target,n+1,plus)
 return {key:A for key,A in out.items() if A}

def origin(model):
 def atzero(field):
  answer=Q(0)
  for (j,n),A in field.items():
   coefficient=A.divide_t(2).exact_value(0)
   if n:assert not coefficient,(j,n)
   else:answer+=coefficient
  return answer
 a0,strain=atzero(model.ry),atzero(model.deriv(2,2))
 assert 1<model.c<2 and strain==1-model.c and a0>=5*model.c-4
 return a0,strain

def same_fields(left,right):
 return set(left)==set(right) and all(left[k]==Rat(right[k]) for k in right)

def trace(projected,n,delta):
 F={(ell,'s',n):A for ell,A in projected.items()}
 dx,dy=derivative(F,0,'x',delta),derivative(F,0,'y',delta)
 xy,yx=derivative(dx,1,'y',delta),derivative(dy,1,'x',delta)
 assert xy==yx
 xx,yy=derivative(dx,1,'x',delta),derivative(dy,1,'y',delta)
 cart={k:xx.get(k,Rat())+yy.get(k,Rat()) for k in set(xx)|set(yy)};cart={k:A for k,A in cart.items() if A}
 polar={};terms=[];endpoints=[]
 for ell,P in sorted(projected.items()):
  z=ell*delta/2
  td=lambda A:(1-2*z*TR)*A+2*TR*VR*A.derivative()
  numerator=td(td(P))-n*n*P
  if not numerator:continue
  lap=numerator.divide_t(1);polar[ell,'s',n]=lap
  nv=lap.numerator_v();q=next(i for i,c in enumerate(nv) if c)
  stripped=Rat(Poly(list(nv)[q:])(V),lap.powers)
  assert lap==VR**q*stripped and ell*delta+2*q-2>0
  terms.append((ell,q,stripped));endpoints.append({'ell':ell,'endpoint_order':q,'numerator_degree':stripped.P.degree(),'pole_powers':list(stripped.powers),'diagonal_integrability_margin':str(ell*delta+2*q-2)})
 assert cart==polar and terms
 return polar,terms,endpoints,{'dx':dx,'dy':dy,'xx':xx,'yy':yy,'xy':xy}

def prepare_groups(terms,delta):
 groups={};pair_count=0
 for i,(ell,q,A) in enumerate(terms):
  for j in range(i,len(terms)):
   k,q2,B=terms[j];b=(ell+k)*delta/2+q+q2-3
   assert b>-1;W.add(groups,b,A*B*(1 if i==j else 2));pair_count+=1
 prepared=[]
 for index,(b,A) in enumerate(sorted(groups.items()),1):
  tick=time.monotonic();numerator=V*A.numerator_v();factors=[(a,k) for a,k in zip(SCALES,A.powers) if k]
  polynomial,parts,merged,degree=MOM.decompose(numerator,factors)
  prepared.append((b,polynomial,parts,merged,{'b_without_a':str(b),'numerator_degree':numerator.degree(),'denominator_degree':degree,'principal_parts':len(parts),'factors':[[str(a),k] for a,k in merged],'exact_reconstruction':True,'elapsed_seconds':time.monotonic()-tick}))
  print('GROUP',index,'/',len(groups),'degree',degree,'seconds',time.monotonic()-tick,flush=True)
 return prepared,pair_count,field_hash({str(b):A for b,A in groups.items()})

def evaluate_prepared(prepared,a):
 total=arb(0);minbits=10**9
 for b,polynomial,parts,merged,record in prepared:
  exp=b+a;assert exp>-1
  value=sum((ar(c/(exp+j+1)) for j,c in enumerate(polynomial)),arb(0))
  cache={scale:MOM.pole_moments(exp,scale,power) for scale,power in merged}
  for scale,power,coefficient in parts:value+=ar(coefficient)*cache[scale][power]
  assert value.is_finite();minbits=min(minbits,value.rel_accuracy_bits());total+=value
 energy=arb.pi()/2*total;assert energy>0 and energy.rel_accuracy_bits()>150
 return energy,minbits

def run(name,modes,bits):
 start=time.monotonic();ctx.prec=bits;assert name in [CALNAME,SCALEDNAME]
 if name==CALNAME:
  src=ROOT/f'research/candidate_audits/data/{name}/canonical.json';apath=ROOT/f'research/candidate_audits/verification/{name}.json'
  audit=json.loads(apath.read_text());assert H(src)==audit['canonical_sha256'] and audit['all_forbidden_zero'] and audit['B0n_exact'] and all(audit['snapshot_hashes_confirmed'].values())
 else:
  src=ROOT/f'research/candidate_audits/data/{name}/d2w_j7_n4_X3bal_legqs_mid180_exact.json';apath=ROOT/f'research/generator_sector_audit/verification/{name}_direct.json'
  audit=json.loads(apath.read_text());assert H(src)==audit['generator_sha256'] and audit['sector_summary']['all_forbidden_zero'] and audit['B0n_exact']
  assert all(H(src.parent/filename)==digest for filename,digest in audit['snapshot_hashes'].items())
 model=ScaledRadial(src);a0,strain=origin(model);points={}
 if name==CALNAME:
  assert a0==Q(model.state['a0']) and strain==Q(model.state['strain'])
 else:
  assert a0==Q(audit['origin']['a0']) and strain==Q(audit['origin']['strain']) and model.c==Q(audit['c_exact'])
  fields=model.evaluate(*audit['point']);points={key:value.overlaps(arb(audit['fields'][key])) for key,value in fields.items()}
  assert set(points)=={'rho','u1','u2','rho_x','rho_y','residual'} and all(points.values())
 paths=[src,apath,Path(__file__),BASE/'PROOF.md',ROOT/'research/scaled_weak_backend/code/fields.py',ROOT/'research/scaled_weak_backend/code/weak_v3.py',ROOT/'research/scaled_weak_backend/PROOF.md',ROOT/'research/rational_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/PROOF.md',ROOT/'research/rational_pole_moments/reviews/T4/ACCEPTANCE.json',ROOT/'research/successor_dyadic_probes/code/check.py',ROOT/'research/successor_dyadic_probes/PROOF.md',ROOT/'research/whole_plane_norms/code/norms.py',ROOT/'research/origin_dyadic_ceiling/reviews/T1_REVIEWS_v13.md',ROOT/'research/origin_dyadic_ceiling/reviews/T1_REVIEWS_v14.md']
 manifest={'candidate':name,'bits':bits,'weights':list(map(str,WEIGHTS)),'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths},'c_exact':str(model.c),'a0_exact':str(a0),'strain_exact':str(strain),'six_physical_point_checks':points}
 dest=BASE/'verification'/name
 if (dest/'manifest.json').exists():assert json.loads((dest/'manifest.json').read_text())==manifest
 else:new(dest/'manifest.json',manifest)
 mh=H(dest/'manifest.json');records={}
 oldmodel=OLD.Radial(src) if name==CALNAME else None
 print('PREPARED',name,'seconds',time.monotonic()-start,flush=True)
 for n in modes:
  path=dest/f'mode_{n:03d}.json'
  if path.exists():
   row=json.loads(path.read_text());assert row['manifest_sha256']==mh;records[n]=row;continue
  tick=time.monotonic();projected,counts=W.project(model,n);polar,terms,endpoints,derivs=trace(projected,n,model.delta);fieldcal={};calpath=None
  print('TRACE',name,n,'branches',len(projected),'seconds',time.monotonic()-tick,flush=True)
  if name==CALNAME:
   oldprojection,_=OLD.W.project(oldmodel,n);fieldcal['projection']=same_fields(projected,oldprojection)
   oldF={(ell,'s',n):P for ell,P in oldprojection.items()};oldx=OLD.derivative(oldF,0,'x',model.delta);oldy=OLD.derivative(oldF,0,'y',model.delta)
   oldderivs={'dx':oldx,'dy':oldy,'xx':OLD.derivative(oldx,1,'x',model.delta),'yy':OLD.derivative(oldy,1,'y',model.delta),'xy':OLD.derivative(oldx,1,'y',model.delta)}
   fieldcal.update({key:same_fields(derivs[key],value) for key,value in oldderivs.items()});assert all(fieldcal.values())
   calpath=ROOT/f'research/successor_dyadic_probes/verification/{name}/mode_{n:03d}.json';previous=json.loads(calpath.read_text())
  else:
   calpath=BASE/f'verification/{CALNAME}/mode_{n:03d}.json';previous=json.loads(calpath.read_text());assert all(previous['exact_polynomial_field_calibration'].values()) and previous['code_sha256']==H(__file__)
  prepared,pair_count,group_hash=prepare_groups(terms,model.delta);weights=[]
  for a in WEIGHTS:
   energy,minbits=evaluate_prepared(prepared,a);norm=energy.sqrt();checks={}
   if name==CALNAME:
    pr=next(z for z in previous['weights'] if Q(z['a'])==a);checks={'energy':energy.overlaps(arb(pr['energy'])),'norm':norm.overlaps(arb(pr['norm']))};assert all(checks.values())
   weights.append({'a':str(a),'energy':energy.str(100),'norm':norm.str(100),'energy_accuracy_bits':energy.rel_accuracy_bits(),'minimum_group_accuracy_bits':minbits,'polynomial_calibration':checks})
   print('WEIGHT',name,n,str(a),norm.str(26),'seconds',time.monotonic()-tick,flush=True)
  row={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'mode':n,'manifest_sha256':mh,'code_sha256':H(__file__),'calibration_input_sha256':H(calpath),'projection_sha256':field_hash(projected),'projection_pairs':counts,'Laplacian_sha256':field_hash(polar),'exact_Cartesian_polar_trace_equal':True,'exact_mixed_derivatives_equal':True,'exact_polynomial_field_calibration':fieldcal,'endpoints':endpoints,'pair_count':pair_count,'group_sha256':group_hash,'radial_groups':len(prepared),'moment_decompositions':[z[4] for z in prepared],'weights':weights,'elapsed_seconds':time.monotonic()-tick,'status':'Polynomial calibration confirmed by comparison; scaled candidate OPEN independent peer'}
  new(path,row);records[n]=row
 star,hmax=OLD.maximum(model.c);cover=OLD.cells(records,modes,model.c,hmax);calibration=[]
 if name==CALNAME:
  oldresultpath=ROOT/f'research/successor_dyadic_probes/verification/{name}/result.json';oldresult=json.loads(oldresultpath.read_text())
  oldrecords={n:json.loads((oldresultpath.parent/f'mode_{n:03d}.json').read_text()) for n in modes};oldcells=OLD.cells(oldrecords,modes,model.c,hmax)
  for a,b in zip(cover,oldcells,strict=True):
   cc={key:arb(a[key]).overlaps(arb(b[key])) for key in ['projected_norm','lower','upper','gap','ratio']};assert all(cc.values());calibration.append(cc)
 output=dest/('result_modes_'+'_'.join(f'{n:03d}' for n in modes)+'.json')
 result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'manifest_sha256':mh,'mode_result_sha256':{str(n):H(dest/f'mode_{n:03d}.json') for n in modes},'selected_modes':modes,'a0_exact':str(a0),'origin_threshold_margin':str(a0-(5*model.c-4)),'s_maximizer':star.str(100),'H_max':hmax.str(100),'seven_cells':cover,'all_seven_excluded':all(z['excluded'] for z in cover),'polynomial_cell_calibration':calibration,'complete_upper_norm':False,'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent peer for scaled candidate; conditional necessary scalar test'}
 new(output,result);print('DONE',name,'all7',result['all_seven_excluded'],'seconds',result['elapsed_seconds'],flush=True)
 for z in cover:print(z['left'],z['right'],z['ratio'][:55],z['excluded'],flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('candidate',nargs='+');p.add_argument('--modes',type=int,nargs='+',default=[1,3]);p.add_argument('--bits',type=int,default=2048);a=p.parse_args()
 assert a.bits>=1024 and a.modes==sorted(set(a.modes)) and all(n>0 and n%2 for n in a.modes) and {1,3}<=set(a.modes)
 for name in a.candidate:run(name,a.modes,a.bits)
