"""Independent series and Barnes-contour realization of result224.

No producer module, meijerg, hyper or numerical differentiation is used.
All differentiation is performed on the integral/series coefficients.
"""
from functools import lru_cache
import mpmath as mp


def parameters(p):
    p=mp.mpf(p)
    return {'p':p,'mu':(1+p)/2,'r':p-2/(1+p),'a':-p/2,
            'b':(1-p)/2,'d':1/(1+p),'B':p/(1+p)}


def constants(p):
    q=parameters(p);a,b,d,B=(q[k]for k in ['a','b','d','B'])
    return dict(A1=mp.gamma(d)*mp.gamma(a)*mp.gamma(b),
        A2=mp.gamma(-d)*mp.gamma(a+d)*mp.gamma(b+d)/mp.gamma(2+d),
        E1=mp.gamma(B)/(mp.gamma(a)*mp.gamma(b)),
        E2=mp.gamma(1+d)*mp.gamma(2+d)/(mp.gamma(a+d)*mp.gamma(b+d)),
        even=mp.gamma(a)*mp.gamma(d+a)*mp.gamma(b-a)/mp.gamma(2-a),
        odd=mp.gamma(b)*mp.gamma(d+b)*mp.gamma(a-b)/mp.gamma(2-b))


def series_moments(p,X,branch,derivatives=3):
    """Return T^j f, with T=X*d/dX, from coefficient recurrences."""
    q=parameters(p);X=mp.mpf(X);d=q['d'];shift=mp.mpf(0) if branch==1 else d
    a=q['a']+shift;b=q['b']+shift
    c=q['B'] if branch==1 else 1+d
    e=mp.mpf(2) if branch==1 else 2+d
    term=X**shift;sums=[term*shift**j for j in range(derivatives+1)]
    cap=max(1000,int(4*X)+4*mp.mp.dps)
    for k in range(1,cap):
        term*=X*(a+k-1)*(b+k-1)/((c+k-1)*(e+k-1)*k)
        for j in range(derivatives+1):sums[j]+=term*(shift+k)**j
        if k>max(30,2*X) and all(abs(term*(shift+k)**j)<mp.eps*max(abs(sums[j]),mp.mpf('1e-50')) for j in range(derivatives+1)):
            return sums,k
    raise ArithmeticError('Series cap exhausted')


def combination_moments(p,X,derivatives=3):
    c=constants(p);one,n1=series_moments(p,X,1,derivatives);two,n2=series_moments(p,X,2,derivatives)
    return [c['A1']*x+c['A2']*y for x,y in zip(one,two)],max(n1,n2)


@lru_cache(maxsize=8)
def legendre_rule(order,dps):
    with mp.workdps(dps):
        x,w=mp.gauss_quadrature(order,'legendre')
        return tuple((+x[j],+w[j])for j in range(order))


@lru_cache(maxsize=40)
def contour_nodes(p_text,order,dps):
    """Fixed contour after both algebraic poles, with uniform pole distance1/4."""
    with mp.workdps(dps):
        q=parameters(mp.mpf(p_text));a,b,d=(q[k]for k in ['a','b','d']);eta=q['p']/2-mp.mpf(3)/4
        rule=legendre_rule(order,dps);cuts=[0,mp.mpf('.25'),mp.mpf('.5'),1,2,4,8,16,32,64]
        vals=[]
        for lo,hi in zip(cuts[:-1],cuts[1:]):
            mid=(lo+hi)/2;rad=(hi-lo)/2
            for xi,wi in rule:
                t=mid+rad*xi;s=eta+1j*t
                kernel=mp.gamma(-s)*mp.gamma(d-s)*mp.gamma(a+s)*mp.gamma(b+s)/mp.gamma(2+s)
                vals.append((s,rad*wi*kernel/mp.pi))
        return tuple(vals)


def contour_moments(p,X,order=32,derivatives=3):
    """Complete improper contour, numerically truncated at |Im s|=64."""
    p=mp.mpf(p);X=mp.mpf(X);q=parameters(p);c=constants(p)
    vals=contour_nodes(mp.nstr(p,mp.mp.dps),order,mp.mp.dps)
    answer=[]
    for j in range(derivatives+1):
        integrand=[mp.re(weight*mp.exp(s*mp.log(X))*s**j)for s,weight in vals]
        residues=c['even']*X**(-q['a'])*(-q['a'])**j+c['odd']*X**(-q['b'])*(-q['b'])**j
        answer.append(residues+mp.fsum(integrand))
    return answer


def z_euler_moments(p,z,lam,X_moments):
    p=mp.mpf(p);z=mp.mpf(z)
    return [z**p*mp.fsum(mp.binomial(j,l)*p**(j-l)*(-2)**l*X_moments[l]for l in range(j+1))for j in range(len(X_moments))]


def ode_terms(p,z,lam,moments):
    q=parameters(p);p=q['p'];r=q['r'];h,H1,H2,H3=moments
    lhs=H3-(2*p+r+2)*H2+(p*r+p*(p+2)+r*(p+2))*H1-p*r*(p+2)*h
    rhs=-2*lam*(H2-H1)/z**2
    return lhs,rhs
