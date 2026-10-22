"""Packet187 static-source provenance and separate high-precision/numeric controls.
No fitting-lane module is imported or executed. No servers or external jobs.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time,platform,ast
import numpy as np
import scipy
import mpmath as mp
from r2_state_values import R2State
import modal_norm_power as iv
from check_full_modal_norm import normcell
start=time.monotonic();root=Path('verification/full_modal_norm_20261021T1730Z')
source=Path('verification/fixed_velocity_block_20261021T0056/source_snapshots/bq3core.py');text=source.read_text();ast.parse(text)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
required=['inner = np.linspace(0.0, 1.0, Nt + 1) ** grade','self.knots = np.concatenate([np.zeros(deg), inner, np.ones(deg)])','self.mk2 = np.minimum(kk // 2, self.Nb - 2)','self.pG = self.beta + 1','return 1 - (L ** 2 / (r ** 2 + L ** 2)) ** (1.0 / (2 * beta))','D = (1 - t) ** pw',"if self.rmap == 'r2' and (k % 2 == 1):",'rho = torch.sqrt(1 - w)','ck = torch.cos(k * phi)','cFk[:m] = 0; cGk[:m] = 0','G = G + facG * ck * (Bv @ cGk)']
assert all(s in text for s in required)
source_checks={'sha256':sha(source),'path':str(source),'method':'Manual static transcription in SOURCE_TRANSCRIPTION.md, fingerprinted by substrings and AST parse only; no execution or import. Ideal field removes runtime upper spline clamp.','required_source_expressions':required}
archives=[];quadratures=[]
for directory in sorted(p for p in root.iterdir()if p.is_dir()):
 inputs=[json.loads((directory/f'input{i}.json').read_text())for i in range(2)]
 states=[]
 assert all(inputs[0][key]==inputs[1][key]for key in ['basis_beta','L','degree','knots','knot_binary_little_endian_sha256'])
 for x in inputs:
  s=R2State(x['archive_path']);states.append(s)
  assert s.sha256==x['archive_sha256'] and sha(source)==x['source_core_sha256']
  assert s.meta['rmap']=='r2' and s.meta['scheme']=='mask' and int(s.meta['mreg'])==2
  assert Q.from_float(s.bb)==Q(x['basis_beta']) and Q.from_float(s.L)==Q(x['L']) and s.degree==x['degree']
  regenerated_knot_sha256=hashlib.sha256(s.knots.astype('<f8').tobytes()).hexdigest()
  assert regenerated_knot_sha256==x['knot_binary_little_endian_sha256']
  masks=[s.rawG.reshape(s.K,s.nb)[k,:k//2]for k in range(s.K)]
  assert all(np.all(m==0)for m in masks)
  assert (s.K-1)//2<=s.nb-2
  assert [str(Q.from_float(float(v)))for v in s.knots]==x['knots']
  archives.append({'archive_sha256':s.sha256,'K':s.K,'Nb':s.nb,'masked_slots':sum(len(m)for m in masks),'nonzero_masked_slots':0,'knot_sha256_recomputed':regenerated_knot_sha256,'verifier_numpy':np.__version__,'rmap':s.meta['rmap'],'basis_beta_exact':str(Q.from_float(s.bb)),'historical_knot_bitwise_identity':'NOT_ASSERTED','ideal_b_plus_one_minus_runtime_float':str(Q(x['basis_beta'])+1-Q.from_float(s.bb+1))})
 # Independent physical-radius evaluation and tensor quadrature. The 96-angle
 # trapezoid integrates products through degree78; radial Gauss is diagnostic.
 c=json.loads((directory/'certificate.json').read_text());b=states[0].bb;L=states[0].L
 q,w=np.polynomial.legendre.leggauss(32);edges=1-states[0].edges[::-1];z=np.concatenate([(a+d)/2+(d-a)*q/2 for a,d in zip(edges[:-1],edges[1:])]);weights=np.concatenate([(d-a)*w/2 for a,d in zip(edges[:-1],edges[1:])]);r=L*np.sqrt(np.expm1(-2*b*np.log(z)));phi=2*np.pi*(np.arange(96)+.317)/96
 vals=[]
 for s in states:
  radial=s.radial(r,'G')/z[:,None]**(b+1);k=np.arange(s.K)
  vals.append([radial@np.cos(k[:,None]*phi),radial@(-k[:,None]*np.sin(k[:,None]*phi))])
 vals.append([a-bb for a,bb in zip(*vals)])
 measured=[]
 for field in vals:measured.append([float(np.dot(weights*z,np.mean(f*f,axis=1))*2)for f in field])
 exact=[[float(Q(v[0])+Q(v[1]))/2 for v in row]for row in c['norm_squared_over_pi_b_L2']]
 errors=np.abs(np.asarray(measured)-exact)/np.maximum(np.abs(exact),1e-300);assert np.max(errors)<5e-10,(directory,errors)
 quadratures.append({'pair':directory.name,'method':'Own SciPy value reader,32 Gauss nodes per z-knot cell and96 full-circle angles. Reuses derived z-weight, so tests values/products and does not independently test Jacobian.','nodes':len(z)*96,'norm_squared_over_pi_b_L2':measured,'relative_differences_to_certificates':errors.tolist(),'max_relative_discrepancy':float(np.max(errors))})
mp.mp.dps=160
mpq=lambda v:mp.mpf(v.numerator)/v.denominator
high=[]
for m in range(5):
 for k in [1,2,5]:
  b=Q(61,20);a=Q(1,3);d=Q(7,10);family=[[Q(0)]*6 for _ in range(k+1)];family[k][m]=1
  got=normcell(family,a,d,b,5)
  integrand=lambda z:z**(2*m+1)*(1-z**mpq(2*b)if k%2 else 1)
  value=mp.quad(integrand,[mpq(a),mpq(d)]);closed=(mpq(d)**(2*m+2)-mpq(a)**(2*m+2))/(2*m+2)
  if k%2:closed-=(mpq(d)**mpq(2*m+2*b+2)-mpq(a)**mpq(2*m+2*b+2))/mpq(2*m+2*b+2)
  assert abs(value-closed)<mp.mpf('1e-150')
  for j,mult in [(0,1),(1,k*k)]:
   assert mpq(got[j][0])<=mult*value<=mpq(got[j][1])
  high.append({'mode':k,'monomial_degree':m,'b':str(b),'interval':[str(a),str(d)],'mpmath_dps':160,'I0':mp.nstr(value,145),'closed_vs_adaptive_absolute':mp.nstr(abs(value-closed),8),'inside_both_rational_intervals':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'verdict':'PASS mathematical reconstruction provenance and independent diagnostic consistency','environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__},'source_static_checks':source_checks,'archives':archives,'z_weighted_value_quadrature':quadratures,'interior_fractional_controls':high,'scope':'Manual static source transcription motivates ideal formulas and removes runtime upper spline clamp; substring checks alone are not semantic verification. Archives do not encode historical binary knot array; no cross-environment bitwise identity or floating evaluation error bound asserted. MP checks are diagnostics, exact enclosure proof is separate.','code_sha256':sha(__file__)}
dest=Path('research/187_full_modal_L2_certificates/verification/provenance_checks.json');dest.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],'PASS',out['elapsed_seconds'],'archives',len(archives),'interior_controls',len(high),'max_quad',max(x['max_relative_discrepancy']for x in quadratures))
