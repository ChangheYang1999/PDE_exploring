import json,datetime
from pathlib import Path
import numpy as np
from independent_residuals import residual_table,pointwise_ratio
from plane_quadrature import Rule

class Manufactured:
    beta=2.5
    def F(self,x,y):return (1+.5*x*x+.25*y*y)*np.exp(-.5*(x*x+y*y))
    def G(self,x,y):return 4*(3-x*x-y*y)*np.exp(-x*x-y*y)
    def H(self,x,y):return np.exp(-x*x-y*y)
    def Theta(self,x,y):return y*self.F(x,y)
    def Omega(self,x,y):return x*y*self.G(x,y)
    def Psi(self,x,y):return x*y*self.H(x,y)
    def exact(self,pts):
        x,y=pts[:,0],pts[:,1];r2=x*x+y*y;e=np.exp(-r2);e2=np.exp(-r2/2);P=1+.5*x*x+.25*y*y
        u1=-x*(1-2*y*y)*e;u2=y*(1-2*x*x)*e
        a=self.beta-(1-2*y*y)*e;b=self.beta+(1-2*x*x)*e
        tx=x*y*(1-P)*e2;ty=(P+.5*y*y-y*y*P)*e2
        ox=4*y*e*((3-r2)-2*x*x*(4-r2));oy=4*x*e*((3-r2)-2*y*y*(4-r2))
        rt=(self.beta*x+u1)*tx+(self.beta*y+u2)*ty-(self.beta-2)*self.Theta(x,y)
        ro=(self.beta*x+u1)*ox+(self.beta*y+u2)*oy+self.Omega(x,y)-tx
        fx=x*(1-P)*e2;fy=y*(.5-P)*e2
        gx=8*x*(r2-4)*e;gy=8*y*(r2-4)*e
        dt=a*x*fx+b*y*fy+(b-self.beta+2)*self.F(x,y)
        do=a*x*gx+b*y*gy+(a+b+1)*self.G(x,y)-(1-P)*e2
        return {'R_Theta':rt,'R_Omega':ro,'D_Theta':dt,'D_Omega':do}

class ForbiddenGauge:
    beta=3.0
    def F(self,x,y):return np.ones(np.broadcast(x,y).shape)
    def G(self,x,y):return np.zeros(np.broadcast(x,y).shape)
    def H(self,x,y):return np.full(np.broadcast(x,y).shape,-2.)
    def Theta(self,x,y):return y*self.F(x,y)
    def Omega(self,x,y):return x*y*self.G(x,y)
    def Psi(self,x,y):return x*y*self.H(x,y)

pts=np.array([[0,0],[.3,0],[0,.4],[1e-12,.4],[.3,1e-12],[.3,.2],[1.1,-.7],[2,.5]])
rows=[]
rule=Rule(radial=96,angular_panels=32,map_power=6,outer_multiplier=1.5,outer_minimum=1.5)
for h in [.01,.004,.0016]:
    obj=Manufactured();a,s=residual_table(obj,pts,rule,hrel=h);ex=obj.exact(pts)
    errors={key:float(np.max(np.abs(a[key]-v))) for key,v in ex.items()}
    errors['E']=float(np.max(np.abs(a['E'])));errors['D_E']=float(np.max(np.abs(a['D_E'])))
    rows.append({'case':'manufactured','hrel':h,'errors':errors,'summary':s})
    print(h,errors,flush=True)
a,s=residual_table(ForbiddenGauge(),pts,rule,hrel=.004)
rows.append({'case':'forbidden_affine_gauge','summary':s})
print('gauge',s['center'],'RTheta',s['R_Theta'],'DTheta',s['D_Theta'],'inverse_Psi_discrepancy',s['max_abs_Psi_inverse_discrepancy'],flush=True)
ratio,meta=pointwise_ratio(np.array([0,1,1e-310],dtype=np.longdouble),np.array([0,0,1e-310],dtype=np.longdouble))
print('ratio_zero_test',ratio,meta,flush=True)
assert ratio[0]==0 and np.isinf(ratio[1]) and ratio[2]==1
assert s['center']['canonical_c']==0 and s['D_Theta']['max_abs']>1.9
assert min(r['errors']['D_E'] for r in rows if r['case']=='manufactured')<1e-6
Path('runs/independent_residuals_manufactured.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'points':pts.tolist(),'rows':rows,'zero_test':meta},indent=2)+'\n')
