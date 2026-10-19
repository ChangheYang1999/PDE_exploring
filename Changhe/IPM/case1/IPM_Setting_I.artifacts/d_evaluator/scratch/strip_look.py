import sys, numpy as np
d=np.load(sys.argv[1])
r,th,R,Nf=d['r'],d['th'],d['R'],d['Nf']
with np.errstate(all='ignore'): x=np.where(Nf>0,R/Nf,0.0)
x[:, (th<1e-9)|(th>1.5)] = 0
i,j=np.unravel_index(np.argmax(np.abs(x)),x.shape)
print('max %.3e r %.4f th %.4f (x %.4f y %.4f) dth %.5f dr %.4f'%(x[i,j],r[i],th[j],r[i]*np.cos(th[j]),r[i]*np.sin(th[j]),th[1]-th[0],r[i+1]-r[i]))
print('theta profile at max r')
for jj in range(0,40): print('  th %.4f y %.4f R/Nf % .3e  R % .3e Nf %.3e'%(th[jj], r[i]*np.sin(th[jj]), x[i,jj], R[i,jj], Nf[i,jj]))
print('r profile at max th')
for ii in range(max(0,i-40),min(len(r),i+40)): print('  r %.4f R/Nf % .3e R % .3e'%(r[ii], x[ii,j], R[ii,j]))
