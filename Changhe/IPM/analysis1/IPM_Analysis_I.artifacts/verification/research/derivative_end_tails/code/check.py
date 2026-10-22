"""Full positive coefficient audit and two distinct rigorous tail integrations."""
from common import *
from fractions import Fraction as F
from math import comb, factorial
import time,resource
import flint,mpmath
from flint import arb,ctx,fmpq,fmpq_poly
from mpmath import iv
ctx.prec=512;ctx.threads=1;iv.dps=200
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
K=F(1615536043799051,9007199254740992);L=F(8614738245908811,1125899906842624)
A=F(-685794559684773,140737488355328);BETA0=F(2289893859708677,281474976710656)
BI=F(3518437208883275,70368744177664);OMEGA=1043;NU=521;M=522

def aq(v):
 v=F(v);return arb(v.numerator)/v.denominator

def iq(v):
 v=F(v);return iv.mpf(v.numerator)/v.denominator

def fq(v):
 v=F(v);return fmpq(v.numerator,v.denominator)

def ff(v):return F(str(v))

def ae(x):
 def dy(z):
  m,e=z.man_exp();return F(int(m))*F(2)**int(e)
 need(x.is_finite(),'finite Arb output');return dy(x.lower()),dy(x.upper())

def ie(x):
 def dy(z):
  s,m,e,b=z;need(b>=0,'finite interval output');return (-1 if s else 1)*F(int(m))*F(2)**int(e)
 return tuple(dy(z) for z in x._mpi_)

def enc(x,engine):
 l,h=(ae if engine=='arb512' else ie)(x);need(l<=h,'ordered output');return {'lower_exact':str(l),'upper_exact':str(h)}

def checked_bound(v):
 # Every stored interval is checked against the actual dyadic ball, whose
 # outward lower()/upper() endpoints can be wider than its exact mid-radius.
 lo,hi=F(v['lower_exact']),F(v['upper_exact']);z=v['ball'];need(z['schema']=='arb-dyadic-mid-radius-v1','ball schema')
 mid=F(z['mid_m'])*F(2)**int(z['mid_e']);rad=F(z['rad_m'])*F(2)**int(z['rad_e'])
 need(rad>=0 and lo<=mid-rad<=mid+rad<=hi and hi>=0,'nonnegative bound and outward endpoints')
 return max(F(0),lo),hi

def add_interval(x,y):return x[0]+y[0],x[1]+y[1]

def convolve_interval(x,y):
 z=[(F(0),F(0)) for _ in range(len(x)+len(y)-1)]
 for i,a in enumerate(x):
  for j,b in enumerate(y):z[i+j]=add_interval(z[i+j],(a[0]*b[0],a[1]*b[1]))
 return z

def lineage(o):
 ds=o['density_sums'];need(len(ds)==11 and len(o['green'])==261,'entire outer constituents');rates=[F(v['beta_exact']) for v in ds]
 need(rates[0]==K and rates[-1]<-117,'outer rates')
 table={};read=0
 for i,row in enumerate(ds):
  table[i]={}
  for key in ('P','Q','D','E','L'):
   z=[checked_bound(x) for x in row[key]];need(len(z)==(1 if i<10 else 7),'whole outer polynomial');table[i][key]=z;read+=len(z)
 trans=[]
 for n,row in enumerate(o['green'],1):
  need(row['n']==n,'all ordered transient modes');trans.append((F(-2*n-2),checked_bound(row['transient_velocity_coefficient'])));read+=1
 C={};D={};blocks=0
 def acc(rate,values):
  need(rate<=2*K-1<0,'strict negative exterior residual rate')
  if rate not in C:C[rate]=[]
  if len(C[rate])<len(values):C[rate]+=[(F(0),F(0))]*(len(values)-len(C[rate]))
  for i,v in enumerate(values):C[rate][i]=add_interval(C[rate][i],v)
 def pacc(rate,lo,hi):
  if rate not in D:D[rate]=(fmpq_poly([]),fmpq_poly([]))
  D[rate]=(D[rate][0]+lo,D[rate][1]+hi)
 def poly(values,side):return fmpq_poly([fq(v[side]) for v in values])
 for i in range(1,11):
  vals=table[i]['L'];acc(rates[i],vals);pacc(rates[i],poly(vals,0),poly(vals,1))
 for i in range(11):
  for j in range(11):
   u=convolve_interval(table[i]['P'],table[j]['D']);v=convolve_interval(table[i]['Q'],table[j]['E']);g=rates[i]+rates[j]-1
   acc(g,[add_interval(x,y) for x,y in zip(u,v)])
   pacc(g,poly(table[i]['P'],0)*poly(table[j]['D'],0)+poly(table[i]['Q'],0)*poly(table[j]['E'],0),poly(table[i]['P'],1)*poly(table[j]['D'],1)+poly(table[i]['Q'],1)*poly(table[j]['E'],1));blocks+=1
 for rate,tr in trans:
  for j in range(11):
   u=[add_interval(x,y) for x,y in zip(table[j]['D'],table[j]['E'])];g=rate+rates[j]
   acc(g,[(tr[0]*x[0],tr[1]*x[1]) for x in u]);pacc(g,fq(tr[0])*(poly(table[j]['D'],0)+poly(table[j]['E'],0)),fq(tr[1])*(poly(table[j]['D'],1)+poly(table[j]['E'],1)));blocks+=1
 need(blocks==2992 and len(C)==len(D)==1864 and len(o['majorant'])==1864,'whole exterior product family')
 safe={};coeffs=0;max_ratio=F(1);rows=[]
 for row in o['majorant']:
  g=F(row['gamma_exact']);need(g in C and g not in safe,'unique saved exponent');safe[g]=[];need(len(C[g])==len(row['coefficients']),'entire saved polynomial')
  for l,old in enumerate(row['coefficients']):
   saved=checked_bound(old);lo,hi=C[g][l]
   need((ff(D[g][0][l]),ff(D[g][1][l]))==(lo,hi),'independent Fraction/fmpq lineage identity')
   need(max(lo,saved[0])<=min(hi,saved[1]),'overlap with accepted coefficient interval')
   v=max(hi,saved[1]);safe[g].append(v);coeffs+=1
   if saved[1]>0:max_ratio=max(max_ratio,v/saved[1])
  rows.append({'gamma_exact':str(g),'coefficients_upper_exact':[str(v) for v in safe[g]]})
 need(coeffs==3508,'all outer monomials');return safe,{'outer_constituent_intervals':read,'outer_product_blocks':blocks,'outer_linear_blocks':10,'outer_exponents':len(C),'outer_monomials':coeffs,'outer_lineage_exact_equalities':2*coeffs,'saved_interval_overlap_checks':coeffs,'maximum_coefficient_inflation_exact':str(max_ratio)},rows

def inner_coeffs(data):
 need(data['schema']=='ipm-inner-exact-density-coefficients-v1' and data['input_sha256']==SH and F(data['ta_exact'])==A and F(data['bi_exact'])==BI,'exact inner schema and geometry');need(len(data['rows'])==262,'all inner slots')
 sums=[{} for _ in range(4)];slots=0;equalities=0;monotone=0
 for j,row in enumerate(data['rows']):
  need(row['j']==j and F(row['C'])==(F(1,4) if j<2 else 0),'exact cubic coefficient');need(len(row['D'])==len(row['Ei'])==7,'all inner polynomial terms')
  family=[(F(2*i+2),[F(v)]) for i,v in enumerate(row['D'])]+[(BI,[F(v) for v in row['Ei']])]
  if j==261:need(all(v==0 for rate,cs in family for v in cs),'zero last density slot')
  for rate,cs in family:
   slots+=len(cs);pol=fmpq_poly([fq(v) for v in cs])
   for p in range(4):
    vals=[]
    for l in range(len(cs)):
     v=sum((F(comb(p,q)*factorial(l+q),factorial(l))*(3+rate)**(p-q)*cs[l+q] for q in range(min(p,len(cs)-l-1)+1)),F(0))
     need(v==ff(pol[l]),'independent exact differentiated density coefficient');equalities+=1;vals.append(v)
     need((rate==2 and l==0) or rate>2 and 5*(rate-2)>=l,'true radial maximum monotonicity');monotone+=1
     key=(rate,l);sums[p][key]=sums[p].get(key,F(0))+abs(v)
    pol=pol.derivative()+fq(3+rate)*pol
 return sums,{'inner_slots':slots,'inner_cubic_checks':262,'inner_derivative_exact_equalities':equalities,'inner_monotonicity_checks':monotone}

def derivatives(C):
 results=[{} for _ in range(3)];checks=0
 for g,cs in C.items():
  need(1+2*K-2*g>0,'positive integral rate');pol=fmpq_poly([fq(v) for v in cs])
  for p in range(3):
   vals=[]
   for l in range(len(cs)):
    v=sum((F(comb(p,q)*factorial(l+q),factorial(l))*abs(g)**(p-q)*cs[l+q] for q in range(min(p,len(cs)-l-1)+1)),F(0))
    need(v==ff(pol[l]),'independent positive derivative recurrence');checks+=1;vals.append(v)
   results[p][g]=vals;pol=pol.derivative()+fq(abs(g))*pol
 return results,checks

def engine(name,sums,derivs,cr,ct):
 q,exp,sqrt,pi=(aq,lambda x:x.exp(),lambda x:x.sqrt(),arb.pi()) if name=='arb512' else (iq,iv.exp,iv.sqrt,iv.pi)
 Ri2=exp(q(2*(A-5)));cl=1/K;c=3/K-1
 ds=[exp(q(-2*A))*sum((q(v*5**l)*exp(q(-5*(rate-2))) for (rate,l),v in row.items()),q(0)) for row in sums]
 ss=[q(cr)];qs=[q(ct)];f0=1+Ri2*(ds[1]+NU*ds[0]);f1=2+Ri2*(ds[2]+(NU+1)*ds[1]+NU*ds[0])
 ss.append(2*ss[0]+M*qs[0]);qs.append(M*ss[0]+2*qs[0]+f0);ss.append(2*ss[1]+M*qs[1]);qs.append(M*ss[1]+2*qs[1]+f1)
 bs=[]
 for p in range(3):
  v=q(abs(cl))*ds[p+1]+ds[p]+q(abs(c))*(ds[p+1]+NU*ds[p])
  for l in range(p+1):v+=comb(p,l)*3**(p-l)*(q(F(3,2))*ss[l]+qs[l])+Ri2*comb(p,l)*(ss[l]*ds[p-l+1]+qs[l]*NU*ds[p-l])
  bs.append(v)
 ci=pi*q(L**6)*(1+Ri2/q(L**2))**q(F(3,2)-K)*exp(q(6*(A-5)))/6
 i0=ci*((1+OMEGA**2)*bs[0]**2+bs[1]**2);i1=ci*((1+OMEGA**2)*(bs[0]+bs[1])**2+(bs[1]+bs[2])**2)
 co=q(L)**q(3+2*K)*exp(q(-(1+2*K)*BETA0))*(1+q(L**2)*exp(q(-2*(BETA0+17))))**q(F(3,2)-K)
 ls=[q(0),q(0),q(0)];integrals=0;weights={}
 for g,cs in derivs[0].items():
  rate=1+2*K-2*g;er=exp(q(-17*rate));js=[]
  if name=='arb512':
   for l in range(len(cs)):
    n=2*l;js.append(er*sum((q(F(factorial(n)*17**(n-j),factorial(n-j))/rate**(j+1)) for j in range(n+1)),q(0)))
  else:
   J=er/q(rate);js=[J]
   for n in range(1,2*len(cs)-1):
    J=er*q(17**n)/q(rate)+q(F(n)/rate)*J
    if n%2==0:js.append(J)
  need(len(js)==len(cs),'all exact tail moment degrees')
  for l,jv in enumerate(js):
   weight=sqrt(co*jv);weights[(g,l)]=weight;integrals+=1
   for p in range(3):ls[p]+=q(derivs[p][g][l])*weight
 o0=pi*((1+OMEGA**2)*ls[0]**2+ls[1]**2);o1=pi*((1+OMEGA**2)*(ls[0]+ls[1])**2+(ls[1]+ls[2])**2)
 result={'d':[enc(x,name) for x in ds],'s':[enc(x,name) for x in ss],'q':[enc(x,name) for x in qs],'B':[enc(x,name) for x in bs],'C_i':enc(ci,name),'C_o':enc(co,name),'L':[enc(x,name) for x in ls],'tail_norms':{k:enc(sqrt(v),name) for k,v in [('inner_eps',i0),('inner_eps_minus_eps_t',i1),('outer_eps',o0),('outer_eps_minus_eps_t',o1)]},'conditional_full_plane_norms':{'eps':enc(sqrt(q(F('0.385656')**2)+i0+o0),name),'eps_minus_eps_t':enc(sqrt(q(F('585.874')**2)+i1+o1),name)},'integrals':integrals}
 return result,weights

def guards():
 cases=[('zero rate',lambda:need(F(0)>0,'bad rate')),('negative rate',lambda:need(F(-1)>0,'bad rate')),('bad core monotonicity',lambda:need(5*(F(2)-2)>=1,'bad maximum')),('zero mode changed',lambda:need(F(1)==0,'bad final slot')),('bad saved enclosure',lambda:checked_bound({'lower_exact':'2','upper_exact':'1','ball':{'schema':'arb-dyadic-mid-radius-v1','mid_m':'1','mid_e':'0','rad_m':'0','rad_e':'0'}})),('negative bound',lambda:checked_bound({'lower_exact':'-2','upper_exact':'-1','ball':{'schema':'arb-dyadic-mid-radius-v1','mid_m':'-1','mid_e':'0','rad_m':'0','rad_e':'0'}}))]
 for name,f in cases:
  try:f()
  except ValueError:pass
  else:raise ValueError('guard did not reject '+name)
 return {'guard_cases':len(cases),'guard_rejections':len(cases),'names':[x[0] for x in cases]}

def run():
 started=now();clock=time.monotonic();pins,parents,pr=base();need(flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0','arithmetic versions')
 inner=load(B/'research/inner_majorant/evidence/inner_result.json');outer=load(B/'research/outer_majorant/evidence/outer_result.json')
 for key,target in [('k_exact',K),('L_exact',L),('ta_exact',A)]:need(F(inner[key])==target,'inner scalar identity')
 need(F(outer['tb_exact'])==BETA0 and F(outer['scalars_exact']['k'])==K and F(outer['scalars_exact']['L'])==L,'outer scalar identity')
 need(inner['cases'][0]['T_exact']=='0','full inner disk constants');cr=checked_bound(inner['cases'][0]['values']['C_r'])[1];ct=checked_bound(inner['cases'][0]['values']['C_theta'])[1]
 coeffs,counts,rows=lineage(outer);sums,ic=inner_coeffs(load(B/'research/inner_majorant/evidence/exact_inner_coefficients.json'));counts.update(ic);derivs,n=derivatives(coeffs);counts['outer_derivative_exact_equalities']=n
 print(json.dumps({'utc':now(),'stage':'whole_exact_lineage_done','seconds':time.monotonic()-clock,'counts':counts}),flush=True)
 ra,wa=engine('arb512',sums,derivs,cr,ct);print(json.dumps({'utc':now(),'stage':'arb_done','seconds':time.monotonic()-clock}),flush=True)
 rb,wb=engine('iv200',sums,derivs,cr,ct);overlaps=0
 for key in wa:
  a=ae(wa[key]);b=ie(wb[key]);need(max(a[0],b[0])<=min(a[1],b[1]),'independent weighted moment intersection');overlaps+=1
 counts['independent_weight_intersections']=overlaps
 ceilings={}
 for family in ('tail_norms','conditional_full_plane_norms'):
  ceilings[family]={}
  for name,v in ra[family].items():
   hi=max(F(v['upper_exact']),F(rb[family][name]['upper_exact']));den=10**12;num=hi.numerator*den//hi.denominator+1;z=F(num,den);need(z>hi,'strict upward ceiling against both engines');ceilings[family][name]=format(num//den,'d')+'.'+str(num%den).zfill(12)
 counts['strict_decimal_ceiling_checks']=12
 guard=guards();counts.update({k:v for k,v in guard.items() if k!='names'})
 write(E/'coefficient_upper_bounds.json',{'schema':'ipm-canonical-residual-coefficient-upper-v1','rows':rows,'scope':'new safe maxima of inherited and independently reassembled coefficient upper bounds'})
 pin(pins,E/'coefficient_upper_bounds.json');rehash(pins)
 result={'start_utc':started,'utc':now(),'status':'PASS_CANONICAL_DERIVATIVE_END_TAILS_REQUIRES_ACTUAL_REVIEW','parents':parents,'proof_review':pr,'files':dict(sorted(pins.items())),'counts':counts,'guard_names':guard['names'],'precision':{'arb_bits':512,'iv_dps':200},'versions':{'python-flint':flint.__version__,'mpmath':mpmath.__version__},'inner_constants_exact':{'C_r':str(cr),'C_theta':str(ct)},'geometry_exact':{'k':str(K),'L':str(L),'a':str(A),'b':str(BETA0),'alpha':str(A-5),'beta':str(BETA0+17),'Omega':OMEGA,'nu':NU,'M':M},'enclosures':{'arb512':ra,'iv200':rb},'strict_decimal_ceilings':ceilings,'seconds':time.monotonic()-clock,'scope':'Canonical modal residual, two infinite derivative end regions unconditionally; displayed full-plane X bounds conditional on all19389 physical annular W hypotheses. No inverse, X3 distance, nonlinear closure, existence or exclusion.'}
 write(E/'checks.json',result);print(json.dumps({'utc':result['utc'],'status':result['status'],'counts':counts,'ceilings':ceilings,'seconds':result['seconds']}),flush=True)
if __name__=='__main__':run()
