"""Independent Arb384 evaluation of the explicit Fourier/source constants."""
from fractions import Fraction
from flint import arb,ctx,fmpq

def evaluate(parameters):
    ctx.prec=384;ctx.threads=1
    def Q(q):
        q=Fraction(q);return arb(fmpq(q.numerator,q.denominator))
    p={k:Q(v) for k,v in parameters['inputs'].items()}
    s=p['s'];pi=arb.pi()
    v={'pi':pi}
    v['CU']=1/(32*pi*(s-1)).sqrt()
    v['Csigma']=1/(64*pi*(s-1)*(s-2)).sqrt()
    v['Cy']=1/(8*pi*(s-1)*(s-2)).sqrt()
    v['CH']=1/(4*pi*(s-1)*(s-2)*(s-3)).sqrt()
    v['c0']=v['CU']+p['xmax']*v['Csigma']/3
    v['c1']=4*v['Csigma']/3
    v['b1']=p['MV']*v['c0']/p['m0']+v['c1']
    v['b2']=v['b1']+2*v['Csigma']/3
    v['b3']=p['Mrho']*v['c0']/p['m0']
    for i in (1,2,3):v['B'+str(i)]=v['b'+str(i)]*p['H']
    v['e0']=v['c0']*p['H'];v['e1']=v['c1']*p['H'];v['e3']=v['Cy']*p['H']
    v['B3_density']=v['B3']+v['e3'];v['m2']=v['CH']*p['H']
    v['d_bound']=v['e0']/p['m0'];v['mR_lower']=p['m0']*p['R']
    v['delta_lower']=(p['R0']-v['d_bound'])/3
    v['box1_radius']=p['box1']/v['b1']
    v['kappa']=Q('1301/200')-Q('101/100')*s
    v['source_multiplier']=12*s+Q('9/2')
    v['E']=(v['source_multiplier']*(p['MV']+v['m2'])+3*p['Mrho'])*p['delta_max']
    v['K1']=1/(v['kappa']-v['E'])
    v['exclusion_lhs']=v['b1']*p['H_exclusion']
    v['exclusion_radius']=(p['defect_lower']-p['defect_error'])/v['b1']
    v['exclusion_e3']=v['Cy']*p['H_exclusion']
    v['exclusion_gradient_lower']=p['g_center']-p['g_error']-p['Mrho']*p['R0']-v['exclusion_e3']
    def endpoint(a):
        m,e=a.man_exp();return Fraction(int(m))*Fraction(2)**int(e)
    out={}
    for key,a in v.items():
        assert a.is_finite();lo,hi=endpoint(a.lower()),endpoint(a.upper());assert lo<=hi
        out[key]={'lower_exact':str(lo),'upper_exact':str(hi)}
    return out
