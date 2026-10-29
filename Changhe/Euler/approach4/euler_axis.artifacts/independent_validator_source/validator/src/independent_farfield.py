"""Angular far-field algebra using ordinary polynomials, independently of AD."""
import numpy as np
from numpy.polynomial import Polynomial as Poly
from numpy.polynomial.legendre import poly2leg,leg2poly


def integral(poly):
    p=poly.integ()
    return float(p(1)-p(-1))


def pad(values,n):
    out=np.zeros(n,dtype=np.float64)
    out[:len(values)]=values
    return out


def angular_data(alpha,A,B):
    A=A if isinstance(A,Poly) else Poly(A)
    B=B if isinstance(B,Poly) else Poly(B)
    mu=Poly([0,1]); s2=Poly([1,0,-1])
    FR=2*mu*A-s2*A.deriv()
    C=(alpha-2)*A
    Fz=mu*FR-s2*C
    NR=-alpha*FR**2-s2*C*FR.deriv()-s2*(C*C+B*B)
    V=(1-alpha)*FR*C+mu*C*C-s2*C*C.deriv()-mu*B*B
    W=(1-alpha)*FR*B+2*mu*C*B-s2*C*B.deriv()
    source=(1-2*alpha)*NR-(s2*V).deriv()
    fmode=poly2leg(source.coef)
    nmode=pad(poly2leg(NR.coef),len(fmode))
    ell=np.arange(len(fmode))
    eigen=ell*(ell+1)-2*alpha*(2*alpha-1)
    Qmode=np.zeros_like(fmode)
    # These coefficients use the proven compatibility identities, including
    # the full-space selection at alpha=1/2 and alpha=1.
    Qmode[0]=nmode[0]/(2*alpha)
    T=1.5*integral(FR*Fz)
    if len(Qmode)>1:
        Qmode[1]=(nmode[1]-T)/(2*alpha+1)
    if len(Qmode)>2:
        Qmode[2:]=fmode[2:]/eigen[2:]
    Q=Poly(leg2poly(Qmode))
    GR=NR-2*alpha*Q
    GV=V-Q.deriv()
    divergence=(1-2*alpha)*GR-(s2*GV).deriv()
    antiderivative=GR.integ()
    numerator=-antiderivative+antiderivative(-1)
    quotient,remainder=np.polynomial.polynomial.polydiv(numerator.coef,s2.coef)
    A1=Poly(quotient)
    E=-(alpha*(alpha-3)*A+s2*A.deriv(2)-4*mu*A.deriv())
    energy=2*np.pi*integral(FR*FR+s2*(C*C+B*B))
    return {'A':A,'B':B,'FR':FR,'C':C,'Fz':Fz,'NR':NR,'V':V,'W':W,'source':source,
            'fmode':fmode,'nmode':nmode,'eigenvalues':eigen,'Q':Q,'Qmode':Qmode,'T':T,
            'GR':GR,'GV':GV,'GW':W,'A1':A1,'B1':W,'A1_remainder':remainder,
            'divergence':divergence,'E':E,'angular_energy':energy}


def evaluate_vector(data,mu,prefix='F'):
    mu=np.asarray(mu,dtype=np.float64)
    s=np.sqrt(1-mu*mu)
    if prefix=='F':
        return np.stack((data['FR'](mu),s*data['C'](mu),s*data['B'](mu)),axis=-1)
    if prefix=='N':
        return np.stack((data['NR'](mu),s*data['V'](mu),s*data['W'](mu)),axis=-1)
    if prefix=='G':
        return np.stack((data['GR'](mu),s*data['GV'](mu),s*data['GW'](mu)),axis=-1)
    raise ValueError(prefix)


def regularized_angular_terms(coefficients,beta,improved=True):
    """Smooth extension with the desired tail; improved cancels the R^-2 error."""
    terms=[]
    for j,c in enumerate(coefficients):
        exponent=(beta+j)/2
        terms.append((float(c),0,j,exponent))
        if improved:
            terms.append((float(c*exponent),0,j,exponent+1))
    return terms


def asymptotic_fixture(alpha,corrected=True,improved=True):
    from independent_fields import PotentialField,ScalarExpansion
    data=angular_data(alpha,[.42,-.23,-.04],[.34,.19,.13])
    phi=regularized_angular_terms(data['A'].coef,alpha,improved)
    q=regularized_angular_terms(data['B'].coef,alpha+1,improved)
    if corrected:
        phi+=regularized_angular_terms(data['A1'].coef,2*alpha+1,improved)
        q+=regularized_angular_terms(data['B1'].coef,2*alpha+2,improved)
    return PotentialField(ScalarExpansion(phi),ScalarExpansion(q),1/(1+alpha)),data
