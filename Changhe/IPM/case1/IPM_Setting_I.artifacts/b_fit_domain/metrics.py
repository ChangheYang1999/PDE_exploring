"""Field diagnostics in physical units; JSON is the numerical record."""
import json
import sys
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from trial import Trial


def residual_table(r,theta,rho,residual,den,n4,axis_flux=None,axis_n4=None):
    """Use the analytic transverse limits when supplied."""
    bands=[("r<=0.1",0,.1),("0.1<=r<=2",.1,2),("2<=r<=10",2,10),
           ("10<=r<=100",10,100),("100<=r<=1000",100,1000),
           ("1000<=r<=R",1000,float(r[-1])),("all",0,float(r[-1]))]
    strips=[("all",0,np.pi/2),("x_strip",0,.05),
            ("middle",.05,np.pi/2-.05),("y_strip",np.pi/2-.05,np.pi/2)]
    nonzero=np.abs(rho)>0
    nonzero[:,[0,-1]]=False
    ratios=np.divide(np.abs(residual),den,out=np.zeros_like(residual),where=den>0)
    oldratios=np.divide(np.abs(residual),n4,out=np.zeros_like(residual),where=n4>0)
    signs=np.sign(residual)
    if axis_flux is not None:
        ratios[:,[0,-1]]=np.abs(axis_flux)
        oldratios[:,[0,-1]]=np.abs(axis_n4)
        signs[:,[0,-1]]=np.sign(axis_flux)
        nonzero[:,[0,-1]]=True
    out={}
    for b,lo,hi in bands:
        for name,tl,th in strips:
            mask=((r[:,None]>=lo)&(r[:,None]<=hi)&
                  (theta[None,:]>=tl)&(theta[None,:]<=th)&nonzero)
            if not mask.any():continue
            index=np.argwhere(mask)
            ratio=ratios[mask]
            old=oldratios[mask]
            i,j=index[np.argmax(ratio)]
            out[b+"/"+name]=dict(max=float(ratio.max()),rms=float(np.sqrt(np.mean(ratio**2))),
                                N4_max=float(old.max()),N4_rms=float(np.sqrt(np.mean(old**2))),
                                r_max=float(r[i]),theta_max=float(theta[j]),samples=len(ratio),
                                residual_signed_at_max=float(signs[i,j]*ratios[i,j]))
    return out


def analyze(name,fields=None):
    z=np.load(fields if fields else name+"_fields.npz")
    trial=Trial(name+"_shape.npz")
    diag=json.loads(str(z["diagnostics"]))
    r=z["r"];theta=z["theta"]
    rh=z["rho"];res=z["residual"]
    fluxden=np.abs(z["W1"]*z["rho_x"])+np.abs(z["W2"]*z["rho_y"])+np.abs(rh)
    reconstructed=z["W1"]*z["rho_x"]+z["W2"]*z["rho_y"]-rh
    check=np.max(np.abs(reconstructed-res)/np.maximum(fluxden,1e-300))
    independent_n4=(np.abs(rh)+np.abs(z["x"]*z["rho_x"]+z["y"]*z["rho_y"])
                    +np.abs(z["U1"]*z["rho_x"]+z["U2"]*z["rho_y"]))
    n4_check=np.max(np.abs(independent_n4-z["denominator"])/
                    np.maximum(independent_n4,1e-300))
    table=residual_table(r,theta,rh,res,fluxden,z["denominator"],
                         z["axis_flux_residual_limits"] if "axis_flux_residual_limits" in z else None,
                         z["axis_N4_residual_limits"] if "axis_N4_residual_limits" in z else None)
    ax=z["axis_x"];sel=ax<40;x=ax[sel]
    ws=CubicSpline(x*x,z["axis_w"][sel]/x)
    w=lambda t:np.asarray(t)*ws(np.asarray(t)**2)
    xp=brentq(w,1.,30.)
    spl={n:CubicSpline(x,z[n][sel]) for n in ("axis_h","axis_w_prime","axis_A2","axis_B3W",
                                             "axis_G1_prime")}
    def axis(t):
        jets=trial.axis(np.asarray(t))
        gg,gp,G,Gp=[jets[n] for n in ("G1","G1_prime","G3","G3_prime")]
        ww=w(t);hh=spl["axis_h"](t);a2=spl["axis_A2"](t);b3=spl["axis_B3W"](t)
        terms=np.stack([ww*Gp,(3*hh-1)*G,a2*gp,b3*gg])
        total=terms.sum(axis=0)
        norm=np.sum(np.abs(terms),axis=0)
        T1=ww*gp+(hh-1)*gg
        norm1=np.abs(ww*gp)+np.abs((hh-1)*gg)
        return dict(T3=total,T3_relative=total/np.maximum(norm,1e-300),
                    T1_relative=T1/np.maximum(norm1,1e-300),
                    T1=T1,T1_denominator=norm1,
                    G3=G,G3_prime=Gp,T3_denominator=norm)
    jets={}
    for lo,hi in ((.01,.5),(.08,xp)):
        xx=np.unique(np.r_[np.geomspace(lo,hi,1200),np.linspace(lo,hi,1200)])
        a=axis(xx)
        j=int(np.argmax(np.abs(a["T3_relative"])))
        jets[f"[{lo},{hi:.12g}]"]=dict(max_relative=float(np.max(np.abs(a["T3_relative"]))),
                    rms_relative=float(np.sqrt(np.mean(a["T3_relative"]**2))),
                    x_max=float(xx[j]),T3_at_max=float(a["T3"][j]),
                    max_absolute=float(np.max(np.abs(a["T3"]))),
                    max_T1_relative=float(np.max(np.abs(a["T1_relative"]))),
                    max_T1_absolute=float(np.max(np.abs(a["T1"]))),
                    max_T1_relative_away_from_source=float(
                        np.max(np.abs(a["T1_relative"][xx<=.99*xp]))))
    points=np.array([.01,.03,.08,.1,.15,.3,.5,1.,2.,4.,8.,.99*xp,xp])
    profile=axis(points)
    profile={n:v.tolist() for n,v in profile.items()};profile["x"]=points.tolist()
    D9={}
    xx=np.linspace(.08,xp,2000)
    gg=trial.axis(xx);hh=spl["axis_h"](xx)
    D9["divergence_max"]=float(np.max(np.abs(spl["axis_w_prime"](xx)+hh-2*float(z["c_l"]))))
    a2p=spl["axis_A2"](xx,1);b3=spl["axis_B3W"](xx)
    D9["a2prime_plus_3b3_max_relative"]=float(np.max(np.abs(a2p+3*b3)/(np.abs(a2p)+3*np.abs(b3)+1e-30)))
    D9["a2prime_plus_3b3_max_absolute"]=float(np.max(np.abs(a2p+3*b3)))
    hp=spl["axis_h"](xx,1);a2=spl["axis_A2"](xx);gp=gg["G1_prime"]
    D9["hprime_minus_2a2_plus_gprime_max_relative"]=float(np.max(np.abs(hp-2*a2+gp)/(np.abs(hp)+2*np.abs(a2)+np.abs(gp)+1e-30)))
    D9["hprime_minus_2a2_plus_gprime_max_absolute"]=float(np.max(np.abs(hp-2*a2+gp)))
    D9["integral"]=[trial.d9(xp,n) for n in (16,32,64)]
    # Nonlocal D9 ratio, using direct interval quadrature of g^-1.
    from scipy.integrate import quad
    integral_checks=[]
    A=2*float(z["c_l"])-1
    for xx in (.08,.15,.5,1.5,4.,8.,.99*xp):
        val,err=quad(lambda t:float(np.exp(-trial.fields(t,0.)[0])/t**2),xx,xp,
                     epsabs=1e-10,epsrel=1e-10,limit=300)
        lhs=abs(float(w(xx)))/float(trial.axis(np.array([xx]))["G1"][0])
        rhs=A*val
        integral_checks.append(dict(x=xx,lhs=lhs,rhs=rhs,relative=(lhs-rhs)/max(abs(lhs),abs(rhs)),quad_error=err))
    D9["nonlocal"]=integral_checks
    c=diag["c_V1"];q=diag["weighted_identity"]["integral"]/c**2
    target=np.pi/3*(1-2/c)
    bp=diag["B3_ansatz"];p3=diag["p3"]
    wpoints=np.array([.15,.5,1.5,4.,8.])
    ans=dict(name=name,cl=diag["cl"],cl_stored=diag["cl_stored"],xstar=xp,
             hP=float(spl["axis_h"](xp)),mu1=float(spl["axis_w_prime"](xp)),
             inverse_c=c,target_c=3*diag["cl_stored"]-1,
             c_discrepancy=c-(3*diag["cl_stored"]-1),L=trial.L,
             residual_reconstruction_max=check,denominator_reconstruction_max=n4_check,
             bands=table,T3=jets,T3_profile=profile,
             D9=D9,D10=dict(q=q,target=target,relative=q/target-1),
             w=dict(x=wpoints.tolist(),values=w(wpoints).tolist()),
             B3_ansatz=bp,B3_ansatz_natural=bp*xp**(p3-2),p3=p3,
             natural_unit=xp**(2-p3),degree=trial.degree,angular=trial.angular)
    Path(name+"_metrics.json").write_text(json.dumps(ans,indent=2))
    print(json.dumps({k:v for k,v in ans.items() if k not in ("bands","T3_profile","D9")},indent=2))
    return ans


if __name__=="__main__":
    analyze(sys.argv[1],sys.argv[2] if len(sys.argv)>2 else None)
