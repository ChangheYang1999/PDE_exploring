"""Independent four-pole projected Laplacian construction and two-weight cover."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import argparse,importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/candidate017_dyadic_preparation'
sys.set_int_max_str_digits(0);sys.path.insert(0,str(R/'research/joint_scaled_factored_weak/code'))
from fields_joint import Rat,ScaledRadial,TR,VR,T,V,SCALES,ar,field_hash
import weak as W

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
M=module('dyadic017_positive_pole',R/'research/rational_pole_moments/code/moments.py')
OLD=module('dyadic017_polynomial_calibration',R/'research/successor_dyadic_probes/code/check.py')
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
WEIGHTS=[Q(1,4),Q(7,4)]
def save(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def derivative(field,d,axis,delta):
 out={}
 for (ell,kind,n),A in field.items():
  P=A*TR**(d//2);radial=(1-d-ell*delta*TR)*P+2*TR*VR*P.derivative()
  minus=((radial+n*P)/2).divide_t((d+1)//2);plus=((radial-n*P)/2).divide_t((d+1)//2)
  target=kind
  if axis=='y':
   target='s' if kind=='c' else 'c';minus*=1 if kind=='s' else -1;plus*=-1 if kind=='s' else 1
  W.put(out,ell,target,n-1,minus);W.put(out,ell,target,n+1,plus)
 return {k:A for k,A in out.items() if A}
def trace(projected,n,delta):
 F={(ell,'s',n):A for ell,A in projected.items()};dx=derivative(F,0,'x',delta);dy=derivative(F,0,'y',delta)
 xx=derivative(dx,1,'x',delta);yy=derivative(dy,1,'y',delta);xy=derivative(dx,1,'y',delta);yx=derivative(dy,1,'x',delta);assert xy==yx
 cart={k:xx.get(k,Rat())+yy.get(k,Rat()) for k in set(xx)|set(yy)};cart={k:A for k,A in cart.items() if A}
 polar={};terms=[];ends=[]
 for ell,P in sorted(projected.items()):
  z=ell*delta/2;td=lambda A:(1-2*z*TR)*A+2*TR*VR*A.derivative();numerator=td(td(P))-n*n*P
  if not numerator:continue
  lap=numerator.divide_t(1);polar[ell,'s',n]=lap;nv=lap.numerator_v();q=next(i for i,c in enumerate(nv) if c)
  stripped=Rat(Poly(list(nv)[q:])(V),lap.powers);assert lap==VR**q*stripped and ell*delta+2*q-2>0
  terms.append((ell,q,stripped));ends.append({'ell':ell,'endpoint_order':q,'degree':stripped.P.degree(),'powers':list(stripped.powers),'diagonal_integrability_margin':str(ell*delta+2*q-2)})
 assert cart==polar and terms
 return polar,terms,ends,{'dx':dx,'dy':dy,'xx':xx,'yy':yy,'xy':xy}
def prepare(terms,delta):
 groups={};pairs=0
 for i,(ell,q,A) in enumerate(terms):
  for j in range(i,len(terms)):
   k,q2,C=terms[j];b=(ell+k)*delta/2+q+q2-3;assert b>-1;W.add(groups,b,A*C*(1 if i==j else 2));pairs+=1
 prepared=[]
 for index,(b,A) in enumerate(sorted(groups.items()),1):
  start=time.monotonic();numerator=V*A.numerator_v();factors=[(a,k) for a,k in zip(SCALES,A.powers) if k]
  polynomial,parts,merged,degree=M.decompose(numerator,factors)
  record={'b_without_a':str(b),'numerator_degree':numerator.degree(),'denominator_degree':degree,'principal_parts':len(parts),'factors':[[str(a),k] for a,k in merged],'exact_reconstruction':True,'numerator_sha256':sha256(('\n'.join(map(str,numerator))+'\n').encode()).hexdigest()}
  prepared.append((b,polynomial,parts,merged,record));print(now(),'GROUP',index,'of',len(groups),'seconds',time.monotonic()-start,flush=True)
 return prepared,pairs,field_hash({str(b):A for b,A in groups.items()})
def integrate(prepared,a):
 total=arb(0);rows=[]
 for b,polynomial,parts,merged,rec in prepared:
  exponent=b+a;assert exponent>-1;z=sum((ar(c/(exponent+j+1)) for j,c in enumerate(polynomial)),arb(0));cache={scale:M.pole_moments(exponent,scale,power) for scale,power in merged}
  for scale,power,c in parts:z+=ar(c)*cache[scale][power]
  assert z.is_finite() and (z==0 or z.rel_accuracy_bits()>150);total+=z;rows.append({'b':str(exponent),'integral':z.str(100),'accuracy_bits':z.rel_accuracy_bits()})
 energy=arb.pi()/2*total;assert energy>0 and energy.rel_accuracy_bits()>150
 return {'a':str(a),'energy':energy.str(100),'norm':energy.sqrt().str(100),'accuracy_bits':energy.rel_accuracy_bits(),'groups':rows}
def same(left,right):return set(left)==set(right) and all(not any(left[k].powers) and left[k].P==right[k] for k in right)
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--calibration-only',action='store_true');args=parser.parse_args();ctx.prec=2048;started=time.monotonic();inputs={}
 def bind(p,h=None):
  p=Path(p);got=sha(p);assert h is None or h==got,(p,h,got);inputs[str(p.relative_to(R))]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 for name,entry in prep['files'].items():bind(B/'source'/name,entry['sha256'])
 peer=read(B/'source/N3_cells.json');assert peer['code_sha256']==sha(B/'source/N3_legqs_cells.py')
 for rel in ['research/joint_scaled_factored_weak/PROOF.md','research/scaled_dyadic_probes/PROOF.md','research/rational_pole_moments/PROOF.md','research/rational_pole_moments/reviews/T4/ACCEPTANCE.json','research/origin_dyadic_ceiling/source/T4_origin_dyadic_inverse_PROOF.md','research/origin_dyadic_ceiling/source/T4_origin_spectral_line_PROOF.md','research/origin_dyadic_ceiling/reviews/T1_REVIEWS_v13.md','research/origin_dyadic_ceiling/reviews/T1_REVIEWS_v14.md']:
  bind(R/rel)
 for mod in list(sys.modules.values()):
  path=getattr(mod,'__file__',None)
  if path and Path(path).is_relative_to(R) and Path(path).suffix=='.py':bind(Path(path))
 allresults={}
 for suffix in ['007-d2w-j7-e2bal','017-legqs50-quot013']:
  name='C1-N1-'+suffix;cal=suffix.startswith('007');directory=B/'verification'/name;directory.mkdir(exist_ok=True)
  if cal:
   src=bind(R/f'research/candidate_audits/data/{name}/canonical.json','153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316');audit=read(R/f'research/candidate_audits/verification/{name}.json');assert audit['canonical_sha256']==sha(src)
  else:
   snap=R/f'research/candidate_audits/data/{name}';manifest=read(snap/'MANIFEST.json');src=bind(snap/manifest['coefficient_files'][0]['name'],'7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114');audit=read(R/f'research/generator_sector_audit/verification/{name}_direct.json');assert audit['generator_sha256']==sha(src) and audit['B0n_exact'] and audit['sector_summary']['all_forbidden_zero'] and peer['source_sha256']==sha(src)
  model=ScaledRadial(src);assert model.c==Q(4076476460239181,2251799813685248)
  if cal:oldmodel=OLD.Radial(src)
  records={}
  for n in [1,3]:
   outpath=directory/f'mode_{n:03d}.json'
   if outpath.exists():
    row=read(outpath);assert row['raw_sha256']==sha(src) and row['code_sha256']==sha(__file__);records[n]=row;continue
   start=time.monotonic();projected,counts=W.project(model,n);lap,terms,ends,derivs=trace(projected,n,model.delta);checks={}
   previous=read(R/f'research/scaled_dyadic_probes/verification/C1-N1-007-d2w-j7-e2bal/mode_{n:03d}.json')
   if cal:
    oldproj,_=OLD.W.project(oldmodel,n);checks['projection']=same(projected,oldproj)
    oldF={(ell,'s',n):P for ell,P in oldproj.items()};ox=OLD.derivative(oldF,0,'x',model.delta);oy=OLD.derivative(oldF,0,'y',model.delta)
    od={'dx':ox,'dy':oy,'xx':OLD.derivative(ox,1,'x',model.delta),'yy':OLD.derivative(oy,1,'y',model.delta),'xy':OLD.derivative(ox,1,'y',model.delta)}
    checks.update({key:same(derivs[key],value) for key,value in od.items()});assert all(checks.values())
   print(now(),'TRACE',name,n,'branches',len(projected),'seconds',time.monotonic()-start,flush=True)
   prepared,pairs,gh=prepare(terms,model.delta);weights=[]
   for a in WEIGHTS:
    w=integrate(prepared,a)
    if cal:
     pr=next(z for z in previous['weights'] if Q(z['a'])==a);assert arb(w['energy']).overlaps(arb(pr['energy']));w['accepted007_energy_overlap']=True
    weights.append(w);print(now(),'WEIGHT',name,n,str(a),w['norm'][:60],flush=True)
   row={'utc':now(),'candidate':name,'raw_sha256':sha(src),'code_sha256':sha(__file__),'mode':n,'projection_sha256':field_hash(projected),'projection_pairs':counts,'Laplacian_sha256':field_hash(lap),'Cartesian_polar_equal':True,'mixed_derivatives_equal':True,'polynomial_calibration':checks,'endpoints':ends,'pairs':pairs,'group_count':len(prepared),'group_sha256':gh,'decompositions':[z[4] for z in prepared],'weights':weights,'elapsed_seconds':time.monotonic()-start}
   save(outpath,row);bind(outpath);records[n]=row
  sums={str(a):sum((arb(next(w['energy'] for w in records[n]['weights'] if Q(w['a'])==a)) for n in [1,3]),arb(0)) for a in WEIGHTS}
  allresults[name]={'square_norms':{a:z.str(100) for a,z in sums.items()},'norms':{a:z.sqrt().str(100) for a,z in sums.items()}}
  if cal:
   if args.calibration_only:break
   continue
  comparisons={}
  for a in WEIGHTS:
   prow=next(z for z in peer['cells'] if Q(z['cell'][1])==a);pball=arb(prow['N_h_modes13_sq_ball']);own=sums[str(a)];assert own.overlaps(pball) and pball.lower()<own.lower() and own.upper()<pball.upper();comparisons[str(a)]={'own_square':own.str(100),'peer_square':str(pball),'containing_display':True}
  c=model.c;star,hmax=OLD.maximum(c);A=1+1/c;assert Q(3,2)<A<Q(7,4);points=[Q(k,4) for k in range(7)]+[A];cells=[]
  for i,(left,right) in enumerate(zip(points[:-1],points[1:])):
   e=Q(1,4) if i==0 else Q(7,4);assert e>=right;norm=sums[str(e)].sqrt();low=arb(5)**ar((left-2)/2)*norm;high=hmax*ar((1+c-c*left)/(1+left));gap=low-high;ratio=low/high;assert gap>0
   floor=Q(int((ratio.lower()*10**12).floor().unique_fmpz())-1,10**12);assert ar(floor)<ratio
   cells.append({'left':str(left),'right':str(right),'norm_evaluation_at':str(e),'projected_norm':norm.str(100),'lower':low.str(100),'upper':high.str(100),'gap':gap.str(100),'ratio':ratio.str(100),'strict_ratio_floor':str(floor),'excluded':True})
  a0=Q(audit['origin']['a0']);strain=Q(audit['origin']['strain']);assert a0>=5*c-4 and strain==1-c
  allresults[name].update(peer_comparisons=comparisons,seven_cells=cells,a0_exact=str(a0),strain_exact=str(strain),smax=star.str(100),Hmax=hmax.str(100),conditional_all_seven_excluded=True)
 assert all(sha(R/path)==h for path,h in inputs.items())
 result={'utc':now(),'precision_bits':ctx.prec,'inputs':inputs,'results':allresults,'two_weights_only':True,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-started,'verdict':'CONFIRMED own two projected norms and N3 displayed-square comparisons; seven-cell implication conditional on exact stated framework hypotheses' if not args.calibration_only else 'CONFIRMED accepted007 calibration only; actual017 OPEN'}
 out=B/'verification'/('calibration.json' if args.calibration_only else 'result.json');save(out,result);print(now(),'DONE',sha(out),flush=True)
if __name__=='__main__':main()
