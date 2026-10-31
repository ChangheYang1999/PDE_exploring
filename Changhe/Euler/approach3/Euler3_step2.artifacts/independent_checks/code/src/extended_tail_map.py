"""Independent explicit 2x2 tail solve at fixed parameters in extended arithmetic."""
import numpy as np

def expand(z,metadata,arrays):
    D=np.longdouble;C=np.clongdouble;z=np.asarray(z,dtype=D);modes=arrays['field_modes'];nq=len(modes);off=0;out={}
    c,w=z[-2:];alpha=(1-c)/c;kappa=w/c
    for name in ['A','C','B','D','E']:
        nr=metadata['red_sizes'][name];nc=metadata['ncols'][name];cols=arrays['cols_'+name];full_n=arrays['base_'+name].shape[0]
        out[name]=np.zeros((full_n,nq),dtype=D);out[name][:nr,cols]=z[off:off+nr*nc].reshape(nr,nc);off+=nr*nc
    assert off==len(z)-2
    lookup={tuple(mode):j for j,mode in enumerate(modes)}
    for name,shift in [('A',0),('C',1)]:
        n=len(out[name]);k=np.arange(n,dtype=D);k2=k*k;K=(D(8)/3)*k2*(k2-1)
        for q,(ell,m,kind) in enumerate(modes):
            if kind:continue
            qs=lookup[(ell,m,1)] if m else q
            free=np.asarray(out[name][:-2,q],dtype=C)+(C(1j)*out[name][:-2,qs] if m else 0)
            P=(alpha+ell-shift)/2+C(1j)*m*kappa/2
            a,b=k2[-2:];d=K[-2]-P;e=K[-1]-P;det=a*e-b*d
            r1=-np.sum(k2[:-2]*free);r2=-np.sum(K[:-2]*free)+P*np.sum(free)
            tail=np.array([(r1*e-b*r2)/det,(a*r2-d*r1)/det],dtype=C)
            out[name][-2:,q]=tail.real
            if m:out[name][-2:,qs]=tail.imag
    for name in ['B','D']:
        n=len(out[name])
        if n>=2:out[name][-1]=-np.sum((np.arange(n-1,dtype=D)**2)[:,None]*out[name][:-1],axis=0)/D((n-1)**2)
    return out
