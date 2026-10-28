"""Independent analytic reduction of the lead's gated witness. Diagnostics only."""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps = 60
q=mp.sqrt(2)-1

def primitive(s,b,d,r):
    den=(r+d)**2+(s*r+b)**2
    return s*mp.log(den)/4+mp.atan((2*r+d+s*b)/(b-s*d))/2

def H(s,b,r):
    return primitive(s,b,0,r)-primitive(s,b,1,r)

def J_primitive(t):
    c=t/mp.sqrt(2); ell=(t-1)/2
    val=mp.pi/2-H(1,c,0)-H(1,-c,c)+H(-1,c,0)-H(-1,c,ell)
    if t<q:
        val+=H(-1,-c,-c)-H(-1,-c,ell)
    return val/mp.pi

def J_regularized(t):
    """J(t)+2 log(t)/pi, evaluated without a singular subtraction."""
    if t==0:
        return mp.log(2)/mp.pi
    c=t/mp.sqrt(2)
    if t<q:
        a=(1-t)/2
        p0=4*a**4+c**4
        p1=((1-a)**2+a*a+c*c)**2-4*a*a*c*c
        val=mp.log(2)+mp.log1p(-c**4)/2+mp.log(p0/p1)/4
        val+=(-mp.atan(c/(1-t+c))+mp.atan(c/(1-t-c))
              +mp.atan((t-c)/(1+c))+mp.atan((t+c)/(1-c)))/2
        return val/mp.pi
    ell=(t-1)/2
    val=mp.log1p(c*c)/2-mp.mpf('1.5')*mp.log(c)+mp.log1p(c)/2-H(-1,c,ell)
    return (val+2*mp.log(t))/mp.pi

def J_rational_quad(t):
    c=t/mp.sqrt(2); ell=(t-1)/2
    def integrand(r):
        out=mp.mpf(0)
        for eps in [-1,1]:
            p=abs(r)+eps*c
            if p>0:
                out+=p*(1/(r*r+p*p)-1/((r+1)**2+p*p))
        return out
    pts=sorted(set([ell,mp.mpf(0),c]+([-c] if ell<-c else [])))+[mp.inf]
    return mp.quad(integrand,pts)/mp.pi

def lower(alpha):
    # The regularized integrand has a double zero at t=0.
    c0=mp.log(2)/mp.pi
    rem=mp.quad(lambda t:t**(alpha-1)*(J_regularized(t)-c0),[0,q,1])
    return 2/(mp.pi*alpha)+c0+alpha*rem

if __name__=='__main__':
    checks=[]
    for txt in ['0.000001','0.01','0.1',str(q),'0.7','1']:
        t=mp.mpf(txt)
        a=J_primitive(t); b=J_regularized(t)-2*mp.log(t)/mp.pi; c=J_rational_quad(t)
        checks.append({'t':mp.nstr(t,45),'primitive':mp.nstr(a,45),'rational_quadrature':mp.nstr(c,45),'residual':mp.nstr(max(abs(a-b),abs(a-c)),10)})
        assert abs(a-b)<mp.mpf('1e-50') and abs(a-c)<mp.mpf('1e-50')
    rows=[]
    for txt in ['.001','.01','.02','.05','.1','.2','.25','.3','.4','.5','.6','.7','.75','.8','.9','.95','.99']:
        a=mp.mpf(txt); val=lower(a)
        rows.append({'alpha':txt,'lower_diagnostic':mp.nstr(val,45),'additive_over_2_pi_alpha':mp.nstr(val-2/(mp.pi*a),45)})
    out={'status':'high precision diagnostic, not a certificate','checks':checks,'values':rows}
    Path('data/gated_reduction_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
    for r in rows:
        print(r,flush=True)
