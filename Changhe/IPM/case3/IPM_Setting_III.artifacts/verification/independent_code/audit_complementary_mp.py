"""High-precision analytic density derivatives with separately refined canonical U/r."""
import argparse,json,hashlib,math
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp
from q_checkpoint_reader import QCheckpoint
from q_high_precision_density import MPQDensity
ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--evaluation',required=True);ap.add_argument('--tag',required=True);args=ap.parse_args()
cand=QCheckpoint(args.snapshot);ev=json.loads(Path(args.evaluation).read_text())
assert cand.meta['sha256']==ev['sha256']
rows=[]
for digits in [70,110]:
    mp.mp.dps=digits;model=MPQDensity(cand.coeff,cand.L,cand.kappa,cand.cl)
    ec=model.kappa/(model.kappa-1);mpoints=[]
    for j,point in enumerate(ev['rows'][-1]['points']):
        if point['y']==0:continue
        x=mp.mpf(float(point['x']));y=mp.mpf(float(point['y']));r=mp.sqrt(x*x+y*y);theta=mp.atan2(y,x);nx=x/r;ny=y/r
        rho,gx,gy=model.at(r,theta);comparisons=[]
        for row in ev['rows'][-2:]:
            old=row['points'][j];ux,uy=map(mp.mpf,old['U_over_r']);variants={}
            for label,ell in [('binary_ell',model.ell),('coupled_ell',ec)]:
                tx=(ell*nx+ux)*gx;ty=(ell*ny+uy)*gy
                residual=tx+ty-rho;nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(nx*gx+ny*gy)+abs(ux*gx+uy*gy)
                variants[label]={'R_over_r':mp.nstr(residual,55),'abs_R':mp.nstr(abs(residual)*r,55),'R_Nf':mp.nstr(abs(residual)/nf,55),'R_Nv':mp.nstr(abs(residual)/nv,55),'Nf':mp.nstr(nf*r,55),'Nv':mp.nstr(nv*r,55)}
            gd=mp.sqrt(gx*gx+gy*gy);derr=mp.sqrt(sum((mp.mpf(v)-g)**2 for v,g in zip(old['gradient'],[gx,gy])))/gd
            comparisons.append({'order':row['order'],'variants':variants,'double_R_Nf':old['R_Nf'],'relative_gradient_difference':mp.nstr(derr,40)})
        mpoints.append({'x':point['x'],'y':point['y'],'log10_radius':float(mp.log10(r)),'rho_over_r':mp.nstr(rho,55),'gradient':[mp.nstr(g,55) for g in [gx,gy]],'comparisons':comparisons})
    row={'precision_digits':digits,'points':mpoints,'ell':mp.nstr(model.ell,60),'coupled_ell':mp.nstr(ec,60),'ell_change':mp.nstr(ec-model.ell,60),'binary_leading_defect':mp.nstr(model.ell*(1-1/model.kappa)-1,60),'summary':{}}
    for variant in ['binary_ell','coupled_ell']:
        rs={}
        for field in ['abs_R','R_Nf','R_Nv']:
            q=max(mpoints,key=lambda z:mp.mpf(z['comparisons'][-1]['variants'][variant][field]));rs[field]={'value':q['comparisons'][-1]['variants'][variant][field],'x':q['x'],'y':q['y'],'log10_radius':q['log10_radius']}
        row['summary'][variant]=rs
    rows.append(row)
    out={'updated_utc':datetime.now(timezone.utc).isoformat(),'snapshot':args.snapshot,'sha256':cand.meta['sha256'],'evaluation':args.evaluation,'rows':rows,'scope':'Independent MP density derivative and arithmetic, with double-precision canonical inverse at two refined orders. Saved binary ell and a separately labeled adjusted ell are both reported. No interval enclosure, global maximum or nearby-profile theorem.'}
    dest=Path('evidence/complementary_mp')/args.tag;dest.mkdir(parents=True,exist_ok=True);(dest/'diagnostic.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'digits':digits,'summary':row['summary'],'utc':out['updated_utc']}),flush=True)
