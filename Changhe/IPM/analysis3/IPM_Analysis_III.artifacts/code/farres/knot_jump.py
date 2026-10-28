"""Cross-check of V198: one-sided t-derivatives of the vertical-axis cofactor of the original trial at knot 700.
The cofactor at theta=pi/2 of H=sum_j h_j sin((2j+1)theta) is A=-sum_j (-1)^j (2j+1)^2 h_j/2. Interval arithmetic on
the exact B-spline polynomials of the two neighbouring spans."""
import sys
sys.path.insert(0,'data/farres')
import profile_points as PP
from flint import arb
from math import factorial
d=PP.G.M.Data();PP.G.check_hash(d);aa=PP.aa;kn=d.knots
def der(span,order,s):
    W=d.poly(span);a,b=kn[span:span+2];h=aa(b-a)
    return [sum((W[j,m]*(factorial(j)//factorial(j-order))*s**(j-order) for j in range(order,8)),arb(0))/h**order for m in range(W.ncols())]
w=[-(-1)**j*(2*j+1)**2/2 for j in range(262)]
print('knot 700 =',kn[700],float(kn[700]))
for order in range(8):
    L=der(699,order,arb(1));R=der(700,order,arb(0))
    AL=sum((wi*v for wi,v in zip(w,L)),arb(0));AR=sum((wi*v for wi,v in zip(w,R)),arb(0))
    print(order,'left',AL.str(6),'right',AR.str(6),'jump',(AR-AL).str(6))
