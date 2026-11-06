"""Gate solved forward pairs before considering mathematical scalar derivatives."""
import argparse
from spectral import *
from collars import collars
from compare_fields import compare
def qualified(pa,pb):
 da=np.load(pa);db=np.load(pb);ab=[audit(da),audit(db)];col=collars(db);cmp=compare(da,db)
 aa,bb=[max(z[s]['transport'] for s in ['i','o']) for z in ab];po=max(ab[1][s]['poisson'] for s in ['i','o']);j=float(db['J'])
 tests=dict(algebra=bool(da['ok'] and db['ok']) and max(da['res'],db['res'])<2e-9,PDE=max(col['origin']['transport'],col['far']['transport'],col['origin']['poisson'],col['far']['poisson'])<2e-6 and bb<=3e-5 and po<=2e-6, angular=bb<=.75*aa or max(aa,bb)<3e-7,J_stable=cmp['Jdiff']<min(3e-7,3e-5*abs(j)),field_stable=max(cmp['rho_rel_i'],cmp['rho_rel_o'])<1e-4,trace=max(col['Jdiff'],col['Jhigh_kinematic'],db['higher'],db['bc'])<1e-8)
 return dict(coarse=str(pa),fine=str(pb),Thi=bb,Tlo=aa,Phi=po,Jlo=float(da['J']),J=j,common=cmp,collar={k:col[k] for k in ['Jdiff','Jhigh_kinematic','far_ujump','origin_jump']},tests={k:bool(v) for k,v in tests.items()},passed=bool(all(tests.values())))
def build(d,a=None):
 arg={k:d[k].item() for k in ['c','a','nf','ng','mi','mo','p','li','lo']};return Spectral(**dict(arg,a=arg['a'] if a is None else a))
def sens(pa):
 pp=Path(pa);out=pp.with_suffix('.deriv.npz')
 if out.exists():return dict(np.load(out))
 f=np.load(pa);x=build(f).derivatives(f,True);np.savez_compressed(out,**x);pp.with_suffix('.deriv.json').write_text(json.dumps({k:v for k,v in x.items() if np.ndim(v)==0},indent=2))
 return x
def predict(d,v,da):
 z=dict(d);z['v_i']=d['v_i']+da*v['va_i']+da**2/2*v['vaa_i'];z['v_o']=d['v_o']+da*v['va_o']+da**2/2*v['vaa_o'];return z
def nearby(pa,da,out):
 d=np.load(pa);v=sens(pa);nf=build(d,a=float(d['a'])+da);q=nf.solve(predict(d,v,da),tol=8e-12);np.savez_compressed(out,**q);return q
if __name__=='__main__':
 args=argparse.ArgumentParser();args.add_argument('coarse');args.add_argument('fine');args.add_argument('--out',required=True);args.add_argument('--derivatives',action='store_true');args.add_argument('--parallel',action='store_true');args=args.parse_args()
 g=qualified(args.coarse,args.fine);Path(args.out).write_text(json.dumps(g,indent=2));print(g['tests'],g['Thi'],g['common']['Jdiff'],flush=True)
 if args.derivatives and g['passed']:
  if args.parallel:
   import concurrent.futures as cf
   with cf.ProcessPoolExecutor(max_workers=2) as pool:
    cc=pool.submit(sens,args.coarse);ff=pool.submit(sens,args.fine);c=cc.result();f=ff.result()
  else:c=sens(args.coarse);f=sens(args.fine)
  deriv={k:[float(c[k]),float(f[k])] for k in ['Jp','Jpp','res1','res2','base_res']}
  g['derivatives']=deriv;g['derivative_passed']=abs(c['Jp']-f['Jp'])<max(2e-7,2e-4*abs(f['Jp'])) and abs(c['Jpp']-f['Jpp'])<max(2e-7,2e-3*abs(f['Jpp']))
  g['derivative_passed']=bool(g['derivative_passed']);Path(args.out).write_text(json.dumps(g,indent=2));print('derivatives',deriv,g['derivative_passed'],flush=True)
