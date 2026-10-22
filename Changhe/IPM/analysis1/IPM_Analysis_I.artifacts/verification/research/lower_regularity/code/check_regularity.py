"""Frozen-source recurrence and constants using exact algebra, Arb and iv."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as sp
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/lower_regularity/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ii(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ends(x):
 if isinstance(x,arb):return tuple(F(int(m))*F(2)**int(e) for m,e in [v.man_exp() for v in (x.lower(),x.upper())])
 return tuple((-1 if s else 1)*F(int(m))*F(2)**int(e) for s,m,e,b in x._mpi_)
def rec(x):l,u=ends(x);assert l<=u;return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def atan_bounds(q,N):
 q=F(q);s=sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(N)),F());nxt=(-1)**N*q**(2*N+1)/F(2*N+1);return min(s,s+nxt),max(s,s+nxt)
def sqrt_bounds(q,P=2048):
 q=F(q);assert q>0;N=math.isqrt((q.numerator << (2*P))//q.denominator);l=F(N,1<<P);u=F(N+1,1<<P);assert l*l<=q<=u*u;return l,u

def gauss(mat,rhs):
 n=len(rhs);z=[list(row)+[v] for row,v in zip(mat,rhs)]
 for k in range(n):
  j=next(j for j in range(k,n) if z[j][k]);z[k],z[j]=z[j],z[k];d=z[k][k];z[k]=[v/d for v in z[k]]
  for j in range(n):
   if j!=k:
    d=z[j][k];z[j]=[v-d*w for v,w in zip(z[j],z[k])]
 return [row[-1] for row in z]

def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180;inp=E/'inputs.json';raw=json.loads(inp.read_text());k=F(raw['k']);g=F(raw['g_illustration']);A=2/k-1;D=2*A+1;c0=(A+3)/2
 data=B/'data_exact/modal_v2.json';stored=json.loads(data.read_text());assert k==F(float.fromhex(stored['scalars_hex']['k']))
 ids={}
 def ident(n,e):
  v=sp.simplify(e);assert v==0,(n,v);ids[n]=str(v)
 s,y,q,r,Av,gv=sp.symbols('s y q r A g',positive=True);w=s**q*y**r;lam=Av*q+r;Tw=Av*s*sp.diff(w,s)+y*sp.diff(w,y)-w
 ident('minus_Laplacian_frozen',(-sp.diff(Tw,s,2)-sp.diff(Tw,y,2)+gv*sp.diff(w,s,2))-((gv+1-lam)*sp.diff(w,s,2)+(1-lam)*sp.diff(w,y,2)))
 p,j,n=sp.symbols('p j n');ident('lambda_j',(Av*(p+2*j)+n-2*j).subs(p,(gv+1-n)/Av)-(gv+1+2*j*(Av-1)))
 ss,a=sp.symbols('sigma a');dv=2*Av+1;c=(Av+3)/2
 ident('weight_lower',(ss*dv-c)/Av-(2*ss-sp.Rational(1,2)+(ss-sp.Rational(3,2))/Av))
 ident('weight_sample',(-c-5*Av+sp.Rational(5,2)*dv)-(1-Av/2))
 ident('weight_upper_s',(sp.Rational(13,2)*Av+c)/dv-(14*Av+3)/(4*Av+2))
 ident('row4_exponent',(4*Av+1)/dv-(2-1/dv))
 ident('strain_dimension_scale',(ss-1)+2-3-(ss-2))
 ident('Hs_scaling_exponent',2*(ss-1)+4-2-2*ss)
 ident('radial_geometric_exponent',2*(a+ss-1)-2*q+2*(q-a-ss+1))
 xi,eta=sp.symbols('xi eta');poly=(1+xi**2+eta**2)**3;multinomial=0;weights={}
 for a1 in range(4):
  for a2 in range(4-a1):
   c=math.factorial(3)//(math.factorial(3-a1-a2)*math.factorial(a1)*math.factorial(a2));weights[f'{a1},{a2}']=c;multinomial+=c*xi**(2*a1)*eta**(2*a2)
 ident('H3_multinomial',poly-multinomial)
 theta=sp.symbols('theta',real=True);ident('strain_angular_integral',sp.integrate(sp.cos(theta)**4*sp.sin(theta)**2,(theta,0,2*sp.pi))-sp.pi/8)
 u,sv=sp.symbols('u sigma',positive=True);anti=(1+u)**(2-sv)/(2-sv)-(1+u)**(1-sv)/(1-sv)
 ident('radial_primitive',sp.diff(anti,u)-u*(1+u)**(-sv));ident('radial_integral',-(1/(2-sv)-1/(1-sv))/2-1/(2*(sv-1)*(sv-2)))
 rows=[]
 for nv in raw['n']:
  pv=(g+1-nv)/A;J=(nv-1)//2;assert pv>1 and pv.denominator>1;coef=[F(1)]
  for jv in range(J):coef.append(-(g+2*jv*(A-1))*(nv-2*jv)*(nv-2*jv-1)*coef[-1]/(2*(jv+1)*(A-1)*(pv+2*jv+2)*(pv+2*jv+1)))
  # Independently apply transport, then ordinary second derivatives, to each monomial.
  out={};columns=[]
  for jv in range(J+1):
   qv=pv+2*jv;rv=nv-2*jv;transport=A*qv+rv-1;col={}
   for ex,ey,v in [(qv-2,rv,-transport*qv*(qv-1)+g*qv*(qv-1)),(qv,rv-2,-transport*rv*(rv-1))]:
    if v:col[(ex,ey)]=col.get((ex,ey),F())+v
   columns.append(col)
   for key,v in col.items():out[key]=out.get(key,F())+coef[jv]*v
  assert all(v==0 for v in out.values());ids[f'n{nv}_all_differential_coefficients']='0'
  keys=sorted(set().union(*(set(c) for c in columns)));assert len(keys)==J
  matrix=[[F(int(jv==0)) for jv in range(J+1)]]+[[col.get(key,F()) for col in columns] for key in keys]
  solved=gauss(matrix,[F(1)]+[F()]*J);assert solved==coef;ids[f'n{nv}_independent_linear_solve']='0'
  rows.append({'n':nv,'p_exact':str(pv),'threshold_exact':str(pv+F(1,2)),'coefficients_exact':list(map(str,coef)),'differential_rows':len(keys)})
 exact={'k':k,'g_illustration':g,'A':A,'D':D,'c0':c0,'weight_s_max':(14*A+3)/(4*A+2),'weight_lower_s2.5':F(9,2)+1/A,'rate_s2.5_a5':1-A/2,'p2':2-1/D,'p2_threshold':F(5,2)-1/D,'fast_s2':2*A-c0-g,'fast_s3':3*A-c0-g,'slow_s2':2-c0,'slow_s3':3-c0,'pure_fast_s2':2*A-c0,'pure_fast_s3':3*A-c0}
 for row in rows:exact['p_n'+str(row['n'])]=F(row['p_exact']);exact['threshold_n'+str(row['n'])]=F(row['threshold_exact'])
 assert A>10 and exact['weight_s_max']>3 and exact['rate_s2.5_a5']<0
 assert exact['fast_s2']<exact['fast_s3']<0 and exact['slow_s2']<exact['slow_s3']<0 and exact['pure_fast_s2']>0
 assert F(rows[1]['p_exact'])+F(1,2)>F(5,2) and F(rows[1]['p_exact'])+F(1,2)<F(31,10) and 1<F(rows[2]['p_exact'])<2
 # Machin's identity, atan alternating remainder, followed by integer square-root brackets.
 a5=atan_bounds(F(1,5),500);a239=atan_bounds(F(1,239),160);pl=16*a5[0]-4*a239[1];pu=16*a5[1]-4*a239[0];assert 3<pl<pu<4
 pi_iv=iv.mpf([ii(pl).a,ii(pu).b]);vals={'arb':{n:aa(v) for n,v in exact.items()},'iv':{n:ii(v) for n,v in exact.items()}};vals['arb']['pi']=arb.pi();vals['iv']['pi']=pi_iv
 for order in raw['strain_orders']:
  sig=F(order);t=(sig-1)*(sig-2);lo=sqrt_bounds(pl*t)[0];hi=sqrt_bounds(pu*t)[1];tag='strain_'+order.replace('/','_');vals['arb'][tag]=1/(8*(arb.pi()*aa(t)).sqrt());vals['iv'][tag]=ii(1)/(8*iv.mpf([ii(lo).a,ii(hi).b]));vals['arb'][tag+'_c']=vals['arb'][tag]/3;vals['iv'][tag+'_c']=vals['iv'][tag]/3
 for name in vals['arb']:
  al,au=ends(vals['arb'][name]);il,iu=ends(vals['iv'][name]);assert max(al,il)<=min(au,iu),name
 vals={m:{n:rec(v) for n,v in row.items()} for m,row in vals.items()}
 o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'proof_sha256':sha(B/'research/lower_regularity/PROOF.md'),'input_sha256':sha(inp),'data_sha256':sha(data),'exact_identities':ids,'recurrences':rows,'exact_parameters':{n:str(v) for n,v in exact.items()},'H3_multinomial':weights,'pi_rational_bracket':[str(pl),str(pu)],'values':vals,'method':'Symbolic differentiated identity, exact Fraction recurrence and independent dense Gauss-Jordan solve; Arb512 constants versus iv180 with exact rational Machin alternating series and integer-square-root brackets.','seconds':time.monotonic()-start,'scope':'Frozen illustrative parameters; no unknown-profile enclosure, global inverse or endpoint.'}
 (E/'checks.json').write_text(json.dumps(o,indent=2)+'\n');summary={k:v for k,v in o.items() if k not in ('values','pi_rational_bracket')};summary['checks_sha256']=sha(E/'checks.json');summary['values_display']={m:{n:r['display'] for n,r in row.items()} for m,row in vals.items()};(E/'review_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({'utc':o['utc'],'status':o['status'],'seconds':o['seconds'],'identities':len(ids),'constants':len(vals['arb']),'p_n11':vals['arb']['p_n11']['display'],'strain_5_2':vals['arb']['strain_5_2']['display']}))
if __name__=='__main__':main()
