"""Outward positive Stieltjes lower sums for a normalized projection cusp, with exact profile scaling and first- and
second-order mean-value rules for the cell masses.

Lead variant (v7) of the verifier's certify_axis_projection_stieltjes_v2.py (local copy cert_v2_copy.py). The witness,
the strip and ratio grids, the kernel endpoint rule and the positive-part rule are those of v2; cert_v4.py is v7 without
rules (c), (d), (e) and (f), cert_v5.py is v7 without (d), (e), (f), cert_v6.py is v7 without (e), (f). In strip i (d in [d_l, d_r], X = 1/2 + sign d) the cell between the ratio nodes v_j < v_j+1 receives the bound
max(c_v2, c_v4, c_mv, c_mv2) over the finite candidates (no bound if none), replaced by 0 if negative, times the smaller endpoint value of the kernel. Each of the four is a
lower bound for F(d) = f(X, d v_j) - f(X, d v_j+1) for every d in the strip, so the maximum is one as well:

(a) c_v2: the lower endpoint of the ball enclosure of F on the strip ball (v2).
(b) c_v4: if at both nodes the enclosures over the strip give Pr < G, Pr < h, Pr > -h, then F(d) = d^alpha (p_j - p_j+1)/K
    with p(v) = P(1, v), and c_v4 = d_l^alpha (p_j - p_j+1)/K if p_j >= p_j+1 (P is homogeneous of degree alpha and even in
    each variable, so P(X - 1/2, d v) = d^alpha p(v)). Here G = g + shift, Pr = -1/2 + P/K and h = 2^(alpha-1) X^alpha.
(c) c_mv (mean value). At each node the active branch of f = max(-h, min(h, min(G, Pr))) is determined, if possible, by
    certain comparisons of the strip enclosures: Pr (profile), G (distance branch), h or -h. For the distance branch it is
    also required that the side of the graph (sigma = +1 or -1) is certain, that one of the four pieces of the zero set
    (the axis X = 0, the segment from (0, 1/2) to (1/2, 0), the segment from (1/2, 0) to (1/2 + b, b), the ray from
    (1/2 + b, b) in direction (sqrt 3, 1)) is certainly nearer than the other three, and that its distance is certainly
    positive. The distance to a closed convex set is C^1 off the set, with gradient (z - proj z)/dist, so on the strip
    t -> f(1/2 + sign t, t v_j) is C^1 with derivative enclosed by the chain rule (direction (sign, v_j)):
      profile: alpha t^(alpha-1) p_j / K;  distance: sigma 2^(alpha-1) alpha dist^(alpha-1) <grad dist, (sign, v_j)>;
      +-h: +-2^(alpha-1) alpha X^(alpha-1) sign.
    If both nodes have a branch, F is C^1 on the strip with F' in the difference E of the two enclosures, and for every d
    in the strip F(d) >= F(d_m) - |E| |d - d_m| with d_m = (d_l + d_r)/2, so c_mv = lo(F(d_m)) - hi(|E|) (d_r - d_l)/2,
    with F(d_m) enclosed by evaluating the witness at the point d_m.
(d) c_mv2 (second order, v6). Under the conditions of (c), t -> f(1/2 + sign t, t v_j) is C^{1,1} on the strip, with second
    derivative a.e. in the enclosure
      profile: alpha(alpha-1) t^(alpha-2) p_j / K;  +-h: +-2^(alpha-1) alpha(alpha-1) X^(alpha-2);
      distance: sigma 2^(alpha-1) [alpha(alpha-1) r^(alpha-2) <grad r, w>^2 + alpha r^(alpha-1) w^T H w], w = (sign, v_j),
    where w^T H w = 0 for the axis piece and for a segment or ray piece whose projection parameter is certainly interior,
    and otherwise w^T H w is enclosed by [0, (|w|^2 - <grad r, w>^2)/r] (the distance r to a closed convex set is C^{1,1}
    off the set, with 0 <= D^2 r <= (I - grad r grad r^T)/r a.e.). Taylor's formula with integral remainder gives
    F(d) >= F(d_m) - |F'(d_m)| |d - d_m| - sup|F''| |d - d_m|^2/2, so c_mv2 = lo(F(d_m)) - hi|F'(d_m)| hw - hi|F''| hw^2/2,
    hw = (d_r - d_l)/2, where F'(d_m) is enclosed at the point d_m (the branch certified on the strip is also the branch at d_m).
(e) Powers of balls touching 0 (v7). In v2, x^alpha for a ball x with lower endpoint 0 (the distance near the zero set,
    X near 0) is evaluated as exp(alpha log x) and gives nan, so the cell received no bound. Here x^alpha is enclosed by
    [0, hi(x)^alpha] when x is not certainly positive (x^alpha is nondecreasing on [0, oo) and x >= 0).
(f) Refinement (v7). If a cell has no finite candidate or its best candidate is c_v2, the strip is split into M equal
    subintervals [e_k, e_k+1] and the cell receives instead max(best, min_k c_v2(k)), where c_v2(k) is the lower endpoint of
    the ball enclosure of F on the ball of the k-th subinterval. Since every d of the strip lies in one subinterval,
    min_k c_v2(k) is a lower bound for F on the strip.
Strips: d in [exp(left), exp(right)] split into nx equal log-strips; for sign -1 the default right end is log(1/2) and a
given rational right end must be <= log(1/2) (X > 0). Different (left, right) pieces of one sign are disjoint sets of strips.
The kernel V(X, Y) = X Y/(pi((X-1/2)^2+Y^2)((X+1/2)^2+Y^2)) is evaluated as X v/(pi d (1+v^2)((X+1/2)^2+d^2 v^2)) on
the strip ball; as in v2 its minimum over a cell is bounded by the smaller endpoint value."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,json,hashlib,time
from flint import arb,ctx
ctx.prec=192;A=arb(1)/2;RT3=arb(3).sqrt();PI=arb.pi();ROOT=Path('the verification work')
def aa(v):
 q=F(v);return arb(q.numerator)/q.denominator
def lo(v):return arb(v.lower())
def hi(v):return arb(v.upper())
def positive(v):return arb.max(arb(0),v)
def distance(X,Y,x0,y0,dx,dy,ray=False):
 t=((X-x0)*dx+(Y-y0)*dy)/(dx*dx+dy*dy)
 if t>=0 and (ray or t<=1):return abs((X-x0)*dy-(Y-y0)*dx)/(dx*dx+dy*dy).sqrt()
 t=positive(t) if ray else arb.min(arb(1),positive(t))
 return ((X-x0-t*dx)**2+(Y-y0-t*dy)**2).sqrt()
def seg_grad(X,Y,x0,y0,dx,dy,ray=False):
 """(dist, gx, gy): distance to the segment (or ray) and an enclosure of its gradient (z - proj z)/dist, or None."""
 t0=((X-x0)*dx+(Y-y0)*dy)/(dx*dx+dy*dy);t=positive(t0) if ray else arb.min(arb(1),positive(t0))
 ux=X-x0-t*dx;uy=Y-y0-t*dy;r=(ux*ux+uy*uy).sqrt()
 if not r>0:return None
 return r,ux/r,uy/r,bool(t0>0 and (ray or t0<1))
def profile_unit(v,alpha):
 r=(1+v*v).sqrt();E=(1-v*v)/r
 return positive((r**alpha+positive(E)**alpha-positive(-E)**alpha)/2)
def ppow(x,a):
 """Enclosure of x^a (0 < a) for a ball x of nonnegative numbers."""
 if x>0:return x**a
 u=hi(x);return arb(0).union(u**a) if u>0 else arb(0)
def branches(drad,v,pv,sign,alpha,b,shift,K):
 """(G, Pr, h) at X = 1/2 + sign drad, Y = drad v; the same formulas as witness() of v2."""
 X=positive(A+sign*drad);Y=drad*v
 d=arb.min(X,distance(X,Y,arb(0),A,A,-A))
 d=arb.min(d,distance(X,Y,A,arb(0),b,b))
 d=arb.min(d,distance(X,Y,A+b,b,RT3,arb(1),True))
 B=arb.max(A-X,arb.min(X-A,(X-A+(RT3-1)*b)/RT3));c=2**(alpha-1);h=c*ppow(X,alpha);power=c*ppow(positive(d),alpha)
 if Y<B:g=power
 elif Y>B:g=-power
 else:g=(-hi(power)).union(hi(power))
 return g+shift,-A+drad**alpha*pv/K,h
def value(G,Pr,h):return arb.max(-h,arb.min(h,arb.min(G,Pr)))
def is_profile(G,Pr,h):return Pr.upper()<G.lower() and Pr.upper()<h.lower() and Pr.lower()>(-h).upper()
def derivatives(drad,v,pv,sign,alpha,b,shift,K,br):
 """Enclosures (f', f'') of the first and (a.e.) second derivative of t -> f(1/2 + sign t, t v) on the ball drad, or None."""
 G,Pr,h=br;X=positive(A+sign*drad);c=2**(alpha-1);s=arb(sign)
 if is_profile(G,Pr,h):return alpha*drad**(alpha-1)*pv/K,alpha*(alpha-1)*drad**(alpha-2)*pv/K
 m=arb.min(G,Pr)
 if h<m:return c*alpha*X**(alpha-1)*s,c*alpha*(alpha-1)*X**(alpha-2)
 if (G<-h) or (Pr<-h):return -c*alpha*X**(alpha-1)*s,-c*alpha*(alpha-1)*X**(alpha-2)
 if not (G<Pr and G<h and G>-h and X>0):return None
 Y=drad*v;B=arb.max(A-X,arb.min(X-A,(X-A+(RT3-1)*b)/RT3))
 if Y<B:sigma=1
 elif Y>B:sigma=-1
 else:return None
 pieces=[(X,arb(1),arb(0),True),seg_grad(X,Y,arb(0),A,A,-A),seg_grad(X,Y,A,arb(0),b,b),seg_grad(X,Y,A+b,b,RT3,arb(1),True)]
 if any(q is None for q in pieces):return None
 near=[k for k in range(4) if all(pieces[k][0]<pieces[l][0] for l in range(4) if l!=k)]
 if len(near)!=1:return None
 r,gx,gy,flat=pieces[near[0]];gw=gx*s+gy*v
 if flat:hw2=arb(0)
 else:hw2=arb(0).union(hi(positive((1+v*v-gw*gw)/r)))
 return sigma*c*alpha*r**(alpha-1)*gw,sigma*c*(alpha*(alpha-1)*r**(alpha-2)*gw*gw+alpha*r**(alpha-1)*hw2)
def Vs(X,drad,v):
 return X*v/(PI*drad*(1+v*v)*((X+A)**2+drad*drad*v*v))
def safe(v):
 k=int((lo(v)*10**10).floor().unique_fmpz());return f'{k//10**10}.{k%10**10:010d}'
def main():
 p=argparse.ArgumentParser();p.add_argument('--alpha',required=True);p.add_argument('--b',required=True);p.add_argument('--shift',required=True);p.add_argument('--K',required=True);p.add_argument('--sign',type=int,choices=[-1,1],required=True);p.add_argument('--nx',type=int,default=4096);p.add_argument('--ny',type=int,default=512);p.add_argument('--start',type=int,default=0);p.add_argument('--stop',type=int);p.add_argument('--left',default='-18');p.add_argument('--right',default=None);p.add_argument('--vleft',default='-12');p.add_argument('--vright',default='14');p.add_argument('--refine',type=int,default=8);p.add_argument('--out',required=True);args=p.parse_args()
 alpha,b,t,K=map(aa,[args.alpha,args.b,args.shift,args.K]);assert 0<alpha<1 and b>0 and t>=-A and K>=1
 stop=args.stop if args.stop is not None else args.nx;assert 0<=args.start<stop<=args.nx
 left=aa(args.left);right=(A.log() if args.sign==-1 else aa(24)) if args.right is None else aa(args.right)
 if args.sign==-1:assert args.right is None or right<=A.log()
 vl=aa(args.vleft);vr=aa(args.vright)
 assert left<right and vl<vr;du=(right-left)/args.nx;dv=(vr-vl)/args.ny;ve=[(vl+j*dv).exp() for j in range(args.ny+1)]
 pv=[profile_unit(v,alpha) for v in ve];dp=[pv[j]-pv[j+1] for j in range(args.ny)]
 total=arb(0);positive_cells=0;counts=dict(v2=0,v4=0,mv=0,mv2=0,ref=0);started=time.monotonic()
 for i in range(args.start,stop):
  dl=(left+i*du).exp();dr=(left+(i+1)*du).exp();d=dl.union(dr);X=A+args.sign*d
  X=positive(X);width=positive(lo(dr-dl));dla=lo(dl**alpha);dm=(dl+dr)/2;hw=hi((dr-dl)/2)
  br=[branches(d,v,q,args.sign,alpha,b,t,K) for v,q in zip(ve,pv)];prof=[is_profile(*x) for x in br];vals=[value(*x) for x in br]
  der=[derivatives(d,v,q,args.sign,alpha,b,t,K,x) for v,q,x in zip(ve,pv,br)]
  bm=[branches(dm,v,q,args.sign,alpha,b,t,K) for v,q in zip(ve,pv)];mid=[value(*x) for x in bm]
  dmid=[derivatives(dm,v,q,args.sign,alpha,b,t,K,x) if y is not None else None for v,q,x,y in zip(ve,pv,bm,der)]
  vv=[Vs(X,d,v) for v in ve];row=arb(0);subs=None
  for j in range(args.ny):
   cand=[(lo(vals[j]-vals[j+1]),'v2')]
   if prof[j] and prof[j+1] and dp[j]>=0:cand.append((lo(dla*dp[j]/K),'v4'))
   if der[j] is not None and der[j+1] is not None:
    cand.append((lo(mid[j]-mid[j+1])-hi(abs(der[j][0]-der[j+1][0]))*hw,'mv'))
    if dmid[j] is not None and dmid[j+1] is not None:
     cand.append((lo(mid[j]-mid[j+1])-hi(abs(dmid[j][0]-dmid[j+1][0]))*hw-hi(abs(der[j][1]-der[j+1][1]))*hw*hw/2,'mv2'))
   cand=[z for z in cand if z[0].is_finite()]
   best=max(cand,key=lambda z:z[0].upper()) if cand else None
   if args.refine>1 and (best is None or best[1]=='v2'):
    if subs is None:
     e=[dl+(dr-dl)*k/args.refine for k in range(args.refine)]+[dr];subs=[e[k].union(e[k+1]) for k in range(args.refine)]
    r=None
    for sb in subs:
     z=lo(value(*branches(sb,ve[j],pv[j],args.sign,alpha,b,t,K))-value(*branches(sb,ve[j+1],pv[j+1],args.sign,alpha,b,t,K)))
     r=z if r is None else arb.min(r,z)
     if not (r.is_finite() and (best is None or r>best[0])):break
    if r.is_finite() and (best is None or r>best[0]):best=(r,'ref')
   if best is None:continue
   mass=positive(best[0])
   kernel=positive(arb.min(lo(vv[j]),lo(vv[j+1])))
   if mass>0 and kernel>0:positive_cells+=1;counts[best[1]]+=1;row+=mass*kernel
  assert row.is_finite() and row>=0;total+=row*width
  if i%256==0:print(i,stop,round(time.monotonic()-started,2),safe(1+4*total),flush=True)
 paths=[Path(__file__),ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md',ROOT/'11_lattice_pole_constraints/monotone_axis/PROOF.md',ROOT/'07_diagonal_identity_term/full_range_profile/PROOF.md']
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(F(args.alpha)),b=str(F(args.b)),shift=str(F(args.shift)),K=str(F(args.K)),sign=args.sign,nx=args.nx,ny=args.ny,start=args.start,stop=stop,left=args.left,right=('log(1/2)' if args.sign==-1 else '24') if args.right is None else args.right,vleft=args.vleft,vright=args.vright,precision_bits=ctx.prec,positive_cells=positive_cells,rule_counts=counts,integral_lower_enclosure=total.str(55,more=True),safe_partial_D_lower=safe(1+4*total),elapsed_seconds=time.monotonic()-started,source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Partial positive lower sum (v7: exact profile scaling, first- and second-order mean-value cell rules, safe powers, refinement of v2 cells); K must have a separately verified global profile certificate.')
 out=Path(args.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
