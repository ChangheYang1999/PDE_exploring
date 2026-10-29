#!/usr/bin/env python3
"""Offline plots with explicit distinction between iteration and continuation."""
from pathlib import Path
import csv,datetime,hashlib,json,time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent;LANE=ROOT.parent

def main():
    start=time.perf_counter();cpu=time.process_time();stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=LANE/'figures'/('free_tail_'+stamp);out.mkdir();inputs={};panels=[]
    def load(p):inputs[str(p.relative_to(LANE))]=hashlib.sha256(p.read_bytes()).hexdigest();return json.loads(p.read_text())
    def history(p):inputs[str(p.relative_to(LANE))]=hashlib.sha256(p.read_bytes()).hexdigest();return [json.loads(x) for x in p.read_text().splitlines()]
    def save(fig,name,caption):
        fig.text(.01,.012,caption,fontsize=8);fig.tight_layout(rect=(0,.07,1,1))
        for ext in ['png','pdf','svg']:fig.savefig(out/(name+'.'+ext),dpi=170)
        plt.close(fig);panels.append(dict(name=name,caption=caption))
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.2})
    dirs=[ROOT/'exploration/free_c_pilot',ROOT/'exploration/free_c_sweep1/c060_K2_zero_seed_L1',ROOT/'exploration/free_c_sweep1/c060_K2_zero_seed_L2']
    fig,ax=plt.subplots(1,3,figsize=(11.8,3.8));table=[]
    for i,d in enumerate(dirs):
        s=load(d/'summary.json');h=history(d/'iterations.jsonl');label='L'+str(i)
        ax[0].plot([x['evaluation'] for x in h],[x['c_l'] for x in h],'.-',label=label)
        ax[1].semilogy([x['evaluation'] for x in h],[x['objective_squared'] for x in h],'.-',label=label)
        table.extend(dict(level=i,**x) for x in h)
    ax[0].axhline(.7495,color='black',ls=':',label='Imposed upper bound');ax[0].set_ylabel('c_l');ax[0].legend(fontsize=8)
    ax[1].set_ylabel('Training objective squared');ax[1].legend(fontsize=8)
    for a in ax[:2]:a.set_xlabel('Function evaluation (improvements only)')
    ss=[load(d/'summary.json') for d in dirs]
    for key,label,style in [('objective_squared','Holdout objective squared','o-'),('raw_q_max','Raw q maximum','s--'),('raw_eta_max','Raw eta maximum','^:')]:
        ax[2].semilogy(range(3),[s['holdout'][key] for s in ss],style,label=label)
    ax[2].set_xticks(range(3),['L0','L1','L2']);ax[2].set_xlabel('Resolution');ax[2].set_ylabel('Separate holdout diagnostics');ax[2].legend(fontsize=8)
    fig.suptitle('Free-c_l S1 source-Green optimization, K=2')
    save(fig,'free_c_l_paths','Failed approximations. These are optimization paths, not a continuation of Euler profiles. L2 reached its evaluation cap.')
    with (out/'iteration_data.json').open('w') as f:json.dump(table,f,indent=2);f.write('\n')
    d=load(ROOT/'results/tail_audits/20261028T214154.656695Z/S1_L0.json');r=d['rows'];scale=d['radial_scale'];x=np.array([a['R']/scale for a in r])
    fig,ax=plt.subplots(1,2,figsize=(9,3.8));ax[0].loglog(x,[a['leading_velocity_error'] for a in r],'o-');ax[0].set_ylabel('Full-sphere leading error (||F||=1)')
    ax[1].loglog(x,[a['observed_first_vs_saved_error'] for a in r],'s--',label='Remainder minus saved H')
    ax[1].loglog(x,[a['observed_first_vs_Euler_error'] for a in r],'o-',label='Remainder minus Euler G')
    ax[1].axhline(d['correction_mismatch_sphere_norm'],color='black',ls=':',label='Exact coefficient norm ||H-G||')
    ax[1].set_ylabel('Full-sphere L2 norm');ax[1].legend(fontsize=8)
    for a in ax:a.set_xlabel('R / reporting-envelope length')
    fig.suptitle('First nonlinear tail correction: S1 c_l=0.74, K=2, L0')
    save(fig,'full_sphere_tail','All norms include 2 pi from azimuthal integration. H is stored; G is forced by F and full-space pressure. Acceptance failed.')
    (out/'tail_data.json').write_text(json.dumps(d,indent=2)+'\n')
    record=dict(created_utc=stamp,completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,input_sha256=inputs,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),figures=panels)
    (out/'manifest.json').write_text(json.dumps(record,indent=2)+'\n');print(str(out))
if __name__=='__main__':main()
