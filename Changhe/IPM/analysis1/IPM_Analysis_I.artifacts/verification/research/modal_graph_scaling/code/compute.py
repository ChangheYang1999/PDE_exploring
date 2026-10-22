from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
import sympy as s
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/modal_graph_scaling'
def check(q,t):
 if not q:raise ValueError(t)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def rat(q):return str(q.numerator)+'/'+str(q.denominator)
def hx(v):return F.from_float(float.fromhex(v))
a=json.loads((B/'data_exact/modal_v2.json').read_text());sc={k:hx(v) for k,v in a['scalars_hex'].items()};k=sc['k'];check(0<k<F(1,2),'k');check(sc['bi']>4 and sc['bo']>4-2*k,'inner and outer powers');check(a['degree']==7,'degree');knots=list(map(hx,a['arrays']['knots']['hex']));unique=sorted(set(knots));check(knots==sorted(knots),'ordered knots');check(knots[:8]==[knots[0]]*8 and knots[-8:]==[knots[-1]]*8,'eightfold ends');check(len(knots)==len(unique)+14,'simple interior');check(len(a['arrays']['S']['hex'])==260*(len(knots)-8),'spline layout')
exponents=[k-3-j*(1-k)-2*l for j,l in a['outer_jl']];check(exponents[0]==k-3 and len(set(exponents))==len(exponents)==10,'distinct powers');check(all(q<=2*k-4 for q in exponents[1:]),'remainder exponent');check(all(q<-2 for q in exponents),'strain convergence');check(exponents[0]+sc['bo']>0,'slope positivity')
scalar=json.loads((B/'research/modal_repair/evidence/audit_verdict.json').read_text());pins={}
for n,h in scalar['source_and_evidence_sha256'].items():check(sha(B/n)==h,'modal dependency');pins[n]=h
zlo,zhi=map(F,scalar['public_decimal_enclosures']['A00_correction']);A00=hx(a['arrays']['Aout']['hex'][0]);leading=[A00+zlo,A00+zhi];check(leading[0]*leading[1]>0,'leading coefficient away from zero')
# Fully symbolic local differential identities; no PDE substituted except its explicit source.
x,y,c=s.symbols('x y c');rho=s.Function('rho')(x,y);u=[s.Function('u1')(x,y),s.Function('u2')(x,y)];p=s.Function('psi')(x,y);coords=[x,y]
def E(q):return sum(z*s.diff(q,z) for z in coords)
def lap(q):return sum(s.diff(q,z,2) for z in coords)
V=[c*z+v for z,v in zip(coords,u)];K=rho-E(rho);UK=[v-E(v) for v in u];eps=sum(v*s.diff(rho,z) for v,z in zip(V,coords))-rho;LK=sum(v*s.diff(K,z) for v,z in zip(V,coords))-K+sum(v*s.diff(rho,z) for v,z in zip(UK,coords));identities={'linearized_spatial':s.expand(LK-eps+E(eps)), 'poisson_commutator':s.expand(-lap(2*p-E(p))-E(lap(p))), 'density_source_commutator':s.expand(s.diff(K,x)+E(s.diff(rho,x))), 'velocity_component1':s.expand(-s.diff(2*p-E(p),y)-(-s.diff(p,y)-E(-s.diff(p,y)))), 'velocity_component2':s.expand(s.diff(2*p-E(p),x)-(s.diff(p,x)-E(s.diff(p,x))))}
for name,v in identities.items():check(v==0,name)
# General Cartesian jet at the origin: E annihilates constant derivative remainder.
jet=[sum(s.Symbol(f'u{j}_{i}{l}')*x**i*y**l for i in range(4) for l in range(4-i)) for j in range(2)];center=0
for v in jet:
 for z in coords:check(s.diff(v-E(v),z).subs({x:0,y:0})==0,'center velocity jet');center+=1
for p in [D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__),B/'research/modal_repair/evidence/audit_verdict.json',B/'research/graph_center_norm/evidence/verdict.json',B/'research/center_obstruction/evidence/verdict.json']:
 pins[str(p.relative_to(B))]=sha(p)
check(json.loads((D/'evidence/proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md'),'proof first')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SYMBOLIC_SPATIAL_IDENTITIES_AND_EXACT_MODAL_INPUT_CONDITIONS','scalars':{n:rat(v) for n,v in sc.items()},'spline':{'degree':7,'modes':260,'total_knots':len(knots),'unique_knots':len(unique),'simple_spans':len(unique)-1},'outer_factor_exponents':[rat(v) for v in exponents],'A00_raw':rat(A00),'A00_normalized_enclosure':[rat(v) for v in leading],'symbolic_identities':list(identities),'center_derivative_identities':center,'radial_X_integrand_powers':{'center':1,'far':-2},'files':pins,'scope':'Exact modal trial regularity hypotheses and spatial identities, qualitative graph membership in PROOF. No zero image, numerical ratio, matrix transfer or IPM endpoint.'};p=D/'evidence/compute.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:out[n] for n in ('utc','status','spline','symbolic_identities','center_derivative_identities','A00_normalized_enclosure')}))
