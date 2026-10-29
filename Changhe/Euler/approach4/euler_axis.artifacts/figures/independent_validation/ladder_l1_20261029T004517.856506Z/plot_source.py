#!/usr/bin/env python3
"""Offline figures from immutable ladder exports and independent audit records."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,csv,hashlib,json,time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from piecewise_loading import load_piecewise
ROOT=Path(__file__).resolve().parent
LANE=ROOT.parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--level',type=int,choices=[1,2],default=1);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(LANE) or out.exists():raise ValueError('fresh output in verifier lane required')
    out.mkdir(parents=True);start=time.perf_counter();cpu=time.process_time();inputs={};figures=[]
    def track(path):
        path=Path(path).resolve();inputs[str(path.relative_to(LANE))]=hashlib.sha256(path.read_bytes()).hexdigest();return path
    def read(path):return json.loads(track(path).read_text())
    def table(name,rows):
        with (out/(name+'.csv')).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    def save(fig,name,caption):
        fig.tight_layout(rect=(0,0.045,1,1));fig.text(.015,.008,'Numerical approximation; independent acceptance failed.',fontsize=9)
        for suffix in ['png','pdf','svg']:fig.savefig(out/f'{name}.{suffix}',dpi=160)
        plt.close(fig);figures.append({'name':name,'caption':caption})
    driver=ROOT/f'results/driver_t1_ladder_l{a.level}';reg=read(driver/'registered/summary.json');tail=read(driver/'tail.json');interface=read(driver/'registered/interfaces.json')
    coefficient=track(Path(reg['candidate_path']));assert inputs[str(coefficient.relative_to(LANE))]==reg['candidate_sha256']==tail['input_sha256']
    field,gauge=load_piecewise(coefficient).reporting_gauge();aeff=float(reg['a_eff']);assert abs(gauge['dilation_L']/reg['gauge']['dilation_L']-1)<1e-14
    track(Path(__file__))
    for name in ['piecewise_loading.py','piecewise_jacobi.py','piecewise_adapter.py','independent_fields.py']:track(ROOT/'src'/name)
    title=f'T1 ladder L{a.level}, c_l={field.c_l:.3f}'
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.2})
    styles=[('shell_gauss','Volume Gauss','o-'),('shell_random','Volume random','s:'),('collar_gauss','Axis collar','^--')]
    rows=[]
    for row in reg['rows']:
        e=row['metrics']['equations'];rows.append(dict(shell=str(row['shell_index']),set=row['set'],radius_over_a_eff=np.sqrt(row['lower']*row['upper'])/aeff,
         q=e['q']['rho'],eta=e['eta']['rho'],momentum=max(e[k]['rho'] for k in ['M_r','M_theta','M_z']),M_r=e['M_r']['rho'],M_theta=e['M_theta']['rho'],M_z=e['M_z']['rho']))
    table('registered_radius',rows);fig,axs=plt.subplots(1,3,figsize=(10.8,3.8),sharey=True)
    for ax,key,label in zip(axs,['q','eta','momentum'],['q equation','eta equation','Largest primitive component']):
        for name,lab,style in styles:
            rr=[r for r in rows if r['set']==name and r['shell']!='origin'];ax.loglog([r['radius_over_a_eff'] for r in rr],[r[key] for r in rr],style,label=lab,ms=3)
        ax.axhline(1e-6,color='k',ls=':',lw=1,label='A1 threshold');ax.set_title(label);ax.set_xlabel('Shell midpoint / a_eff')
    axs[0].set_ylabel('Registered RMS ratio rho');axs[-1].legend(fontsize=8);fig.suptitle(title)
    save(fig,'registered_radius','All 18 dyadic shells, with origin excluded here. Momentum is the maximum of the three component ratios at each displayed set, not the auxiliary vector ratio.')
    # Coefficient envelopes stay in the native documented basis.
    coeffrows=[];fig,axs=plt.subplots(2,3,figsize=(10.5,6.1))
    for i in range(3):
        for j,key in enumerate(['phi','q']):
            C=field.matrices[i,key];values=np.max(abs(C),axis=1);ax=axs[j,i]
            ax.semilogy(np.arange(len(values)),np.maximum(values,1e-20),'o-',ms=3);ax.set_title(f'{key}: {field.elements[i]["kind"]}');ax.set_xlabel('Legendre degree n');ax.set_ylabel('Max |native coefficient|')
            coeffrows.extend(dict(field=key,element=i,angular_degree=n,envelope=float(v)) for n,v in enumerate(values))
    table('angular_coefficients',coeffrows);fig.suptitle(title+'; angular coefficient envelopes')
    save(fig,'angular_coefficients','The envelope is max over radial columns in the saved native basis. Element normalizations differ. This is not a physical energy spectrum.')
    radrows=[];fig,axs=plt.subplots(2,2,figsize=(8.5,6.1))
    for i in range(2):
        for j,key in enumerate(['phi','q']):
            C=field.matrices[i,key];values=np.max(abs(C),axis=0);ax=axs[j,i];ks=field.radial_keys[i,key]
            ax.semilogy(ks,np.maximum(values,1e-20),'o-',ms=3);ax.set_title(f'{key}: {field.elements[i]["kind"]}');ax.set_xlabel('Radial polynomial index k');ax.set_ylabel('Max |native coefficient|')
            radrows.extend(dict(field=key,element=i,radial_index=k,envelope=float(v)) for k,v in zip(ks,values))
    table('radial_coefficients',radrows);fig.suptitle(title+'; radial coefficient envelopes')
    save(fig,'radial_coefficients','Ball radial indices depend on angular degree through the total-degree cutoff. The exterior has distinct powers, not a polynomial-degree ladder, and is omitted.')
    # Fresh values only for visualization; no optimizer sees these samples.
    r,z=np.meshgrid(np.linspace(0,4*aeff,81),np.linspace(-4*aeff,4*aeff,145));d=field.cylindrical(r,z,1);U=d['U'];up=np.hypot(U[...,0],U[...,2])
    np.savez_compressed(out/'field_samples.npz',r=r,z=z,U=U,a_eff=aeff)
    fig,axs=plt.subplots(1,2,figsize=(8.4,5.2));lim=float(np.max(abs(U[...,1])))
    im=axs[0].pcolormesh(r/aeff,z/aeff,U[...,1],shading='auto',cmap='RdBu_r',vmin=-lim,vmax=lim);fig.colorbar(im,ax=axs[0],label='Swirl velocity U_theta')
    im=axs[1].pcolormesh(r/aeff,z/aeff,up,shading='auto',cmap='viridis');fig.colorbar(im,ax=axs[1],label='Poloidal speed')
    angles=np.linspace(0,np.pi,257)
    for ax in axs:
        for radius in field.interfaces:ax.plot(radius*np.sin(angles)/aeff,radius*np.cos(angles)/aeff,'w--',lw=.8)
        ax.set(xlim=(0,4),ylim=(-4,4),aspect='equal',xlabel='r / a_eff',ylabel='z / a_eff')
    fig.suptitle(title+'; field samples in the reporting gauge')
    save(fig,'field_distribution','Independent values on an 81 x 145 meridional grid. White dashed arcs mark element interfaces; visual smoothness does not establish global regularity.')
    trows=[dict(radius_over_a_eff=row['R']/aeff,leading_error=row['leading_velocity_error']/tail['leading_sphere_norm'],first_vs_saved=row['observed_first_vs_saved_error']/tail['Euler_correction_sphere_norm'],first_vs_Euler=row['observed_first_vs_Euler_error']/tail['Euler_correction_sphere_norm']) for row in tail['rows']]
    table('far_field',trows);fig,axs=plt.subplots(1,2,figsize=(9,3.9));x=[r['radius_over_a_eff'] for r in trows]
    axs[0].loglog(x,[r['leading_error'] for r in trows],'o-');axs[0].set_ylabel('Relative leading velocity error')
    for key,label,style in [('first_vs_saved','Remainder minus saved H','o-'),('first_vs_Euler','Remainder minus Euler G','s--')]:axs[1].loglog(x,[r[key] for r in trows],style,label=label)
    axs[1].axhline(tail['correction_relative_to_Euler'],ls=':',c='k',label='Coefficient mismatch');axs[1].axhline(1e-3,ls='-.',c='gray',label='A6 threshold');axs[1].set_ylabel('Correction error / ||G||');axs[1].legend(fontsize=8)
    for ax in axs:ax.set_xlabel('Radius / a_eff')
    fig.suptitle(title+'; leading agreement leaves a wrong correction')
    save(fig,'far_field','Full-sphere L2 norms. The first remainder uses the prescribed exponent 2 alpha + 1. The horizontal mismatch comes from saved coefficients, not a fitted asymptote.')
    # Exact-axis reduced residuals use analytic regular limits and retain signs in CSV.
    az=aeff*np.unique(np.r_[np.linspace(-4,4,801),np.linspace(-.08,.08,321)]);red=field.reduced(np.zeros_like(az),az)
    axisrows=[dict(z_over_a_eff=float(zz/aeff),q_residual=float(q),eta_residual=float(e)) for zz,q,e in zip(az,red['q'],red['eta'])];table('axis',axisrows)
    fig,axs=plt.subplots(1,3,figsize=(11,3.8))
    for ax,xlim in zip(axs[:2],[(-4,4),(-.08,.08)]):
        ax.semilogy(az/aeff,np.maximum(abs(red['q']),1e-18),label='|R_q|');ax.semilogy(az/aeff,np.maximum(abs(red['eta']),1e-18),'--',label='|R_eta|');ax.set(xlim=xlim,xlabel='z / a_eff',ylabel='Absolute residual, r=0');ax.legend(fontsize=8)
    labels=['q','eta','M_r','M_theta','M_z'];xx=np.arange(len(labels))
    for shift,(name,label,_) in enumerate(styles):
        rr=next(r for r in rows if r['set']==name and r['shell']=='origin');axs[2].bar(xx+(shift-1)*.25,[rr[k] for k in labels],.24,label=label)
    axs[2].set_yscale('log');axs[2].axhline(1e-6,c='k',ls=':',label='A1 threshold');axs[2].set_xticks(xx,labels,rotation=35);axs[2].set_ylabel('Origin-region RMS ratio');axs[2].legend(fontsize=7);fig.suptitle(title+'; axis and origin diagnostics')
    save(fig,'axis_origin','The first panels are unnormalized exact-axis reduced residuals. The final panel uses the registered origin-region denominators. A low origin defect does not control the rest of the axis.')
    jumps=interface['derivative_jumps'];table('interface_jumps',jumps);radii=sorted({r['interface'] for r in jumps});fig,axs=plt.subplots(1,len(radii),figsize=(10,3.9),squeeze=False)
    for ax,radius in zip(axs[0],radii):
        rr=[r for r in jumps if r['interface']==radius];xx=np.arange(len(rr));ax.semilogy(xx,[r['relative_jump'] for r in rr],'o-',ms=4)
        ax.axhline(1e-6,c='k',ls=':',label='A8');ax.axhline(1e-3,c='gray',ls='--',label='B4');ax.set_xticks(xx,[f'{r["field"]}({r["d_R"]},{r["d_mu"]})' for r in rr],rotation=90,fontsize=7);ax.set_title(f'Interface R / a_eff = {radius/aeff:.3g}');ax.set_ylabel('Relative derivative jump');ax.legend(fontsize=8)
    fig.suptitle(title+'; global regularity fails at interfaces')
    save(fig,'interface_jumps','Labels field(d_R,d_mu) give derivative orders. Every ratio uses the largest one-sided value of that derivative as its scale. Axis regularity inside the elements cannot remove these jumps.')
    balance=ROOT/f'results/ladder_l{a.level}_balances_normalized.json'
    if balance.exists():
        b=read(balance);table('balances',b['rows']);fig,axs=plt.subplots(1,2,figsize=(8.6,3.8));x=[r['radius_over_a_eff'] for r in b['rows']]
        for ax,key in zip(axs,['energy','helicity']):
            ax.loglog(x,[r[key+'_relative_defect'] for r in b['rows']],'o-',label='Unforced identity defect');ax.loglog(x,[r[key+'_relative_corrected_error'] for r in b['rows']],'s--',label='Residual/jump-corrected error');ax.set(xlabel='Radius / a_eff',ylabel='Largest-term relative error',title=key.capitalize())
            if key=='energy':ax.axhline(1e-6,c='k',ls=':',label='A9 threshold')
            ax.legend(fontsize=8)
        fig.suptitle(title+'; Euler defect and quadrature closure')
        save(fig,'balances','Fine quadrature results normalized by the largest absolute balance term. Residual work and interface flux jumps account for the raw defect; their inclusion does not make the field an unforced solution.')
    pressure=ROOT/f'results/ladder_l{a.level}_pressure.json'
    if pressure.exists():
        p=read(pressure)
        if p['phase']=='complete':
            pts=np.asarray(p['points_r_z']);R=np.linalg.norm(pts,axis=1)/(aeff/gauge['dilation_L']);fine=np.asarray(p['direct_newton_values'][-1]['pressure']);coarse=np.asarray(p['direct_newton_values'][0]['pressure']);fig,ax=plt.subplots(figsize=(7.2,4));order=np.argsort(R);prows=[]
            for i,green in enumerate(p['green_refinements']):
                difference=abs(np.asarray(green['pressure'])-fine);ax.loglog(R[order],np.maximum(difference[order],1e-18),'o' if i else 's',label=f'Green level {i+1} vs Newton fine',ms=4)
                prows.extend(dict(point=j,radius_over_a_eff=float(R[j]),comparison=f'Green{i+1}-NewtonFine',absolute_difference=float(difference[j])) for j in range(len(R)))
            ax.loglog(R[order],np.maximum(abs(coarse-fine)[order],1e-18),'^',label='Newton coarse vs fine',ms=4);ax.set(xlabel='Point radius / a_eff',ylabel='Absolute pressure difference',title=title+'; pressure accuracy');ax.legend(fontsize=8);prows.extend(dict(point=j,radius_over_a_eff=float(R[j]),comparison='NewtonCoarse-NewtonFine',absolute_difference=float(abs(coarse[j]-fine[j]))) for j in range(len(R)));table('pressure',prows)
            save(fig,'pressure','Twenty retained points; coincident radii can have different angles. Absolute working-coordinate pressure differences do not by themselves give the shell-relative A7 criterion.')
    for path,h in inputs.items():
        if hashlib.sha256((LANE/path).read_bytes()).hexdigest()!=h:raise RuntimeError('input changed: '+path)
    record=dict(created_utc=datetime.now(timezone.utc).isoformat(),level=a.level,candidate_sha256=reg['candidate_sha256'],c_l=field.c_l,a_eff=aeff,inputs_sha256=inputs,figures=figures,wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,scope='Offline figures of a rejected frozen approximation; no new acceptance test or continuous error certificate.')
    (out/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
    (out/'CAPTIONS.md').write_text('# Frozen ladder diagnostic figures\n\n'+'\n\n'.join(f'## {r["name"]}\n\n{r["caption"]}\n\n![{r["name"]}]({r["name"]}.png)' for r in figures)+'\n')
    print(json.dumps({k:record[k] for k in ['created_utc','candidate_sha256','wall_seconds','cpu_seconds']}));print('figures',len(figures))
if __name__=='__main__':main()
