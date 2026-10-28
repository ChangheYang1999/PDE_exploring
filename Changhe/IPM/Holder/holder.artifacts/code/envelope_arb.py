"""Outward ball evaluation of exact finite cone envelopes at alpha=1/2.
Tree traversal choices are heuristics. Every skipped subtree is bounded
by exact rectangle and data-value enclosures before it is discarded.
"""
from pathlib import Path
from decimal import Decimal
from flint import arb,ctx
from scipy.spatial import cKDTree
import numpy as np,json

class Node:
    __slots__=('box','vmin','vmax','children','indices')
    def __init__(self,box,vmin,vmax,children,indices):
        self.box=box;self.vmin=vmin;self.vmax=vmax
        self.children=children;self.indices=indices

class ArbEnvelope:
    def __init__(self,path='data/envelope_D_half_axis_nodes_symmetric.json',leaf_size=8):
        data=json.loads(Path(path).read_text());assert data['alpha']=='1/2'
        dec=[[Decimal(x) for x in row] for row in data['nodes']]
        self.exact=[tuple(arb(str(x)) for x in row) for row in dec]
        self.float=np.array(data['nodes'],dtype=float)
        self.kdtree=cKDTree(self.float[:,:2]);self.leaf_size=leaf_size
        def build(indices):
            box=tuple(arb(str(fun(dec[i][j] for i in indices))) for j in [0,1] for fun in [min,max])
            vmin=arb(str(min(dec[i][2] for i in indices)));vmax=arb(str(max(dec[i][2] for i in indices)))
            if len(indices)<=leaf_size:return Node(box,vmin,vmax,None,indices)
            spans=np.ptp(self.float[indices,:2],axis=0);axis=int(np.argmax(spans))
            indices=sorted(indices,key=lambda i:self.float[i,axis]);k=len(indices)//2
            return Node(box,vmin,vmax,(build(indices[:k]),build(indices[k:])),None)
        self.root=build(list(range(len(dec))))
        self.last_counts=None
    def evaluate(self,x,y):
        x=arb(x);y=arb(y)
        _,initial=self.kdtree.query([float(x.mid()),float(y.mid())])
        def cone(i):
            px,py,v=self.exact[i]
            d=((x-px)**2+(y-py)**2).sqrt();a=d.sqrt()
            return v+a,v-a,d
        U,L,nearest=cone(int(initial))
        counts=dict(nodes=0,leaves=0,vertices=1,pruned=0)
        stack=[self.root]
        while stack:
            node=stack.pop();counts['nodes']+=1
            xmin,xmax,ymin,ymax=node.box
            dx=arb.max(arb(0),arb.max(arb((xmin-x).lower()),arb((x-xmax).lower())))
            dy=arb.max(arb(0),arb.max(arb((ymin-y).lower()),arb((y-ymax).lower())))
            lower=(dx*dx+dy*dy).sqrt();power=lower.sqrt()
            if node.vmin+power>=U and node.vmax-power<=L and lower>=nearest:
                counts['pruned']+=1;continue
            if node.indices is not None:
                counts['leaves']+=1
                for i in node.indices:
                    a,b,d=cone(i);U=arb.min(U,a);L=arb.max(L,b);nearest=arb.min(nearest,d);counts['vertices']+=1
            else:
                # Order affects speed only. Both children remain subject to certified bounds.
                ca,cb=node.children
                def heuristic(child):
                    aa,bb,cc,dd=child.box
                    xx=float(x.mid());yy=float(y.mid())
                    return max(float(aa.mid())-xx,0,xx-float(bb.mid()))**2+max(float(cc.mid())-yy,0,yy-float(dd.mid()))**2
                if heuristic(ca)<heuristic(cb):stack.extend([cb,ca])
                else:stack.extend([ca,cb])
        self.last_counts=counts
        return (U+L)/2,nearest
