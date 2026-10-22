"""Independent exact endpoint/output audit and fresh symbolic identities.
Does not import either arithmetic engine or the producer.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from collections import Counter
import json,hashlib,sys,itertools
import sympy as S
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/sobolev_source_box';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for a in iter(lambda:f.read(1<<20),b''):h.update(a)
 return h.hexdigest()
def load(p):return json.loads(p.read_text())
v=load(E/'checks.json');p=load(D/'source/parameters.json');n=Counter()
assert v['status']=='PASS_TWO_INDEPENDENT_SOURCE_BOX_ENCLOSURES'
for f,h in v['files'].items():assert sha(B/f)==h,f;n['current_input_pins']+=1
assert set(v['engines'])=={'arb384','rational_machin_isqrt'}
keys=set('pi CU Csigma Cy CH c0 c1 b1 b2 b3 B1 B2 B3 e0 e1 e3 B3_density m2 d_bound mR_lower delta_lower box1_radius kappa source_multiplier E K1 exclusion_lhs exclusion_radius exclusion_e3 exclusion_gradient_lower'.split())
for engine,values in v['engines'].items():
 assert set(values)==keys and len(values)==30
 bounds={}
 for key,item in values.items():
  assert set(item)=={'lower_exact','upper_exact'}
  lo,hi=Q(item['lower_exact']),Q(item['upper_exact']);assert 0<lo<=hi;bounds[key]=(lo,hi);n['exact_endpoint_pairs']+=1
 for key,target in p['upper_claims'].items():assert bounds[key][1]<Q(target);n['strict_ceiling_audit']+=1
 for key,target in p['lower_claims'].items():assert bounds[key][0]>Q(target);n['strict_floor_audit']+=1
 assert bounds['e0'][1]<bounds['mR_lower'][0]
 assert bounds['E'][1]<bounds['kappa'][0]
 assert bounds['exclusion_lhs'][1]<Q(p['inputs']['defect_lower'])
 assert bounds['exclusion_gradient_lower'][0]>0;n['logical_implication_audit']+=4
 assert bounds['kappa'][0]<=Q(2134,625)<=bounds['kappa'][1]
 assert bounds['source_multiplier'][0]<=Q(2061,50)<=bounds['source_multiplier'][1];n['exact_kappa_and_multiplier']+=2
 # These square intervals must enclose the defining expressions using the
 # same saved pi ball and exact angular/radial normalization.
 s=Q(p['inputs']['s']);pl,pu=bounds['pi']
 for key,factors in [('CU',32*(s-1)),('Csigma',64*(s-1)*(s-2)),('Cy',8*(s-1)*(s-2)),('CH',4*(s-1)*(s-2)*(s-3))]:
  lo,hi=bounds[key];assert lo*lo<1/(factors*pu) and hi*hi>1/(factors*pl);n['fourier_constant_exact_square_audit']+=1
# Fresh symbolic reconstruction of the full vector tensor, divergence,
# reflection parity, source eigenvalue box and explicit cutoff coefficient.
x,y,s,A,mu,g,Mv,Mr,H,c0,c1,cs,m0,delta=S.symbols('x y s A mu g Mv Mr H c0 c1 cs m0 delta',real=True)
def eq(a,b=0):assert S.cancel(a-b)==0,(a,b);n['fresh_symbolic_identities']+=1
r2=x*x+y*y;velocity=[x*y/r2,-x*x/r2]
eq(x*velocity[0]+y*velocity[1])
eq(sum(t*t for t in velocity),x*x/r2)
eq(sum((a*b*v0)**2 for a,b,v0 in itertools.product([x,y],[x,y],velocity)),r2*x*x)
eq(velocity[0].subs(x,-x),-velocity[0]);eq(velocity[0].subs(y,-y),-velocity[0])
eq(velocity[1].subs(x,-x),velocity[1]);eq(velocity[1].subs(y,-y),velocity[1])
eq(S.I*y*velocity[1],-S.I*x*velocity[0])
eq(1/(s-3)-2/(s-2)+1/(s-1),2/((s-1)*(s-2)*(s-3)))
eq(1/(s-2)-1/(s-1),1/((s-1)*(s-2)))
eq(S.Rational(9,4)*2+s*(3+S.Rational(9,2)*2),12*s+S.Rational(9,2))
slow=1+A/2+(S.Rational(1,2)-s)*mu
fast=1+(S.Rational(1,2)-s)*A+mu/2+g
for av,muv,gv in itertools.product([10,S.Rational(51,5)],[S.Rational(99,100),S.Rational(101,100)],[29,30]):
 vals={A:av,mu:muv,g:gv,s:S.Rational(153,50)}
 assert slow.subs(vals)>=S.Rational(2134,625) and fast.subs(vals)>S.Rational(2134,625);n['source_box_vertices']+=1
# Machin tangent identity checked over exact rationals, without pi.
tan2=2*Q(1,5)/(1-Q(1,5)**2);tan4=2*tan2/(1-tan2*tan2)
assert tan2==Q(5,12) and tan4==Q(120,119)
assert (tan4-Q(1,239))/(1+tan4/239)==1;n['exact_machin_identity']=3
assert Q(p['inputs']['R0'])/3==Q(p['inputs']['delta_max']);n['strict_scale_refutation']=1

# Decode original binary64 knot strings through their integer mantissa and
# exponent, without the producer's float.fromhex conversion.
def hexq(text):
 sign=-1 if text.startswith('-') else 1
 text=text.lstrip('+-');head,exponent=text.split('p');assert head.startswith('0x')
 whole,frac=head[2:].split('.')
 return sign*Q(int(whole+frac,16),16**len(frac))*Q(2)**int(exponent)
modal=load(B/'data_exact/modal_v2.json');knots=[hexq(x) for x in modal['arrays']['knots']['hex']]
assert len(knots)==1573 and len(set(knots))==1559
assert knots[:8]==[knots[0]]*8 and knots[-8:]==[knots[-1]]*8
assert all(knots[j]<knots[j+1] for j in range(7,1565)) and knots[7]<1<3<knots[-8]
n['independent_exact_simple_knots']=1557
pv={k:Q(x) for k,x in p['inputs'].items()}
assert Q(8)<pv['p_lower']-pv['R']-pv['regularity_radius']
assert pv['p_upper']+pv['R']+pv['regularity_radius']<Q(9)
assert pv['R0']<pv['regularity_radius'] and pv['H_exclusion']<pv['H']
n['independent_neighbourhood_checks']=4
assert v['source_exact']['k']==str(hexq(modal['scalars_hex']['k']));n['independent_exact_k_decode']=1

out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_OUTPUT_AND_SYMBOLIC_AUDIT','checks_sha256':sha(E/'checks.json'),'source_sha256':sha(Path(__file__)),'counts':dict(n),'scope':'Exact stored endpoints, all printed inequalities, source geometry algebra and current input pins. Analytic theorem still requires the standalone proof and actual-model review.'}
(E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
