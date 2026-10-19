"""Reproducible checks for the added D14 rows and tensor storage."""
import importlib.util
import json
from pathlib import Path
import numpy as np
from centre_fit import CentreShape,CentreDerivative,load_shape

root=Path("construct1")
spec=importlib.util.spec_from_file_location("reference_stationary",root/"stationary.py")
ref=importlib.util.module_from_spec(spec);spec.loader.exec_module(ref)
rng=np.random.default_rng(412)
d=10;a=4;k=.18
z=np.r_[k,rng.normal(0,.015,(a+1)*d),rng.normal(0,.015,2)]
s=CentreShape(192,32,100,d,a,"matched",2)
s.configure(dict(z=z,degree=d,angular=a,spline_order=7,origin_radius=.02))
old=ref.Shape(192,32,100,d,a,"matched",2)
old.radial_basis="spline";old.spline_order=7;old.origin_radius=.02
old.p.tail_terms=2;old.build_basis(k)
new_fields=s.evaluate(z);old_fields=old.evaluate(z)
equivalence={key:float(np.max(np.abs(new_fields[1][key]-old_fields[1][key])))
             for key in ("rho","ht","ha","q","v","ux","uy","haa_axis")}
equivalence["residual_max"]=float(np.max(np.abs(new_fields[3]-old_fields[3])))
op=CentreDerivative(s,z)
u=rng.normal(size=len(z));u/=np.linalg.norm(u)
y=rng.normal(size=op.shape[0]);y/=np.linalg.norm(y)
lhs=np.dot(op@u,y);rhs=np.dot(u,op.rmatvec(y))
checks=[]
for eps in (1e-4,1e-5,1e-6):
    fd=(s.raw_fun(z+eps*u)[0]-s.raw_fun(z-eps*u)[0])/(2*eps)
    jv=op@u
    checks.append(dict(eps=eps,relative=float(np.linalg.norm(fd-jv)/np.linalg.norm(jv)),
                       centre_fd=fd[-2:].tolist(),centre_jv=jv[-2:].tolist()))
result=dict(tensor_equivalence=equivalence,
            adjoint_relative=abs(lhs-rhs)/max(abs(lhs),abs(rhs)),finite_differences=checks)
Path("centre/verification/tensor_derivative.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
if "--start" in __import__("sys").argv:
    del old,s,op,new_fields,old_fields
    s,z=load_shape(root/"final_shape.npz")
    f,cen,src=s.raw_fun(z)
    result=dict(centre=cen,objective=float(np.linalg.norm(f)),source=src,
                shape_radius_min=float(s.p.r[s.rows][0]),rows=int(np.sum(s.rows)),columns=len(s.cols))
    Path("centre/verification/start_tensor.json").write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
