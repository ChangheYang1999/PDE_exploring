"""Lead floating experiment: remove the period-two (knot-scale) component of the B-spline coefficients of the
original trial in the fine-knot zone and estimate the effect on the weighted axis trace of the residual.
Filter: c_new = c - Delta^8 c / 256 (index differences, centred), applied to the control rows whose B-spline support
lies in [T0, T1]; this annihilates a sign-alternating sequence and changes a smooth sequence by O(h^8). The removed
part rho_alt = rho_0 - rho_new is a C^6 spline of the same space. To first order the axis trace of the residual changes
by the transport part g_alt = [r A_alt' + (D - r - 2 r') A_alt]/a_* (U[rho_alt].grad rho_0 is of lower order at the
knot scale and is neglected). Fifth central differences of g_alt use the stencil and step of axis_ratio.py, so
g5_new = g5_old - g5_alt at the same points. Not a certificate."""
import os,sys,time,json,types,bisect
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
sys.path.insert(0,'code/farres')
from fractions import Fraction as F
from math import comb
from flint import arb,ctx
import profile_points as PP
ctx.prec=160
G=PP.G;aa=G.aa
d=G.M.Data();G.check_hash(d);cache=G.load_cache(d);ell=1/aa(d.k);D=4*ell-1
T0,T1=F(1),F(7,2)
kn=d.knots;C=d.control;nr=len(C);nc=len(C[0])
alt=[[arb(0)]*nc for _ in range(nr)];rows_f=[]
for i in range(4,nr-4):
    if kn[i]>=T0 and kn[i+8]<=T1:
        rows_f.append(i)
        alt[i]=[sum(((-1)**k*comb(8,k)*C[i-4+k][m] for k in range(9)),arb(0))/256 for m in range(nc)]
ns=types.SimpleNamespace(knots=kn,control=alt)
dmax=max(abs(float(v.mid())) for i in rows_f for v in alt[i])
cmax=max(abs(float(v.mid())) for i in rows_f for v in C[i])
print('filtered rows',rows_f[0],rows_f[-1],len(rows_f),'max|removed coeff|',dmax,'max|coeff|',cmax,flush=True)
w=[-(-1)**j*(2*j+1)**2/2 for j in range(nc)]
Wc={}
def Aalt(t):
    sp=bisect.bisect_right(kn,t)-1
    if sp not in Wc:Wc[sp]=type(d).poly(ns,sp)
    W=Wc[sp];a,b=kn[sp:sp+2];h=aa(b-a);s=(aa(t)-aa(a))/h
    pv=[sum((W[j,m]*s**j for j in range(8)),arb(0)) for m in range(nc)]
    pd=[sum((W[j,m]*j*s**(j-1) for j in range(1,8)),arb(0))/h for m in range(nc)]
    return sum((wi*v for wi,v in zip(w,pv)),arb(0)),sum((wi*v for wi,v in zip(w,pd)),arb(0))
def galt(t):
    rh,drh,P,Q,Pt=PP.point(d,cache,t)
    r=ell-sum(((-1)**n*v for n,v in enumerate(P,1)),arb(0))
    rt=-sum(((-1)**n*v for n,v in enumerate(Pt,1)),arb(0))
    A,At=Aalt(t)
    tt=aa(t);astar=(aa(F(9,5))*tt).exp()*(1+tt.exp())**(-aa(F(53,10)))
    return (r*At+(D-r-2*rt)*A)/astar
hs=F(1,2**18)
def d5(t0):
    c={-3:-1,-2:4,-1:-5,1:5,2:-4,3:1}
    return sum((c[i]*galt(t0+i*hs) for i in c),arb(0))/(2*aa(hs)**5)
old=json.load(open('data/farres/axis_ratio.json'))
out=[];st=time.time()
for t,g5,q5,dax in old['rows']:
    if not (float(T0)+0.05<=t<=float(T1)-0.05):continue
    tf=F(t).limit_denominator(2**40)
    a5=float(d5(tf).mid())
    out.append([t,g5,a5,g5-a5])
    print('%.4f g5_old=%.3e g5_alt=%.3e g5_new=%.3e'%(t,g5,a5,g5-a5),round(time.time()-st),flush=True)
# seventh-derivative alternation of A before and after at a few spans
def A7(ctrl,sp):
    W=type(d).poly(types.SimpleNamespace(knots=kn,control=ctrl),sp);h=aa(kn[sp+1]-kn[sp])
    return float((sum((wi*W[7,m] for m,wi in enumerate(w)),arb(0))*5040/h**7).mid())
new=[[C[i][m]-alt[i][m] for m in range(nc)] if i in set(rows_f) else C[i] for i in range(nr)]
a7=[[sp,A7(C,sp),A7(new,sp)] for sp in (698,699,700,701,702,703)]
for r in a7:print('span',r[0],'A7 old %.3e new %.3e'%(r[1],r[2]))
json.dump({'filtered_rows':[rows_f[0],rows_f[-1]],'max_removed_coeff':dmax,'max_coeff':cmax,
           'columns':['t','g5_old','g5_alt','g5_new'],'rows':out,'A7_spans':a7},
          open('data/farres/axis_filter.json','w'),indent=1)
print('done',len(out),round(time.time()-st))
