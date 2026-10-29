# Lead check of the t1nk2 saved runs from their grid arrays and summaries (no referee code imported).
import json, sys, numpy as np
base='referee/R21/results/'
names=sys.argv[1:] or ['c074_level1']
out={}
for nm in names:
    g=dict(np.load(base+nm+'/grid.npz')); sm=json.load(open(base+nm+'/summary.json'))
    c=sm['c_l']; beta=1/c; K=sm['K']; r={}
    x=g['x']; mu=g['mu']; R=np.exp(x)
    # (a) E from saved shell arrays
    w=g['shell_weights']; d=g['shell_elliptic']-g['shell_eta']
    eps=np.sqrt((d**2)@w/((g['shell_eta']**2)@w)); r['E_recomputed']=float(np.sqrt(np.mean(eps**2))); r['E_summary']=sm['E']
    r['shell_eps_maxdiff']=float(np.max(abs(eps-g['shell_eps'])))
    sx=g['shell_x']; r['shell_R_range']=[float(np.exp(sx.min())),float(np.exp(sx.max()))]
    # (h) q = K h and eta = K^2 e on the grid
    r['q_vs_Kh']=float(np.max(abs(g['q']-K*g['h']))/np.max(abs(g['q'])))
    r['eta_vs_K2e']=float(np.max(abs(g['eta']-K**2*g['e']))/np.max(abs(g['eta'])))
    r['h_vs_exp_logh']=float(np.max(abs(g['h']-np.exp(g['logh']))))
    # (b) strain moment S = (3/4) int R dx int mu (1-mu^2) e dmu
    inner=np.trapezoid(mu*(1-mu**2)*g['e'],mu,axis=1)
    S=0.75*np.trapezoid(R*inner,x); r['S_grid_trapz']=float(S); r['S_summary']=sm['S']; r['twoK2S_minus1']=float(2*K**2*S-1)
    # (d) oddness of phi and of e in mu (grid symmetric?)
    sym=np.allclose(mu,-mu[::-1],atol=1e-14); r['mu_grid_symmetric']=bool(sym)
    if sym:
        r['phi_odd_defect']=float(np.max(abs(g['phi']+g['phi'][:,::-1]))/np.max(abs(g['phi'])))
        r['e_odd_defect']=float(np.max(abs(g['e']+g['e'][:,::-1]))/np.max(abs(g['e'])))
        r['h_even_defect']=float(np.max(abs(g['h']-g['h'][:,::-1])))
    # (c) finite-difference -Delta_5 phi in (x, mu): R^-2 [f_xx + 3 f_x + (1 - mu^2) f_mumu - 4 mu f_mu]
    # quintic interpolating spline of the saved phi grid (the mu nodes cluster at the poles, so plain differences are inaccurate)
    from scipy.interpolate import RectBivariateSpline
    f=g['phi']; sp=RectBivariateSpline(x,mu,f,kx=5,ky=5,s=0)
    fx=sp(x,mu,dx=1); fxx=sp(x,mu,dx=2); fm=sp(x,mu,dy=1); fmm=sp(x,mu,dy=2)
    lap=(fxx+3*fx+(1-mu**2)*fmm-4*mu*fm)/R[:,None]**2
    ell=g['elliptic_eta']; band=(R>0.02)&(R<50)
    rel=np.max(abs(-lap[band][:,5:-5]-ell[band][:,5:-5]),axis=1)/np.max(abs(ell[band]),axis=1)
    r['spline_lap_vs_elliptic_maxrel_0.02_50']=float(np.max(rel)); r['spline_lap_vs_elliptic_medianrel']=float(np.median(rel))
    # (e) axis identity w e = 2 h (h - 1) at mu = +1 (z = R)
    j=int(np.argmax(mu)); z=R; wz=c*z+2*f[:,j]; lhs=wz*g['e'][:,j]; rhs=2*g['h'][:,j]*(g['h'][:,j]-1)
    sel=(R>1e-2)&(R<1e3)
    r['axis_identity_maxrel']=float(np.max(abs(lhs[sel]-rhs[sel])/np.maximum(abs(rhs[sel]),1e-300)))
    r['axis_mu']=float(mu[j])
    # (g) far-axis amplitude H from h z^beta, and T1 = -2 K^2 H / c_l
    big=(R>1e3)
    Hs=g['h'][big,j]*z[big]**beta; r['H_from_grid_last']=float(Hs[-1]); r['H_summary']=sm['far_axis']['H']
    r['T1_from_H']=float(-2*K**2*Hs[-1]/c); r['T1_summary']=sm['far_axis']['transported']['T1']
    # (f) cubic source relation p_s = -(3 p_z/4)(1 + K^2/(1 + c_l)^2)
    ps=sm['p_s']; pz=sm['p_z']; r['cubic_rel_defect']=float((ps+0.75*pz*(1+K**2/(1+c)**2))/abs(ps))
    r['K']=K; r['p_s']=ps; r['p_z']=pz
    # source slope from grid phi near origin on the axis: phi(0,z)/z -> 1/2
    small=np.argsort(R)[:3]; r['phi_over_z_axis_small_R']=[float(f[i,j]/R[i]) for i in small]
    out[nm]=r
json.dump(out,open('author_checks/t1nk2_check_output.json','w'),indent=1)
print(json.dumps(out,indent=1))
