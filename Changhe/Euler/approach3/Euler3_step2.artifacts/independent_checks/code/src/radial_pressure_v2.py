"""Version 2: tensor-grid sources and exact power/log leading-tail integration.

Origin-centered full-space radial Green pressure, independent of ray tensors.

Each requested radius is a quadrature breakpoint. Additional dyadic shells
resolve the core even when the target is far away. The final interval extends
to infinity. The source may be any supplied scalar callable.
"""
import math,time
import numpy as np
from quadrature import sphere_grid
from solid_harmonics import spherical_harmonics,solid_harmonics

def radius_groups(radii):
    """Coalesce only roundoff variants, with relative separation at most32eps."""
    radii=np.asarray(radii,dtype=float)
    order=np.argsort(radii,kind='stable');groups=[];centers=[]
    for index in order:
        r=radii[index]
        if not centers or r-centers[-1]>32*np.finfo(float).eps*max(r,centers[-1]):
            centers.append(float(r));groups.append([])
        groups[-1].append(int(index))
    return np.asarray(centers),[np.asarray(g,dtype=int) for g in groups]

def radial_nodes(radii,n_r=16,scale=1.):
    if scale<=0:raise ValueError('positive scale required')
    radii=np.asarray(radii);positive=radii[radii>0]
    low=min(float(positive.min()),scale) if len(positive) else scale
    high=max(float(positive.max()),scale) if len(positive) else scale
    first=math.floor(math.log2(low/scale));last=math.ceil(math.log2(high/scale))+2
    raw_edges=np.unique(np.r_[0.,positive,scale*2.**np.arange(first,last+1)])
    edges=[raw_edges[0]]
    for value in raw_edges[1:]:
        if value-edges[-1]>32*np.finfo(float).eps*max(value,edges[-1]):edges.append(value)
    edges=np.asarray(edges)
    t,w=np.polynomial.legendre.leggauss(n_r);t=(t+1)/2;w=w/2
    nodes=[];weights=[];intervals=[]
    for a,b in zip(edges[:-1],edges[1:]):
        nodes.extend(a+(b-a)*t);weights.extend((b-a)*w);intervals.extend([(float(a),float(b))]*len(t))
    a=edges[-1];nodes.extend(a/t);weights.extend(a*w/t**2);intervals.extend([(float(a),None)]*len(t))
    return np.asarray(nodes),np.asarray(weights),edges,intervals

class RadialGreenPressure:
    def __init__(self,source,radii,lmax,n_r=16,n_mu=None,n_phi=None,scale=1.,angular_phase=.219,radial_batch=8,progress=None,zero_moments=(),leading_tail=None):
        start=time.time();self.lmax=lmax;self.zero_moments=tuple(zero_moments)
        if any(ell not in (0,1) for ell in self.zero_moments):raise ValueError('Only proved monopole/dipole constraints are supported')
        n_mu=n_mu or lmax+2;n_phi=n_phi or 2*lmax+4
        self.directions,self.angular_weights=sphere_grid(n_mu,n_phi,phase=angular_phase)
        yy,_,self.labels=spherical_harmonics(self.directions,lmax)
        projection=yy.conj()*self.angular_weights[:,None]
        self.nodes,self.weights,edges,intervals=radial_nodes(radii,n_r,scale)
        parts=[]
        for start_index in range(0,len(self.nodes),radial_batch):
            rr=self.nodes[start_index:start_index+radial_batch]
            xx=(rr[:,None,None]*self.directions[None,:,:]).reshape(-1,3)
            if hasattr(source,'projected_values'):
                coefficients=source.projected_values(rr,self.directions,projection)
                if not np.all(np.isfinite(coefficients)):raise FloatingPointError('Nonfinite projected source')
                parts.append(coefficients)
            else:
                ff=np.asarray(source.grid_values(rr,self.directions) if hasattr(source,'grid_values') else source(xx)).reshape(len(rr),len(self.directions))
                if not np.all(np.isfinite(ff)):raise FloatingPointError('Nonfinite pressure source')
                parts.append(ff@projection)
            if progress:progress(min(start_index+radial_batch,len(self.nodes)),len(self.nodes))
        self.source_coefficients=np.concatenate(parts)
        self.tail=None;self.tail_start=float(edges[-1])
        if leading_tail is not None:
            if leading_tail is True:
                alpha=float(source.field.alpha);kappa=float(source.field.omega/source.field.c_l)
                a,b=source.leading_coefficients(self.directions,self.labels,projection)
            else:
                alpha=float(leading_tail['alpha']);kappa=float(leading_tail['omega/c_l'])
                a=np.asarray(leading_tail['source_on_unit_sphere'](self.directions))@projection
                b=np.zeros_like(a)
            self.tail={'alpha':alpha,'omega/c_l':kappa,'coefficients':a,'log_coefficients':b}
            tail_nodes=self.nodes>self.tail_start
            exponent=-2*alpha-2+1j*self.labels[:,1]*kappa
            rr=self.nodes[tail_nodes,None]
            self.source_coefficients[tail_nodes]-=(a[None,:]+b[None,:]*np.log(rr))*rr**exponent[None,:]
        self.metadata={'method':'full-space radial Green integral','lmax':lmax,'n_r_per_interval':n_r,'n_mu':n_mu,'n_phi':n_phi,'scale':scale,'radial_nodes':len(self.nodes),'radial_edges':edges.tolist(),'last_interval':'[last edge,infinity), s=a/t','seconds':time.time()-start,'requested_radius_count':len(np.asarray(radii)),'requested_radii':radius_groups(radii)[0].tolist(),'gradient':'Cartesian solid-harmonic recurrence, no polar-axis quotient','imposed_zero_source_moments':list(self.zero_moments),'leading_tail_subtracted_on_final_interval':self.tail is not None}
        self.metadata['unconstrained_source_moment_diagnostics']=[]
        for k,(ell,m) in enumerate(self.labels):
            if ell>1:continue
            terms=self.weights*self.nodes**(ell+2)*self.source_coefficients[:,k]
            moment=terms.sum()+self.tail_integral(ell+2)[k]
            self.metadata['unconstrained_source_moment_diagnostics'].append({'ell':int(ell),'m':int(m),'real':float(moment.real),'imag':float(moment.imag),'absolute_sum_including_tail':float(np.sum(abs(terms))+abs(self.tail_integral(ell+2)[k])),'relative_absolute_sum':float(abs(moment)/max(np.sum(abs(terms))+abs(self.tail_integral(ell+2)[k]),1e-300))})
    def tail_integral(self,power):
        if self.tail is None:return np.zeros(len(self.labels),complex)
        alpha=self.tail['alpha'];kappa=self.tail['omega/c_l'];exponent=power-2*alpha-1+1j*self.labels[:,1]*kappa
        if np.any(np.real(exponent)>=0):raise ValueError('Divergent leading-tail moment')
        return self.tail_start**exponent/(-exponent)*(self.tail['coefficients']+self.tail['log_coefficients']*(np.log(self.tail_start)-1/exponent))
    def values(self,points):
        points=np.asarray(points,dtype=float);radii=np.linalg.norm(points,axis=1)
        if np.any(radii>=self.tail_start):raise ValueError('Evaluation radius beyond prepared radial grid')
        p=np.zeros(len(points),complex);g=np.zeros((len(points),3),complex)
        ell=self.labels[:,0];denom=2*ell+1
        weighted=self.weights[:,None]*self.source_coefficients
        centers,groups=radius_groups(radii)
        self.metadata['evaluation_radius_groups']=len(centers)
        self.metadata['low_moment_evaluation']='choose lower absolute quadrature sum, inside or proved zero-moment outside'
        for radius,select in zip(centers,groups):
            if radius==0:
                h,dh,labels=solid_harmonics(points[select],self.lmax)
                moments=np.sum(weighted*self.nodes[:,None],axis=0)+self.tail_integral(1)
                p[select]=h[:,0]*moments[0]
                l1=ell==1
                if np.any(l1):g[select]=np.einsum('nki,k->ni',dh[:,l1],(np.sum(weighted[:,l1],axis=0)+self.tail_integral(0)[l1])/3)
                continue
            directions=points[select]/radii[select,None]
            y,gs,labels=spherical_harmonics(directions,self.lmax)
            inside=self.nodes<radius;outside=~inside
            inner=np.sum(weighted[inside]*radius*(self.nodes[inside,None]/radius)**(ell[None,:]+2),axis=0)
            outer=np.sum(weighted[outside]*self.nodes[outside,None]*(radius/self.nodes[outside,None])**ell[None,:],axis=0)
            outer+=radius**ell*self.tail_integral(1-ell)
            for degree in self.zero_moments:
                mask=ell==degree
                inside_terms=weighted[inside][:,mask]*radius*(self.nodes[inside,None]/radius)**(degree+2)
                outside_terms=weighted[outside][:,mask]*radius*(self.nodes[outside,None]/radius)**(degree+2)
                analytic_tail=radius**(-degree-1)*self.tail_integral(degree+2)[mask]
                exterior=-np.sum(outside_terms,axis=0)-analytic_tail
                # A zero total moment is vital in the far field, but its
                # exterior evaluation cancels large terms near the origin.
                # Both expressions have the same exact value. Choose using
                # absolute quadrature sums before cancellation, per mode.
                prefer_exterior=(np.sum(abs(outside_terms),axis=0)+abs(analytic_tail)<np.sum(abs(inside_terms),axis=0))
                inner[mask]=np.where(prefer_exterior,exterior,inner[mask])
            pc=(inner+outer)/denom;dp=(-(ell+1)*inner+ell*outer)/(radius*denom)
            p[select]=y@pc
            g[select]=directions*(y@dp)[:,None]+np.einsum('nki,k->ni',gs,pc/radius)
        self.metadata['max_imaginary_pressure']=float(np.max(np.abs(p.imag),initial=0))
        self.metadata['max_imaginary_gradient']=float(np.max(np.abs(g.imag),initial=0))
        return p.real,g.real
