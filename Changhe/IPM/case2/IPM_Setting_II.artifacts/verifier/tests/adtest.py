import torch, sys, math
sys.path.insert(0,'code')
import torch.autograd.forward_ad as fwAD
from forced_pal import ExtSolver
nt=int(sys.argv[1])
D=torch.load('runs/fx_mu1_L4_h0.200.pt',weights_only=False); A0=D['args']
xi=D['xi'].double()
if nt!=D['nt']: xi=torch.fft.irfft(torch.fft.rfft(xi,dim=1),n=nt,dim=1)*(nt/D['nt'])
S=ExtSolver(D['edges'],D['q'],nt,D['r1'],'cuda'); S.set_forcing(0.0,A0['mu'],A0['LE'])
xi=xi.cuda(); p=torch.tensor(D['d']['p'],dtype=torch.float64,device='cuda'); h=torch.tensor(0.2,dtype=torch.float64,device='cuda')
rho=xi**2; c,b=S.moments(rho,p); cl,l=S.jet(h*c+(1-h)*S.mu,h*b)
W1,W2=S.velocity(rho,p); W1=h*W1+(1-h)*S.E1; W2=h*W2+(1-h)*S.E2
Vr=cl*S.R+W1*S.cs+W2*S.sn; Vt=(-W1*S.sn+W2*S.cs)/S.R
q,P,p0=S.q,S.P,S.p0; npn=P-p0
torch.manual_seed(1); dV=torch.randn_like(Vr)*Vr.abs()*1e-3
def parts(Vr):
    Vr_p=Vr[p0*q:].reshape(npn,q,nt); Vt_p=Vt[p0*q:].reshape(npn,q,nt)
    Dt=S.Dt[None]/S.hp[p0:,None,None]
    eq=torch.eye(q,dtype=torch.float64,device='cuda'); et=torch.eye(nt,dtype=torch.float64,device='cuda')
    A=(Vr_p[:,:,:,None,None]*Dt[:,:,None,1:,None]*et[None,None,:,None,:]+Vt_p[:,:,:,None,None]*eq[None,:,None,:,None]*S.Dth[None,None,:,None,:]-0.5*eq[None,:,None,:,None]*et[None,None,:,None,:]).reshape(npn,q*nt,q*nt)
    B=(-(Vr_p*Dt[:,:,0:1])[:,:,:,None]*et[None,None,:,:]).reshape(npn,q*nt,nt)
    return A,B
A,B=parts(Vr)
with fwAD.dual_level():
    Ad,Bd=parts(fwAD.make_dual(Vr,dV))
    dA=fwAD.unpack_dual(Ad).tangent; dB=fwAD.unpack_dual(Bd).tangent
    Gd=torch.linalg.solve(Ad,Bd); G=fwAD.unpack_dual(Gd).primal; dG_ad=fwAD.unpack_dual(Gd).tangent
G0=torch.linalg.solve(A,B)
dG_ex=torch.linalg.solve(A,dB-dA@G0)
e=1e-6
Ap,Bp=parts(Vr+e*dV); Am,Bm=parts(Vr-e*dV)
dG_fd=(torch.linalg.solve(Ap,Bp)-torch.linalg.solve(Am,Bm))/(2*e)
for k in [0,5,10,15,20,22,23,24,25,30,40,npn-1]:
    if k>=npn: continue
    s=float(dG_fd[k].abs().max())
    print(k,'|G|',f'{float(G0[k].abs().max()):.2e}','|dG_fd|',f'{s:.2e}','ad-fd',f'{float((dG_ad[k]-dG_fd[k]).abs().max())/s:.1e}','ex-fd',f'{float((dG_ex[k]-dG_fd[k]).abs().max())/s:.1e}','cond',f'{float(torch.linalg.cond(A[k])):.1e}')
print('--- full march')
z0=S.r1*(l[0]*torch.cos(S.th)+l[1]*torch.sin(S.th))
with fwAD.dual_level():
    o=S.march(fwAD.make_dual(Vr,dV),Vt,z0); o_ad=fwAD.unpack_dual(o).tangent
o_fd=(S.march(Vr+e*dV,Vt,z0)-S.march(Vr-e*dV,Vt,z0))/(2*e)
# manual tangent using dG_ex
Eright=S.Eright; et=torch.eye(nt,dtype=torch.float64,device='cuda')
Gp=G0.reshape(npn,q,nt,nt); dGp=dG_ex.reshape(npn,q,nt,nt)
Pi=Eright[0]*et[None]+torch.einsum('k,pkjl->pjl',Eright[1:],Gp); dPi=torch.einsum('k,pkjl->pjl',Eright[1:],dGp)
zl=z0; dz=torch.zeros_like(z0); man=[]
for k in range(npn):
    man.append(torch.einsum('kjl,l->kj',dGp[k],zl)+torch.einsum('kjl,l->kj',Gp[k],dz))
    dz=dPi[k]@zl+Pi[k]@dz; zl=Pi[k]@zl
man=torch.stack(man,0).reshape(npn*q,nt)
for k in range(0,npn,4):
    sl=slice(k*q,(k+1)*q); s=float(o_fd[sl].abs().max())
    print(k,f'fd {s:.2e} ad {float(o_ad[sl].abs().max()):.2e} man {float(man[sl].abs().max()):.2e} man-fd {float((man[sl]-o_fd[sl]).abs().max())/s:.1e}')
print('--- staged')
with fwAD.dual_level():
    Ad,Bd=parts(fwAD.make_dual(Vr,dV))
    X=torch.linalg.solve(Ad,Bd)
    t=fwAD.unpack_dual(X).tangent; print('solve tangent stride',t.stride(),'primal stride',fwAD.unpack_dual(X).primal.stride(), 'err',float((t-dG_ex).abs().max()))
    Gpd=X.reshape(npn,q,nt,nt)
    t=fwAD.unpack_dual(Gpd).tangent; print('reshape tangent stride',t.stride(),'err',float((t-dGp).abs().max()))
    Pid=Eright[0]*et[None]+torch.einsum('k,pkjl->pjl',Eright[1:],Gpd)
    t=fwAD.unpack_dual(Pid).tangent; print('Pi tangent err',float((t-dPi).abs().max()), float(dPi.abs().max()))
    o0=torch.einsum('kjl,l->kj',Gpd[0],z0); t=fwAD.unpack_dual(o0).tangent
    print('out0 err',float((t-torch.einsum('kjl,l->kj',dGp[0],z0)).abs().max()), float(torch.einsum('kjl,l->kj',dGp[0],z0).abs().max()))
    z1=Pid[0]@z0; t=fwAD.unpack_dual(z1).tangent; print('z1 err',float((t-dPi[0]@z0).abs().max()), float((dPi[0]@z0).abs().max()))
    o1=torch.einsum('kjl,l->kj',Gpd[1],z1); t=fwAD.unpack_dual(o1).tangent
    ref=torch.einsum('kjl,l->kj',dGp[1],Pi[0]@z0)+torch.einsum('kjl,l->kj',Gp[1],dPi[0]@z0)
    print('out1 err',float((t-ref).abs().max()), float(ref.abs().max()))
print('--- per panel solve tangent, 2 trials')
for trial in range(2):
    with fwAD.dual_level():
        Ad,Bd=parts(fwAD.make_dual(Vr,dV))
        t=fwAD.unpack_dual(torch.linalg.solve(Ad,Bd)).tangent
    err=(t-dG_ex).abs().amax(dim=(1,2)); ref=dG_ex.abs().amax(dim=(1,2))
    print([f'{k}:{float(err[k]/ref[k]):.0e}' for k in range(npn)])
