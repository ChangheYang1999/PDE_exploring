"""Lead (2026-10-18T14:20Z): angular spectrum of the signed flux-normalized residual R/dd (quick_scan's N_f) in the band
r_lo <= r <= r_hi next to P, per radius row; reports the frequency (cycles per 2 pi) of the largest amplitude and the
amplitude at 2 m_max. Look-ahead diagnostic only. Usage: python3 ang_spec.py SHAPE NR NT [r_lo r_hi]"""
import sys, json
import numpy as np
from centre_fit import load_shape
path=sys.argv[1]; nr=int(sys.argv[2]); nt=int(sys.argv[3])
rlo=float(sys.argv[4]) if len(sys.argv)>4 else 7.0; rhi=float(sys.argv[5]) if len(sys.argv)>5 else 8.6
s,z=load_shape(path,nr,nt)
_,f,L2,res,den=s.evaluate(z)
L=np.sqrt(L2); rho=L**3*f["rho"]; R=rho*res
W1=(1/z[0]+L2*f["ux"])*L*s.p.rr*s.p.ct; W2=(1/z[0]+L2*f["uy"])*L*s.p.rr*s.p.st
rx=L2*f["fx"]; ry=L2*(s.p.st*f["rt"]+s.p.ct*f["ra"])/s.p.rr
dd=np.abs(W1*rx)+np.abs(W2*ry)+np.abs(rho)
q=(R/dd)[:,1:-1]; r=s.p.r*L; th=s.p.theta[1:-1]  # axis rows dropped (0/0 there)
mmax=int(np.load(path)["angular"])
dth=np.diff(th); uniform=float(np.max(np.abs(dth-dth.mean()))/dth.mean())
om=np.arange(0,4*mmax+1)
rows=[]
for i in np.where((r>=rlo)&(r<=rhi))[0][::max(1,int(np.sum((r>=rlo)&(r<=rhi))//40))]:
    a=q[i]; w=np.gradient(th)
    amp=np.abs(np.exp(-1j*np.outer(om,th))@(a*w))*2/np.pi
    k=int(np.argmax(amp[20:]))+20
    near=amp[max(0,2*mmax-8):2*mmax+9]
    rows.append(dict(r=float(r[i]),max_abs=float(np.max(np.abs(a))),th_at_max=float(th[np.argmax(np.abs(a))]),
                     peak_omega=int(om[k]),peak_amp=float(amp[k]),amp_2m_band=float(near.max()),
                     omega_2m_band=int(om[max(0,2*mmax-8)+int(np.argmax(near))]),low_amp=float(amp[:20].max())))
out=dict(file=path,nr=nr,nt=nt,mmax=mmax,theta_nonuniform=uniform,rows=rows)
o=path.replace('_shape.npz','')+'_angspec_%d_%d.json'%(nr,nt)
json.dump(out,open(o,'w'),indent=1)
for x in rows: print('r %.3f max|q| %.3e at th %.4f | peak omega %d amp %.2e | 2m band omega %d amp %.2e | low %.2e'%(x['r'],x['max_abs'],x['th_at_max'],x['peak_omega'],x['peak_amp'],x['omega_2m_band'],x['amp_2m_band'],x['low_amp']))
