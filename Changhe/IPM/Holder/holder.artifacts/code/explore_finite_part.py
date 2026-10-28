"""Diagnostic finite part of the absolute Txy increment density."""
import mpmath as mp
mp.mp.dps=60
a=mp.mpf('0.5')

def b(y):
    return mp.sqrt((a*a-y*y+2*mp.sqrt(y**4+a*a*y*y+a**4))/3)

def variation_slice(y):
    z=b(y)
    return 2*y/mp.pi*(1/((z-a)**2+y*y)-1/((z+a)**2+y*y))

def fp():
    return mp.quad(lambda y:variation_slice(y)-2/(mp.pi*y),[0,mp.mpf('.5'),1])+mp.quad(variation_slice,[1,mp.inf])

v=fp()
print('Strip finite part',mp.nstr(v,50))
print('Circular finite part',mp.nstr(v+1/mp.pi,50))
print('Candidate additive coefficient',mp.nstr(v+mp.log(2)/mp.pi,50))
for n in [4,8,12]:
    e=mp.mpf(10)**(-n)
    test=2*mp.log(e)/mp.pi+mp.quad(variation_slice,[e,mp.mpf('.5'),1,mp.inf])
    print('Cutoff check',n,mp.nstr(test,45),mp.nstr(test-v,10))

def by(x):
    X=x*x
    return abs(X-a*a)/mp.sqrt(X+a*a+2*mp.sqrt(X*X-a*a*X+a**4))

def axis_slice(x):
    z=by(x)
    return 2*z/mp.pi*(1/((x-a)**2+z*z)-1/((x+a)**2+z*z))

E=mp.mpf('1e-16')
axisstrip=2*mp.log(E)/mp.pi+mp.quad(axis_slice,[0,a-E])+mp.quad(axis_slice,[a+E,1,2,mp.inf])
correction=2/mp.pi*mp.quad(lambda t:abs(mp.cos(2*t))*(-mp.log(mp.cos(t))),[0,mp.pi/4,mp.pi/2])
axiscircle=axisstrip+correction
print('Axis strip finite part',mp.nstr(axisstrip,45))
print('Axis correction',mp.nstr(correction,45))
print('Axis circular finite part',mp.nstr(axiscircle,45))
print('Axis additive candidate',mp.nstr(axiscircle+(mp.log(2)-1)/mp.pi,45))
