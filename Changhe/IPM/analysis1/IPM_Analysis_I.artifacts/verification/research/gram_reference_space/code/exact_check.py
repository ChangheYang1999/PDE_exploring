"""Exact expanded polynomial and Gaussian-rational Laurent calculations; static AST inspection."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime,timezone
import ast,json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_reference_space'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def require(x,msg):
 if not x:raise ValueError(msg)
def conv(a,b):
 out={}
 for i,x in a.items():
  for j,y in b.items():out[i+j]=out.get(i+j,F(0))+x*y
 return {i:x for i,x in out.items() if x}
def deriv(a):return {i-1:i*x for i,x in a.items() if i}
def integrate(a,extra=0):return sum((x/F(i+extra+1) for i,x in a.items()),F(0))
chi={2*j:F((-1)**j*comb(6,j)) for j in range(7)};dchi=deriv(chi)
q0=conv(chi,chi);q1=conv(chi,dchi);q2=conv(dchi,dchi)
I0=integrate(q0,1);Ic=integrate(q1,2);I2=integrate(q2,3);It=15*I0+6*Ic+I2
require((I0,Ic,I2,It)==(F(1,26),-F(1,26),F(12,143),F(123,286)),'radial integrals')
# Gaussian rational pair (real, imaginary); no floating trigonometry.
def ca(x,y):return (x[0]+y[0],x[1]+y[1])
def cm(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def lc(a,b):
 out={}
 for i,x in a.items():
  for j,y in b.items():out[i+j]=ca(out.get(i+j,(F(0),F(0))),cm(x,y))
 return {i:x for i,x in out.items() if x!=(0,0)}
co={-1:(F(1,2),F(0)),1:(F(1,2),F(0))};si={-1:(F(0),F(1,2)),1:(F(0),-F(1,2))}
phi=lc(lc(co,co),si);dp={i:cm((F(0),F(i)),x) for i,x in phi.items()}
a0=lc(phi,phi)[0];a1=lc(dp,dp)[0]
require(a0==(F(1,16),0) and a1==(F(5,16),0),'Laurent angular constants')
require(phi=={-3:(0,F(1,8)),-1:(0,F(1,8)),1:(0,-F(1,8)),3:(0,-F(1,8))},'Phi identity')
# Exact nonnegative-square identity underlying the weighted upper estimate.
full={};squarebase=dict((i,3*x) for i,x in chi.items())
for i,x in dchi.items():squarebase[i+1]=squarebase.get(i+1,F(0))+x
square=conv(squarebase,squarebase)
for i,x in q0.items():full[i]=full.get(i,F(0))+15*x
for i,x in q1.items():full[i+1]=full.get(i+1,F(0))+6*x
for i,x in q2.items():full[i+2]=full.get(i+2,F(0))+x
rhs={i:6*x for i,x in q0.items()}
for i,x in square.items():rhs[i]=rhs.get(i,F(0))+x
require(full==rhs,'nonnegative square identity')
require(F(3,8)*It==F(369,2288) and F(1476,2288)<1,'norm upper constant with pi<4')
# Current source semantics. The finite matrices themselves are not run.
manifest=json.loads((D/'evidence/source_manifest.json').read_text());pins={}
for row in manifest['files']:
 p=B/row['snapshot'];require(sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],'snapshot '+str(p));pins[row['snapshot']]=row['sha256']
texts={name:(D/'sources'/('src__'+name+'.py')).read_text() for name in ['c2_gram','c2_fminus','lin_assembly']}
trees={name:ast.parse(text) for name,text in texts.items()}
def dump(x):return ast.dump(x,include_attributes=False)
checks=[]
def bind(name,snippet,label):
 nodes=ast.parse(snippet).body;require(len(nodes)==1,'one binding statement')
 target=dump(nodes[0]);hits=[n for n in ast.walk(trees[name]) if dump(n)==target]
 require(len(hits)==1,'AST '+label)
 checks.append({'source':name,'label':label,'line':hits[0].lineno,'expected_statement':snippet,'ast_sha256':hashlib.sha256(target.encode()).hexdigest()})
bind('c2_fminus','cols.append((0, ExpPolyBasis([(-np.inf, T.tmin, 0.0, [1.0]), (T.tmin, T.t0, 0.0, [1.0])]), "J"))','J_code two constant pieces')
bind('c2_gram','rad_pieces = [pieces for (m, pieces, lab) in cols] + [kp_pieces, tau_pieces, [(-np.inf, tmin, 0.0, [1.0])]]','J_inner last radial reference')
bind('c2_gram','rad_of = list(range(nF)) + [nF, nF + 1] + [nF + 1] * Mh + [nF + 2]','last reference radial index')
bind('c2_gram','acoef = [avec([(int(m), 1.0)]) for (m, pieces, lab) in cols] + [avec([(m, A0[m]) for m in range(Mt)]), avec([(m, Bm[m]) for m in range(min(Mt, len(Bm)))])] + [avec([(m, 1.0)]) for m in range(Mh)] + [avec([(0, 1.0)])]','last reference angular m0')
bind('c2_gram','Fd = np.array([ExpPolyBasis(pc).eval(tq, 1) for pc in rad_pieces])','piecewise derivative evaluation')
bind('c2_gram','Fs = 3 * F + Fd','radial logarithmic derivative')
bind('c2_gram','wX = wq * L ** 6 * np.exp(2 * tq) * (1 + uq ** 2) ** (3 - k - GAMMA_H1)','H1m radial weight')
bind('c2_gram','return AA0 * (R0 + R1)[np.ix_(rad_of, rad_of)] + AA1 * R0[np.ix_(rad_of, rad_of)], len(tq)','piecewise-gradient Gram assembly')
bind('c2_gram','jidx = [i for i, (m, pieces, lab) in enumerate(cols) if lab == "J"]','unconstrained J reference index')
bind('c2_gram','jin_idx = [ntot]','unconstrained inner reference index')
bind('c2_gram','p = G[idxs, :] @ h','projection uses raw references')
bind('c2_gram','return float(p @ Kp @ p / hGh)','reported squared correlation')
bind('lin_assembly','out = np.zeros_like(t)','evaluation zero outside pieces')
bind('lin_assembly','out[sel] += np.exp(alpha * sig) * pv','piecewise evaluation assembly')
# source endpoint-selection conditions and finite-energy interpretations are recorded explicitly.
cls=next(n for n in trees['lin_assembly'].body if isinstance(n,ast.ClassDef) and n.name=='ExpPolyBasis')
ev=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='eval')
require('np.isinf(a)' in ast.unparse(ev) and 'sel = t < b' in ast.unparse(ev) and 'sel = (t >= a) & (t < b)' in ast.unparse(ev),'half-open support')
# Read all nine JSONs as reported decimal numbers, not as certified spectra.
reports=[]
for ppc in [2,4,6]:
 for mode in ['H1m_NJ0','H1m_NJ1','L2y_NJ0']:
  p=D/'sources'/f'runs__c2__c2gram_M16_s16_p{ppc}_{mode}.json';a=json.loads(p.read_text(),parse_float=str)
  require(a['ppc']==ppc and a['nrows']==a['Ne']*a['Mout'] and a['mode']==mode.split('_')[0],'reported metadata')
  for key in ['J_code','J_inner']:require(F(a['Xnorm2'][key])>0,'finite broken norm scalar')
  sec=a['sections']['Fminus'];reports.append({'source':str(p.relative_to(B)),'ppc':ppc,'mode':a['mode'],'NJ':a['NJ'],'nrows':a['nrows'],'n_kept':sec['n_kept'],'Xnorm2_J_code':a['Xnorm2']['J_code'],'Xnorm2_J_inner':a['Xnorm2']['J_inner'],'sigma_min':sec['sigma_small5'][0],'sigma_max':sec['sigma_max'],'J_code_cos2_max':str(max(F(q['J_code']) for q in sec['smallest5_shares'])),'J_inner_cos2_max':str(max(F(q['J_inner']) for q in sec['smallest5_shares'])),'tails_cos2_max':str(max(F(q['tails']) for q in sec['smallest5_shares']))})
# A jump of radial coefficient1 is present at each relevant positive finite radius.
support={'J_code':{'pieces':[['-infinity','tmin','1'],['tmin','t0','1']],'jump_at':'t0','right_minus_left':'-1'},'J_inner':{'pieces':[['-infinity','tmin','1']],'jump_at':'tmin','right_minus_left':'-1'}}
output={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_POLYNOMIAL_LAURENT_AND_SELECTED_SOURCE_CHECKS','polynomial_chi':{str(i):str(x) for i,x in chi.items()},'radial_integrals':dict(I0=str(I0),cross=str(Ic),I2=str(I2),total=str(It)),'angular_integrals_over_pi':{'Phi_squared':'1/8','Phi_derivative_squared':'5/8'},'norm_constant_over_pi':'369/2288','using_pi_lt_4_constant':'369/572','AST_bindings':checks,'reference_support':support,'reported_floating_outputs':reports,'files':pins,'scope':'Exact analytic constants and current static source definitions only. Full spectrum, quadrature errors, historical execution and global inverse not verified.'}
for p in [D/'PROOF.md',D/'evidence/proof_first.json',D/'evidence/source_manifest.json',Path(__file__)]:output['files'][str(p.relative_to(B))]=sha(p)
out=D/'evidence/exact_check.json';require(not out.exists(),'immutable output');out.write_text(json.dumps(output,indent=2)+'\n');print(output['utc'],output['status'],len(checks),len(reports),sha(out))
