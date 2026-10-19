# V121: concentration of the x-odd Ritz vectors (fraction of the squared node norm in the top-k nodes, and
# the number of distinct radial / angular nodes needed for 50 / 90 %), u is the mode on the (r, th) grid
import numpy as np, sys
for S in sys.argv[1:]:
    d=np.load('runs/v108_mode_%s.npz'%S, allow_pickle=True)
    u=d['u']; r=d['r']; th=d['th']; lr=np.log(r)
    w=(u**2).ravel(); o=np.argsort(w)[::-1]; c=np.cumsum(w[o])/w.sum()
    top={k:round(float(c[k-1]),4) for k in (1,2,4,10,50,200)}
    n50=int(np.searchsorted(c,0.5))+1; n90=int(np.searchsorted(c,0.9))+1
    i,j=np.unravel_index(o[:n90],u.shape)
    # radial and angular profiles of |u|^2
    pr=(u**2).sum(1); pr/=pr.sum(); pa=(u**2).sum(0); pa/=pa.sum()
    ir=np.argsort(pr)[::-1]; ia=np.argsort(pa)[::-1]
    nr90=int(np.searchsorted(np.cumsum(pr[ir]),0.9))+1; na90=int(np.searchsorted(np.cumsum(pa[ia]),0.9))+1
    # sign changes along th at the radial maximum, and along r at the angular maximum
    i0,j0=np.unravel_index(o[0],u.shape)
    print(S,'lam',float(d['lam']),'top_k',top,'n50',n50,'n90',n90,
          'peak (log r, deg)',(round(float(lr[i0]),3),round(float(np.degrees(th[j0])),2)),
          'radial nodes for 90%',nr90,'angular nodes for 90%',na90,
          'dlogr at peak',round(float(lr[min(i0+1,len(r)-1)]-lr[i0]),4),'dth deg',round(float(np.degrees(th[1]-th[0])),3),
          'top radial', [round(float(lr[k]),2) for k in ir[:5]], 'top ang', [round(float(np.degrees(th[k])),1) for k in ia[:6]])
