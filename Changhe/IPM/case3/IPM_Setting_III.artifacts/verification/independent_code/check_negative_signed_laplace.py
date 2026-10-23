"""Result228 independent symbolic and real-integral verification."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,traceback,math
import numpy as np
import mpmath as mp
import sympy as sy
from negative_signed_laplace import rules,laplace_jets,reduced_ode,h_jets,growing_coefficient
from negative_signed_layer import constants,contour_moments
ROOT=Path('research/negative_signed_laplace_proof');V=ROOT/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
def main():
    pipeline=json.loads(Path('research/hydrostatic_resolved_map_audit/verification/PIPELINE.json').read_text())
    assert pipeline['status']=='DONE','Result227 still owns the sole heavy lane slot'
    result=dict(status='RUNNING',utc_started=utc(),pid=os.getpid(),proof_sha256=sha(ROOT/'PROOF.md'),module_sha256=sha('independent_code/negative_signed_laplace.py'),driver_sha256=sha(__file__),checks=[],rows=[],large_q_diagnostics=[])
    def save():result['utc_updated']=utc();(V/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    def check(name,ok,evidence=None):
        result['checks'].append(dict(name=name,passed=bool(ok),evidence=evidence))
        if not ok:save();raise AssertionError(name)
    save()
    try:
        gate=json.loads(Path('research/negative_signed_inner_layer/verification/CHECKS.json').read_text())
        check('independent Barnes parent gate',gate['status']=='PASS' and gate['module_sha256']==sha('independent_code/negative_signed_layer.py'))
        p,z,lam=sy.symbols('p z lam',positive=True);d=1/(1+p);r=p-2*d;h=sy.Function('h')(z)
        th=lambda f:sy.expand(z*sy.diff(f,z))
        original=th(th(th(h)-p*h)-r*(th(h)-p*h))-(p+2)*(th(th(h)-p*h)-r*(th(h)-p*h))+2*lam*sy.diff(h,z,2)
        P=(1-2*p-r)/z+2*lam/z**3;Q=(p*p+2*p*r+r-1)/z**2;R=-p*r*(p+2)/z**3
        check('scalar ODE coefficients',sy.simplify(original-z**3*(sy.diff(h,z,3)+P*sy.diff(h,z,2)+Q*sy.diff(h,z)+R*h))==0)
        W=z**(2*p+r-1)*sy.exp(lam/z**2)
        check('Abel factor exact',sy.simplify(sy.diff(W,z)+P*W)==0)
        q=sy.symbols('q',positive=True);F=sy.Function('F')
        for e in [0,1]:
            a=(e-p)/2;c=sy.Rational(2*e+1,2);g=a+d
            H=z**e*F(z*z/lam)
            expr=th(th(th(H)-p*H)-r*(th(H)-p*H))-(p+2)*(th(th(H)-p*H)-r*(th(H)-p*H))+2*lam*sy.diff(H,z,2)
            # Construct the q equation and substitute q=z^2/lam only after differentiation.
            dt=lambda f:sy.expand(q*sy.diff(f,q))
            f=F(q);prod=dt(dt(dt(f)+g*f)+(a-1)*(dt(f)+g*f))+a*(dt(dt(f)+g*f)+(a-1)*(dt(f)+g*f))
            eq=dt(dt(f))+(c-1)*dt(f)+q*prod
            check('Laplace reduction epsilon'+str(e),sy.simplify(expr-8*z**e/(z*z/lam)*eq.subs(q,z*z/lam))==0)
        # Positive beta/gamma quadrature manufactures, independent exact moments.
        for pp in [.25,.5,.75]:
            for e in [0,1]:
                for order in [16,32]:
                    a,c,g,t,bw,s,sw=rules(pp,e,order)
                    with mp.workdps(70):
                        for k in range(8):
                            beta=float(mp.rf(mp.mpf(a)+1,k)/mp.rf(mp.mpf(c)+1,k));gm=float(mp.rf(mp.mpf(g),k))
                            eb=abs(float(np.dot(bw,t**k))-beta);eg=abs(float(np.dot(sw,s**k))-gm)/max(1,abs(gm))
                            check(f'moments p{pp} e{e} n{order} k{k}',max(eb,eg)<2e-12,dict(beta_error=eb,gamma_relative_error=eg))
                    jets=laplace_jets(pp,e,0.,order)
                    with mp.workdps(70):
                        exact=[float((-1)**j*mp.rf(mp.mpf(a),j)*mp.rf(mp.mpf(a)-1,j)*mp.rf(mp.mpf(g),j)/mp.rf(mp.mpf(c),j))for j in range(4)]
                    err=max(abs(jets-np.array(exact))/np.maximum(1,abs(np.array(exact))))
                    check(f'origin derivatives p{pp} e{e} n{order}',err<3e-12,float(err))
        print(utc(),'manufactures',len(result['checks']),flush=True);save()
        ps=[mp.mpf(1)/4,mp.mpf(1)/3,mp.sqrt(2)-1,mp.mpf(1)/2,mp.mpf(3)/4]
        # Keep exact decimal p values fixed across the high-precision reference and double integral.
        for pvalue in ps:
            pp=float(pvalue)
            with mp.workdps(70):
                Pm=mp.mpf(pp);D=1/(1+Pm);lammp=4*Pm**2/((1+Pm)**2*(1-Pm));LM=float(lammp);cs=constants(Pm)
                AA=[]
                for e in [0,1]:
                    a=(e-Pm)/2;c=mp.mpf(e)+mp.mpf('.5')
                    A=mp.gamma(c)*mp.gamma(1+D)*lammp**(-(Pm+2-e)/2)/(mp.gamma(a)*mp.gamma(a+D)*mp.gamma(c-a+1));AA.append(A)
                    check(f'exact sign p{pp} e{e}',A<0 if e==0 else A>0)
                    dbl=growing_coefficient(pp,e,LM);check(f'double gamma coefficient p{pp} e{e}',abs(mp.mpf(dbl)/A-1)<mp.mpf('2e-14'),dict(value=mp.nstr(A,45),double=dbl))
                ratio=-AA[0]/AA[1];expect=cs['odd']/cs['even']/mp.sqrt(lammp)
                check('corner ratio gamma identity p'+str(pp),abs(ratio-expect)<mp.mpf('1e-60'),mp.nstr(abs(ratio-expect),15))
            for e in [0,1]:
                for qq in [.01,.1,1.,10/3]:
                    levels=[]
                    for order in [48,96,192]:
                        jets=laplace_jets(pp,e,qq,order);ode=reduced_ode(pp,e,qq,jets);zz=math.sqrt(LM*qq);hh=h_jets(pp,e,zz,LM,order)
                        rr=pp-2/(1+pp);coefP=(1-2*pp-rr)/zz+2*LM/zz**3;coefQ=(pp**2+2*pp*rr+rr-1)/zz**2;coefR=-pp*rr*(pp+2)/zz**3
                        pieces=[hh[3],coefP*hh[2],coefQ*hh[1],coefR*hh[0]];physical=sum(pieces)/max(1.,sum(abs(x)for x in pieces))
                        levels.append(dict(order=order,F_derivatives=jets.tolist(),reduced_ode=ode,physical_normalized_residual=physical))
                    delta=float(max(abs(np.array(levels[-1]['F_derivatives'])-levels[-2]['F_derivatives'])/np.maximum(1,abs(np.array(levels[-1]['F_derivatives'])))))
                    odeerr=abs(levels[-1]['reduced_ode']['residual'])/max(1.,levels[-1]['reduced_ode']['scale'])
                    check(f'integral ODE p{pp} e{e} q{qq}',odeerr<2e-8 and abs(levels[-1]['physical_normalized_residual'])<2e-8,dict(reduced_error=odeerr,physical_error=levels[-1]['physical_normalized_residual']))
                    check(f'quadrature refinement p{pp} e{e} q{qq}',delta<2e-8,delta)
                    check(f'integral monotonicity p{pp} e{e} q{qq}',levels[-1]['F_derivatives'][1]<0 if e==0 else levels[-1]['F_derivatives'][1]>0)
                    result['rows'].append(dict(p=pp,epsilon=e,q=qq,lambda_value=LM,levels=levels,highest_refinement=delta))
                for qq in [1e2,1e4,1e6]:
                    levels=[]
                    for order in [96,192]:
                        jets=laplace_jets(pp,e,qq,order);zz=math.sqrt(LM*qq);value=zz**e*jets[0]/zz**(pp+2);levels.append(dict(order=order,growing_ratio=value,exact_growing_coefficient=growing_coefficient(pp,e,LM),relative_difference=value/growing_coefficient(pp,e,LM)-1))
                    result['large_q_diagnostics'].append(dict(p=pp,epsilon=e,q=qq,levels=levels))
            # Independently computed Barnes values, not externally reported numbers.
            with mp.workdps(55):
                Pm=mp.mpf(pp);cs=constants(Pm);LMmp=mp.mpf(LM)
                for XX in [mp.mpf('.3'),mp.mpf(3),mp.mpf(30)]:
                    zz=mp.sqrt(LMmp/XX);qq=float(1/XX);mom=contour_moments(Pm,XX,order=32,derivatives=0);reference=zz**Pm*mom[0]
                    even0=cs['even']*LMmp**(Pm/2);odd0=cs['odd']*LMmp**(-(1-Pm)/2)
                    E=h_jets(pp,0,float(zz),LM,192)[0];O=h_jets(pp,1,float(zz),LM,192)[0];value=even0*mp.mpf(E)+odd0*mp.mpf(O);error=abs(value-reference)/max(1,abs(reference))
                    check(f'Laplace vs own Barnes p{pp} X{XX}',error<mp.mpf('3e-8'),dict(reference=mp.nstr(reference,40),value=mp.nstr(value,40),relative_error=mp.nstr(error,15)))
            save();print(utc(),'p',pp,'done checks',len(result['checks']),flush=True)
        result.update(status='PASS',count=len(result['checks']),utc_finished=utc());save();print(utc(),'PASS',result['count'],flush=True)
    except Exception:
        result.update(status='FAILED',utc_failed=utc(),error=traceback.format_exc());save();raise
if __name__=='__main__':main()
