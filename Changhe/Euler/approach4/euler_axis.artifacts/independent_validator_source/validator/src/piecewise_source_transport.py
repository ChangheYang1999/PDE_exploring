"""Backward source transport, including derivatives across radial interfaces."""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp


def augmented_field(field,points,elements):
    points=np.asarray(points,dtype=float);elements=np.asarray(elements,dtype=int)
    F=np.empty((len(points),3));DF=np.zeros((len(points),3,3))
    for element in np.unique(elements):
        hit=elements==element;r=points[hit,0];z=points[hit,1];s=r*r
        p=field.jets(s,z,2,element=int(element))['phi'];c=field.c_l
        F[hit,0]=-c*r+r*p[0,1]
        F[hit,1]=-c*z-2*p[0,0]-2*s*p[1,0]
        F[hit,2]=1-2*p[0,1]
        DF[hit,0,0]=-c+p[0,1]+2*s*p[1,1];DF[hit,0,1]=r*p[0,2]
        DF[hit,1,0]=-8*r*p[1,0]-4*r*s*p[2,0];DF[hit,1,1]=-c-2*p[0,1]-2*s*p[1,1]
        DF[hit,2,0]=-4*r*p[1,1];DF[hit,2,1]=-2*p[0,2]
    return F,DF


def source_transport(field,points,K,*,cutoffs=(16.,32.,48.),rtol=2e-9,atol=2e-11,max_step=.2,max_crossings_per_path=16,callback=None):
    points=np.asarray(points,dtype=float);N=len(points);cutoffs=sorted(set(map(float,cutoffs)))
    if points.shape!=(N,2) or np.any(points[:,0]<0) or not np.all(np.isfinite(points)) or not cutoffs or cutoffs[0]<=0:
        raise ValueError('finite half-plane points and positive cutoffs required')
    boundaries=np.asarray(field.interfaces,dtype=float);R=np.linalg.norm(points,axis=1)
    if len(boundaries) and np.min(np.abs(R[:,None]-boundaries))<1e-10:raise ValueError('initial point on interface')
    elements=np.searchsorted(boundaries,R);state=np.zeros((N,9));state[:,:2]=points
    state[:,3:]=np.tile(np.array([[1.,0.],[0.,1.],[0.,0.]]).ravel(),(N,1))
    time=0.;crossings=[];rows=[];status='complete';nfev=0;counts=np.zeros(N,dtype=int)
    for target in cutoffs:
        while target-time>1e-12:
            def rhs(t,y):
                y=y.reshape(N,9);F,DF=augmented_field(field,y[:,:2],elements)
                return np.concatenate((F,np.einsum('nij,njk->nik',DF,y[:,3:].reshape(N,3,2)).reshape(N,6)),axis=1).ravel()
            events=[];labels=[]
            for i,current in enumerate(elements):
                for bi,direction in [(current-1,-1),(current,+1)]:
                    if not 0<=bi<len(boundaries):continue
                    radius=boundaries[bi]
                    def event(t,y,i=i,radius=radius):return np.hypot(y[9*i],y[9*i+1])-radius
                    event.terminal=True;event.direction=direction
                    events.append(event);labels.append((i,int(current),int(current+direction),direction))
            sol=solve_ivp(rhs,(time,target),state.ravel(),method='DOP853',rtol=rtol,atol=atol,
                          max_step=max_step,events=events)
            nfev+=sol.nfev;time=float(sol.t[-1]);state=sol.y[:,-1].reshape(N,9)
            if not sol.success:status='integrator_failed: '+sol.message;break
            if target-time<=1e-12:break
            hits=[i for i,values in enumerate(sol.t_events) if len(values)]
            if len(hits)!=1:status='unresolved_event_count';break
            crossings_now=[labels[hits[0]]]
            # Coincident crossings can otherwise be missed after the first
            # terminal event, because its peer is a few ulps inside the sphere.
            radii=np.linalg.norm(state[:,:2],axis=1)
            currentF,_=augmented_field(field,state[:,:2],elements)
            for j,current in enumerate(elements):
                if j==crossings_now[0][0]:continue
                for bi,direction in [(current-1,-1),(current,+1)]:
                    if not 0<=bi<len(boundaries):continue
                    tol=64*np.finfo(float).eps*max(1.,boundaries[bi])
                    if abs(radii[j]-boundaries[bi])>tol:continue
                    normal=state[j,:2]/radii[j]
                    if direction*float(normal@currentF[j,:2])>1e-12:
                        crossings_now.append((j,int(current),int(current+direction),direction))
                        break
            for i,old,new,direction in crossings_now:
                point=state[i,:2];normal=np.r_[point/np.linalg.norm(point),0.]
                Fminus,_=augmented_field(field,point[None,:],np.array([old]));Fplus,_=augmented_field(field,point[None,:],np.array([new]))
                Fminus=Fminus[0];Fplus=Fplus[0];vin=float(normal@Fminus);vout=float(normal@Fplus)
                crossings.append(dict(time=time,path_index=i,element_before=old,element_after=new,
                                      normal_velocity_before=vin,normal_velocity_after=vout,
                                      coincident_event_group=len(crossings_now)))
                if direction*vin<=1e-12 or direction*vout<=1e-12:
                    status='unresolved_transverse_continuation';break
                counts[i]+=1
                if counts[i]>max_crossings_per_path:status='unresolved_crossing_limit';break
                saltation=np.eye(3)+np.outer(Fplus-Fminus,normal)/vin
                state[i,3:]=(saltation@state[i,3:].reshape(3,2)).ravel();elements[i]=new
            if status!='complete':break
        if status!='complete':break
        F,_=augmented_field(field,state[:,:2],elements);I=state[:,2];q=K*np.exp(-I);gradI=state[:,3:].reshape(N,3,2)[:,2,:]
        rows.append(dict(cutoff=target,terminal_points=state[:,:2].tolist(),terminal_a=F[:,2].tolist(),
                         integral_a=I.tolist(),q=q.tolist(),gradient_q=(-q[:,None]*gradI).tolist(),
                         predicted_relative_q_residual=F[:,2].tolist()))
        if callback is not None:callback(rows[-1],dict(nfev=nfev,crossings=len(crossings)))
    return dict(status=status,success=status=='complete' and len(rows)==len(cutoffs),nfev=nfev,rtol=rtol,atol=atol,
                max_step=max_step,K=float(K),points=points.tolist(),rows=rows,crossings=crossings,
                reached_time=time,scope='Finite backward cutoff with exact one-sided derivative formulas and numerical transverse events; source compatibility and convergence remain separate tests.')
