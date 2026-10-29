# Lead check of the referee's t1nk fine fields (c_l = 0.68 and 0.74, 402 coefficients): independent finite-difference
# -Delta_5 phi against the module's elliptic eta; shell discrepancy of -Delta_5 phi against the saved transported K^2 e on a
# few shells; K^2 S = 1/2; source slope phi_z(0,0) = 1/2 and oddness; cubic relation defect D from a local fit; far-axis A, B.
import sys, json, time, importlib.util, numpy as np
t0=time.time()
base='referee/R19/results/'
out={}
def load(name):
    spec=importlib.util.spec_from_file_location('f_'+name, base+name+'/field.py')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def phi_rz(m,r,z):
    return m.phi(np.asarray(r)**2,np.asarray(z))
for name in ('gaussian_c068_n20','gaussian_c074_n20'):
    m=load(name); c=m.c_l; K=m.K; S=m.S
    res={'c_l':c,'K':K,'S':S,'K2S':K*K*S,'E_module':m.E}
    # 1. FD Laplacian vs module elliptic eta at points (R, mu)
    rng=np.random.default_rng(0)
    errs=[]
    for k in range(40):
        R=np.exp(rng.uniform(np.log(0.05),np.log(20))); mu=rng.uniform(-0.95,0.95)
        r=R*np.sqrt(1-mu*mu); z=R*mu; h=2e-3*R
        f0=phi_rz(m,r,z)
        fr=(phi_rz(m,r+h,z)-phi_rz(m,r-h,z))/(2*h)
        frr=(phi_rz(m,r+h,z)-2*f0+phi_rz(m,r-h,z))/h**2
        fzz=(phi_rz(m,r,z+h)-2*f0+phi_rz(m,r,z-h))/h**2
        lap=frr+3/r*fr+fzz
        ee=m.elliptic_eta(r*r,z)
        errs.append(abs(-lap-ee)/max(abs(ee),1e-3*np.max(abs(ee))+1e-12))
    res['fd_vs_elliptic_eta_median_rel']=float(np.median(errs)); res['fd_vs_elliptic_eta_max_rel']=float(np.max(errs))
    # 2. source slope and oddness
    hz=1e-4
    res['phi_z_origin_fd']=float((phi_rz(m,0.0,hz)-phi_rz(m,0.0,-hz))/(2*hz))
    res['oddness_max']=float(max(abs(phi_rz(m,0.3,0.4)+phi_rz(m,0.3,-0.4)),abs(phi_rz(m,1.0,2.0)+phi_rz(m,1.0,-2.0))))
    # 3. local cubic fit near the origin: phi = z/2 + p_s s z + p_z z^3 + O(R^5)
    pts=[]
    for R in (0.01,0.015,0.02):
        for mu in (0.2,0.5,0.8):
            r=R*np.sqrt(1-mu*mu); z=R*mu
            pts.append((r*r*z, z**3, phi_rz(m,r,z)-z/2))
    A=np.array([[p[0],p[1]] for p in pts]); b=np.array([p[2] for p in pts])
    ps,pz=np.linalg.lstsq(A,b,rcond=None)[0]
    D=ps+0.75*pz*(1+K*K/(1+c)**2)
    res.update({'p_s_fit':float(ps),'p_z_fit':float(pz),'D_over_abs_ps':float(D/abs(ps))})
    # 4. far axis: phi(0, z) = A z^(1-2p) + B z^(1-4p) + ...; fit at large z
    p=1/(2*c)
    zs=np.array([200.,400.,800.,1600.])
    vals=np.array([float(phi_rz(m,0.0,zz)) for zz in zs])
    M=np.vstack([zs**(1-2*p),zs**(1-4*p),zs**(1-6*p)]).T
    coef=np.linalg.lstsq(M,vals,rcond=None)[0]
    res.update({'far_axis_A_fit':float(coef[0]),'far_axis_B_fit':float(coef[1])})
    # 5. shell discrepancy on three shells: FD -Delta_5 phi vs transported eta (module interpolant)
    shells={}
    for R in (0.05,0.5,1.5,2.65,10.0):
        mus=np.linspace(-0.98,0.98,41); d=[];t=[]
        for mu in mus:
            r=R*np.sqrt(1-mu*mu); z=R*mu; h=2e-3*R
            f0=phi_rz(m,r,z)
            fr=(phi_rz(m,r+h,z)-phi_rz(m,r-h,z))/(2*h)
            frr=(phi_rz(m,r+h,z)-2*f0+phi_rz(m,r-h,z))/h**2
            fzz=(phi_rz(m,r,z+h)-2*f0+phi_rz(m,r,z-h))/h**2
            d.append(-(frr+3/r*fr+fzz)); t.append(float(m.eta(r,z)))
        d=np.array(d).ravel(); t=np.array(t).ravel()
        shells[str(R)]=float(np.sqrt(np.mean((d-t)**2)/np.mean(t**2)))
    res['shell_rel_discrepancy_fd_vs_transported']=shells
    out[name]=res
out['seconds']=time.time()-t0
json.dump(out,open('author_checks/t1nk_check_output.json','w'),indent=1)
print(json.dumps(out,indent=1))
