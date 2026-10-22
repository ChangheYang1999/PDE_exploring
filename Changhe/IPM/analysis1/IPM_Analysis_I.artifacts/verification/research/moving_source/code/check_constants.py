"""Exact source-shift implications and directed Fourier constants."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,sys,itertools,math
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/moving_source';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def qa(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def qi(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def ends(v):
 if isinstance(v,arb):
  assert v.is_finite()
  def cv(z):m,e=z.man_exp();return F(int(m))*F(2)**int(e)
  return cv(v.lower()),cv(v.upper())
 def cv(z):s,m,e,bc=z;assert bc>=0;return F((-1 if s else 1)*int(m))*F(2)**int(e)
 return tuple(map(cv,v._mpi_))
def rec(v):l,u=ends(v);return {'lower_exact':str(l),'upper_exact':str(u)}
counts=Counter();files={}
for dep in ['source_instance','n8_density_hessian','n8_velocity_hessian','source_local_estimate','canonical_strain_sign']:
 p=B/'research'/dep/'evidence/verdict.json';v=json.loads(p.read_text());assert v['status'].startswith('CONFIRMED')
 for rel,h in v['files'].items():assert sha(B/rel)==h,rel;counts['dependency_pins']+=1
 files[str(p.relative_to(B))]=sha(p)
sp=B/'research/modal_source/evidence/source_result.json';sa=B/'research/modal_source/evidence/output_audit.json';sv=json.loads(sp.read_text());audit=json.loads(sa.read_text());assert sha(sp)==audit['source_result_sha256']=='51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691'
assert audit['verdict']=='PASS'
for key,p in [('input_sha256','data_exact/modal_v2.json'),('scalar_input_sha256','research/modal_repair/evidence/independent_gauss_iv.json'),('source_sha256','research/modal_source/code/certify_source.py'),('moments_sha256','research/exponential_moments/code/moments.py'),('Cox_sha256','research/canonical_inverse/code/exact_audit.py')]:assert sha(B/p)==sv[key]==audit['verified_dependencies'][key];counts['source_integral_dependency_pins']+=1;files[p]=sha(B/p)
for p in [sp,sa,D/'PROOF.md',D/'evidence/proof_first.json',D/'evidence/source/lead_lemma.md',Path(__file__)]:files[str(p.relative_to(B))]=sha(p)
raw=json.loads((B/'data_exact/modal_v2.json').read_text());k=F(float.fromhex(raw['scalars_hex']['k']))
vals=sv['final_values']
def interval(name):v=vals[name];return F(v['lower_exact']),F(v['upper_exact'])
p_lo,p_hi=map(F,sv['final_root_endpoints_exact']);big_lo,big_hi=map(F,json.loads((B/'research/source_instance/evidence/verdict.json').read_text())['source_bracket']);assert big_lo<p_lo<=p_hi<big_hi;counts['exact_source_bracket_identification']+=1
mu_lo,mu_hi=interval('mu_minus_1');g_lo,g_hi=interval('g');a_lo,a_hi=interval('A_trial')
assert F('-2.2528046115e-8')-F('4.7e-19')<mu_lo<=mu_hi<F('-2.2528046115e-8')+F('4.7e-19');counts['source_scalar_rounding']+=1
assert F('29.7494906633335090153')-F('9.2e-20')<g_lo<=g_hi<F('29.7494906633335090153')+F('9.2e-20');counts['source_scalar_rounding']+=1
# A from a separate exact normalization/trace reconstruction; intersecting
# is unnecessary. Use this new enclosing interval directly.
Al,Au=2/k-1-mu_hi,2/k-1-mu_lo
assert F('10.150725243')<Al<=Au<F('10.150725244');counts['source_scalar_rounding']+=1
MV,Mr,R0,delta,kap=F(743,2500),F(5059,10000),F(99,2000),F(33,2000),F(1687,500)
mlow=Al-MV*R0;mpublic=F('10.1360138');assert mlow>mpublic>0 and 1/mpublic<F('.09866');counts['motion_bounds']+=2
margins={'mu_to_lower':F(1,100)+mu_lo,'mu_to_upper':F(1,100)-mu_hi,'A_to_lower':Al-10,'A_to_upper':F(51,5)-Au,'g_to_lower':g_lo-29,'g_to_upper':30-g_hi}
wants={'mu_to_lower':F('.0099999'),'mu_to_upper':F('.0099999'),'A_to_lower':F('.1507252'),'A_to_upper':F('.0492747'),'g_to_lower':F('.7494906'),'g_to_upper':F('.2505093')}
for n,m in margins.items():assert m>wants[n],n;counts['source_box_margin']+=1
bad_mu_margin=F('.01')-F('2.2528046e-8');actual_mu_margin_upper=F('.01')+mu_hi;assert actual_mu_margin_upper<bad_mu_margin;counts['inward_lead_margin_refuted']+=1
correct_margin=F('.01')-F('2.2528046115e-8')-F('4.7e-19');assert correct_margin<margins['mu_to_lower'];counts['corrected_mu_margin']+=1
eps=F('2.1886e-8');deflow=F('2.2528046e-8');lhs=eps*(1+MV/mpublic)
assert lhs<deflow-F('4.7e-19')<-mu_hi;counts['moving_source_obstruction']+=2
assert 29+Mr*R0<g_lo;assert big_lo-R0>F('8.55') and R0<(big_lo-R0)/2 and delta<1;counts['nonzero_gradient_and_scale']+=4
rows=[]
for m2,claim in [(F(0),F('.3181')),(F(1),F('.40709660')),(F(2),F('.56549268'))]:
 Ebound=delta*(F(417,10)*(MV+m2)+3*Mr);K=1/(kap-Ebound);assert Ebound<kap and K<claim,(m2,float(K),float(claim));counts['perturbed_local_coefficient']+=2
 rows.append({'m2':str(m2),'E_upper':str(Ebound),'K_upper':str(K),'K_decimal_ceiling':str(claim)})
threshold=(kap/delta-3*Mr)/F(417,10)-MV
assert F('4.5701177')<threshold<F('4.5701178');counts['m2_threshold']+=1
r=F(31,10);directed={};targets={'alpha':F('.194664'),'beta':F('.185605'),'gamma':F('.830050')}
for name,Q,pi in [('arb512',qa,arb.pi()),('iv180',qi,iv.pi)]:
 rr=Q(r);one=Q(1);alpha=1/(2*(pi*(rr-1))**Q(F(1,2)));beta=1/(2*(pi*(rr-1)*(rr-2))**Q(F(1,2)));gamma=1/(2*pi*(rr-1)*(rr-2)*(rr-3))**Q(F(1,2))
 x={'alpha':alpha,'beta':beta,'gamma':gamma,'k0':100/(2*pi),'k1':200/(2*pi)*(4/Q(delta)),'Cc_lo':3*Q(delta)/(pi**Q(F(1,2))*(Q(p_hi)-3*Q(delta))**3),'Cc_hi':3*Q(delta)/(pi**Q(F(1,2))*(Q(p_lo)-3*Q(delta))**3)}
 for n,c in targets.items():a,b=ends(x[n]);assert 0<a<=b<c;counts['directed_fourier_ceiling']+=1
 for row in rows:
  e=Q(delta)*(Q(F(417,10))*(Q(MV)+Q(F(row['m2'])))+3*Q(Mr));kk=1/(Q(kap)-e);assert ends(kk)[1]<F(row['K_decimal_ceiling']);counts['directed_local_coefficient']+=1
 for n,v in x.items():assert 0<ends(v)[0]<=ends(v)[1];counts['directed_finite_positive']+=1
 directed[name]={n:rec(v) for n,v in x.items()}
# Independent exact polar beta integrals: integrate u^j/(1+u)^r by
# splitting u^j=(1+u-1)^j, then antiderivatives at 0 and infinity.
for j in range(3):
 integral=sum((F((-1)**(j-l)*math.comb(j,l),1)/(r-l-1) for l in range(j+1)),F())
 product=F(math.factorial(j))
 for i in range(j+1):product/=r-1-i
 assert integral==product and integral>0;counts['exact_polar_integrals']+=1
# Parameter examples check the first-order denominator and both reciprocal
# error forms algebraically. They illustrate the proof, not its coverage.
for d in [F(0),R0/10,R0/2]:
 for e1 in [F(0),mpublic/2]:
  aa=Al;err=MV*d/2+e1
  for shift in [-err,err]:
   ab=aa+shift;assert ab>0
   assert abs(1/ab-1/aa)<=err/(aa*(aa-err));counts['exact_reciprocal_error_examples']+=1
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_MOVING_SOURCE_CONSTANTS_WITH_ONE_CORRECTION','counts':dict(counts),'source_bounds':{'p_lo':str(p_lo),'p_hi':str(p_hi),'mu_minus_1_lo':str(mu_lo),'mu_minus_1_hi':str(mu_hi),'g_lo':str(g_lo),'g_hi':str(g_hi),'A_lo':str(Al),'A_hi':str(Au)},'m_lower':str(mlow),'m_public_lower':str(mpublic),'margins':{n:str(v) for n,v in margins.items()},'refuted_lead_mu_margin':str(bad_mu_margin),'actual_mu_margin_upper':str(actual_mu_margin_upper),'corrected_mu_margin':str(correct_margin),'epsilon':str(eps),'epsilon_transformed_upper':str(lhs),'defect_lower':str(deflow),'m2_threshold':str(threshold),'local_rows':rows,'engines':directed,'files':files,'scope':'Source motion, conditional norm consequences, narrow moving-source obstruction and local K1 hypotheses. Source moments are frozen imported dependencies; no new full resummation and no global inverse.'}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['files','source_bounds','engines','margins']}))
