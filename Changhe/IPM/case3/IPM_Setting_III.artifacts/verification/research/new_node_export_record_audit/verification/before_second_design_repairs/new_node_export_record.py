"""Exact finite-operand arithmetic for producer node records. No inverse reuse."""
from fractions import Fraction as Q
import math,re
from pathlib import Path
import numpy as np
U=Q(1,2**53);GAMMA=8*U/(1-8*U);TINY=np.finfo(float).tiny
ARRAYS=['x','y','g','g_xi','g_y','V1','V2','R_h','N_f']
SCALARS=['c','N','M','fine','rule','state_file','state_sha256','solver_nodes_Fmax']
REGIONS=[('core',0,.1),('subannulus',.1,1),('annulus',1,100),('far',100,math.inf)]
def exact(x,y,g,gx,gy,v,w):
 x,y,g,gx,gy,v,w=map(lambda z:Q(float(z)),(x,y,g,gx,gy,v,w))
 e=x*gx+y*gy;a=v*gx+w*gy;r=2*e+a-g
 nf=abs(2*x*gx+v*gx)+abs(2*y*gy+w*gy)+abs(g);nv=abs(g)+abs(e)+abs(a)
 return r,nf,nv,abs(r)/nf if nf else None,abs(r)/nv if nv else None

def normal_intermediates(x,y,g,gx,gy,v,w):
 with np.errstate(over='ignore',under='ignore',invalid='ignore'):
  ax=2*x;ay=2*y;bx=ax+v;by=ay+w;px=bx*gx;py=by*gy;plus=px+py;minus=plus-g;nf0=np.abs(px)+np.abs(py);nf=nf0+np.abs(g)
 bad_product=((bx!=0)&(gx!=0)&(px==0))|((by!=0)&(gy!=0)&(py==0))
 return not np.any(bad_product)and all(np.isfinite(t).all()and np.all((t==0)|(np.abs(t)>=TINY))for t in [ax,ay,bx,by,px,py,plus,minus,nf0,nf])

def round_values(a,index):
 out=[];under=[]
 for k,z in enumerate(a):
  if z is None:out.append(math.nan);continue
  try:f=float(z)
  except OverflowError:raise ValueError(('nonrepresentable value',index,k))
  if not math.isfinite(f)or(k<3 and z!=0 and f==0):raise ValueError(('nonrepresentable value',index,k))
  if k>=3 and z!=0 and f==0:under.append(dict(index=index,field=['R','Nf','Nv','Rf','Rv'][k],exact=str(z),rounded=0.,status='UNDERFLOW'))
  out.append(f)
 return out,under

def check_rows(d):
 n=len(d['x'])
 if not all(d[k].shape==(n,)and d[k].dtype==np.float64 and np.isfinite(d[k]).all()for k in ARRAYS):raise ValueError('nonfinite or wrong field shape/dtype')
 args=[d[k]for k in ARRAYS[:7]]
 if not normal_intermediates(*args):raise ValueError('non-normal arithmetic intermediate or product underflow')
 out=[];errR=[];errN=[];under=[];nonzero=0
 for i,operands in enumerate(zip(*args)):
  a=exact(*operands);r,nf=a[:2];er=abs(Q(float(d['R_h'][i]))-r);en=abs(Q(float(d['N_f'][i]))-nf)
  if er>GAMMA*nf or en>GAMMA*nf:raise ValueError(('outside gamma8 bound',i,str(er),str(en),str(nf)))
  row,ur=round_values(a,i);out.append(row);under+=ur;nonzero+=er!=0;errR.append(er/nf if nf else Q(0));errN.append(en/nf if nf else Q(0))
 er=max(errR,default=Q(0));en=max(errN,default=Q(0))
 return np.asarray(out),dict(max_R_error_over_exact_Nf=float(er),max_Nf_error_over_exact_Nf=float(en),max_R_error_over_exact_Nf_exact=str(er),max_Nf_error_over_exact_Nf_exact=str(en),gamma8=float(GAMMA),gamma8_exact=str(GAMMA),nonzero_R_rounding_discrepancies=int(nonzero),ratio_underflows=under)

def schema(d):
 if set(d)!=set(ARRAYS+SCALARS):raise ValueError('closed export key set')
 for k in SCALARS:
  if not isinstance(d[k],np.ndarray)or d[k].shape!=():raise ValueError('scalar shape '+k)
 for k in ['rule','state_file','state_sha256']:
  if d[k].dtype.kind!='U':raise ValueError('unicode scalar '+k)
 for k in ['N','M']:
  if d[k].dtype.kind not in 'iu' or int(d[k])<1:raise ValueError('positive integer scalar '+k)
 if d['fine'].dtype.kind!='b':raise ValueError('boolean fine scalar')
 for k in ['c','solver_nodes_Fmax']:
  if d[k].dtype!=np.float64:raise ValueError('float64 scalar '+k)
 if not np.isfinite(d['c']):raise ValueError('finite c scalar')
 if not re.fullmatch('[0-9a-f]{64}',str(d['state_sha256'])):raise ValueError('state hash syntax')
 f=float(d['solver_nodes_Fmax'])
 if math.isinf(f)or f<0:raise ValueError('nonnegative finite or NaN solver metadata')

def metadata(d,q,z):
 schema(d);N,M,fine=z['N'],z['M'],z['fine'];n=N*M*(3 if fine else 1)
 if not(int(d['N'])==q.N==N and int(d['M'])==q.M==M and bool(d['fine'])==fine and float(d['c'])==q.cl==2 and q.L==1 and q.kappa==2 and q.p==.5 and q.meta['basis_nodes_source']=='stored'and q.basis=='local'):raise ValueError('state and export parameters')
 if 'c' in q.meta and q.meta['c']!=2:raise ValueError('raw state c disagrees')
 if 'map_exponent_P'in q.data and float(q.data['map_exponent_P'])!=q.kappa:raise ValueError('raw map exponent disagrees')
 if str(d['state_sha256'])!=z['state_sha256']:raise ValueError('source hash disagreement')
 if Path(str(d['state_file'])).name!=z['producer_state_basename']:raise ValueError('producer state basename')
 rule='resolved evaluator (32, 10x16, 400, q=2); rows: '+('3M oversampled angles (fine)'if fine else'M collocation angles')
 if str(d['rule'])!=rule:raise ValueError('rule disagreement')
 result=q.data.get('result')or{};opts=q.data.get('inverse_options')or{}
 if (bool(result.get('fine',False))or bool(opts.get('fine',False)))!=fine:raise ValueError('state fine flag')
 f=float(result.get('nodes_Fmax',math.nan));g=float(d['solver_nodes_Fmax'])
 if not((math.isnan(f)and math.isnan(g))or f==g):raise ValueError('solver residual metadata')
 if len(d['x'])!=n:raise ValueError('node count')
 return dict(raw_c_present='c'in q.meta,map_exponent_present='map_exponent_P'in q.data,rule=rule)

def expected_coordinates(tk,M,fine):
 m=M*(3 if fine else 1);r=np.sqrt((1+np.asarray(tk)[1:])/2)/(1-np.asarray(tk)[1:])**2;th=(np.arange(m)+.5)*np.pi/(2*m)
 return (r[:,None]*np.cos(th)).ravel(),(r[:,None]*np.sin(th)).ravel()
def coordinates(x,y,xx,yy):
 if x.shape!=xx.shape or y.shape!=yy.shape:raise ValueError('coordinate shape/order count')
 scale=np.stack([abs(xx),abs(yy)],1)
 if not(np.isfinite(scale).all()and np.all(scale>0)):raise ValueError('positive finite coordinate scales')
 relative=abs(np.stack([x-xx,y-yy],1))/scale
 if not np.isfinite(relative).all():raise ValueError('finite coordinate differences')
 pos=np.unravel_index(int(np.argmax(relative)),relative.shape);v=float(relative[pos])
 if v>32*float(U):raise ValueError(('coordinate tolerance',v,list(map(int,pos))))
 return dict(relative_error=v,index=int(pos[0]),component=['x','y'][pos[1]])

def regions(x,y,fields):
 radius=np.hypot(x,y);out=[]
 for name,lo,hi in REGIONS:
  ids=np.flatnonzero((radius>=lo)&(radius<hi));metrics={}
  for name2,col in [('absR',0),('Rf',3),('Rv',4)]:
   vals=np.abs(fields[ids,col]);ok=np.isfinite(vals);valid=ids[ok]
   if len(valid):
    i=int(valid[np.argmax(vals[ok])]);metrics[name2]=dict(index=i,value=float(abs(fields[i,col])),x=float(x[i]),y=float(y[i]),fields=fields[i].tolist(),defined_count=int(ok.sum()),undefined_count=int((~ok).sum()))
   else:metrics[name2]=dict(index=None,value=None,defined_count=0,undefined_count=len(ids))
  out.append(dict(region=name,count=len(ids),metrics=metrics))
 return out

def export_regions(d,vals):
 f=np.full_like(vals,np.nan);f[:,0]=d['R_h'];f[:,1]=d['N_f'];f[:,3]=np.divide(abs(d['R_h']),d['N_f'],out=np.full(len(f),np.nan),where=d['N_f']!=0);reg=regions(d['x'],d['y'],f)
 for r in reg:
  del r['metrics']['Rv']
  for v in r['metrics'].values():
   if v['index']is not None:
    i=v['index'];v['fields']=dict(R_h=float(d['R_h'][i]),N_f=float(d['N_f'][i]),Rf=float(f[i,3]))
 return reg

def selected(reg,exportreg,n):
 ids={0,n//2,n-1}
 for r in reg+exportreg:
  for a in r['metrics'].values():
   if a['index']is not None:ids.add(a['index'])
 return sorted(ids)

def printed_value(token,value,undefined=0):
 if token.lower()=='nan':
  if not undefined:raise ValueError('printed NaN without undefined ratio')
  return 'NAN_PROPAGATED_IN_PRODUCER_REGION'
 if undefined:raise ValueError('numeric print despite undefined ratio')
 if value is None or not math.isfinite(value):raise ValueError('defined finite printed value expected')
 m=re.fullmatch(r'([+-]?\d+)(?:\.(\d+))?[eE]([+-]?\d+)',token)
 if m is None:raise ValueError('malformed finite scientific token '+token)
 places=len(m[2]or'');half=Q(10)**(int(m[3])-places)/2;center=Q(token)
 if not center-half<=Q(value)<=center+half:raise ValueError(('printed interval',token,value))
 return 'WITHIN_CLOSED_DECIMAL_HALF_ULP'

def printed_table(text,reg):
 rows=re.findall(r'r in \[([^,]+), ([^\)]+)\): max \|R_h\| (\S+)\s+max \|R_h\|/N_f (\S+)',text)
 if len(rows)!=4:raise ValueError('four printed regions required')
 out=[]
 for k,row in enumerate(rows):
  bounds=[(Q(0),Q('0.1')),(Q('0.1'),Q(1)),(Q(1),Q(100)),(Q(100),Q('1e300'))][k]
  try:parsed=(Q(row[0]),Q(row[1]))
  except(ValueError,ZeroDivisionError):raise ValueError('invalid printed region label')
  if parsed!=bounds:raise ValueError('printed region order or label')
  for metric,token in [('absR',row[2]),('Rf',row[3])]:
   a=reg[k]['metrics'][metric];out.append(dict(region=reg[k]['region'],metric=metric,token=token,semantics=printed_value(token,a['value'],a['undefined_count'])))
 return out

def printed_header(text,d,z):
 expected=f"{z['producer_state_basename']} {z['N']}x{z['M']} c=2.0: solver node |F|max (maps) "
 if not text.startswith(expected):raise ValueError('printed state/dimension/c header')
 tail=text[len(expected):];token,sep,rest=tail.partition(';  ')
 if not sep:raise ValueError('printed header separator')
 f=float(d['solver_nodes_Fmax']);printed_value(token,f,1 if math.isnan(f)else 0)
 expected2=f"{str(d['rule'])} AT THE SAME NODES ({len(d['x'])} points):\n"
 if not rest.startswith(expected2):raise ValueError('printed rule/count header')
 return True
