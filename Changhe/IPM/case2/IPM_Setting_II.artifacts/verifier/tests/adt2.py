import torch, sys
sys.path.insert(0,'code')
import torch.autograd.forward_ad as fwAD
exec(open('tests/adtest.py').read().split("with fwAD.dual_level():")[0])
dA=dB=None
with fwAD.dual_level():
    Ad,Bd=parts(fwAD.make_dual(Vr,dV)); dA=fwAD.unpack_dual(Ad).tangent.clone(); dB=fwAD.unpack_dual(Bd).tangent.clone()
G0=torch.linalg.solve(A,B); dG_ex=torch.linalg.solve(A,dB-dA@G0)
print('dA nonzero frac',float((dA!=0).double().mean()),'|dA|',float(dA.abs().max()),'|dB|',float(dB.abs().max()))
for trial in range(3):
    with fwAD.dual_level():
        Ad,Bd=parts(fwAD.make_dual(Vr,dV))
        pA=fwAD.unpack_dual(Ad).primal; tA=fwAD.unpack_dual(Ad).tangent
        X=torch.linalg.solve(Ad,Bd); torch.cuda.synchronize()
        px=fwAD.unpack_dual(X).primal; tx=fwAD.unpack_dual(X).tangent
        print(trial,'primal A diff',float((pA-A).abs().max()),'tA diff',float((tA-dA).abs().max()),'X primal diff',float((px-G0).abs().max()),'X tangent rel',float((tx-dG_ex).abs().max()/dG_ex.abs().max()))
# without parts in dual: make_dual directly on A,B
for trial in range(2):
    with fwAD.dual_level():
        X=torch.linalg.solve(fwAD.make_dual(A,dA),fwAD.make_dual(B,dB))
        tx=fwAD.unpack_dual(X).tangent
        print('direct dual', trial, float((tx-dG_ex).abs().max()/dG_ex.abs().max()))
    with fwAD.dual_level():
        X=torch.linalg.solve(fwAD.make_dual(A[:10],dA[:10]),fwAD.make_dual(B[:10],dB[:10]))
        tx=fwAD.unpack_dual(X).tangent
        print('direct dual first 10', trial, float((tx-dG_ex[:10]).abs().max()/dG_ex[:10].abs().max()))
    with fwAD.dual_level():
        X=torch.linalg.solve(fwAD.make_dual(A[3],dA[3]),fwAD.make_dual(B[3],dB[3]))
        tx=fwAD.unpack_dual(X).tangent
        print('direct dual single', trial, float((tx-dG_ex[3]).abs().max()/dG_ex[3].abs().max()))
