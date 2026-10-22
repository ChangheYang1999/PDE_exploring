"""Exact polynomial audit of serialized stream states; packet115, no NUM code."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,argparse

def trim(a):
 a=list(a)
 while len(a)>1 and not a[-1]:a.pop()
 return a

def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return trim(c)

def scale(a,s):return trim([s*x for x in a])
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def deriv(a):return trim([F(i)*a[i] for i in range(1,len(a))] or [F(0)])
def value(a,z):
 out=F(0)
 for c in reversed(a):out=out*z+c
 return out

def cheb(n):
 a=[F(1)];b=[F(0),F(1)]
 if not n:return a
 for k in range(1,n):a,b=b,add(scale(mul([F(0),F(1)],b),2),scale(a,-1))
 return b

def angular(data,key,d):
 out=[F(0)]
 for (i,j,shift),v in zip(data['labels'],data[key]):
  if shift==d:out=add(out,scale(cheb(j),(-1)**i*F(v)))
 return out

def transport_derivative(a,power):return add(scale(mul([F(0),F(1)],a),power),mul([F(1),F(0),F(-1)],deriv(a)))
def checks(data):
 beta=F(data['beta'])
 if not F(2)<beta<F(3):raise ValueError('this certificate applies only to 2<beta<3')
 s=1/beta;Cinf=-sum((F(c)*cheb(j)[0] for (i,j,d),c in zip(data['labels'],data['C'])),F(0))
 P0,P1,Q0,Q1=[angular(data,k,d) for k,d in [('C',0),('C',1),('D',0),('D',1)]]
 dp=add(scale(transport_derivative(P0,1-s),Cinf),scale(P1,-beta))
 dq=add(scale(transport_derivative(Q0,-1-2*s),Cinf),scale(Q1,-beta))
 witness=lambda a:next(({'z':str(z),'value':str(value(a,z))} for z in [F(0),F(1,3),F(-1,3),F(2,3),F(-2,3),F(1,2),F(-1,2)] if value(a,z)),None)
 return {'beta':str(beta),'constant_vertical':str(Cinf),'P0':[str(v) for v in P0],'P1':[str(v) for v in P1],'Q0':[str(v) for v in Q0],'Q1':[str(v) for v in Q1],
 'stream_residual_potential_polynomial':[str(v) for v in dp],'temperature_residual_polynomial':[str(v) for v in dq],
 'stream_nonzero':any(dp),'temperature_nonzero':any(dq),'stream_witness':witness(dp),'temperature_witness':witness(dq),
 'scope':'exact algebra of imported binary-rational coefficients; distinct residual tail powers prove a stored state is not exact, but give no nearby-profile exclusion and no residual lower bound'}

def make(path,out):
 data=json.loads(path.read_text());c=checks(data);c.update(source_path=str(path.resolve()),source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),created_utc=datetime.now(timezone.utc).isoformat());out.write_text(json.dumps(c,indent=2)+'\n');return c

def verify(path,cert):
 data=json.loads(path.read_text());c=json.loads(cert.read_text())
 if c['source_sha256']!=hashlib.sha256(path.read_bytes()).hexdigest():raise ValueError('input digest mismatch')
 for k,v in checks(data).items():
  if c.get(k)!=v:raise ValueError('certificate mismatch: '+k)
 return True

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['create','check','archive']);ap.add_argument('input',type=Path);ap.add_argument('output',type=Path,nargs='?');a=ap.parse_args()
 if a.mode=='create':make(a.input,a.output)
 elif a.mode=='check':verify(a.input,a.output);print('CONFIRMED exact input and polynomial arithmetic')
 else:
  root=a.input;dest=root/'fractional_tail_certificates';dest.mkdir(exist_ok=True);summary=[]
  for p in sorted(root.glob('*_state.json')):
   c=make(p,dest/(p.stem+'_certificate.json'));verify(p,dest/(p.stem+'_certificate.json'));summary.append({'state':p.name,'beta':float(F(c['beta'])),'constant_vertical':float(F(c['constant_vertical'])),'stream_nonzero':c['stream_nonzero'],'temperature_nonzero':c['temperature_nonzero'],'stream_coefficient_max':max(abs(float(F(v))) for v in c['stream_residual_potential_polynomial']),'temperature_coefficient_max':max(abs(float(F(v))) for v in c['temperature_residual_polynomial']),'certificate':str((dest/(p.stem+'_certificate.json')).relative_to(root))})
  (dest/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
