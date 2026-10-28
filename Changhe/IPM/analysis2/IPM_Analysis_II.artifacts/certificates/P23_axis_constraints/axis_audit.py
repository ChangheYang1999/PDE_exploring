"""Exact-source, two-method audit of the vertical-axis restrictions.
One small single-threaded computation; no producer evaluator is imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from math import comb
import sys,json,hashlib,time
from flint import arb,ctx
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'source_audit'))
import recover_state as rec
sys.path.insert(0,str(BASE/'11_residual_norms/verification'))
from audit_norms import direct_chi
ctx.prec=768
AQ=lambda x:arb(Q(x).numerator)/Q(x).denominator

def add(P,key,value):
 if value:
  P[key]=P.get(key,Q(0))+value
  if not P[key]:del P[key]

def build_axis(A,c):
 # Phi(y)=chi(0,y); Ax(y)=partial_x^2 chi(0,y).
 # Independently derive the x^2 coefficient of H_(2m)(x,y)(x^2+y^2)^(k-m).
 # It is (-1)^m(k-2m^2)y^(2k-2), giving the two Ax terms below.
 pj={j:(3+1/c-j*(1-1/c))/2 for j,m,k in A}
 # Explicit key(j,p,b) denotes y^p(1+y^2)^b.
 Phi={};Ax={}
 for (j,m,k),v in A.items():
  sign=(-1)**m;b=pj[j]-k
  add(Phi,(j,2*k,b),sign*v)
  add(Ax,(j,2*k-2,b),2*sign*v*(k-2*m*m))
  add(Ax,(j,2*k,b-1),2*sign*v*b)
 assert all(p>=0 for j,p,b in Phi) and all(p>=0 for j,p,b in Ax)
 def diff(P):
  out={}
  for (j,p,b),v in P.items():
   if p:add(out,(j,p-1,b),p*v)
   add(out,(j,p+1,b-1),2*b*v)
  return out
 DP=[Phi];DA=[Ax]
 for n in range(5):DP.append(diff(DP[-1]))
 for n in range(3):DA.append(diff(DA[-1]))
 def coeff(P,n):
  # Exact ordinary power-series coefficient of y^n at zero.
  out=Q(0)
  for (j,p,b),v in P.items():
   if n>=p and (n-p)%2==0:out+=v*rec.choose(b,(n-p)//2)
  return out
 a0=-24*coeff(Phi,4)-2*coeff(Ax,2)
 strain=2*coeff(Ax,2);b=-120*coeff(Phi,6)-4*coeff(Ax,4);d=4*coeff(Ax,4)
 assert strain==1-c and a0>0
 return DP,DA,{'a0':a0,'strain':strain,'q_cubic':b,'v_cubic':d,'F_cubic':2*b+a0*d}

def ev(P,y):
 S=1+y*y
 yp={p:y**p for j,p,b in P}
 bp={b:S**AQ(b) for j,p,b in P}
 return sum((AQ(v)*yp[p]*bp[b] for (j,p,b),v in P.items()),arb(0))

def fields(q,q1,q2,v,v1,v2,c,y):
 V=AQ(c)*y+v;V1=AQ(c)+v1
 f=V*q1-q;f1=V1*q1+V*q2-q1
 m11=2*AQ(c)+1-v1+q1;m22=2*AQ(c)+1+v1
 out={'q':q,'q_prime':q1,'q_second':q2,'v':v,'v_prime':v1,'v_second':v2,'V':V,'V_prime':V1,'F':f,'F_prime':f1,'M11':m11,'M22':m22}
 if q1>0:
  Kf=(q+f)*q2/q1**2-f1/q1
  assert Kf.overlaps(1-V1)
  out['K_with_residual']=Kf;out['K_without_residual']=q*q2/q1**2
 return out

def run():
 start=time.monotonic()
 rec.HERE=HERE
 rec.COPY=Path('case4/IPM_case4.artifacts')
 c,C,original=rec.read_state(131)
 assert original['canonical_serialization_sha256']=='4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01'
 cases=[('state131',dict(zip(rec.CANON,C)),original['source_json_sha256'],original['canonical_serialization_sha256'],None)]
 for name in ['nb_stableA2_exact','nb_stableA3_exact']:
  p=BASE/'19_nb_candidates/verification'/(name+'.audit.json')
  data=json.loads(p.read_text())
  assert Q(data['cl'])==c
  A={tuple(k):Q(v) for k,v in zip(data['canonical_order'],data['canonical_coefficients'])}
  # Bind the fresh exact input, not just the previous point output.
  original_path=Path('numerics/data')/(name+'.json')
  source_hash=hashlib.sha256(original_path.read_bytes()).hexdigest()
  assert source_hash==hashlib.sha256((BASE/'19_nb_candidates/verification'/(name+'.input.json')).read_bytes()).hexdigest()
  saved=json.loads((BASE/'19_nb_candidates/verification'/(name+'.points.json')).read_text())
  assert saved['canonical_sha256']==data['canonical_sha256']
  cases.append((name,A,source_hash,data['canonical_sha256'],saved))
 kappa=Q(19,5);epsilon=c+2-kappa;a=1-epsilon;s=Q(3,2**31);r0=Q(5,2**32)
 assert 0<epsilon<1 and 0<a/c<1
 out={'utc_start':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','precision_bits':ctx.prec,'cl':str(c),'kappa':str(kappa),'epsilon':str(epsilon),'concavity_power':str(a),'epsilon_ball':AQ(epsilon).str(65),'concavity_power_ball':AQ(a).str(65),'s':str(s),'r0':str(r0),'candidates':[]}
 for name,A,sourcehash,canonical,saved in cases:
  DP,DA,jets=build_axis(A,c)
  rows=[]
  for ys in ['1/10','1','2']:
   y=AQ(ys);ch=direct_chi(A,c,arb(0),y)
   one=fields(-ch[2,1]-ch[0,3],-ch[2,2]-ch[0,4],-ch[2,3]-ch[0,5],ch[2,1],ch[2,2],ch[2,3],c,y)
   ax=[ev(P,y) for P in DA]
   two=fields(-ax[1]-ev(DP[3],y),-ax[2]-ev(DP[4],y),-ax[3]-ev(DP[5],y),ax[1],ax[2],ax[3],c,y)
   assert all(v.is_finite() and two[k].is_finite() and v.overlaps(two[k]) for k,v in one.items()),(name,ys)
   if saved:
    prev=next(z for z in saved['points'] if z['point']==['0',ys])
    for newkey,oldkey in [('q','rho'),('q_prime','rho_y'),('v','u2'),('F','F')]:assert one[newkey].overlaps(arb(prev['polar'][oldkey]))
    lm=(one['M11']+one['M22']-abs(one['M11']-one['M22']))/2
    assert lm.overlaps(arb(prev['polar']['M_lambda_min']))
   row={'point':['0',ys],'independent_axis_and_cartesian_agree':True,'cartesian':{k:v.str(65) for k,v in one.items()},'axis_series':{k:v.str(65) for k,v in two.items()},'violates_axial_lower_matrix':one['M22']<AQ(kappa),'violates_integrated_velocity_necessary_condition':one['V']<AQ(a)*y}
   defect=AQ(kappa)-one['M22']
   if defect>0:
    dist=defect*AQ(s).sqrt()/4;ratio=dist/AQ(r0)
    row['matrix_defect']=defect.str(65);row['N_distance_lower_witness']=dist.str(65);row['distance_over_theorem_radius_witness']=ratio.str(65)
    if ys=='1':
     n=12000 if name=='nb_stableA2_exact' else 5000
     assert ratio>n
     row['certified_distance_over_radius_lower']=n
   rows.append(row)
   print(name,ys,'M22',one['M22'].str(18),'V',one['V'].str(18),'Kf',one['K_with_residual'].str(18),flush=True)
  out['candidates'].append({'name':name,'source_json_sha256':sourcehash,'canonical_sha256':canonical,'exact_origin_jets':{k:str(v) for k,v in jets.items()},'origin_jet_balls':{k:AQ(v).str(65) for k,v in jets.items()},'points':rows})
 deps=[HERE.parent/'PROOF.md',BASE/'source_audit/recover_state.py',BASE/'11_residual_norms/verification/audit_norms.py',BASE/'11_residual_norms/verification/compact_norms.py',BASE/'02_energy/verification/compact_matrix.py',BASE/'18_fractional_constants/PROOF.md',BASE/'19_nb_candidates/PROOF.md']
 for name in ['nb_stableA2_exact','nb_stableA3_exact']:
  deps +=[BASE/'19_nb_candidates/verification'/(name+suffix) for suffix in ['.audit.json','.points.json']]
 out['dependency_hashes']={str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}
 out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 out['utc_complete']=datetime.now(timezone.utc).isoformat();out['seconds']=time.monotonic()-start
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',out['seconds'],flush=True)
if __name__=='__main__':run()
