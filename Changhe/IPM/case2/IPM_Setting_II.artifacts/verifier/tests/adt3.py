import torch, sys
sys.path.insert(0,'code')
import torch.autograd.forward_ad as fwAD
exec(open('tests/adt2.py').read().split("for trial in range(3):")[0])
print('default lib', torch.backends.cuda.preferred_linalg_library())
for lib in ['cusolver','magma']:
    torch.backends.cuda.preferred_linalg_library(lib)
    with fwAD.dual_level():
        X=torch.linalg.solve(fwAD.make_dual(A,dA),fwAD.make_dual(B,dB))
        px=fwAD.unpack_dual(X).primal; tx=fwAD.unpack_dual(X).tangent
    print(lib,'primal',float((px-G0).abs().max()),'tangent rel',float((tx-dG_ex).abs().max()/dG_ex.abs().max()))
    X2=torch.linalg.solve(A,B); print(lib,'nondual primal',float((X2-G0).abs().max()))
torch.backends.cuda.preferred_linalg_library('default')
# loop of single dual solves
with fwAD.dual_level():
    Ad=fwAD.make_dual(A,dA); Bd=fwAD.make_dual(B,dB)
    X=torch.stack([torch.linalg.solve(Ad[k],Bd[k]) for k in range(npn)])
    px=fwAD.unpack_dual(X).primal; tx=fwAD.unpack_dual(X).tangent
print('loop primal',float((px-G0).abs().max()),'tangent rel',float((tx-dG_ex).abs().max()/dG_ex.abs().max()))
