"""Pure rational and containing-ball norms and quotient arithmetic."""
from flint import fmpq as Q,fmpq_poly,arb,arb_poly
from math import comb
CHECKS=0
BITS=192
def need(x,label=''):
 global CHECKS
 assert x,label
 CHECKS+=1
def pair(v):
 lo,hi=map(Q,v);need(lo<=hi);return lo,hi
def round_out(q,upper=False):
 q=Q(q);s=1<<BITS;v=q*s;n=-((-int(v.p))//int(v.q))if upper else int(v.p)//int(v.q);r=Q(n,s);need(r>=q if upper else r<=q);return r
def enclosure(lo,hi,nonnegative=False):
 need(lo<=hi)
 if nonnegative:lo=max(Q(0),lo);need(hi>=lo)
 return list(map(str,[round_out(lo),round_out(hi,True)]))
def reciprocal_integral(coefficients,c,h,K):
 need(len(coefficients)==K+1 and h>0)
 d0,d1,d2=1+4*c*c,8*c*h,4*h*h;v=[1/d0]
 for j in range(1,K+1):v.append((-d1*v[j-1]-(d2*v[j-2]if j>=2 else 0))/d0)
 weights=[Q(1,k+1)if k%2==0 else Q(0)for k in range(K+1)]
 convolution=fmpq_poly(v)*fmpq_poly(list(reversed(weights)));lo=hi=Q(0)
 for j,(a,b)in enumerate(coefficients):
  need(a<=b);alpha=2*h*convolution[K-j];lo+=alpha*(a if alpha>=0 else b);hi+=alpha*(b if alpha>=0 else a)
 need(lo<=hi);return lo,hi
def newton_integral(coefficients,c,h,K):
 need(len(coefficients)==K+1 and h>0);p=[]
 for a,b in coefficients:
  need(a<=b);v=arb(a).union(arb(b));need(v.lower().fmpq()<=a<=b<=v.upper().fmpq());p.append(v)
 D=arb_poly([arb(1+4*c*c),arb(8*c*h),arb(4*h*h)]);V=arb_poly([1/arb(1+4*c*c)]);n=1
 while n<K+1:
  m=min(2*n,K+1);V=(V*(arb_poly([2])-(D*V).truncate(m))).truncate(m);n=m
 identity=(D*V).truncate(K+1)
 for k in range(K+1):need(identity[k].contains(1 if k==0 else 0))
 quotient=(arb_poly(p)*V).truncate(K+1);finite=sum((quotient[k]/(k+1)for k in range(0,K+1,2)),arb(0))*arb(2*h);need(finite.is_finite());return finite.lower().fmpq(),finite.upper().fmpq()
def tensor_totals(regions,reverse=False):
 need(len(regions)==3);rows=range(2,-1,-1)if reverse else range(3);out=[[Q(0),Q(0)]for _ in range(4)]
 for i in rows:
  need(len(regions[i])==4)
  for j,row in enumerate(regions[i]):
   need(row['order']==j);lo,hi=pair([row['lower_exact'],row['upper_exact']]);need(lo>=0);out[j][0]+=lo;out[j][1]+=hi
 return out
def root_interval(lo,hi,power):
 need(0<=lo<=hi and power in [2,20]);l=arb(lo).root(power).lower().fmpq();u=arb(hi).root(power).upper().fmpq();l=max(Q(0),round_out(l));u=round_out(u,True);need(0<=l<=u and l**power<=lo<=hi<=u**power);return list(map(str,[l,u]))
def norms(tensors,reverse=False):
 need(len(tensors)==4);energies=[];integers=[]
 for k in range(4):
  order=range(k,-1,-1)if reverse else range(k+1)
  lo=sum((comb(k,j)*tensors[j][0]for j in order),Q(0));hi=sum((comb(k,j)*tensors[j][1]for j in range(k+1)),Q(0));need(0<=lo<=hi);energies.append((lo,hi));integers.append({'order':k,'energy_lower_exact':str(lo),'energy_upper_exact':str(hi),'norm_interval_exact':root_interval(lo,hi,2)})
 if energies[1][1]==0:
  need(all(lo==0 for lo,hi in energies));frac=['0','0']
 else:
  lower20=max(energies[2][0]**10,energies[2][0]**11/energies[1][1]);upper20=energies[2][1]**9*energies[3][1];need(lower20<=upper20);frac=root_interval(lower20,upper20,20)
 return {'tensor_energies':[{'order':j,'lower_exact':str(v[0]),'upper_exact':str(v[1])}for j,v in enumerate(tensors)],'integer_norms':integers,'fractional_order_exact':'21/10','fractional_norm_interval_exact':frac}
def outer(origin,exterior):
 ol,ou=pair(origin);tl,tu=pair(exterior);need(0<=ol and 0<=tl)
 return {'origin_energy_interval_exact':[str(ol/(1+Q(4,2500))),str(ou)],'exterior_energy_interval_exact':['0',str(tu/(1+4*10000**2))]}
def total_quotient(rows,regions,reverse=False):
 lo=hi=Q(0);items=list(rows)+list(regions.values());items=list(reversed(items))if reverse else items
 for values in items:
  l,u=pair(values);need(0<=l);lo+=l;hi+=u
 energy=enclosure(lo,hi,True);return {'energy_interval_exact':energy,'norm_interval_exact':root_interval(*pair(energy),2)}
