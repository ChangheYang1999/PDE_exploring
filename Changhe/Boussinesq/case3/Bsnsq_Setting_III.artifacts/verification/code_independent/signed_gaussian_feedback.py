"""Independent multi-Gaussian inverse, adaptive characteristics and full-plane strain.
Only frozen numerical DATA are read. No numerics-lane implementation is imported.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, math, os, time, resource
import numpy as np
from numpy.polynomial.legendre import leggauss
from gaussian_characteristics import GaussianFlow

ROOT=Path('research/236_signed_gaussian_feedback/verification')
def now(): return datetime.now(timezone.utc).isoformat()
def save(path,obj): path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def cases():
 out={}
 for p in sorted((ROOT/'sources').glob('*.json')):
  doc=json.loads(p.read_text())
  for r in doc.get('results',[]):
   if r['case'] in out: raise ValueError('duplicate case needs explicit adjudication')
   out[r['case']]={'data':r,'file':str(p),'args':doc['args']}
 return out

class SignedGaussianFlow(GaussianFlow):
 def __init__(self,c,lobes):
  self.c=float(c);self.beta=2*(self.c-1);self.lam=(self.beta-2)/2;self.mu=1+1.5*self.beta
  if self.beta<=2: raise ValueError('center-source construction requires beta>2')
  self.lobes=[];cs=[]
  for l in lobes:
   o=object.__new__(GaussianFlow);o.a=1/(2*l['s']**2)
   B,bp,bpp=o.B(l['y0']**2)
   self.lobes.append({'a':l['a'],'h':l['y0'],'s':l['s'],'radial':o})
   cs.append(-2*l['a']*l['s']**4*l['y0']*bp)
  self.c_unit=math.fsum(cs);self.A=self.c/self.c_unit
  self.u0=0.;self.ax_y0=0.
  for l in self.lobes:
   l['fac']=self.A*l['a']*l['s']**4
   B,bp,bpp=l['radial'].B(l['h']**2)
   self.u0+=l['fac']*B
   self.ax_y0+=-2*l['fac']*(bp+2*l['h']**2*bpp)
  self.f01=-2*self.ax_y0/self.mu;self.b0=4/self.beta
  self.g01=(2*self.f01-self.ax_y0*self.b0)/(2*self.beta+1)
 def field(self,X):
  x,y=map(float,X);u=np.zeros(2);J=np.zeros((2,2))
  for l in self.lobes:
   Y=y-l['h'];B,bp,bpp=l['radial'].B(x*x+Y*Y);f=l['fac']
   u+=np.array([-2*f*x*Y*bp,f*(B+2*x*x*bp)])
   J+=np.array([[-2*f*Y*(bp+2*x*x*bpp),-2*f*x*(bp+2*Y*Y*bpp)],
                [f*(6*x*bp+4*x**3*bpp),2*f*Y*(bp+2*x*x*bpp)]])
  return u,self.beta*np.array([x,y])+u-np.array([0.,self.u0]),J,J+self.beta*np.eye(2)
 def external_omega(self,x,y):
  return self.A*x*math.fsum(l['a']*math.exp(-(x*x+(y-l['h'])**2)/(2*l['s']**2)) for l in self.lobes)
 def canonical_psi(self,x,y):
  return math.fsum(l['fac']*x*l['radial'].B(x*x+(y-l['h'])**2)[0] for l in self.lobes)

def integrate(g,nr,na,L,rin,rtol,path):
 start=time.monotonic();z,w=leggauss(nr);t=(z+1)/2;radii=L*(t**(-g.beta)-1)
 rw=(w/2)*L*g.beta*t**(-g.beta-1)/radii;z,w=leggauss(na);phis=np.pi*z/2;aw=np.pi*w/2
 terms=[];fail=[];count=0
 with path.open('w') as stream:
  for i,(r,wr) in enumerate(zip(radii,rw)):
   for j,(phi,wa) in enumerate(zip(phis,aw)):
    point=[float(r*math.cos(phi)),float(r*math.sin(phi))]
    ans=g.evaluate(point,r_in=rin,rtol=rtol)
    if ans['status'] in ('COMPLETE','LOCAL_JET'):
     term=2/math.pi*wr*wa*math.cos(phi)*math.sin(phi)*ans['Omega'];terms.append(float(term))
    else: term=None;fail.append({'i':i,'j':j,'point':point,**ans})
    stream.write(json.dumps({'i':i,'j':j,'point':point,'term':term,**ans})+'\n');count+=1
    if count%32==0:stream.flush();print('points',path.name,count,nr*na,'seconds',round(time.monotonic()-start,2),'failures',len(fail),flush=True)
 return {'nr':nr,'na':na,'L':L,'r_in':rin,'rtol':rtol,'c_out':math.fsum(terms) if not fail else None,
         'sum_abs_terms':math.fsum(abs(x) for x in terms),'min_radius':float(min(radii)),'max_radius':float(max(radii)),
         'failures':fail,'point_count':count,'seconds':time.monotonic()-start,'point_file':str(path)}

def controls(allcases):
 start=time.monotonic();out={'started_utc':now(),'checks':[]};cc=out['checks']
 def check(name,truth,**detail):cc.append({'name':name,'pass':bool(truth),**detail})
 # Manufactured analytic Gaussian identity, exactly before numerical checks.
 import sympy as sp
 S,a=sp.symbols('S a',positive=True);B=(1-sp.exp(-a*S))/S
 check('radial Poisson identity exact',sp.simplify(8*sp.diff(B,S)+4*S*sp.diff(B,S,2)+4*a*a*sp.exp(-a*S))==0)
 n_signed=0
 for key,c in allcases.items():
  r=c['data'];g=SignedGaussianFlow(r['c_in'],r['lobes']);pre=key+': '
  check(pre+'amplitude',abs(g.A-r['A'])<1e-11,A_own=g.A,A_num=r['A'])
  check(pre+'unit strain',abs(g.c_unit-r['c_unit'])<2e-14)
  check(pre+'beta',abs(g.beta-r['beta'])<1e-13)
  u,W,J,DW=g.field([0,0]);check(pre+'center matrix',np.max(abs(DW-np.diag([g.lam,g.mu])))<1e-12 and np.max(abs(W))<1e-12)
  points=[[.13,-.4],[1.7,2.1],[-.4,5.2],[0.,r['lobes'][0]['y0']],[1e-7,r['lobes'][0]['y0']]]
  max_poisson=max_div=max_fd=max_parity=0.
  for point in points:
   u,W,J,DW=g.field(point);x,y=point
   max_poisson=max(max_poisson,abs(J[0,1]-J[1,0]-g.external_omega(x,y)))
   max_div=max(max_div,abs(np.trace(J)))
   Jr=np.zeros((2,2));h=2e-4
   for k in range(2):
    e=np.zeros(2);e[k]=h
    Jr[:,k]=(g.field(np.array(point)-2*e)[0]-8*g.field(np.array(point)-e)[0]+8*g.field(np.array(point)+e)[0]-g.field(np.array(point)+2*e)[0])/(12*h)
   max_fd=max(max_fd,float(np.max(abs(J-Jr))))
   ur=g.field([-x,y])[0];max_parity=max(max_parity,abs(ur[0]+u[0]),abs(ur[1]-u[1]))
  check(pre+'Poisson curl sign',max_poisson<3e-12,error=max_poisson)
  check(pre+'incompressibility',max_div<1e-13,error=max_div)
  check(pre+'independent finite-difference derivative',max_fd<2e-7,error=max_fd)
  check(pre+'x symmetry',max_parity<1e-12,error=max_parity)
  if any(l['a']<0 for l in r['lobes']):
   n_signed+=1;vv=[g.external_omega(.13,l['y0']) for l in r['lobes']]
   check(pre+'source changes sign on x>0',min(vv)<0<max(vv),witness_values=vv)
  check(pre+'reported feedback ratio',abs(r['c_out']/r['c_in']-r['ratio'])<1e-9 if abs(r['ratio'])<1e9 else abs(r['c_out']/r['c_in']-r['ratio'])/abs(r['ratio'])<1e-14)
  # Exact source inverse independently checked by whole-plane direct quadrature.
  z,w=leggauss(90);t=(z+1)/2;rs=1.5*(t**-2-1);ws=(w/2)*3*t**-3/rs
  z,w=leggauss(100);phis=np.pi*z/2;aws=np.pi*w/2
  val=math.fsum(2/math.pi*wr*wa*math.cos(phi)*math.sin(phi)*g.external_omega(rad*math.cos(phi),rad*math.sin(phi)) for rad,wr in zip(rs,ws) for phi,wa in zip(phis,aws))
  check(pre+'independent full-plane source strain',abs(val-g.c)<2e-6,c_quad=val,c_exact=g.c)
 check('signed frozen configuration count',n_signed==17,count=n_signed)
 check('total frozen configuration count',len(allcases)==20,count=len(allcases))
 # Exact linear manufactured transport including two finite-time reconstructions.
 # W=(alpha x,mu y), Theta=x^2, Omega=(4/beta)x, center drift zero.
 class LinearFlow(GaussianFlow):
  def __init__(self,beta):
   self.beta=beta;self.lam=(beta-2)/2;self.mu=1+1.5*beta;self.f01=0.;self.g01=0.;self.b0=4/beta
  def field(self,X):
   D=np.diag([self.lam,self.mu]);W=D@np.asarray(X);return W-self.beta*np.asarray(X),W,D-self.beta*np.eye(2),D
 for beta in [2.4,3.,4.]:
  g=LinearFlow(beta)
  for point in [[.3,.7],[1.,-3.],[-2.,.2]]:
   q=g.evaluate(point,r_in=3e-4,rtol=2e-10)
   err=max(abs(q['Theta']-point[0]**2)/(1+point[0]**2),abs(q['Omega']-4/beta*point[0])/(1+abs(point[0])),abs(q['gradient'][0]-2*point[0])/(1+abs(point[0])),abs(q['gradient'][1]))
   check('manufactured characteristic '+str((beta,point)),q['status']=='COMPLETE' and err<2e-7,error=err)
 # Symmetric exact source and the constructed transport reflection.
 r=allcases['2.5|1,2.87,1.0|-1.0,-2.87,1.0']['data'];g=SignedGaussianFlow(r['c_in'],r['lobes'])
 check('antisymmetric source zero drift/mixed center coefficient',abs(g.u0)<1e-14 and abs(g.ax_y0)<1e-14)
 for point in [[.3,.7],[1.5,3.],[2.,-5.]]:
  plus=g.evaluate(point,r_in=3e-4);minus=g.evaluate([point[0],-point[1]],r_in=3e-4)
  err=max(abs(plus[k]-minus[k]) for k in ['Theta','Omega'])
  check('antisymmetric source even transported output '+str(point),err<2e-8,error=err)
 # Published negative sample locations are (radius,y), not Cartesian (x,y).
 out['negative_samples']=[]
 for key,c in allcases.items():
  r=c['data']
  if r['unfinished'] or r['G_min']>=0:continue
  radius,y=r['G_min_at'];x=math.sqrt(max(0,radius**2-y**2));g=SignedGaussianFlow(r['c_in'],r['lobes'])
  q=g.evaluate([x,y],r_in=3e-4,rtol=2e-10)
  row={'case':key,'point':[x,y],'radius':radius,'reported_G':r['G_min'],'own_G':q.get('Omega',0)/x,**q};out['negative_samples'].append(row)
  check(key+': negative transported witness',q['status']=='COMPLETE' and row['own_G']<0,own_G=row['own_G'],reported_G=r['G_min'])
 out.update(ended_utc=now(),seconds=time.monotonic()-start,passed=sum(x['pass'] for x in cc),total=len(cc),status='PASS' if all(x['pass'] for x in cc) else 'FAIL')
 save(ROOT/'controls.json',out);print(json.dumps({k:v for k,v in out.items() if k not in ['checks','negative_samples']},indent=2),flush=True)
 return out['status']=='PASS'

def run(allcases,planpath):
 plan=json.loads(Path(planpath).read_text());started=time.monotonic()
 out={'started_utc':now(),'pid':os.getpid(),'plan':plan,'runs':[],'status':'RUNNING','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'characteristics_sha256':hashlib.sha256(Path('code_independent/gaussian_characteristics.py').read_bytes()).hexdigest()}
 save(ROOT/'feedback_status.json',out)
 for k,p in enumerate(plan):
  r=allcases[p['case']]['data'];g=SignedGaussianFlow(r['c_in'],r['lobes']);file=ROOT/f'feedback_{k:02d}_points.jsonl'
  print('START_CASE',k,p,now(),flush=True)
  q=integrate(g,p['nr'],p['na'],p.get('L',1.5),p.get('rin',3e-4),p.get('rtol',2e-9),file)
  q.update(case=p['case'],num_c_out=r['c_out'],c_input=g.c,beta=g.beta,ratio=q['c_out']/g.c if q['c_out'] is not None else None,ended_utc=now())
  out['runs'].append(q);out['seconds_so_far']=time.monotonic()-started;save(ROOT/'feedback_status.json',out);print('CASE_COMPLETE',json.dumps(q),flush=True)
 out.update(status='COMPLETE',ended_utc=now(),seconds=time.monotonic()-started);save(ROOT/'feedback_status.json',out)

if __name__=='__main__':
 resource.setrlimit(resource.RLIMIT_AS,(10*1024**3,10*1024**3))
 parser=argparse.ArgumentParser();parser.add_argument('--controls',action='store_true');parser.add_argument('--plan');args=parser.parse_args();data=cases()
 if args.controls:
  if not controls(data):raise SystemExit('controls failed; inspect controls.json')
 if args.plan:run(data,args.plan)
