"""Exact signed-frequency T to F hull, independent of producer maps."""
from collections import defaultdict
from common import f64_units,units_array

def make_weights():
 H=[defaultdict(int) for _ in range(262)]
 for m in range(260):
  for frequency in (1+2*m,1-2*m,3+2*m,3-2*m):
   H[(abs(frequency)-1)//2][m]+=1 if frequency>0 else -1
 assert not H[261]
 result=[]
 for n in range(1,262):
  row=[]
  for k in range(8):
   weights=defaultdict(int)
   for j,factor in ((n-1,4-2*n),(n,4+2*n)):
    for m,value in H[j].items():
     weights[(k,m)]+=factor*value
     if k<7:weights[(k+1,m)]+=(k+1)*value
   row.append(tuple((j,m,w) for (j,m),w in sorted(weights.items()) if w))
  result.append(tuple(row))
 return tuple(result)
WEIGHTS=make_weights()

def check(arrays):
 Tm,Tr=units_array(arrays['T_mid']),units_array(arrays['T_rad']);count=0;minimum=None;worst=None
 for ni,row in enumerate(WEIGHTS):
  for k,weights in enumerate(row):
   lower=0;upper=0
   for j,m,w in weights:
    a,b=Tm[j][m]-Tr[j][m],Tm[j][m]+Tr[j][m]
    if w>=0:lower+=w*a;upper+=w*b
    else:lower+=w*b;upper+=w*a
   mid=f64_units(arrays['F_mid'][ni,k]);rad=f64_units(arrays['F_rad'][ni,k]);assert rad>=0
   gap=min(lower-16*(mid-rad),16*(mid+rad)-upper)
   assert gap>=0,('forcing linkage failed',ni+1,k)
   if minimum is None or gap<minimum:
    minimum=gap;worst={'n':ni+1,'k':k,'image_lo_units_over16':str(lower),'image_hi_units_over16':str(upper),'candidate_lo_units':str(mid-rad),'candidate_hi_units':str(mid+rad),'margin_units_over16':str(gap)}
   count+=1
 assert count==2088
 return {'count':count,'worst':worst}
