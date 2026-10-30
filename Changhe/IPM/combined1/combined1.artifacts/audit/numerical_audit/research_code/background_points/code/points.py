"""Independent radial Fourier evaluation of background violations."""
from pathlib import Path
from datetime import datetime,timezone
from math import comb
import sys,json,hashlib,time
from flint import ctx,arb,acb
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import Radial,ar,q

class Point:
 def __init__(self,model,x,y,maxd=7):
    self.model=model;self.x=ar(q(x));self.y=ar(q(y));self.r2=self.x**2+self.y**2;self.r=self.r2.sqrt()
    self.R=1+self.r2;self.u=1/self.R;self.t=self.r2/self.R
    self.rp={j:self.R**ar(p) for j,p in model.p.items()};self.rd={d:self.r**(-d) for d in range(maxd+1)}
    maxn=2*max(m for j,m,k in model.state['order'])+maxd
    z=acb(self.x/self.r,self.y/self.r);self.powers=[acb(1)]
    for _ in range(maxn):self.powers.append(self.powers[-1]*z)
    self.cache={}
 def chi(self,x,y):
    key=x,y
    if key in self.cache:return self.cache[key]
    value=arb(0)
    for (j,n),P in self.model.deriv(x,y).items():
        trig=self.powers[n].imag if y%2 else self.powers[n].real
        value+=self.rp[j]*self.rd[x+y]*self.model.poly_arb(P,self.t,self.u)*trig
    self.cache[key]=value;return value
 def rho(self,x,y):return -self.chi(x+2,y+1)-self.chi(x,y+3)
 def velocity(self,x,y):return [-self.chi(x+1,y+2),self.chi(x+2,y+1)]
 def tensor(self,d,velocity=False):
    sq=arb(0)
    for x in range(d+1):
        values=self.velocity(x,d-x) if velocity else [self.rho(x,d-x)]
        sq+=comb(d,x)*sum((v*v for v in values),arb(0))
    return sq.sqrt()
 def matrices(self):
    c=ar(self.model.c);u1,u2=self.velocity(0,0);radial=c*self.r2+self.x*u1+self.y*u2
    a,b,d,e=self.chi(2,2),self.chi(3,1),self.chi(0,4),self.chi(1,3)
    def eig(a,b,d):return (a+d-((a-d)**2+4*b*b).sqrt())/2
    w1=-radial/(5*self.R);w2=16*radial/(5*(1+4*self.r2))
    return {'M':eig(2*c+1-2*a-d,b,2*c+1+a),
            'M1_unweighted':eig(1-d,e,1-a),
            'M1_weighted':eig(1+w1-d,e,1+w1-a),
            'M2_weighted':eig(1-c+w2+a-d,(3*e-b)/2,1-c+w2-2*a)}

def run(name):
    ctx.prec=768;start=time.monotonic();path=ROOT/f'research/refit_audit/data/{name}_canonical.json'
    model=Radial(path);prior=json.loads((ROOT/'research/background_points/data/prior_P54_P58.json').read_text())
    rows=[]
    claims=[c for c in prior['claims'] if c['reference']=='nb_'+name+'_exact']
    if name=='b6':claims=[{'point':['3','4'],'quantity':'M2_weighted','contract':'1/2','direction':'lower'},
                         {'point':['0','1/5'],'quantity':'D2rho','contract':'3'},
                         {'point':['3','4'],'quantity':'S_4','contract':'512'}]
    cache={}
    for claim in claims:
        x,y=claim['point'];point=cache.setdefault((x,y),Point(model,x,y));qty=claim['quantity']
        if qty=='S_U':value=point.R.sqrt()*point.tensor(3,True)
        elif qty=='S_3':value=point.R*point.tensor(3)
        elif qty=='S_4':value=point.R*point.tensor(4)
        elif qty=='D2rho':value=point.tensor(2)
        else:value=point.matrices()[qty]
        cap=ar(q(claim['contract']));violation=value<cap if claim.get('direction')=='lower' else value>cap
        assert violation,(name,claim,value)
        row={'point':[x,y],'quantity':qty,'cap':str(claim['contract']),'direction':claim.get('direction','upper'),
             'value':value.str(60),'strict_violation':bool(violation)}
        rows.append(row);print(name,row,'seconds',time.monotonic()-start,flush=True)
    out={'candidate':name,'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
         'canonical_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_generator_sha256':model.state['source_sha256'],
         'precision_bits':ctx.prec,'claims':rows,'elapsed_seconds':time.monotonic()-start}
    (ROOT/f'research/background_points/verification/{name}_violations.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    for name in sys.argv[1:] or ['d2','Mpen2','b6']:run(name)
