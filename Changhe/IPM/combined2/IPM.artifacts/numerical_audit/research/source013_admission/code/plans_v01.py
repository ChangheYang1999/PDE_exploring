"""Exact partition and independent containing arithmetic for startup plans."""
from math import factorial
from flint import arb,fmpq as Q,ctx
TAU=[Q(1,10**18),Q(1,10**16),Q(1,10**14),Q(1,10**12)]
def geometry():
 start=Q(1,50);right=Q(10000);rows=[]
 while start<right:
  end=min(2*start,right);width=(end-start)/6
  for i in range(6):
   a,b=start+i*width,start+(i+1)*width;rows.append(((a+b)/2,(b-a)/2))
  start=end
 assert len(rows)==114
 return rows

def check_row(row,index,M):
 c,h=geometry()[index];r=row['request'];D1,D2=c/5,c/4
 assert row['parent_index']==index and row['policy']=='six_per_doubling'
 assert row['all_analytic_remainders_within_budget']is True
 assert r=={'center_exact':str(c),'half_width_exact':str(h),'inner_disk_exact':str(D1),'outer_disk_exact':str(D2),'sigma_exact':'1','r0_exact':'1/2','order':row['order']}
 K=row['order'];assert type(K)is int and 48<=K<=2048
 assert type(M)is int and M>=0 and M%2==0
 assert 0<h<D1<D2<c and Q(1,4)+c*c-2*c*D2-D2*D2>0
 BF=Q(row['source_majorant_upper_exact']);assert BF>0
 H=list(map(Q,row['integrand_majorant_upper_exact']));errors=list(map(Q,row['remainder_upper_exact']))
 assert len(H)==len(errors)==4 and list(map(Q,row['tolerances_exact']))==TAU
 coefficients=[[1],[M,1],[M*(M+2),2*M+1,1],[M*(M+2)*(M+4),3*M*M+9*M+3,3*M+3,1]]
 # sigma=1 and r0=1/2; this rearrangement avoids the producer's general powers.
 Bg=arb(BF)*2*(arb(Q(1,4)+(c+D2)**2)).sqrt()
 for j,weights in enumerate(coefficients):
  multiplier=sum((Q(v)*(c-D1)**(ell-j)*factorial(ell)/(D2-D1)**ell for ell,v in enumerate(weights)),Q(0))
  bound=2*arb.pi()*arb(c+D1)*(2**j)*(Bg*arb(multiplier))**2
  assert bound.is_finite() and 0<bound.upper().fmpq()<=H[j]
  q=h/D1;exact=2*h*H[j]*q**(K+1)/(1-q)
  assert exact==errors[j] and 0<=exact<=TAU[j]
  if K>48:assert any(v/q>tau for v,tau in zip(errors,TAU))
 return r,errors

def verify(first,second):
 assert first['job']=='planner_a' and second['job']=='planner_b'
 assert first['source']==second['source'] and first['center']==second['center']
 assert first['safe_structural_bandwidth']==second['safe_structural_bandwidth']
 M=first['safe_structural_bandwidth'];rows={};totals=[Q(0)]*4
 old=ctx.prec;ctx.prec=1536
 try:
  for result,parity in [(first,0),(second,1)]:
   assert [row['parent_index']for row in result['rows']]==list(range(parity,114,2))
   assert result['majorant_calibration']['overlap']is True
   for row in result['rows']:
    i=row['parent_index'];request,errors=check_row(row,i,M);assert i not in rows;rows[i]=request
    totals=[a+b for a,b in zip(totals,errors)]
  assert sorted(rows)==list(range(114)) and all(a<=114*b for a,b in zip(totals,TAU))
 finally:ctx.prec=old
 return {'panels':[rows[i]for i in range(114)],'safe_structural_bandwidth':M,'analytic_remainder_totals_exact':list(map(str,totals)),'all_114_indices_once':True}
