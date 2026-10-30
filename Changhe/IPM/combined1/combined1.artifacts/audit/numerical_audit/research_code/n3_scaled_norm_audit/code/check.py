"""Independent exact domain, recurrence, decomposition and norm calibration."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,floor
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,sys,time,argparse
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/n3_scaled_norm_audit'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def save(p,d):
 with Path(p).open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def common():
 prep=json.loads((B/'verification/PREPARE.json').read_text());assert sha(B/'PROOF.md')==prep['proof_sha256']
 out={str((B/'PROOF.md').relative_to(ROOT)):sha(B/'PROOF.md'),str((B/'verification/PREPARE.json').relative_to(ROOT)):sha(B/'verification/PREPARE.json'),str(Path(__file__).relative_to(ROOT)):sha(__file__)}
 for r in prep['sources']:
  p=ROOT/r['copy'];assert sha(p)==r['sha256'];out[r['copy']]=r['sha256']
 return out

def domain():
 start=time.monotonic();inputs=common();bad=F(-1,2)+F(1824676646553933,4076476460239181)-1
 assert bad==F(-8580076087609677,8152952920478362) and -2<bad<-1
 src=(B/'source/legqs_tests.py').read_text();assert 'Q(-1, 2) + Q(1824676646553933, 4076476460239181) - 1' in src
 rows=[]
 for a in [99,624,2499]:
  for i in range(15):
   for m in range(0,41,7):rows.append({'a':a,'i':i,'m':m,'b':str(bad+m),'final_exponent_admissible':bad+m>-1,'base_I0_admissible':False})
 assert len(rows)==270 and sum(not r['final_exponent_admissible'] for r in rows)==45
 src=(B/'source/legqs_norms.py').read_text();assert 'assert b > -1' in src and 'b0 = frac - 1 if frac > 0 else Q(0)' in src and 'm0 >= 0 and b0 > -1' in src
 rec={'utc':now(),'claim':'All three base classes of the original test A are admissible for the stated convergent-integral proof','verdict':'REFUTED','production_backend_verdict':'OPEN; production accumulator has a separate valid domain guard and normalization','b_bad':str(bad),'b_bad_plus_one':str(bad+1),'bad_base_rows':270,'requested_divergent_integrals':45,'all_test_rows':810,'rows':rows,'inputs':inputs,'elapsed_seconds':time.monotonic()-start}
 save(B/'verification/domain.json',rec);print('DOMAIN_DONE',rec['utc'],sha(B/'verification/domain.json'),flush=True)

def calibrate():
 start=time.monotonic();inputs=common();sys.path.insert(0,str(B/'source'));import legqs_norms as N;import legqs_integrals as LI
 spec=importlib.util.spec_from_file_location('n4_independent_pole_moments',ROOT/'research/rational_pole_moments/code/moments.py');M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
 for p in [ROOT/'research/rational_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/PROOF.md']:inputs[str(p.relative_to(ROOT))]=sha(p)
 ctx.prec=1536;ar=M.ar;V=Poly([0,1]);T=1-V;delta=F(1824676646553933,4076476460239181);tab=N.ScaleTables();checks=[]
 def overlap(label,a,b,minimum=300):
  assert a.is_finite() and b.is_finite() and a.overlaps(b),(label,a,b)
  assert a.rel_accuracy_bits()>minimum and b.rel_accuracy_bits()>minimum,(label,a.rel_accuracy_bits(),b.rel_accuracy_bits())
  checks.append({'label':label,'overlap':True,'left_bits':a.rel_accuracy_bits(),'right_bits':b.rel_accuracy_bits()})
 bases=[F(-37,100),F(0),delta-F(1,2)];assert all(-1<b<=0 for b in bases)
 for a in [99,624,2499,9999]:
  for b0 in bases:
   I0=tab.I0(F(a),b0,1536)
   for m in range(0,41,7):
    b=b0+m;other=M.pole_moments(Q(str(b)),Q(a),14)
    for i in range(15):
     R1,R2=tab.entry(F(a),b0,m,i);mine=ar(R1)+ar(R2)*I0
     overlap(f'table a{a} b0{b0} m{m} i{i}',mine,other[i])
     direct=LI.J(b,0,F(a),i,1536);overlap(f'direct a{a} b0{b0} m{m} i{i}',mine,direct)
 print('TABLES_DONE',len(checks),'seconds',time.monotonic()-start,flush=True)
 # These are the residue classes arising from ell delta and the norm shifts.
 classes=sorted({(F(ell)*delta+shift)-floor(F(ell)*delta+shift) for ell in range(17) for shift in [F(0),F(-1),F(-4,5)]})
 actual=[]
 for frac in classes:
  b0=frac-1 if frac else F(0);assert -1<b0<=0
  for a in [624,2499]:
   for m,i in [(0,1),(1,7),(13,23)]:
    R1,R2=tab.entry(F(a),b0,m,i);mine=ar(R1)+ar(R2)*tab.I0(F(a),b0,1536);ref=M.pole_moments(Q(str(b0+m)),Q(a),i)[i]
    overlap(f'actualclass a{a} b0{b0} m{m} i{i}',mine,ref)
  actual.append(str(b0))
 for m in [600,1800,2400]:
  b0=F(-37,100);a=F(624);i=23;R1,R2=tab.entry(a,b0,m,i);mine=ar(R1)+ar(R2)*tab.I0(a,b0,1536)
  ref=M.pole_moments(Q(str(b0+m)),Q(624),i)[i];overlap(f'large m{m}',mine,ref)
 # Full exact polynomial replays of N3 reciprocal partial fractions.
 pfrows=[]
 for aa,ms in [([99],[7]),([624],[36]),([2499],[19]),([99,624],[3,4]),([624,2499],[18,19]),([99,624,2499],[2,3,2]),([99,624,2499,9999],[1,2,1,2])]:
  D=Poly([1])
  for a,k in zip(aa,ms):D*=(1+Q(a)*V)**k
  pf=LI.partial_fractions(ms,[F(a) for a in aa]);replay=Poly([])
  for (r,k),c in pf.items():
   quo,rem=divmod(D,(1+Q(aa[r])*V)**k);assert not rem;replay+=Q(str(c))*quo
  assert replay==1
  pfrows.append({'a':aa,'M':ms,'complete_polynomial_identity':True,'terms':len(pf)})
 # Polynomial quotient and large denominator-order cases, plus a sum crossing classes.
 accrows=[];allacc=N.Accumulator(tab);allref=arb(0)
 fixtures=[(F(-2,3),Poly([3,-7,2]),[(99,3)]),(F(1,7),Poly([1,-3,2,4]),[(624,4),(2499,3)]),(delta-F(1,2),T**5,[(99,2),(624,3)]),(F(2),V**12+3*V-2,[(99,1),(624,1)]),(F(-37,100),T**8*(1+2*V),[(624,18),(2499,19)]),(F(4,5),Poly([1,2,3]),[(99,1),(624,2),(2499,1),(9999,2)]),(F(0),Poly([2,-1,3]),[])]
 for ix,(b,Pv,factors) in enumerate(fixtures):
  acc=N.Accumulator(tab);Ms=tuple((F(a),k) for a,k in factors);acc.add(Pv(T),b,Ms);mine=acc.value(1536);ref,meta=M.integral(Q(str(b)),Pv,[(Q(a),k) for a,k in factors]);overlap(f'polynomial integral{ix}',mine,ref,200)
  allacc.add(Pv(T),b,Ms);allref+=ref;accrows.append({'id':ix,'b':str(b),'numerator':[str(x) for x in Pv],'factors':[[a,k] for a,k in factors],'mine':mine.str(90),'reference':ref.str(90),'independent_decomposition':meta})
 overlap('all polynomial fixtures jointly accumulated',allacc.value(1536),allref,200)
 rejected=False
 try:N.Accumulator(tab).add(Poly([1]),F(-1),((F(624),1),))
 except AssertionError:rejected=True
 assert rejected
 print('RADIAL_DONE',len(checks),'seconds',time.monotonic()-start,flush=True)
 # Independently assemble every ordered angular pair and radial measure.
 def own_square(comps,d,ashift,tp,weighted):
  S=arb(0);TW=arb(0);records=[];Nterm=56;z=(3*T-Q(3,2))/Q(5,2);wp=Poly([1]);coef=Q(1);power=Poly([1])
  for k in range(1,Nterm+1):coef*=Q(4,5)-(k-1);coef/=k;power*=z;wp+=coef*power
  nextcoef=coef*(Q(4,5)-Nterm)/(Nterm+1);eps=abs(nextcoef)*Q(3,5)**(Nterm+1)/Q(2,5)
  for mult,D in comps:
   for (ell,kind,n,sc),p in D.items():
    for (ell2,kind2,n2,sc2),p2 in D.items():
     if kind!=kind2 or n!=n2:continue
     b=Q(d-3)+Q(str(delta))*(ell+ell2)/2+Q(str(ashift));Pv=p(T)*p2(T)
     if d%2==0:Pv*=T
     Pv*=T**tp;order=0
     while Pv and Pv[0]==0:Pv,rem=divmod(Pv,V);assert not rem;order+=1
     if not Pv:continue
     b+=order;assert b>-1
     factors={}
     for a,k in sc+sc2:factors[Q(str(a))]=factors.get(Q(str(a)),0)+k
     factors=list(factors.items());factor=Q(mult)*Q(2 if kind=='c' and n==0 else 1,2)
     val,meta=M.integral(b,Pv,factors);S+=ar(factor)*val
     if weighted:
      tw,meta2=M.integral(b,Pv*wp,factors);TW+=ar(factor)*tw
     records.append({'b':str(b),'origin_removed_v_power':order,'factor':str(factor),'mode':n,'kind':kind,'endpoint_integrable':True,'decomposition':meta})
  assert S>0
  if not weighted:return arb.pi()*S,arb.pi()*S,records
  pref=ar(Q(5,2))**ar(Q(4,5));return arb.pi()*pref*(TW-ar(eps)*S),arb.pi()*pref*(TW+ar(eps)*S),records
 def field(d):
  OM=1-V
  if d%2==0:return {(1,'s',1,((F(624),3),)):OM**2*(1+2*V),(2,'s',1,((F(99),2),)):OM**2*(2-V),(1,'c',3,((F(2499),1),)):V*OM**2}
  return {(1,'s',2,((F(624),3),)):V*OM**2*(1+2*V),(2,'s',2,((F(99),2),)):V*OM**2*(2-V),(1,'c',0,((F(2499),1),)):OM**2}
 normrows=[]
 for label,d,ashift,tp,weighted in [('G0',0,F(0),0,False),('rF',0,F(-1),1,False),('G1',1,F(0),0,False),('P2',2,F(-4,5),0,True)]:
  D=field(d);comp=[(1,D),(2,{k:p*Q(2,7) for k,p in D.items()})];series=[(F(3),F(4,5))] if weighted else []
  peer=N.normsq_t(comp,d,delta,ashift,tp,series,56,tab,1536);assert peer['status']=='FINITE';lo,hi,records=own_square(comp,d,ashift,tp,weighted)
  overlap(f'{label} lower square',peer['lo'],lo,200);overlap(f'{label} upper square',peer['hi'],hi,200)
  normrows.append({'label':label,'degree':d,'a_shift':str(ashift),'t_power':tp,'series':weighted,'peer_square_lo':peer['lo'].str(90),'peer_square_hi':peer['hi'].str(90),'own_square_lo':lo.str(90),'own_square_hi':hi.str(90),'ordered_pairs':records})
 rec={'utc':now(),'status':'PASS independent scaled primitive and small-field norm calibration; actual candidate norms OPEN','precision_bits':1536,'inputs':inputs,'checks':checks,'comparison_count':len(checks),'minimum_relative_accuracy_bits':min(min(x['left_bits'],x['right_bits']) for x in checks),'admissible_base_classes':list(map(str,bases)),'production_norm_classes':actual,'exact_partial_fraction_replays':pfrows,'polynomial_integrals':accrows,'invalid_exponent_rejected':rejected,'small_field_norms':normrows,'elapsed_seconds':time.monotonic()-start,'foreign_code_executed':False,'frozen_peer_code_executed':True}
 save(B/'verification/calibration.json',rec);print('CALIBRATION_DONE',rec['utc'],len(checks),rec['minimum_relative_accuracy_bits'],rec['elapsed_seconds'],sha(B/'verification/calibration.json'),flush=True)

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['domain','calibrate']);args=parser.parse_args()
 domain() if args.mode=='domain' else calibrate()
