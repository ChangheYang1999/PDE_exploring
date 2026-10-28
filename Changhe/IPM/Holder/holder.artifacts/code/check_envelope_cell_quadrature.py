"""Directly compare the LP cell quadrature with its continuous envelope."""
from pathlib import Path
from datetime import datetime,timezone
from envelope_witness import Envelope
import numpy as np,json
from numpy.polynomial.legendre import leggauss

def kernel(X,Y):
    return ((X-.5)**2-Y*Y)/(2*np.pi*((X-.5)**2+Y*Y)**2)-((X+.5)**2-Y*Y)/(2*np.pi*((X+.5)**2+Y*Y)**2)

def run(ng):
    data=json.loads((Path(__file__).resolve().parents[1]/'numerics_data/lp4/D_a05_b0.json').read_text())
    params=data['params'];g,w=leggauss(ng);f=Envelope();rows=[]
    n=np.array(data['nodes']);n[:,0]-=.5;mass=np.array(data['masses']);lab=np.array(data['labels']);fv=f.evaluate(n)[0]
    for label,center,J,nt,theta0 in [(0,-.5,data['info']['J'],params['ntheta'],np.pi/4),(1,.5,data['info']['J'],params['ntheta'],np.pi/4),(2,0,data['info']['Jf'],params['ntheta_f'],0)]:
        ii=np.flatnonzero(lab==label);parts=[]
        for j in range(J):
            if label==2:lo=2.**j;hi=2.**(j+1)
            else:lo=.5*2.**(-j-1);hi=.5*2.**(-j)
            logr=(np.log(lo)+np.log(hi))/2+np.log(hi/lo)/2*g
            angle=theta0+2*np.pi*(np.arange(nt)[:,None]+(g[None,:]+1)/2)/nt
            r=np.exp(logr)[:,None,None];th=angle[None,:,:]
            X=center+r*np.cos(th);Y=r*np.sin(th);points=np.column_stack([X.ravel(),Y.ravel()])
            values=f.evaluate(points)[0].reshape(X.shape)
            if label in [0,1]:
                fp=f.evaluate([[center,0]])[0][0]
                own=np.cos(2*th)/(2*np.pi*r*r)*(1 if label==1 else -1)
                integrand=kernel(X,Y)*values-own*fp
            else:integrand=kernel(X,Y)*values
            value=float(np.sum(integrand*r*r*w[:,None,None]*w[None,None,:])*np.log(hi/lo)/2*np.pi/nt)
            center_value=float(mass[ii[j*nt:(j+1)*nt]]@fv[ii[j*nt:(j+1)*nt]])
            parts.append(dict(shell=j,continuous=value,discrete=center_value))
        rows.append(dict(label=label,parts=parts,continuous_sum=sum(p['continuous'] for p in parts),discrete_sum=sum(p['discrete'] for p in parts)))
    return dict(gauss_order=ng,rows=rows)
if __name__=='__main__':
    rows=[]
    for n in [2,4,8]:
        row=run(n);rows.append(row);print(n,[(r['label'],r['continuous_sum'],r['discrete_sum']) for r in row['rows']],flush=True)
    Path('data/envelope_cell_comparison.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows,status='Floating consistency diagnostic, not a theorem'),indent=2)+'\n')
