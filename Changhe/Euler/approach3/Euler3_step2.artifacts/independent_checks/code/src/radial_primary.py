"""Independent radial-derivative evaluation of saved toroidal-poloidal coefficients."""
import math
import numpy as np
import torch
from primary_exchange import PrimaryExchangeField

class RadialJet2:
    def __init__(self,v,d=None,h=None):
        self.v=v;self.d=torch.zeros_like(v) if d is None else d;self.h=torch.zeros_like(v) if h is None else h
    def __add__(self,b):
        if not isinstance(b,RadialJet2):return RadialJet2(self.v+b,self.d,self.h)
        return RadialJet2(self.v+b.v,self.d+b.d,self.h+b.h)
    __radd__=__add__
    def __neg__(self):return self*(-1)
    def __sub__(self,b):return self+-b
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if not isinstance(b,RadialJet2):return RadialJet2(self.v*b,self.d*b,self.h*b)
        return RadialJet2(self.v*b.v,self.d*b.v+self.v*b.d,self.h*b.v+2*self.d*b.d+self.v*b.h)
    __rmul__=__mul__
    def power(self,b):
        v=self.v.pow(b);d=b*self.v.pow(b-1);h=b*(b-1)*self.v.pow(b-2)
        return RadialJet2(v,d*self.d,d*self.h+h*self.d*self.d)
    def log(self):return RadialJet2(self.v.log(),self.d/self.v,self.h/self.v-(self.d/self.v)**2)
    def sin(self):return RadialJet2(self.v.sin(),self.v.cos()*self.d,self.v.cos()*self.h-self.v.sin()*self.d*self.d)
    def cos(self):return RadialJet2(self.v.cos(),-self.v.sin()*self.d,-self.v.sin()*self.h-self.v.cos()*self.d*self.d)
    def select(self,indices):return RadialJet2(*(a[:,indices] for a in [self.v,self.d,self.h]))


def polynomial_coefficients(ell,m,kind):
    coefficient={}
    for j in range((ell-m)//2+1):
        c=(-1)**j*math.factorial(2*ell-2*j)/(2**ell*math.factorial(j)*math.factorial(ell-j)*math.factorial(ell-2*j-m))
        for b in range(m+1):
            w=math.comb(m,b)*(1j)**b
            for a0 in range(j+1):
                for a1 in range(j-a0+1):
                    a2=j-a0-a1;p=(m-b+2*a0,b+2*a1,ell-2*j-m+2*a2);v=c*w*math.factorial(j)/(math.factorial(a0)*math.factorial(a1)*math.factorial(a2));coefficient[p]=coefficient.get(p,0)+v
    factor=math.sqrt((2*ell+1)*math.factorial(ell-m)/(4*math.pi*math.factorial(ell+m)))*(math.sqrt(2) if m else 1)
    return {p:factor*(complex(v).real if kind==0 else complex(v).imag) for p,v in coefficient.items() if (complex(v).real if kind==0 else complex(v).imag)!=0}

class SolidTable:
    def __init__(self,modes,device='cpu'):
        self.modes=np.asarray(modes,dtype=int);self.degree=int(self.modes[:,0].max());derivatives=[()]+[(i,) for i in range(3)]+[(i,j) for i in range(3) for j in range(3)];polys=[]
        for ell,m,kind in self.modes:
            base=polynomial_coefficients(int(ell),int(m),int(kind));row=[]
            for axes in derivatives:
                d={}
                for power,c in base.items():
                    p=list(power)
                    for axis in axes:c*=p[axis];p[axis]-=1
                    if c:d[tuple(p)]=c
                row.append(d)
            polys.append(row)
        self.powers=sorted(set(p for row in polys for d in row for p in d));lookup={p:i for i,p in enumerate(self.powers)};matrix=np.zeros((len(self.powers),len(modes)*13))
        for m,row in enumerate(polys):
            for d,poly in enumerate(row):
                for power,c in poly.items():matrix[lookup[power],13*m+d]=c
        self.matrix=torch.as_tensor(matrix,device=device,dtype=torch.float64)
    def values(self,y):
        powers=[]
        for axis in range(3):
            seq=[torch.ones_like(y[:,axis]),y[:,axis]]
            for _ in range(2,self.degree+1):seq.append(seq[-1]*y[:,axis])
            powers.append(seq)
        mon=torch.stack([powers[0][a]*powers[1][b]*powers[2][c] for a,b,c in self.powers],dim=1);h=(mon@self.matrix).reshape(len(y),len(self.modes),13);return h[:,:,0],h[:,:,1:4],h[:,:,4:].reshape(len(y),len(self.modes),3,3)

class RadialPrimaryExchangeField(PrimaryExchangeField):
    def __init__(self,directory,device='cpu',chunk=4096):
        super().__init__(directory,device,chunk);self.table=SolidTable(self.modes,device);self.radial_ratio=self.omega/self.c_l
    def radial_coefficients(self,rho,exterior=False):
        q=RadialJet2(rho,torch.ones_like(rho));s=(q if exterior else q+self.r0**2).power(.5);sr=s*(1/self.r0);angle=sr.log()*self.radial_ratio;cs=(angle*self.ms).cos();sn=(angle*self.ms).sin()
        if exterior:cheb=[q*0+1]
        else:
            x=q*(s+self.r0).power(-2);tt=2*x-1;cheb=[q*0+1,tt]
            for k in range(2,max(len(v) for v in self.coeff.values())):cheb.append(2*tt*cheb[-1]-cheb[-2])
        def amplitude(name):
            coeff=self.coeff[name]
            if exterior:return (q*0+1)*coeff.sum(0)
            a=cheb[0]*coeff[0]
            for k in range(1,len(coeff)):a=a+cheb[k]*coeff[k]
            return a
        def twisted(a):return a*cs-a.select(self.partner)*self.sign*sn
        tor=sr.power(-self.alpha-self.ls)*twisted(amplitude('A'));pol=sr.power(1-self.alpha-self.ls)*twisted(amplitude('C'))
        if not exterior and any(len(self.coeff[name]) for name in ['B','D','E']):
            ratio=q*(q+float(self.channels.get('R1') or self.r0)**2).power(-1);damp=q*0+1
            for _ in range(int(self.channels['core_damp'])):damp=damp*ratio
            if len(self.coeff['B']):tor=tor+damp*sr.power(-2*self.alpha-1-self.ls)*twisted(amplitude('B'))
            if len(self.coeff['D']):pol=pol+damp*sr.power(-2*self.alpha-self.ls)*twisted(amplitude('D'))
            if len(self.coeff['E']):pol=pol+damp*sr.power(-2*self.ls-1)*amplitude('E')*(self.ls>=2)
        return tor,pol
    def torch_values(self,y,exterior=False):
        rho=(y*y).sum(1,keepdim=True)
        if exterior and bool(torch.any(rho<=0)):raise ValueError('Exterior excludes origin')
        f,g=self.radial_coefficients(rho,exterior);H,h,K=self.table.values(y);A=(self.ls+1)*g.v+2*rho*g.d;Ap=(self.ls+3)*g.d+2*rho*g.h;B=-2*self.ls*g.d;Bp=-2*self.ls*g.h;eye=torch.eye(3,device=y.device,dtype=y.dtype);cross=torch.linalg.cross(h,y[:,None,:].expand_as(h),dim=-1)
        u=(f.v[:,:,None]*cross+A[:,:,None]*h+B[:,:,None]*y[:,None,:]*H[:,:,None]).sum(1)
        dt=2*f.d[:,:,None,None]*cross[:,:,:,None]*y[:,None,None,:]
        dt=dt+f.v[:,:,None,None]*(torch.linalg.cross(K.transpose(-1,-2),y[:,None,None,:].expand_as(K),dim=-1).transpose(-1,-2)+torch.linalg.cross(h[:,:,None,:].expand_as(K),eye[None,None,:,:].expand_as(K),dim=-1).transpose(-1,-2))
        dp=A[:,:,None,None]*K+2*Ap[:,:,None,None]*h[:,:,:,None]*y[:,None,None,:]+B[:,:,None,None]*(eye[None,None,:,:]*H[:,:,None,None]+y[:,None,:,None]*h[:,:,None,:])+2*Bp[:,:,None,None]*H[:,:,None,None]*y[:,None,:,None]*y[:,None,None,:]
        return u,(dt+dp).sum(1)
