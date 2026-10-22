"""Independent stream-only B2 reduction, packet128.

Analytic spatial derivatives of monomial stream terms; horizontal quadrature.
No numerics-lane imports, automatic differentiation, Fourier/spline calculus.
"""
from collections import OrderedDict
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad_vec
from stream_basis import derivative,combine,evaluate_terms
from free_beta_stream import make_chart,divide_terms,metrics

KEYS=('av','bv','ay','byv','Q','Qx','Qy','Qxy','Qyy')

def stream_rows(basis):
    out=[]
    for p in basis.psi:
        av=divide_terms(p['U1'],1);q=divide_terms(p['Omega'],1)
        qx=derivative(q,0,basis.s);qy=derivative(q,1,basis.s)
        out.append({'av':av,'bv':p['U2'],'ay':derivative(av,1,basis.s),
            'byv':derivative(p['U2'],1,basis.s),'Q':q,'Qx':qx,'Qy':qy,
            'Qxy':derivative(qx,1,basis.s),'Qyy':derivative(qy,1,basis.s)})
    return out

def rows_from_terms(terms,s):
    rows=[]
    for psi in terms:
        px=derivative(psi,0,s);py=derivative(psi,1,s)
        omega=combine((-1,derivative(px,0,s)),(-1,derivative(py,1,s)))
        gauge=float(evaluate_terms(px,0.,0.,s))
        rows.append({'U1':combine((-1,py)), 'U2':combine((1,px),(-gauge,{(0,0,0,0):1})), 'Omega':omega})
    class Holder:pass
    b=Holder();b.psi=rows;b.s=s
    return stream_rows(b)

def matrices(rows,s,points):
    p=np.asarray(points,float);x,y=p.T
    return {key:np.stack([evaluate_terms(row[key],x,y,s)for row in rows],axis=1) for key in KEYS}

def horizontal_nodes(points,order=32,rule='sinh'):
    p=np.asarray(points,float);x,y=p.T;v,w=leggauss(order);v=(v+1)/2;w=w/2
    if rule=='linear':
        t=np.broadcast_to(v,(len(p),order));weights=np.broadcast_to(v*w,t.shape)
    elif rule=='sinh':
        ell=np.arcsinh(x);u=ell[:,None]*v
        scale=np.divide(ell,x,out=np.ones_like(x),where=abs(x)>=1e-3)
        small=abs(x)<1e-3
        scale[small]=1-x[small]**2/6+3*x[small]**4/40
        sinhc=np.divide(np.sinh(u),u,out=np.ones_like(u),where=abs(u)>=1e-3)
        smallu=abs(u)<1e-3
        sinhc[smallu]=1+u[smallu]**2/6+u[smallu]**4/120
        t=v[None,:]*scale[:,None]*sinhc
        weights=w[None,:]*scale[:,None]*t*np.cosh(u)
    else:raise ValueError(rule)
    nodes=np.stack((x[:,None]*t,np.broadcast_to(y[:,None],t.shape)),axis=-1)
    return nodes.reshape(-1,2),weights

def projected(data,base,chart):
    return {key:(m@base,m@chart)for key,m in data.items()}

def calculate(data,z,points,beta,with_jac=False):
    q={k:v+M@z for k,(v,M)in data.items()};x,y=np.asarray(points).T
    q['A']=beta+q['av'];q['B']=beta*y+q['bv'];q['By']=beta+q['byv']
    A,B,Q,Qx,Qy,Qxy,Qyy,Ay,By=(q[k]for k in ['A','B','Q','Qx','Qy','Qxy','Qyy','ay','By'])
    H=(A+1)*Q+x*A*Qx+B*Qy
    Hy=Ay*(Q+x*Qx)+(A+1)*Qy+x*A*Qxy+By*Qy+B*Qyy
    q.update(H=H,Hy=Hy)
    if with_jac:
        j={k:M for k,(v,M)in data.items()};col=lambda a:a[:,None]
        JH=j['av']*col(Q+x*Qx)+col(A+1)*j['Q']+col(x*A)*j['Qx']+j['bv']*col(Qy)+col(B)*j['Qy']
        JHy=j['ay']*col(Q+x*Qx)+col(Ay)*(j['Q']+col(x)*j['Qx'])+j['av']*col(Qy+x*Qxy)+col(A+1)*j['Qy']+col(x*A)*j['Qxy']+j['byv']*col(Qy)+col(By)*j['Qy']+j['bv']*col(Qyy)+col(B)*j['Qyy']
        q.update(JH=JH,JHy=JHy,JA=j['av'],JB=j['bv'])
    return q

class PrimitiveProblem:
    def __init__(self,basis,points,order=32,rule='sinh',regularization=0.,reference_beta=None,weight_power=None,rows=None):
        self.basis=basis;self.beta=basis.beta;self.points=np.asarray(points,float);self.order=order;self.rule=rule;self.reg=regularization
        self.rows=stream_rows(basis)if rows is None else rows
        self.nodepoints,self.quadweights=horizontal_nodes(self.points,order,rule)
        self.center=projected(matrices(self.rows,basis.s,self.points),basis.Cbase,basis.Cnull)
        self.nodes=projected(matrices(self.rows,basis.s,self.nodepoints),basis.Cbase,basis.Cnull)
        self.size=basis.Cnull.shape[1];self.last=None
        s0=1/(reference_beta if reference_beta else self.beta)
        self.weight=np.sqrt(1+(self.points**2).sum(axis=1))**(weight_power if weight_power is not None else 1+3*s0)/basis.a0
        self.scale=1/np.sqrt(len(self.points))
    def integrate(self,v):
        return np.einsum('ij,ij...->i...',self.quadweights,v.reshape((len(self.points),self.order)+v.shape[1:]))
    def fields(self,z,with_jac=False):
        e=calculate(self.center,z,self.points,self.beta,with_jac);n=calculate(self.nodes,z,self.nodepoints,self.beta,with_jac)
        S=self.integrate(n['H']);Sy=self.integrate(n['Hy'])
        terms=np.column_stack((e['A']*e['H'],e['B']*Sy,-(self.beta-2)*S))
        e.update(S=S,Sy=Sy,RF=terms.sum(axis=1),NF=abs(terms).sum(axis=1),F_terms=terms,
            Theta=self.points[:,0]**2*S,Theta_y=self.points[:,0]**2*Sy,Theta_x_intended=self.points[:,0]*e['H'],Omega=self.points[:,0]*e['Q'])
        if with_jac:
            e['JS']=self.integrate(n['JH']);e['JSy']=self.integrate(n['JHy'])
            e['JR']=e['JA']*e['H'][:,None]+e['A'][:,None]*e['JH']+e['JB']*Sy[:,None]+e['B'][:,None]*e['JSy']-(self.beta-2)*e['JS']
        return e
    def residual(self,z):
        f=self.fields(z,False);self.last=(z.copy(),f)
        r=self.scale*self.weight*f['RF']
        return np.r_[r,self.reg*z]if self.reg else r
    def jacobian(self,z):
        f=self.fields(z,True);J=self.scale*self.weight[:,None]*f['JR']
        return np.vstack((J,self.reg*np.eye(self.size)))if self.reg else J
    def diagnostics(self,z):
        f=self.fields(z);out={'thermal_divided':metrics(f['RF'],f['NF'],self.points),
            'vorticity_equation':'exact primitive enforces it; finite quadrature derivative must be checked separately',
            'minimum_Theta':float(f['Theta'].min()),'maximum_absolute_Theta':float(abs(f['Theta']).max()),
            'minimum_Omega':float(f['Omega'].min()),'maximum_absolute_Omega':float(abs(f['Omega']).max()),
            'center_a0':float(f['S'][np.linalg.norm(self.points,axis=1).argmin()])if np.any(np.all(self.points==0,axis=1))else None,
            'quadrature_rule':self.rule,'quadrature_order':self.order}
        return out,f

class FreeBetaPrimitive:
    def __init__(self,ni,nj,points,reference_beta,order=32,rule='sinh',regularization=0.):
        self.ni=ni;self.nj=nj;self.points=np.asarray(points);self.reference_beta=reference_beta;self.order=order;self.rule=rule;self.reg=regularization;self.cache=OrderedDict();self.rebuilds=0
    def case(self,beta):
        beta=float(beta)
        if beta not in self.cache:
            b=make_chart(beta,self.ni,self.nj);self.cache[beta]=PrimitiveProblem(b,self.points,self.order,self.rule,self.reg,self.reference_beta);self.rebuilds+=1
        self.cache.move_to_end(beta)
        while len(self.cache)>3:self.cache.popitem(last=False)
        return self.cache[beta]
    def residual(self,z):return self.case(z[0]).residual(z[1:])
    def jacobian(self,z):
        b=z[0];h=min(1e-5*max(1.,abs(b)),(b-2)/4)
        jc=self.case(b).jacobian(z[1:]);jb=(self.case(b+h).residual(z[1:])-self.case(b-h).residual(z[1:]))/(2*h)
        return np.column_stack((jb,jc))

def adaptive_primitive(basis,C,points,eps=2e-10):
    """Separate adaptive u=asinh(s) integration, with explicit core breakpoints."""
    rows=stream_rows(basis);base=np.asarray(C);chart=np.zeros((len(C),0));out=[]
    for x,y in np.asarray(points,float):
        e=calculate(projected(matrices(rows,basis.s,[[x,y]]),base,chart),np.zeros(0),[[x,y]],basis.beta)
        if x==0:S=e['H'][0]/2;Sy=e['Hy'][0]/2;err=0.
        else:
            ell=np.arcsinh(x)
            def integrand(v):
                u=ell*v;s=np.sinh(u);q=calculate(projected(matrices(rows,basis.s,[[s,y]]),base,chart),np.zeros(0),[[s,y]],basis.beta)
                fac=(ell/x)*(s/x)*np.cosh(u)
                return fac*np.array([q['H'][0],q['Hy'][0]])
            split=[np.arcsinh(v)/abs(ell)for v in [.25,1.,4.,16.,64.,256.,1024.]if v<abs(x)]
            (S,Sy),err=quad_vec(integrand,0.,1.,epsabs=eps,epsrel=eps,points=split,limit=300)
        R=e['A'][0]*e['H'][0]+e['B'][0]*Sy-(basis.beta-2)*S
        N=abs(e['A'][0]*e['H'][0])+abs(e['B'][0]*Sy)+abs((basis.beta-2)*S)
        out.append({'point':[float(x),float(y)],'S':float(S),'Sy':float(Sy),'Theta':float(x*x*S),'RF':float(R),'NF':float(N),'estimated_quadrature_error':float(err)})
    return out
