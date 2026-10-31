"""Full-space fixed-source Green moments with actual partial-panel quadrature.

The optional radial coefficient cache is a second numerical interpolation,
checked separately. See theory/partial_panel_green/PROOF.md for scope.
"""
import json
from pathlib import Path
import numpy as np
from solid_harmonics import spherical_harmonics,solid_harmonics
from radial_pressure import RadialGreenPressure


def barycentric_matrix(x,nodes,weights):
    x=np.asarray(x,dtype=float).reshape(-1);d=x[:,None]-nodes[None,:]
    equal=d==0;safe=np.where(equal,1.,d);v=weights[None,:]/safe
    v/=v.sum(axis=1)[:,None]
    rows=np.flatnonzero(equal.any(axis=1))
    if len(rows):v[rows]=equal[rows].astype(float)
    return v


class PartialPanelGreen:
    def __init__(self,pressure,partial_order=None):
        self.pressure=pressure;self.labels=np.asarray(pressure.labels);self.ell=self.labels[:,0];self.den=2*self.ell+1;self.lmax=int(self.ell.max())
        self.edges=np.asarray(pressure.metadata['radial_edges']);self.nr=int(pressure.metadata['n_r_per_interval']);self.npanel=len(self.edges)-1
        self.nodes=np.asarray(pressure.nodes);self.weights=np.asarray(pressure.weights);self.q=np.asarray(pressure.source_coefficients)
        assert len(self.nodes)==(self.npanel+1)*self.nr and self.q.shape==(len(self.nodes),len(self.labels))
        self.t,self.gw=np.polynomial.legendre.leggauss(self.nr);self.bw=(-1.)**np.arange(self.nr)*np.sqrt((1-self.t**2)*self.gw)
        self.partial_order=partial_order or max(32,self.nr+8);qnodes,qweights=np.polynomial.legendre.leggauss(self.partial_order);self.qt=(qnodes+1)/2;self.qw=qweights/2
        self.low=np.flatnonzero(np.isin(self.ell,pressure.zero_moments));self.cache={};self.counters={'direct_radii':0,'cached_panels':0,'cached_radii':0}
        modes=len(self.labels);self.inner=np.zeros((len(self.edges),modes),complex);self.outer=np.zeros_like(self.inner);self.inner_abs=np.zeros((len(self.edges),len(self.low)));self.exterior=np.zeros((len(self.edges),len(self.low)),complex);self.exterior_abs=np.zeros_like(self.inner_abs)
        # Validate the meaning and order of every saved finite-panel sample.
        for j,(a,b) in enumerate(zip(self.edges[:-1],self.edges[1:])):
            ix=slice(j*self.nr,(j+1)*self.nr);expected=a+(b-a)*(self.t+1)/2
            if not np.allclose(self.nodes[ix],expected,rtol=1e-13,atol=1e-300):raise ValueError('Saved source panel nodes do not match their metadata')
            if not np.allclose(self.weights[ix],(b-a)*self.gw/2,rtol=1e-13,atol=1e-300):raise ValueError('Saved source panel weights do not match their metadata')
            ss=self.nodes[ix,None];weighted=self.weights[ix,None]*self.q[ix];terms=weighted*b*(ss/b)**(self.ell+2)
            self.inner[j+1]=(a/b)**(self.ell+1)*self.inner[j]+terms.sum(axis=0)
            if len(self.low):self.inner_abs[j+1]=(a/b)**(self.ell[self.low]+1)*self.inner_abs[j]+np.abs(terms[:,self.low]).sum(axis=0)
        ix=slice(self.npanel*self.nr,None);rr=self.edges[-1];ss=self.nodes[ix,None];weighted=self.weights[ix,None]*self.q[ix]
        self.outer[-1]=(weighted*ss*(rr/ss)**self.ell).sum(axis=0)+rr**self.ell*pressure.tail_integral(1-self.ell)
        if len(self.low):
            ee=self.ell[self.low];terms=weighted[:,self.low]*rr*(ss/rr)**(ee+2);tail=np.zeros(len(self.low),complex)
            for degree in pressure.zero_moments:
                mask=ee==degree;tail[mask]=rr**(-degree-1)*pressure.tail_integral(degree+2)[self.low[mask]]
            self.exterior[-1]=terms.sum(axis=0)+tail;self.exterior_abs[-1]=np.abs(terms).sum(axis=0)+np.abs(tail)
        for j in range(self.npanel-1,-1,-1):
            a,b=self.edges[j:j+2];ix=slice(j*self.nr,(j+1)*self.nr);ss=self.nodes[ix,None];weighted=self.weights[ix,None]*self.q[ix]
            self.outer[j]=(a/b)**self.ell*self.outer[j+1]+(weighted*ss*(a/ss)**self.ell).sum(axis=0)
            if a and len(self.low):
                ee=self.ell[self.low];terms=weighted[:,self.low]*a*(ss/a)**(ee+2)
                self.exterior[j]=(b/a)**(ee+1)*self.exterior[j+1]+terms.sum(axis=0);self.exterior_abs[j]=(b/a)**(ee+1)*self.exterior_abs[j+1]+np.abs(terms).sum(axis=0)
        weighted=self.weights[:,None]*self.q
        self.origin_p=np.zeros(modes,complex);self.origin_dp=np.zeros(modes,complex)
        l0=self.ell==0;l1=self.ell==1
        self.origin_p[l0]=(weighted*self.nodes[:,None]).sum(axis=0)[l0]+pressure.tail_integral(1)[l0]
        self.origin_dp[l1]=(weighted.sum(axis=0)[l1]+pressure.tail_integral(0)[l1])/3

    def direct_coefficients(self,radii):
        radii=np.asarray(radii,dtype=float).reshape(-1)
        if np.any(radii<0) or np.any(radii>self.edges[-1]):raise ValueError('Radius outside prepared source grid')
        pc=np.zeros((len(radii),len(self.labels)),complex);dp=np.zeros_like(pc);zero=radii==0;pc[zero]=self.origin_p;dp[zero]=self.origin_dp
        panel=np.minimum(np.searchsorted(self.edges,radii,side='right')-1,self.npanel-1)
        for j in np.unique(panel[~zero]):
            selected=np.flatnonzero((panel==j)&~zero);a,b=self.edges[j:j+2];qpanel=self.q[j*self.nr:(j+1)*self.nr]
            for lo in range(0,len(selected),64):
                ix=selected[lo:lo+64];r=radii[ix];sin=a+(r[:,None]-a)*self.qt;sout=r[:,None]+(b-r[:,None])*self.qt
                sourcein=(barycentric_matrix((2*sin-a-b)/(b-a),self.t,self.bw)@qpanel).reshape(len(r),self.partial_order,-1)
                sourceout=(barycentric_matrix((2*sout-a-b)/(b-a),self.t,self.bw)@qpanel).reshape(len(r),self.partial_order,-1)
                wi=(r[:,None]-a)*self.qw;wo=(b-r[:,None])*self.qw
                iterms=wi[:,:,None]*sourcein*r[:,None,None]*(sin[:,:,None]/r[:,None,None])**(self.ell+2)
                inner=(a/r[:,None])**(self.ell+1)*self.inner[j]+iterms.sum(axis=1)
                outer=(r[:,None]/b)**self.ell*self.outer[j+1]+(wo[:,:,None]*sourceout*sout[:,:,None]*(r[:,None,None]/sout[:,:,None])**self.ell).sum(axis=1)
                if len(self.low):
                    ee=self.ell[self.low];exterms=wo[:,:,None]*sourceout[:,:,self.low]*r[:,None,None]*(sout[:,:,None]/r[:,None,None])**(ee+2)
                    exterior=(b/r[:,None])**(ee+1)*self.exterior[j+1]+exterms.sum(axis=1)
                    ia=(a/r[:,None])**(ee+1)*self.inner_abs[j]+np.abs(iterms[:,:,self.low]).sum(axis=1);ea=(b/r[:,None])**(ee+1)*self.exterior_abs[j+1]+np.abs(exterms).sum(axis=1)
                    inner[:,self.low]=np.where(ea<ia,-exterior,inner[:,self.low])
                pc[ix]=(inner+outer)/self.den;dp[ix]=(-(self.ell+1)*inner+self.ell*outer)/(r[:,None]*self.den)
        self.counters['direct_radii']+=len(radii)
        return pc,dp

    def coefficients(self,radii,cache_order=None):
        if cache_order is None:return self.direct_coefficients(radii)
        if cache_order<8:raise ValueError('At least 8 radial interpolation nodes required')
        radii=np.asarray(radii,dtype=float).reshape(-1)
        if np.any(radii<0) or np.any(radii>self.edges[-1]):raise ValueError('Radius outside prepared source grid')
        pc=np.zeros((len(radii),len(self.labels)),complex);dp=np.zeros_like(pc);panel=np.minimum(np.searchsorted(self.edges,radii,side='right')-1,self.npanel-1)
        for j in np.unique(panel):
            a,b=self.edges[j:j+2];ix=np.flatnonzero(panel==j);key=(int(j),int(cache_order))
            if key not in self.cache:
                tx=-np.cos(np.arange(cache_order)*np.pi/(cache_order-1));rr=a+(b-a)*(tx+1)/2;rr[0]=a;rr[-1]=b
                pp,dd=self.direct_coefficients(rr);bw=(-1.)**np.arange(cache_order);bw[[0,-1]]*=.5;self.cache[key]=(tx,bw,pp,dd);self.counters['cached_panels']+=1
            tx,bw,pp,dd=self.cache[key]
            for lo in range(0,len(ix),1024):
                ii=ix[lo:lo+1024];matrix=barycentric_matrix((2*radii[ii]-a-b)/(b-a),tx,bw);pc[ii]=matrix@pp;dp[ii]=matrix@dd
        self.counters['cached_radii']+=len(radii)
        return pc,dp

    def values(self,points,cache_order=None,batch=512):
        points=np.asarray(points,dtype=float);r=np.linalg.norm(points,axis=1);pc,dp=self.coefficients(r,cache_order);p=np.zeros(len(r),complex);g=np.zeros((len(r),3),complex);zero=r==0
        if np.any(zero):
            y,dh,_=solid_harmonics(points[zero],self.lmax);p[zero]=y@self.origin_p;g[zero]=np.einsum('nki,k->ni',dh,self.origin_dp)
        select=np.flatnonzero(~zero)
        for lo in range(0,len(select),batch):
            ix=select[lo:lo+batch];n=points[ix]/r[ix,None];y,gs,_=spherical_harmonics(n,self.lmax);p[ix]=np.einsum('nk,nk->n',y,pc[ix]);g[ix]=n*np.einsum('nk,nk->n',y,dp[ix])[:,None]+np.einsum('nki,nk->ni',gs,pc[ix]/r[ix,None])
        self.last_imaginary_max={'P':float(np.abs(p.imag).max(initial=0)),'gradP':float(np.abs(g.imag).max(initial=0))}
        return p.real,g.real


def load_saved_common_pressure(directory,n_r):
    """Load immutable source arrays; reconstruct the analytic tail exactly once."""
    directory=Path(directory);record=json.loads((directory/f'pressure_{n_r}.json').read_text());summary=json.loads((directory/'summary.json').read_text());cfg=summary['basis_config'];metadata=record['pressure_metadata']
    p=RadialGreenPressure.__new__(RadialGreenPressure)
    with np.load(directory/f'pressure_{n_r}.npz') as z:
        p.nodes=z['source_nodes'];p.weights=z['source_weights'];p.source_coefficients=z['source_coefficients'];p.labels=z['source_labels']
    p.metadata=metadata.copy();p.lmax=int(metadata['lmax']);p.zero_moments=tuple(metadata['imposed_zero_source_moments']);p.tail_start=float(metadata['radial_edges'][-1]);p.tail=None
    if metadata['leading_tail_subtracted_on_final_interval']:
        with np.load(directory/'leading_tail.npz') as z:
            source=np.einsum('nij,nji->n',z['DF'],z['DF']);yy,_,labels=spherical_harmonics(z['directions'],p.lmax);coef=source@(yy.conj()*z['weights'][:,None])
        assert np.array_equal(labels,p.labels)
        p.tail={'alpha':(1-cfg['c_l'])/cfg['c_l'],'omega/c_l':cfg['omega']/cfg['c_l'],'coefficients':coef}
    return p
