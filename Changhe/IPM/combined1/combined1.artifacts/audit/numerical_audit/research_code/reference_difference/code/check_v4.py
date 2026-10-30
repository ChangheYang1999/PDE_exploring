"""Whole-plane exact density differences, with explicit reference compatibility."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from collections import defaultdict
import argparse,importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,acb,ctx
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/reference_difference';sys.set_int_max_str_digits(0)
def load(name,rel):
 spec=importlib.util.spec_from_file_location(name,ROOT/rel);out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out
J=load('difference_radial','research/joint_scaled_factored_weak/code/fields_joint.py')
C=load('difference_cartesian','research/multiscale_generators/code/cartesian.py')
M=load('difference_moments','research/rational_pole_moments/code/moments.py')
Rat,T,V,ar=J.Rat,J.T,J.V,J.ar
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def log(*x):print(now(),*x,flush=True)
def save(path,data):
 p=path.with_suffix('.pending');p.write_text(json.dumps(data,indent=2)+'\n');p.replace(path)
def polyhash(P):
 h=sha256();h.update(str(len(P)).encode()+b'\n')
 for q in P:h.update(str(q).encode()+b'\n')
 return h.hexdigest()
def shape(g):return int(g['j']),int(g['m']),tuple(g['spec'])
def exact_rows(raw):
 assert C.rational(raw.get('cl',raw.get('cl_exact')))==Q(4076476460239181,2251799813685248)
 rows={}
 for g in raw['generators']:
  j,m,spec=shape(g);w,n,q,R=C.spec_parts(spec);a=C.rational(g['coef'])
  assert min(j,m,w,n,q)>=0 and R in [Q(1),Q(10),Q(25),Q(50),Q(100)]
  key=j,m,spec;assert key not in rows,('duplicate raw shape',key);rows[key]=a
 return rows

def difference(parent,successor):
 one,two=exact_rows(parent),exact_rows(successor);keys=sorted(set(one)|set(two),key=lambda k:(k[0],k[1],str(k[2])))
 rows=[{'j':j,'m':m,'spec':list(spec),'coef':str(two.get((j,m,spec),Q(0))-one.get((j,m,spec),Q(0)))} for j,m,spec in keys if two.get((j,m,spec),Q(0))!=one.get((j,m,spec),Q(0))]
 raw={'cl_exact':str(Q(4076476460239181,2251799813685248)),'generators':rows,'meaning':'Exact successor potential minus parent potential; not a new stationary candidate'}
 prefixes=[]
 for ell in range(1,5):
  first,second=defaultdict(Q),defaultdict(Q)
  for collection,target in [(one,first),(two,second)]:
   for (j,m,spec),a in collection.items():
    if j+1==ell and C.spec_parts(spec)[2]==0:target[2*m]+=a
  first={n:a for n,a in first.items() if a};second={n:a for n,a in second.items() if a}
  diff={n:second.get(n,Q(0))-first.get(n,Q(0)) for n in set(first)|set(second) if second.get(n,Q(0))!=first.get(n,Q(0))}
  prefixes.append({'ell':ell,'first':{str(n):str(a) for n,a in sorted(first.items())},'second':{str(n):str(a) for n,a in sorted(second.items())},'difference':{str(n):str(a) for n,a in sorted(diff.items())},'equal':not diff})
 return raw,prefixes

def compact_fields(raw):
 model=J.ScaledRadial(raw);out={};endpoints=[]
 for label in ['rho','u1','u2']:
  field,d,kind=model.fields[label];assert d==3;out[label]={}
  for (j,n),A in field.items():
   A=A.divide_t(2)
   if not A:continue
   assert n>=0 and (kind!='s' or n>0)
   if label=='rho':assert kind=='s' and n%2==1
   out[label][j+1,kind,n]=A
   if j<4:
    value=A.exact_value(Q(1));assert value==0,(label,j,n,'uncancelled non-L2 endpoint')
    endpoints.append({'field':label,'ell':j+1,'kind':kind,'n':n,'value':'0'})
 return model,out,endpoints

def fieldrecord(field):
 rows=[];h=sha256()
 for key,A in sorted(field.items()):
  row={'key':list(key),'degree_t':A.P.degree(),'powers':list(A.powers),'numerator_sha256':polyhash(A.P)}
  h.update(json.dumps(row,sort_keys=True,separators=(',',':')).encode()+b'\n');rows.append(row)
 return {'component_count':len(rows),'representation_sha256':h.hexdigest(),'components':rows}

def point_checks(raw,fields,delta):
 result=[];minimum=10**9
 for xs,ys in [('3/7','-2/5'),('21','-9'),('600','800')]:
  direct=C.GeneratorJet(raw,xs,ys,order=4).fields();x,y=ar(C.rational(xs)),ar(C.rational(ys));r=(x*x+y*y).sqrt();v=1/(1+r*r);t=1-v;z=acb(x/r,y/r);maximum=max((n for field in fields.values() for ell,kind,n in field),default=0);powers=[acb(1)]
  for _ in range(maximum):powers.append(powers[-1]*z)
  fractional={ell:v**ar(ell*delta/2) for field in fields.values() for ell,kind,n in field};row={'x':xs,'y':ys,'fields':{}}
  for label,field in fields.items():
   val=arb(0)
   for (ell,kind,n),A in field.items():val+=r*fractional[ell]*A.evaluate(t,v)*(powers[n].imag if kind=='s' else powers[n].real)
   expected=direct[label];assert val.overlaps(expected),(xs,ys,label,val,expected)
   if field:
    bits=min(val.rel_accuracy_bits(),expected.rel_accuracy_bits());assert bits>150;minimum=min(minimum,bits)
   else:bits=None;assert expected.contains(0)
   row['fields'][label]={'compact':val.str(100),'Cartesian':expected.str(100),'overlap':True,'accuracy_bits':bits}
  result.append(row);log('POINT',xs,ys)
 return {'points':result,'value_count':len(result)*3,'minimum_accuracy_bits':minimum if minimum<10**9 else None}

def norm(field,delta,checkpoint=lambda s:None):
 if not field:return {'exact_zero':True,'square_ball':'0','norm_ball':'0','tau_upper_exact':'0','groups':[],'group_count':0,'ordered_pairs':0}
 bymode={};groups={};count=0
 for (ell,kind,n),A in field.items():assert kind=='s' and n>0;bymode.setdefault(n,[]).append((ell,A))
 for n,rows in sorted(bymode.items()):
  for ell,A in rows:
   for ell2,Bb in rows:groups[ell+ell2]=groups.get(ell+ell2,Rat())+A*Bb;count+=1
 records=[];total=arb(0);minimum=10**9;log('GROUPS_READY',len(groups),'ordered_pairs',count)
 for ell,A in sorted(groups.items()):
  if not A:continue
  numerator=V*A.numerator_v();order=0
  while numerator[0]==0:numerator,remainder=divmod(numerator,T);assert not remainder;order+=1
  exponent=ell*delta/2-3+order;assert exponent>-1,(ell,str(exponent))
  factors=[(a,k) for a,k in zip(J.SCALES,A.powers) if k];value,meta=M.integral(exponent,numerator,factors)
  assert value.is_finite() and value.rel_accuracy_bits()>150,(ell,value);minimum=min(minimum,value.rel_accuracy_bits());total+=value
  records.append({'ell_sum':ell,'endpoint_v_order':order,'b':str(exponent),'degree_v':numerator.degree(),'powers':list(A.powers),'numerator_v_sha256':polyhash(numerator),'integral_ball':value.str(100),'integral_accuracy_bits':value.rel_accuracy_bits(),'decomposition':meta})
  checkpoint({'status':'RUNNING complete radial groups','group_count':len(records),'groups':records,'sum_ball':total.str(100),'ordered_pairs':count});log('GROUP',ell,'b',str(exponent),'bits',value.rel_accuracy_bits())
 square=arb.pi()/2*total;assert square>0 and square.is_finite();val=square.sqrt();denom=10**30;tau=Q(int((val.upper()*denom).ceil().unique_fmpz())+1,denom);assert val<ar(tau)
 return {'exact_zero':False,'square_ball':square.str(100),'norm_ball':val.str(100),'tau_upper_exact':str(tau),'norm_accuracy_bits':val.rel_accuracy_bits(),'minimum_group_accuracy_bits':minimum,'sum_ball':total.str(100),'groups':records,'group_count':len(records),'ordered_pairs':count}

def own_snapshot(name):
 path=ROOT/'research/candidate_audits/data'/name;manifestp=path/'MANIFEST.json';manifest=json.loads(manifestp.read_text());assert manifest['id']==name and len(manifest['coefficient_files'])==1
 entry=manifest['coefficient_files'][0];assert Path(entry['name']).name==entry['name'];rawp=path/entry['name'];assert sha(rawp)==entry['sha256'];shared=ROOT.parent/'c1-shared/candidate_snapshots'/name/rawp.name;assert sha(shared)==sha(rawp)
 return rawp,json.loads(rawp.read_text()),manifestp

def main():
 ap=argparse.ArgumentParser();ap.add_argument('successor');ap.add_argument('parent');ap.add_argument('--bits',type=int,default=2048);args=ap.parse_args();ctx.prec=args.bits;start=time.monotonic();output=B/f'verification/{args.successor}_minus_{args.parent}_{args.bits}_v4.json';assert not output.exists()
 pp,parent,pm=own_snapshot(args.parent);sp,successor,sm=own_snapshot(args.successor);raw,prefix=difference(parent,successor)
 paths=[Path(__file__),B/'RUNNER_V4.md',B/'PROOF.md',B/'verification/fixtures.json',ROOT/'research/joint_scaled_factored_weak/code/fields_joint.py',ROOT/'research/joint_scaled_factored_weak/PROOF.md',ROOT/'research/multiscale_generators/code/cartesian.py',ROOT/'research/multiscale_generators/PROOF.md',ROOT/'research/rational_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/PROOF.md',pp,sp,pm,sm]
 fixture=json.loads((B/'verification/fixtures.json').read_text());assert all(fixture['checks'].values())
 for rel,h in fixture['inputs'].items():assert sha(ROOT/rel)==h
 state={'utc_start':now(),'parent':args.parent,'successor':args.successor,'parent_raw_sha256':sha(pp),'successor_raw_sha256':sha(sp),'inputs':{str(p.relative_to(ROOT)):sha(p) for p in paths},'precision_bits':args.bits,'prefix':prefix,'potential_prefix_equal':all(row['equal'] for row in prefix),'difference_nonzero_generator_count':len(raw['generators']),'no_foreign_code_executed':True,'status':'RUNNING own difference calculation'};save(output,state)
 if not state['potential_prefix_equal']:
  state.update({'utc':now(),'status':'Sufficient potential-prefix hypothesis fails; density L2 membership and screening OPEN','elapsed_seconds':time.monotonic()-start});save(output,state);log('PREFIX_NOT_EQUAL');return
 rawp=B/f'data/{args.successor}_minus_{args.parent}.json';assert not rawp.exists();rawp.write_text(json.dumps(raw,indent=2)+'\n');state['inputs'][str(rawp.relative_to(ROOT))]=sha(rawp)
 model,fields,endpoints=compact_fields(raw);state.update({'fields':{k:fieldrecord(v) for k,v in fields.items()},'endpoint_checks':endpoints,'canonical_velocity_scope':'PROOF(P) implies V=U[g] by L2 harmonic uniqueness; common weak class is all real S1 L2 functions','point_checks':point_checks(raw,fields,model.delta)});save(output,state)
 def checkpoint(record):state['norm']=record;state['utc']=now();state['elapsed_seconds']=time.monotonic()-start;save(output,state)
 result=norm(fields['rho'],model.delta,checkpoint);checkpoint(result)
 known={'C1-N1-016-legqs25-quot013':('research/candidate016_weak_peer/verification/result.json','research/candidate016_weak_peer/PROOF.md'),'C1-N1-020-legqs25p50-quot013':('research/candidate020_weak_peer/verification/result.json','research/candidate020_weak_peer/PROOF.md')}
 if args.parent in known:
  rp,proof=map(lambda rel:ROOT/rel,known[args.parent]);accepted=json.loads(rp.read_text());assert accepted['candidate']==args.parent and accepted['verdict'].startswith('CONFIRMED');row=next(r for r in accepted['rows'] if r['n']==19 and r['K']==1800);d=Q(row['strict_floor']);bindings={}
  for rel,h in accepted['own_inputs'].items():assert sha(ROOT/rel)==h;bindings[rel]=h
  for rel,info in accepted['frozen_or_retained_sources'].items():assert sha(ROOT/rel)==info['stored_sha256'];bindings[rel]=info['stored_sha256']
  assert bindings[str(pp.relative_to(ROOT))]==sha(pp);state['inputs'][str(rp.relative_to(ROOT))]=sha(rp);state['inputs'][str(proof.relative_to(ROOT))]=sha(proof);state['parent_evidence_bindings']=bindings;square=arb(result['square_ball']);tau=Q(result['tau_upper_exact']);screens=[]
  for name,b in [('graded',Q(25,54684)),('sharpw_unrestricted_safe_ceiling',Q(28496,10**10)),('TB_sharp_safe_ceiling',Q(3793,10**9))]:
   margin=d-b;passes=margin>=0 and square<=ar(margin*margin);tau_passes=tau<=margin;assert not tau_passes or passes
   screens.append({'ceiling_id':name,'b':str(b),'strict_parent_distance_floor':str(d),'d_minus_b':str(margin),'tau_upper_exact':str(tau),'certified_square_below_margin_squared':passes,'tau_below_margin':tau_passes,'scope':'Conditional on independently accepted actual difference and the parent weak hypotheses; no inverse or existence claim'})
  state['screens']=screens
 state.update({'utc':now(),'status':'COMPLETE OWN exact density difference; independent pair-level reproduction OPEN','elapsed_seconds':time.monotonic()-start});save(output,state);log('DONE',result['norm_ball'],'tau',result['tau_upper_exact'],'sha',sha(output),'seconds',state['elapsed_seconds'])
if __name__=='__main__':main()
