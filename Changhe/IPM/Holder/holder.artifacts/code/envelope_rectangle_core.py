"""Exact rectangular kernel masses and rigorous envelope cell bounds."""
from fractions import Fraction
from flint import arb,acb

def asarb(x):
    if isinstance(x,Fraction):return arb(x.numerator)/x.denominator
    return arb(x)

def pole_mass(a,b,c,d,p):
    def angle(x,y):return acb(y,x-p).arg()
    return (angle(b,d)-angle(a,d)-angle(b,c)+angle(a,c))/(2*arb.pi())

def cell_mass(a,b,c,d):
    a,b,c,d=map(asarb,(a,b,c,d))
    return pole_mass(a,b,c,d,arb(1)/2)-pole_mass(a,b,c,d,-arb(1)/2)

def cell_interval(env,rect):
    a,b,c,d=map(asarb,rect)
    x=(a+b)/2;y=(c+d)/2
    eta=((b-a)**2+(d-c)**2).sqrt()/2
    value,nearest=env.evaluate(x,y)
    epsilon=eta.sqrt()
    near_lower=arb(nearest.lower());eta_upper=arb(eta.upper())
    if near_lower>eta_upper:
        epsilon=arb.min(epsilon,eta/(2*(near_lower-eta_upper).sqrt()))
    z=acb(a.union(b),c.union(d))
    density=(z/(arb.pi()*(z*z-arb(1)/4)**2)).real
    assert density.is_finite()
    mass=pole_mass(a,b,c,d,arb(1)/2)-pole_mass(a,b,c,d,-arb(1)/2)
    if density>0 or density<0:tv=abs(mass)
    else:tv=(b-a)*(d-c)*abs(density)
    error=arb((tv*epsilon).upper())
    return mass*value+arb(0,error.upper()),error,env.last_counts

def shell_rectangles(exponent,n):
    r=Fraction(2)**exponent;half=Fraction(1,2)
    bands=[(max(Fraction(0),half-2*r),half+2*r,r,2*r),
           (half+r,half+2*r,Fraction(0),r)]
    if half-r>0:
        bands.append((max(Fraction(0),half-2*r),half-r,Fraction(0),r))
    out=[]
    for a,b,c,d in bands:
        if b<=a:continue
        nx=max(1,((b-a)*n/r).__ceil__());ny=n
        for i in range(nx):
            for j in range(ny):
                out.append((a+(b-a)*i/nx,a+(b-a)*(i+1)/nx,c+(d-c)*j/ny,c+(d-c)*(j+1)/ny))
    return out
