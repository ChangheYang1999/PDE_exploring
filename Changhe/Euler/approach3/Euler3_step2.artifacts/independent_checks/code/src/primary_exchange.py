"""Independent scalar-potential reconstruction of the primary exchange format.

Uses the explicit Legendre polynomial formula and third Cartesian product jets.
No primary numerical source is imported. See theory/primary_exchange/PROOF.md.
"""
import json, math, hashlib
from pathlib import Path
import numpy as np
import torch
from third_jets import BatchJet3


def jet_sum(jet):
    return BatchJet3(*(v.sum(dim=1, keepdim=True) for v in (jet.v, jet.g, jet.h, jet.t)))


def jet_cat(jets):
    return BatchJet3(*(torch.cat([getattr(j, key) for j in jets], dim=1) for key in ('v','g','h','t')))


def jet_part(jet, part):
    return BatchJet3(*(getattr(v, part) for v in (jet.v, jet.g, jet.h, jet.t)))


def polynomial_harmonics(points, modes):
    """Real solid harmonics without the Condon-Shortley sign, including jets."""
    xyz = [BatchJet3.coordinate(points, i) for i in range(3)]
    one = xyz[0]*0+1
    rho = sum(v*v for v in xyz)
    cy = BatchJet3(*(v.to(torch.complex128) for v in (xyz[1].v, xyz[1].g, xyz[1].h, xyz[1].t)))
    w = xyz[0]+cy*1j
    top = max(int(q[0]) for q in modes)
    zp, wp, rp = [one], [one+0j], [one]
    for j in range(top):
        zp.append(zp[-1]*xyz[2]); wp.append(wp[-1]*w); rp.append(rp[-1]*rho)
    values = {}
    out = []
    for ell, m, kind in modes:
        ell, m, kind = int(ell), int(m), int(kind)
        if (ell,m) not in values:
            pol = one*0
            for j in range((ell-m)//2+1):
                c = (-1)**j * math.factorial(2*ell-2*j) / (2**ell*math.factorial(j)*math.factorial(ell-j)*math.factorial(ell-2*j-m))
                pol = pol+c*zp[ell-2*j-m]*rp[j]
            normal = math.sqrt((2*ell+1)*math.factorial(ell-m)/(4*math.pi*math.factorial(ell+m)))
            values[ell,m] = normal*wp[m]*pol
        h = values[ell,m]
        out.append(jet_part(h, 'real' if kind==0 else 'imag')*(1 if m==0 else math.sqrt(2)))
    return jet_cat(out)


class PrimaryExchangeField:
    def __init__(self, directory, device='cpu', chunk=512):
        self.directory = Path(directory).resolve(); self.device=device; self.chunk=chunk
        manifest=json.loads((self.directory/'SHA256.json').read_text())
        self.checksums={}
        for name, expected in manifest.items():
            path=self.directory/name
            if path.parent!=self.directory:raise ValueError('Invalid exchange path')
            digest=hashlib.sha256(path.read_bytes()).hexdigest()
            if digest!=expected:raise ValueError(f'Exchange checksum mismatch: {name}')
            self.checksums[name]=digest
        self.meta=json.loads((self.directory/'meta.json').read_text())
        with np.load(self.directory/'coeffs.npz',allow_pickle=False) as data:
            self.arrays={k:data[k].copy() for k in data.files}
        raw_modes=np.asarray(self.arrays['modes'])
        if raw_modes.ndim!=2 or raw_modes.shape[1]!=3 or not len(raw_modes):raise ValueError('Invalid harmonic mode array')
        self.modes=np.asarray(raw_modes,dtype=int)
        if not np.array_equal(raw_modes,self.modes):raise ValueError('Nonintegral harmonic mode')
        if len({tuple(q) for q in self.modes})!=len(self.modes):raise ValueError('Duplicate harmonic mode')
        self.c_l=float(self.arrays['c_l']);self.omega=float(self.arrays['omega']);self.r0=float(self.arrays['R0'])
        self.alpha=(1-self.c_l)/self.c_l;self.kappa=self.omega/self.c_l
        self.channels=json.loads(str(self.arrays['channels']))
        self.leading_degree=int(self.arrays['L'])
        # The union may carry nonlinear channels above the leading degree.
        # Every pressure grid must see the largest represented angular mode.
        self.lmax=max(self.leading_degree,int(self.modes[:,0].max()))
        if self.lmax>8:self.chunk=min(self.chunk,256)
        if not 0.4<self.c_l<.5 or self.omega==0 or self.r0<=0:raise ValueError('Exchange outside target parameter class')
        if self.meta['c_l']!=self.c_l or self.meta['omega']!=self.omega or self.meta['R0']!=self.r0:raise ValueError('Metadata parameter mismatch')
        if any(q[0]<1 or q[1]<0 or q[1]>q[0] or q[2] not in (0,1) for q in self.modes):raise ValueError('Invalid harmonic modes')
        if any(q[1]==0 and q[2]!=0 for q in self.modes):raise ValueError('Null sine mode')
        for name in ['A','C','B','D','E']:
            values=np.asarray(self.arrays[name])
            if values.ndim!=2 or values.shape[1]!=len(self.modes) or not np.isfinite(values).all():raise ValueError(f'Invalid coefficient matrix: {name}')
            if name in ('A','C') and not len(values):raise ValueError('Missing leading coefficient rows')
        self.coeff={name:torch.tensor(self.arrays[name],device=device,dtype=torch.float64) for name in ['A','C','B','D','E']}
        lookup={tuple(q):j for j,q in enumerate(self.modes)}
        self.partner=[lookup[(int(l),int(m),1-int(t))] if m else j for j,(l,m,t) in enumerate(self.modes)]
        self.sign=torch.tensor([1 if t else -1 for l,m,t in self.modes],device=device,dtype=torch.float64)
        self.ms=torch.tensor(self.modes[:,1],device=device,dtype=torch.float64)
        self.ls=torch.tensor(self.modes[:,0],device=device,dtype=torch.float64)

    def potentials(self, points, exterior=False):
        xyz=[BatchJet3.coordinate(points,i) for i in range(3)];rho=sum(v*v for v in xyz)
        if exterior and torch.any(rho.v<=0):raise ValueError('Homogeneous tail undefined at origin')
        ss=(rho if exterior else rho+self.r0**2).power_positive(.5)
        angle=(ss*(1/self.r0)).log()*self.kappa
        h=polynomial_harmonics(points,self.modes)
        phase=angle*self.ms
        twisted=h*phase.cos()+h.select(self.partner)*(phase.sin()*self.sign)
        if exterior:
            cheb=[rho*0+1]
        else:
            xx=(ss-self.r0)*(ss+self.r0).power_positive(-1)
            tt=2*xx-1
            length=max(len(v) for v in self.coeff.values())
            cheb=[rho*0+1,tt]
            for k in range(2,length):cheb.append(2*tt*cheb[-1]-cheb[-2])
        def polynomial(name):
            coeff=self.coeff[name]
            if exterior:return (rho*0+1)*coeff.sum(0)
            answer=cheb[0]*coeff[0]
            for k in range(1,len(coeff)):answer=answer+cheb[k]*coeff[k]
            return answer
        sratio=ss*(1/self.r0)
        t=twisted*sratio.power_positive(-self.alpha-self.ls)*polynomial('A')
        s=twisted*sratio.power_positive(1-self.alpha-self.ls)*polynomial('C')
        if not exterior and any(len(self.coeff[name]) for name in ['B','D','E']):
            r1=self.channels.get('R1') or self.r0
            count=int(self.channels['core_damp'])
            if count<0 or float(r1)<=0:raise ValueError('Invalid core damping')
            f=rho*(rho+float(r1)**2).power_positive(-1);damp=rho*0+1
            for _ in range(count):damp=damp*f
            if len(self.coeff['B']):t=t+twisted*damp*sratio.power_positive(-2*self.alpha-1-self.ls)*polynomial('B')
            if len(self.coeff['D']):s=s+twisted*damp*sratio.power_positive(-2*self.alpha-self.ls)*polynomial('D')
            if len(self.coeff['E']):s=s+h*damp*sratio.power_positive(-2*self.ls-1)*polynomial('E')*(self.ls>=2)
        return jet_sum(t),jet_sum(s)

    def torch_values(self,points,exterior=False):
        t,s=self.potentials(points,exterior)
        tg,th=t.g[:,0],t.h[:,0];sg,sh,st=s.g[:,0],s.h[:,0],s.t[:,0]
        lap=torch.diagonal(sh,dim1=-2,dim2=-1).sum(-1)
        dlap=torch.einsum('nkkj->nj',st)
        identity=torch.eye(3,device=points.device,dtype=points.dtype)
        u=torch.linalg.cross(tg,points)+2*sg+torch.einsum('nij,nj->ni',sh,points)-points*lap[:,None]
        du_t=torch.linalg.cross(th.transpose(1,2),points[:,None,:].expand_as(th),dim=-1).transpose(1,2)
        du_t=du_t+torch.linalg.cross(tg[:,None,:].expand_as(th),identity[None,:,:].expand_as(th),dim=-1).transpose(1,2)
        du=du_t+3*sh+torch.einsum('nikj,nk->nij',st,points)-lap[:,None,None]*identity[None,:,:]-points[:,:,None]*dlap[:,None,:]
        return u,du

    def values(self,points,exterior=False):
        points=np.asarray(points,dtype=float);uu=[];dd=[]
        with torch.no_grad():
            for start in range(0,len(points),self.chunk):
                y=torch.as_tensor(points[start:start+self.chunk],device=self.device,dtype=torch.float64)
                u,d=self.torch_values(y,exterior);uu.append(u.cpu().numpy());dd.append(d.cpu().numpy())
        return np.concatenate(uu),np.concatenate(dd)

    def source(self,points,exterior=False):
        _,d=self.values(points,exterior)
        return np.einsum('nij,nji->n',d,d)
