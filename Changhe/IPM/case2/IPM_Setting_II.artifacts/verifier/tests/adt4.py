import torch, sys, time
sys.path.insert(0,'code')
import torch.autograd.forward_ad as fwAD
nt0=int(sys.argv[1])
exec(open('tests/adtest.py').read().split("torch.manual_seed(1)")[0].replace("nt=int(sys.argv[1])","nt=nt0"))
torch.manual_seed(1); dV=torch.randn_like(Vr)*Vr.abs()*1e-3
z0=S.r1*(l[0]*torch.cos(S.th)+l[1]*torch.sin(S.th))
e=1e-6
for lib in ['default','cusolver']:
    torch.backends.cuda.preferred_linalg_library(lib)
    torch.cuda.synchronize(); t0=time.time()
    for _ in range(3):
        with fwAD.dual_level():
            o=S.march(fwAD.make_dual(Vr,dV),Vt,z0); t=fwAD.unpack_dual(o).tangent
    torch.cuda.synchronize(); tj=(time.time()-t0)/3
    t0=time.time(); o_fd=(S.march(Vr+e*dV,Vt,z0)-S.march(Vr-e*dV,Vt,z0))/(2*e); torch.cuda.synchronize(); tp=(time.time()-t0)/2
    print(nt0,lib,'jvp time',round(tj,3),'primal time',round(tp,3),'ad vs fd rel',float((t-o_fd).abs().max()/o_fd.abs().max()))
