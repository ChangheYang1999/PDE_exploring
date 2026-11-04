"""Independent Fraction implementation of endpoint power and sum checks."""
from fractions import Fraction as Q
from math import comb
CHECKS=0
def need(x):
 global CHECKS
 assert x
 CHECKS+=1
def pair(v):
 lo,hi=map(Q,v);need(0<=lo<=hi);return lo,hi
def powers(interval,lo,hi,power):
 l,u=pair(interval);need(l**power<=lo<=hi<=u**power)
def weighted(regions,saved):
 levels=[];need(len(regions)==3 and len(saved['tensor_energies'])==4)
 for j in range(4):
  lo=hi=Q(0)
  for rows in reversed(regions):
   need(len(rows)==4 and rows[j]['order']==j);a,b=pair([rows[j]['lower_exact'],rows[j]['upper_exact']]);lo+=a;hi+=b
  s=saved['tensor_energies'][j];need(s['order']==j and pair([s['lower_exact'],s['upper_exact']])==(lo,hi));levels.append((lo,hi))
 energies=[];need(len(saved['integer_norms'])==4)
 for k in range(4):
  lo=sum((Q(comb(k,j))*levels[j][0]for j in range(k,-1,-1)),Q(0));hi=sum((Q(comb(k,j))*levels[j][1]for j in range(k,-1,-1)),Q(0));s=saved['integer_norms'][k]
  need(s['order']==k and pair([s['energy_lower_exact'],s['energy_upper_exact']])==(lo,hi));powers(s['norm_interval_exact'],lo,hi,2);energies.append((lo,hi))
 need(saved['fractional_order_exact']=='21/10')
 if energies[1][1]==0:need(all(l==0 for l,h in energies)and saved['fractional_norm_interval_exact']==['0','0'])
 else:powers(saved['fractional_norm_interval_exact'],max(energies[2][0]**10,energies[2][0]**11/energies[1][1]),energies[2][1]**9*energies[3][1],20)
 return {'checks':CHECKS,'tensor_and_integer_sums_exact':True,'norm_powers_exact':True}
def unweighted(rows,regions,saved):
 lo=hi=Q(0)
 for values in list(reversed(rows))+list(reversed(list(regions.values()))):
  l,u=pair(values);lo+=l;hi+=u
 l,u=pair(saved['energy_interval_exact']);need(l<=lo<=hi<=u);powers(saved['norm_interval_exact'],l,u,2)
 return {'checks':CHECKS,'energy_sum_contained':True,'norm_powers_exact':True}
