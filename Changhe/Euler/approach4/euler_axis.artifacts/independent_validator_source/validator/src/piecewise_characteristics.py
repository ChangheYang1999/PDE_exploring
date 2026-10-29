"""Segmented meridional characteristics with explicit circulation jumps."""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp


def trace(field,r,z,element):
    jets=field.jets(np.asarray(r*r),np.asarray(z),1,element=element)
    p=jets['phi'];q=jets['q'];s=r*r
    W=np.array([field.c_l*r-r*p[0,1],field.c_l*z+2*p[0,0]+2*s*p[1,0]],dtype=float)
    Rq=(1-2*p[0,1])*q[0,0]+2*r*W[0]*q[1,0]+W[1]*q[0,1]
    return W,float(s*q[0,0]),float(s*Rq)


def characteristic(field,start,endpoint,*,rtol=1e-10,atol=1e-12,max_step=.15,max_crossings=32,samples=81):
    start=np.asarray(start,dtype=float);T=float(endpoint)
    if start.shape!=(2,) or start[0]<=0 or not np.all(np.isfinite(start)) or T==0:
        raise ValueError('finite positive-radius start and nonzero endpoint required')
    boundaries=np.asarray(field.interfaces,dtype=float)
    R0=float(np.linalg.norm(start))
    if np.min(np.abs(boundaries-R0),initial=np.inf)<1e-10:
        raise ValueError('start must be away from an interface')
    element=int(np.searchsorted(boundaries,R0));k=1-2*field.c_l;orientation=np.sign(T)
    _,gamma0,_=trace(field,*start,element)
    segments=[];crossings=[];state=np.r_[start,0.];time=0.;status='complete';nfev=0
    while orientation*(T-time)>1e-13:
        current=element
        def rhs(t,y):
            W,_,residual=trace(field,y[0],y[1],current)
            return np.r_[W,np.exp(k*t)*residual]
        events=[];event_labels=[]
        for boundary_index,direction in [(current-1,-1),(current,+1)]:
            if not 0<=boundary_index<len(boundaries):continue
            a=boundaries[boundary_index]
            def event(t,y,a=a):return np.hypot(y[0],y[1])-a
            event.terminal=True;event.direction=direction
            events.append(event);event_labels.append((boundary_index,direction))
        sol=solve_ivp(rhs,(time,T),state,method='DOP853',rtol=rtol,atol=atol,
                      max_step=max_step,dense_output=True,events=events)
        nfev+=sol.nfev
        segments.append((time,float(sol.t[-1]),current,sol.sol))
        if not sol.success:
            status='integrator_failed: '+sol.message;break
        time=float(sol.t[-1]);state=sol.y[:,-1]
        if orientation*(T-time)<=1e-13:break
        hits=[j for j,ts in enumerate(sol.t_events) if len(ts)]
        if len(hits)!=1:
            status='unresolved_event_count';break
        boundary_index,direction=event_labels[hits[0]];new=current+direction
        oldW,oldGamma,_=trace(field,state[0],state[1],current)
        newW,newGamma,_=trace(field,state[0],state[1],new)
        radius=float(np.hypot(*state[:2]));normal=state[:2]/radius
        before_normal=float(orientation*np.dot(oldW,normal));after_normal=float(orientation*np.dot(newW,normal))
        jump=newGamma-oldGamma
        crossings.append(dict(time=time,r=float(state[0]),z=float(state[1]),radius=radius,
                              element_before=current,element_after=new,direction=int(direction),
                              traversal_normal_before=before_normal,traversal_normal_after=after_normal,
                              gamma_jump=jump,weighted_gamma_jump=float(np.exp(k*time)*jump)))
        if direction*before_normal<=1e-12 or direction*after_normal<=1e-12:
            status='unresolved_transverse_continuation';break
        if len(crossings)>=max_crossings:
            status='unresolved_crossing_limit';break
        if len(segments)>1 and abs(segments[-1][1]-segments[-1][0])<1e-12:
            status='unresolved_repeated_zero_event';break
        element=new
    end=float(segments[-1][1]);times=np.linspace(0,end,samples);rows=[]
    for t in times:
        # At an exact crossing select the later segment in traversal order.
        eligible=[seg for seg in segments if orientation*(t-seg[0])>=-1e-13 and orientation*(seg[1]-t)>=-1e-13]
        seg=eligible[-1];y=seg[3](t);_,gamma,_=trace(field,y[0],y[1],seg[2])
        weighted=float(np.exp(k*t)*gamma)
        jsum=sum(x['weighted_gamma_jump'] for x in crossings
                 if orientation*(t-x['time'])>1e-12
                 or (abs(t-x['time'])<=1e-12 and seg[2]==x['element_after']))
        # Endpoint at a crossing remains on the last successfully integrated side.
        rows.append(dict(t=float(t),r=float(y[0]),z=float(y[1]),element=int(seg[2]),weighted_gamma=weighted,
                         integrated_residual=float(y[2]),jump_sum=float(jsum),
                         corrected_error=weighted-gamma0-float(y[2])-jsum,
                         uncorrected_change=weighted-gamma0))
    scale=max(abs(gamma0),max(abs(row['weighted_gamma']) for row in rows),1e-300)
    return dict(start=start.tolist(),requested_endpoint=T,reached_endpoint=end,status=status,
                success=status=='complete' and abs(end-T)<1e-12,nfev=nfev,rtol=rtol,atol=atol,max_step=max_step,
                initial_gamma=gamma0,crossings=crossings,path=rows,
                max_corrected_error=max(abs(row['corrected_error']) for row in rows),
                max_relative_corrected_error=max(abs(row['corrected_error']) for row in rows)/scale,
                max_uncorrected_change=max(abs(row['uncorrected_change']) for row in rows),
                max_relative_uncorrected_change=max(abs(row['uncorrected_change']) for row in rows)/scale,
                scope='Finite segmented path with explicit residual and jump corrections; no global-basin claim.')
