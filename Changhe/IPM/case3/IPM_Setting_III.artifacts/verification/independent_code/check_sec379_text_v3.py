"""Result226v3 exact text, signed symmetry and outer coefficient audit."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,ast
import sympy as S
import mpmath as mp
ROOT=Path('research/sec379_text_audit');V=ROOT/'verification/v3';V2=ROOT/'verification/v2'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
flat=lambda s:' '.join(s.split())
checks=[]
def check(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
def replacements(path):
    tree=ast.parse(Path(path).read_text())
    node=next(n for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='reps'for t in n.targets))
    return ast.literal_eval(node.value)
def main():
    prior=json.loads((V2/'CHECKS.json').read_text());check('v2 gate78',prior['status']=='PASS'and prior['count']==78)
    for k,f in [('body_sha256','body.txt'),('app_sha256','app.txt')]:check('v2 frozen '+f,prior[k]==sha(V2/f))
    check('v2 proof unchanged',prior['proof_sha256']==sha(ROOT/'REVISION2_PROOF.md'))
    cp=Path('research/hydrostatic_second_compatibility_v2_audit/verification/CHECKS.json');cg=json.loads(cp.read_text());check('209 repaired trace gate46',cg['pass_count']==46 and cg['fail_count']==0)
    for row in json.loads((V/'INPUTS.json').read_text())['files']:
        check('v3 frozen '+Path(row['frozen']).name,sha(row['frozen'])==row['sha256'])
        check('v3 current source '+Path(row['frozen']).name,sha(row['source'])==row['sha256'])
    b=flat((V/'body.txt').read_text());a=flat((V/'app.txt').read_text());b2=flat((V2/'body.txt').read_text());a2=flat((V2/'app.txt').read_text())
    check('inner equation and count unchanged',b.split('(a) Inner equations.')[1].split('|lambda|).')[0]==b2.split('(a) Inner equations.')[1].split('|lambda|).')[0])
    check('appendix inner derivation unchanged',a.split('Sign of K.')[0]==a2.split('Sign of K.')[0])
    check('appendix endpoint proof and checks unchanged',a.split('Behaviour at z = 0.')[1]==a2.split('Behaviour at z = 0.')[1])
    for clause in ['except the sign of K and the symmetry in (d), which are proved','if and only if -g solves that of (3) of 3.72','g_y(0) = -1 in place of g_y(0) = 1','1/2 < p < 1','the term of degree 3p - 2 is the function f_{3p-2} defined by (1) of 3.76','some of the positive monotone traces of 3.76(b) satisfy both','other layer widths, nonlinear inner balances','not profiles at finite slope']:
        check('body clause '+clause,clause in b)
    for clause in ['the steps of A.3.73(a) that give the positivity and the far field','The other identities of 3.73(a), (2) and the cubic relation, change sign','since v\'\' = g_xixi(0, .) here; they are not used','D f_{2p-1} + V[f_p] . grad f_p = 0','the second becomes (1) of 3.76','(c X + V[-g]) . grad (-g) = -(c X - V[g]) . grad g']:
        check('appendix clause '+clause,clause in a)
    old=replacements(V2/'producer_ed69.py');new=replacements(V/'producer_ed69.py');check('seven installer replacements',len(new)==len(old)==7)
    check('old replacement targets unchanged',[x[0]for x in old]==[x[0]for x in new]);check('coverage notation unchanged',old[:4]==new[:4]);check('Section6 summary unchanged',old[5]==new[5])
    repair=prior['required_summary_repair'];check('Section1 repair exact',new[4][1]==old[4][1].replace(repair['old'],repair['new']))
    for clause in ['leading order','even and C^1 at the axis','layers of other widths and nonlinear inner balances are not excluded','with g_y(0) = -1','termwise far-field conditions','for 1 < c < 2','conditions on the trace, not an obstruction']:
        check('Section7 scope '+clause,clause in new[6][1])
    # Bilinear symmetry with independent component symbols.
    c,x,y,g,gx,gy,u,v=S.symbols('c x y g gx gy u v');lhs=(c*x-u)*(-gx)+(c*y-v)*(-gy)+g;minus=-((c*x-u)*gx+(c*y-v)*gy-g)
    check('exact signed residual negation',S.expand(lhs-minus)==0)
    p=S.symbols('p',positive=True);D=(1-p)/p;d=2*p-1;e=3*p-2
    check('first degree coefficient',S.simplify(d/p-1+D)==0);check('second degree coefficient',S.simplify(e/p-1+2*D)==0)
    A,B,C=S.symbols('A B C');h=A/D;k=(B+C)/(2*D)
    check('signed first coefficient',S.simplify(-D*(-h)-A)==0);check('signed third coefficient unchanged',S.simplify(-2*D*k-(-B)-(-C))==0)
    z,bb,ee=S.symbols('z B E');G=z+ee*z**3;vel=z+bb*z**3/3
    check('signed cubic B=-6E',S.expand(vel*S.diff(G,z)-G).coeff(z,3).subs(bb,-6*ee)==0)
    t,R=S.symbols('t R',positive=True);f=S.Function('v')(t)
    # The exact primitive of (1-t/R)v'' is (1-t/R)v'+v/R.
    primitive=(1-t/R)*S.diff(f,t)+f/R
    check('weighted axis primitive',S.simplify(S.diff(primitive,t)-(1-t/R)*S.diff(f,t,2))==0)
    with mp.workdps(70):
        for pp in [mp.mpf('0.55'),mp.mpf('0.6'),mp.mpf('0.75'),mp.mpf('0.9')]:
            dd=2*pp-1;DD=(1-pp)/pp;beta=pp*(pp+2);J=mp.sqrt(mp.pi)*mp.gamma((2-dd)/2)/(2*mp.gamma((3-dd)/2))
            C0=1/(pp+2);A0=C0*C0/DD
            raw=-A0*J*(beta*(1-dd**2)/dd+(3-beta)*(dd+1)*(dd+2)/(3-dd))
            exact=-3*pp**2*(4*pp**2+5*pp-1)*J/((pp+2)**2*(2*pp-1)*(2-pp))
            check('independent explicit second cusp p'+str(pp),raw<0 and abs(raw-exact)<mp.mpf('1e-60'),mp.nstr(raw,40))
            plus=pp*raw/(2*DD);signed=(-1)*pp*(-raw)/(2*DD)
            check('signed second cusp unchanged p'+str(pp),plus==signed,mp.nstr(signed,40))
    out=dict(status='PASS'if all(q['passed']for q in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(ROOT/'REVISION3_PROOF.md'),driver_sha256=sha(__file__),body_sha256=sha(V/'body.txt'),app_sha256=sha(V/'app.txt'),installer_sha256=sha(V/'producer_ed69.py'),parent209_sha256=sha(cp),required_repairs=[],scope='Exact proposed v3 body/app and planned summary strings confirmed. Installation unverified; nonlinear PDE endpoint OPEN.')
    (V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([q for q in checks if not q['passed']])
    if out['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
