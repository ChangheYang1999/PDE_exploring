"""Arb leading tails from exact cyclic sums, no trigonometric library calls."""
from fractions import Fraction as Q
from flint import arb,ctx

def evaluate(p):
 ctx.prec=512;ctx.threads=1
 def a(x):
  x=Q(x);return arb(x.numerator)/x.denominator
 def h(x):return Q(float.fromhex(x))
 def sq(x):return str(Q(int(x.man_exp()[0]))*Q(2)**int(x.man_exp()[1]))
 def box(x):return {'lower_exact':sq(x.lower()),'upper_exact':sq(x.upper()),'display':str(x)}
 beta=list(map(h,p['beta_hex']));co=list(map(h,p['modal_A0_hex']));t=list(map(h,p['chebyshev_hex']));cyc=[1,0,-1,0]
 S=sum((x*cyc[i%4] for i,x in enumerate(beta)),Q(0));C=sum((x*cyc[i%4] for i,x in enumerate(co)),Q(0));T=sum(t,Q(0));k=Q(p['k']);pp=Q(p['p'])
 z=a(p['z_public_bracket'][0]).union(a(p['z_public_bracket'][1]));L=a(p['L']);two=arb(2);Lpow=(a(3-k)*L.log()).exp();Mpow=(a(3-k)*a(p['tplus'])).exp();angular=1/(two*two.sqrt())
 inner=(a(S)+a(T)*(-a(pp)*two.log()/2).exp()).exp()
 thetaX=Lpow*angular*inner;thetaM=Mpow*angular*(a(C)+z)
 return {'method':'Arb512 exact dyadic cyclic sums and logarithmic exponentials','values':{k:box(v) for k,v in {'T1':a(T),'p':a(pp),'ThetaX':thetaX,'ThetaM':thetaM,'Delta':thetaX-thetaM,'D_F0':Lpow*(sum((a(b)*((-1)**i) for i,b in enumerate(beta)),arb(0))).exp()*a(T),'z':z}.items()},'counts':{'beta':len(beta),'outer':len(co),'chebyshev':len(t)},'exact_sums':{'beta_cycle':str(S),'outer_cycle':str(C)}}
