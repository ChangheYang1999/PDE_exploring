"""Compare continuum-scaled physical fields on a common staggered radius/angle grid."""
from spectral import *
def compare(dc,df):
 th=np.arange(1201)*np.pi/2/1200;ls=min(float(dc['li']),float(df['li']));le=min(float(dc['lo']),float(df['lo']));cc=float(df['c']);j=0
 out={'Jdiff':float(abs(dc['J']-df['J']))};tail={}
 for j,side in enumerate(['i','o']):
  z=np.linspace(-ls,0,85) if not j else np.unique(np.r_[np.linspace(0,le,257),np.linspace(0,min(10.,le),151)])
  vals=[];waves=[]
  for d in [dc,df]:
   f,g,p=int(d['nf']),int(d['ng']),int(d['p']);S=np.sin((2*np.arange(f)+1)[:,None]*th)
   k=2*np.arange(1,g+1);E=np.sin(k[:,None]*th);D=k[:,None]*np.cos(k[:,None]*th);v=evalpoly(d['edge_'+side],d['v_'+side],p,z)
   rho=v[:,:f]@S;psi=v[:,f:f+g]@E;utheta=v[:,f:f+g]@D;ur=v[:,f+g:]@E;vals.append([rho,psi,utheta,ur])
   lift=1 if not j else np.exp((1/cc-1)*z)[:,None]
   if d is df:out['min_crad_'+side]=float(np.min(cc-lift*utheta));out['max_speed_over_r_'+side]=float(np.max(lift*np.hypot(ur,utheta)))
   tails={}; 
   for first,name in [(0,'rho'),(f,'psi'),(f+g,'U')]:
    length=f if name=='rho' else g;v0=v[:,first:first+length]
    tails[name]=[float(np.max(np.sum(np.abs(v0[:,max(0,length-width):]),axis=1))) for width in [1,4,8]]
   waves.append(tails)
  for u,key in enumerate(['rho','psi','utheta','ur']):
   coarse,fine=vals[0][u],vals[1][u];err=abs(coarse-fine)
   out[key+'_abs_'+side]=float(np.max(err));out[key+'_rel_'+side]=float(np.max(err/(1+np.max(np.abs(fine),axis=1)[:,None])))
  tail[side]=waves
 out['spectral_last_1_4_8_l1']=tail
 return out
if __name__=='__main__':
 a,b,out=sys.argv[1:];d=compare(np.load(a),np.load(b));Path(out).write_text(json.dumps(d,indent=2));print({k:v for k,v in d.items() if 'rho_rel' in k or k=='Jdiff'})
