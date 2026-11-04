from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import ast,json,os,time
D=Path(__file__).resolve().parents[1];R=D.parents[1];AT=R.parent/'theory_audit'
assert os.sched_getaffinity(0)=={50} and os.getpriority(os.PRIO_PROCESS,0)>=19
assert all(os.environ.get(k)=='1'for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'])
start=datetime.now(timezone.utc);tick=time.monotonic();checks=[];bindings={}
def ck(x,n):
    assert x,n
    checks.append(n)
def bind(p,h=None):
    p=Path(p);data=p.read_bytes();z=sha256(data).hexdigest();n=os.path.relpath(p,R)
    ck(h is None or z==h,'identity '+n);bindings[n]=z;return data
def load(p,h=None):return json.loads(bind(p,h))
def defs(p):return {x.name:ast.dump(x,include_attributes=False)for x in ast.parse(p.read_text()).body if isinstance(x,(ast.FunctionDef,ast.ClassDef))}
prep=load(D/'verification/prepared_v01.json')
for p,h in prep['files'].items():bind(R/p,h)
old=load(D/'source/inputs_v06.json');oldout=load(D/'source/closure_check_v06.json')
current=[];input_records=[]
for v,topic,h in [('07','near_tuple_actual_audit','e8fe1c3b3c9c31728863da6ca74f747dd2e69410ab96fef68bfe63d6e12e38c5'),('08','near_direct_tuple_audit','bfe7538d85c632d5ecc9723d7f4b7c4744179ddd44146e2513523c9ffa85f220')]:
    I=load(D/f'source/inputs_v{v}.json');O=load(D/f'source/closure_check_v{v}.json');input_records.append(I)
    nc=load(R/'research'/topic/'verification/check_v01.json',h)
    for field in ['own_bindings','external_dependencies']:
        for p,z in nc[field].items():bind(R/p,z)
    ck(O['inputs_sha256']==sha256((D/f'source/inputs_v{v}.json').read_bytes()).hexdigest(),'input hash '+v)
    ck(O['program_sha256']==sha256((D/f'source/closure_check_v{v}.py').read_bytes()).hexdigest(),'program hash '+v)
    ck(defs(D/f'source/closure_check_v{v}.py')==defs(D/'source/closure_check_v06.py'),'mathematical functions unchanged '+v)
    for group in ['conventions','fixed','source','background','far_Fa','kb','rest','ce','cases','h4_reading']:ck(I[group]==old[group],group+' unchanged '+v)
    for k,x in I['near'].items():
        if k not in ['D4_an','D5_an','D6_an']:ck(x==old['near'][k],'unchanged near '+k+v)
        else:ck(x['status']=='CONFIRMED','actual derivative '+k+v)
    V={k:Q(x['value'])for g in ['fixed','source','background','far_Fa','kb','near','rest','ce']for k,x in I[g].items()if isinstance(x,dict)and'value'in x}
    ck(V['eps_rest']==V['C_rest']==0,'zero placeholders '+v)
    ck(I['rest']['eps_rest']['status']==I['rest']['C_rest']['status']=='STANDIN-ZERO','placeholder labels '+v)
    ck(V['beta0']-V['g_star']>=V['beta0_star']==Q(7,4),'conservative beta0star '+v)
    rad=V['f']/V['beta0_star'];cap=V['c']+1-V['q'];far=V['q']*(V['c']-V['s_star'])-max(V['SC_plus'],V['AE_plus'])-V['SW_plus']-V['OMF_plus']
    ck(Q(O['common']['cap'])==cap,'exact cap '+v);ck(Q(O['common']['far_margin'])==far>0,'exact far margin '+v)
    ck(Q(O['common']['R_star_upper'])>=rad,'radius outward '+v);ck(O['common']==oldout['common'],'same background union '+v)
    rows={x['name']:x for x in O['results']}
    ck(O['verdict']=='CLOSURE OPEN'and O['h4_reading']=='ii','open verdict '+v)
    ck(rows['N4']['status']=='PASS'and rows['N4']['value']=='differ: none','same near inputs '+v)
    expected_open={'H-RC','H1','H2','H-BALL','H4-REST','H-N1','H-REG'}
    ck({k for k,x in rows.items()if x['block']=='H'and x['status']=='OPEN'}==expected_open,'open hypotheses '+v)
    ck(rows['H-NEARU']['status']=='supplied','near numerical component supplied '+v)
    ck('not needed for (a), (b)'in rows['H-REG']['note'],'stronger-only regularity '+v)
    for a in nc['cases']:
        label=a['label'];o=O['cases'][label];previous=oldout['cases'][label];ci=next(x for x in I['cases']if x['label']==label)
        b=Q(o['b0']);e=Q(o['e_up']);price=Q(o['C0']);allow=Q(o['D_out']);rate=V['beta_star']-b-e;room=allow-price
        ck(e==Q(a['e_up']),'independent near loss '+label+v);ck(rate==Q(a['h4_rate_margin_lower']),'exact remaining rate '+label+v)
        ck(Q(o['margin_ii'])<=rate and Q(o['margin_i'])<=cap-b-e,'directed margin displays '+label+v)
        ck(Q(o['beta_star_needed_ii_exact'])==b+e<=Q(o['beta_star_needed_ii']),'beta threshold displays '+label+v)
        ck(price==Q(a['C_N_upper'])+V['C_rest'],'same near price '+label+v)
        k0,k2,kj=(Q(ci[k]['value'])for k in ['kappa_0','kappa_2q','kappa_j'])
        raw=2*(max(V['sup_abs_an_W2'],V['sup_pos_an_W2'])*k0*k2+2*V['sup_pos_an_W2']*kj**2/(1-V['t']))
        ck(raw<=price<raw+1,'independent rational price '+label+v)
        for k in ['C0','D_out','Z','C0_over_D_out','room','M','B','A','Kbar','loss','bprime']:ck(o[k]==previous[k],'unchanged CE '+k+label+v)
        M=Q(o['M']);loss=Q(o['loss']);Z=M*((b-loss)*M-V['n'])
        ck(price*rad**2<=Z,'conservative CE inequality '+label+v)
        ck(Q(o['room'])<=room and Q(o['C0_over_D_out'])>=price/allow,'price room and ratio directed '+label+v)
        ck(room==(Q(9941475955)if b==Q(11,20)else Q(47277952671,5)),'exact room '+label+v)
        ck(Q(o['bprime'])<=b-loss,'bprime lower '+label+v)
        for prefix in ['A3','E0','N2','N3','G1','G2','G3']:ck(rows[prefix+o['tag']]['status']=='PASS','status '+prefix+label+v)
        for prefix in ['E1','E2','F1','G4','G5','J1']:ck(rows[prefix+o['tag']]['status']=='PASS-COND','conditional status '+prefix+label+v)
        co=o['companion_ii'];cb=Q(co['b0']);ck(cb*100==(100*(V['beta_star']-e)).numerator//(100*(V['beta_star']-e)).denominator,'companion grid '+label+v)
        ck(Q(co['E2_margin'])<=V['beta_star']-cb-e,'companion separate rate '+label+v)
        current.append({'closure_version':v,'label':label,'b':str(b),'e':str(e),'remaining_rate':str(rate),'price':str(price),'allowance':str(allow),'exact_price_room':str(room),'CE_conservative_slack':str(Z-price*rad**2)})
ck({k:x for k,x in input_records[0].items()if k not in ['title','near_binding']}=={k:x for k,x in input_records[1].items()if k not in ['title','near_binding']},'v07-v08 identical numerical inputs')
A=AT/'research/closure_v07_v08_audit';a=load(A/'verification/actual_review_v01.json','3a4b279e56f616bdcb3f5caf502a7aa4ef7fa9f78aedf1c5f84f85f779a4ac28');ck(a['status']=='BOUND','actual AT review')
for p,h in a['bindings'].items():bind(AT/p,h)
c=load(A/'verification/check_v01.json','5bc48c04a2bb289122ea3da8c8ce254a7d6a7aa707a68d5d28d89e10bdeee405');ck(c['status']=='PASS'and c['checks']==543,'AT complete check')
for p,h in c['files'].items():bind(AT/p,h)
ex=load(AT/'runs/closure_v07_v08_v02/execution_v01.json');ck(ex['status']=='COMPLETED'and ex['returncode']==0 and ex['cpu']==40 and ex['nice']==19 and ex['threads']==1,'AT successful guard')
ck(datetime.fromisoformat(ex['started_utc'])<=datetime.fromisoformat(c['started_utc'])<=datetime.fromisoformat(c['finished_utc'])<=datetime.fromisoformat(ex['finished_utc']),'AT time containment')
for x,row in zip([case for ver in c['versions']for case in ver['cases']],current):
    for key,ours in [('rate','remaining_rate'),('near_loss','e'),('price','price'),('allowance','allowance'),('exact_price_room','exact_price_room')]:ck(Q(x[key])==Q(row[ours]),'distinct review agreement '+key+row['label']+row['closure_version'])
bind(R/'research/near_tuple_review_adoption/verification/actual_review_v01.json','d41d641a19b6905b921769a100e8845cffa5378cfc0b3c8d4f8332cfdb7423dd')
for p in [D/'PROOF.md',D/'formal/README.md',Path(__file__)]:bind(p)
result={'status':'CONFIRMED_CONDITIONAL_CURRENT_CLOSURE_ARITHMETIC','started_utc':start.isoformat(),'finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'checks':len(checks),'binding_count':len(bindings),'cases':current,'bindings':bindings,'AT_actual_review_sha256':'3a4b279e56f616bdcb3f5caf502a7aa4ef7fa9f78aedf1c5f84f85f779a4ac28','scope':'Own rational integration check and adoption of distinct complete AT review. Prior CE theorem and witness retained, not recomputed; prior recursive maps authenticated rather than traversed. Full closure, analytic near and H4 rest remain open; fallback kernels unaudited. Old HI displays keep old rates.'}
p=D/'verification/check_v01.json'
with p.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
print(result['status'],result['checks'],result['binding_count'],result['elapsed_seconds'],sha256(p.read_bytes()).hexdigest())
