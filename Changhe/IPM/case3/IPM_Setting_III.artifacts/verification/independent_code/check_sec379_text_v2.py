"""Result226v2: frozen text changes, Laplace identity, distinct scalar quadrature."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib,math,difflib
import mpmath as mp
import numpy as np
import sympy as S
from negative_signed_laplace import rules
from negative_signed_gauss_scalar import gauss_value,laplace_large_ratio,params
ROOT=Path('research/sec379_text_audit');V=ROOT/'verification/v2';old=ROOT/'verification/v1'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
flat=lambda s:' '.join(s.split())
checks=[];rows=[]
def check(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
def main():
    gate=json.loads(Path('research/negative_signed_laplace_proof/verification/CHECKS.json').read_text());assert gate['status']=='PASS','228 pending or failed'
    check('228 proof gate',gate['proof_sha256']==sha('research/negative_signed_laplace_proof/PROOF.md'));check('228 module gate',gate['module_sha256']==sha('independent_code/negative_signed_laplace.py'))
    previous=json.loads((old/'CHECKS.json').read_text());check('v1 confirmed97',previous['status']=='PASS'and previous['count']==97)
    for key,f in [('body_sha256','body.txt'),('app_sha256','app.txt')]:check('v1 hash '+f,sha(old/f)==previous[key])
    for a in json.loads((V/'INPUTS.json').read_text())['files']:check('v2 frozen '+a['frozen'],sha(a['frozen'])==a['sha256'])
    b=flat((V/'body.txt').read_text());app=flat((V/'app.txt').read_text());bodyold=flat((old/'body.txt').read_text());appold=flat((old/'app.txt').read_text())
    for x in ['On z > 0, solutions with all the other properties exist','does not satisfy (1) across z = 0 in the sense of distributions','delta(z) with the factor 2 h\'(0+)','contains no multiple of delta(z)','asymptotic expansion in powers of z^2','0 < K < inf','three bounds of 3.72(d)','not profiles at finite slope']:
        check('body scope '+x,x in b)
    for x in ['Gamma(-s/2)^{-1}','-s/2 > 0','8 (tau d/dtau - s/2 - tau) Phi','d/dtau (e^{-tau} tau^{-s/2} Phi)','asymptotic series','DLMF 15.8(ii)','Gamma((p + 2 - s)/2)','even extension, the multiples of E','These checks concern the formal inner problem only']:
        check('appendix new proof '+x,x in app)
    check('signed axis proof unchanged',app.split('Sign of K.')[1].split('Behaviour at z = 0.')[0]==appold.split('Sign of K.')[1].split('Behaviour at z = 0.')[0])
    check('inner equations unchanged',app.split('Sign of K.')[0]==appold.split('Sign of K.')[0]);check('count unchanged',app.split('Count.')[1].split('Checks.')[0]==appold.split('Count.')[1].split('Checks.')[0])
    for name in ['body','app']:
        delta=list(difflib.unified_diff((old/(name+'.txt')).read_text().splitlines(),(V/(name+'.txt')).read_text().splitlines(),fromfile='v1',tofile='v2'))
        (V/(name+'.independent.diff')).write_text('\n'.join(delta)+'\n')
    tree=ast.parse((V/'producer_ed69.py').read_text());assign=next(n for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='reps'for t in n.targets));reps=ast.literal_eval(assign.value)
    check('installer seven replacements',len(reps)==7)
    for i in [4,5]:check('summary formal and leading order '+str(i),'formally' in reps[i][1]and ('leading order'in reps[i][1]or'at that order'in reps[i][1]))
    check('summary class restrictions','even and C^1 at the axis'in reps[5][1]);check('summary alternative layers retained','layers of other widths and nonlinear inner balances are not excluded'in reps[6][1])
    # The frozen installer still requires the explicit half-line parenthesis repair.
    oldtext='(solutions with a corner at the axis exist for every C_p(Theta))'
    newtext='(on z > 0, solutions with a corner permitted at the axis exist for every C_p(Theta); their even extensions with a nonzero corner do not solve the inner equations distributionally across the axis)'
    repair=dict(file='lead/code/ed69.py',old=oldtext,new=newtext,reason='The v2 body excludes a distributional corner solution across zero; the summary must retain the half-line scope.')
    check('summary repair target exact',oldtext in reps[4][1])
    x,p,tau,z,lam=S.symbols('x p tau z lam',positive=True);a=-p/2;b0=a-1;c0=S.Rational(1,2);d=1/(p+1);s=p-2*d;g=-s/2;J=S.Function('J')(x)
    delta=lambda f:S.expand(x*S.diff(f,x));Phi=delta(delta(J)+b0*J)+a*(delta(J)+b0*J)
    th=lambda f:2*delta(f)
    cubic=th(th(th(J)-p*J)-s*(th(J)-p*J))-(p+2)*(th(th(J)-p*J)-s*(th(J)-p*J))
    physical2=4*tau*S.diff(J,x)+8*tau*x*S.diff(J,x,2)
    right=8*(delta(Phi)+(g-tau)*Phi)
    Gauss=x*(1+x)*S.diff(J,x,2)+(c0+(a+b0+1)*x)*S.diff(J,x)+a*b0*J
    check('pointwise Laplace identity modulo Gauss',S.simplify(cubic+physical2-right-8*tau*Gauss)==0)
    P=S.Function('P')(tau);weight=S.exp(-tau)*tau**(g-1)
    check('integration by parts identity',S.simplify(weight*(tau*S.diff(P,tau)+(g-tau)*P)-S.diff(S.exp(-tau)*tau**g*P,tau))==0)
    check('gamma coefficient argument',S.simplify((p+2-s)/2-(1+d))==0)
    for pp in [.25,.5,.75]:
        for xx in [0.,.2,.8,1.5,2.,2.000001,8.,100.]:
            calc=gauss_value(pp,xx);refs=[]
            for n in [64,128]:
                aa,cc,gg,T,W,ss,ww=rules(pp,0,n);ref=1+(aa/cc)*np.dot(W,np.expm1((1-aa)*np.log1p(xx*T))/T);refs.append(float(ref))
            error=abs(calc-refs[-1])/max(1,abs(calc));check(f'scalar series vs real integral p{pp} x{xx}',error<2e-11,dict(scalar=calc,ref=refs,error=error))
        with mp.workdps(70):
            Pm=mp.mpf(pp);D=1/(1+Pm);A=-Pm/2;C=mp.mpf('.5');beta=1-A;G=A+D;LM=4*Pm**2/((1+Pm)**2*(1-Pm));L=mp.gamma(C)/(mp.gamma(A)*mp.gamma(C-A+1));AE=L*mp.gamma(1+D)*LM**(-(Pm+2)/2)/mp.gamma(G)
            quote={.25:'-.896637',.5:'-.193424',.75:'-.0210086'}[pp];check('printed A_E '+str(pp),abs(AE-mp.mpf(quote))<mp.mpf('5e-7'),mp.nstr(AE,45));check('A_E negative '+str(pp),AE<0)
            q=mp.mpf('1e8')/LM;small=2*mp.exp(-120*G)/(G*abs(L)*q**beta*mp.gamma(1+D))
            CB=abs(mp.gamma(C)/(mp.gamma(A)*mp.gamma(C-A)));factor=1/abs(L)+CB*beta*2**(beta-1)/abs(L)*(mp.beta(A+1,C-A)+1/(C-A));large=factor*mp.gammainc(1+D,100,mp.inf)/mp.gamma(1+D)
            expected=beta*(C-A)/(D*q)*(mp.log(q)+mp.digamma(D)+mp.digamma(1)+mp.digamma(2)-mp.digamma(A)-mp.digamma(C-A))
        vals=[laplace_large_ratio(pp,1e4,float(LM),16,1.),laplace_large_ratio(pp,1e4,float(LM),24,.75)]
        check('log quadrature refinement '+str(pp),abs(vals[-1]-vals[0])<2e-11,vals);check('finite z1e4 ratio within1e-6 '+str(pp),abs(vals[-1]-1)<1e-6,vals[-1]-1)
        check('omitted numerical tails '+str(pp),max(small,large)<mp.mpf('1e-18'),dict(lower=mp.nstr(small,20),upper=mp.nstr(large,20)))
        rows.append(dict(p=pp,lambda_value=float(LM),A_E=mp.nstr(AE,45),finite_z=1e4,ratios=vals,first_correction=float(expected),omitted_lower_bound=mp.nstr(small,20),omitted_upper_bound=mp.nstr(large,20)))
    result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS'if all(t['passed']for t in checks)else'FAIL',count=len(checks),checks=checks,rows=rows,required_summary_repair=repair,proof_sha256=sha(ROOT/'REVISION2_PROOF.md'),module_sha256=sha('independent_code/negative_signed_gauss_scalar.py'),driver_sha256=sha(__file__),body_sha256=sha(V/'body.txt'),app_sha256=sha(V/'app.txt'),scope='Fixed signed ODE and exact text changes. One planned summary repair required. Producer outward integration not independently rerun; full PDE endpoint OPEN.')
    (V/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count']);print([t for t in checks if not t['passed']])
    if result['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
