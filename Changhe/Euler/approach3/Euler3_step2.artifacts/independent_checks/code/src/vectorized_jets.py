"""Batched second-order jets for the same Cartesian potentials.

This accelerates fixed-parameter pressure quadrature; the scalar Jet2 and
independent torch.func implementations remain available as references.
"""
import torch

class BatchJet:
    def __init__(self,v,g,h):self.v,self.g,self.h=v,g,h
    @classmethod
    def coordinate(cls,points,i):
        v=points[:,i,None];g=torch.zeros((len(points),1,3),device=points.device,dtype=points.dtype);g[:,:,i]=1
        return cls(v,g,torch.zeros((len(points),1,3,3),device=points.device,dtype=points.dtype))
    def __add__(self,b):
        if isinstance(b,BatchJet):return BatchJet(self.v+b.v,self.g+b.g,self.h+b.h)
        return BatchJet(self.v+b,self.g,self.h)
    __radd__=__add__
    def __neg__(self):return BatchJet(-self.v,-self.g,-self.h)
    def __sub__(self,b):return self+-b
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if not isinstance(b,BatchJet):
            b=torch.as_tensor(b,device=self.v.device,dtype=self.v.dtype)
            return BatchJet(self.v*b,self.g*b[...,None],self.h*b[...,None,None])
        cross=self.g[..., :,None]*b.g[...,None,:]
        return BatchJet(self.v*b.v,self.g*b.v[...,None]+b.g*self.v[...,None],self.h*b.v[...,None,None]+b.h*self.v[...,None,None]+cross+cross.transpose(-1,-2))
    __rmul__=__mul__
    def unary(self,value,first,second):
        return BatchJet(value,self.g*first[...,None],self.h*first[...,None,None]+self.g[..., :,None]*self.g[...,None,:]*second[...,None,None])
    def power_positive(self,p):
        p=torch.as_tensor(p,device=self.v.device,dtype=self.v.dtype)
        return self.unary(self.v**p,p*self.v**(p-1),p*(p-1)*self.v**(p-2))
    def exp(self):
        v=self.v.exp();return self.unary(v,v,v)
    def log(self):return self.unary(self.v.log(),1/self.v,-1/self.v**2)
    def sin(self):return self.unary(self.v.sin(),self.v.cos(),-self.v.sin())
    def cos(self):return self.unary(self.v.cos(),-self.v.sin(),-self.v.cos())
    def select(self,index):return BatchJet(self.v[:,index],self.g[:,index],self.h[:,index])

def combine(jets):
    return type(jets[0])(*[torch.cat([getattr(j,name) for j in jets],dim=1) for name in (('v','g','h','t') if hasattr(jets[0],'t') else ('v','g','h'))])

def potential_jets_batched(basis,points,exterior=False,jet_type=BatchJet):
    cfg=basis.config
    x,y,z=(jet_type.coordinate(points,i) for i in range(3));q=x*x+y*y+z*z
    if not exterior:q=q+cfg.r0**2
    psi=(q*(1/cfg.r0**2)).log()*(cfg.omega/(2*cfg.c_l));cs=psi.cos();sn=psi.sin()
    twisted_xyz=(cs*x-sn*y,sn*x+cs*y,z);plain_xyz=(x,y,z)
    unique=list(dict.fromkeys(tuple(label[1]) for label in basis.labels));lookup={v:i for i,v in enumerate(unique)}
    mons=[]
    for xyz in [twisted_xyz,plain_xyz]:
        powers=[]
        for coordinate in xyz:
            seq=[coordinate*0+1,coordinate]
            for degree in range(2,cfg.degree+1):seq.append(seq[-1]*coordinate)
            powers.append(seq)
        for triple in unique:mons.append(powers[0][triple[0]]*powers[1][triple[1]]*powers[2][triple[2]])
    mon=combine(mons)
    features=[basis.radial_feature(label[2]) for label in basis.labels]
    selection=torch.tensor([lookup[tuple(label[1])]+(0 if feat[1] else len(unique)) for label,feat in zip(basis.labels,features)],device=points.device)
    mon=mon.select(selection)
    p=torch.tensor([feat[0] for feat in features],device=points.device,dtype=points.dtype)
    degree=torch.tensor([sum(label[1]) for label in basis.labels],device=points.device,dtype=points.dtype)
    beta=(1-basis.alpha-degree)/2-p
    scalar=mon*q.power_positive(beta)*(cfg.r0**(2*p))
    if not exterior and any(basis.gaussian_scale(label[2]) is not None for label in basis.labels):
        inverse=torch.tensor([0. if basis.gaussian_scale(label[2]) is None else 1/(cfg.r0*basis.gaussian_scale(label[2]))**2 for label in basis.labels],device=points.device,dtype=points.dtype)
        scalar=scalar*((x*x+y*y+z*z)*(-inverse)).exp()
    if exterior:scalar=scalar*torch.tensor([1. if label[2]==0 else 0. for label in basis.labels],device=points.device,dtype=points.dtype)
    masks=[torch.tensor([1. if label[0]==i else 0. for label in basis.labels],device=points.device,dtype=points.dtype) for i in range(3)]
    twisted=torch.tensor([1. if feat[1] else 0. for feat in features],device=points.device,dtype=points.dtype)
    c=cs*twisted+(1-twisted);s=sn*twisted
    parts=(scalar*(c*masks[0]+s*masks[1]),scalar*(-s*masks[0]+c*masks[1]),scalar*masks[2])
    return parts

def basis_jets_batched(basis,points,exterior=False,include_potential=False):
    parts=potential_jets_batched(basis,points,exterior)
    g=torch.stack([v.g for v in parts],dim=2);h=torch.stack([v.h for v in parts],dim=2)
    u=torch.stack((g[:,:,2,1]-g[:,:,1,2],g[:,:,0,2]-g[:,:,2,0],g[:,:,1,0]-g[:,:,0,1]),dim=2)
    d=torch.stack((h[:,:,2,1,:]-h[:,:,1,2,:],h[:,:,0,2,:]-h[:,:,2,0,:],h[:,:,1,0,:]-h[:,:,0,1,:]),dim=2)
    if include_potential:return u,d,torch.stack([v.v for v in parts],dim=2),g
    return u,d

def stable_linear_basis_batched(basis,points,exterior=False):
    """The established potential commutator evaluated on all basis columns."""
    from equations import j_action
    u,d,a,da=basis_jets_batched(basis,points,exterior,include_potential=True)
    cfg=basis.config;q=torch.sum(points*points,dim=-1)+(0 if exterior else cfg.r0**2)
    sf=torch.zeros_like(q) if exterior else cfg.r0**2/q
    gs=torch.zeros_like(points) if exterior else -2*cfg.r0**2*points/q[:,None]**2
    ka=j_action(a)-torch.einsum('nbij,nj->nbi',da,j_action(points))
    ku=j_action(u)-torch.einsum('nbij,nj->nbi',d,j_action(points))
    sa=torch.linalg.cross(gs[:,None,:].expand_as(a),a,dim=-1)+sf[:,None,None]*u
    ska=torch.linalg.cross(gs[:,None,:].expand_as(ka),ka,dim=-1)+sf[:,None,None]*ku
    features=[basis.radial_feature(label[2]) for label in basis.labels]
    power=torch.tensor([f[0] for f in features],device=points.device,dtype=points.dtype)
    twist=torch.tensor([f[1] for f in features],device=points.device,dtype=points.dtype)
    degree=torch.tensor([sum(v[1]) for v in basis.labels],device=points.device,dtype=points.dtype)
    beta=(1-basis.alpha-degree)/2-power
    result=-2*cfg.c_l*power[None,:,None]*u-2*cfg.c_l*beta[None,:,None]*sa+cfg.omega*(twist[None,:,None]*ska+(1-twist[None,:,None])*ku)
    if not exterior and any(basis.gaussian_scale(label[2]) is not None for label in basis.labels):
        inverse=torch.tensor([0. if basis.gaussian_scale(label[2]) is None else 1/(cfg.r0*basis.gaussian_scale(label[2]))**2 for label in basis.labels],device=points.device,dtype=points.dtype)
        rr=torch.sum(points*points,dim=-1)
        result=result-2*cfg.c_l*inverse[None,:,None]*(rr[:,None,None]*u+2*torch.linalg.cross(points[:,None,:].expand_as(a),a,dim=-1))
    return result
