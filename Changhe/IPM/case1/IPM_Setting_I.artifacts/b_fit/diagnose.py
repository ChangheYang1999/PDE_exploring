"""Independent diagnostic tables for a saved stationary shape."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ[key]="1"
import argparse
import csv
import json
import numpy as np
from scipy.integrate import simpson
from scipy.interpolate import CubicSpline,RectBivariateSpline
from scipy.optimize import brentq,root
from stationary import Shape
from solver import derivative


def angular_derivative(a,h,left,right):
    e=np.concatenate((left*a[:,2:0:-1],a,right*a[:,-2:-4:-1]),axis=1)
    return (e[:,:-4]-8*e[:,1:-3]+8*e[:,3:-1]-e[:,4:])/(12*h)


def region_stats(R,den,mask,logres):
    if not np.any(mask):return {}
    return dict(absolute=float(np.max(np.abs(R[mask]))),
                regional=float(np.max(np.abs(R[mask]))/max(float(np.max(den[mask])),1e-300)),
                pointwise=float(np.max(np.abs(logres[mask]))))


def diagnostic(path,nr=512,nt=96,R=1000.,export=None,tail="homogeneous",rmin=1e-4):
    z=np.load(path)
    compact=str(z["compact"]) if "compact" in z else "quadratic"
    sh=Shape(nr,nt,R,int(z["degree"]),int(z["angular"]),compact,
             int(z["singular"]) if "singular" in z else 0,
             int(z["angular_cap"]) if "angular_cap" in z else 0,rmin=rmin)
    sh.p.tail_terms=2 if tail=="two-term" else 1
    sh.radial_basis=str(z["radial_basis"]) if "radial_basis" in z else "chebyshev"
    sh.spline_order=int(z["spline_order"]) if "spline_order" in z else 3
    sh.origin_radius=float(z["origin_radius"]) if "origin_radius" in z else 0.
    if "spline_knots" in z:sh.spline_knots=z["spline_knots"]
    sh.build_basis(float(z["k"]))
    # Diagnostics need the sampled fields, not parameter derivatives.
    H,f,L2,elog,dlog=sh.evaluate(z["z"],release_basis=True)
    L=float(z["L"])
    # Preserve the candidate's physical scale when changing quadrature/domain.
    # Recomputing L at every resolution would hide strain discretization errors.
    L2=L*L;p=sh.p;k=float(z["k"])
    c=L2*f["c"];cl=(1+c)/3
    ht,ha=f["ht"],f["ha"]
    uadv=L2*(2*f["ux"]+f["uy"]+f["ur"]*ht+f["ua"]*ha)
    elog=cl*(3+ht)+uadv-1
    dlog=1+np.abs(3+ht)+np.abs(uadv)
    r=L*p.r;rr=r[:,None];theta=p.theta
    rho=L**3*f["rho"]
    residual=rho*elog;den=np.abs(rho)*dlog
    xx=rr*p.ct;yy=rr*p.st
    full=np.ones_like(rho,dtype=bool)
    regions={
        "inner":np.broadcast_to(rr<=2,rho.shape),
        "annulus":np.broadcast_to((rr>=2)&(rr<=10),rho.shape),
        "x_strip":(yy<=.1)&(rr<=10),
        "y_strip":(xx<=.1)&(rr<=10),
        "whole":full}
    results={name:region_stats(residual,den,mask,elog/dlog) for name,mask in regions.items()}
    aaxis=cl+L2*f["ux"][:,0];baxis=cl+L2*f["uy"][:,0]
    aspline=CubicSpline(p.t,aaxis);bspline=CubicSpline(p.t,baxis)
    # q_t=v-2q follows directly from V1. At a root of W1/x this
    # gives d_x W1 without differentiating the interpolated quotient.
    aaxis_t=L2*np.sum(p.m*(2*f["q"]-f["v"]),axis=1)
    atspline=CubicSpline(p.t,aaxis_t)
    roots=[]
    for i in range(nr-1):
        if aaxis[i]*aaxis[i+1]<0:
            t0=brentq(aspline,p.t[i],p.t[i+1])
            roots.append(dict(x=float(L*np.exp(t0)),mu1=float(atspline(t0)),
                              mu1_finite_difference=float(aspline(t0,1)),
                              mu2=float(bspline(t0)),
                              mu1_error=float(abs(atspline(t0)-(2*cl-1))),
                              mu2_error=float(abs(bspline(t0)-1))))
    # Search cells in which both components might cross zero.
    wa=cl+L2*f["ux"];wb=cl+L2*f["uy"]
    possible=np.ones((nr-1,nt),bool)
    for ar in (wa,wb):
        corners=np.array([ar[:-1,:-1],ar[1:,:-1],ar[:-1,1:],ar[1:,1:]])
        possible &= (corners.min(0)<=0)&(corners.max(0)>=0)
    sa=RectBivariateSpline(p.t,p.theta,wa);sb=RectBivariateSpline(p.t,p.theta,wb)
    interior=[]
    for i,j in np.argwhere(possible):
        sol=root(lambda q:[sa.ev(*q),sb.ev(*q)],[p.t[i]+p.dt/2,p.theta[j]+p.dtheta/2])
        tt,th=sol.x
        if sol.success and p.t[0]<tt<p.t[-1] and 1e-5<th<np.pi/2-1e-5:
            point=[float(L*np.exp(tt)*np.cos(th)),float(L*np.exp(tt)*np.sin(th))]
            if all(np.linalg.norm(np.array(point)-v)>1e-3 for v in interior):interior.append(point)
    del sa,sb,corners,possible
    # Independent finite differences of streamfunction and Cartesian velocity.
    q=f["q"]
    qt=derivative(q,p.dt,0);qtt=derivative(qt,p.dt,0)
    emodes=(p.m**2-4)*q-4*qt-qtt-f["f"]
    E=L2*(emodes @ p.sin+f["f"]@p.sin-f["fx"])
    del qt,qtt,emodes
    ux=L**3*p.rr*p.ct*f["ux"];uy=L**3*p.rr*p.st*f["uy"]
    uxt=derivative(ux,p.dt,0);uyt=derivative(uy,p.dt,0)
    uxa=angular_derivative(ux,p.dtheta,1,-1)
    uya=angular_derivative(uy,p.dtheta,-1,1)
    div=(p.ct*uxt-p.st*uxa+p.st*uyt+p.ct*uya)/rr
    curl=(p.ct*uyt-p.st*uya-p.st*uxt-p.ct*uxa)/rr
    del uxt,uyt,uxa,uya
    fphysical=L2*f["fx"]
    elliptic={}
    for name,mask in regions.items():
        # Two applications of the centered first-derivative stencil reach
        # four rings. Exclude the rings influenced by endpoint formulas.
        safe=mask.copy();safe[:4]=False;safe[-4:]=False
        scale=max(np.max(np.abs(fphysical[safe])),1e-300)
        nonzero=safe&(abs(fphysical)>1e-8*scale)
        elliptic[name]=dict(E_abs=float(np.max(np.abs(E[safe]))),
                            E_rel=float(np.max(np.abs(E[safe]))/scale),
                            E_pointwise_nonzero=float(np.max(abs(E[nonzero]/fphysical[nonzero]))),
                            E_pointwise_cutoff_relative=1e-8,
                            div_abs=float(np.max(np.abs(div[safe]))),
                            div_rel=float(np.max(np.abs(div[safe]))/scale),
                            curl_rel=float(np.max(np.abs((curl+fphysical)[safe]))/scale))
    # The finite-difference and root-search work arrays are not needed by
    # the export. Release them before allocating the Cartesian field jets.
    del E,div,curl,fphysical
    # Weighted identity, with analytic exterior integral.
    angularweights=np.ones(nt+1)*p.dtheta
    angularweights[[0,-1]]*=.5
    def wint(ur,ua):
        return np.sum(4*rho/rr*L2*(-3*ur*np.sin(3*theta)+3*ua*np.cos(3*theta))
                      *angularweights,axis=1)
    integral=simpson(wint(f["ur"],f["ua"]),x=p.t)
    qR=q[-1]
    tailq=[]
    tailrho=[]
    for exponent,modes in zip(f["tail_powers"],f["tail_modes"]):
        fext=((exponent-p.m+1)*modes[:-1]+(exponent+p.m+1)*modes[1:])/(2*p.R)
        tailq.append(fext/(p.m**2-(exponent+1)**2))
        tailrho.append(L**3*(modes@p.sodd))
    qdec=qR-np.sum(tailq,axis=0)
    exterior_axis_ratio_bound=L2*np.sum(p.m*((1+p.m)*np.abs(qdec)+
        sum((1+abs(exponent+1))*np.abs(qpart)
            for exponent,qpart in zip(f["tail_powers"],tailq))))
    tailpart=0.
    for exponent_i,rho_i in zip(f["tail_powers"],tailrho):
        for exponent_j,qpart in zip(f["tail_powers"],tailq):
            urpart=-(qpart*p.m)@p.cos;uapart=((exponent_j+1)*qpart)@p.sin
            tailpart+=np.sum(4*rho_i/r[-1]*L2*(-3*urpart*np.sin(3*theta)+3*uapart*np.cos(3*theta))
                            *angularweights)/(2-exponent_i-exponent_j)
    taildec=0.
    for j,m in enumerate(p.m):
        urj=-m*qdec[j]*p.cos[j];uaj=-m*qdec[j]*p.sin[j]
        for exponent,rho_i in zip(f["tail_powers"],tailrho):
            taildec+=np.sum(4*rho_i/r[-1]*L2*(-3*urj*np.sin(3*theta)+3*uaj*np.cos(3*theta))
                            *angularweights)/(m+3-exponent)
    integral+=tailpart+taildec
    identity=np.pi*(1-cl)*c+integral
    # Exact angular density derivative of the trial formula.
    # The B3 fit is explicitly exploratory.
    axis_g=r**2*np.exp(H[:,0])
    # G3=(rho_{theta theta theta}/6r³)+(g'(r)/(2r²)-g(r)/(6r³)).
    # A simpler fixed-x identity for a=e^H:
    # G3=e^H*(H_t/2+H_{theta theta}/2), at theta=0.
    hess=f["haa_axis"]
    G3=np.exp(H[:,0])*(ht[:,0]+hess)/2
    p3=6+2/(2*cl-1)
    singular_coefficients=[value for name,value in zip(z["names"],z["z"][1:]) if name[0]==-1]
    B3_ansatz=sum(value*(-1)**j for j,value in enumerate(singular_coefficients))/L**float(6+2*k/(2-k))
    fits=[]
    for upper in (.15,.25,.4,.65,1.):
        mask=(r>=upper/5)&(r<=upper)
        if mask.sum()<8:continue
        x=r[mask]/upper
        design=np.array([x**2,x**4,x**6,x**p3,x**8]).T
        coef,_,_,_=np.linalg.lstsq(design,G3[mask],rcond=1e-12)
        fits.append(dict(upper=upper,B3=float(coef[3]/upper**p3),
                         relative_fit=float(np.linalg.norm(design@coef-G3[mask])/
                                            max(np.linalg.norm(G3[mask]),1e-300)),
                         condition=float(np.linalg.cond(design))))
    far=[]
    limiting_H=np.zeros_like(theta)
    exponent=6+2*k/(2-k)
    for name,value in zip(z["names"],z["z"][1:]):
        m,j=map(int,name)
        if m<0:
            limiting_H+=value*p.ct**(exponent-2)*p.st**2
        elif sh.radial_basis!="spline" or j==sh.degree-1:
            limiting_H+=value*np.cos(2*m*theta)
    Theta=L**(3-k)*p.ct**2*p.st*np.exp(limiting_H)
    for radius in (10,30,100,300,1000):
        i=int(np.argmin(abs(r-radius)))
        far.append(dict(r=float(r[i]),rho_over_rk=(rho[i]/r[i]**k).tolist(),
                        U_over_rk=(np.hypot(ux[i],uy[i])/r[i]**k).tolist(),
                        max_U_over_r=float(np.max(np.hypot(ux[i],uy[i])/r[i])),
                        Theta_relative_error=float(np.max(abs(rho[i]/r[i]**k-Theta))/
                                                   max(np.max(abs(Theta)),1e-300))))
    out=dict(nr=nr,nt=nt,R_shape=R,R_physical=float(r[-1]),tail=tail,
             rmin_shape=rmin,rmin_physical=float(r[0]),
             cl=cl,cl_stored=float(z["c_l"]),k_tail=k,k_from_cl=1/cl,
             c_V1=c,c_rho3=L2*f["c2"],center_relation=abs(3*cl-c-1),
             center_relation_stored=abs(3*float(z["c_l"])-c-1),
             origin_eigenvalues=[1-2*cl,4*cl-1],
             a0=1.,parity_error=0.,rho_axes_max=0.,U_origin=[0.,0.],
             roots_xaxis=roots,interior_roots_detected=interior,
             min_W2_yaxis_over_y=float(np.min(wb[:,-1])),
             min_W2_over_y_in_Q=float(np.min(wb)),
             exterior_axis_ratio_bound=float(exterior_axis_ratio_bound),
             exterior_bound_below_cl=bool(exterior_axis_ratio_bound<cl),
             rho_positive_in_open_Q=bool(np.all(rho[:,1:-1]>0)),
             rho_y_xaxis_positive=True,
             residuals=results,elliptic=elliptic,
             weighted_identity=dict(defect=float(identity),integral=float(integral),
                 target=float(np.pi*(cl-1)*c),
                 relative=float(abs(identity)/max(abs(integral),abs(np.pi*(cl-1)*c),1e-300))),
             p3=p3,B3_ansatz=float(B3_ansatz),B3_fits=fits,farfield=far,
             Theta_limit=Theta.tolist())
    reference_x=np.array([.15,.5,1.5,4.,8.])
    axis_interpolant=CubicSpline(r*r,aaxis)
    out["axis_velocity_samples"]=dict(
        x=reference_x.tolist(),
        w=(reference_x*axis_interpolant(reference_x**2)).tolist())
    if export:
        # Evaluate the actual trial's density jet analytically in small
        # batches.  Keeping this in the single export pass avoids a second
        # complete field archive on disk.
        from trial import Trial
        trial=Trial(path)
        G3_prime_fd=derivative(G3,p.dt,0)/r
        G3_exact=np.empty_like(r);G3_prime_exact=np.empty_like(r)
        for start in range(0,len(r),256):
            stop=min(start+256,len(r))
            axis=trial.axis(r[start:stop])
            G3_exact[start:stop]=axis["G3"]
            G3_prime_exact[start:stop]=axis["G3_prime"]
        out["axis_G3_direct_formula_max_difference"]=float(np.max(abs(G3-G3_exact)))
        # W1(x,y)=w+A2*y²+..., W2(x,y)=h*y+B3W*y³+...
        # u1=x*wa(r,theta); coefficient A2=(wa_t+wa_aa)/(2x).
        # u2=y*wb(r,theta); coefficient B3W=(wb_t+wb_aa)/(2x²).
        wat=derivative(wa,p.dt,0);wbt=derivative(wb,p.dt,0)
        waa=angular_derivative(angular_derivative(wa,p.dtheta,1,1),p.dtheta,-1,-1)
        wba=angular_derivative(angular_derivative(wb,p.dtheta,1,1),p.dtheta,-1,-1)
        # V1 gives q_t=v-2q and v_t=m²q-2v-f. Use those identities
        # and exact trigonometric derivatives for the primary velocity jets.
        baxis_t=L2*np.sum(p.m*((p.m**2+2)*q-3*f["v"]-f["f"]),axis=1)
        aaxis_aa=L2*np.sum(p.m**3*q-2*p.m*f["v"],axis=1)
        baxis_aa=L2*np.sum(p.m**3*q-(p.m**3+2*p.m)*f["v"]/3,axis=1)
        axis_denflux=np.stack([
            np.abs(wa[:,0]*(2+ht[:,0]))+np.abs(wb[:,0])+1,
            np.abs(2*wa[:,-1])+np.abs(wb[:,-1]*(1+ht[:,-1]))+1],axis=1)
        np.savez_compressed(export,r=r,theta=theta,x=xx,y=yy,rho=rho,c_l=cl,c=c,
             c_second=L2*f["c2"],c_l_stored=float(z["c_l"]),a0=1.,
             origin_rho=0.,origin_U=np.array([0.,0.]),
             rho_x=L2*f["fx"],rho_y=L2*(p.st*f["rt"]+p.ct*f["ra"])/p.rr,
             psi=L**4*p.rr**2*(q@p.sin),U1=ux,U2=uy,W1=cl*xx+ux,W2=cl*yy+uy,
             H=H,residual=residual,denominator=den,axis_x=r,axis_w=r*wa[:,0],
             axis_flux_residual_limits=elog[:,[0,-1]]/axis_denflux,
             axis_N4_residual_limits=(elog/dlog)[:,[0,-1]],
             axis_w_prime=aaxis+aaxis_t,axis_h=wb[:,0],
             axis_G1=axis_g,axis_G1_prime=r*np.exp(H[:,0])*(2+ht[:,0]),
             axis_G3=G3_exact,axis_G3_prime=G3_prime_exact,
             axis_G3_prime_finite_difference=G3_prime_fd,
             axis_A2=(aaxis_t+aaxis_aa)/(2*r),
             axis_B3W=(baxis_t+baxis_aa)/(2*r*r),
             axis_A2_finite_difference=(wat[:,0]+waa[:,0])/(2*r),
             axis_B3W_finite_difference=(wbt[:,0]+wba[:,0])/(2*r*r),
             Theta_limit=Theta,shape_z=z["z"],shape_names=z["names"],
             shape_L=L,shape_k=k,diagnostics=json.dumps(out))
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument("candidate")
    ap.add_argument("--resolutions",default="256:48,512:96,768:128")
    ap.add_argument("--domains",default="100,300,1000")
    ap.add_argument("--tails",default="homogeneous")
    ap.add_argument("--prefix",default="diagnostic")
    ap.add_argument("--inner-radius",type=float,default=1e-4)
    args=ap.parse_args()
    rows=[]
    for pair in args.resolutions.split(","):
        nr,nt=map(int,pair.split(":"))
        for R in map(float,args.domains.split(",")):
            for tail in args.tails.split(","):
                if tail not in ("homogeneous","two-term"):raise ValueError(tail)
                out=diagnostic(args.candidate,nr,nt,R,tail=tail,rmin=args.inner_radius)
                rows.append(out)
                q=out["roots_xaxis"][0] if out["roots_xaxis"] else {}
                print(json.dumps({key:out[key] for key in
                                  ("nr","nt","R_shape","tail","cl","c_V1","c_rho3")},
                                 separators=(",",":")),q,out["residuals"]["inner"],
                      out["residuals"]["annulus"],flush=True)
                with open(args.prefix+".json","w") as f:json.dump(rows,f,indent=2)
    with open(args.prefix+".csv","w") as f:
        fields=["nr","nt","R_shape","cl","c_V1","c_rho3","tail","xstar","mu1","mu2","res_inner","res_annulus"]
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for v in rows:
            q=v["roots_xaxis"][0] if v["roots_xaxis"] else {}
            w.writerow({**{key:v[key] for key in fields[:7]},
                        "xstar":q.get("x"),"mu1":q.get("mu1"),"mu2":q.get("mu2"),
                        "res_inner":v["residuals"]["inner"]["regional"],
                        "res_annulus":v["residuals"]["annulus"]["regional"]})
    nr,nt=map(int,args.resolutions.split(",")[-1].split(":"))
    diagnostic(args.candidate,nr,nt,max(map(float,args.domains.split(","))),
               args.prefix+"_fields.npz",tail=args.tails.split(",")[-1],
               rmin=args.inner_radius)

if __name__=="__main__":main()
