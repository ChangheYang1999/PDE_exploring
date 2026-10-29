# Second lead check: compare the saved shell eps(R) with my FD -Delta_5 phi minus the module's transported eta at the same
# shell nodes, and refit the far-axis A, B with the (1 + R^2)^(-p) correction terms included.
import json, importlib.util, numpy as np
base='referee/R19/results/'
out={}
for name in ('gaussian_c068_n20','gaussian_c074_n20'):
    spec=importlib.util.spec_from_file_location('f_'+name, base+name+'/field.py')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    g=dict(np.load(base+name+'/grid.npz'))
    from scipy.interpolate import RectBivariateSpline
    spl=RectBivariateSpline(g['x'],g['mu'],g['eta'])
    def eta_tr(r,z):
        R=np.hypot(r,z); return float(spl.ev(np.log(R),z/R))
    xx=g['shell_x']; mm=g['shell_mu']; ww=g['shell_weights']
    res={'shell_x_shape':list(np.shape(xx)),'shell_mu_shape':list(np.shape(mm)),'weights_shape':list(np.shape(ww))}
    eps_saved=np.sqrt(((g['shell_elliptic']-g['shell_eta'])**2)@ww)/np.sqrt((g['shell_eta']**2)@ww)
    R=np.exp(np.ravel(xx)) if np.ndim(xx)==1 else np.exp(xx[:,0])
    mu=np.ravel(mm) if np.ndim(mm)==1 else mm[0]
    picks=[int(np.argmax(eps_saved))]+[int(np.argmin(abs(R-v))) for v in (0.5,1.5,2.65,10.0)]
    rows=[]
    for i in picks:
        Ri=R[i]; d=[]; t=[]
        for muj in mu:
            r=Ri*np.sqrt(max(1-muj*muj,0)); z=Ri*muj; h=2e-3*Ri
            f=lambda a,b: float(m.phi(np.array(a*a),np.array(b)))
            f0=f(r,z); fr=(f(r+h,z)-f(r-h,z))/(2*h); frr=(f(r+h,z)-2*f0+f(r-h,z))/h**2; fzz=(f(r,z+h)-2*f0+f(r,z-h))/h**2
            d.append(-(frr+3/r*fr+fzz) if r>1e-8 else np.nan); t.append(eta_tr(r,z))
        d=np.array(d); t=np.array(t); ok=np.isfinite(d)
        w=ww[ok]
        mine=float(np.sqrt(((d[ok]-t[ok])**2)@w)/np.sqrt((t[ok]**2)@w))
        mine_vs_saved_eta=float(np.max(abs(t[ok]-g['shell_eta'][i][ok]))/np.max(abs(g['shell_eta'][i])))
        mine_vs_saved_ell=float(np.max(abs(d[ok]-g['shell_elliptic'][i][ok]))/np.max(abs(g['shell_elliptic'][i])))
        rows.append(dict(R=float(Ri),eps_saved=float(eps_saved[i]),eps_mine=mine,eta_interp_vs_saved=mine_vs_saved_eta,fd_vs_saved_elliptic=mine_vs_saved_ell))
    res['shells']=rows; res['mu_range']=[float(mu.min()),float(mu.max())]
    c=m.c_l; p=1/(2*c)
    zs=np.geomspace(1e3,1e6,25)
    vals=np.array([float(m.phi(np.array(0.0),np.array(zz))) for zz in zs])
    ex=[1-2*p,1-4*p,-1-2*p,1-6*p,-1-4*p,-3-2*p]
    M=np.vstack([zs**e for e in ex]).T
    coef=np.linalg.lstsq(M/np.abs(vals)[:,None],vals/np.abs(vals),rcond=None)[0]
    res['far_axis_fit']=dict(exponents=ex,A=float(coef[0]),B=float(coef[1]))
    out[name]=res
json.dump(out,open('author_checks/t1nk_check2_output.json','w'),indent=1)
print(json.dumps(out,indent=1))
