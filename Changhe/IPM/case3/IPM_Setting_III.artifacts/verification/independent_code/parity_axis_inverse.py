"""Direct-kernel parity interpolation. Does not use angular inverse data."""
import numpy as np

def interpolate_vertical(inverse,x,y,relative_h):
    scale=abs(float(x));h=scale*float(relative_h)
    if not h>0:raise ValueError('Requires a nonzero horizontal coordinate')
    nodes=np.array([1.,.25,.0625,.015625]);target=(float(y)/h)**2
    if target>1:raise ValueError('Target lies outside interpolation interval')
    weights=np.ones(4)
    for i in range(4):
        for j in range(4):
            if i!=j:weights[i]*=(target-nodes[j])/(nodes[i]-nodes[j])
    values=[];samples=[]
    for node in nodes:
        hi=h*np.sqrt(node);up=inverse.velocity(x,hi)[1];um=inverse.velocity(x,-hi)[1]
        value=(up-um)/(2*hi);values.append(value)
        samples.append(dict(h=float(hi),up=float(up),um=float(um),vertical_quotient=float(value),parity_sum=float(up+um)))
    quotient=float(weights@np.array(values))
    return dict(vertical_quotient=quotient,u2=float(y)*quotient,relative_h=float(relative_h),weights=weights.tolist(),weight_l1=float(np.sum(abs(weights))),samples=samples)
