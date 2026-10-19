# Compare the outputs of the peak-memory runs (scratch/rss) with the stored audit files: max relative difference over
# all numeric leaves of each JSON pair, string leaves compared for equality (paths and times skipped).
import json, sys, math
V='..'; D=V+'/scratch/rss'; A=V+'/runs/audit'
LA='artifacts'
pairs=[(D+'/d_evaluator/runs/audit/rssa_N11250_q384_R7.652e6.json', A+'/c6g_N11250_q384_R7.652e6.json'),
       (D+'/d_evaluator/runs/audit/rssb_N16875_q768_R7.652e6.json', A+'/c6g_N16875_q768_R7.652e6.json'),
       (D+'/d_evaluator/runs/audit/rssc_N22500_q512_R7.652e6.json', A+'/c6g_N22500_q512_R7.652e6.json'),
       (D+'/d_evaluator/runs/audit/rsse_N16875_q512_R7.652e6.json', A+'/c6g_N16875_q512_R7.652e6.json'),
       (D+'/d_evaluator/runs/audit/rssf_N22500_q384_R7.652e6.json', A+'/c6g_N22500_q384_R7.652e6.json'),
       (D+'/d_evaluator/runs/audit/rssj_ax.json', A+'/c6g_N16875_q384_R7.652e6_ax.json'),
       (D+'/d_evaluator/runs/audit/rssj_jd2.json', A+'/c6g_N16875_q384_R7.652e6_jd2.json'),
       (D+'/d_evaluator/runs/audit/rssx_zeros.json', A+'/c6g_zeros.json'),
       (D+'/b_fit/out.json', LA+'/c_diagnostics/c6g_scan.json'),
       (D+'/b_fit/out960.json', LA+'/c_diagnostics/c6g_scan960.json')]
SKIP={'file','path','time','date','tag','wall','label'}
def walk(a,b,k,acc):
    if isinstance(a,dict) and isinstance(b,dict):
        for key in set(a)|set(b):
            if key in SKIP or key.startswith('t_'): continue
            if key not in a or key not in b: acc['missing'].append(k+'/'+key); continue
            walk(a[key],b[key],k+'/'+key,acc)
    elif isinstance(a,list) and isinstance(b,list):
        if len(a)!=len(b): acc['missing'].append(k+' len %d %d'%(len(a),len(b))); return
        for i,(x,y) in enumerate(zip(a,b)): walk(x,y,k+'[%d]'%i,acc)
    elif isinstance(a,(int,float)) and isinstance(b,(int,float)) and not isinstance(a,bool):
        acc['n']+=1
        if a!=b:
            d=abs(a-b)/max(abs(a),abs(b),1e-300)
            if d>acc['rel']: acc['rel']=d; acc['at']=k
    else:
        acc['n']+=1
        if a!=b: acc['strdiff'].append(k)
for p,q in pairs:
    try: a=json.load(open(p)); b=json.load(open(q))
    except Exception as e: print('SKIP', p.split('/')[-1], q.split('/')[-1], type(e).__name__, e); continue
    acc={'n':0,'rel':0.0,'at':'','missing':[],'strdiff':[]}
    walk(a,b,'',acc)
    print(p.split('/')[-1], 'vs', q.split('/')[-1], 'leaves', acc['n'], 'max rel diff %.3e'%acc['rel'], acc['at'],
          'missing', acc['missing'][:5], 'strdiff', acc['strdiff'][:5])
