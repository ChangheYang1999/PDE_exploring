import json,sys,glob
for f in sorted(glob.glob('notes/sens_s56_v6/*.json')):
    d=json.load(open(f)); r=d['reduced']['1e-12']; e=d['eta']; m=d['record_meta']['params_record']
    w=r['widths']['0.01']
    print(f.split('/')[-1][:30], 'n',d['n'],'rank',r['coef_rank_kept'],'O1 %.4e'%d['O1'], 'p (%.6f, %.6f)'%(m['c_l'],m['omega']))
    print('  eta0 %.3f eta1e-8 %.3f eta1e-10 %.3f'%(e['0'],e['1e-08'],e['1e-10']), 'grad',['%.2g'%x for x in d['scaled_param_grad']],
      'abs',['%.2g'%x for x in r['absorption_cos_columns']],'condS %.2g'%r['cond_S'],'corr %.2f'%r['corr_cl_omega'],
      'step',['%.3f'%x for x in r['reduced_GN_step_physical']],'pred %.3f'%r['reduced_predicted_rel_decrease'],'minimizer',['%.4f'%x for x in r['model_minimizer_physical']])
    print('  colscale dev %.2g'%d['record_column_scaling_deviation'], 'sigma_max %.4g'%d['sigma_max'])
    for ww in w: print('   width', {k:(v if not isinstance(v,float) else round(v,5)) for k,v in ww.items() if k not in ('eigvec_scaled',)})
    r8=d['reduced']['1e-08']; print('  cutoff1e-8 pred %.4f abs %s'%(r8['reduced_predicted_rel_decrease'],['%.2g'%x for x in r8['absorption_cos_columns']]))
