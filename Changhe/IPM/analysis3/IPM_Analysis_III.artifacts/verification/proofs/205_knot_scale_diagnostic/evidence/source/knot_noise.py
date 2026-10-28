"""Floating diagnostic: span-wise seventh t-derivative of the vertical-axis cofactor A of the original trial
(A=-sum_j (-1)^j (2j+1)^2 h_j/2), in several t ranges, to see whether the knot-scale structure alternates in sign."""
import sys,json
sys.path.insert(0,'data/farres')
import profile_points as PP
from flint import arb
from math import factorial
d=PP.G.M.Data();aa=PP.aa;kn=d.knots
w=[-(-1)**j*(2*j+1)**2/2 for j in range(262)]
def A_der(span,order,s):
    W=d.poly(span);a,b=kn[span:span+2];h=aa(b-a)
    tot=arb(0)
    for m in range(W.ncols()):
        v=sum((W[j,m]*(factorial(j)//factorial(j-order))*s**(j-order) for j in range(order,8)),arb(0))
        tot+=w[m]*v
    return float((tot/h**order).mid())
rows=[]
spans=sorted(d.spans)
for lo in (700,1100,1500):
    for sp in range(lo-6,lo+6):
        if sp not in spans: continue
        a,b=kn[sp:sp+2]
        rows.append(dict(span=sp,t=float(a),h=float(b-a),A=A_der(sp,0,arb(0)),A5=A_der(sp,5,arb(0.5)),A6=A_der(sp,6,arb(0.5)),A7=A_der(sp,7,arb(0.5))))
        r=rows[-1];print(r['span'],'%.4f %.2e A=%.4e A5=%.3e A6=%.3e A7=%.3e'%(r['t'],r['h'],r['A'],r['A5'],r['A6'],r['A7']),flush=True)
json.dump(rows,open('data/farres/knot_noise.json','w'),indent=1)
