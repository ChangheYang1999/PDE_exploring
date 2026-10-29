#!/usr/bin/env python3
"""Offline figures from saved failed approximations; no optimization or server."""
from pathlib import Path
import argparse,csv,datetime,hashlib,json,time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import roots_legendre
from independent_fields import PotentialField
from independent_geometry import reporting_gauge
from independent_tail_audit import tail_audit
ROOT=Path(__file__).resolve().parent
LANE=ROOT.parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True,type=Path);a=ap.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(LANE):raise ValueError('output outside lane')
    out.mkdir(parents=True,exist_ok=False);started=time.perf_counter();cpu=time.process_time()
    inputs={};figures=[]
    def read(path):
        inputs[str(path.relative_to(LANE))]=hashlib.sha256(path.read_bytes()).hexdigest()
        return json.loads(path.read_text())
    def table(name,rows):
        with (out/(name+'.csv')).open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    def save(fig,name,caption):
        fig.text(.01,.008,'Numerical approximation: acceptance failed. '+caption,fontsize=8,wrap=True)
        fig.tight_layout(rect=(0,.055,1,1))
        for suffix in ['png','pdf','svg']:fig.savefig(out/(name+'.'+suffix),dpi=165)
        plt.close(fig);figures.append(dict(name=name,caption=caption))
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.18})
    series=[]
    for level in range(3):
        directory=ROOT/f'exploration/sweep2/c0.740_q2_pole0_L{level}'
        summary=read(directory/'summary.json');config=read(directory/'configuration.json');coeff=read(directory/'best_field.json')
        series.append(dict(level=level,summary=summary,config=config,coeff=coeff))
    # 1. Different residual definitions stay in separate panels.
    rows=[dict(level=d['level'],unknowns=d['summary']['unknown_count'],objective=d['summary']['holdout']['objective_squared'],q_max=d['summary']['holdout']['raw_q_max'],eta_max=d['summary']['holdout']['raw_eta_max']) for d in series]
    table('resolution',rows);fig,ax=plt.subplots(1,2,figsize=(8.2,3.7));x=[r['unknowns'] for r in rows]
    ax[0].semilogy(x,[r['objective'] for r in rows],'o-',color='#2166ac');ax[0].set_ylabel('Custom holdout objective squared')
    for key,label,style in [('q_max','q equation','o-'),('eta_max','eta equation','s--')]:ax[1].semilogy(x,[r[key] for r in rows],style,label=label)
    ax[1].set_ylabel('Raw maximum residual');ax[1].legend()
    for aa in ax:aa.set_xlabel('Free coefficient count');aa.set_xticks(x)
    fig.suptitle('Source-compatible S1, c_l=0.74, K=2')
    save(fig,'resolution','Custom objective and raw maxima are distinct diagnostics.')
    audit=ROOT/'results/s1_refinement_c074_q2/L0/summary.json';reg=read(audit);aeff=reg['a_eff'];fieldpath=ROOT/'exploration/sweep2/c0.740_q2_pole0_L0/best_field.json'
    read(fieldpath);field,gauge=reporting_gauge(PotentialField.load(fieldpath))
    # 2. Registered shell metrics, including collars.
    rows=[]
    for row in reg['rows']:
        if row['shell_index']=='origin':continue
        e=row['metrics']['equations']
        rows.append(dict(shell=row['shell_index'],set=row['set'],radius_over_a_eff=np.sqrt(row['lower']*row['upper'])/aeff,
            q=e['q']['rho'],eta=e['eta']['rho'],momentum=max(e[k]['rho'] for k in ['M_r','M_theta','M_z'])))
    table('registered_shells',rows);fig,axs=plt.subplots(1,3,figsize=(10.3,3.7),sharey=True)
    for aa,key,title in zip(axs,['q','eta','momentum'],['q equation','eta equation','Primitive momentum']):
        for name,label,style in [('shell_gauss','Volume Gauss','o-'),('shell_random','Volume random','s:'),('collar_gauss','Axis collar','^--')]:
            rr=sorted([r for r in rows if r['set']==name],key=lambda r:r['radius_over_a_eff'])
            aa.loglog([r['radius_over_a_eff'] for r in rr],[max(r[key],1e-17) for r in rr],style,markersize=3,label=label)
        aa.axhline(1e-6,color='black',ls=':',lw=1,label='A1 threshold');aa.set_xlabel('Shell midpoint / a_eff');aa.set_title(title)
    axs[0].set_ylabel('Registered shell RMS ratio rho');axs[-1].legend(fontsize=8)
    fig.suptitle('Source-compatible S1, c_l=0.74, K=2, L0')
    save(fig,'registered_radius','All 18 dyadic shells. Each momentum component uses the vector denominator.')
    # 3. Actual basis order, no claim of orthogonal spectral energy.
    rows=[];fig,axs=plt.subplots(1,2,figsize=(8.2,3.7))
    for d in series:
        for aa,key in zip(axs,['phi','q']):
            terms=d['coeff'][key]['terms'];values=[abs(t[0]) for t in terms]
            aa.semilogy(np.arange(len(values)),np.maximum(values,1e-18),'.-',label='L'+str(d['level']),markersize=3)
            rows.extend(dict(level=d['level'],field=key,index=i,coefficient=t[0],i_power=t[1],j_power=t[2],beta=t[3]) for i,t in enumerate(terms))
            aa.set_title(key+' coefficients');aa.set_xlabel('Saved basis index');aa.set_ylabel('Absolute coefficient');aa.legend()
    table('coefficients',rows);fig.suptitle('Source-compatible S1, c_l=0.74, K=2');save(fig,'coefficient_size','Nonorthogonal power-envelope basis: these are not energy spectra.')
    # 4. Sample the saved field after one verified dilation.
    raxis=np.linspace(0,4*aeff,97);zaxis=np.linspace(-4*aeff,4*aeff,161);r,z=np.meshgrid(raxis,zaxis)
    data=field.cylindrical(r,z,1);U=data['U'];up=np.hypot(U[...,0],U[...,2]);np.savez_compressed(out/'field_distribution.npz',r=r,z=z,U=U,a_eff=np.array(aeff))
    fig,axs=plt.subplots(1,2,figsize=(7.8,5.4));limit=float(np.max(abs(U[...,1])))
    im=axs[0].pcolormesh(r/aeff,z/aeff,U[...,1],shading='auto',cmap='RdBu_r',vmin=-limit,vmax=limit);fig.colorbar(im,ax=axs[0],label='U_theta')
    im=axs[1].pcolormesh(r/aeff,z/aeff,up,shading='auto',cmap='viridis');fig.colorbar(im,ax=axs[1],label='Poloidal speed')
    ss=(slice(None,None,16),slice(None,None,12));axs[1].quiver((r/aeff)[ss],(z/aeff)[ss],U[...,0][ss],U[...,2][ss],color='white',width=.005)
    for aa,title in zip(axs,['Swirl velocity','Poloidal velocity']):aa.set_xlabel('r / a_eff');aa.set_ylabel('z / a_eff');aa.set_title(title);aa.set_aspect('equal')
    save(fig,'field_distribution','c_l=0.74, K=2, L0. Reporting gauge: integral |F|^2 dS=1.')
    # 5. Keep a parameter scan distinct from continuation.
    rows=[]
    for p in sorted((ROOT/'exploration/sweep1').glob('c*_q2_trf/summary.json')):
        s=read(p);c=read(p.with_name('configuration.json'));rows.append(dict(c_l=c['c_l'],objective=s['holdout']['objective_squared'],q_max=s['holdout']['raw_q_max'],eta_max=s['holdout']['raw_eta_max']))
    table('fixed_c_l_scan',rows);fig,axs=plt.subplots(1,2,figsize=(8.2,3.7))
    axs[0].semilogy([r['c_l'] for r in rows],[r['objective'] for r in rows],'o-');axs[0].set_ylabel('Custom holdout objective squared')
    for key,label in [('q_max','q equation'),('eta_max','eta equation')]:axs[1].semilogy([r['c_l'] for r in rows],[r[key] for r in rows],'o-',label=label)
    for aa in axs:aa.set_xlabel('Fixed c_l')
    axs[1].set_ylabel('Raw maximum residual');axs[1].legend();fig.suptitle('Fixed-c_l S1 scan, K=2, one basis')
    save(fig,'fixed_c_l_scan','These independent fixed-c_l fits are not free-c_l continuation.')
    # 6. Leading-tail convergence versus first nonlinear correction.
    mu,w=roots_legendre(80);radii=aeff*2.**np.arange(0,12);tail=tail_audit(field,radii,mu,w)
    (out/'tail_data.json').write_text(json.dumps(tail,indent=2)+'\n');rows=tail['rows'];fig,axs=plt.subplots(1,2,figsize=(8.2,3.7))
    axs[0].loglog(radii/aeff,[x['scaled_velocity_error_l2']/x['leading_velocity_l2'] for x in rows],'o-');axs[0].set_ylabel('Relative leading-tail error')
    axs[1].loglog(radii/aeff,[x['first_correction_error_l2'] for x in rows],'o-');axs[1].set_ylabel('Scaled first-correction L2 error')
    for aa in axs:aa.set_xlabel('R / a_eff')
    fig.suptitle('Source-compatible S1, c_l=0.74, K=2, L0')
    save(fig,'far_field','G is calculated from F and full angular compatibility, not fitted to the discrepancy.')
    # 7. The residual-source identity is not the unforced Euler identity.
    balance=read(ROOT/'results/external/S1_pilot_L0/balance_audit.json');rows=balance['rows'];fig,axs=plt.subplots(1,2,figsize=(8.2,3.7))
    table('energy_balance',[dict(resolution=r['label'],R_over_a_eff=r['radius_over_a_eff'],energy_defect=r['energy_defect'],corrected_closure_error=r['energy_corrected_error']) for r in rows])
    for name,style in [('medium','o--'),('fine','s-')]:
        rr=[r for r in rows if r['label']==name]
        axs[0].loglog([r['radius_over_a_eff'] for r in rr],[abs(r['energy_defect']) for r in rr],style,label=name)
        axs[1].loglog([r['radius_over_a_eff'] for r in rr],[max(abs(r['energy_corrected_error']),1e-18) for r in rr],style,label=name)
    for aa in axs:aa.set_xlabel('R / a_eff');aa.legend()
    axs[0].set_ylabel('Raw energy-flux defect');axs[1].set_ylabel('Residual/interface-corrected closure')
    save(fig,'energy_flux','External Chebyshev pilot. Original working coordinates; raw and corrected defects differ.')
    # 8. Analytic axis limits and independently integrated origin-ball metrics.
    zz=np.r_[np.linspace(-4,-.05,180),np.linspace(-.05,.05,161),np.linspace(.05,4,180)]*aeff;red=field.reduced(np.zeros_like(zz),zz)
    table('axis_residuals',[dict(z_over_a_eff=float(zv/aeff),q_residual=float(qv),eta_residual=float(ev)) for zv,qv,ev in zip(zz,red['q'],red['eta'])])
    origin=[dict(set=r['set'],q_rho=r['metrics']['equations']['q']['rho'],eta_rho=r['metrics']['equations']['eta']['rho']) for r in reg['rows'] if r['shell_index']=='origin'];table('origin_ball',origin)
    fig,axs=plt.subplots(1,3,figsize=(10.5,3.7))
    for aa,limit in zip(axs[:2],[4,.05]):
        keep=abs(zz/aeff)<=limit
        aa.plot(zz[keep]/aeff,red['q'][keep],label='q equation');aa.plot(zz[keep]/aeff,red['eta'][keep],ls='--',label='eta equation')
        aa.set_xlabel('z / a_eff, r=0');aa.set_ylabel('Raw axis residual');aa.legend(fontsize=8)
    labels=[r['set'].replace('shell_','').replace('collar_','collar ') for r in origin];x=np.arange(len(origin))
    axs[2].bar(x-.18,[max(r['q_rho'],1e-20) for r in origin],width=.36,label='q');axs[2].bar(x+.18,[max(r['eta_rho'],1e-20) for r in origin],width=.36,label='eta')
    axs[2].set_yscale('log');axs[2].set_xticks(x,labels,rotation=25);axs[2].set_ylabel('Origin-ball registered rho');axs[2].axhline(1e-6,color='black',ls=':');axs[2].legend()
    fig.suptitle('Source-compatible S1, c_l=0.74, K=2, L0')
    save(fig,'axis_origin','Regular axis limits are evaluated analytically. A pinned jet does not control nearby points.')
    source_paths=[Path(__file__),ROOT/'src/independent_fields.py',ROOT/'src/independent_geometry.py',ROOT/'src/independent_tail_audit.py',ROOT/'src/independent_farfield.py']
    metadata=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),wall_seconds=time.perf_counter()-started,cpu_seconds=time.process_time()-cpu,
        input_sha256=inputs,source_sha256={str(p.relative_to(LANE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths},figures=figures,
        open_deliverables=['Free-c_l runs are recorded separately; this bundle contains fixed-c_l scans only.','Independent human or lead review of the plots is pending.'])
    (out/'manifest.json').write_text(json.dumps(metadata,indent=2)+'\n');print(json.dumps(dict(output=str(out),figures=len(figures),wall_seconds=metadata['wall_seconds'])))
if __name__=='__main__':main()
