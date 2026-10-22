"""Read-only AST audit, exact polynomial identities and Arb fixture."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import ast,hashlib,json,sys
import sympy as s
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/fd_repair_scope'
def check(v,t):
 if not v:raise ValueError(t)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rr(q):q=F(q);return str(q.numerator)+'/'+str(q.denominator)
def aq(x):
 check(x.rad()==0,'exact endpoint');m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def enc(a):return [rr(aq(a.lower())),rr(aq(a.upper()))]
source=(D/'evidence/c2_gram2_source.py.txt').read_text();tree=ast.parse(source);main=next(a for a in tree.body if isinstance(a,ast.FunctionDef) and a.name=='main');wr=next(a for a in main.body if isinstance(a,ast.FunctionDef) and a.name=='weighted_rows');con=next(a for a in main.body if isinstance(a,ast.FunctionDef) and a.name=='constraints')
def dump(x):return ast.dump(x,include_attributes=False)
def expr(text):return dump(ast.parse(text,mode='eval').body)
assignments={}
for a in ast.walk(wr):
 if isinstance(a,ast.Assign):
  for target in a.targets:
   if isinstance(target,ast.Name):assignments.setdefault(target.id,[]).append(a.value)
expected={'quad':'ROWS.endswith("q")','sq_dt':'np.sqrt(dtv)','dt':'np.diff(t_eval)','wm':'0.5*(w_i[1:]+w_i[:-1])','der':'((X3[1:]-X3[:-1])*(wm*sq_dt/dt)[:,None,None]).reshape((Ne-1)*Mout,nc)'}
for name,e in expected.items():check(any(dump(z)==expr(e) for z in assignments[name]),'row AST '+name)
check(any(dump(z)==expr('np.ones(Ne-1)') for z in assignments['sq_dt']),'unweighted sqrt width1')
join=next(z for z in ast.walk(con) if isinstance(z,ast.For) and isinstance(z.target,ast.Name) and z.target.id=='join');check(dump(join.iter)==expr('(tmin,t00)'),'external-only join locations')
# exact Fourier identity by polynomial substitution using e^(i theta)
z=s.symbols('z',nonzero=True);sin=(z-z**-1)/(2*s.I);cos=(z+z**-1)/2;phi=s.expand(cos*cos*sin);check(s.expand(phi-((z-z**-1)+(z**3-z**-3))/(8*s.I))==0,'Phi0 Fourier identity')
x=s.symbols('x');p=x*(1-x*x)**3;jets={str(a):[str(s.diff(p,x,j).subs(x,a)) for j in range(3)] for a in [-1,0,1]};check(jets['-1']==jets['1']==['0','0','0'] and jets['0']==['0','1','0'],'C2 compact polynomial jets')
J,ap,am,delta,fp,fm=s.symbols('J ap am delta fp fm',nonzero=True);sec=(fp+ap*delta/2-fm+am*delta/2)/delta;check(s.expand((sec-(J/delta+(ap+am)/2)).subs(fp,fm+J))==0,'secant identity')
f=json.loads((D/'evidence/fixture.json').read_text());q={n:F(f[n]) for n in ['L','k','cl','R','d','Delta']};ctx.prec=512;ctx.threads=1
def A(v):return arb(v.numerator)/v.denominator
L,k,cl,R,d,Delta=[A(q[n]) for n in ['L','k','cl','R','d','Delta']];weights=[]
for sign in [-1,1]:
 u=R*(sign*Delta/2).exp()/L;weights.append((1+u).sqrt()/(u**3*((k-3)/2*(1+u*u).log()).exp()))
jump=q['cl']*q['R']**3*q['d']/4;wm=sum(weights)/2;fd=wm*A(jump)/Delta;fdq=wm*A(jump)/Delta.sqrt();vals={'weight_left':enc(weights[0]),'weight_right':enc(weights[1]),'H1_jump':enc(fd),'H1q_jump':enc(fdq)}
for n in ['H1_jump','H1q_jump']:check(F(vals[n][0])>F(1,10**11),'amplification exceeds claimed scalar implication')
report=(D/'evidence/NUM_REPORT_snapshot.md').read_text();sentences=['so the floating spectra are those of a repaired continuous section up to','contributions below 1e-11','saved pieces\' internal derivative jumps are below 2.5e-14']
for text in sentences:check(text in report,'captured report claim')
pins={}
for pth in [D/'PROOF.md',D/'evidence/proof_first.json',D/'evidence/fixture.json',D/'evidence/source_snapshot.json',D/'evidence/c2_gram2_source.py.txt',D/'evidence/NUM_REPORT_snapshot.md',D/'evidence/num_TO_TEAM_snapshot.md',Path(__file__)]:pins[str(pth.relative_to(B))]=sha(pth)
check(json.loads((D/'evidence/proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md'),'proof first')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_AST_EXACT_IDENTITIES_AND_ARB512_AMPLIFICATION_FIXTURE','ast_checks':7,'compact_polynomial_jets':jets,'jump_coefficient':rr(jump),'arb_exact_intervals':vals,'display_only':{n:float(F(v[0])) for n,v in vals.items()},'captured_claims':sentences,'files':pins,'scope':'Frozen-source interpretation and independent model fixture. No actual numerical row or spectrum bound.'}
pth=D/'evidence/compute.json';check(not pth.exists(),'immutable');pth.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:out[n] for n in ['utc','status','ast_checks','jump_coefficient','display_only']}))
