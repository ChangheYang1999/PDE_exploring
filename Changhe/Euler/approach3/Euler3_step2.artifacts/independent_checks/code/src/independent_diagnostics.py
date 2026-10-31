"""Spatial AD of the independently reconstructed field for vorticity checks."""
import numpy as np
import torch

def curl_from_du(du):
    return torch.stack((du[:,2,1]-du[:,1,2],du[:,0,2]-du[:,2,0],du[:,1,0]-du[:,0,1]),1)

def field_vorticity(field,points,parameter=None,batch=128):
    results={key:[] for key in ['U','DU','Omega','DOmega']}
    for start in range(0,len(points),batch):
        y=torch.tensor(np.asarray(points[start:start+batch]),device=field.device,dtype=torch.float64,requires_grad=True)
        u,du=field.torch_parameter_values(y,parameter)
        om=curl_from_du(du)
        dom=torch.stack([torch.autograd.grad(om[:,i].sum(),y,retain_graph=(i<2))[0] for i in range(3)],1)
        for key,value in zip(results,[u,du,om,dom]):results[key].append(value.detach().cpu().numpy())
    return {key:np.concatenate(parts) for key,parts in results.items()}

def vorticity_residual(points,values,c_l,omega):
    u,du,om,dom=[values[key] for key in ['U','DU','Omega','DOmega']]
    jy=np.stack((-points[:,1],points[:,0],np.zeros(len(points))),axis=1)
    jom=np.stack((-om[:,1],om[:,0],np.zeros(len(points))),axis=1)
    w=c_l*points-omega*jy+u
    return om+np.einsum('nij,nj->ni',dom,w)+omega*jom-np.einsum('nij,nj->ni',du,om)
