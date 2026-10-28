"""Floating scan of the period-two (knot-scale) component of the original trial over all spline spans.
On each span the trial is a degree-7 polynomial, so the seventh t-derivative of each sine mode h_j is constant there:
D7_j(i). For consecutive spans i, i+1 the alternating part (D7_j(i) - D7_j(i+1))/2 times (h/pi)^7 estimates the
amplitude of a period-two component (a pure such component has k-th derivative (pi/h)^k times its amplitude).
Reported for mode 0, the vertical-axis cofactor A=-sum_j (-1)^j (2j+1)^2 h_j/2, and the maximum over modes."""
import sys,json,math,time
sys.path.insert(0,'data/farres')
import profile_points as PP
from flint import arb
d=PP.G.M.Data();PP.G.check_hash(d);aa=PP.aa;kn=d.knots
w=[-(-1)**j*(2*j+1)**2/2 for j in range(262)]
spans=sorted(d.spans);rows=[];st=time.time()
prev=None
for sp in spans:
    W=d.poly(sp);a,b=kn[sp:sp+2];h=float(b-a);nc=W.ncols()
    D7=[float(W[7,m].mid())*5040/h**7 for m in range(nc)]
    V=[float(sum((W[j,m]*arb(0.5)**j for j in range(8)),arb(0)).mid()) for m in range(nc)]
    A7=sum(wi*v for wi,v in zip(w,D7));A=sum(wi*v for wi,v in zip(w,V))
    cur=dict(span=sp,t=float(a),h=h,A=A,A7=A7,D7=D7,V=V)
    if prev is not None and abs(prev['h']-h)<0.2*h:
        f=(h/math.pi)**7
        alt=[abs(x-y)/2*f for x,y in zip(prev['D7'],D7)]
        jm=max(range(nc),key=lambda m:alt[m])
        rows.append(dict(span=sp,t=cur['t'],h=h,A=A,altA=abs(prev['A7']-A7)/2*f,smA7=(prev['A7']+A7)/2,alt0=alt[0],v0=V[0],
                         altmax=alt[jm],jmax=jm,vmax=max(abs(v) for v in V)))
    prev=cur
    if sp%100==0:print(sp,round(time.time()-st),flush=True)
json.dump(rows,open('data/farres/knot_scan.json','w'))
print('done',len(rows),round(time.time()-st))
