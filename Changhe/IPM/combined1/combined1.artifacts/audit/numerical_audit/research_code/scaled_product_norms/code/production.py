"""Independent exact full residual norms, with compact group evidence."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import importlib.util,json,sys,time,argparse,os
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/scaled_product_norms';sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path(__file__).resolve().parent));import packed as P
Rat,T,V,ar=P.Rat,P.T,P.V,P.J.ar

def load(name,rel):
 spec=importlib.util.spec_from_file_location(name,ROOT/rel);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
M=load('production_own_positive_pole_moments','research/rational_pole_moments/code/moments.py')
H=load('production_own_fixture_tools','research/n3_synthetic_field_audit/code/check.py')
C=load('production_own_cartesian_jet','research/multiscale_generators/code/cartesian.py')
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def log(*args):print(now(),*args,flush=True)
def save(path,data):
 temp=path.with_suffix('.pending');temp.write_text(json.dumps(data,indent=2)+'\n');temp.replace(path)

def polyhash(poly):
 h=sha256();h.update(str(len(poly)).encode()+b'\n')
 for q in poly:h.update(str(q).encode()+b'\n')
 return h.hexdigest()

def fieldrecord(field):
 h=sha256();records=[]
 for key,A in sorted(field.items()):
  record={'key':list(key),'degree':A.P.degree(),'powers':list(A.powers),'numerator_sha256':polyhash(A.P)}
  h.update(json.dumps(record,sort_keys=True,separators=(',',':')).encode()+b'\n');records.append(record)
 return {'representation_sha256':h.hexdigest(),'component_count':len(field),'components':records}

def normgroups(D,d):
 groups={};pairs=0
 for a in range(d+1):
  bymode={}
  for (ell,kind,n),A in D[d,a].items():bymode.setdefault((kind,n),[]).append((ell,A))
  for (kind,n),rows in bymode.items():
   mult=Q(comb(d,a)*(2 if kind=='c' and n==0 else 1))
   for ell,A in rows:
    for ell2,Cc in rows:
     key=ell+ell2;groups[key]=groups.get(key,Rat())+mult*A*Cc;pairs+=1
  log('NORM_GROUP_COMPONENT',d,a,'ordered_pairs',pairs)
 return {key:A for key,A in groups.items() if A},pairs

def integrate_norm(groups,d,delta,ashift,tp,weighted,label,checkpoint):
 z=(3*V-Q(3,2))/Q(5,2);wp=Poly([1]);power=Poly([1]);coef=Q(1)
 for k in range(1,57):coef*=Q(4,5)-(k-1);coef/=k;power*=z;wp+=coef*power
 eps=abs(coef*(Q(4,5)-56)/57)*Q(3,5)**57/Q(2,5);S=arb(0);TW=arb(0);records=[];started=time.monotonic()
 for ell,A in sorted(groups.items()):
  Pv=A.numerator_v()*V**((1 if d%2==0 else 0)+tp);order=0
  while Pv and Pv[0]==0:Pv,rem=divmod(Pv,T);assert not rem;order+=1
  assert Pv;b=Q(d-3)+ell*delta/2+Q(ashift)+order;assert b>-1,(label,ell,'nonintegrable group',str(b))
  factors=[(a,k) for a,k in zip(P.J.SCALES,A.powers) if k]
  val,meta=M.integral(b,Pv,factors);assert val.is_finite(),(label,ell,'nonfinite integral');S+=val
  record={'ell_sum':ell,'endpoint_v_order':order,'b':str(b),'degree_v':Pv.degree(),'powers':list(A.powers),'numerator_v_sha256':polyhash(Pv),'integral_ball':val.str(100),'integral_accuracy_bits':val.rel_accuracy_bits(),'decomposition':meta}
  if weighted:
   wval,wmeta=M.integral(b,Pv*wp,factors);assert wval.is_finite(),(label,ell,'nonfinite weighted integral');TW+=wval;record.update({'weighted_integral_ball':wval.str(100),'weighted_integral_accuracy_bits':wval.rel_accuracy_bits(),'weighted_decomposition':wmeta})
  records.append(record);log('NORM_GROUP',label,ell,'b',str(b),'degree',Pv.degree(),'accuracy',val.rel_accuracy_bits(),'seconds',time.monotonic()-started)
  checkpoint({'status':'RUNNING integrals','label':label,'complete_group_count':len(records),'groups':records,'current_S':S.str(100),'current_T':TW.str(100) if weighted else None})
 assert S>0,(label,'S not certified positive',S)
 if weighted:
  pref=ar(Q(5,2))**ar(Q(4,5));lo=arb.pi()/2*pref*(TW-ar(eps)*S);hi=arb.pi()/2*pref*(TW+ar(eps)*S)
 else:lo=hi=arb.pi()/2*S
 assert lo>0 and hi>0,(label,'square not certified positive',lo,hi)
 return {'status':'COMPLETE OWN independent peer review OPEN','label':label,'square_lower_ball':lo.str(100),'square_upper_ball':hi.str(100),'norm_lower_ball':lo.sqrt().str(100),'norm_upper_ball':hi.sqrt().str(100),'S_ball':S.str(100),'T_ball':TW.str(100) if weighted else None,'series_absolute_error':str(eps) if weighted else '0','complete_group_count':len(records),'groups':records,'elapsed_seconds':time.monotonic()-started}

def points(D,Bg,raw,delta):
 records=[];minimum=10**9
 for xs,ys in [('3/7','-2/5'),('21','-9'),('3/10','70')]:
  jet=C.GeneratorJet(raw,xs,ys,order=6);vals={}
  for (d,a),field in sorted(D.items()):
   own=H.evaluate(field,d,delta,xs,ys);direct=H.direct_derivative(jet,a,d-a);assert own.overlaps(direct),(xs,ys,d,a,own,direct);minimum=min(minimum,own.rel_accuracy_bits(),direct.rel_accuracy_bits());assert minimum>120;vals[f'F_{a}_{d-a}']={'own':own.str(80),'Cartesian':direct.str(80),'overlap':True}
  for label,field in Bg.items():
   own=H.evaluate(field,1 if label in ['rho_x','rho_y'] else 0,delta,xs,ys);direct=jet.fields()[label];assert own.overlaps(direct),(label,xs,ys);minimum=min(minimum,own.rel_accuracy_bits(),direct.rel_accuracy_bits());assert minimum>120;vals[label]={'own':own.str(80),'Cartesian':direct.str(80),'overlap':True}
  records.append({'x':xs,'y':ys,'values':vals});log('POINT',xs,ys,'minimum_accuracy',minimum)
 return {'records':records,'value_count':sum(len(row['values']) for row in records),'minimum_accuracy_bits':minimum}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('candidate');parser.add_argument('--bits',type=int,default=2048);parser.add_argument('--norms',default='G0,rF,G1,P2');args=parser.parse_args();ctx.prec=args.bits;started=time.monotonic()
 path=B/f'verification/{args.candidate}_{args.bits}.json';assert not path.exists();fixturep=B/'verification/fixtures.json';fixture=json.loads(fixturep.read_text());inputs=dict(fixture['inputs'])
 for rel,h in inputs.items():assert sha(ROOT/rel)==h,rel
 for p in [fixturep,Path(__file__),ROOT/'research/rational_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/PROOF.md',ROOT/'research/multiscale_generators/code/cartesian.py']:inputs[str(p.relative_to(ROOT))]=sha(p)
 rawpaths=list((ROOT/'research/candidate_audits/data'/args.candidate).glob('*_exact.json'));assert len(rawpaths)==1;rawp=rawpaths[0];raw=json.loads(rawp.read_text());inputs[str(rawp.relative_to(ROOT))]=sha(rawp)
 shared=ROOT.parent/'c1-shared/candidate_snapshots'/args.candidate/rawp.name;assert shared.is_file() and sha(shared)==sha(rawp)
 state={'utc_start':now(),'candidate':args.candidate,'raw_sha256':sha(rawp),'precision_bits':args.bits,'inputs':inputs,'status':'RUNNING own exact residual assembly','norms':{},'no_spatial_quadrature':True,'foreign_code_executed':False,'source_copy_only':True,'frozen_peer_modules_imported_for_own_fixture_helpers':True,'peer_field_or_norm_routines_called':False};save(path,state)
 jet=P.J.ScaledRadial(raw);state['cl_exact']=str(jet.c);state['delta_exact']=str(jet.delta);log('JET_READY',args.candidate,'seconds',time.monotonic()-started)
 F,Bg=P.residual(jet,log);log('F_READY',len(F),'seconds',time.monotonic()-started)
 D=P.all_derivatives(F,jet.delta,2);log('DERIVATIVES_READY','seconds',time.monotonic()-started)
 state['fields']={f'D{d}_{a}':fieldrecord(field) for (d,a),field in sorted(D.items())};state['backgrounds']={label:fieldrecord(field) for label,field in Bg.items()};state['status']='RUNNING Cartesian point checks';state['elapsed_seconds']=time.monotonic()-started;save(path,state)
 state['point_checks']=points(D,Bg,raw,jet.delta);save(path,state)
 cache={}
 for label,d,ashift,tp,weighted in [('G0',0,Q(0),0,False),('rF',0,Q(-1),1,False),('G1',1,Q(0),0,False),('P2',2,Q(-4,5),0,True)]:
  if label not in args.norms.split(','):continue
  if d not in cache:cache[d]=normgroups(D,d)
  groups,pairs=cache[d]
  def checkpoint(part):
   state['norms'][label]=part;state['utc']=now();state['elapsed_seconds']=time.monotonic()-started;save(path,state)
  result=integrate_norm(groups,d,jet.delta,ashift,tp,weighted,label,checkpoint);result['ordered_pair_count']=pairs;checkpoint(result);log('NORM_DONE',label,result['norm_lower_ball'],result['norm_upper_ball'],'seconds',time.monotonic()-started)
 state.update({'status':'COMPLETE OWN exact norm balls; independent peer review OPEN','utc':now(),'elapsed_seconds':time.monotonic()-started});save(path,state);log('DONE',sha(path))
if __name__=='__main__':main()
