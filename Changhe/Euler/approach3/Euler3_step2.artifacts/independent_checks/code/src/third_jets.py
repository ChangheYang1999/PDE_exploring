"""Explicit third-order Cartesian jets for U, DU, D2U and vorticity checks."""
import torch
from vectorized_jets import potential_jets_batched


def symmetric_hg(h,g):
    a=h[..., :, :,None]*g[...,None,None,:]
    return a+a.transpose(-1,-2)+a.transpose(-1,-3)

class BatchJet3:
    def __init__(self,v,g,h,t):self.v,self.g,self.h,self.t=v,g,h,t
    @classmethod
    def coordinate(cls,points,i):
        v=points[:,i,None]
        g=torch.zeros((len(points),1,3),device=points.device,dtype=points.dtype);g[:,:,i]=1
        return cls(v,g,torch.zeros((*v.shape,3,3),device=points.device,dtype=points.dtype),torch.zeros((*v.shape,3,3,3),device=points.device,dtype=points.dtype))
    def __add__(self,b):
        if isinstance(b,BatchJet3):return BatchJet3(self.v+b.v,self.g+b.g,self.h+b.h,self.t+b.t)
        return BatchJet3(self.v+b,self.g,self.h,self.t)
    __radd__=__add__
    def __neg__(self):return BatchJet3(-self.v,-self.g,-self.h,-self.t)
    def __sub__(self,b):return self+-b
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if not isinstance(b,BatchJet3):
            b=torch.as_tensor(b,device=self.v.device,dtype=self.v.dtype)
            return BatchJet3(self.v*b,self.g*b[...,None],self.h*b[...,None,None],self.t*b[...,None,None,None])
        cross=self.g[..., :,None]*b.g[...,None,:]
        return BatchJet3(self.v*b.v,self.g*b.v[...,None]+b.g*self.v[...,None],
            self.h*b.v[...,None,None]+b.h*self.v[...,None,None]+cross+cross.transpose(-1,-2),
            self.t*b.v[...,None,None,None]+b.t*self.v[...,None,None,None]+symmetric_hg(self.h,b.g)+symmetric_hg(b.h,self.g))
    __rmul__=__mul__
    def unary(self,value,first,second,third):
        gg=self.g[..., :,None]*self.g[...,None,:]
        ggg=gg[..., :, :,None]*self.g[...,None,None,:]
        return BatchJet3(value,self.g*first[...,None],self.h*first[...,None,None]+gg*second[...,None,None],
            self.t*first[...,None,None,None]+symmetric_hg(self.h,self.g)*second[...,None,None,None]+ggg*third[...,None,None,None])
    def power_positive(self,p):
        p=torch.as_tensor(p,device=self.v.device,dtype=self.v.dtype)
        return self.unary(self.v**p,p*self.v**(p-1),p*(p-1)*self.v**(p-2),p*(p-1)*(p-2)*self.v**(p-3))
    def exp(self):
        v=self.v.exp();return self.unary(v,v,v,v)
    def log(self):return self.unary(self.v.log(),1/self.v,-1/self.v**2,2/self.v**3)
    def sin(self):return self.unary(self.v.sin(),self.v.cos(),-self.v.sin(),-self.v.cos())
    def cos(self):return self.unary(self.v.cos(),-self.v.sin(),-self.v.cos(),self.v.sin())
    def select(self,index):return BatchJet3(self.v[:,index],self.g[:,index],self.h[:,index],self.t[:,index])

def basis_third_jets(basis,points,exterior=False):
    parts=potential_jets_batched(basis,points,exterior,jet_type=BatchJet3)
    g=torch.stack([v.g for v in parts],dim=2);h=torch.stack([v.h for v in parts],dim=2);t=torch.stack([v.t for v in parts],dim=2)
    u=torch.stack((g[:,:,2,1]-g[:,:,1,2],g[:,:,0,2]-g[:,:,2,0],g[:,:,1,0]-g[:,:,0,1]),dim=2)
    d=torch.stack((h[:,:,2,1,:]-h[:,:,1,2,:],h[:,:,0,2,:]-h[:,:,2,0,:],h[:,:,1,0,:]-h[:,:,0,1,:]),dim=2)
    dd=torch.stack((t[:,:,2,1,:,:]-t[:,:,1,2,:,:],t[:,:,0,2,:,:]-t[:,:,2,0,:,:],t[:,:,1,0,:,:]-t[:,:,0,1,:,:]),dim=2)
    return u,d,dd

def curl_and_jacobian(d,dd):
    om=torch.stack((d[...,2,1]-d[...,1,2],d[...,0,2]-d[...,2,0],d[...,1,0]-d[...,0,1]),dim=-1)
    dom=torch.stack((dd[...,2,1,:]-dd[...,1,2,:],dd[...,0,2,:]-dd[...,2,0,:],dd[...,1,0,:]-dd[...,0,1,:]),dim=-2)
    return om,dom

def stable_vorticity_linear_basis(basis,points,exterior=False):
    """Curl of the cancellation-resistant velocity linear operator.

    It is Omega+c_l D Omega y+omega(J Omega-D Omega Jy), evaluated by
    commutators with the represented regularization factors.
    """
    parts=potential_jets_batched(basis,points,exterior,jet_type=BatchJet3)
    a=torch.stack([v.v for v in parts],dim=2)
    da=torch.stack([v.g for v in parts],dim=2)
    ha=torch.stack([v.h for v in parts],dim=2)
    ta=torch.stack([v.t for v in parts],dim=2)
    u=torch.stack((da[:,:,2,1]-da[:,:,1,2],da[:,:,0,2]-da[:,:,2,0],da[:,:,1,0]-da[:,:,0,1]),dim=2)
    d=torch.stack((ha[:,:,2,1,:]-ha[:,:,1,2,:],ha[:,:,0,2,:]-ha[:,:,2,0,:],ha[:,:,1,0,:]-ha[:,:,0,1,:]),dim=2)
    dd=torch.stack((ta[:,:,2,1,:,:]-ta[:,:,1,2,:,:],ta[:,:,0,2,:,:]-ta[:,:,2,0,:,:],ta[:,:,1,0,:,:]-ta[:,:,0,1,:,:]),dim=2)
    vort,dv=curl_and_jacobian(d,dd)
    j=torch.tensor([[0.,-1.,0.],[1.,0.,0.],[0.,0.,0.]],device=points.device,dtype=points.dtype)
    jy=points@j.T
    ka=a@j.T-torch.einsum('nbij,nj->nbi',da,jy)
    ku=u@j.T-torch.einsum('nbij,nj->nbi',d,jy)
    kv=vort@j.T-torch.einsum('nbij,nj->nbi',dv,jy)
    dka=torch.einsum('ij,nbjk->nbik',j,da)-torch.einsum('nbijk,nj->nbik',ha,jy)-da@j
    cfg=basis.config;rr=(points*points).sum(-1)
    r0sq=0. if exterior else cfg.r0**2;q=rr+r0sq
    sf=r0sq/q;gs=-2*r0sq*points/q[:,None]**2
    hs=-2*r0sq*torch.eye(3,device=points.device,dtype=points.dtype)[None,:,:]/q[:,None,None]**2+8*r0sq*points[:,:,None]*points[:,None,:]/q[:,None,None]**3
    lap=torch.diagonal(hs,dim1=-2,dim2=-1).sum(-1)
    def double_curl_product(av,dav,cav,ccav):
        diva=torch.diagonal(dav,dim1=-2,dim2=-1).sum(-1)
        return sf[:,None,None]*ccav+torch.linalg.cross(gs[:,None,:].expand_as(cav),cav,dim=-1)+gs[:,None,:]*diva[:,:,None]-av*lap[:,None,None]+torch.einsum('nij,nbj->nbi',hs,av)-torch.einsum('nbij,nj->nbi',dav,gs)
    sa=double_curl_product(a,da,u,vort)
    ska=double_curl_product(ka,dka,ku,kv)
    features=[basis.radial_feature(label[2]) for label in basis.labels]
    powers=torch.tensor([v[0] for v in features],device=points.device,dtype=points.dtype)
    twisted=torch.tensor([v[1] for v in features],device=points.device,dtype=points.dtype)
    degree=torch.tensor([sum(label[1]) for label in basis.labels],device=points.device,dtype=points.dtype)
    beta=(1-basis.alpha-degree)/2-powers
    result=-2*cfg.c_l*powers[None,:,None]*vort-2*cfg.c_l*beta[None,:,None]*sa+cfg.omega*(twisted[None,:,None]*ska+(1-twisted[None,:,None])*kv)
    if not exterior and any(basis.gaussian_scale(label[2]) is not None for label in basis.labels):
        inverse=torch.tensor([0. if basis.gaussian_scale(label[2]) is None else 1/(cfg.r0*basis.gaussian_scale(label[2]))**2 for label in basis.labels],device=points.device,dtype=points.dtype)
        diva=torch.diagonal(da,dim1=-2,dim2=-1).sum(-1)
        correction=rr[:,None,None]*vort+2*torch.linalg.cross(points[:,None,:].expand_as(u),u,dim=-1)+2*points[:,None,:]*diva[:,:,None]-4*a-2*torch.einsum('nbij,nj->nbi',da,points)
        result=result-2*cfg.c_l*inverse[None,:,None]*correction
    return result
