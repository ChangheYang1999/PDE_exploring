"""Fixed positive quadrature nodes on three transformed whole-radius blocks.

All three parameter intervals are finite Gauss integration intervals. The
origin and infinity are covered by changes of variables, rather than omitted
from the residual vector. A finite Gauss rule is still an approximation and
does not become an exactly invariant integral or a certified error enclosure.
"""
import math
import os
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Whole-axis mesh preparation requires a resource supervisor')
import numpy as np
from absolute_model import FrozenLogMesh


def _unit_gauss(order):
    if not isinstance(order,int) or order<1:raise ValueError('Positive integer Gauss order required')
    z,w=np.polynomial.legendre.leggauss(order)
    return (z+1)/2,w/2


def build_whole_axis_mesh(origin_radius,upper_log_radius,origin_order=24,middle_order=16,
                          infinity_order=64,angular_order=96,panel_width=1.,name='whole_axis_fixed'):
    """Return (FrozenLogMesh, metadata, node-block identifiers).

    Origin: r=r0*u, ds=du/u, u in (0,1).
    Middle: s in [log(r0),S], ordinary composite Gauss.
    Infinity: r=exp(S)/u, ds=-du/u, orientation reversed to u in (0,1).
    Weights and nodes do not depend on any optimization coefficient or cl.
    """
    r0=float(origin_radius);S=float(upper_log_radius);width=float(panel_width)
    if not (r0>0 and math.isfinite(r0) and math.isfinite(S) and width>0 and math.isfinite(width)):
        raise ValueError('Finite positive radius and panel width required')
    lo=math.log(r0)
    if not lo<S:raise ValueError('Middle interval must have positive width')
    ou,ow=_unit_gauss(origin_order);tu,tw=_unit_gauss(infinity_order)
    os=lo+np.log(ou);osw=ow/ou
    ts=S-np.log(tu);tsw=tw/tu
    z,w=np.polynomial.legendre.leggauss(middle_order)
    edges=np.linspace(lo,S,max(1,int(math.ceil((S-lo)/width)))+1)
    ms=np.concatenate([.5*(a+b+(b-a)*z) for a,b in zip(edges[:-1],edges[1:])])
    msw=np.concatenate([.5*(b-a)*w for a,b in zip(edges[:-1],edges[1:])])
    radial_s=np.r_[os,ms,ts];radial_w=np.r_[osw,msw,tsw]
    radial_blocks=np.r_[np.zeros(len(os),dtype=np.int8),np.ones(len(ms),dtype=np.int8),np.full(len(ts),2,dtype=np.int8)]
    au,aw=_unit_gauss(angular_order);angles=au*np.pi/2;angular_w=aw*np.pi/2
    s,theta=np.meshgrid(radial_s,angles,indexing='ij')
    mesh=FrozenLogMesh(s.ravel(),theta.ravel(),np.outer(radial_w,angular_w).ravel(),name)
    blocks=np.repeat(radial_blocks,len(angles))
    metadata={'schema':'absolute_loss_three_block_whole_axis_mesh_v1',
        'origin_radius':r0,'upper_log_radius':S,'origin_order':origin_order,
        'middle_order':middle_order,'infinity_order':infinity_order,
        'angular_order':angular_order,'middle_panel_width_max':width,
        'middle_panel_count':len(edges)-1,'radial_nodes':len(radial_s),
        'blocks':[{'id':0,'name':'origin','mapping':'s=log(r0)+log(u), 0<u<1','weight':'du/u',
            'radial_nodes':len(os),'log_radius_min_node':float(min(os)),'log_radius_max_node':float(max(os))},
            {'id':1,'name':'middle','mapping':'s in [log(r0), S]','weight':'ds',
            'radial_nodes':len(ms),'log_radius_min_node':float(min(ms)),'log_radius_max_node':float(max(ms))},
            {'id':2,'name':'infinity','mapping':'s=S-log(u), 0<u<1','weight':'du/u',
            'radial_nodes':len(ts),'log_radius_min_node':float(min(ts)),'log_radius_max_node':float(max(ts))}],
        'whole_axis_domain_covered_by_transformations':True,
        'weights_positive':bool(np.all(mesh.weights>0)),
        'nodes_and_weights_independent_of_cl_and_candidate_parameters':True,
        'origin_or_infinity_contribution_omitted_from_residual_vector':False,
        'finite_quadrature_is_exact_integral':False,
        'finite_quadrature_is_exactly_scale_invariant':False,
        'whole_axis_qualified':False,'neighborhood_validated':False,
        'mesh':mesh.record()}
    return mesh,metadata,blocks
