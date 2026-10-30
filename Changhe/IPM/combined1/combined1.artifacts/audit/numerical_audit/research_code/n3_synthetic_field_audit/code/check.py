"""Complete exact synthetic fields through D2F and independent norm groups."""
from pathlib import Path
from fractions import Fraction as Fr
from math import comb
from datetime import datetime,timezone
from hashlib import sha256
import ast,importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,acb,ctx
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/n3_synthetic_field_audit';SRC=ROOT/'research/n3_scaled_norm_audit/source'
sys.set_int_max_str_digits(0);sys.path.insert(0,str(SRC));import legqs_norms as N;import legqs_e2norms as LS
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def load(name,rel):
 spec=importlib.util.spec_from_file_location(name,ROOT/rel);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
J=load('own_joint_exact','research/joint_scaled_factored_weak/code/fields_joint.py');C=load('own_cart_jet','research/multiscale_generators/code/cartesian.py');M=load('own_pole_moments','research/rational_pole_moments/code/moments.py')
Rat=J.Rat;ar=J.ar;T=J.T;V=J.V;ctx.prec=1536

def add(out,key,A):
 ell,kind,n=key
 if n<0:n=-n;A=-A if kind=='s' else A
 if not A or kind=='s' and n==0:return
 key=(ell,kind,n);out[key]=out.get(key,Rat())+A
 if not out[key]:del out[key]
def combine(*rows):
 out={}
 for factor,field in rows:
  for key,A in field.items():add(out,key,A*Q(factor))
 return out
def products(k,m,l,n):
 if k==l=='c':return [('c',m+n,Q(1,2)),('c',m-n,Q(1,2))]
 if k==l=='s':return [('c',m-n,Q(1,2)),('c',m+n,Q(-1,2))]
 if k=='s':return [('s',m+n,Q(1,2)),('s',m-n,Q(1,2))]
 return [('s',m+n,Q(1,2)),('s',m-n,Q(-1,2))]
def multiply(A,da,Bb,db,d):
 assert da+db==d+1;out={};extra=Rat(T) if da%2==db%2==0 else Rat(1)
 for (e,k,m),a in A.items():
  for (f,l,n),b in Bb.items():
   for kind,mode,c in products(k,m,l,n):add(out,(e+f,kind,mode),a*b*extra*c)
 return out
def packed_chi(jet,a,b):
 d=a+b;assert 3<=d<=6
 return {(j+1,'s' if b%2 else 'c',n):A.divide_t((d+1)//2) for (j,n),A in jet.deriv(a,b).items()}
def own_fields(jet):
 cache={}
 def field(label,a,b):
  key=label,a,b
  if key not in cache:
   if label=='rho':value=combine((-1,packed_chi(jet,a+2,b+1)),(-1,packed_chi(jet,a,b+3)))
   elif label=='u1':value=combine((-1,packed_chi(jet,a+1,b+2)))
   else:assert label=='u2';value=packed_chi(jet,a+2,b+1)
   cache[key]=value
  return cache[key]
 X={(0,'c',1):Rat(1)};Y={(0,'s',1):Rat(1)};D={};c=jet.c
 for d in range(3):
  for a in range(d+1):
   b=d-a;terms=[(c,multiply(X,0,field('rho',a+1,b),d+1,d)),(c,multiply(Y,0,field('rho',a,b+1),d+1,d)),(c*d-1,field('rho',a,b))]
   for i in range(a+1):
    for j in range(b+1):
     fac=Q(comb(a,i)*comb(b,j));db=i+j;dc=d-db+1
     terms.extend([(fac,multiply(field('u1',i,j),db,field('rho',a-i+1,b-j),dc,d)),(fac,multiply(field('u2',i,j),db,field('rho',a-i,b-j+1),dc,d))])
   D[d,a]=combine(*terms)
 return D,{label:field(base,a,b) for label,base,a,b in [('rho','rho',0,0),('u1','u1',0,0),('u2','u2',0,0),('rho_x','rho',1,0),('rho_y','rho',0,1)]}
def peer_field(D):
 out={}
 for (ell,kind,n,sc),p in D.items():
  powers=[0]*len(J.SCALES)
  for a,k in sc:powers[J.SCALES.index(Q(str(a)))]=k
  add(out,(ell,kind,n),Rat(p,tuple(powers)))
 return out
def equal(label,one,two,records):
 assert set(one)==set(two),(label,'key difference',set(one)^set(two))
 for key,A in one.items():assert A==two[key],(label,key)
 records.append({'label':label,'exact_coefficient_count':len(one),'full_positive_denominator_identity':True,'own_field_sha256':J.field_hash(one),'peer_field_sha256':J.field_hash(two)})
def evaluate(D,d,delta,xs,ys):
 x,y=ar(Q(xs)),ar(Q(ys));r2=x*x+y*y;r=r2.sqrt();v=1/(1+r2);t=1-v;z=acb(x/r,y/r);value=arb(0)
 for (ell,kind,n),A in D.items():value+=v**ar(ell*delta/2)*A.evaluate(t,v)*((z**n).real if kind=='c' else (z**n).imag)
 return (r if d%2==0 else arb(1))*v**(d//2)*value

def direct_derivative(jet,a,b):
 rho=lambda i,j:-jet.chi(i+2,j+1)-jet.chi(i,j+3)
 u1=lambda i,j:-jet.chi(i+1,j+2)
 u2=lambda i,j:jet.chi(i+2,j+1)
 d=a+b;value=ar(jet.c)*(jet.x*rho(a+1,b)+jet.y*rho(a,b+1))+(ar(jet.c)*d-1)*rho(a,b)
 for i in range(a+1):
  for j in range(b+1):value+=comb(a,i)*comb(b,j)*(u1(i,j)*rho(a-i+1,b-j)+u2(i,j)*rho(a-i,b-j+1))
 return value

def independent_norm(D,d,delta,ashift,tp,weighted):
 groups={};pairs=0
 for a in range(d+1):
  field=D[d,a];mult=Q(comb(d,a))
  for (ell,kind,n),A in field.items():
   for (ell2,kind2,n2),Bv in field.items():
    if kind2!=kind or n2!=n:continue
    k=ell+ell2;groups[k]=groups.get(k,Rat())+mult*(2 if kind=='c' and n==0 else 1)*A*Bv;pairs+=1
 z=(3*V-Q(3,2))/Q(5,2);wp=Poly([1]);power=Poly([1]);coef=Q(1)
 for k in range(1,57):coef*=Q(4,5)-(k-1);coef/=k;power*=z;wp+=coef*power
 eps=abs(coef*(Q(4,5)-56)/57)*Q(3,5)**57/Q(2,5);S=arb(0);TW=arb(0);records=[]
 for ell,A in sorted(groups.items()):
  if not A:continue
  Pv=A.numerator_v()*V**((1 if d%2==0 else 0)+tp);order=0
  while Pv and Pv[0]==0:Pv,rem=divmod(Pv,T);assert not rem;order+=1
  assert Pv;exponent=Q(d-3)+ell*delta/2+Q(ashift)+order;assert exponent>-1
  factors=[(a,k) for a,k in zip(J.SCALES,A.powers) if k];val,meta=M.integral(exponent,Pv,factors);assert val.is_finite() and val.rel_accuracy_bits()>150;S+=val
  rec={'ell_sum':ell,'endpoint_v_order':order,'b':str(exponent),'integral':val.str(90),'decomposition':meta}
  if weighted:
   wval,wmeta=M.integral(exponent,Pv*wp,factors);assert wval.is_finite() and wval.rel_accuracy_bits()>150;TW+=wval;rec.update({'weighted_integral':wval.str(90),'weighted_decomposition':wmeta})
  records.append(rec)
 assert S>0
 if weighted:
  pref=ar(Q(5,2))**ar(Q(4,5));lo=arb.pi()/2*pref*(TW-ar(eps)*S);hi=arb.pi()/2*pref*(TW+ar(eps)*S)
 else:lo=hi=arb.pi()/2*S
 assert hi>0 and lo>0
 return lo,hi,{'ordered_pair_count':pairs,'complete_group_count':len(records),'groups':records,'series_absolute_error':str(eps) if weighted else '0'}

def main():
 start=time.monotonic();out=B/'verification/result.json';assert not out.exists();inputs={};checks=[]
 for p in [B/'PROOF.md',B/'data/synthetic.json',Path(__file__),ROOT/'research/n3_scaled_norm_audit/PROOF.md',ROOT/'research/n3_scaled_norm_audit/verification/calibration.json',ROOT/'research/joint_scaled_factored_weak/PROOF.md',ROOT/'research/joint_scaled_factored_weak/code/fields_joint.py',ROOT/'research/multiscale_generators/PROOF.md',ROOT/'research/multiscale_generators/code/cartesian.py',ROOT/'research/rational_pole_moments/PROOF.md',ROOT/'research/rational_pole_moments/code/moments.py']:inputs[str(p.relative_to(ROOT))]=sha(p)
 calibration=json.loads((ROOT/'research/n3_scaled_norm_audit/verification/calibration.json').read_text())
 for rel,h in calibration['inputs'].items():assert sha(ROOT/rel)==h;inputs[rel]=h
 rawp=B/'data/synthetic.json';raw=json.loads(rawp.read_text())
 source_tree=ast.parse((SRC/'legqs_tests.py').read_text())
 generator_lists=[ast.literal_eval(n.value) for n in ast.walk(source_tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='gens' for t in n.targets)]
 assert sum(raw['generators']==g for g in generator_lists)==1
 c,A,As,rawsha,meta=LS.load_reference_legqs(rawp);delta=Q(str(1-1/c));assert c==Fr(4076476460239181,2251799813685248)
 peerD,peerB=N.residual_t(A,As,c,2,log=lambda *s:print(*s,flush=True));print('N3_FIELDS_DONE',time.monotonic()-start,flush=True)
 jet=J.ScaledRadial(raw);ownD,ownB=own_fields(jet);print('OWN_FIELDS_DONE',time.monotonic()-start,flush=True)
 for k,field in ownD.items():equal('Fderivative'+str(k),field,peer_field(peerD[k]),checks)
 for label,field in ownB.items():equal(label,field,peer_field(peerB[label]),checks)
 points=[];minimum=100000
 for xs,ys in [('3/7','-2/5'),('21','-9'),('3/10','70'),('400','3')]:
  car=C.GeneratorJet(raw,xs,ys,order=6);vals={}
  for (d,a),field in ownD.items():
   own=evaluate(field,d,delta,xs,ys);ref=direct_derivative(car,a,d-a);assert own.overlaps(ref);minimum=min(minimum,own.rel_accuracy_bits(),ref.rel_accuracy_bits());assert minimum>150;vals[f'F_{a}_{d-a}']={'own':own.str(90),'Cartesian':ref.str(90),'overlap':True}
  for label,field in ownB.items():
   own=evaluate(field,1 if label in ['rho_x','rho_y'] else 0,delta,xs,ys);ref=car.fields()[label];assert own.overlaps(ref);minimum=min(minimum,own.rel_accuracy_bits(),ref.rel_accuracy_bits());assert minimum>150;vals[label]={'own':own.str(90),'Cartesian':ref.str(90),'overlap':True}
  points.append({'x':xs,'y':ys,'values':vals})
 print('IDENTITIES_POINTS_DONE',sum(r['exact_coefficient_count'] for r in checks),minimum,time.monotonic()-start,flush=True)
 norms=[];tables=N.ScaleTables()
 for label,d,ashift,tp,weighted in [('G0',0,Q(0),0,False),('rF',0,Q(-1),1,False),('G1',1,Q(0),0,False),('P2',2,Q(-4,5),0,True)]:
  ser=[(Fr(3),Fr(4,5))] if weighted else [];peer=N.norm_t(peerD,d,Fr(str(delta)),Fr(str(ashift)),tp,ser,56,label,tables,1536);assert peer['status']=='FINITE';lo,hi,details=independent_norm(ownD,d,delta,ashift,tp,weighted)
  assert lo.overlaps(arb(peer['square_lo_ball'])) and hi.overlaps(arb(peer['square_hi_ball'])),(label,lo,hi,peer)
  assert lo.sqrt().overlaps(arb(peer['norm_lower_ball'])) and hi.sqrt().overlaps(arb(peer['norm_upper_ball']))
  norms.append({'label':label,'own_lower_square':lo.str(90),'own_upper_square':hi.str(90),'own_lower_norm':lo.sqrt().str(90),'own_upper_norm':hi.sqrt().str(90),'peer':peer,'all_containing_bound_balls_overlap':True,'independent_integration':details})
  print('NORM',label,lo.sqrt().str(35),hi.sqrt().str(35),'seconds',time.monotonic()-start,flush=True)
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED complete exact six-generator field identities through D2F and four whole-plane fixture norms; actual016/017 norms OPEN','raw_sha256':rawsha,'precision_bits':1536,'exact_field_checks':checks,'exact_coefficient_count':sum(r['exact_coefficient_count'] for r in checks),'point_checks':points,'point_value_count':sum(len(p['values']) for p in points),'minimum_point_accuracy_bits':minimum,'norms':norms,'inputs':inputs,'foreign_code_executed':False,'frozen_peer_code_executed':True,'elapsed_seconds':time.monotonic()-start}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('DONE',result['utc'],sha(out),'seconds',result['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
