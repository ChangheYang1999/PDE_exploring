"""Finite exact polynomial, root-power and malformed-source fixtures."""
from pathlib import Path
from fractions import Fraction
from flint import fmpq as Q,fmpq_poly,ctx
import copy,time
import method_v01 as m
import independent_v01 as independent
import evidence_v01 as e
import publish_v01 as publish
CHECKS=0
def need(x):
 global CHECKS
 assert x
 CHECKS+=1
def reject(f):
 try:f()
 except (AssertionError,KeyError,ValueError,TypeError):need(True);return
 raise AssertionError('malformed fixture accepted')
def main():
 ctx.prec=1024
 # The weighted integrand is D(x)*P(x), so quotient integrals are exact polynomials.
 for K in [2,3,6,12,24]:
  for c,h in [(Q(1,10),Q(1,100)),(Q(2),Q(1,20)),(Q(9),Q(1,4))]:
   P=fmpq_poly([Q((-1)**j*(j+1),17)for j in range(K-1)]);D=fmpq_poly([1+4*c*c,8*c*h,4*h*h]);F=P*D;coeff=[(F[j],F[j])for j in range(K+1)]
   exact=2*h*sum((P[j]/(j+1)for j in range(0,K-1,2)),Q(0));lo,hi=m.reciprocal_integral(coeff,c,h,K);need(lo==hi==exact)
   lo,hi=m.newton_integral(coeff,c,h,K);need(lo<=exact<=hi)
   # Independent sign and endpoint checks with interval coefficients.
   width=Q(1,10**12);interval=[(a-width,b+width)for a,b in coeff];a,b=m.reciprocal_integral(interval,c,h,K);x,y=m.newton_integral(interval,c,h,K);need(a<=exact<=b and x<=exact<=y and max(a,x)<=min(b,y))
   reject(lambda:m.reciprocal_integral(interval[:-1],c,h,K))
   malformed=copy.deepcopy(interval);malformed[0]=(Q(1),Q(-1));reject(lambda:m.newton_integral(malformed,c,h,K))
 # Physically consistent tensor energies are moments of a positive frequency measure.
 for seed in range(1,13):
  regions=[]
  for region in range(3):
   values=[sum((Q(seed+k+region,1000)*(Q(k,3)**j)for k in range(1,5)),Q(0))for j in range(4)]
   regions.append([{'order':j,'lower_exact':str(v*Q(999,1000)),'upper_exact':str(v*Q(1001,1000))}for j,v in enumerate(values)])
  totals=m.tensor_totals(regions);value=m.norms(totals);need(independent.weighted(regions,value)['checks']>0)
  for j in range(4):
   bad=copy.deepcopy(value);bad['integer_norms'][j]['norm_interval_exact']=['0','0'];reject(lambda:independent.weighted(regions,bad))
  bad=copy.deepcopy(value);bad['fractional_norm_interval_exact']=['0','0'];reject(lambda:independent.weighted(regions,bad))
  bad=copy.deepcopy(value);bad['tensor_energies'][0]['upper_exact']='0';reject(lambda:independent.weighted(regions,bad))
  # Publication intersections remain containing and retain every order and energy.
  paired=publish.combine('weighted',{'values':value},{'values':copy.deepcopy(value)});need(paired==value)
  bad=copy.deepcopy(value);bad['integer_norms'][0]['energy_upper_exact']='999';reject(lambda:publish.combine('weighted',{'values':value},{'values':bad}))
  bad=copy.deepcopy(value);bad['fractional_order_exact']='2';reject(lambda:publish.combine('weighted',{'values':value},{'values':bad}))
  bad=copy.deepcopy(value);bad['integer_norms'].pop();reject(lambda:publish.combine('weighted',{'values':value},{'values':bad}))
 zero=[[{'order':j,'lower_exact':'0','upper_exact':'0'}for j in range(4)]for _ in range(3)];value=m.norms(m.tensor_totals(zero));need(independent.weighted(zero,value)['checks']>0 and value['fractional_norm_interval_exact']==['0','0'])
 # Exact114-panel publication, using declared synthetic local blocks.
 intervals=[]
 for i in range(114):
  intervals.append({'panel_index':i,'block':'synthetic_'+str(i//19),'local_index':i%19,'binding':{'path':'fixture/panel_'+str(i),'sha256':'a'*64},'order':4,'denominator_lower_exact':'3','remainder_upper_exact':'1/100000','energy_interval_exact':['1/1000','1/500']})
 regions={'origin_energy_interval_exact':['0','1/100'],'exterior_energy_interval_exact':['0','1/1000']};primary={'panels':intervals,'regions':regions};reduction=copy.deepcopy(primary)
 out=publish.combine('unweighted',primary,reduction);need(independent.unweighted(out['panels'],out['regions'],out['values'])['checks']>0)
 for key,bad_value in [('panel_index',1),('block','wrong'),('local_index',1),('binding',{}),('order',5),('denominator_lower_exact','4'),('remainder_upper_exact','0'),('energy_interval_exact',['2','3'])]:
  bad=copy.deepcopy(reduction);bad['panels'][0][key]=bad_value;reject(lambda:publish.combine('unweighted',primary,bad))
 bad=copy.deepcopy(reduction);bad['panels'].pop();reject(lambda:publish.combine('unweighted',primary,bad))
 bad=copy.deepcopy(reduction);bad['regions']['origin_energy_interval_exact']=['0','0'];reject(lambda:publish.combine('unweighted',primary,bad))
 reject(lambda:publish.combine('wrong',primary,reduction))
 regions=m.outer(['1/3','2/3'],['1/10','3/10']);value=m.total_quotient([['1/10','1/9'],['1/11','1/8']],regions);need(independent.unweighted([['1/10','1/9'],['1/11','1/8']],regions,value)['checks']>0)
 for n in ['/absolute','../outside','a/../b','']:reject(lambda:e.local(n))
 for path in(e.BASE/'code').glob('*.py'):compile(path.read_text(),str(path.relative_to(e.ROOT)),'exec');need(True)
 return CHECKS
if __name__=='__main__':
 start,tick=e.stamp(),time.monotonic();n=main();e.put(e.BASE/'verification/fixtures_v01.json',{'status':'PASS','started_utc':start,'finished_utc':e.stamp(),'elapsed_seconds':time.monotonic()-tick,'checks':n,'method_assertions':m.CHECKS,'independent_assertions':independent.CHECKS,'scope':'Synthetic quotient, energy and root-power checks only. Actual source admission not replaced.'});print('PASS',n,m.CHECKS,independent.CHECKS,flush=True)
